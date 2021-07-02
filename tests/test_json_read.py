from exercise1 import *

import pytest
import os


def test_json_reader_is_dict():
    file_name = './run_results.json'
    file_output = read_file(file_name)
    assert isinstance(file_output, dict)


def test_is_output_json():
    out_path = '/home/aakashdatta/PycharmProjects/Exercise1/Output'
    for file in os.listdir(out_path):
        print(file)
        file_name, extension = os.path.splitext(file)
        if extension == '.json':
            assert True
        else:
            print("Test failed: File is not .json format. Test{0} extension is:".format(file_name[-1]), extension)
            assert False


def test_pass_fail():
    suc_data, fail_data = does_test_pass()
    suc_wrong = 0
    s_wrong_ind = []
    fail_wrong = 0
    f_wrong_ind = []
    for suc_test in suc_data:
       if suc_test[1]['status'] != 'pass':
           suc_wrong += 1
           s_wrong_ind.append(suc_test[0])
    for fail_test in fail_data:
        if fail_test[1]['status'] != 'fail':
            fail_wrong += 1
            f_wrong_ind.append(fail_test[0])
    if suc_wrong == 0 and fail_wrong == 0:
        assert True
    else:
        print("Error, {0} tests are incorreclty organised. \n Incorrect pass indices: {1}. \
         \n  Incorrect fail indices {2}".format((suc_wrong + fail_wrong), s_wrong_ind, f_wrong_ind))
        assert False






