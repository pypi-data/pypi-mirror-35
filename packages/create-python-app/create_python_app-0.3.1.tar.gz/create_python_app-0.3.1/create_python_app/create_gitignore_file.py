from create_python_app.path_utils import *

_file_name= ".gitignore"
_file_content= f"""\
__pycache__
*.pyc
.cache
.pytest_cache

.idea
.vscode/
*.iml

log
data
venv
"""

def create_gitignore_file(base_dir, **kwargs):
    create_file(base_dir, _file_name, content=_file_content)
