from exercise1 import *
import pytest
#check whether pass works correctly...
def test_does_test_pass():
    file_name = './run_results.json'
    file_output = read_file(file_name)
    assert isinstance(file_output, dict)
