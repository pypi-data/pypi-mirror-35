import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
    
setuptools.setup(
    name="create_python_app",
    version="0.3.1",
    author="Xu Chaoqian",
    author_email="chaoranxu@gmail.com",
    description="A tool for creating python apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xuchaoqian/create-python-app.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': ['create_python_app=create_python_app.main:main'],
    }
)
