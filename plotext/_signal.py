from plotext._clink import clink, wstring
from plotext._point import point_filled_class
from plotext._constants import inf
from plotext._marker import marker
from plotext._methods.list import unique
from plotext._correct import correct_class as correct
from plotext._points import points_class


class signal_class:
    def __init__(self, length = None, _pointer = None):
        self._pointer = clink.signal_new(length) if _pointer is None else _pointer
        self._lines = False

    def __del__(self):
        clink.signal_delete(self._pointer)
        self._pointer = None

    # --- Basic flags ---
    def set_lines(self, lines = False):
        self._lines = lines
        return self

    def get_lines(self):
        return self._lines

    # --- Clear ---
    def clear(self):
        clink.signal_clear(self._pointer)
        return self

    # --- Sides ---
    def get_xside(self):
        return clink.signal_get_xside(self._pointer)

    def set_xside(self, value):
        clink.signal_set_xside(self._pointer, value)
        return self

    def get_yside(self):
        return clink.signal_get_yside(self._pointer)

    def set_yside(self, value):
        clink.signal_set_yside(self._pointer, value)
        return self

    # --- Labels ---
    def get_label(self):
        p = clink.signal_get_label(self._pointer)
        out = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return out

    def set_label(self, label):
        clink.signal_set_label(self._pointer, wstring(label))
        return self

    # --- Marker ---
    def get_marker(self):
        return marker(_pointer = clink.signal_get_marker(self._pointer))

    def set_marker(self, m):
        clink.signal_set_marker(self._pointer, m._pointer)
        return self

    # --- Methods ---
    def get_fill_method(self):
        return clink.signal_get_fill_method(self._pointer)

    def set_fill_method(self, method):
        clink.signal_set_fill_method(self._pointer, correct.line_method(method))
        return self

    def get_line_method(self):
        return clink.signal_get_line_method(self._pointer)

    def set_line_method(self, method):
        clink.signal_set_line_method(self._pointer, correct.line_method(method))
        return self

    # --- Points (simple API) ---
    def add_point(self, p):
        clink.signal_add_point(self._pointer, p._pointer)
        return self

    def set_point(self, index, x, y, m):
        clink.signal_set_point(self._pointer, index, x, y, m._pointer)
        return self

    def set_points(self, x=None, y=None, m=None): 
        [self.add_point(point_filled_class(x[i], y[i], m[i])) for i in range(len(x))]
        return self 

    def set_fill_point(self, index, x, y, m):
        clink.signal_set_fill_point(self._pointer, index, x, y, m._pointer)
        return self

    def set_fill(self, signal):
        for i in signal.get_range():
            point = signal.get_point(i)
            x, y, m = point.get_x(), point.get_y(), point.get_marker()
            self.set_fill_point(i, x, y, m)
        return self

    def get_point(self, index):
        return point_filled_class(_pointer = clink.signal_get_point(self._pointer, index))

    # --- Length & iteration ---
    def get_length(self):
        return clink.signal_get_length(self._pointer)

    def get_range(self):
        return range(self.get_length())

    def __iter__(self):
        return (self.get_point(i) for i in self.get_range())

    # --- X/Y extraction (Python side only) ---
    def get_x(self):
        return [p.get_x() for p in self]

    def get_y(self):
        return [p.get_y() for p in self]

    # --- Bounds ---
    def get_xmin(self, ymin = None, ymax = None):
        return clink.signal_get_xmin(self._pointer, -inf if ymin is None else ymin, inf if ymax is None else ymax)

    def get_xmax(self, ymin = None, ymax = None):
        return clink.signal_get_xmax(self._pointer, -inf if ymin is None else ymin, inf if ymax is None else ymax)

    def get_xlimits(self, ymin = None, ymax = None):
        return self.get_xmin(ymin, ymax), self.get_xmax(ymin, ymax)

    def get_ymin(self, xmin = None, xmax = None):
        return clink.signal_get_ymin(self._pointer, -inf if xmin is None else xmin, inf if xmax is None else xmax)

    def get_ymax(self, xmin = None, xmax = None):
        return clink.signal_get_ymax(self._pointer, -inf if xmin is None else xmin, inf if xmax is None else xmax)

    def get_ylimits(self, xmin = None, xmax = None):
        return self.get_ymin(xmin, xmax), self.get_ymax(xmin, xmax)

    # --- Colors ---
    def get_foreground_unique_integer_colors(self):
        return unique([p.get_foreground_integer_color() for p in self])

    # --- Geometry + matrix selection ---
    def select_in_matrix(self, w, h):
        clink.signal_select_in_matrix(self._pointer, w, h)
        return self

    def fix_background(self, pixel):
        clink.signal_fix_background(self._pointer, pixel._pointer)
        return self

    def add_offset(self, dx, dy):
        clink.signal_add_offset(self._pointer, dx, dy)
        return self

    # --- Combine & squash ---
    def append(self, other):
        clink.signal_append(self._pointer, other._pointer)
        return self

    def plot(self): 
        clink.signal_plot(self._pointer) 
        return self

    def get_filled_points(self): 
        return points_class(_pointer = clink.signal_get_filled_points(self._pointer))

    def squash(self, points_map):
        clink.signal_squash(self._pointer, points_map._pointer)
        return self

    # --- Log scaling ---
    def log_x(self):
        clink.signal_log_x(self._pointer)
        return self

    def log_y(self):
        clink.signal_log_y(self._pointer)
        return self

    # --- Rescaling ---
    def rescale_x(self, limits, width, delta):
        clink.signal_rescale_x(self._pointer, limits[0], limits[1], width, delta)
        return self

    def rescale_y(self, limits, height, delta):
        clink.signal_rescale_y(self._pointer, limits[0], limits[1], height, delta)
        return self

    # --- Copying ---
    def copy(self):
        out = signal_class(_pointer = clink.signal_copy(self._pointer))
        out._lines = self._lines
        return out

    def copy_from(self, points):
        clink.signal_assign(self._pointer, points._pointer)
        return self

    # --- Logging ---
    def get_log(self, fill = False):
        p = clink.signal_get_wstring(self._pointer, fill)
        out = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return out

    def log(self, fill = False):
        print(self.get_log(fill))
        return self

    def __repr__(self):
        return self.get_log()
