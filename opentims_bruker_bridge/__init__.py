import sys
import os
import platform


_abspath = os.path.abspath(__file__)
_mod_dir = os.path.dirname(_abspath)

_opj = os.path.join



_paths = {
        ("64bit", "ELF") : _opj(_mod_dir, "libtimsdata.so"),
        ("32bit", "WindowsPE") : _opj(_mod_dir, "win32", "timsdata.dll"),
        ("64bit", "WindowsPE") : _opj(_mod_dir, "win64", "timsdata.dll"),
        # Probably CYGWIN:
        ("32bit", "") : _opj(_mod_dir, "win32", "timsdata.dll"),
        ("64bit", "") : _opj(_mod_dir, "win64", "timsdata.dll"),
     }


def get_so_paths():
    try:
        return [_paths[platform.architecture()]] + list(set(_paths.values()) -  set([_paths[platform.architecture()]]))
    except KeyError:
        # unsupported platform: return everything and hope for the best
        return list(set(_paths.values()))

def get_appropriate_so_path():
    '''Use only in proof of concept, quick-and-dirty code. In serious software,
    the try everything and use the one which loads without errors pattern should
    be used.'''
    return _paths[platform.architecture()]
