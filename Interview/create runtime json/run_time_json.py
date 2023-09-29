import os
import json

path = os.path.dirname(os.path.abspath(__file__))+ '/result.json'

my_dict = {'a':1, 'b':2}

with open(path,'w') as file:
    json.dump(my_dict, file)

with open(path,'r') as read_file:
    a = json.load(read_file)
    print(a)