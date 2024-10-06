import pytest
from u_sh.result import Result, ErrorState, ErrorCode
from u_sh import __version__ as u_sh_version

class TestResultClass:
    
    def test_is_not_ok(self):
        # Create an instance with error_state not equal to ErrorState.Ok
        instance = Result(ErrorState.Error, ErrorCode.UnspecificError, "Error message")
        assert instance.is_not_ok == True
        assert instance.error_state == ErrorState.Error
        
        instance = Result(ErrorState.Fatal, ErrorCode.UnspecificFatal, "Fatal error message")
        assert instance.is_not_ok == True
        assert instance.error_state == ErrorState.Fatal
        
        # Create an instance with error_state equal to ErrorState.Ok
        instance = Result(ErrorState.Ok)
        assert instance.is_ok == True
        assert instance.is_not_ok == False
        assert instance.error_state == ErrorState.Ok

    def test_is_error(self):
        # Create an instance with error_state indicating an error
        instance = Result(ErrorState.Error, ErrorCode.UnspecificError, "Error message")
        assert instance.is_error == True
        
        # Create an instance with error_state not indicating an error
        instance = Result(ErrorState.Ok)
        assert instance.is_error == False

# Run the tests
if __name__ == "__main__":
    print( f'testing {u_sh_version}')
    pytest.main()