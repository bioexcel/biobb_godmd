""" Common functions for package biobb_godmd.godmd """
from pathlib import Path, PurePath
from biobb_common.tools import file_utils as fu


# CHECK INPUT PARAMETERS
def check_input_path(path, argument, optional, out_log, classname):
    """ Checks input file """
    if optional and not path:
        return None
    if not Path(path).exists():
        fu.log("Path: " + path)
        fu.log("Path " + path + " --- " + classname + ': Unexisting %s file, exiting' % argument, out_log)
        raise SystemExit(classname + ': Unexisting %s file' % argument)
    file_extension = PurePath(path).suffix
    if not is_valid_file(file_extension[1:], argument):
        fu.log(classname + ': Format %s in %s file is not compatible' % (file_extension[1:], argument), out_log)
        raise SystemExit(classname + ': Format %s in %s file is not compatible' % (file_extension[1:], argument))
    return path


def check_output_path(path, argument, optional, out_log, classname):
    """ Checks output file """
    if optional and not path:
        return None
    if PurePath(path).parent and not Path(PurePath(path).parent).exists():
        fu.log(classname + ': Unexisting  %s folder, exiting' % argument, out_log)
        raise SystemExit(classname + ': Unexisting  %s folder' % argument)
    file_extension = PurePath(path).suffix
    if not is_valid_file(file_extension[1:], argument):
        fu.log(classname + ': Format %s in  %s file is not compatible' % (file_extension[1:], argument), out_log)
        raise SystemExit(classname + ': Format %s in  %s file is not compatible' % (file_extension[1:], argument))
    return path


def is_valid_file(ext, argument):
    """ Checks if file format is compatible """
    formats = {
        'input_pdb_orig_path': ['pdb'],
        'input_pdb_target_path': ['pdb'],
        'input_aln_orig_path': ['aln', 'txt'],
        'input_aln_target_path': ['aln', 'txt'],
        'input_config_path': ['in', 'txt'],
        'output_aln_orig_path': ['aln', 'txt'],
        'output_aln_target_path': ['aln', 'txt'],
        'output_log_path': ['log', 'out', 'txt'],
        'output_ene_path': ['log', 'out', 'txt'],
        'output_trj_path': ['x', 'trj', 'crd', 'mdcrd'],
        'output_pdb_path': ['pdb']
    }
    return ext in formats[argument]
