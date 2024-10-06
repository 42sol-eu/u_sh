import pytest
from pathlib import Path
from time import sleep as sleep_seconds
from u_sh.result import Result, ErrorState, ErrorCode
from u_sh import __version__ as u_sh_version
from u_sh.common import Yes, No
from u_sh.file import touch_file, copy_file
from u_sh.directory import list_directory

def remove_directory(directory_name):
    if directory_name.exists():
        for file in directory_name.iterdir():
            file.unlink(missing_ok=Yes)
        directory_name.rmdir()


@pytest.fixture
def directory_exist_1():
    file_name = "tests/temp/exists/test_file.txt"
    parent = Path(file_name).parent 
    if not Path(file_name).exists():
        parent.mkdir(parents=Yes, exist_ok=Yes)
        Path(file_name).touch()

    yield parent

    remove_directory(parent)


@pytest.fixture
def directory_not_exist_1():
    file_name = "tests/temp/not_exists"

    remove_directory(file_name)

    yield file_name

    remove_directory(file_name)



class TestDirectoryClass:

    def test_copy_directory(directory_exist_1, directory_not_exist_1):
        #TODO: Implement the test copy directory test.