import pytest 
import json
from unittest.mock import patch,mock_open
from src.load_todo import jsonWork

def test_load_list_success():
    #Tests that load_list reads and returns valid JSON data from the file path which is predefined.
    mock_data='[{"id": 1,"task": "Test the method"}]'
    with patch("builtins.open",mock_open(read_data=mock_data)):
        with patch("json.load",return_value=[{"id": 1,"task": "Test the method"}]):
            result= jsonWork.load_list()
            assert result==[{"id": 1,"task": "Test the method"}]

def test_load_list_file_not_found_error():
    #Test the filenotfound exception in case the file doesn't exist
    with patch("builtins.open",side_effect=FileNotFoundError):
        result = jsonWork.load_list()
        assert result == []

def test_load_list_JSonDecodeError():
    invalid_data='{"id":1,"task": "Test task"'
    with patch("builtins.open",mock_open(read_data=invalid_data)):
        with patch("json.load",side_effect=json.JSONDecodeError("Invalid Json","",0)):
            result=jsonWork.load_list()
            assert result==[]

def test_load_list_unexpected_error():
    #To test that load_list handle unexpected errors properly.
    with patch("builtins.open",side_effect=Exception("Unexpected error")):
        result=jsonWork.load_list()
        assert result == []

