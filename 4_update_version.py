"""
----
file-name:      4_update_version.py
file-uuid:      1f43af9d-169c-43c1-888f-4aef296a4cb8
description:    Tool-script to update the version of a python library

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


# [Parameter]
P_path = 'u_sh/__VERSION__'
P_format = r'(?P<major>[0-9]{4})\.(?P<minor>[0-9]{1,3})\.(?P<patch>[0-9]{1,3})'
P_code = 'u_sh/__init__.py'
P_project = 'pyproject.toml'

regex_version = compile(P_format)

def get_actual_year():
    return datetime.now().year

class Version:
    major: int
    minor: int
    patch: int


    def __init__(self, major: int, minor: int, patch: int):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __init__(self, version: str):
        
        if not self.check_version(version):
            raise ValueError(f"The given version is not a correct version like 2024.1.123 {version}")
    
        version = version.split('.')
        self.major = int(version[0])
        self.minor = int(version[1])
        self.patch = int(version[2])

    def check_version(self, version: str) -> bool:
        global regex_version
        
        result = regex_version.match(version)
        if result:
            return True
        return False
    
    def get_version(self, version : str) -> str:
        global regex_version
        
        match = regex_version.match(version)
        if match:
            self.major = match.group('major') # Year
            self.minor = match.group('minor') # Release
            self.patch = match.group('patch') # Path

    def set_actual_year(self):
        self.major = get_actual_year()

    def update_version(self, release: bool = False):
        year = get_actual_year()
        if year != self.major:
            self.major = year
            self.minor = 0
            self.patch = 0
        if release:
            self.minor += 1
            self.patch = 0
        else:
            self.patch += 1

        return self

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"
    
    def __repr__(self):
        return f"Version({self.major}, {self.minor}, {self.patch})"



@click.command()
@click.option('--release', is_flag=True, default=False,
               help='Make a release version (reset path to 0)')
def main(release: bool = False):    

    with open(P_path) as version_file:
        __version__ = version_file.read().strip()

        version = Version(__version__)
        version.update_version(release=release)
        console.print(f"Version: {str(version)}")
    

    with open(P_path, 'w') as version_file:
        version_file.write(str(version))
        console.print(f"Library updated to {str(version)}")

    content = ""
    with open(P_code, 'r') as version_file:
        for line in version_file.readlines():
            if '__version__' in line:
                line = f"__version__ = '{str(version)}'\n"            
            content += line 


    with open(P_code, 'w') as version_file:
        version_file.write(content)

        console.print(f"Code updated to {str(version)}")

    with open(P_project, 'r') as project_file:
        project = load(project_file)

    if 'tool' not in project:
        project['tool'] = {}
    if 'poetry' not in project['tool']:
        project['tool']['poetry'] = {}
    
    project['tool']['poetry']['version'] = str(version)

    with open(P_project, 'w') as project_file:
        dump(project, project_file)
        console.print(f"Project updated to {str(version)}")

if __name__ == '__main__':
    main()