# Axis: single frame axis (one axis / one side), with status, style and pixel

from plotext._primitives.colorize import colorize
from plotext._primitives.matrix import matrix as matrix_class
from plotext._primitives.box import box_class
from plotext._correct import bool as correct_bool
from plotext._correct import pixel as correct_pixel
from plotext._settings import defaults


# Frame axis: one axis (x or y) on one side (lower/upper or left/right)
class axis_class:
    # Initialize axis with axis and side
    def __init__(self, axis = 0, side = 0):
        self.set_axis(axis, side)
        self.set_status().set_style().set_pixel()

    # Set axis and side attributes
    def set_axis(self, axis = 0, side = 0):
        self._axis = axis
        self._side = side
        return self

    # Set status, style, and pixel attributes
    def set(self, status = None, style = None, pixel = None):
        self.set_status(status)
        self.set_style(style) if style is not None else None
        self.set_pixel(pixel) if pixel is not None else None
        return self

    # Clear all settings, pixel and style
    def clear(self):
        self.clear_settings()
        self.clear_pixel()
        self.clear_style()
        return self

    # Reset status to default
    def clear_settings(self):
        self.set_status()
        return self

    # Reset pixel to default axis pixel
    def clear_pixel(self):
        self._pixel.clone(defaults.pixels["axis"])
        return self

    # Reset style to default
    def clear_style(self):
        self.set_style()
        return self

    # Set axis status status
    def set_status(self, status = True):
        status = correct_bool.boolean(status, defaults.axis["status"])
        self._status = status
        return self

    # Set style of axis symbols (line-style int; caller pre-corrects)
    def set_style(self, style = 0):
        self._style = style
        return self

    # Set pixel, default if none provided
    def set_pixel(self, pixel = None, default_pixel = None):
        pixel = correct_pixel.pixel(pixel, defaults.pixels["axis"])
        self._pixel = pixel
        return self

    # Self-contained axis matrix (length×1 for x, 1×length for y) baking axis line + tick stubs + grid crossings. Insert via matrix._insert_matrix.
    def get(self, length, ticks = (), grid_lines = ()):
        out = matrix_class(length, 1, self._pixel) if self._axis == 0 else matrix_class(1, length, self._pixel)         # blank base matrix sized for the axis
        if not self._status:
            return out                                                                                      # disabled axis → empty pixel strip
        if self._axis == 0:                                                                                 # x-axis: row 0
            axis_line = box_class(left = True,            right = True,             pixel = self._pixel, style = self._style)
            tick      = box_class(up = self._side,        down = not self._side,    pixel = self._pixel, style = self._style)   # stub points TOWARD the labels (lower axis → down to bottom labels, upper axis → up to top labels)
            grid      = box_class(up = not self._side,    down = self._side,        pixel = self._pixel, style = self._style)   # stub points TOWARD the canvas (opposite of tick)
            out._add_line(0, axis_line, 0, length)                                                          # paint the line across all cols
            for c in ticks:      out._add_box_marker(c, 0, tick)                                            # tick stamps merge with axis arms → ┴/┬
            for c in grid_lines: out._add_box_marker(c, 0, grid)                                            # grid/line stamps point inward → ┬/┴ (or ┼ if also a tick)
        else:                                                                                               # y-axis: col 0
            axis_line = box_class(up = True,              down = True,              pixel = self._pixel, style = self._style)
            tick      = box_class(left = not self._side,  right = self._side,       pixel = self._pixel, style = self._style)   # stub points TOWARD the labels (left axis → left to its labels, right axis → right to its labels)
            grid      = box_class(left = self._side,      right = not self._side,   pixel = self._pixel, style = self._style)   # stub points TOWARD the canvas (opposite of tick)
            out._add_line(0, axis_line, 0, length)
            for r in ticks:      out._add_box_marker(0, r, tick)                                            # tick stamps → ├/┤
            for r in grid_lines: out._add_box_marker(0, r, grid)                                            # grid/line stamps point inward → ┤/├ (or ┼ if also a tick)
        return out

    # Draw the axis on the matrix at the given position and length, placing a tick mark at each tick position and a crossing at each line one.
    def draw(self, matrix, axis_col, axis_row, axis_length, ticks_positions, lines_positions,
             left_corner_width = 0, right_corner_width = 0):
        matrix._insert_matrix(axis_col, axis_row, self.get(axis_length, ticks_positions, lines_positions))
        if left_corner_width:
            matrix._insert_matrix(0, axis_row, matrix_class(left_corner_width, 1, self._pixel))
        if right_corner_width:
            matrix._insert_matrix(matrix.width() - right_corner_width, axis_row, matrix_class(right_corner_width, 1, self._pixel))
        return self

    # Clone properties from another axis instance
    def clone(self, axis):
        self._axis = axis._axis
        self._side = axis._side
        self._status = axis._status
        self._style = axis._style
        self._pixel.clone(axis._pixel)
        return self

    # Get axis index (0 for x, 1 for y)
    def get_axis(self):
        return self._axis

    # Get side index
    def get_side(self):
        return self._side

    # Get axis status
    def get_status(self):
        return self._status

    # Get axis style
    def get_style(self):
        return self._style

    # Get axis pixel
    def pixel(self):
        return self._pixel

    # Build a compact log line for the axis
    def _get_log(self):
        return f"side {self._side},  {self._status}, style {self._style}, pixel {self._pixel}"

    # Represent axis in Plotext style
    def __repr__(self):
        return "PlotextAxis(" + self._get_log() + ")"
