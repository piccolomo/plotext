# Point: single (x, y) position with a marker, backed by the C kernel. Thin wrapper around the C++ Point class.

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring
from plotext._primitives.marker import marker as marker_class
from plotext._primitives.box import box_class


# Plain point: x/y with a marker. Used wherever you need to stamp one marker at one location through Matrix::insert(Point&).
class point_class:
    # Initialize from (x, y, marker) or an existing C pointer. marker may be marker_class, box_class (or line subclass), or anything coercible to marker_class, each of these wraps a C++ Marker*.
    def __init__(self, x = 0, y = 0, marker = None, _pointer = None):
        if marker is None:                                      marker = marker_class()
        elif not isinstance(marker, (marker_class, box_class)): marker = marker_class(marker)
        self._pointer = clink.point_new_marker(x, y, marker._pointer) if _pointer is None else _pointer

    # Release the C pointer on deletion
    def __del__(self):
        if self._pointer is not None:
            clink.point_delete(self._pointer)
            self._pointer = None

    # Get x coordinate
    def get_x(self):
        return clink.point_get_x(self._pointer)

    # Get y coordinate
    def get_y(self):
        return clink.point_get_y(self._pointer)

    # Get string representation (delegated to C)
    def string(self):
        p = clink.point_get_wstring(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # String representation
    def __repr__(self):
        return "PlotextPoint(" + self.string() + ")"
