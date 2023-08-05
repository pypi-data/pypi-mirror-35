import argparse
from create_python_app.path_utils import *
from create_python_app.create_gitignore_file import create_gitignore_file
from create_python_app.create_license_file import create_license_file
from create_python_app.create_makefile_file import create_makefile_file
from create_python_app.create_readme_file import create_readme_file
from create_python_app.create_requirements_file import create_requirements_file
from create_python_app.create_setup_file import create_setup_file
from create_python_app.create_root_package import create_root_package
from create_python_app.create_config_files import create_config_files
from create_python_app.create_config_module import create_config_module

def _parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, type=str)
    args = parser.parse_args()
    return args.name

def main():
    app_name = _parse()
    base_dir = create_dir(os.getcwd(), app_name)
    create_gitignore_file(base_dir)
    create_license_file(base_dir)
    create_makefile_file(base_dir, app_name=app_name)
    create_readme_file(base_dir, app_name=app_name)
    create_requirements_file(base_dir)
    create_setup_file(base_dir)
    create_root_package(base_dir, app_name=app_name)
    create_config_files(base_dir)
    create_config_module(base_dir, app_name=app_name)

if __name__ == '__main__':
    main()