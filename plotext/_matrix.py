from plotext._default import default_placement as dp
from plotext._default import get_horizontal_alignment_index
from plotext._pixel import *
from plotext._system import write


class matrix_class():
    def __init__(self, width = None, height = None, pixel = pixel_class()):
        width = width if width is not None else 0
        height = height if height is not None else 0
        self.pointer = matrix_create(width, height, pixel.pointer)

    def fill(self, pixel = pixel_class()):
        matrix_fill(self.pointer, pixel.pointer)

    def insert_h(self, col, row, string, pixel = pixel_class()):
        string = c.c_wchar_p(string)
        matrix_insert_h(self.pointer, col, row, string, pixel.pointer)
        return self

    def insert_v(self, col, row, string, pixel = pixel_class()):
        string = c.c_wchar_p(string)
        matrix_insert_v(self.pointer, col, row, string, pixel.pointer)
        
    def insert_m(self, col, row, matrix, horizontal_alignment = "left", vertical_alignment = "top", check_space = False):
        col = self.align_col(col, matrix.cols(), horizontal_alignment)
        check = True if not check_space else self.check_matrix(col, row, matrix)
        matrix_insert_m(self.pointer, col, row, matrix.pointer) if check else None

    def insert_d(self, col, row, string, pixel = pixel_class()):
        string = c.c_wchar_p(string)
        return matrix_insert_d(self.pointer, col, row, string, pixel.pointer)

    def align_col(self, col, length, horizontal_alignement):
        integer_alignment = get_horizontal_alignment_index(horizontal_alignement)
        delta = [0, - length // 2 , - length + 1]
        return col + delta[integer_alignment]

    def check_matrix(self, col, row, matrix):
        cols, rows = matrix.size()
        res = cols <= self.cols() and rows <= self.rows() and self.check(col, row, cols, rows)
        res = res if col == 0 else res and self.check(col - 1, row, 1, rows)
        res = res if col == self.cols() - cols else res and self.check(col + cols, row, 1, rows)
        return res

    def check(self, col, row, cols, rows):
        return matrix_check(self.pointer, col, row, cols, rows)

    def rows(self):
        return matrix_rows(self.pointer)
    
    def cols(self):
        return matrix_cols(self.pointer)

    def size(self):
        return [self.cols(), self.rows()]

    def print(self):
        write(self.get_string())

    def print2(self):
        matrix_show(self.pointer)
        
    def get_string(self, colorless = False):
        p = matrix_get_string(self.pointer, colorless)
        string = c.c_wchar_p.from_buffer(p).value#.decode()
        string_free_memory(p)
        return string

    def __str__(self):
        return self.get_string()

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(str(self))

    def __del__(self):
        matrix_destroy(self.pointer)

    def clear(self):
        matrix_clear(self.pointer)
        return self

    def copy(self):
        new = matrix_class()
        new.pointer = matrix_copy(self.pointer)

    def part(self, start, end):
        new = matrix_class()
        new.pointer = matrix_part(self.pointer, start, end)
        return new
