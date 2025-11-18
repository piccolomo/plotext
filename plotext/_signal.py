from plotext._clink import clink, wstring
from plotext._point import point_filled_class 
from plotext._constants import inf  # Axis side constants
from plotext._marker import marker
from plotext._methods.list import unique
from plotext._correct import correct_class as correct
from plotext._points import points_class


class signal_class:
    # Initialize points with new or existing pointer
    def __init__(self, length=None, _pointer=None): 
        self._pointer = clink.signal_new(length) if _pointer is None else _pointer 

    # Clean up pointer on deletion
    def __del__(self): 
        clink.signal_delete(self._pointer)
        self._pointer = None

    def set_lines(self, lines=False): 
        self._lines = lines

    def get_lines(self): 
        return self._lines

    # --- NEW: Clear all points ---
    def clear(self): 
        clink.signal_clear(self._pointer)

    # --- NEW: Basic Getters/Setters ---
    def get_xside(self):
        return clink.signal_get_xside(self._pointer)

    def set_xside(self, value: bool):
        clink.signal_set_xside(self._pointer, value)
        return self

    def get_yside(self):
        return clink.signal_get_yside(self._pointer)

    def set_yside(self, value: bool):
        clink.signal_set_yside(self._pointer, value)
        return self

    def get_label(self):
        p = clink.signal_get_label(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    def set_label(self, label):
        clink.signal_set_label(self._pointer, wstring(label))
        return self

    def get_marker(self):
        return marker(_pointer=clink.signal_get_marker(self._pointer))

    def set_marker(self, marker_obj):
        clink.signal_set_marker(self._pointer, marker_obj._pointer)
        return self

    def get_fill_method(self):
        return clink.signal_get_fill_method(self._pointer)

    def set_fill_method(self, method):
        method = correct.line_method(method)
        clink.signal_set_fill_method(self._pointer, method)
        return self

    def get_line_method(self):
        return clink.signal_get_line_method(self._pointer)

    def set_line_method(self, method):
        method = correct.line_method(method)
        clink.signal_set_line_method(self._pointer, method)
        return self


    # --- Existing Methods ---
    def get_point(self, index): 
        return point_filled_class(_pointer = clink.signal_get_point(self._pointer, index))

    def get_fill_point(self, index): 
        return point_filled_class(pointer=clink.signal_get_fill_point(self._pointer, index))

    def get_length(self): 
        return clink.signal_get_length(self._pointer)

    def get_range(self): 
        return range(self.get_length())

    def get_x(self):
        return [p.get_x() for p in self]

    def get_y(self):
        return [p.get_y() for p in self]

    def get_xmin(self, ymin=None, ymax=None):
        ymin = -inf if ymin is None else ymin
        ymax = inf if ymax is None else ymax
        return clink.signal_get_xmin(self._pointer, ymin, ymax)

    def get_xmax(self, ymin=None, ymax=None):
        ymin = -inf if ymin is None else ymin
        ymax = inf if ymax is None else ymax
        return clink.signal_get_xmax(self._pointer, ymin, ymax)

    def get_xlimits(self, ymin=None, ymax=None):
        return (self.get_xmin(ymin, ymax), self.get_xmax(ymin, ymax))

    def get_ymin(self, xmin=None, xmax=None):
        xmin = -inf if xmin is None else xmin
        xmax = inf if xmax is None else xmax
        return clink.signal_get_ymin(self._pointer, xmin, xmax)

    def get_ymax(self, xmin=None, xmax=None):
        xmin = -inf if xmin is None else xmin
        xmax = inf if xmax is None else xmax
        return clink.signal_get_ymax(self._pointer, xmin, xmax)

    def get_ylimits(self, xmin=None, xmax=None):
        return (self.get_ymin(xmin, xmax), self.get_ymax(xmin, xmax))

    def get_foreground_unique_integer_colors(self):
        #return self.get(0).get_foreground_integer_color()
        return unique([el.get_foreground_integer_color() for el in self])

    def select_in_matrix(self, width, height):
        clink.signal_select_in_matrix(self._pointer, width, height)
        return self

    def fix_background(self, pixel):
        clink.signal_fix_background(self._pointer, pixel._pointer)
        return self

    def set_points(self, x=None, y=None, m=None):
        [self.add_point(point_filled_class(x[i], y[i], m[i])) for i in range(len(x))]
        return self

    def set_point(self, index=None, x=None, y=None, m=None):
        clink.signal_set_point(self._pointer, index, x, y, m._pointer)
        return self

    def set_fill_point(self, index=None, x=None, y=None, m=None):
        clink.signal_set_fill_point(self._pointer, index, x, y, m._pointer)
        return self

    def add_point(self, point):
        clink.signal_add_point(self._pointer, point._pointer)
        return self

    def append(self, signal):
        clink.signal_append(self._pointer, signal._pointer)
        return self

    def plot(self): 
        clink.signal_plot(self._pointer)
        return self

    def get_filled_points(self):
        return points_class(_pointer = clink.signal_get_filled_points(self._pointer))

    def add_offset(self, dx, dy):
        clink.signal_add_offset(self._pointer, dx, dy)
        return self

    def squash(self, points_map): 
        clink.signal_squash(self._pointer, points_map._pointer)
        return self

    def log_x(self):
        clink.signal_log_x(self._pointer)
        return self

    def log_y(self):
        clink.signal_log_y(self._pointer)
        return self

    def rescale_x(self, limits, width, delta):
        clink.signal_rescale_x(self._pointer, *limits, width, delta)
        return self

    def rescale_y(self, limits, height, delta):
        clink.signal_rescale_y(self._pointer, *limits, height, delta)
        return self

    def copy(self): 
        out = signal_class(_pointer=clink.signal_copy(self._pointer))
        out._lines = self._lines
        return out

    def copy_from(self, points): 
        return clink.signal_assign(self._pointer, points._pointer)

    def get_log(self, fill=False): 
        p = clink.signal_get_wstring(self._pointer, fill)
        string = wstring.from_buffer(p).value 
        clink.wstring_delete(p)
        return string 

    def log(self, fill=False):
        print(self.get_log(fill))
        return self

    def __repr__(self): 
        return self.get_log()

    def __iter__(self):
        return (self.get_point(i) for i in self.get_range())



# class signal_class:
#     # Initialize points with new or existing pointer
#     def __init__(self, length = None, _pointer = None): 
#         self._pointer = clink.signal_new(length) if _pointer is None else _pointer 

#     # Clean up pointer on deletion
#     def __del__(self): clink.signal_delete(self._pointer); self._pointer = None

#     def set_lines(self, lines = False): self._lines = lines

#     def get_lines(self): return self._lines

#     # def set(self, *args, marker = None, xside = None, yside = None, plot = None, label = None):
#     #     x, y = correct.data(*args) 
#     #     #m = correct.markers(marker, default_marker, len(x)) 
#     #     self._pointer = clink.signal_new(length)
#     #     self.set_points(x, y, m) 
#     #     label = '' if label is None else label
#     #     self.set_details(xside, yside, label)
#     #     self._plot = correct.bool(plot) 

#     # Clear all points 
#     def clear(self): clink.signal_clear(self._pointer)

#     # Get point by index 
#     def get_point(self, index): return point_filled_class(pointer = clink.signal_get_point(self._pointer, index))

#     # Get point by index 
#     def get_fill_point(self, index): return point_filled_class(pointer = clink.signal_get_fill_point(self._pointer, index))

#     # Get number of  
#     def get_length(self): return clink.signal_get_length(self._pointer)

#     # Get range of valid indices 
#     def get_range(self): return range(self.get_length())


#     # Get min and max x-values 
#     def get_xmin(self, ymin=None, ymax=None):
#         ymin = -inf if ymin is None else ymin
#         ymax = inf if ymax is None else ymax
#         return clink.signal_get_xmin(self._pointer, ymin, ymax)

#     def get_xmax(self, ymin=None, ymax=None):
#         ymin = -inf if ymin is None else ymin
#         ymax = inf if ymax is None else ymax
#         return clink.signal_get_xmax(self._pointer, ymin, ymax)

#     def get_xlimits(self, ymin=None, ymax=None):
#         return (self.get_xmin(ymin, ymax), self.get_xmax(ymin, ymax))


#     # Get min and max y-values 
#     def get_ymin(self, xmin=None, xmax=None):
#         xmin = -inf if xmin is None else xmin
#         xmax = inf if xmax is None else xmax
#         return clink.signal_get_ymin(self._pointer, xmin, xmax)

#     def get_ymax(self, xmin=None, xmax=None):
#         xmin = -inf if xmin is None else xmin
#         xmax = inf if xmax is None else xmax
#         return clink.signal_get_ymax(self._pointer, xmin, xmax)

#     def get_ylimits(self, xmin=None, xmax=None):
#         return (self.get_ymin(xmin, xmax), self.get_ymax(xmin, xmax))

#     def select_in_matrix(self, width, height):
#         clink.signal_select_in_matrix(self._pointer, width, height)
#         return self


#     # Fix background pixel for points 
#     def fix_background(self, pixel):
#         clink.signal_fix_background(self._pointer, pixel._pointer)
#         return self

#     def set_points(self, x = None, y = None, m = None):
#         [self.add_point(point_filled_class(x[i], y[i], m[i])) for i in range(len(x))]
#         return self

#     def set_point(self, index = None, x = None, y = None, m = None):
#         clink.signal_set_point(self._pointer, index, x, y, m._pointer) 
#         return self 

#     def set_fill_point(self, index = None, x = None, y = None, m = None):
#         clink.signal_set_fill_point(self._pointer, index, x, y, m._pointer) 
#         return self 

#     # def set_fill_points(self, x = None, y = None, m = None):
#     #     [self.set_fill_point(i, x[i], y[i], m[i]) for i in range(len(x))]
#     #     return self

#     def set_fill(self, signal):
#         for i, point in enumerate(signal): 
#             #print(i, point, self.get(i))
#             self.set_fill_point(i, point.get_x(), point.get_y(), point.get_marker()) 
#         return self  

#     def fill(self, points): 
#         signal_class(_pointer = clink.signal_fill(self._pointer, points._pointer))
#         return self

#     def get_filled_lines_length(self):
#         return clink.signal_get_filled_lines_length(self._pointer)

#     def plot(self, method = 0): 
#         clink.signal_plot(self._pointer, method)
#         return self

#         # Add offset to all points
#     def add_offset(self, dx, dy):
#         clink.signal_add_offset(self._pointer, dx, dy)
#         return self

#     def squash(self, points_map): 
#         clink.signal_squash(self._pointer, points_map._pointer)
#         return self

#     def get_label(self):
#         p = clink.signal_get_label(self._pointer)
#         string = wstring.from_buffer(p).value
#         clink.wstring_delete(p)
#         return string

#     def get_xside(self):
#         return clink.signal_get_side(self._pointer, False)

#     def get_yside(self):
#         return clink.signal_get_side(self._pointer, True)

#     def set_marker(self, marker):
#         clink.signal_set_marker(self._pointer, marker._pointer)
#         return self

#     def get_marker(self):
#         return marker(_pointer = clink.signal_get_marker(self._pointer))

#     def get_foreground_unique_integer_colors(self):
#         #return self.get(0).get_foreground_integer_color()
#         return unique([el.get_foreground_integer_color() for el in self])

#     def set_details(self, xside, yside, label, line_method, fill_method):
#         clink.signal_set_details(self._pointer, xside, yside, wstring(label), line_method, fill_method) 
#         return self 

#     # Add a point
#     def add_point(self, point):
#         clink.signal_add_point(self._pointer, point._pointer)
#         return self

#     def append(self, signal):
#         clink.signal_append(self._pointer, signal._pointer)
#         return self

#     # # Set a fill point at index
#     # def set_fill(self, index, point):
#     #     clink.signal_set_fill_point(self._pointer, index, point._pointer)
#     #     return self 

#     # Log x-values
#     def log_x(self):
#         clink.signal_log_x(self._pointer)
#         return self

#     # Log y-values
#     def log_y(self):
#         clink.signal_log_y(self._pointer)
#         return self

#     # Rescale x-values with given limits and width
#     def rescale_x(self, limits, width, delta):
#         clink.signal_rescale_x(self._pointer, *limits, width, delta)

#     # Rescale y-values with given limits and height
#     def rescale_y(self, limits, height, delta):
#         clink.signal_rescale_y(self._pointer, *limits, height, delta)

#     # Copy points instance 
#     def copy(self): 
#         out = signal_class(_pointer = clink.signal_copy(self._pointer))
#         out._lines = self._lines
#         return out

#     # Copy data from another points instance
#     def copy_from(self, points): 
#         return clink.signal_assign(self._pointer, points._pointer)

#     # Get string representation
#     def get_log(self, fill = False): 
#         p = clink.signal_get_wstring(self._pointer, fill) 
#         string = wstring.from_buffer(p).value 
#         clink.wstring_delete(p) 
#         return string 

#     # Print the log string
#     def log(self, fill = False):
#         print(self.get_log(fill))
#         return self

#     def __repr__(self): 
#         return self.get_log()

#     # Print points string representation
#     def print(self):
#         print(self.get_string())
#         return self

#     # Iterator over points
#     def __iter__(self):
#         return (self.get_point(i) for i in self.get_range())