import pathlib
import platform
import subprocess
import sys

from setuptools.command.build_py import build_py
from setuptools.command.develop import develop


HERE = pathlib.Path(__file__).parent.resolve()
CPP_DIR = HERE / "plotext" / "_kernel" / "cpp"
CPP_SRC = CPP_DIR / "kernel.cpp"


def compile_kernel():
    """Compile the C++ kernel into kernel.so (or kernel.dll on Windows)."""
    if not CPP_SRC.exists():
        print(f"[plotext] skip: {CPP_SRC} not found", file=sys.stderr)
        return

    if platform.system() == "Windows":
        out = CPP_DIR / "kernel.dll"
        cmd = ["x86_64-w64-mingw32-g++", "-shared",
               "-O2", "-o", str(out), str(CPP_SRC)]
    else:
        out = CPP_DIR / "kernel.so"
        cmd = ["g++", "-fPIC", "-shared",
               "-O2", "-Wall", "-Wextra",
               "-o", str(out), str(CPP_SRC)]

    print(f"[plotext] compiling kernel: {' '.join(cmd)}", flush=True)
    try:
        subprocess.check_call(cmd)
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"[plotext] WARNING: kernel compilation failed ({exc}).",
              file=sys.stderr)
        print("[plotext] If no prebuilt kernel is bundled, run "
              "'python build_cpp.py' from a cloned repository.",
              file=sys.stderr)


class BuildPyWithKernel(build_py):
    """setuptools build_py command that compiles the C++ kernel first."""
    def run(self):
        compile_kernel()
        super().run()


class DevelopWithKernel(develop):
    """setuptools develop command that compiles the C++ kernel first."""
    def run(self):
        compile_kernel()
        super().run()


# Allow `python3 build_cpp.py` for a quick manual build.
if __name__ == "__main__":
    compile_kernel()
