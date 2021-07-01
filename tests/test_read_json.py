from exercise1 import *
import pytest

def test_json_reader_is_dict():
    file_name = './run_results.json'
    file_output = read_file('run_results.json')
    assert isinstance(file_output, dict)
