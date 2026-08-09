# Line signal: a line with a position on its ruler, a label and a way to draw itself on the canvas, using the limits of the ruler it belongs to.

from plotext._primitives.box import line
from plotext._methods import ruler as ruler_methods


class line_signal(line):
    def __init__(self, position, orientation = 0, relative = False, pixel = None, style = None, label = None):
        super().__init__(orientation, pixel, style)
        self._position    = position
        self._orientation = bool(orientation)
        self._relative    = bool(relative)
        self._label       = label
        self._canvas_position = None

    def get_position(self):        return self._position
    def get_orientation(self):     return self._orientation
    def is_relative(self):         return self._relative
    def get_label(self):           return self._label
    def get_canvas_position(self): return self._canvas_position

    # Cache the canvas position. relative=True → position in ruler's data range (rescale via ruler); relative=False → position already in canvas cells.
    def rescale(self, ruler, bins):
        if self._relative:
            limits = ruler._get_limits(direction = True)
            delta  = ruler._get_delta()
            self._canvas_position = int(ruler_methods.rescale(self._position, *limits, bins, delta))
        else:
            self._canvas_position = int(self._position)
        return self

    # Stamp this line onto the canvas matrix at the cached canvas position.
    def draw(self, matrix, canvas_part):
        canvas_col, canvas_row = canvas_part.position()
        canvas_width, canvas_height = canvas_part.size()
        span = canvas_height if self._orientation else canvas_width
        pos  = self._canvas_position
        if self._orientation:
            matrix._add_line(canvas_col + pos, self, canvas_row, canvas_row + span)
        else:
            matrix._add_line(canvas_row + pos, self, canvas_col, canvas_col + span)
        return self
