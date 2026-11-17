import os
import pathlib
import platform
import subprocess
import sys

from setuptools.command.build_py import build_py
from setuptools.command.develop import develop


# Where this file, the kernel sources and the file compiling them all sit.
here = pathlib.Path(__file__).parent.resolve()
cpp_folder = here / "plotext" / "_kernel" / "cpp"
cpp_source = cpp_folder / "kernel.cpp"


# The command compiling the kernel on windows: the Microsoft compiler when installed, one of the two mingw ones otherwise, and nothing when none is found.
# The mingw commands carry the static flags, which fold the compiler own libraries into the file: without them the file is built but python cannot load it, its companion libraries sitting elsewhere.
def get_windows_command(out):
    import shutil
    if shutil.which("cl.exe"):
        return ["cl.exe", "/LD", "/O2", "/EHsc", "/std:c++17", "/permissive-",   # the strict setting, the one conda-forge builds with
                str(cpp_source), "/link", "/OUT:" + str(out)]
    if shutil.which("g++"):
        return ["g++", "-shared", "-O2", "-std=c++17", "-fno-stack-protector",
                "-static", "-static-libgcc", "-static-libstdc++",
                "-o", str(out), str(cpp_source)]
    if shutil.which("x86_64-w64-mingw32-g++"):
        return ["x86_64-w64-mingw32-g++", "-shared", "-O2", "-std=c++17", "-fno-stack-protector",
                "-static", "-static-libgcc", "-static-libstdc++",
                "-o", str(out), str(cpp_source)]
    return None


# Build the kernel through setuptools, which finds Microsoft's compiler for the machine python runs on; it raises when none is installed, and the commands above take over
def compile_kernel_with_setuptools(out):
    from setuptools._distutils.ccompiler import new_compiler
    compiler = new_compiler()
    compiler.initialize()
    objects = compiler.compile([str(cpp_source)], output_dir = str(cpp_folder), extra_postargs = ["/O2", "/EHsc", "/std:c++17", "/permissive-"])
    compiler.link_shared_object(objects, str(out))


# The machine a windows file was built for, read from its header, as "AMD64" or "ARM64"
def get_windows_file_machine(path):
    machine_names = {0x14c: "x86", 0x8664: "AMD64", 0xaa64: "ARM64"}
    with open(path, "rb") as file:
        file.seek(0x3c)
        header_position = int.from_bytes(file.read(4), "little")
        file.seek(header_position + 4)
        machine = int.from_bytes(file.read(2), "little")
    return machine_names.get(machine, str(machine))


# Compile the kernel into kernel.so, or kernel.dll on windows; a missing compiler, or a build that produces nothing, stops the installation, since the package would not run.
def compile_kernel():
    if not cpp_source.exists():
        print(f"[plotext] skip: {cpp_source} not found", file=sys.stderr)
        return

    # The -fno-stack-protector option turns off a compiler check that some systems fail on the kernel fixed size buffers, even when nothing is actually wrong; without it the package would not build there.
    cmd = None                            # the command to run, left unset when setuptools has already built the kernel itself
    if platform.system() == "Windows":
        out = cpp_folder / "kernel.dll"
        try:                              # setuptools first, the only one knowing which compiler belongs to this machine
            print("[plotext] compiling kernel through setuptools", flush = True)
            compile_kernel_with_setuptools(out)
        except Exception as exc:
            print(f"[plotext] setuptools could not compile the kernel ({exc}), trying the compilers on the path", flush = True)
            cmd = get_windows_command(out)
            if cmd is None:
                if out.exists():          # an already built kernel travels with the package, so there is nothing to do
                    return
                raise SystemExit("[plotext] no C++ compiler found (looked for cl.exe, g++, x86_64-w64-mingw32-g++), so the drawing kernel cannot be built and plotext would not run.\n"
                                 "[plotext] Install a ready made version instead, with pip install plotext, or install the MSVC build tools and try again.")
    else:
        out = cpp_folder / "kernel.so"
        cmd = ["g++", "-fPIC", "-shared",                              # the standard is named, older compilers defaulting to one this kernel does not compile under
               "-O2", "-std=c++17", "-Wall", "-Wextra", "-pedantic", "-fno-stack-protector",   # -pedantic names anything the standard does not allow, as an array sized while running, which Microsoft's compiler refuses outright
               "-o", str(out), str(cpp_source)]
        if platform.system() == "Darwin":                              # macos builds one wheel per architecture and names the wanted one here, which a raw compiler call must pass on
            cmd += os.environ.get("ARCHFLAGS", "").split()

    if cmd is not None:
        print(f"[plotext] compiling kernel: {' '.join(cmd)}", flush=True)
        try:
            subprocess.check_call(cmd)
        except (subprocess.CalledProcessError, FileNotFoundError) as exc:
            raise SystemExit(f"[plotext] the drawing kernel failed to compile ({exc}), so plotext would not run.\n"
                             "[plotext] Install a ready made version instead, with pip install plotext.")

    if not out.exists():              # the compiler said nothing, yet nothing came out of it
        raise SystemExit(f"[plotext] the drawing kernel was not produced at {out}, so plotext would not run.")

    if platform.system() == "Windows":   # a compiler building for the wrong machine leaves a file python refuses, saying only that it is not a valid application
        built_for = get_windows_file_machine(out)
        wanted = platform.machine()
        if built_for != wanted:
            raise SystemExit(f"[plotext] the drawing kernel was built for {built_for} while this python is {wanted}, so it would not load.\n"
                             "[plotext] Use the compiler of this machine, from a developer command prompt opened for it, and try again.")


# The building step of the installation, compiling the kernel before the rest.
class BuildPyWithKernel(build_py):
    def run(self):
        compile_kernel()
        super().run()


# The same, for an installation made to be edited in place.
class DevelopWithKernel(develop):
    def run(self):
        compile_kernel()
        super().run()


# Running this file on its own compiles the kernel, as python3 build_cpp.py.
if __name__ == "__main__":
    compile_kernel()
