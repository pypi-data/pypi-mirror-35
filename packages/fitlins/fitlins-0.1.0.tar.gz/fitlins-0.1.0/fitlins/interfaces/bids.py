import os
from functools import reduce
from pathlib import Path
from gzip import GzipFile
import json
import shutil
import numpy as np
import nibabel as nb

from collections import defaultdict

from nipype import logging
from nipype.utils.filemanip import makedirs, copyfile
from nipype.interfaces.base import (
    BaseInterfaceInputSpec, TraitedSpec, SimpleInterface,
    InputMultiPath, OutputMultiPath, File, Directory,
    traits, isdefined
    )
from nipype.interfaces.io import IOBase

from ..utils import dict_intersection, snake_to_camel

iflogger = logging.getLogger('nipype.interface')


def bids_split_filename(fname):
    """Split a filename into parts: path, base filename, and extension

    Respects multi-part file types used in BIDS standard and draft extensions

    Largely copied from nipype.utils.filemanip.split_filename

    Parameters
    ----------
    fname : str
        file or path name

    Returns
    -------
    pth : str
        path of fname
    fname : str
        basename of filename, without extension
    ext : str
        file extension of fname
    """
    special_extensions = [
        ".R.surf.gii", ".L.surf.gii",
        ".R.func.gii", ".L.func.gii",
        ".nii.gz", ".tsv.gz",
        ]

    pth = os.path.dirname(fname)
    fname = os.path.basename(fname)

    for special_ext in special_extensions:
        if fname.lower().endswith(special_ext.lower()):
            ext_len = len(special_ext)
            ext = fname[-ext_len:]
            fname = fname[:-ext_len]
            break
    else:
        fname, ext = os.path.splitext(fname)

    return pth, fname, ext


def _ensure_model(model):
    model = getattr(model, 'filename', model)

    if isinstance(model, str):
        if os.path.exists(model):
            with open(model) as fobj:
                model = json.load(fobj)
        else:
            model = json.loads(model)
    return model


class ModelSpecLoaderInputSpec(BaseInterfaceInputSpec):
    bids_dir = Directory(exists=True,
                         mandatory=True,
                         desc='BIDS dataset root directory')
    model = traits.Either('default', InputMultiPath(File(exists=True)),
                          desc='Model filename')
    selectors = traits.Dict(desc='Limit models to those with matching inputs')


class ModelSpecLoaderOutputSpec(TraitedSpec):
    model_spec = OutputMultiPath(traits.Dict())


class ModelSpecLoader(SimpleInterface):
    input_spec = ModelSpecLoaderInputSpec
    output_spec = ModelSpecLoaderOutputSpec

    def _run_interface(self, runtime):
        import bids
        from bids.analysis import auto_model
        models = self.inputs.model
        if not isinstance(models, list):
            layout = bids.BIDSLayout(self.inputs.bids_dir)

            if not isdefined(models):
                models = layout.get(type='model')
                if not models:
                    raise ValueError("No models found")
            elif models == 'default':
                models = auto_model(layout)

        models = [_ensure_model(m) for m in models]

        if self.inputs.selectors:
            # This is almost certainly incorrect
            models = [model for model in models
                      if all(val in model['input'].get(key, [val])
                             for key, val in self.inputs.selectors.items())]

        self._results['model_spec'] = models

        return runtime


IMPUTATION_SNIPPET = """\
<div class="warning">
    The following confounds had NaN values for the first volume: {}.
    The mean of non-zero values for the remaining entries was imputed.
    If another strategy is desired, it must be explicitly specified in
    the model.
</div>
"""


class LoadBIDSModelInputSpec(BaseInterfaceInputSpec):
    bids_dir = Directory(exists=True,
                         mandatory=True,
                         desc='BIDS dataset root directory')
    preproc_dir = Directory(exists=True,
                            desc='Optional preprocessed files directory')
    model = traits.Dict(desc='Model specification', mandatory=True)
    selectors = traits.Dict(desc='Limit collected sessions', usedefault=True)
    include_pattern = InputMultiPath(
        traits.Str, xor=['exclude_pattern'],
        desc='Patterns to select sub-directories of BIDS root')
    exclude_pattern = InputMultiPath(
        traits.Str, xor=['include_pattern'],
        desc='Patterns to ignore sub-directories of BIDS root')


class LoadBIDSModelOutputSpec(TraitedSpec):
    session_info = traits.List(traits.Dict())
    contrast_info = traits.List(traits.List(File()))
    contrast_indices = traits.List(traits.List(traits.List(traits.Dict)))
    entities = traits.List(traits.List(traits.Dict()))
    warnings = traits.List(File)


class LoadBIDSModel(SimpleInterface):
    input_spec = LoadBIDSModelInputSpec
    output_spec = LoadBIDSModelOutputSpec

    def _run_interface(self, runtime):
        import bids
        bids.config.set_options(loop_preproc=True)
        include = self.inputs.include_pattern
        exclude = self.inputs.exclude_pattern
        if not isdefined(include):
            include = None
        if not isdefined(exclude):
            exclude = None

        paths = [(self.inputs.bids_dir, 'bids')]
        if isdefined(self.inputs.preproc_dir):
            paths.append((self.inputs.preproc_dir, ['bids', 'derivatives']))
        layout = bids.BIDSLayout(paths, include=include, exclude=exclude)

        selectors = self.inputs.selectors

        analysis = bids.Analysis(model=self.inputs.model, layout=layout)
        analysis.setup(drop_na=False, **selectors)
        self._load_level1(runtime, analysis)
        self._load_higher_level(runtime, analysis)

        # Debug - remove, eventually
        runtime.analysis = analysis

        return runtime

    def _load_level1(self, runtime, analysis):
        block = analysis.blocks[0]
        block_subdir = Path(runtime.cwd) / block.level
        block_subdir.mkdir(parents=True, exist_ok=True)

        entities = []
        session_info = []
        contrast_indices = []
        contrast_info = []
        warnings = []
        for paradigm, _, ents in block.get_design_matrix(
                block.model['HRF_variables'], mode='sparse', force=True):
            info = {}

            space = analysis.layout.get_spaces(type='preproc',
                                               extensions=['.nii', '.nii.gz'])[0]
            preproc_files = analysis.layout.get(type='preproc',
                                                extensions=['.nii', '.nii.gz'],
                                                space=space,
                                                **ents)
            if len(preproc_files) != 1:
                raise ValueError('Too many BOLD files found')

            fname = preproc_files[0].filename

            # Required field in seconds
            TR = analysis.layout.get_metadata(fname, type='bold',
                                              full_search=True)['RepetitionTime']
            dense_vars = set(block.model['variables']) - set(block.model['HRF_variables'])

            _, confounds, _ = block.get_design_matrix(dense_vars,
                                                      mode='dense',
                                                      force=True,
                                                      sampling_rate=1/TR,
                                                      **ents)[0]

            ent_string = '_'.join('{}-{}'.format(key, val)
                                  for key, val in ents.items())

            events_file = block_subdir / '{}_events.h5'.format(ent_string)
            paradigm.to_hdf(events_file, key='events')

            imputed = []
            if confounds is not None:
                # Note that FMRIPREP includes CosineXX columns to accompany
                # t/aCompCor
                # We may want to add criteria to include HPF columns that are not
                # explicitly listed in the model
                names = [col for col in confounds.columns
                         if col.startswith('NonSteadyStateOutlier') or
                         col in block.model['variables']]
                confounds = confounds[names]

                # These confounds are defined pairwise with the current volume
                # and its predecessor, and thus may be undefined (have value
                # NaN) at the first volume.
                # In these cases, we impute the mean non-zero value, for the
                # expected NaN only.
                # Any other NaNs must be handled by an explicit transform in
                # the BIDS model.
                for imputable in ('FramewiseDisplacement',
                                  'stdDVARS', 'non-stdDVARS',
                                  'vx-wisestdDVARS'):
                    if imputable in confounds.columns:
                        vals = confounds[imputable].values
                        if not np.isnan(vals[0]):
                            continue

                        # Impute the mean non-zero, non-NaN value
                        confounds[imputable][0] = np.nanmean(vals[vals != 0])
                        imputed.append(imputable)

                if np.isnan(confounds.values).any():
                    iflogger.warning('Unexpected NaNs found in confounds; '
                                     'regression may fail.')

                confounds_file = block_subdir / '{}_confounds.h5'.format(ent_string)
                confounds.to_hdf(confounds_file, key='confounds')

            else:
                confounds_file = None

            info['events'] = str(events_file)
            info['confounds'] = str(confounds_file)
            info['repetition_time'] = TR

            # Transpose so each contrast gets a row of data instead of column
            contrasts, index, _ = block.get_contrasts(**ents)[0]

            contrast_type_map = defaultdict(lambda: 'T')
            contrast_type_map.update({contrast['name']: contrast['type']
                                      for contrast in block.contrasts})
            contrast_type_list = [contrast_type_map[contrast]
                                  for contrast in contrasts.columns]

            contrasts = contrasts.T
            # Add test indicator column
            contrasts['type'] = contrast_type_list

            contrasts_file = block_subdir / '{}_contrasts.h5'.format(ent_string)
            contrasts_file.parent.mkdir(parents=True, exist_ok=True)
            contrasts.to_hdf(contrasts_file, key='contrasts')

            warning_file = block_subdir / '{}_warning.html'.format(ent_string)
            with warning_file.open('w') as fobj:
                if imputed:
                    fobj.write(IMPUTATION_SNIPPET.format(', '.join(imputed)))

            entities.append(ents)
            session_info.append(info)
            contrast_indices.append(index.to_dict('records'))
            contrast_info.append(str(contrasts_file))
            warnings.append(str(warning_file))

        self._results['session_info'] = session_info
        self._results['warnings'] = warnings
        self._results.setdefault('entities', []).append(entities)
        self._results.setdefault('contrast_indices', []).append(contrast_indices)
        self._results.setdefault('contrast_info', []).append(contrast_info)

    def _load_higher_level(self, runtime, analysis):
        cwd = Path(runtime.cwd)
        for block in analysis.blocks[1:]:
            block_subdir = cwd / block.level
            block_subdir.mkdir(parents=True, exist_ok=True)

            entities = []
            contrast_indices = []
            contrast_info = []
            for contrasts, index, ents in block.get_contrasts():
                if contrasts.empty:
                    continue

                # The contrast index is the name of the input contrasts,
                # which will very frequently be non-unique
                # Hence, add the contrast to the index (table of entities)
                # and switch to a matching numeric index
                index['contrast'] = contrasts.index
                contrasts.index = index.index

                contrast_type_map = defaultdict(lambda: 'T')
                contrast_type_map.update({contrast['name']: contrast['type']
                                          for contrast in block.contrasts})
                contrast_type_list = [contrast_type_map[contrast]
                                      for contrast in contrasts.columns]

                indices = index.to_dict('records')

                # Entities for a given contrast matrix include the intersection of
                # entities of inputs, e.g., if this level is within-subject, the
                # subject should persist
                out_ents = reduce(dict_intersection, indices)
                # Explicit entities take precedence over derived
                out_ents.update(ents)
                # Input-level contrasts will be overridden by the current level
                out_ents.pop('contrast', None)

                ent_string = '_'.join('{}-{}'.format(key, val)
                                      for key, val in out_ents.items())

                # Transpose so each contrast gets a row of data instead of column
                contrasts = contrasts.T
                # Add test indicator column
                contrasts['type'] = contrast_type_list

                contrasts_file = block_subdir / '{}_contrasts.h5'.format(ent_string)
                contrasts_file.parent.mkdir(parents=True, exist_ok=True)
                contrasts.to_hdf(contrasts_file, key='contrasts')

                entities.append(out_ents)
                contrast_indices.append(indices)
                contrast_info.append(str(contrasts_file))

            self._results['entities'].append(entities)
            self._results['contrast_info'].append(contrast_info)
            self._results['contrast_indices'].append(contrast_indices)


class BIDSSelectInputSpec(BaseInterfaceInputSpec):
    bids_dir = Directory(exists=True,
                         mandatory=True,
                         desc='BIDS dataset root directories')
    preproc_dir = Directory(exists=True,
                            desc='Optional preprocessed files directory')
    entities = InputMultiPath(traits.Dict(), mandatory=True)
    selectors = traits.Dict(desc='Additional selectors to be applied',
                            usedefault=True)


class BIDSSelectOutputSpec(TraitedSpec):
    bold_files = OutputMultiPath(File)
    mask_files = OutputMultiPath(traits.Either(File, None))
    entities = OutputMultiPath(traits.Dict)


class BIDSSelect(SimpleInterface):
    input_spec = BIDSSelectInputSpec
    output_spec = BIDSSelectOutputSpec

    def _run_interface(self, runtime):
        import bids
        paths = [(self.inputs.bids_dir, 'bids')]
        if isdefined(self.inputs.preproc_dir):
            paths.append((self.inputs.preproc_dir, ['bids', 'derivatives']))
        layout = bids.BIDSLayout(paths)

        bold_files = []
        mask_files = []
        entities = []
        for ents in self.inputs.entities:
            selectors = {**self.inputs.selectors, **ents}
            bold_file = layout.get(extensions=['.nii', '.nii.gz'], **selectors)

            if len(bold_file) == 0:
                raise FileNotFoundError(
                    "Could not find BOLD file in {} with entities {}"
                    "".format(self.inputs.bids_dir, selectors))
            elif len(bold_file) > 1:
                raise ValueError(
                    "Non-unique BOLD file in {} with entities {}.\n"
                    "Matches:\n\t{}"
                    "".format(self.inputs.bids_dir, selectors,
                              "\n\t".join(
                                  '{} ({})'.format(
                                      f.filename,
                                      layout.files[f.filename].entities)
                                  for f in bold_file)))

            # Select exactly matching mask file (may be over-cautious)
            bold_ents = layout.parse_file_entities(
                bold_file[0].filename)
            bold_ents['type'] = 'brainmask'
            mask_file = layout.get(extensions=['.nii', '.nii.gz'], **bold_ents)
            bold_ents.pop('type')

            bold_files.append(bold_file[0].filename)
            mask_files.append(mask_file[0].filename if mask_file else None)
            entities.append(bold_ents)

        self._results['bold_files'] = bold_files
        self._results['mask_files'] = mask_files
        self._results['entities'] = entities

        return runtime


def _copy_or_convert(in_file, out_file):
    in_ext = bids_split_filename(in_file)[2]
    out_ext = bids_split_filename(out_file)[2]

    # Copy if filename matches
    if in_ext == out_ext:
        copyfile(in_file, out_file, copy=True, use_hardlink=True)
        return

    # gzip/gunzip if it's easy
    if in_ext == out_ext + '.gz' or in_ext + '.gz' == out_ext:
        read_open = GzipFile if in_ext.endswith('.gz') else open
        write_open = GzipFile if out_ext.endswith('.gz') else open
        with read_open(in_file, mode='rb') as in_fobj:
            with write_open(out_file, mode='wb') as out_fobj:
                shutil.copyfileobj(in_fobj, out_fobj)
        return

    # Let nibabel take a shot
    try:
        nb.save(nb.load(in_file), out_file)
    except Exception:
        pass
    else:
        return

    raise RuntimeError("Cannot convert {} to {}".format(in_ext, out_ext))


class BIDSDataSinkInputSpec(BaseInterfaceInputSpec):
    base_directory = Directory(
        mandatory=True,
        desc='Path to BIDS (or derivatives) root directory')
    in_file = InputMultiPath(File(exists=True), mandatory=True)
    entities = InputMultiPath(traits.Dict, usedefault=True,
                              desc='Per-file entities to include in filename')
    fixed_entities = traits.Dict(usedefault=True,
                                 desc='Entities to include in all filenames')
    path_patterns = InputMultiPath(
        traits.Str, desc='BIDS path patterns describing format of file names')


class BIDSDataSinkOutputSpec(TraitedSpec):
    out_file = OutputMultiPath(File, desc='output file')


class BIDSDataSink(IOBase):
    input_spec = BIDSDataSinkInputSpec
    output_spec = BIDSDataSinkOutputSpec

    _always_run = True

    def _list_outputs(self):
        import bids
        base_dir = self.inputs.base_directory

        os.makedirs(base_dir, exist_ok=True)

        layout = bids.BIDSLayout(base_dir)
        path_patterns = self.inputs.path_patterns
        if not isdefined(path_patterns):
            path_patterns = None

        out_files = []
        for entities, in_file in zip(self.inputs.entities,
                                     self.inputs.in_file):
            ents = {**self.inputs.fixed_entities}
            ents.update(entities)

            ents = {k: snake_to_camel(str(v)) for k, v in ents.items()}

            out_fname = os.path.join(
                base_dir, layout.build_path(ents, path_patterns))
            makedirs(os.path.dirname(out_fname), exist_ok=True)

            _copy_or_convert(in_file, out_fname)
            out_files.append(out_fname)

        return {'out_file': out_files}
