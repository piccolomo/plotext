# Colorized string object with pixel-based styling and matrix operations

from plotext._kernel.clink import clink 
from plotext._kernel.tools import wstring 
from plotext._primitives.pixel import pixel 
from plotext._methods.string import write 


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
    def set_pixel(self, pixel=None):
        pixel = pixel_class() if pixel is None else pixel
        clink.colorize_set_pixel(self._pointer, pixel._pointer)
        return self

    # Set string content preserving current pixel style
    def set_string(self, string):
        new = colorize(string).set_pixel(self.get_pixel())
        return self.clone(new)

    # Return a new colorize with the same pixel and the string uppercased.
    def upper(self):
        return self.copy().set_string(self.get_string(colorless = True).upper())

    # Return a new colorize with the same pixel and the string lowercased.
    def lower(self):
        return self.copy().set_string(self.get_string(colorless = True).lower())

    # Return a new colorize with the same pixel and the string title-cased.
    def title(self):
        return self.copy().set_string(self.get_string(colorless = True).title())

    # Get length of colorized string
    def get_length(self):
        return clink.colorize_get_length(self._pointer)

    # Get pixel associated with colorize object
    def get_pixel(self):
        return pixel(_pointer=clink.colorize_get_pixel(self._pointer))

    # Get matrix representation of colorized string
    def get_matrix(self):
        from plotext._primitives.matrix import matrix
        return matrix(_pointer=clink.colorize_get_matrix(self._pointer))

    # Retrieve string optionally without colors
    def get_string(self, colorless=False):
        p = clink.colorize_get_wstring(self._pointer, colorless)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Print colorized string with optional flush
    def print(self, colorless=False, flush=False):
        clink.colorize_print(self._pointer, colorless, flush)
        return self

    # Create a copy of this colorize object
    def copy(self):
        return colorize(_pointer=clink.colorize_copy(self._pointer))

    # Get substring of colorized string
    def _part(self, start, stop):
        return colorize(_pointer=clink.colorize_part(self._pointer, start, stop))

    # Horizontally stack with another colorized object; returns a matrix
    def hstack(self, colorized, adapt=True):
        colorized = correct_colorized(colorized)
        return self.get_matrix().hstack(colorized.get_matrix(), adapt)

    # Vertically stack with another colorized object; returns a matrix
    def vstack(self, colorized, adapt=True):
        colorized = correct_colorized(colorized)
        return self.get_matrix().vstack(colorized.get_matrix(), adapt)

    # Clone from another colorized object
    def clone(self, colorized):
        clink.colorize_copy_from(self._pointer, colorized._pointer)
        return self

    # Check if no background is set
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

    # Fix both unset foreground and background from another pixel/colorize
    def _fix(self, object):
        clink.colorize_fix(self._pointer, object._pointer)
        return self

    # String representation
    def __repr__(self):
        return self.get_string()

    # Horizontal concatenation
    def __add__(self, string):
        return self.hstack(string, 1)

    # Vertical concatenation
    def __truediv__(self, string):
        return self.vstack(string, 1)

    # Length operator
    def __len__(self):
        return self.get_length()

    # Indexing and slicing support
    def __getitem__(self, key):
        from plotext._correct import matrix as correct_matrix
        key = correct_matrix.slice(key, self.get_length())
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


# Ensure input is a colorize object (kept local to _primitives/colorize.py to avoid a circular import with _correct).
# When default_pixel is provided and the input is a bare string, the resulting colorize gets that pixel applied.
def correct_colorized(colorized, default_pixel = None):
    if isinstance(colorized, str):
        c = colorize(colorized)
        if default_pixel is not None:
            c.set_pixel(default_pixel)
        return c
    return colorized