from create_python_app.path_utils import *

_file_name= "README.md"
def _get_file_content(app_name):
    return f"""README for {app_name} app."""

def create_readme_file(base_dir, **kwargs):
    create_file(base_dir, _file_name, content=_get_file_content(kwargs["app_name"]))