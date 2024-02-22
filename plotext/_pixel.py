from plotext._link import *
from plotext._color import *
from plotext._style import *

class pixel_class():
    def __init__(self, marker = None, fullground = None, background = None, style = None):
        self._pointer = pixel_create()
        self.set_marker(marker)
        self.set_fullground(fullground)
        self.set_background(background)
        self.set_style(style)

    def __del__(self):
        pixel_destroy(self._pointer)

    def set_marker(self, marker):
        #str.encode(marker)
        pixel_set_marker(self._pointer, c.c_wchar(marker)) if marker is not None else None
        return self

    def set_fullground(self, color = None):
        if isinstance(color, int):
            self.set_fullground_integer(color)
        elif isinstance(color, str):
            color = color_to_integer(color)
            self.set_fullground_integer(color) if color is not None else None
        elif isinstance(color, tuple) and len(color) == 3:
            self.set_fullground_rgb(*color)
        return self

    def set_background(self, color = None):
        if isinstance(color, int):
            self.set_background_integer(color)
        elif isinstance(color, str):
            color = color_to_integer(color)
            self.set_background_integer(color) if color is not None else None
        elif isinstance(color, tuple) and len(color) == 3:
            self.set_background_rgb(*color)
        return self

    def set_style(self, styles = None):
        [self.set_style_integer(index) for index in styles_to_integers(styles)]
        return self

    def set_fullground_integer(self, i):
        pixel_set_fullground(self._pointer, 1, i, 0, 0)

    def set_fullground_rgb(self, r, g, b):
        pixel_set_fullground(self._pointer, 2, r, g, b)
    
    def set_background_integer(self, i):
        pixel_set_background(self._pointer, 1, i, 0, 0)

    def set_background_rgb(self, r, g, b):
        pixel_set_background(self._pointer, 2, r, g, b)
    
    def set_style_integer(self, i):   
        pixel_set_style(self._pointer, i)

    def log(self):
        pixel_log(self._pointer)

    def get_string(self):
        p = pixel_get_string(self._pointer)
        string = c.c_wchar_p.from_buffer(p).value#.decode()
        string_free_memory(p)
        return string

    def print(self):
        print(self)

    def __repr__(self):
        return self.get_string()

    def copy(self):
        new = pixel_class(0, 0)
        return new.copy_from(self)

    def copy_from(self, pixel):
        pixel_assign(self._pointer, pixel._pointer)
        return self
