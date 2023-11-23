from plotext._kernel_link import *


class pixel_class():
    def __init__(self):
        self.pointer = pixel_create()

    def set_marker(self, marker):
        pixel_set_marker(self.pointer, str.encode(marker))
        return self

    def set_fullground_color(self, color = None):
        if isinstance(color, int):
            self.set_fullground_integer(color)
        elif isinstance(color, str):
            color = color_to_integer(color)
            self.set_fullground_integer(color) if color is not None else None
        elif isinstance(color, tuple) and len(color) == 3:
            self.set_fullground_rgb(*color)
        return self

    def set_background_color(self, color = None):
        if isinstance(color, int):
            self.set_background_integer(color)
        elif isinstance(color, str):
            color = color_to_integer(color)
            self.set_background_integer(color) if color is not None else None
        elif isinstance(color, tuple) and len(color) == 3:
            self.set_background_rgb(*color)
        return self

    def set_style(self, styles = None):
        styles = styles.split() if styles is not None else []
        for style in styles:
            if style in style_codes:
                pos = style_codes.index(style)
                self.set_style_integer(pos)
        return self

    def set_fullground_integer(self, i):
        pixel_set_fullground(self.pointer, 1, i, 0, 0)

    def set_fullground_rgb(self, r, g, b):
        pixel_set_fullground(self.pointer, 2, r, g, b)
    
    def set_background_integer(self, i):
        pixel_set_background(self.pointer, 1, i, 0, 0)
        return self

    def set_background_rgb(self, r, g, b):
        pixel_set_background(self.pointer, 2, r, g, b)
        return self
    
    def set_style_integer(self, i):   
        pixel_set_style(self.pointer, i)
        return self

    def log(self):
        pixel_log(self.pointer)

    def show(self):
        pixel_show(self.pointer)

    def __del__(self):
        pixel_destroy(self.pointer)


color_codes = {"black":   0,    "white": 15,
               "gray":    8,    "gray+": 7,
               "red":     1,     "red+": 9,
               "green":   2,   "green+": 10,
               "orange":  3,  "orange+": 11,
               "blue":    4,    "blue+": 12,
               "magenta": 5, "magenta+": 13,
               "cyan":    6,    "cyan+": 14}


style_codes = ["bold", "dim", "italic", "underline", "double-underline", "strike", "inverted", "flash"]


def color_to_integer(color):
    color = color.strip()
    valid = color in color_codes
    return color_codes[color] if valid else None


