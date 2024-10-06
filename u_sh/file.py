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
from rich import print          # [docs](https://rich.readthedocs.io)
from rich.console import Console
from pathlib import Path            # [docs](https://docs.python.org/3/library/pathlib.html)
from u_sh.result import Result, ErrorState

# [Parameters]

# [Global_Variables]
console = Console()

# [Code]

#Q: Implement the cp command for one ore more files
def copy_file( file_name, to_path):
    # check if the `file_name` exists
    in_file = Path(file_name)
    if not in_file.exists():
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