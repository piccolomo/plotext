# Bridge to the C kernel: loads the compiled library and registers each of its functions with the types it takes and gives back.

from plotext._settings.system import platform as system_platform
import ctypes
import os


# The compiled kernel library, beside this file, named after the system.
script_folder = os.path.dirname(os.path.realpath(__file__))
kernel_file_name = 'kernel.dll' if system_platform == 'windows' else 'kernel.so'
kernel_file_path = os.path.join(script_folder, 'cpp', kernel_file_name)

# The drawing is done by the C++ kernel, so a missing or unloadable file is said plainly here, the alternative being a bare loading error from ctypes
if not os.path.isfile(kernel_file_path):
    raise ImportError(f"plotext cannot draw: its C++ part, {kernel_file_name}, was not built during the installation, most likely for want of a C++ compiler.\nInstall a ready made version instead, with pip install --upgrade --force-reinstall plotext, which carries the file already built.")

try:
    kernel = ctypes.CDLL(kernel_file_path)
except OSError as error:
    raise ImportError(f"plotext cannot draw: its C++ part, {kernel_file_path}, is there but will not load ({error}).\nOn windows this usually means the compiler that built it left its own libraries behind; installing a ready made version, with pip install --upgrade --force-reinstall plotext, avoids the matter.") from None


# The plain name of each type the kernel functions take or give back, as "float" for a C float.
types_dict = {
    # scalars
    "size": ctypes.c_size_t,
    "integer": ctypes.c_int,
    "float": ctypes.c_float,
    "bool": ctypes.c_bool,

    # strings
    "wstring": ctypes.c_wchar_p,
    "string": ctypes.c_char_p,
    "wchar": ctypes.c_wchar,

    # pointers
    "void": ctypes.c_void_p,
    "float pointer": ctypes.POINTER(ctypes.c_float),
    "wchar pointer": ctypes.POINTER(ctypes.c_wchar)}


wstring = types_dict["wstring"]
wchar = types_dict["wchar"]


# The registry of the kernel functions: each is added by name, then told the types it takes and the one it gives back.
class clink_class:
    # Initialize the registry; last_function is the one just added, which input() and output() describe.
    def __init__(self):
        self.last_function = None

    # Add a kernel function, its name being the given words joined by underscores, as add("matrix", "new") for matrix_new; its output starts as void.
    def add(self, *names):
        name = '_'.join(names)

        function = getattr(kernel, name)
        setattr(self, name, function)
        self.last_function = function

        self.output("void")
        return self

    # Declare the types the last added function takes, as input("void", "size").
    def input(self, *type_names):
        self.last_function.argtypes = tuple(types_dict[type_name] for type_name in type_names)
        return self

    # Declare the type the last added function gives back, as output("float").
    def output(self, type_name):
        self.last_function.restype = types_dict[type_name]
        return self

    # The signature of every registered function, one per line, as "matrix_new(size, size) -> void".
    def __repr__(self):
        lines = []
        for name, function in self.__dict__.items():
            if not callable(function) or name == "last_function":
                continue
            input_types = getattr(function, "argtypes", None)
            output_type = getattr(function, "restype", None)
            inputs = ", ".join(self._get_type_name(type_used) for type_used in input_types) if input_types else ""
            output = self._get_type_name(output_type) if output_type is not None else "None"
            lines.append(f"{name}({inputs}) -> {output}")
        return "\n".join(sorted(lines))

    # The plain name of a ctypes type, as "float" for c_float; an unknown type gives its own text.
    def _get_type_name(self, type_used):
        if type_used is None:
            return "None"
        for name, ctypes_type in types_dict.items():
            if ctypes_type == type_used:
                return name
        return str(type_used)


clink = clink_class()
