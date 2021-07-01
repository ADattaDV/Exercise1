from exercise1 import *

import pytest
import os


def test_json_reader_is_dict():
    file_name = './run_results.json'
    file_output = read_file(file_name)
    assert isinstance(file_output, dict)


def test_is_output_json():
    out_path = '/home/aakashdatta/PycharmProjects/Exercise1/Output'
    for file_name in os.listdir(out_path):
        print(file_name)
        if file_name.endswith('.json'):
            assert True
        else:
            print("Test failed: File is not .json format.")


def test_pass_fail():
    suc_data, fail_data = does_test_pass()
    suc_working = True
    fail_working = True
    for suc_test in suc_data:
       if suc_test[1]['status'] != 'pass':
           suc_working = False
    for fail_test in fail_data:
        if fail_test[1]['status'] != 'fail':
            fail_working = False
    if suc_working == True and fail_working == True:
        assert True
    else:
        print("Success list:", suc_working, "Failure list:", fail_working)







