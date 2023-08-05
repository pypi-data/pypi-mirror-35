from create_python_app.path_utils import *

_file_name= "Makefile"
def _get_file_content(app_name):
    return f"""\
.DEFAULT_GOAL := init

prj-dir := $(shell pwd)
src-dir := $(prj-dir)
venv-dir := $(prj-dir)/venv
python-sys := python3
python-venv := $(venv-dir)/bin/python
pip-venv := $(venv-dir)/bin/pip
jupyter-venv := $(venv-dir)/bin/jupyter
ipython-venv := $(venv-dir)/bin/ipython
pytest-sys := pytest

define get_site_dir
$(shell $(python-venv) -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
endef

create-env:
	$(python-sys) -m venv $(venv-dir)

upgrade-pip:
	$(pip-venv) install --upgrade pip

create-dirs:
	mkdir -p log

install-deps:
	$(pip-venv) install -r requirements.txt

set-path:
	echo $(src-dir) > $(call get_site_dir)/my.pth

install-ipykernel:
	$(pip-venv) install ipykernel
	$(ipython-venv) kernel install --user --name={app_name}

uninstall-ipykernel:
	$(jupyter-venv) kernelspec uninstall -f {app_name} || true

rm-temp-files:
	rm -rf $(venv-dir) $(prj-dir)/build $(prj-dir)/dist $(prj-dir)/{app_name}.egg-info

init: create-env upgrade-pip create-dirs install-deps set-path

run:
	$(python-venv) $(filter-out $@, $(MAKECMDGOALS))

test:
	$(pytest-sys)

pkg:
	$(python-sys) setup.py sdist bdist_wheel

nb: install-ipykernel
	$(jupyter-venv) notebook

clean: uninstall-ipykernel rm-temp-files
"""

def create_makefile_file(base_dir, **kwargs):
    create_file(base_dir, _file_name, content=_get_file_content(kwargs["app_name"]))
