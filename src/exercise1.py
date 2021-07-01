import sys
import json
import os


def read_file(file_name):
    with open(os.path.join(sys.path[0], file_name)) as file:
        data = json.load(file)
    return data


results_data = read_file('run_results.json')
suc_data = []
for test in results_data:
    print(test)
print(results_data.keys())

for test in results_data['results']:
    if test['status'] == 'pass':
        suc_data.append(test)

print(suc_data)
print("hi")
