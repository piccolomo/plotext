#!/usr/bin/env python3
import pathlib
from setuptools import setup, find_namespace_packages

from build_cpp import BuildPyWithKernel, DevelopWithKernel


HERE = pathlib.Path(__file__).parent.resolve()
README = (HERE / "README.md").read_text(encoding="utf-8")


setup(
    name="plotext",
    version="6.0.0beta",
    author="Savino Piccolomo",
    author_email="piccolomo@gmail.com",
    description="plotext plots directly on terminal",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/piccolomo/plotext",

    packages=find_namespace_packages(include=["plotext", "plotext.*"]),
    include_package_data=True,
    package_data={"plotext": ["_kernel/cpp/kernel.so",
                              "_kernel/cpp/kernel.dll"]},

    python_requires=">=3.5",
    install_requires=[],
    extras_require={
        "image": ["pillow>=8.4"],
        "video": ["pillow>=8.4",
                  "pafy>=0.5.5",
                  "opencv-python>=4.5.5",
                  "ffpyplayer>=4.3.5",
                  "youtube-dl==2020.12.2"],
        "completion": ["shtab"],
    },
    classifiers=[],

    # C++ kernel build hooks (defined in build_cpp.py)
    cmdclass={
        "build_py": BuildPyWithKernel,
        "develop": DevelopWithKernel,
    },
)
