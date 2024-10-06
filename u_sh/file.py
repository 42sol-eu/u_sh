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



def copy_file( file_name : Union[str,Path], to_path : Union[str,Path] ) -> Result:
    """
    Copy a file to a new location
    
    Args:
        file_name (Union[str,Path]): the source file
        to_path (Union[str,Path]):   the destination path

    """
    # check if the `file_name` exists
    if type(file_name) == str:
        file_name = Path(file_name) 

    if not file_name.exists():
        console.print(f"[red]Error: {file_name} does not exist[/red]")
        return 
    
    with open(file_name, 'r') as file:
        data = file.read()



    # check if the `to_path` is a directory
    sink_path = Path(to_path)
    if sink_path.is_dir():
        sink_path = sink_path / file_name

    with open(to_path, 'w') as file:
        file.write(data)

# [Main]
if __name__ == "__main__":
    with file_write('test_file.txt') as file:
        file.write("Hello, World!")
        print("Inside the block")
