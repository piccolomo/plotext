from plotext._pixel import *
from plotext._list import matrix_size, cumulative_sum

class matrix_class():
    def __init__(self, width = None, height = None, pixel = pixel_class()):
        width = width if width is not None else 0
        height = height if height is not None else 0
        self.pointer = matrix_create(width, height, pixel.pointer)

    def insert_h(self, col, row, string, pixel = pixel_class()):
        string = c.c_wchar_p(string)
        matrix_insert_h(self.pointer, col, row, string, pixel.pointer)
        return self

    def insert_v(self, col, row, string, pixel = pixel_class()):
        string = c.c_wchar_p(string)
        matrix_insert_v(self.pointer, col, row, string, pixel.pointer)
        
    def insert_m(self, col, row, matrix):
        matrix_insert_m(self.pointer, col, row, matrix.pointer)

    def insert_d(self, col, row, string, pixel = pixel_class()):
        string = c.c_wchar_p(string)
        return matrix_insert_d(self.pointer, col, row, string, pixel.pointer)

    def check(self, col, row, l):
        return matrix_check(self.pointer, col, row, l)

    def get_string(self, colorless = False):
        p = matrix_get_string(self.pointer, colorless)
        string = c.c_wchar_p.from_buffer(p).value#.decode()
        string_free_memory(p)
        return string

    def rows(self):
        return matrix_rows(self.pointer)
    
    def cols(self):
        return matrix_cols(self.pointer)

    def size(self):
        return [self.cols(), self.rows()]

    def __str__(self):
        return self.get_string()

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(str(self))

    def print(self):
        matrix_show(self.pointer)

    def __del__(self):
        matrix_destroy(self.pointer)

        
def join_matrices(matrices):
    cols, rows = matrix_size(matrices); Rows = range(rows); Cols = range(cols)
    w = [matrices[0][col].cols() for col in Cols]
    h = [matrices[row][0].rows() for row in Rows]
    cw = [0] + cumulative_sum(w)
    ch = [0] + cumulative_sum(h)
    new = matrix_class(sum(w), sum(h))
    for row in Rows:
        for col in Cols:
            new.insert_m(cw[col], ch[row], matrices[row][col])
    return new 
