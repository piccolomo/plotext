# Matrix primitive: wraps C++ matrix pointer; supports pixels, insertion, stacking and slicing

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring, wchar
from plotext._primitives.pixel import pixel as pixel_class
from plotext._methods.string import write
from plotext._methods.object import hash as object_hash
from plotext._methods.file import write, _get_extension
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

    # Apply a pixel to the cell at (col, row)
    def _set_pixel(self, col, row, pixel):
        clink.matrix_set_pixel(self._pointer, col, row, pixel._pointer)
        return self

    # Set both pixel (color) and character at (col, row) in a single call (cell becomes a normal-kind MatrixCharacter holding the wchar + pixel).
    def _set_pixelled_character(self, col, row, char, pixel):
        clink.matrix_set_normal_character(self._pointer, col, row, wchar(char), pixel._pointer)
        return self

    # Stamp a single box marker at (col, row). Caller is responsible for keeping (col, row) in bounds.
    def add_box_marker(self, col, row, box):
        clink.matrix_add_box_marker(self._pointer, col, row, box._pointer)
        return self

    # Stamp a line spanning [start, end) along the variable axis. coord is the FIXED axis (row for horizontal lines, col for vertical). start/end default to the matrix bounds. Single FFI call — the loop runs in C++.
    def add_line(self, coord, line, start=None, end=None):
        vertical = line.get_orientation() == 1
        s = 0 if start is None else start
        e = (self.get_height() if vertical else self.get_width()) if end is None else end
        clink.matrix_add_line(self._pointer, coord, line._pointer, s, e, vertical)
        return self

    # Insert a matrix, colorize, or raw string at (col, row) with horizontal/vertical alignment
    def insert(self, col, row, matrix, ha=-1, va=1):
        ha = correct.ha(ha)
        va = correct.va(va)
        matrix = correct.matrix(matrix)
        return self._insert_matrix_aligned(col, row, matrix, ha, va)

    # Insert another matrix with explicit alignment ints (delegates to clink)
    def _insert_matrix_aligned(self, col, row, obj, ha=-1, va=-1):
        return clink.matrix_insert_matrix(
            self._pointer, col, row, obj._pointer, ha, -va)

    # Insert a points object into the matrix
    def _insert_points(self, points):
        clink.matrix_insert_points(self._pointer, points._pointer)
        return self

    # Insert another matrix into this matrix at (col, row) with default left/top alignment
    def _insert_matrix(self, col, row, obj):
        clink.matrix_insert_matrix(self._pointer, col, row, obj._pointer, -1, -1)
        return self

    # Insert a Text into the matrix at its own (x, y), respecting its alignment and orientation.
    # check_space defaults to True so overflow strings are skipped instead of
    # writing past matrix bounds (which segfaults the C++ kernel). Pass
    # check_space=False to opt into the unchecked write.
    def _insert_text(self, text, check_space = True, change_color = True):
        return clink.matrix_insert_text(self._pointer, text._pointer, check_space, change_color)

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

    # Build the rendered HTML representation (run-length colored spans inside <pre>)
    def get_html(self):
        p = clink.matrix_get_html(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Save the matrix to disk. Extension-driven: "html" → HTML via get_html(), "ansi" → colored text, anything else → plain colorless text. append=True appends.
    def save(self, path, append=False):
        ext = _get_extension(path)
        canvas = self.get_html() if ext == "html" else self.get_string(colorless=(ext != "ansi"))
        write(canvas, path, append)
        return self

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

    # Apply `pixel`'s background to every cell that doesn't already have one (per-cell forward to Pixel::fix_background in C++).
    def _fix_background(self, pixel):
        clink.matrix_fix_background(self._pointer, pixel._pointer)
        return self

    # Apply `pixel` to every cell, preserving each cell's glyph. Bulk counterpart to the per-cell `_set_pixel(col, row, pixel)`.
    def set_pixel(self, pixel):
        clink.matrix_apply_pixel(self._pointer, pixel._pointer)
        return self

    # Hash of the rendered string (used by tests)
    def _hash(self):
        return object_hash(self.get_string())
