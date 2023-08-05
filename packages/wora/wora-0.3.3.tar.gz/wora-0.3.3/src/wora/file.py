from pathlib import Path
import os

from wora.fn import identity
from wora.syntax import tern_func

def to_path(fp: str) -> Path:
    ''' Convert str to Path '''
    if isinstance(fp, Path):
        return fp
    elif isinstance(fp, str):
        return Path(fp)

def read_file(fname: str) -> str:
    ''' Reads a file into a string '''
    file = open(fname, 'r')
    res = file.read()
    file.close()
    return res

def write_file(fname: str, content: str):
    ''' Write a string to a file '''
    file = open(fname, 'w')
    file.write(content)
    file.close()

def mkpath(p: str | Path):
    ''' Convert strings to paths '''
    return tern_func(isinstance(p, Path), identity, lambda p: Path(p), p)

def mkdir(file):
    ''' Make a directory from a str or Path '''
    if isinstance(file, str):
        Path(file).mkdir(parents=True, exist_ok=True)
    elif isinstance(file, Path):
        file.mkdir(parents=True, exist_ok=True)

def exists(path):
    ''' Determine if a file/folder/symlink exists '''
    return to_path(path).exists()

def get_cwd_of(file: str) -> str:
    ''' Retrieve the current working directory of a given file '''
    return os.path.dirname(file)

def make_folder(file: str):
    ''' Make folder for a file if it doesn't already exist '''
    if not (path := Path(file).exists()):
        mkdir(get_cwd_of(file))
    pass

def expand(path):
    ''' Expands platform specific environment variables for paths '''
    return mkpath(path).expanduser()
