from plotext._methods import *
from plotext._clink import clink, wstring
from plotext._pixel import pixel


class colorize:
    
    # Initialize colorize object with optional string and pixel styling
    def __init__(self, string = None, foreground = None, background = None, style = None, _pointer = None):
        if _pointer is None:
            string = '' if string is None else str(string)
            px = pixel(foreground, background, style)
            self._pointer = clink.colorize_new(wstring(str(string)), px._pointer)
        else:
            self._pointer = _pointer

    # Cleanup colorize object
    def __del__(self):
        clink.colorize_delete(self._pointer)

    # Set pixel object for this colorize instance
    def set_pixel(self, pixel = None):
        pixel = pixel_class() if pixel is None else pixel
        clink.colorize_set_pixel(self._pointer, pixel._pointer)
        return self

    # Set string content, preserving current pixel style
    def set_string(self, string):
        new = colorize(string).set_pixel(self.get_pixel())
        return self.clone(new)

    # Get length of colorized string
    def get_length(self):
        return clink.colorize_get_length(self._pointer)

    # Get pixel associated with colorize object
    def get_pixel(self):
        return pixel(_pointer = clink.colorize_get_pixel(self._pointer))

    # Get matrix representation of the colorized string
    def get_matrix(self):
        from plotext._matrix import matrix
        return matrix(_pointer = clink.colorize_get_matrix(self._pointer))

    # Retrieve the string; optionally remove colors
    def get_string(self, colorless = False):
        p = clink.colorize_get_wstring(self._pointer, colorless)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Print the colorized string with optional colorless mode
    def print(self, colorless = False, end = '\n', flush = True):
        clink.colorize_print(self._pointer, colorless)
        string_methods.write(end, flush)
        return self

    # Create a copy of this colorize object
    def copy(self):
        return colorize(_pointer = clink.colorize_copy(self._pointer))

    # Get substring of the colorized string
    def _part(self, start, stop):
        return colorize(_pointer = clink.colorize_part(self._pointer, start, stop))

    # Horizontally stack with another string or colorize object
    def hstack(self, colorized, adapt = True):
        #string = colorize(string) if isinstance(string, str) else string
        return self.get_matrix().hstack(colorized.get_matrix(), adapt)

    # Vertically stack with another string or colorize object
    def vstack(self, colorized, adapt = True):
        #string = colorize(string) if isinstance(string, str) else string
        return self.get_matrix().vstack(colorized.get_matrix(), adapt)

    # Clone from another string or colorize object
    def clone(self, colorized):
        #string = colorize(string) if isinstance(string, str) else string
        clink.colorize_copy_from(self._pointer, colorized._pointer)
        return self

    # Check if no background set
    def _no_background(self):
        return clink.colorize_no_background(self._pointer)

    # Copy background from a pixel object
    def _copy_background(self, pixel):
        clink.colorize_copy_background(self._pointer, pixel._pointer)
        return self

    # Fix by copying background from another object
    def _fix_background(self, object):
        clink.colorize_fix_background(self._pointer, object._pointer)
        return self

    # String representation
    def __repr__(self):
        return self.get_string()

    # Horizontal concatenation operator
    def __add__(self, string):
        return self.hstack(string, 1)

    # Vertical concatenation operator
    def __truediv__(self, string):
        return self.vstack(string, 1)

    # Length operator
    def __len__(self):
        return self.get_length()

    # Get item or slice support
    def __getitem__(self, key):
        from plotext._correct import correct_class as correct
        key = correct.slice(key, self.get_length())
        return self._part(key.start, key.stop)

    # Equality comparison
    def __eq__(self, string):
        string = colorize(string) if isinstance(string, str) else string
        return clink.colorize_equals(self._pointer, string._pointer)

    # Copy protocol
    def __copy__(self):
        return self.copy()

    # String cast
    def __str__(self):
        return self.get_string()

    # Hash helper
    def _hash(self):
        return object_methods.hash(self.get_string())