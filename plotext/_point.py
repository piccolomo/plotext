from plotext._clink import clink, wstring
from plotext._marker import marker as marker_class


class point_filled_class:
    def __init__(self, x = 0, y = 0, marker = None, _pointer = None):
        marker = marker_class() if marker is None else marker
        self._pointer = clink.point_filled_new(x, y, marker._pointer) if _pointer is None else _pointer

    def __del__(self):
        clink.point_filled_delete(self._pointer)

    # Coordinates
    def get_x(self):
        return clink.point_filled_get_x(self._pointer)

    def get_y(self):
        return clink.point_filled_get_y(self._pointer)

    def get_col(self):
        return clink.point_filled_get_col(self._pointer)

    def get_row(self):
        return clink.point_filled_get_row(self._pointer)

    # Marker
    def get_marker(self):
        return marker_class(_pointer = clink.point_filled_get_marker(self._pointer))

    # Foreground color code
    def get_foreground_integer_color(self):
        return clink.point_filled_get_code(self._pointer)

    # String representation
    def get_string(self, fill = True):
        p = clink.point_filled_get_wstring(self._pointer, fill)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    def __repr__(self):
        return self.get_string(True)

    # Print and return self
    def log(self, fill = True):
        print(self.get_string(fill))
        return self


class point_class:
    def __init__(self, x = 0, y = 0, marker = None, _pointer = None):
        marker = marker_class() if marker is None else marker
        self._pointer = clink.point_filled_new(x, y, marker._pointer) if _pointer is None else _pointer

    def __del__(self):
        clink.point_delete(self._pointer)
        self._pointer = None

    # Coordinates
    def get_x(self):
        return clink.point_get_x(self._pointer)

    def get_y(self):
        return clink.point_get_y(self._pointer)

    # String representation
    def get_string(self):
        p = clink.point_get_wstring(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    def __repr__(self):
        return self.get_string()

    def log(self):
        print(self.get_string())
        return self
