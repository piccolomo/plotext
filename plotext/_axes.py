from plotext._axis import axis_class
from plotext._constants import r2


class axes_class:
    # Initialize x and y axes with two sides each
    def __init__(self):
        self.xaxis = [axis_class(0, 0), axis_class(0, 1)]
        self.yaxis = [axis_class(1, 0), axis_class(1, 1)]

    # Clear all axes
    def clear(self):
        self.get(0, 0).clear()
        self.get(0, 1).clear()
        self.get(1, 0).clear()
        self.get(1, 1).clear()
        return self

    # Set frame status, style, and pixel for all axes
    def frame(self, frame = True, style = None, pixel = None):
        [self.get(axis, side).set_status(frame).set_style(style).set_pixel(pixel) for axis in r2 for side in r2]
        return self

    # Get axis object based on axis and side
    def get(self, axis = 0, side = 0):
        container = self.yaxis if axis else self.xaxis
        return container[side]

    # Clone all axes properties from another axes_class instance
    def clone(self, axes):
        [self.get(axis, side).clone(axes.get(axis, side)) for axis in r2 for side in r2]
        return self

    # Get string representation of a specific axis
    def get_string(self, axis = 0, side = 0):
        return self.get(axis, side).get_string()

    # Return combined log string for all axes
    def get_log(self):
        log = ''
        for axis in r2:
            for side in r2:
                log += self.get(axis, side).get_log() + '\n'
        return log

    # Print the combined log string
    def log(self):
        print(self.get_log())

    # String representation returns combined log
    def __repr__(self): return self.get_log()
