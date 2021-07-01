# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os
import sys
import unittest

with open(os.path.join(sys.path[0], 'run_results.json')) as file:
    results_data = json.load(file)

suc_data = []
for test in results_data:
    print(test)
print(results_data.keys())

for test in results_data['results']:
    if test['status'] == 'pass':
        suc_data.append(test)

print(suc_data)
print("hi")