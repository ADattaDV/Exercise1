import json
import os
output_path = '/home/aakashdatta/PycharmProjects/Exercise1/Output'


def read_file(file_name):
    source_path = '/home/aakashdatta/PycharmProjects/Exercise1/src'
    with open(os.path.join(source_path, file_name)) as file:
        data = json.load(file)
        file.close()
    return data


results_data = read_file('run_results.json')


def save_json(index, test):
    test_f_name = os.path.join(output_path, 'test_num{0}.json'.format(index))
    with open(test_f_name, 'w') as json_test:
        json.dump(test, json_test)
        json_test.close()


def does_test_pass():
    suc_data = []
    fail_data = []
    pass_count = 0
    for index, test in enumerate(results_data['results']):
        save_json(index, test)
        if test['status'] == 'pass':
            suc_data.append([index, test])
            pass_count += 1
        elif test['status'] == 'fail':
            fail_data.append([index, test])
    return suc_data, fail_data
suc_data, fail_data = does_test_pass()
print(suc_data[0][1])