import os
from errno import EEXIST
from os import makedirs


base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sql_dir = 'sql'


def get_full_path(*path):
    return os.path.join(base_dir, *path)


def absolute_path(*path):
    return os.path.join(*path)


def makedir(mypath):
    # Creates new directory.
    try:
        makedirs(mypath)
    except OSError as exc:
        if exc.errno == EEXIST and os.path.isdir(mypath):
            pass
        else:
            raise
