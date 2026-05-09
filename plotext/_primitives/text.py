# Text primitive: wraps a C++ Text pointer; a Colorize anchored at (x, y) with alignment, orientation, axis sides and relative placement

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring
from plotext._primitives.colorize import colorize as colorize_class


class text:
    # Initialize text with raw types: caller is responsible for validation (see draw.text)
    def __init__(self, x = 0, y = 0, colorized = None, alignment = -1, orientation = 0, xside = 0, yside = 0, relative = False, _pointer = None):
        colorized = colorize_class() if colorized is None else colorized
        self._pointer = clink.text_new(float(x), float(y), colorized._pointer, orientation, alignment) if _pointer is None else _pointer
        self._xside = xside
        self._yside = yside
        self._relative = relative

    # Release the C text pointer on deletion
    def __del__(self):
        if self._pointer is not None:
            clink.text_delete(self._pointer)
            self._pointer = None

    # Deep copy of the text (independent C pointer + same Python-side attributes)
    def copy(self):
        return text(_pointer = clink.text_copy(self._pointer), xside = self._xside, yside = self._yside, relative = self._relative)

    # Set the (x, y) anchor position
    def _set_position(self, x, y):
        clink.text_set_position(self._pointer, float(x), float(y))
        return self

    # Set alignment along the writing direction (-1 left, 0 center, 1 right)
    def _set_alignment(self, value):
        clink.text_set_alignment(self._pointer, value)
        return self

    # Set orientation (0 horizontal, 1 vertical)
    def _set_orientation(self, value):
        clink.text_set_orientation(self._pointer, value)
        return self

    # Set the x-axis side
    def _set_xside(self, value):
        self._xside = value
        return self

    # Set the y-axis side
    def _set_yside(self, value):
        self._yside = value
        return self

    # Set the relative flag (True = canvas coords, False = data coords)
    def _set_relative(self, value):
        self._relative = value
        return self

    # Rescale the x coordinate from data space to canvas cell columns
    def _rescale_x(self, limits, width, delta):
        clink.text_rescale_x(self._pointer, limits[0], limits[1], width, delta)
        return self

    # Rescale the y coordinate from data space to canvas cell rows
    def _rescale_y(self, limits, height, delta):
        clink.text_rescale_y(self._pointer, limits[0], limits[1], height, delta)
        return self

    # Copy background from the given pixel only when no background is set
    def _fix_background(self, pixel):
        clink.text_fix_background(self._pointer, pixel._pointer)
        return self

    # Get the x coordinate
    def _get_x(self):
        return clink.text_get_x(self._pointer)

    # Get the y coordinate
    def _get_y(self):
        return clink.text_get_y(self._pointer)

    # Get the alignment as an integer (-1 left, 0 center, 1 right)
    def _get_alignment(self):
        return clink.text_get_alignment(self._pointer)

    # Get the orientation as an integer (0 horizontal, 1 vertical)
    def _get_orientation(self):
        return clink.text_get_orientation(self._pointer)

    # Get the x-axis side
    def _get_xside(self):
        return self._xside

    # Get the y-axis side
    def _get_yside(self):
        return self._yside

    # True if the text is in absolute canvas coordinates rather than data coordinates
    def _is_relative(self):
        return self._relative

    # Render this text onto the canvas region of matrix using the owning x/y rulers.
    def draw(self, matrix, xruler, yruler, canvas_part):
        canvas_col, canvas_row = canvas_part.get_position()
        canvas_width, canvas_height = canvas_part.get_size()
        t = self.copy()
        if t._is_relative():
            t._set_position(t._get_x() + canvas_col, t._get_y() + canvas_row)
        else:
            t._rescale_x(xruler._get_limits(direction = True), canvas_width, xruler._get_delta())
            t._rescale_y(yruler._get_limits(direction = True), canvas_height, yruler._get_delta())
            t._set_position(t._get_x() + canvas_col, t._get_y() + canvas_row)
        matrix._insert_text(t, check_space = False)
        return self

    # Wide-string summary built by the C++ Text::get_wstring (coords, colorize, alignment, orientation)
    def _get_log(self):
        p = clink.text_get_wstring(self._pointer)
        out = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return out + f", xside={self._xside}, yside={self._yside}, relative={self._relative}"

    def __repr__(self):
        return self._get_log()
