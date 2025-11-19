from plotext._system import platform
import ctypes as c
import sys, os


script_folder = os.path.dirname(os.path.realpath(__file__))  # Get the folder where the current file is located
kernel_file_name = 'kernel.dll' if platform == 'windows' else 'kernel.so'  # Set the appropriate kernel file based on the platform
kernel_file_path = os.path.join(script_folder, 'cpp', kernel_file_name)  # Path to the kernel file
kernel = c.CDLL(kernel_file_path)  # Load the kernel DLL or SO file

class Clink:
    # Add a function from the kernel to the class
    def add(self, *names):
        name = '_'.join(names) 
        #(name + '_' + surname) if surname is not None else name  # Construct function name
        cfunction = getattr(kernel, name)  # Get the function from the kernel
        #globals()[name] = cfunction  # Make the function globally available
        setattr(self, name, cfunction)  # Store the function internally
        setattr(self, 'last', cfunction)  # Store the function as the last function
        return self

    # Define the argument types for the last function added
    def input(self, *args):
        setattr(self.last, 'argtypes', list(args))  # Set argument types for the function
        return self

    # Define the return type for the last function added
    def output(self, output):
        setattr(self.last, 'restype', output)  # Set return type for the function
        return self

clink = Clink()  # Instantiate the Clink object to manage kernel functions


# C Data Types
void = c.c_void_p  # Represents a void pointer (no data type)
size = c.c_size_t  # Represents an unsigned integer type for sizes (usually used for memory sizes)
integer = c.c_int  # Represents a C integer type (commonly used for int)
float = c.c_float  # Represents a C float type (commonly used for floating point numbers)
float_pointer = c.POINTER(c.c_float)  # Represents a pointer to a C float type
bool = c.c_bool  # Represents a C boolean type (True/False)
wstring = c.c_wchar_p  # Represents a pointer to a wide-character string (C wchar_t type)
string = c.c_char_p  # Represents a pointer to a C string (C char type)
wchar = c.c_wchar  # Represents a C wide-character type (wchar_t)
cstring = c.POINTER(c.c_wchar)  # Represents a pointer to a C wide-character string (array of wchar_t)


# Add general function to link
clink.add('rescale').input(float, float, float, size, float).output(float)
clink.add('wstring', 'delete').input(wstring).output(void)

# Add pixel-related functions to link
clink.add('pixel', 'new').input().output(void)
clink.add('pixel', 'delete').input(void).output(void)
clink.add('pixel', 'set', 'fullground', 'integer').input(void, size).output(void)
clink.add('pixel', 'set', 'fullground', 'rgb').input(void, size, size, size).output(void)
clink.add('pixel', 'set', 'fullground', 'code').input(void, string).output(void)
clink.add('pixel', 'set', 'background', 'integer').input(void, size).output(void)
clink.add('pixel', 'set', 'background', 'rgb').input(void, size, size, size).output(void)
clink.add('pixel', 'set', 'background', 'code').input(void, string).output(void)
clink.add('pixel', 'set', 'style', 'code').input(void, string).output(void)
clink.add('pixel', 'get', 'wstring').input(void).output(cstring) 
clink.add('pixel', 'log').input(void).output(void)
clink.add('pixel', 'copy').input(void).output(void)
clink.add('pixel', 'no', 'background').input(void).output(bool)
clink.add('pixel', 'copy', 'background').input(void, void).output(void)
clink.add('pixel', 'copy', 'pixel').input(void, void).output(void)
clink.add('pixel', 'fix', 'background').input(void, void).output(void)
clink.add('pixel', 'fix').input(void, void).output(void)

# Add colorize-related functions to link
clink.add('colorize', 'new').input(wstring, void).output(void)
clink.add('colorize', 'delete').input(void).output(void)
clink.add('colorize', 'get', 'length').input(void).output(size)
clink.add('colorize', 'get', 'wstring').input(void, bool).output(cstring)
clink.add('colorize', 'get', 'matrix').input(void).output(void)
clink.add('colorize', 'get', 'pixel').input(void).output(void)
clink.add('colorize', 'set', 'pixel').input(void).output(void)
clink.add('colorize', 'part').input(void, size, size).output(void)
clink.add('colorize', 'print').input(void, bool).output(void)
clink.add('colorize', 'copy').input(void).output(void)
clink.add('colorize', 'copy', 'from').input(void, void).output(void)
clink.add('colorize', 'equals').input(void, void).output(bool)
clink.add('colorize', 'no', 'background').input(void).output(bool)
clink.add('colorize', 'copy', 'background').input(void, void).output(void)
clink.add('colorize', 'fix', 'background').input(void, void).output(void)

# Add matrix-related functions to link
clink.add('matrix', 'new').input(size, size).output(void)
clink.add('matrix', 'clear').input(void).output(void)
clink.add('matrix', 'delete').input().output(void)
clink.add('matrix', 'get', 'width').input(void).output(size)
clink.add('matrix', 'get', 'height').input(void).output(size)
clink.add('matrix', 'vstack').input(void, void, bool).output(void)
clink.add('matrix', 'hstack').input(void, void, bool).output(void)
clink.add('matrix', 'get', 'wstring').input(void, bool).output(cstring)
clink.add('matrix', 'part').input(void, size, size, size, size).output(void)
clink.add('matrix', 'is', 'empty').input(void, size, size, size, size).output(bool)
clink.add('matrix', 'print').input(void, bool).output(void)
clink.add('matrix', 'copy').input(void).output(void)
clink.add('matrix', 'insert', 'matrix').input(void, size, size, void).output(void)
clink.add('matrix', 'insert', 'matrix', 'aligned').input(void, size, size, void, integer, integer).output(void) 
clink.add('matrix', 'insert', 'colorized', 'aligned').input(void, size, size, void, integer, bool).output(bool)
clink.add('matrix', 'insert', 'colorized', 'dynamically').input(void, size, size, void).output(integer)
clink.add('matrix', 'insert', 'wstring').input(void, size, size, wstring).output(void)
clink.add('matrix', 'set', 'wcharacter').input(void, size, size, wchar).output(void)
clink.add('matrix', 'set', 'pixel').input(void, size, size, void).output(void)
#clink.add('matrix', 'insert', 'dots').input(void, void).output(bool)
#clink.add('matrix', 'insert', 'signal').input(void, void).output(void) 
clink.add('matrix', 'insert', 'points').input(void, void).output(void) 

clink.add('matrix', 'fill', 'pixel').input(void, void).output(void) 
clink.add('matrix', 'set', 'wcharacter').input(void, size, size, wchar).output(void) 
clink.add('fast', 'print').input().output(void)

# Add marker-related functions to link
clink.add('marker', 'new', 'normal').input(wchar, void).output(void)
clink.add('marker', 'new', 'type').input(size, void).output(void)

clink.add('marker', 'delete').input().output(void)
clink.add('marker', 'copy').input(void).output(void)
clink.add('marker', 'get', 'wstring').input(void).output(cstring)
clink.add('marker', 'get', 'model').input(void).output(cstring)
clink.add('marker', 'get', 'pixel').input(void).output(void)
clink.add('marker', 'fix').input(void, void).output(void)

# Add point-related functions to link
clink.add('point', 'filled', 'new').input(float, float, void).output(void)
clink.add('point', 'filled', 'get', 'marker').input(void).output(void)
#clink.add('point', 'set', 'fill').input(void, bool, float, float).output(void)
clink.add('point', 'filled', 'delete').input().output(void) 
clink.add('point', 'filled', 'get', 'wstring').input(void, bool).output(cstring) 
clink.add('point', 'filled', 'get', 'col').input(void).output(size) 
clink.add('point', 'filled', 'get', 'row').input(void).output(size) 
clink.add('point', 'filled', 'get', 'x').input(void).output(float) 
clink.add('point', 'filled', 'get', 'y').input(void).output(float) 
clink.add('point', 'filled', 'get', 'marker').input(void).output(void) 
clink.add('point', 'filled', 'get', 'code').input(void).output(size)


# --- Points Creation / Destruction ---
clink.add('points', 'new').input(size).output(void)
clink.add('points', 'delete').input(void).output(void)
clink.add('points', 'clear').input(void).output(void)

# --- Append operations ---
clink.add('points', 'append', 'point').input(void, void).output(void)
clink.add('points', 'append', 'points').input(void, void).output(void)

# --- Getters ---
clink.add('points', 'get', 'point').input(void, size).output(void)
clink.add('points', 'get', 'length').input(void).output(size)

clink.add('points', 'add', 'offset').input(void, size, size).output(void)
clink.add('points', 'select', 'in', 'matrix').input(void, size, size).output(void)
clink.add('points', 'fix', 'background').input(void, void).output(void)

# --- Derived Data ---
clink.add('points', 'squash').input(void).output(void)

# --- Representation ---
clink.add('points', 'log').input(void).output(void)

# --- Copying ---
clink.add('points', 'copy').input(void).output(void)

# Add point-related functions to link
clink.add('points', 'map', 'new').input(size, size).output(void)
clink.add('points', 'map', 'delete').input(void).output(void)
clink.add('points', 'map', 'log').input(void).output(void)
clink.add('points', 'map', 'clear').input(void).output(void)
clink.add('points', 'map', 'get', 'length').input(void).output(size)

# --- Creation / Destruction ---
clink.add('point', 'new', 'marker').input(float, float, void).output(void)
clink.add('point', 'delete').input(void).output(void)

# --- Getters ---
clink.add('point', 'get', 'x').input(void).output(float)
clink.add('point', 'get', 'y').input(void).output(float)

# --- Logging ---
clink.add('point', 'get', 'wstring').input(void).output(cstring) 
clink.add('point', 'log').input(void).output(void)


# --- Signal Creation / Destruction ---
clink.add('signal', 'new').input(size).output(void)
clink.add('signal', 'delete').input(void).output(void)
clink.add('signal', 'clear').input(void).output(void)

# --- Signal Getters ---
clink.add('signal', 'get', 'xside').input(void).output(bool)
clink.add('signal', 'get', 'yside').input(void).output(bool)
clink.add('signal', 'get', 'label').input(void).output(cstring)
clink.add('signal', 'get', 'marker').input(void).output(void)
clink.add('signal', 'get', 'fill', 'method').input(void).output(bool)
clink.add('signal', 'get', 'line', 'method').input(void).output(bool)

# --- Signal Setters ---
clink.add('signal', 'set', 'xside').input(void, bool).output(void)
clink.add('signal', 'set', 'yside').input(void, bool).output(void)
clink.add('signal', 'set', 'label').input(void, wstring).output(void)
clink.add('signal', 'set', 'marker').input(void, void).output(void)
clink.add('signal', 'set', 'fill', 'method').input(void, bool).output(void)
clink.add('signal', 'set', 'line', 'method').input(void, bool).output(void)

# --- Points and Structure ---
clink.add('signal', 'add', 'point').input(void, void).output(void)
clink.add('signal', 'append').input(void, void).output(void)
clink.add('signal', 'set', 'point').input(void, size, float, float, void).output(void)
clink.add('signal', 'set', 'fill', 'point').input(void, size, float, float, void).output(void)
clink.add('signal', 'get', 'point').input(void, size).output(void)
clink.add('signal', 'get', 'fill', 'point').input(void, size).output(void)

# --- Transformations ---
clink.add('signal', 'log', 'x').input(void).output(void)
clink.add('signal', 'log', 'y').input(void).output(void)
clink.add('signal', 'rescale', 'x').input(void, float, float, size, float).output(float)
clink.add('signal', 'rescale', 'y').input(void, float, float, size, float).output(float)
clink.add('signal', 'add', 'offset').input(void, size, size).output(void)
clink.add('signal', 'select', 'in', 'matrix').input(void, size, size).output(void)

# --- Range Queries ---
clink.add('signal', 'get', 'xmin').input(void, float, float).output(float)
clink.add('signal', 'get', 'xmax').input(void, float, float).output(float)
clink.add('signal', 'get', 'ymin').input(void, float, float).output(float)
clink.add('signal', 'get', 'ymax').input(void, float, float).output(float)

# --- Copying / Assignment ---
clink.add('signal', 'copy').input(void).output(void)
clink.add('signal', 'assign').input(void, void).output(void)

# --- Plotting and Rendering ---
clink.add('signal', 'fix', 'background').input(void, void).output(void)
clink.add('signal', 'plot').input(void).output(void)
#clink.add('signal', 'squash').input(void, void).output(void)

# --- Info ---
clink.add('signal', 'get', 'wstring').input(void, bool).output(cstring)
clink.add('signal', 'get', 'length').input(void).output(size)

clink.add('signal', 'get', 'filled', 'points').input(void).output(void)





# Add point-related functions to link
#clink.add('dot', 'new').input(void).output(void)
#clink.add('dot', 'delete').input().output(void)
#clink.add('dot', 'get', 'wstring').input(void).output(cstring)

# Add dots-related functions to link
#clink.add('dots', 'new').input(size).output(void)
#clink.add('dots', 'delete').input(void).output(void)
# clink.add('dots', 'add').input(void, void, void).output(void)
# clink.add('dots', 'get').input(void, size).output(void)
# clink.add('dots', 'get', 'wstring').input(void).output(cstring)
# clink.add('dots', 'get', 'length').input(void).output(size)
# clink.add('dots', 'log').input(void).output(void)
# clink.add('dots', 'add', 'offset').input(void, size, size).output(void)

