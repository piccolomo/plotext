# Matrix primitive: wraps C++ matrix pointer; supports pixels, insertion, stacking and slicing

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring, wchar
from plotext._primitives.pixel import pixel as pixel_class
from plotext._correct.pixel import pixel_par as correct_pixel
from plotext._methods.object import hash as object_hash
from plotext._methods.file import write, _get_extension
from plotext._methods.string import get_page
import plotext._correct.matrix as correct
from plotext._settings import defaults


class matrix:
    # Initialize from size (and optional fill pixel) or from an existing C pointer
    def __init__(self, width, height, pixel = None, _pointer = None):
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
    def width(self):
        return clink.matrix_get_width(self._pointer)

    # Number of rows
    def height(self):
        return clink.matrix_get_height(self._pointer)

    # Return (width, height) tuple
    def size(self):
        return self.width(), self.height()

    # Pixel coloring the character at (row, col), as in matrix.get(0, 0) for the top left one; negative indexes count from the end
    def get(self, row, col):
        row = correct.slice(row, self.height()).start
        col = correct.slice(col, self.width()).start
        return pixel_class(_pointer = clink.matrix_get_pixel(self._pointer, col, row))

    # Apply a pixel to the cell at (col, row)
    def _set_pixel(self, col, row, pixel):
        clink.matrix_set_pixel(self._pointer, col, row, pixel._pointer)
        return self

    # Set both pixel (color) and character at (col, row) in a single call (cell becomes a normal-kind MatrixCharacter holding the wchar + pixel).
    def _set_pixelled_character(self, col, row, char, pixel):
        clink.matrix_set_normal_character(self._pointer, col, row, wchar(char), pixel._pointer)
        return self

    # Stamp a single box marker at (col, row). Builds a Point carrying the marker and dispatches through the general insert(Point) path, Marker::stamp polymorphism does the right thing per marker kind.
    def _add_box_marker(self, col, row, box):
        from plotext._signal.point import point_class
        p = point_class(col, row, box)
        clink.matrix_insert_point(self._pointer, p._pointer, False)
        return self

    # Draw a line along one axis, coord being the fixed one, the row for a horizontal line and the column for a vertical one; with no start and end, it spans the whole matrix.
    def _add_line(self, coord, line, start = None, end = None):
        from plotext._signal.point import point_class
        from plotext._signal.points import points_class
        vertical = line.get_orientation() == 1
        s = 0 if start is None else start
        e = (self.height() if vertical else self.width()) if end is None else end
        n = e - s
        pts = points_class(n)
        for k in range(s, e):
            p = point_class(coord if vertical else k, k if vertical else coord, line)
            clink.points_append_point(pts._pointer, p._pointer)
        clink.matrix_insert_points(self._pointer, pts._pointer)
        return self

    # Insert a matrix, colorize, or raw string at (col, row): ha and va name the item edge anchored to the position, left and top by default, so the item extends right and down
    def insert(self, col, row, item, ha = -1, va = -1):
        ha = correct.ha(ha)
        va = correct.va(va)
        item = correct.matrix(item)
        self._insert_matrix_aligned(col, row, item, ha, va)
        return self

    # Insert another matrix with explicit alignment ints (delegates to clink)
    def _insert_matrix_aligned(self, col, row, obj, ha = -1, va = -1):
        return clink.matrix_insert_matrix(
            self._pointer, col, row, obj._pointer, ha, va)

    # Stamp a single point. Returns True if it fit, False otherwise (out of bounds, no valid alignment, or, with check_space on, cells already taken).
    def _insert_point(self, point, check_space = False):
        return clink.matrix_insert_point(self._pointer, point._pointer, check_space)

    # Insert a points object into the matrix
    def _insert_points(self, points):
        clink.matrix_insert_points(self._pointer, points._pointer)
        return self

    # Insert another matrix into this matrix at (col, row) with default left/top alignment
    def _insert_matrix(self, col, row, obj):
        clink.matrix_insert_matrix(self._pointer, col, row, obj._pointer, -1, -1)
        return self

    # Stack this matrix next to another
    def hstack(self, item, adapt = False):
        item = correct.matrix(item)
        return self.__class__(0, 0, _pointer = clink.matrix_hstack(self._pointer, item._pointer, adapt))

    # Stack this matrix below another matrix, colorize, or raw string
    def vstack(self, item, adapt = False):
        item = correct.matrix(item)
        return self.__class__(0, 0, _pointer = clink.matrix_vstack(self._pointer, item._pointer, adapt))

    # Return a deep copy of the matrix
    def copy(self):
        return self.__class__(0, 0, _pointer = clink.matrix_copy(self._pointer))

    # Copy the contents of another matrix into this one in place
    def clone(self, matrix):
        clink.matrix_clone(self._pointer, matrix._pointer)
        return self

    # Transpose in place (W×H → H×W). Used by vertical-text construction.
    def transpose(self):
        clink.matrix_transpose(self._pointer)
        return self

    # Build the rendered wide string (optionally colorless)
    def string(self, colorless = False):
        p = clink.matrix_get_wstring(self._pointer, colorless)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Build the rendered HTML representation (run-length colored spans inside <pre>)
    def html(self):
        p = clink.matrix_get_html(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Save the matrix to a file, the format following the extension: html gives a web page, ansi keeps the colors as text, anything else gives plain text; colorless forces one or the other, and append adds to the file instead of overwriting it.
    def save(self, path, colorless = None, append = False, log = False):
        ext = _get_extension(path)
        if ext == "html":
            canvas = f"<pre>{self.string(colorless = True)}</pre>" if colorless else self.html()
            canvas = get_page(canvas)
        else:
            cl = (ext != "ansi") if colorless is None else colorless
            canvas = self.string(colorless = cl)
        write(canvas, path, append, log)
        return self

    # Print the matrix to stdout
    def print(self, colorless = False, flush = True):
        clink.matrix_print(self._pointer, colorless, flush)
        return self

    # String representation
    def __str__(self):
        return self.string()

    # Debug representation (same as __str__)
    def __repr__(self):
        return self.string()

    # Horizontal concatenation via +
    def __add__(self, item):
        return self.hstack(item, True)

    # Right-side counterpart for the + operator (e.g. "prefix" + matrix)
    def __radd__(self, item):
        return correct.matrix(item).hstack(self, True)

    # Vertical concatenation via /
    def __truediv__(self, item):
        return self.vstack(item, True)

    # Right-side counterpart for the / operator
    def __rtruediv__(self, item):
        return correct.matrix(item).vstack(self, True)

    # Slicing support: matrix[row, col] returns a sub-matrix
    def __getitem__(self, key):
        width, height = self.width(), self.height()
        key = (key, slice(0, width)) if isinstance(key, (int, slice)) else key
        col_key = correct.slice(key[1], width)
        row_key = correct.slice(key[0], height)
        return self._part(col_key.start, col_key.stop, row_key.start, row_key.stop)

    # Extract a sub-matrix [col_start, col_stop) x [row_start, row_stop)
    def _part(self, col_start, col_stop, row_start, row_stop):
        return self.__class__(0, 0, _pointer = clink.matrix_part(self._pointer, col_start, col_stop, row_start, row_stop))

    # Give every cell the background, the foreground and the style of the pixel, where it carries none of its own
    def _fix(self, pixel):
        clink.matrix_fix(self._pointer, pixel._pointer)
        return self

    # Give every cell the background of the pixel, where it carries none of its own
    def _fix_background(self, pixel):
        clink.matrix_fix_background(self._pointer, pixel._pointer)
        return self

    # Apply `pixel` to every cell, preserving each cell's glyph. Bulk counterpart to the per-cell `_set_pixel(col, row, pixel)`.
    def fill(self, pixel = None):
        pixel = correct_pixel(pixel)
        clink.matrix_apply_pixel(self._pointer, pixel._pointer)
        return self

    # Hash of the rendered string (used by tests)
    def _hash(self):
        return object_hash(self.string())
