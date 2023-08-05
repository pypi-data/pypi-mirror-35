import json
import os

path = os.path.join(os.path.dirname(__file__), '..', 'config', 'sys.json')
with open(path) as file:
    options = json.load(file)

def get_options():
    return options