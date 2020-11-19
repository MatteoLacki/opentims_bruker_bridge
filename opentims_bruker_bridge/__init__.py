import os


_abspath = os.path.abspath(__file__)
_mod_dir = os.path.dirname(_abspath)

_opj = os.path.join

_paths = [
    _opj(_mod_dir, "libtimsdata.so"),
    _opj(_mod_dir, "win32", "timsdata.dll"),
    _opj(_mod_dir, "win64", "timsdata.dll")
    ]


def get_so_paths():
    return _paths
