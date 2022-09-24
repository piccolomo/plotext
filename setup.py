# /usr/bin/env python3
import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    author="Savino Piccolomo",
    author_email="piccolomo@gmail.com",
    name='plotext',
    version='2.2.2',
    description='plotext plots data directly on terminal',
    long_description=README,
    long_description_content_type="text/markdown",  
    license="MIT",
    url='https://github.com/piccolomo/plotext',
    packages=find_packages(),
    python_requires=">=3.5",
    include_package_data=True,
    #install_requires=[],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
    ],
)
