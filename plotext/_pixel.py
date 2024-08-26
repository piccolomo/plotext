from ._link import *


class pixel_class:
    def __init__(self):
        self._pointer = pixel_new()

    def __del__(self):
        pixel_delete(self._pointer)

    def set_fullground(self, color = None):
        None if color is None else self.set_fullground_integer(color) if isinstance(color, int) else self.set_fullground_rgb(*color) if isinstance(color, (tuple, list)) else self.set_fullground_code(color)
        return self

    def set_background(self, color = None):
        None if color is None else self.set_background_integer(color) if isinstance(color, int) else self.set_background_rgb(*color) if isinstance(color, (tuple, list)) else self.set_background_code(color)
        return self

    def set_style(self, style = None):
        None if style is None else self.set_style_code(style)
        return self

    def set_fullground_integer(self, r):
        pixel_set_fullground_integer(self._pointer, r)
        return self

    def set_fullground_rgb(self, r, g, b):
        pixel_set_fullground_rgb(self._pointer, r, g, b)
        return self

    def set_fullground_code(self, code):
        code = code.encode('utf-8')
        pixel_set_fullground_code(self._pointer, code)
        return self

    def set_background_integer(self, r):
        pixel_set_background_integer(self._pointer, r)
        return self

    def set_background_rgb(self, r, g, b):
        pixel_set_background_rgb(self._pointer, r, g, b)
        return self

    def set_background_code(self, code):
        code = code.encode('utf-8')
        pixel_set_background_code(self._pointer, code)
        return self

    def set_style_code(self, code):
        code = code.encode('utf-8')
        pixel_set_style_code(self._pointer, code)
        return self

    def log(self):
        pixel_log(self._pointer)
        return self

    def __add__(self, matrix):
        self.hstack(matrix)
        return matrix



white_pixel = pixel_class().set_background_code("white")


