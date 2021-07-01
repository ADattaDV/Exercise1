from exercise1 import *
import pytest

def test_json_reader_is_dict():
    file_name = './run_results.json'
    file_output = read_file(file_name)
    assert isinstance(file_output, dict)
