"""
----
file-name:      common.py
file-uuid:      7bd4e97b-828a-4607-8bc1-b5d88aa2decc
description:    {{description}}

project:
    name:       u-sh
    uuid:       ae582fa5-020c-489c-9140-fb49972e7cab
    url:        https://u-sh.readthedocs.io
"""


# [Imports]
from rich import print                                     # [docs](https://rich.readthedocs.io)
from rich.console import Console                           #
from typing import Union                                   # [docs](https://docs.python.org/3/library/typing.html)
from pathlib import Path                                   # [docs](https://docs.python.org/3/library/pathlib.html)
from contextlib import contextmanager                      # [docs](https://docs.python.org/3/library/contextlib.html)
from u_sh.result import Result, ErrorState, ErrorCode                          #       

# [Parameters]
Yes, No = True, False

# [Global_Variables]
console = Console()

# [Code]
def log( message: str ):
    console.print(f"[bold blue]Log:[/bold blue] {message}")