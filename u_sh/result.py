"""A Simple Result Class
----
file-name:      result.py
file-uuid:      6fa66503-7047-4780-8dbf-cf58ec3f6827
description:    Generate an intielligent Result Class

project:
    name:       u-sh
    uuid:       ae582fa5-020c-489c-9140-fb49972e7cab
    url:        https://u-sh.readthedocs.io
"""

# [Imports]
from rich import print          # [docs](https://rich.readthedocs.io)
from rich.console import Console
import sys
import inspect
from enum import Enum

# [Parameters]

# [Global_Variables]
console = Console()

# [Code]

class ErrorState(Enum):
    Ok = 0
    Error = 1
    Fatal = 2

class ErrorCode(Enum):
    Ok = 0
    UnspecificError = 1
    FileError = 1000
    FileNotFound = 1001
    FileNotReadable = 1002
    FileNotWritable = 1003
    DirectoryError = 1100
    DirectoryNotFound = 1101
    DirectoryNotReadable = 1102
    DirectoryNotWritable = 1103
    UnspecificFatal = 2000

#TODO: add exception handling on error

#ErrorState = Enum('ErrorState', [('Ok',0), ('Error',1), ('Fatal',2)])
current_function_name = lambda n=0: sys._getframe(n + 1).f_code.co_name
#TODO: what is current_function_name for, why is it not used

class Result:
    """
    Result Class

    Returns:
        Result: Result Class
    """
    # -------------------------------------------------------------
    @classmethod
    def ok(cls,value:any=None):
        """ Classmethod ok"""
        return cls(error_state=ErrorState.Ok, value=value)
    
    @classmethod
    def error(cls,message:str=""):
        """ Classmethod error"""
        return cls(error_state=ErrorState.Error, error_code=ErrorCode.UnspecificError, message=message)
    
    @classmethod
    def fatal(cls,message:str=""):
        """ Classmethod fatal"""
        return cls(error_state=ErrorState.Fatal, error_code=ErrorCode.UnspecificFatal, message=message)
    # ---------------------------------------------------------------------------------------
    def __init__( self, error_state:ErrorState=None, error_code:ErrorCode=None, message:str = None,  value:any = None ) -> None:
        """
        Result Object anlegen

        Args:
            error_state (ErrorState): ok, Error, Fatal
            message (str, optional): if Error. Defaults to None.
            value (any, optional): if ok. Defaults to None.
        """        
        self.error_state = error_state
        self.error_code = error_code
        self._message = message
        self._value = value
        
    # ---------------------------------------------------------------------------------------
    def __str__(self) -> str:
        """
        Result Object als String ausgeben 

        Returns:
            str: 
        """
        ret:str = f"Result State: '{self.error_state.name}'({self.error_state.value}) "
        #ret += f" Call from: {inspect.stack()[0][3]} "
        #ret += f" Call from: {inspect.stack()[3].function} "
        if self._message is not None:
            ret += f" - Message: {self._message} "
        if self._value is not None:
            ret += f" - Type: {type(self._value)} - Value: {self._value}"
        return ret
    
    def __eq__(self, value: object) -> bool:
        return self.error_state == ErrorState.Ok
    
    def __bool__(self) -> bool:
        return self.error_state == ErrorState.Ok
    # ---------------------------------------------------------------------------------------
    @property
    def is_ok(self)->bool:
        """
        wenn kein Fehler        

        Returns:
            bool: TRUE wenn kein Fehler
        """        
        
        return self.error_state == ErrorState.Ok
    
    @property
    def is_not_ok(self)->bool:
        """
        wenn Fehler vorhanden

        Returns:
            bool: False im Fehlerfall
        """        
        return self.error_state != ErrorState.Ok
    @property
    def is_error(self)->bool:
        """
        wenn Error

        Returns:
            bool: True wenn Error
        """        
        return self.error_state == ErrorState.Error
    @property
    def is_fatal(self)->bool:
        """
        wenn Fatal

        Returns:
            bool: True wenn Fatal Fehler
        """        
        return self.error_state == ErrorState.Fatal
    @property
    def get_value(self)->any:
        """
        gibt den Inhalt zurück

        Returns:
            any: alle Typen
        """        
        if self._value is not None:
            return self._value
    @property
    def get_result(self)->tuple:
        """
        ein Tuple mit is_ok und einen bool Wert der in Value steht

        Returns:
            tuple: _description_
        """        
        return (self.is_ok,self.get_value)
        
    # ---------------------------------------------------------------------------------------
    def value(self)->any:
        """
        liefert den Inhalt von Value zurück

        Returns:
            any: alle Typen
        """        
        if self.is_not_ok:
            return None
        return self._value
    
    def error_message(self)->str:
        """
        error Message

        Returns:
            str: Error Message or None
        """        
        if self.is_error:
            return self._message
        return None

# ---------------------------------------------------------------------------------------
#def example_use_result_ok(result:Result):
#    return Result.ok(42)

#def example_use_result_error(result:Result):
#    return Result.error("Not too bad")

#def example_use_result_fatal(result:Result):
#    return Result.fatal("Really fucked up")
