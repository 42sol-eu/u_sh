import pytest
from pathlib import Path
from time import sleep as sleep_seconds
from u_sh.result import Result, ErrorState, ErrorCode
from u_sh import __version__ as u_sh_version
from u_sh.common import Yes, No
from u_sh.file import touch_file, copy_file
from u_sh.directory import list_directory

@pytest.fixture
def file_exist_1():
    file_name = "tests/temp/test_file.txt"
    if Path(file_name).exists():
        Path(file_name).unlink()
    
    yield file_name

    if Path(file_name).exists():
        Path(file_name).unlink()

@pytest.fixture
def file_not_exist_1():
    file_name = "tests/temp/test_directory/test_file.txt"
    file_path = Path(file_name)

    if file_path.parent.exists():
        parent = file_path.parent
        for file in parent.iterdir():
            file.unlink(missing_ok=Yes)
        if parent.exists():
            parent.rmdir()
    
    yield file_name

    if file_path.exists():
        file_path.unlink()

class TestFileClass:
        
        def test_touch_file(self, file_exist_1):
            # Part 1: Create a file (new file)
            file_name = file_exist_1
            
            if Path(file_name).exists():
                Path(file_name).unlink(missing_ok=Yes)

            assert Path(file_name).exists() == False
            result = touch_file(file_name)
            assert result.is_ok == True
            assert Path(file_name).exists() == True
            assert Path(file_name).is_file() == True
            atime_1 = Path(file_name).stat().st_atime
            mtime_1 = Path(file_name).stat().st_mtime
            assert atime_1 == mtime_1
            sleep_seconds(10)
            
            # Part 2: Create the file again
            result = touch_file(file_name)
            assert result.is_ok == True
            atime_2 = Path(file_name).stat().st_atime
            mtime_2 = Path(file_name).stat().st_mtime
            
            assert int(atime_1)+10 == int(atime_2)
            assert int(mtime_2) == int(atime_2)
            
        def test_touch_file_subfolder(self, file_not_exist_1):
            # Create a file in a directory that does not exist
            # > directory will not be created (because the command `touch` does not create directories)
            file_name = file_not_exist_1
            result = touch_file(file_name)
            assert result.is_not_ok == True
            assert Path(file_name).exists() == False
            
        def test_copy_file(self):
            # Create a file
            file_name = "tests/temp/test_file.txt"
            result = touch_file(file_name)
            assert result.is_ok == True
            
            # Copy the file
            to_path = "tests/temp/test_file_copy.txt"
            result = copy_file(file_name, to_path)
            assert result.is_ok == True
            
            # Copy the file to a directory that does not exist
            # -> directory will be created
            to_path = "tests/temp/test_directory/test_file_copy.txt"
            result = copy_file(file_name, to_path)
            assert result.is_ok == True
            
            # Copy a file that does not exist
            file_name = "tests/temp/test_file_not_exist.txt"
            to_path = "tests/temp/test_file_copy.txt"
            result = copy_file(file_name, to_path)
            assert result.is_not_ok == True
            
            # Copy a file to a directory that does not exist
            # -> directory will be created
            file_name = "tests/temp/test_file.txt"
            to_path = "tests/temp/test_directory/test_file_copy.txt"
            result = copy_file(file_name, to_path)
            assert result.is_ok == True


if __name__ == "__main__":
    pytest.main(args=[__file__])