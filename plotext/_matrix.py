from plotext._placement import placement
from plotext._placement import placement
from plotext._pixel import *
from plotext._system import write
from copy import copy


class matrix_class():
    def __init__(self, width = None, height = None, marker = None, fullground = None, background = None):
        width = width if width is not None else 0
        height = height if height is not None else 0
        pixel = pixel_class(marker, fullground, background)
        self._pointer = matrix_create(width, height, pixel._pointer)

    def __del__(self):
        matrix_destroy(self._pointer)

    def fill(self, marker = None, background = None):
        pixel = pixel_class().set_marker(marker).set_background(background)
        matrix_fill(self._pointer, pixel._pointer)
        return self

    def _insert_pixel(self, col, row, pixel):
        matrix_insert_pixel(self._pointer, col, row, pixel._pointer)
        return self

    def _insert_matrix(self, col, row, matrix):
        matrix_insert_matrix(self._pointer, col, row, matrix._pointer)

    def _insert_aligned(self, col, row, matrix, ha = 'left', va = 'top', check_spaces = False):
        ha = placement.get_horizontal_alignment_index(ha) - 1
        va = placement.get_vertical_alignment_index(va) - 1
        return matrix_insert_aligned(self._pointer, col, row, matrix._pointer, ha, va, check_spaces)

    def _insert_dynamic(self, col, row, matrix):
        return matrix_insert_dynamic(self._pointer, col, row, matrix._pointer)

    def _insert_matrices(self, x, y, matrices):
        Length = list(range(len(x)))
        [self._insert_matrix(x[i], y[i], matrices[i]) for i in Length]

    def _hstack(self, matrix):
        new = matrix_class(0, 0);
        new._pointer = matrix_hstack(self._pointer, matrix._pointer)
        return new
    
    def _vstack(self, matrix):
        new = matrix_class(0, 0)
        new._pointer = matrix_vstack(self._pointer, matrix._pointer)
        return new

    def _hstack2(self, matrix):
        width = self._get_width() + matrix._get_width()
        height = self._get_height() 
        new = matrix_class(width, height)
        new._insert_matrix(0, 0, self)
        new._insert_matrix(self._get_width(), 0, matrix)
        return new

    def _vstack2(self, matrix):
        width = self._get_width()
        height = self._get_height() + matrix._get_height()
        new = matrix_class(width, height)
        new._insert_matrix(0, 0, self)
        new._insert_matrix(0, self._get_height(), matrix)
        return new

    def _transpose(self):
        new = matrix_class(0, 0)
        new._pointer = matrix_transpose(self._pointer)
        return new

    def __add__(self, matrix):
        width = self._get_width() + matrix._get_width()
        height = max(self._get_height(), matrix._get_height())
        new = matrix_class(width, height)
        new._insert_matrix(0, 0, self)
        new._insert_matrix(self._get_width(), 0, matrix)
        return new

    def __truediv__(self, k):
        height = self._get_height() 
        out = matrix_class(self._get_width(), height * k)
        for i in range(k):
            out._insert_matrix(0, height * i, self)
        return out

    def __mul__(self, k):
        width = self._get_width() 
        out = matrix_class(width * k, self._get_height())
        for i in range(k):
            out._insert_matrix(width * i, 0, self)
        return out

    
    def _clear(self):
        matrix_clear(self._pointer)
        return self

    def _get_height(self):
        return matrix_height(self._pointer)
    
    def _get_width(self):
        return matrix_width(self._pointer)

    def _get_size(self):
        return [self._get_width(), self._get_height()]

    def __len__(self):
        return len(str(self))
    
    def _select(self, col, row, cols, rows):
        new = matrix_class(0, 0)
        matrix_assign(new._pointer, matrix_part(self._pointer, col, row, cols, rows))
        return new

    def _part(self, start, end):
        return self._select(0, start, self._get_width(), end - start)

    def _get_pixel(self, col, row):
        pointer = matrix_get_pixel(self._pointer, col, row)
        new = pixel_class()
        pixel_assign(new._pointer, pointer)
        pixel_destroy(pointer)
        return new

    def _copy(self):
        new = matrix_class(0, 0)
        matrix_assign(new._pointer, self._pointer)
        return new

    def _copy_from(self, matrix):
        matrix_assign(self._pointer, matrix._pointer)

    def _resize(self, width, height, background = None):
        p = pixel_class().set_background(background)
        matrix_resize(self._pointer, width, height, p._pointer)
        return self
        
    def _reset(self, width, height, background = None):
        new = matrix_class(width, height, background = background) 
        self._copy_from(new)
        return self

    def _get_string(self, colorless = False):
        p = matrix_get_string(self._pointer, colorless)
        string = c.c_wchar_p.from_buffer(p).value#.decode()
        string_free_memory(p)
        return string

    def __str__(self):
        return self._get_string()

    def __repr__(self):
        return str(self)

    def _print(self):
        write(self._get_string())

    def _print2(self):
        matrix_show(self._pointer)        



