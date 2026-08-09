# Axes: 2x2 container of frame axes (x lower/upper, y left/right) with batch operations

from plotext._plotter.frame.axis import axis_class
from plotext._constants.numerical import binary
from plotext._correct import axis as correct
from plotext._settings import defaults


# 2x2 container for the four frame axes, providing batch get/set/clone operations
class axes_class:
    # Initialize x and y axes with two sides each
    def __init__(self):
        self._xaxis = [axis_class(0, 0), axis_class(0, 1)]
        self._yaxis = [axis_class(1, 0), axis_class(1, 1)]

    # Clear all axes
    def clear_settings(self):
        [axis.clear_settings() for axis in self.get_multiple(binary, binary)]
        return self

    # Set default pixel for all axes
    def clear_pixels(self):
        [axis.clear_pixel() for axis in self.get_multiple(binary, binary)]
        return self

    # Set default style for all axes
    def clear_styles(self):
        [axis.clear_style() for axis in self.get_multiple(binary, binary)]
        return self

    # Access a specific axis
    def get(self, axis = 0, side = 0):
        container = self._yaxis if axis else self._xaxis
        return container[side]

    # Access multiple axes filtered by axis/side selectors
    def get_multiple(self, axis = 0, side = 0):
        axes = correct.axes(axis)
        sides = correct.sides(axes, side)
        return [self.get(axis, side) for axis in axes for side in sides]

    # Set axis status, style, and pixel
    def set(self, status = None, style = None, pixel = None, axis = 0, side = 0):
        [axis.set(status, style, pixel) for axis in self.get_multiple(axis, side)]
        return self

    # Set frame status, style, and pixel for all axes
    def frame(self, active = True, style = None, pixel = None):
        return self.set(active, style, pixel, binary, binary)

    # Clone all axes properties from another axes_class instance
    def clone(self, axes):
        for axis in binary:
            for side in binary:
                self.get(axis, side).clone(axes.get(axis, side))
        return self

    # Get string representation of a specific axis
    def string(self, axis = 0, side = 0):
        return self.get(axis, side).string()

    # Represent axes in Plotext style
    def __repr__(self):
        out = f"Plotext Axes\n "
        out += '\n '.join([ax._get_log() for ax in self._xaxis + self._yaxis])
        return out
