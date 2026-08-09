# BoxStyle primitive: thin wrapper around C++ BoxStyle (style + pixel; no arms, no active flag).

from plotext._kernel.clink import clink
from plotext._primitives.pixel import pixel as pixel_class
from plotext._correct import enums as correct_line


class box_style_class:
    # style + pixel; or pass _pointer to wrap an existing C-side BoxStyle.
    def __init__(self, style = None, pixel = None, _pointer = None):
        self._pointer = _pointer if _pointer is not None else clink.box_style_new(
            correct_line.line_style(style),
            (pixel if pixel is not None else pixel_class())._pointer)

    def __del__(self):
        if self._pointer is not None:
            clink.box_style_delete(self._pointer)
            self._pointer = None

    def get_style(self):
        return int(clink.box_style_get_style(self._pointer))

    def set_style(self, style):
        clink.box_style_set_style(self._pointer, correct_line.line_style(style))
        return self

    def pixel(self):
        return pixel_class(_pointer = clink.box_style_get_pixel(self._pointer))

    def set_pixel(self, pixel):
        clink.box_style_set_pixel(self._pointer, pixel._pointer)
        return self
