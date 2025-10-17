from plotext._clink import clink
from plotext._point import point_class
from plotext._points import points_class
from plotext._correct import correct_class as correct


class signallll_class(points_class):

    # Initialize a signal from x, y, m arrays or pointer
    def __init__(self, length = 10):
        self.points = points_class(length)
        self.fill = points_class(length)
        self.set_xside()
        self.set_yside()
        self.set_label()

    def get_length(self):
        return min(self.points.get_length(), self.fill.get_length())



    def set_fill(self, x = None, y = None, m = None):
        [self.fill.add(point_class(x[i], y[i], m[i])) for i in range(len(x))]
        return self

    # Destructor calls parent destructor
    def __del__(self): 
        del(self.points)
        del(self.fill)

    # # Set x-side attribute
    # def set_xside(self, side = None): 
    #     side = correct.side(0, side)
    #     self.xside = side; 
    #     return self

    # # Set y-side attribute
    # def set_yside(self, side = None): 
    #     side = correct.side(1, side)
    #     self.yside = side; 
    #     return self

    # # Set label attribute
    # def set_label(self, label = None): 
    #     self.label = label; 
    #     return self

    # # Set fill points from x, y, m arrays
    # def set_fill(self, x = None, y = None, m = None):
    #     length = min(len(x), self.get_length())
    #     [self.set_fill_point(i, point_class(x[i], y[i], m[i])) for i in range(length)]
    #     return self

    def get_fill(self): 
        signal = self.points.get_fill(self.fill)
        out = signal_class(0)
        out.points.copy_from(signal)
        return out

    def fix_background(self, pixel):
        self.points.fix_background(pixel)
        self.fill.fix_background(pixel)
        return self

    def get_xmin(self):
        return min(self.points.get_xmin(), self.fill.get_xmin())

    def get_xmax(self):
        return max(self.points.get_xmax(), self.fill.get_xmax())

    def get_xlimits(self):
        return self.get_xmin(), self.get_xmax()


    def get_ymin(self):
        return min(self.points.get_ymin(), self.fill.get_ymin())

    def get_ymax(self):
        return max(self.points.get_ymax(), self.fill.get_ymax())

    def get_ylimits(self):
        return self.get_ymin(), self.get_ymax()

    # Rescale x-values with given limits and width
    def rescale_x(self, limits, width, delta):
        self.points.rescale_x(limits, width, delta)
        self.fill.rescale_x(limits, width, delta)
        return self

    def rescale_y(self, limits, width, delta):
        self.points.rescale_y(limits, width, delta)
        self.fill.rescale_y(limits, width, delta)
        return self

    # Add offset to all points
    def add_offset(self, dx, dy):
        self.points.add_offset(dx, dy)
        self.fill.add_offset(dx, dy)
        return self

    # Return a copy of the signal 
    def copy(self): 
        out = signal_class(0)
        out.points.copy_from(self.points)
        out.fill.copy_from(self.fill)
        self.set_xside(self.xside)
        self.set_yside(self.yside)
        self.set_label(self.label)
        return out

    # Get label as string
    def get_label(self): 
        return str(self.label)

    def get_marker(self):
        return self.points.get(0).get_marker()

    # Generate a log string of the signal
    def get_log(self, full = True):
        log = self.get_label() + ', '
        log += 'length ' + str(self.get_length()) + ', '
        log += 'xside ' + str(self.xside) + ', '
        log += 'yside ' + str(self.yside) + ', '
        log += "first marker " + str(self.get_marker())+ '\n'
        if full:
            log += self.points.get_string() + '\n'
            log += self.fill.get_string() + '\n'
        return log

    # Print the log string
    def log(self):
        print(self.get_log())
        return self

    # Representation returns the log string
    def __repr__(self): 
        return self.get_log()

    def __iter__(self):
        return self.points.__iter__()
