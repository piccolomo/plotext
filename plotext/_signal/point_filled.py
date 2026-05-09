# PointFilled: single filled data point with x/y/col/row, marker and foreground color, backed by the C kernel

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring
from plotext._primitives.marker import marker as marker_class


# Filled point: x/y/col/row with a marker and an integer foreground color
class point_filled_class:
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
    def get_x(self):
        return clink.point_filled_get_x(self._pointer)

    # Get y coordinate
    def get_y(self):
        return clink.point_filled_get_y(self._pointer)

    # Get column
    def get_col(self):
        return clink.point_filled_get_col(self._pointer)

    # Get row
    def get_row(self):
        return clink.point_filled_get_row(self._pointer)

    # Get marker object
    def get_marker(self):
        return marker_class(_pointer=clink.point_filled_get_marker(self._pointer))

    # Whether the point has an explicit fill marker
    def has_fill(self):
        return clink.point_filled_has_fill(self._pointer)

    # Foreground palette indices: main marker always, fill marker only when the point has one
    def get_foreground_integer_codes(self):
        codes = [clink.point_filled_get_main_foreground_integer_code(self._pointer)]
        if self.has_fill():
            codes.append(clink.point_filled_get_fill_foreground_integer_code(self._pointer))
        return codes

    # Get string representation (delegated to C)
    def get_string(self, fill=True):
        p = clink.point_filled_get_wstring(self._pointer, fill)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # String representation
    def __repr__(self):
        return f"Plotext PointFilled: " + self.get_string()
