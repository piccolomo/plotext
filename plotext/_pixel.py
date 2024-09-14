from ._link import *


class pixel:
    def __init__(self, foreground = None, background = None, style = None, pointer = None):
        self._pointer = pixel_new() if pointer is None else pointer
        self.set(foreground, background, style)

    def __del__(self):
        pixel_delete(self._pointer)

    def set(self, foreground = None, background = None, style = None):
        self._set_foreground(foreground)
        self._set_background(background)
        self._set_style(style)
        return self

    def _set_foreground(self, color = None):
        None if color is None else self._set_foreground_integer(color) if isinstance(color, int) else self._set_foreground_rgb(*color) if isinstance(color, (tuple, list)) else self._set_foreground_code(color)
        return self

    def _set_background(self, color = None):
        None if color is None else self._set_background_integer(color) if isinstance(color, int) else self._set_background_rgb(*color) if isinstance(color, (tuple, list)) else self._set_background_code(color)
        return self

    def _set_style(self, style = None):
        None if style is None else self._set_style_code(style)
        return self

    def _set_foreground_integer(self, r):
        pixel_set_fullground_integer(self._pointer, r)
        return self

    def _set_foreground_rgb(self, r, g, b):
        pixel_set_fullground_rgb(self._pointer, r, g, b)
        return self

    def _set_foreground_code(self, code):
        code = code.encode('utf-8')
        pixel_set_fullground_code(self._pointer, code)
        return self

    def _set_background_integer(self, r):
        pixel_set_background_integer(self._pointer, r)
        return self

    def _set_background_rgb(self, r, g, b):
        pixel_set_background_rgb(self._pointer, r, g, b)
        return self

    def _set_background_code(self, code):
        code = code.encode('utf-8')
        pixel_set_background_code(self._pointer, code)
        return self

    def _set_style_code(self, code):
        code = code.encode('utf-8')
        pixel_set_style_code(self._pointer, code)
        return self

    def _show(self):
        pixel_log(self._pointer)
        return self

    def copy(self):
        return pixel(pointer = pixel_copy(self._pointer))

    def __repr__(self):
        from ._colorize import colorize
        return colorize("Pixel()").set_pixel(self).get_string()



