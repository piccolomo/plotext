# /usr/bin/env python3
import pathlib
import sys
from setuptools import setup, find_namespace_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# build_cpp.py lives next to setup.py — make it importable so cibuildwheel
# triggers the kernel compile per platform via the cmdclass hooks below.
sys.path.insert(0, str(HERE))
from build_cpp import BuildPyWithKernel, DevelopWithKernel  # noqa: E402

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    author = "Savino Piccolomo",
    author_email = "piccolomo@gmail.com",
    name = 'plotext',
    version='6.0.0b0',
    description = 'plotext plots directly on terminal',
    long_description = README,
    long_description_content_type = "text/markdown",  
    license = "MIT",
    url = 'https://github.com/piccolomo/plotext',
    packages = find_namespace_packages(include=['plotext', 'plotext.*']),
    python_requires = ">=3.8",
    include_package_data = True,
    install_requires = [],
    extras_require = {"image": ["pillow>=8.4"], "video": ["pillow>=8.4", "ffpyplayer>=4.3.5", "yt-dlp>=2024.1.1"]},
    entry_points = {"console_scripts": ["plotext = plotext._cli:main"]},
    cmdclass = {"build_py": BuildPyWithKernel, "develop": DevelopWithKernel},
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Terminals",
    ]
    )
