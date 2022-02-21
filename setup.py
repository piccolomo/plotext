# /usr/bin/env python3
import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    author = "Savino Piccolomo",
    author_email = "piccolomo@gmail.com",
    name = 'plotext',
    version='4.2.0',
    description = 'plotext plots directly on terminal',
    long_description = README,
    long_description_content_type = "text/markdown",  
    license = "MIT",
    url = 'https://github.com/piccolomo/plotext',
    packages = find_packages(),
    python_requires = ">=3.5",
    include_package_data = True,
    install_requires = [],
    extras_require = {"image": ["pillow>=8.4"]},
    classifiers = []
    )
