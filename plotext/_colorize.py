from plotext._matrix import * 
from plotext._system import memorize
from plotext._string import space, nl

class colorize(matrix_class):
    def __init__(self, string = '', fullground = None, background = None, style = None):
        pixel = pixel_class()
        pixel.set_fullground_color(fullground)
        pixel.set_background_color(background)
        pixel.set_style(style)

        strings = string.split('\n')
        width = max([len(s) for s in strings]);
        height = len(strings)

        super().__init__(width, height, pixel)
        for i in range(height):
            self.insert_h(0, i, strings[i], pixel)

    def __add__(self, string):
        string = colorize(string) if isinstance(string, str) else string
        height = max(self.rows(), string.rows())
        width = self.cols() + string.cols()
        new = matrix_class(width, height)
        new.insert_m(0, 0, self)
        new.insert_m(self.cols(), 0, string)
        return new

    def append(self, string):
        string = colorize(string) if isinstance(string, str) else string
        height = self.rows() + string.rows()
        width = max(self.cols(), string.cols())
        new = matrix_class(width, height)
        new.insert_m(0, 0, self)
        new.insert_m(0, self.rows(), string)
        return new
