# Corner: one of the four frame corners (lower-left, lower-right, upper-left, upper-right) with its tick symbol

from plotext._primitives.matrix import matrix
from plotext._primitives.box import box_class


# Frame corner: holds alignment, size, style, axis/ticks pixels and produces the corner matrix
class corner_class:
    # Initialize alignment, size, style and pixels
    def __init__(self, vertical = 0, horizontal = 0):
        self.set_alignment(vertical, horizontal)
        self.set_size()
        self.set_style()
        self.set_pixels()

    # Set vertical/horizontal alignment
    def set_alignment(self, vertical = 0, horizontal = 0):
        self._vertical = vertical
        self._horizontal = horizontal
        return self

    # Set corner width and height
    def set_size(self, width = 0, height = 0):
        self._width = width
        self._height = height
        return self

    # Set corner style (line-style int; caller pre-corrects)
    def set_style(self, style = 0):
        self._style = style
        return self

    # Set axis and ticks pixels
    def set_pixels(self, axis = None, ticks = None):
        self._axis_pixel = axis
        self._ticks_pixel = ticks
        return self

    # Check if corner is the lower-left one
    def is_lower_left(self):
        return not self._vertical and not self._horizontal

    # Check if corner is the lower-right one
    def is_lower_right(self):
        return not self._vertical and self._horizontal

    # Check if corner is the upper-left one
    def is_upper_left(self):
        return self._vertical and not self._horizontal

    # Check if corner is the upper-right one
    def is_upper_right(self):
        return self._vertical and self._horizontal

    # Row at which the tick symbol is placed
    def get_tick_row(self):
        return 0 if not self._vertical else self._height - 1

    # Column at which the tick symbol is placed
    def get_tick_col(self):
        return 0 if self._horizontal else self._width - 1

    # Line marker for this corner, arms set by alignment (up=not vertical, down=vertical, left=horizontal, right=not horizontal).
    def get_tick_marker(self):
        return box_class(up = not self._vertical, down = self._vertical, left = self._horizontal, right = not self._horizontal, pixel = self._axis_pixel, style = self._style)

    # Rendered glyph string for the corner tick.
    def get_tick_string(self):
        return self.get_tick_marker()._get_string()

    # Build the corner matrix with the tick line marker stamped in the correct cell.
    def get(self):
        out = matrix(self._width, self._height, self._ticks_pixel)
        out._add_box_marker(self.get_tick_col(), self.get_tick_row(), self.get_tick_marker())
        return out

    # Configure pixels/style/size and stamp the corner matrix at (corner_col, corner_row).
    def draw(self, matrix, corner_col, corner_row, corner_width, corner_height, axis_pixel, axis_style, ticks_pixel):
        self.set_pixels(axis_pixel, ticks_pixel).set_style(axis_style).set_size(corner_width, corner_height)
        matrix._insert_matrix(corner_col, corner_row, self.get())
        return self

    # Build a compact log line for the corner
    def _get_log(self):
        return (
            f"vertical {self._vertical}, horizontal {self._horizontal}, "
            f"width {self._width}, height {self._height}, "
            f"ticks pixel {self._ticks_pixel}, "
            f"axis pixel {self._axis_pixel}, "
            f"style {self._style}, "
            f"tick {self.get_tick_string()}"
            )

    # Represent corner in Plotext style
    def __repr__(self):
        return "PlotextCorner(" + self._get_log() + ")"
