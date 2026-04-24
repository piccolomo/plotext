# Matrix primitive: wraps C++ matrix pointer; supports pixels, insertion, stacking and slicing

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring, wchar
from plotext._primitives.pixel import pixel as pixel_class
from plotext._methods.string import write
from plotext._methods.object import hash as object_hash
import plotext._correct.matrix as correct
from plotext._settings import defaults


class matrix:
    # Initialize from size (and optional fill pixel) or from an existing C pointer
    def __init__(self, width = 0, height = 0, pixel = None, _pointer = None):
        pixel_pointer = defaults.pixels["matrix"]._pointer if pixel is None else pixel._pointer
        self._pointer = clink.matrix_new(width, height, pixel_pointer) if _pointer is None else _pointer

    # Release the C matrix pointer on deletion
    def __del__(self):
        if self._pointer is not None:
            clink.matrix_delete(self._pointer)
            self._pointer = None

    # Clear every cell of the matrix
    def clear(self):
        clink.matrix_clear(self._pointer)
        return self

    # Number of columns
    def get_width(self):
        return clink.matrix_get_width(self._pointer)

    # Number of rows
    def get_height(self):
        return clink.matrix_get_height(self._pointer)

    # Return (width, height) tuple
    def get_size(self):
        return self.get_width(), self.get_height()

    # Write a single character at (col, row)
    def _set_character(self, col, row, char):
        clink.matrix_set_wcharacter(self._pointer, col, row, wchar(char))
        return self

    # Apply a pixel to the cell at (col, row)
    def _set_pixel(self, col, row, pixel):
        clink.matrix_set_pixel(self._pointer, col, row, pixel._pointer)
        return self

    # Set both pixel (color) and character at (col, row)
    def _set_pixelled_character(self, col, row, char, pixel):
        self._set_pixel(col, row, pixel)
        self._set_character(col, row, char)
        return self

    # Insert a matrix, colorize, or raw string at (col, row) with horizontal/vertical alignment
    def insert(self, col, row, matrix, ha=-1, va=1):
        ha = correct.ha(ha)
        va = correct.va(va)
        matrix = correct.matrix(matrix)
        return self._insert_matrix_aligned(col, row, matrix, ha, va)

    # Insert another matrix with explicit alignment ints (delegates to clink)
    def _insert_matrix_aligned(self, col, row, obj, ha=-1, va=-1):
        return clink.matrix_insert_matrix_aligned(
            self._pointer, col, row, obj._pointer, ha, -va)

    # Insert a points object into the matrix
    def _insert_points(self, points):
        clink.matrix_insert_points(self._pointer, points._pointer)
        return self

    # Insert another matrix into this matrix at (col, row)
    def _insert_matrix(self, col, row, obj):
        clink.matrix_insert_matrix(self._pointer, col, row, obj._pointer)
        return self

    # Insert a colorized object into the matrix with horizontal alignment
    def _insert_colorized_aligned(self, col, row, colorized, ha = -1, check_space = False):
        return clink.matrix_insert_colorized_aligned(self._pointer, col, row, colorized._pointer, ha, check_space)

    # Insert a colorized object dynamically at (col, row); returns an integer status
    def _insert_colorized_dynamically(self, col, row, colorized):
        return clink.matrix_insert_colorized_dynamically(self._pointer, col, row, colorized._pointer)

    # Stack this matrix next to another
    def hstack(self, other, adapt=False):
        other = correct.matrix(other)
        return self.__class__(_pointer=clink.matrix_hstack(self._pointer, other._pointer, adapt))

    # Stack this matrix below another
    def vstack(self, other, adapt=False):
        other = correct.matrix(other)
        return self.__class__(_pointer=clink.matrix_vstack(self._pointer, other._pointer, adapt))

    # Return a deep copy of the matrix
    def copy(self):
        return self.__class__(_pointer=clink.matrix_copy(self._pointer))

    # Build the rendered wide string (optionally colorless)
    def get_string(self, colorless=False):
        p = clink.matrix_get_wstring(self._pointer, colorless)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Print the matrix to stdout
    def print(self, colorless = False, flush = True):
        clink.matrix_print(self._pointer, colorless, flush)
        return self

    # String representation
    def __str__(self):
        return self.get_string()

    # Debug representation (same as __str__)
    def __repr__(self):
        return self.get_string()

    # Horizontal concatenation via +
    def __add__(self, other):
        return self.hstack(other, True)

    # Vertical concatenation via /
    def __truediv__(self, other):
        return self.vstack(other, True)

    # Slicing support: matrix[row, col] returns a sub-matrix
    def __getitem__(self, key):
        width, height = self.get_width(), self.get_height()
        key = (key, slice(0, width)) if isinstance(key, (int, slice)) else key
        col_key = correct.slice(key[1], width)
        row_key = correct.slice(key[0], height)
        return self._part(col_key.start, col_key.stop, row_key.start, row_key.stop)

    # Extract a sub-matrix [col_start, col_stop) x [row_start, row_stop)
    def _part(self, col_start, col_stop, row_start, row_stop):
        return self.__class__(_pointer=clink.matrix_part(self._pointer, col_start, col_stop, row_start, row_stop))

    # Hash of the rendered string (used by tests)
    def _hash(self):
        return object_hash(self.get_string())
