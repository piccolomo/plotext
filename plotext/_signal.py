from plotext._clink import clink
from plotext._point import point_class
from plotext._points import points_class


class signal_class(points_class):

    # Initialize a signal from x, y, m arrays or pointer
    def __init__(self, x = None, y = None, m = None, xside = None, yside = None, label = None, pointer = None):
        if pointer is None:
            length = len(x)
            super().__init__(length)
            [self.add(point_class(x[i], y[i], m[i])) for i in range(length)]
        else:
            super().__init__(pointer = pointer)
        self.set_xside(xside)
        self.set_yside(yside)
        self.set_label(label)

    # Destructor calls parent destructor
    def __del__(self): super().__del__()

    # Set x-side attribute
    def set_xside(self, side = None): self.xside = side; return self

    # Set y-side attribute
    def set_yside(self, side = None): self.yside = side; return self

    # Set label attribute
    def set_label(self, label = None): self.label = label; return self

    # Set fill points from x, y, m arrays
    def set_fill(self, x = None, y = None, m = None):
        length = min(len(x), self.get_length())
        [self.set_fill_point(i, point_class(x[i], y[i], m[i])) for i in range(length)]
        return self

    # Return a copy of the signal
    def copy(self):
        return signal_class(xside = self.xside, yside = self.yside, label = self.label, pointer = clink.points_copy(self._pointer))

    # Get label as string
    def get_label(self): return str(self.label)

    # Generate a log string of the signal
    def get_log(self):
        log = self.get_label() + ', '
        log += 'xside ' + str(self.xside) + ', '
        log += 'yside ' + str(self.yside) + '\n'
        log += self.get_string() + '\n'
        return log

    # Print the log string
    def log(self):
        print(self.get_log())
        return self

    # Representation returns the log string
    def __repr__(self): return self.get_log()
