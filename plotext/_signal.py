from plotext._clink import clink, wstring
from plotext._point import point_class
from plotext._correct import correct_class as correct
from plotext._derived import default_marker


class signal_class:
    # Initialize points with new or existing pointer
    def __init__(self, *args, marker = None, xside = None, yside = None, plot = None, label = None, _pointer = None):
        if _pointer is None: 
            x, y = correct.data(*args) 
            length = len(x) 
            label = correct.signal_label(label) 
            m = correct.markers(marker, default_marker, length) 
            self._pointer = clink.signal_new(length)
            self.set_points(x, y, m) 
            #self.set_details(xside, yside, label)
        else:
            self._pointer = _pointer 
        self._plot = correct.bool(plot) 

    # Clean up pointer on deletion
    def __del__(self): clink.signal_delete(self._pointer); self._pointer = None

    # Clear all points 
    def clear(self): clink.signal_clear(self._pointer)

    # Get point by index 
    def get_point(self, index): return point_class(pointer = clink.signal_get_point(self._pointer, index))

    # Get point by index 
    def get_fill_point(self, index): return point_class(pointer = clink.signal_get_fill_point(self._pointer, index))

    # Get number of  
    def get_length(self): return clink.signal_get_length(self._pointer)

    # Get range of valid indices 
    def get_range(self): return range(self.get_length())

    # Get min and max x-values 
    def get_xmin(self): return clink.signal_get_xmin(self._pointer)
    def get_xmax(self): return clink.signal_get_xmax(self._pointer)
    def get_xlimits(self): return (self.get_xmin(), self.get_xmax())

    # Get min and max y-values 
    def get_ymin(self): return clink.signal_get_ymin(self._pointer)
    def get_ymax(self): return clink.signal_get_ymax(self._pointer)
    def get_ylimits(self): return (self.get_ymin(), self.get_ymax())

    # Fix background pixel for points 
    def fix_background(self, pixel):
        clink.signal_fix_background(self._pointer, pixel._pointer)
        return self

    def set_points(self, x = None, y = None, m = None):
        [self.add_point(point_class(x[i], y[i], m[i])) for i in range(len(x))]
        return self

    def set_point(self, index = None, x = None, y = None, m = None):
        clink.signal_set_point(self._pointer, index, x, y, m._pointer) 
        return self 

    def set_fill_point(self, index = None, x = None, y = None, m = None):
        clink.signal_set_fill_point(self._pointer, index, x, y, m._pointer) 
        return self 

    # def set_fill_points(self, x = None, y = None, m = None):
    #     [self.set_fill_point(i, x[i], y[i], m[i]) for i in range(len(x))]
    #     return self

    def set_fill(self, signal):
        for i, point in enumerate(signal): 
            #print(i, point, self.get(i))
            self.set_fill_point(i, point.get_x(), point.get_y(), point.get_marker()) 
        return self  

    def fill(self, points): 
        signal_class(_pointer = clink.signal_fill(self._pointer, points._pointer))
        return self

    def get_filled_lines_length(self):
        return clink.signal_get_filled_lines_length(self._pointer)

    def plot(self): 
        clink.signal_plot(self._pointer)
        return self

        # Add offset to all points
    def add_offset(self, dx, dy):
        clink.signal_add_offset(self._pointer, dx, dy)

    def squash(self, points_map): 
        clink.signal_squash(self._pointer, points_map._pointer)
        return self

    def get_label(self):
        p = clink.signal_get_label(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    def get_xside(self):
        return clink.signal_get_side(self._pointer, False)

    def get_yside(self):
        return clink.signal_get_side(self._pointer, True)

    def get_marker(self):
        return self.get_point(0).get_marker()

    def set_details(self, xside, yside, label):
        clink.signal_set_details(self._pointer, xside, yside, wstring(label)) 
        return self 

    # Add a point
    def add_point(self, point):
        clink.signal_add_point(self._pointer, point._pointer)
        return self

    # # Set a fill point at index
    # def set_fill(self, index, point):
    #     clink.signal_set_fill_point(self._pointer, index, point._pointer)
    #     return self

    # Log x-values
    def log_x(self):
        clink.signal_log_x(self._pointer)
        return self

    # Log y-values
    def log_y(self):
        clink.signal_log_y(self._pointer)
        return self

    # Rescale x-values with given limits and width
    def rescale_x(self, limits, width, delta):
        clink.signal_rescale_x(self._pointer, *limits, width, delta)

    # Rescale y-values with given limits and height
    def rescale_y(self, limits, height, delta):
        clink.signal_rescale_y(self._pointer, *limits, height, delta)

    # Copy points instance 
    def copy(self): 
        return signal_class(_pointer = clink.signal_copy(self._pointer), plot = self._plot)

    # Copy data from another points instance
    def copy_from(self, points): 
        return clink.signal_assign(self._pointer, points._pointer)

    # Get string representation
    def get_log(self, fill = False): 
        p = clink.signal_get_wstring(self._pointer, fill) 
        string = wstring.from_buffer(p).value 
        clink.wstring_delete(p) 
        return string 

    # Print the log string
    def log(self, fill = False):
        print(self.get_log(fill))
        return self

    def __repr__(self): 
        return self.get_log()

    # Print points string representation
    def print(self):
        print(self.get_string())
        return self

    # Iterator over points
    def __iter__(self):
        return (self.get_point(i) for i in self.get_range())