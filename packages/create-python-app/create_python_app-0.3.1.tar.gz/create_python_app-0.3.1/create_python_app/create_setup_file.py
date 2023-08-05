from create_python_app.path_utils import *

_file_name= "setup.py"
def _get_file_content():
    return f"""\
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
    
setuptools.setup(
    name="",
    version="0.1.0",
    author="nobody",
    author_email="nobody@nohost",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
) 
"""

def create_setup_file(base_dir, **kwargs):
    create_file(base_dir, _file_name, content=_get_file_content())