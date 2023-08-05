from create_python_app.path_utils import *

_file_name= "config.py"
_file_content=f"""\
import json
import os

path = os.path.join(os.path.dirname(__file__), '..', 'config', 'sys.json')
with open(path) as file:
    options = json.load(file)

def get_options():
    return options
"""

def create_config_module(base_dir, **kwargs):
    create_file(base_dir, kwargs["app_name"], _file_name, content=_file_content)