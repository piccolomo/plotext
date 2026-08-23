# /usr/bin/env python3
import pathlib
import sys
from setuptools import setup, find_namespace_packages
from setuptools.dist import Distribution
try:                                                     # setuptools carries it from version 70, the wheel package before that
    from setuptools.command.bdist_wheel import bdist_wheel
except ImportError:
    from wheel.bdist_wheel import bdist_wheel

# The folder holding this file.
here = pathlib.Path(__file__).parent

# build_cpp.py sits beside this file: make it reachable, so that the kernel is compiled on every system the package is built for.
sys.path.insert(0, str(here))
from build_cpp import BuildPyWithKernel, DevelopWithKernel  # noqa: E402

# The text of the readme file, shown as the package description.
readme = (here / "README.md").read_text()

# The version, read as text out of the one file holding it, since importing plotext would load its kernel
def get_version():
    text = (here / "plotext" / "_settings" / "system.py").read_text()
    return text.split('__version__ = version = "')[1].split('"')[0]

# The package carries a kernel compiled for one system, so its wheel must be labelled for that system alone, and not as working everywhere
class binary_distribution(Distribution):
    def has_ext_modules(self):
        return True


# One wheel per system rather than one per python: the kernel is loaded when the package runs, so it is tied to the system alone
class wheel_of_this_system(bdist_wheel):
    def finalize_options(self):
        super().finalize_options()
        self.root_is_pure = False

    def get_tag(self):
        return "py3", "none", super().get_tag()[2]


setup(
    author = "Savino Piccolomo",
    author_email = "piccolomo@gmail.com",
    name = 'plotext',
    version = get_version(),
    description = 'plotext plots directly on terminal',
    long_description = readme,
    long_description_content_type = "text/markdown",  
    license = "MIT",
    url = 'https://github.com/piccolomo/plotext',
    packages = find_namespace_packages(include=['plotext', 'plotext.*']),
    python_requires = ">=3.8",
    include_package_data = True,
    install_requires = [],
    extras_require = {"image": ["pillow>=8.4"], "video": ["pillow>=8.4", "ffpyplayer>=4.3.5", "yt-dlp>=2024.1.1"]},
    entry_points = {"console_scripts": ["plotext = plotext._cli:main"]},
    cmdclass = {"build_py": BuildPyWithKernel, "develop": DevelopWithKernel, "bdist_wheel": wheel_of_this_system},
    distclass = binary_distribution,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Terminals",
    ]
    )
