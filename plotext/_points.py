from plotext._clink import clink, wstring
from plotext._point import point_class


class points_class:
    # Initialize points with new or existing pointer
    def __init__(self, length = 10, pointer = None):
        self._pointer = clink.points_new(length) if pointer is None else pointer

    # Clean up pointer on deletion
    def __del__(self): clink.points_delete(self._pointer); self._pointer = None

    # Clear all points
    def clear(self): clink.points_clear(self._pointer)

    # Get point by index
    def get(self, index): return point_class(pointer = clink.points_get(self._pointer, index))

    # Get number of points
    def get_length(self): return clink.points_get_length(self._pointer)

    # Get range of valid indices
    def get_range(self): return range(self.get_length())

    # Get min and max x-values
    def get_xmin(self): return clink.points_get_xmin(self._pointer)
    def get_xmax(self): return clink.points_get_xmax(self._pointer)
    def get_xlimits(self): return (self.get_xmin(), self.get_xmax())

    # Get min and max y-values
    def get_ymin(self): return clink.points_get_ymin(self._pointer)
    def get_ymax(self): return clink.points_get_ymax(self._pointer)
    def get_ylimits(self): return (self.get_ymin(), self.get_ymax())

    # Fix background pixel for points
    def fix_background(self, pixel):
        clink.points_fix_background(self._pointer, pixel._pointer)
        return self

    # Add a point
    def add(self, point):
        clink.points_add(self._pointer, point._pointer)
        return self

    # Set a fill point at index
    def set_fill_point(self, index, point):
        clink.points_set_fill_point(self._pointer, index, point._pointer)
        return self

    # Log x-values
    def log_x(self):
        clink.points_log_x(self._pointer)
        return self

    # Log y-values
    def log_y(self):
        clink.points_log_y(self._pointer)
        return self

    # Rescale x-values with given limits and width
    def rescale_x(self, limits, width, delta):
        clink.points_rescale_x(self._pointer, *limits, width, delta)

    # Rescale y-values with given limits and height
    def rescale_y(self, limits, height, delta):
        clink.points_rescale_y(self._pointer, *limits, height, delta)

    # Add offset to all points
    def add_offset(self, dx, dy):
        clink.points_add_offset(self._pointer, dx, dy)

    # Fill points from another source (unused return, kept for API)
    def fill(self):
        points_class(pointer = clink.points_fill(self._pointer))
        return self

    # Copy points instance
    def copy(self):
        return points_class(pointer = clink.points_copy(self._pointer))

    # Copy data from another points instance
    def copy_from(self, points):
        return clink.points_assign(self._pointer, points._pointer)

    # Get string representation
    def get_string(self):
        p = clink.points_get_wstring(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Print points string representation
    def print(self):
        print(self.get_string())
        return self

    # Iterator over points
    def __iter__(self):
        return (self.get(i) for i in self.get_range())
