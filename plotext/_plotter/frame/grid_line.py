# Grid line: ruler-local box_style + active flag.

from plotext._primitives.box_style import box_style_class


class grid_line_class(box_style_class):
    # style + pixel (inherited) + active flag (Python-side, not in C++)
    def __init__(self, style = None, pixel = None, active = False):
        super().__init__(style = style, pixel = pixel)
        self._active = bool(active)

    def is_active(self):
        return self._active

    def set_active(self, active):
        self._active = bool(active)
        return self

    def _get_log(self):
        return f"active {self._active}, style {self.get_style()}, pixel {self.pixel()}"
