import sys
import json
import os


def read_file(file_name):
    path = '/home/aakashdatta/PycharmProjects/Exercise1/src'
    with open(os.path.join(path, file_name)) as file:
        data = json.load(file)
        file.close
    return data


results_data = read_file('run_results.json')

def does_pass_test:
    suc_data = []
    fail_data = []
    pass_count = 0
    for index, test in enumerate(results_data['results']):
        test_f_name = 'test_num{0}.json'.format(index)
        with open(test_f_name, 'w') as json_test:
            json.dump(test, json_test)
            json_test.close()
        if test['status'] == 'pass':
            suc_data.append([index, test])
            pass_count += 1
        elif test['status'] == 'fail':
            fail_data.append([index, test])
print(fail_data)