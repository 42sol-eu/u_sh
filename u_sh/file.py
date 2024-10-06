"""
----
file-name:      file.py
file-uuid:      f9a23354-de6e-4f09-9061-1719121ceff1
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
from shutil import copyfile                                                    # [docs](https://docs.python.org/3/library/shutil.html) 
from u_sh.result import Result, ErrorState, ErrorCode                          #       
from u_sh.common import *                                                      #

# [Parameters]

# [Global_Variables]

# [Code]

@contextmanager
def file_write(file_name : Union[str,Path]):
    log("file: write resource acquired")

    if type(file_name) == str:
        file_name = Path(file_name)

    if not file_name.exists():
        file_name.touch()
    file = open(file_name, 'a')

    try:
        log("file: using")
        yield(file)
    finally:
        log("file: released")
        file.close()


def touch_file(file_name : Union[str,Path]) -> Result:
    """
    Create a file if it does not exist
    
    Args:
        file_name (Union[str,Path]): the file name
    """
    if type(file_name) == str:
        file_name = Path(file_name)

    if file_name.parent.exists():
        try:
            file_name.touch()
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
            return Result(ErrorState.Error, ErrorCode.FileError, f'Error: {file_name} exception={e}')
    else:
        return Result(ErrorState.Error, ErrorCode.DirectoryError, f'Error: parent directory {file_name.parent} does not exist')
    
    return Result.ok()


def copy_file( file_name : Union[str,Path], to_path : Union[str,Path] ) -> Result:
    """
    Copy a file to a new location
    Parent directories are created if they do not exist.    
    
    Args:
        file_name (Union[str,Path]): the source file
        to_path (Union[str,Path]):   the destination path (with or without the file name)

    """
    # check if the `file_name` exists
    if type(file_name) == str:
        file_name = Path(file_name) 

    if not file_name.exists():
        console.print(f"[red]Error: {file_name} does not exist[/red]")
        return Result(ErrorState.Error, ErrorCode.FileNotFound, f'Error: source file {file_name} does not exist')

    # check if the `to_path` is a directory
    if type(to_path) == str:
        to_path = Path(to_path) 

    if to_path.is_dir():
        # append the file name to the destination path
        to_path = to_path / file_name
    elif not to_path.exists():
        # check if the parent directory exists
        parent = to_path.parent
        log(f'creating parent directory: {parent}')
        if not parent.exists():
            try:
                parent.mkdir(parents=True)    
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
                return Result(ErrorState.Error, ErrorCode.DirectoryError, f'Error: can not create parent directory {parent} exception={e}')
    try:
        copyfile(file_name, to_path)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return Result(ErrorState.Error, ErrorCode.FileError, f'Error: {file_name}, {to_path} exeptoin={e}') 
    
    return Result.ok()


# [Main]
if __name__ == "__main__":
    with file_write('test_file.txt') as file:
        file.write("Hello, World!")
        print("Inside the block")
