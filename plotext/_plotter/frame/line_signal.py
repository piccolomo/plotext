# Line signal: a positioned line — extends primitive `line` with coord, relative flag, label,
# and knows how to render itself onto the canvas matrix using its owning ruler's bounds.

from plotext._primitives.box import line
from plotext._methods import ruler as ruler_methods


class line_signal(line):
    def __init__(self, coord, orientation = 0, relative = False, pixel = None, style = None, label = None):
        super().__init__(orientation, pixel, style)
        self._coord       = coord
        self._orientation = bool(orientation)
        self._relative    = bool(relative)
        self._label       = label
        self._canvas_position = None

    def get_coord(self):           return self._coord
    def get_orientation(self):     return self._orientation
    def is_relative(self):         return self._relative
    def get_label(self):           return self._label
    def get_canvas_position(self): return self._canvas_position

    # Cache the canvas position. relative=True → coord in ruler's data range (rescale via ruler); relative=False → coord already in canvas cells.
    def rescale(self, ruler, bins):
        if self._relative:
            limits = ruler._get_limits(direction = True)
            delta  = ruler._get_delta()
            self._canvas_position = int(ruler_methods.rescale(self._coord, *limits, bins, delta))
        else:
            self._canvas_position = int(self._coord)
        return self

    # Stamp this line onto the canvas matrix at the cached canvas position.
    def draw(self, matrix, canvas_part):
        canvas_col, canvas_row = canvas_part.get_position()
        canvas_width, canvas_height = canvas_part.get_size()
        span = canvas_height if self._orientation else canvas_width
        pos  = self._canvas_position
        if self._orientation:
            matrix.add_line(canvas_col + pos, self, canvas_row, canvas_row + span)
        else:
            matrix.add_line(canvas_row + pos, self, canvas_col, canvas_col + span)
        return self
