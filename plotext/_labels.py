from plotext._colorize import colorize
from plotext._constants import r2
from plotext._correct import correct_class as correct
from plotext._derived import *


class labels_class:
    def __init__(self):
        self.clear()

    def clear(self):
        self.x = [None, None]
        self.y = [None, None]
        self.title = None
        self.set_pixel()
        return self

    def get(self, axis=0, side=0):
        return self.y[side] if axis else self.x[side]

    def set_label(self, axis=0, side=0, label=None):
        axis = correct.axis(axis)
        side = correct.side(axis, side)
        label = correct.label(label, default_label_pixel)
        if axis:
            self.y[side] = label
        else:
            self.x[side] = label
        return self

    def set_title(self, label):
        self.title = correct.label(label, default_label_pixel)
        return self

    def set_pixel(self, pixel=None, default_pixel=None):
        self.pixel = correct.pixel(pixel, default_line_pixel)
        return self

    def upper_present(self):
        return self.title is not None or self.x[1] is not None

    def lower_present(self):
        return self.x[0] is not None or self.y[0] is not None or self.y[1] is not None

    def clone(self, labels):
        for a in r2:
            for s in r2:
                self.set_label(a, s, labels.get(a, s))
        self.set_title(labels.title)
        return self

    def __repr__(self):
        return f"xlabels {self.x[0]} and {self.x[1]}, ylabels {self.y[0]} and {self.y[1]}, title {self.title}, Pixel {self.pixel}"
