# Colorized string object with pixel-based styling and matrix operations

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring
from plotext._primitives.pixel import pixel
from plotext._correct.pixel import pixel_par as correct_pixel
from plotext._methods.string import write


class colorize:
    # Initialize colorize object with optional string and pixel styling
    def __init__(self, string = None, pixel = None, _pointer = None):
        if _pointer is None:
            string = '' if string is None else str(string)
            px = correct_pixel(pixel)
            self._pointer = clink.colorize_new(wstring(str(string)), px._pointer)
        else:
            self._pointer = _pointer

    # Cleanup colorize object
    def __del__(self):
        clink.colorize_delete(self._pointer)

    # Apply `pixel` to every character, preserving each glyph
    def fill(self, pixel = None):
        pixel = correct_pixel(pixel)
        clink.colorize_set_pixel(self._pointer, pixel._pointer)
        return self

    # Replace the string content, preserving the current pixel.
    def write(self, string):
        new = colorize(string).fill(self.pixel())
        return self.clone(new)

    # Uppercase the colorize string in place, preserving the pixel.
    def upper(self):
        return self.write(self.string(colorless = True).upper())

    # Uppercase the colorize string in place, preserving the pixel.
    def lower(self):
        return self.write(self.string(colorless = True).lower())

    # Title-case the colorize string in place, preserving the pixel.
    def title(self):
        return self.write(self.string(colorless = True).title())

    # Get length of colorized string
    def length(self):
        return clink.colorize_get_length(self._pointer)

    # Get pixel associated with colorize object
    def pixel(self):
        return pixel(_pointer = clink.colorize_get_pixel(self._pointer))

    # Get matrix representation of colorized string
    def matrix(self):
        from plotext._primitives.matrix import matrix
        return matrix(0, 0, _pointer = clink.colorize_get_matrix(self._pointer))

    # Retrieve string optionally without colors
    def string(self, colorless = False):
        p = clink.colorize_get_wstring(self._pointer, colorless)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Print colorized string with optional flush
    def print(self, colorless = False, flush = False):
        clink.colorize_print(self._pointer, colorless, flush)
        return self

    # Create a copy of this colorize object
    def copy(self):
        return colorize(_pointer = clink.colorize_copy(self._pointer))

    # Get substring of colorized string
    def _part(self, start, stop):
        return colorize(_pointer = clink.colorize_part(self._pointer, start, stop))

    # Horizontally stack with another colorized object; returns a matrix
    def hstack(self, item, adapt = True):
        return self.matrix().hstack(item, adapt)

    # Vertically stack with another colorize, matrix, or raw string; returns a matrix
    def vstack(self, item, adapt = True):
        return self.matrix().vstack(item, adapt)

    # Clone from another colorized object
    def clone(self, colorized):
        clink.colorize_clone(self._pointer, colorized._pointer)
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
        return self.string()

    # Horizontal concatenation
    def __add__(self, item):
        return self.hstack(item, 1)

    # Right-side counterpart for the + operator (e.g. "prefix" + colorize)
    def __radd__(self, item):
        return colorize(item).hstack(self, 1)

    # Vertical concatenation
    def __truediv__(self, item):
        return self.vstack(item, 1)

    # Right-side counterpart for the / operator
    def __rtruediv__(self, item):
        return colorize(item).vstack(self, 1)

    # Length operator
    def __len__(self):
        return self.length()

    # Indexing and slicing support
    def __getitem__(self, key):
        from plotext._correct import matrix as correct_matrix
        key = correct_matrix.slice(key, self.length())
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
        return self.string()

    # Hash helper
    def _hash(self):
        return object_methods.hash(self.string())


# The value as a colorize object, a plain string taking the given pixel when one is passed; it lives here, and not in the _correct folder, to avoid importing that folder from this one.
def correct_colorized(colorized, default_pixel = None):
    if isinstance(colorized, str):
        c = colorize(colorized)
        if default_pixel is not None:
            c.fill(default_pixel)
        return c
    return colorized