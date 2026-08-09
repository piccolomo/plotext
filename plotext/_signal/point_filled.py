# PointFilled: single filled data point with x/y/col/row, marker and foreground color, backed by the C kernel

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring
from plotext._primitives.marker import marker as marker_class
from plotext._primitives.pixel import pixel as pixel_class


# Filled point: x/y/col/row with a marker and an integer foreground color
class point:
    # Initialize from (x, y, marker) or an existing C pointer
    def __init__(self, x = 0, y = 0, marker = None, _pointer = None):
        marker = marker_class() if marker is None else marker if isinstance(marker, marker_class) else marker_class(marker)
        self._pointer = clink.point_filled_new(x, y, marker._pointer) if _pointer is None else _pointer

    # Release the C pointer on deletion
    def __del__(self):
        if self._pointer is not None:
            clink.point_filled_delete(self._pointer)
            self._pointer = None

    # Get x coordinate
    def x(self):
        return clink.point_filled_get_x(self._pointer)

    # Get y coordinate
    def y(self):
        return clink.point_filled_get_y(self._pointer)

    # Get marker object
    def marker(self):
        return marker_class(_pointer = clink.point_filled_get_marker(self._pointer))

    # Whether the point has an explicit fill marker
    def _has_fill(self):
        return clink.point_filled_has_fill(self._pointer)

    # Pixels in use: main marker always, fill marker only when the point has one
    def _get_pixels(self):
        pixels = [pixel_class(_pointer = clink.point_filled_get_main_pixel(self._pointer))]
        if self._has_fill():
            pixels.append(pixel_class(_pointer = clink.point_filled_get_fill_pixel(self._pointer)))
        return pixels

    # Get string representation (delegated to C)
    def _get_string(self):
        p = clink.point_filled_get_wstring(self._pointer, True)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # String representation
    def __repr__(self):
        return "PlotextPoint(" + self._get_string() + ")"
