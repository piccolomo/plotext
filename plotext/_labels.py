from plotext._colorize import colorize
from plotext._constants import r2
from plotext._correct import correct_class as correct
from plotext._derived import *


class labels_class:
    # Initialize labels and clear all
    def __init__(self):
        self.clear()

    # Clear all labels to None
    def clear(self):
        self.x = [None, None]
        self.y = [None, None]
        self.title = None
        self.set_pixel()
        return self

    # Get label for given axis and side
    def get(self, axis = 0, side = 0):
        return self.y[side] if axis else self.x[side]

    # Set label for a specific axis and side
    def set_label(self, axis = 0, side = 0, label = None):
        axis = correct.axis(axis)
        side = correct.side(axis, side)
        label = correct.label(label, default_label_pixel)
        if axis:
            self.y[side] = label
        else:
            self.x[side] = label
        return self

    # Set the title label
    def set_title(self, label):
        label = correct.label(label, default_label_pixel)
        self.title = label
        return self

    # Set pixel, default if none provided
    def set_pixel(self, pixel = None, default_pixel = None):
        pixel = correct.pixel(pixel, default_line_pixel)
        self.pixel = pixel 
        return self

    # Check if upper bar (title or upper x label) is present
    def upper_present(self):
        return self.title is not None or self.x[1] is not None

    # Check if lower bar (lower x label or any y label) is present
    def lower_present(self):
        return self.x[0] is not None or self.y[0] is not None or self.y[1] is not None

    # Clone labels from another labels_class instance
    def clone(self, labels):
        [self.set_label(a, s, labels.get(a, s)) for a in r2 for s in r2]
        self.set_title(labels.title)
        return self

    # String representation showing current labels
    def __repr__(self):
        x = f'xlabels {self.x[0]} and {self.x[1]}'
        y = f'ylabels {self.y[0]} and {self.y[1]}'
        t = f'title {self.title}'
        p = f'Pixel {self.pixel}'
        return ', '.join([x, y, t, p])
