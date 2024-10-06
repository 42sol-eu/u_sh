"""
----
file-name:      directory.py
file-uuid:      7e5862de-627a-4999-ae06-ef549e020275
description:    {{description}}

project:
    name:       u-sh
    uuid:       ae582fa5-020c-489c-9140-fb49972e7cab
    url:        https://u-sh.readthedocs.io
"""

# [Imports]
from rich import print                                                         # [docs](https://rich.readthedocs.io)
from rich.console import Console                                               #
from pathlib import Path                                                       # [docs](https://docs.python.org/3/library/pathlib.html)
from shutil import copytree                                                    # [docs](https://docs.python.org/3/library/shutil.html)
from os import chdir                                                           # [docs](https://docs.python.org/3/library/os.html)
from u_sh.result import Result, ErrorState, ErrorCode                          #       
from u_sh.common import *                                                      #
# [Parameters]

# [Global_Variables]

# [Code]
working_directory = Path.cwd
change_directory = chdir

@contextmanager
def directory(directory_name: Union[str, Path]):
    previous_directory = working_directory()
    log(f"directory: acquired in {previous_directory}")

    if type(directory_name) == str:
        directory_name = Path(directory_name)
    
    if not directory_name.is_dir():
        raise FileNotFoundError(f"{directory_name} is not a directory")
    if not directory_name.exists():
        log(f'creating directory: {directory_name}')
        directory_name.mkdir()
    change_directory(directory_name)
    
    try:
        log(f"directory: {directory_name} using")
        yield(directory_name)
    finally:
        log(f"directory: {directory_name} released -> {previous_directory}")
        change_directory(previous_directory)

def copy_directory( directory_name : Union[str,Path], to_path : Union[str,Path] ) -> Result:
    """
    Copy a directory to a new location.
    Parent directories are created if they do not exist.
    
    Args:
        directory_name (Union[str,Path]): the source directory
        to_path (Union[str,Path]):        the destination path

    """
    # check if the `directory_name` exists
    if type(directory_name) == str:
        directory_name = Path(directory_name) 

    if not directory_name.exists():
        console.print(f"[red]Error: {directory_name} does not exist[/red]")
        return Result(ErrorState.Error, ErrorCode.DirectoryNotFound, f"the source directory {directory_name} does not exist")

    # check if the `to_path` exists
    if type(to_path) == str:
        to_path = Path(to_path) 

    if not to_path.exists():
        log(f'creating directory: {to_path}')
        to_path.mkdir() 

    # check if the `to_path` is a directory
    if not to_path.is_dir():
        console.print(f"[red]Error: {to_path} is not a directory[/red]")
        return Result(ErrorState.Error, ErrorCode.DirectoryError, f"the destination path {to_path} is not a directory")

    # copy the directory
    try:
        log(f"copying {directory_name} to {to_path}")
        copytree(directory_name, to_path)
    except Exception as e:
        #TODO: optimize error handling for this exception
        console.print(f"[red]Error: {e}[/red]")
        return Result(ErrorState.Error, ErrorCode.UnknownError)
    
    return Result.ok()

def list_directory(directory : Union[str,Path] = '.'):
    """
    List the contents of a directory

    Args:
        directory ([type]): [description]
    """
    if type(directory) == str:
        directory = Path(directory)
    
    items = []
    for item in directory.iterdir():
        items.append(item)
        #TODO: how to manage stdout?
        print(item)

    return items

# [Main]
if __name__ == "__main__":
    with directory(Path('tests')) as directory:
        list_directory()
