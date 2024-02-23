from plotext._matrix import * 
from plotext._hd_marker import hd_marker_codes
from plotext._marker import marker_codes


class colorize(matrix_class):
    def __init__(self, string = '', fullground = None, background = None, style = None, correct_marker = True):

        strings = self._get_strings(string, correct_marker = correct_marker)
        width, height = self._get_strings_size(strings)
        super().__init__(width, height)

        self._pixel = pixel_class(None, fullground, background, style)
        
        [self._insert_string(0, i, strings[i], self._pixel) for i in range(height)]

        
    def _get_strings(self, string, correct_marker = True):
        string = self._correct_marker(string) if correct_marker else string
        strings = string.split('\n')
        return strings

    def _get_strings_size(self, strings):
        width = max([len(s) for s in strings])
        height = len(strings)
        return width, height

    def _reset_string(self, string, correct_marker = True):
        strings = self._get_strings(string, correct_marker = correct_marker)
        width, height = self._get_strings_size(strings)
        self._resize(width, height)
        [self._insert_string(0, i, strings[i], self._pixel) for i in range(height)]
        return self


    def _correct_marker(self, marker):
        return marker if marker in hd_marker_codes else marker_codes[marker] if marker in marker_codes.keys() else marker

    def resolution(self, product = True):
        string = self.get_string(1)
        return hd_marker_codes[string].resolution(product) if string in hd_marker_codes else (1 if product else (1, 1))
        

    def is_hd(self):
        return self.resolution() != (1, 1)
         
    def __del__(self):
        #self._pixel.__del__()
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
        new = colorize()
        new._pixel.copy_from(self._pixel)
        new._reset_string(self.get_string(True))
        return new

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


