from plotext._clink import clink, wstring
from plotext._point import point_class


class points_class:
    def __init__(self, n = 0, _pointer = None):
        self._pointer = clink.points_new(n) if _pointer is None else _pointer

    def __del__(self):
        clink.points_delete(self._pointer)
        self._pointer = None

    # --- Management ---
    def clear(self):
        clink.points_clear(self._pointer)
        return self

    def copy(self):
        return points_class(_pointer = clink.points_copy(self._pointer))

    # --- Append operations ---
    def append_point(self, point):
        clink.points_append_point(self._pointer, point._pointer)
        return self

    def append_points(self, other):
        clink.points_append_points(self._pointer, other._pointer)
        return self

    # --- Getters ---
    def get_point(self, index):
        return point_class(_pointer = clink.points_get_point(self._pointer, index))

    def get_length(self):
        return clink.points_get_length(self._pointer)

    def get_range(self): 
        return range(self.get_length())

    def get_x(self):
        return [p.get_x() for p in self]

    def get_y(self):
        return [p.get_y() for p in self]

    # --- Background and transformations ---
    def fix_background(self, pixel):
        clink.points_fix_background(self._pointer, pixel._pointer)
        return self

    def add_offset(self, x_offset, y_offset):
        clink.points_add_offset(self._pointer, x_offset, y_offset)
        return self

    def select_in_matrix(self, w, h):
        clink.points_select_in_matrix(self._pointer, w, h)
        return self

    # --- Derived Data ---
    def squash(self, map):
        return clink.points_squash(self._pointer, map._pointer)

    # --- Representation ---
    def get_wstring(self):
        return clink.points_get_wstring(self._pointer)

    def log(self):
        clink.points_log(self._pointer)
        return self

    # --- Iteration ---
    def __iter__(self):
        return (self.get_point(i) for i in self.get_range())