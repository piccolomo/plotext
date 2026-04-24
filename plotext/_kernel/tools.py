# ctypes bridge to the C kernel: loads the shared library and exposes a thin wrapper to register functions

from plotext._settings.system import platform as system_platform
import ctypes as c
import os


# =========================
# Load shared library safely
# =========================

script_folder = os.path.dirname(os.path.realpath(__file__))
kernel_file_name = 'kernel.dll' if system_platform == 'windows' else 'kernel.so'
kernel_file_path = os.path.join(script_folder, 'cpp', kernel_file_name)

kernel = c.CDLL(kernel_file_path)


# =========================
# Types namespace
# =========================

Types = {
    # scalars
    "size": c.c_size_t,
    "integer": c.c_int,
    "float": c.c_float,
    "bool": c.c_bool,

    # strings
    "wstring": c.c_wchar_p,
    "string": c.c_char_p,
    "wchar": c.c_wchar,

    # pointers
    "void": c.c_void_p,
    "float pointer": c.POINTER(c.c_float),
    "wchar pointer": c.POINTER(c.c_wchar)}


wstring = Types["wstring"]
wchar = Types["wchar"]


# =========================
# Clink wrapper
# =========================

# Thin registry that attaches a C function and declares its ctypes signature
class Clink:
    # Initialize state; last tracks the most recently added function for fluent input/output calls
    def __init__(self):
        self.last = None

    # Register a C function by its underscore-joined name and default its output to void
    def add(self, *names):
        name = '_'.join(names)

        cfunction = getattr(kernel, name)
        setattr(self, name, cfunction)
        self.last = cfunction

        self.output("void")
        return self

    # Declare the argument types of the most recently added function
    def input(self, *args):
        self.last.argtypes = tuple(self._resolve(a) for a in args)
        return self

    # Declare the return type of the most recently added function
    def output(self, output):
        self.last.restype = self._resolve(output)
        return self

    # Map a type name to its ctypes equivalent
    def _resolve(self, arg):
        return Types[arg]

    # Return readable signature of all registered C functions
    def __repr__(self):
        lines = []

        for name, func in self.__dict__.items():
            if not callable(func) or name == "last":
                continue

            argtypes = getattr(func, "argtypes", None)
            restype = getattr(func, "restype", None)

            # format args
            if argtypes is None:
                args = ""
            else:
                args = ", ".join(self._ctype_name(a) for a in argtypes)

            # format return
            ret = self._ctype_name(restype) if restype is not None else "None"

            lines.append(f"{name}({args}) -> {ret}")

        return "\n".join(sorted(lines))

    # Convert a ctypes type back to its readable name
    def _ctype_name(self, t):
        if t is None:
            return "None"

        for k, v in Types.items():
            if v == t:
                return k

        return str(t)


clink = Clink()
