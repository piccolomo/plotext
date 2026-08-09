# Points: container of data points backed by the C kernel; supports appending, offsetting, selection and squashing

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring


# Container of data points with batch C-backed operations
class points_class:
    # Initialize from a size or an existing C pointer
    def __init__(self, n = 0, _pointer = None):
        self._pointer = clink.points_new(n) if _pointer is None else _pointer

    # Release the C pointer on deletion
    def __del__(self):
        clink.points_delete(self._pointer)
        self._pointer = None

    # Clear all points
    def clear(self):
        clink.points_clear(self._pointer)
        return self

    # Append another points container
    def append(self, other):
        clink.points_append_points(self._pointer, other._pointer)
        return self

    # Fix background against a pixel
    def fix_background(self, pixel):
        clink.points_fix_background(self._pointer, pixel._pointer)
        return self

    # Offset all points by (x_offset, y_offset)
    def add_offset(self, x_offset, y_offset):
        clink.points_add_offset(self._pointer, x_offset, y_offset)
        return self

    # Keep only points within a matrix of the given size
    def select_in_matrix(self, w, h):
        clink.points_select_in_matrix(self._pointer, w, h)
        return self

    # Squash points through the given grid
    def squash(self, grid):
        return clink.points_squash(self._pointer, grid._pointer)

    # Get number of points
    def length(self):
        return clink.points_get_length(self._pointer)

    # Get range for iteration
    def get_range(self):
        return range(self.length())

    # Log to stdout via the C kernel
    def log(self):
        clink.points_log(self._pointer)
        return self

    # Create a copy
    def copy(self):
        return points_class(_pointer = clink.points_copy(self._pointer))

    # Representation
    def __repr__(self):
        return f"PlotextPoints({self.length()})"
