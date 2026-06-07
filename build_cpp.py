import pathlib
import platform
import subprocess
import sys

from setuptools.command.build_py import build_py
from setuptools.command.develop import develop


HERE = pathlib.Path(__file__).parent.resolve()
CPP_DIR = HERE / "plotext" / "_kernel" / "cpp"
CPP_SRC = CPP_DIR / "kernel.cpp"


def _windows_compile_cmd(out):
    """Pick a Windows compile command. Native MSVC (cl.exe) when available
    (typical on GitHub Actions windows runners); otherwise fall back to mingw,
    either native (g++ on PATH inside MSYS) or the cross toolchain. The kernel
    is a single TU so we don't need a full setuptools-style invocation."""
    import shutil
    if shutil.which("cl.exe"):
        return ["cl.exe", "/LD", "/O2", "/EHsc", "/std:c++17",
                str(CPP_SRC), "/link", "/OUT:" + str(out)]
    if shutil.which("g++"):
        return ["g++", "-shared", "-O2", "-fno-stack-protector",
                "-o", str(out), str(CPP_SRC)]
    if shutil.which("x86_64-w64-mingw32-g++"):
        return ["x86_64-w64-mingw32-g++", "-shared", "-O2", "-fno-stack-protector",
                "-o", str(out), str(CPP_SRC)]
    return None


def compile_kernel():
    """Compile the C++ kernel into kernel.so (or kernel.dll on Windows)."""
    if not CPP_SRC.exists():
        print(f"[plotext] skip: {CPP_SRC} not found", file=sys.stderr)
        return

    # NOTE: -fno-stack-protector disables gcc's stack canary checks. The kernel
    # uses a few fixed-size wchar_t buffers (e.g. Point::get_wstring's [50])
    # that have always been borderline; on some build environments the canary
    # trips at -O2 even though the buffers are not actually corrupted in
    # practice. Disabling the protector keeps the build portable. The buffers
    # themselves should be enlarged in a follow-up cleanup.
    if platform.system() == "Windows":
        out = CPP_DIR / "kernel.dll"
        cmd = _windows_compile_cmd(out)
        if cmd is None:
            print("[plotext] WARNING: no C++ compiler found (looked for cl.exe, g++, "
                  "x86_64-w64-mingw32-g++). Install MSVC build tools or MSYS2.",
                  file=sys.stderr)
            return
    else:
        out = CPP_DIR / "kernel.so"
        cmd = ["g++", "-fPIC", "-shared",
               "-O2", "-Wall", "-Wextra", "-fno-stack-protector",
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
