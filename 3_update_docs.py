"""
----
file-name:      3_update_docs.py
file-uuid:      63a48d57-650a-46a6-a321-0062a301bbee
description:    Tool-script to update the documentation of a python library

project:
    name:       u-sh
    uuid:       ae582fa5-020c-489c-9140-fb49972e7cab
    url:        https://u-sh.readthedocs.io
"""

# [Imports]
from rich.console import Console                # https://rich.readthedocs.io/en/latest/
from re import compile                          # https://docs.python.org/3/library/re.html     
                                                # https://regex101.com           
from datetime import datetime                   # https://docs.python.org/3/library/datetime.html

from dataclasses import dataclass               # https://docs.python.org/3/library/dataclasses.html
console = Console()
from toml import load, dump                     # https://github.com
import click                                    # https://click.palletsprojects.com/en/8.0.x/
from os import system as execute 


# [Parameter]
P_path = 'u_sh/__VERSION__'
P_format = r'(?P<major>[0-9]{4})\.(?P<minor>[0-9]{1,3})\.(?P<patch>[0-9]{1,3})'
P_code = 'u_sh/__init__.py'
P_project = 'pyproject.toml'

regex_version = compile(P_format)

@click.command()
@click.option('--release', is_flag=True, default=False,
               help='Make a release version (reset path to 0)')
def main(release: bool = False):    

    execute("poetry run sphinx-build -b html docs docs/_build")

if __name__ == '__main__':
    main()