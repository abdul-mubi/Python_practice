import os
import json

path = os.path.dirname(os.path.abspath(__file__)) + '/my_json.json'

with open (path, 'r') as file:
    a = json.load(file)
    print((a))

