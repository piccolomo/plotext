from plotext._matrix import * 
from plotext._marker import space, nl

class colorize(matrix_class):
    def __init__(self, string = '', fullground = None, background = None, style = None):
        strings = string.split('\n')
        width = max([len(s) for s in strings])
        height = len(strings)
        super().__init__(width, height)

        pixel = pixel_class()
        pixel.set_fullground(fullground)
        pixel.set_background(background)
        pixel.set_style(style)
        
        [self._insert_string(0, i, strings[i], pixel) for i in range(height)]

    def __del__(self):
        matrix_class.__del__(self)

    def _insert_string(self, col, row, string, pixel = pixel_class()):
        string = c.c_wchar_p(string)
        matrix_insert_string(self._pointer, col, row, string, pixel._pointer)
        return self

    def _insert_marker(self, col, row, marker, fullground = None, background = None):
        pixel = pixel_class(marker, fullground, background)
        return self._insert_pixel(col, row, pixel)

    def clear(self):
        return self._clear()

    def part(self, start, end):
        return self._part(start, end)

    def copy(self):
        return self._copy()

    def resize(self, width, height):
        return self._resize(width, height)

    def print(self):
        self._print()

    def __add__(self, string):
        string = string if isinstance(string, colorize) else colorize(string)
        return super().__add__(string)

    def vstack(self, matrix):
        height = self._get_height() + matrix._get_height()
        width = max(self._get_width(), matrix._get_width())
        new = matrix_class(width, height)
        new._insert_matrix(0, 0, self)
        new._insert_matrix(0, self._get_height(), matrix)
        return new
