from create_python_app.path_utils import *

_file_name= "requirements.txt"
def _get_file_content():
    return f"""\
-e git+https://github.com/xuchaoqian/pycommons.git@master#egg=pycommons    
"""

def create_requirements_file(base_dir, **kwargs):
    create_file(base_dir, _file_name, content=_get_file_content())