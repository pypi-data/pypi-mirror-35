from create_python_app.path_utils import *

def create_root_package(base_dir, **kwargs):
    create_dir(base_dir, kwargs["app_name"])
    create_file(base_dir, kwargs["app_name"], '__init__.py', content="")