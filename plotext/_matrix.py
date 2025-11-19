from plotext._pixel import pixel as pixel_class
from plotext._correct import correct_class as correct
from plotext._methods.string import write
from plotext._clink import clink, wchar, wstring
# from plotext._methods import object_methods  # hash, write


class matrix:

    # Initialize a matrix with optional pixel and pointer
    def __init__(self, width = 0, height = 0, pixel = None, _pointer = None):
        px = pixel_class(background = "white") if pixel is None else pixel
        self._pointer = clink.matrix_new(width, height, px._pointer) if _pointer is None else _pointer

    # Delete the matrix (free memory)
    def __del__(self):
        clink.matrix_delete(self._pointer)

    # Clear the content of the matrix
    def clear(self):
        clink.matrix_clear(self._pointer)
        return self

    # Get dimensions
    def get_width(self):
        return clink.matrix_get_width(self._pointer)

    def get_height(self):
        return clink.matrix_get_height(self._pointer)

    def get_size(self):
        return self.get_width(), self.get_height()

    # Set a character at a specific position
    def _set_character(self, col, row, char):
        clink.matrix_set_wcharacter(self._pointer, col, row, wchar(char))
        return self

    # Set a pixel at a specific position
    def _set_pixel(self, col, row, pixel):
        clink.matrix_set_pixel(self._pointer, col, row, pixel._pointer)
        return self

    # Set both character and pixel at a position
    def _set_pixelled_character(self, col, row, char, pixel):
        self._set_character(col, row, char)
        self._set_pixel(col, row, pixel)
        return self

    # Insert a matrix-like object with alignment
    def insert(self, col, row, matrix, ha = -1, va = 1):
        ha = correct.ha(ha)
        va = correct.va(va)
        matrix = correct.matrix(matrix)
        return self._insert_matrix_aligned(col, row, matrix, ha, va)

    # Insert another matrix directly
    def _insert_matrix(self, col, row, object):
        clink.matrix_insert_matrix(self._pointer, col, row, object._pointer)
        return self

    # Insert a matrix with alignment
    def _insert_matrix_aligned(self, col, row, object, ha = -1, va = -1):
        va *= -1
        return clink.matrix_insert_matrix_aligned(self._pointer, col, row, object._pointer, ha, va)

    # Insert a colorized label with alignment
    def _insert_colorized_aligned(self, col, row, label, ha = -1, check_space = 1, change_color = True):
        return clink.matrix_insert_colorized_aligned(self._pointer, col, row, label._pointer, ha, check_space, change_color)

    # Insert a colorized label dynamically
    def _insert_colorized_dynamically(self, col, row, label):
        return clink.matrix_insert_colorized_dynamically(self._pointer, col, row, label._pointer)

    def _insert_points(self, points):
        clink.matrix_insert_points(self._pointer, points._pointer)

    # Vertical and horizontal stacking
    def vstack(self, matrix, adapt = False):
        return self.__class__(_pointer = clink.matrix_vstack(self._pointer, matrix._pointer, adapt))

    def hstack(self, matrix, adapt = False):
        return self.__class__(_pointer = clink.matrix_hstack(self._pointer, matrix._pointer, adapt))

    # Create and return a copy of this matrix
    def copy(self):
        return self.__class__(_pointer = clink.matrix_copy(self._pointer))

    # Get the matrix as a string
    def get_string(self, colorless = False):
        p = clink.matrix_get_wstring(self._pointer, colorless)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Print the matrix to terminal
    def print(self, colorless = False, end = '\n', flush = True):
        clink.matrix_print(self._pointer, colorless)
        write(end, flush)
        return self

    # String representations
    def __str__(self):
        return self.get_string()

    def __repr__(self):
        return self.get_string()

    def _hash(self):
        return object_methods.hash(self.get_string())

    # Operators for stacking
    def __truediv__(self, object):
        return self.vstack(object, 1)

    def __add__(self, object):
        return self.hstack(object, 1)

    # Slice access
    def __getitem__(self, key):
        width, height = self.get_width(), self.get_height()
        key = (key, slice(0, width)) if isinstance(key, int) or isinstance(key, slice) else key
        col_key = correct.slice(key[1], width)
        row_key = correct.slice(key[0], height)
        return self._part(col_key.start, col_key.stop, row_key.start, row_key.stop)

    def _part(self, col_start, col_stop, row_start, row_stop):
        return self.__class__(_pointer = clink.matrix_part(self._pointer, col_start, col_stop, row_start, row_stop))


# Combine a 2D list (matrix) of matrix objects into a single larger matrix
def join_matrices(matrices):
    if not matrices or not matrices[0]:
        return matrix(0, 0)

    rows, cols = len(matrices), len(matrices[0])
    widths = [m.get_width() for m in matrices[0]]
    heights = [matrices[r][0].get_height() for r in range(rows)]

    total_width = sum(widths)
    total_height = sum(heights)

    M = matrix(total_width, total_height)

    for r in range(rows):
        y_offset = sum(heights[:r])
        for c in range(cols):
            x_offset = sum(widths[:c])
            M._insert_matrix(x_offset, y_offset, matrices[r][c])

    return M