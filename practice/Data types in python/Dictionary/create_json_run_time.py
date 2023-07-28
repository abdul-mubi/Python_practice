import os
import json

path = os.path.dirname(os.path.abspath(__file__)) + 'run_time_created.json'
dict_one = {'a':1, 'b':2, 'c':3}

with open(path, 'w') as pointer:
    json.dump(dict_one,pointer)
