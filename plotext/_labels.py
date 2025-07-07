from plotext._colorize import colorize_class as colorize
from plotext._constants import r2
from plotext._default import default_labels_pixel


class labels_class:
    # Initialize labels and clear all
    def __init__(self):
        self.clear()

    # Clear all labels to None
    def clear(self):
        self.x = [None, None]
        self.y = [None, None]
        self.title = None
        return self

    # Get label for given axis and side
    def get(self, axis = 0, side = 0):
        return self.y[side] if axis else self.x[side]

    # Set label for a specific axis and side
    def set_label(self, axis = 0, side = 0, label = None):
        if axis:
            self.y[side] = label
        else:
            self.x[side] = label
        return self

    # Set the title label
    def set_title(self, label):
        if self.title is not None and label is not None:
            self.title.clone(label)
        else:
            self.title = label
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
        return ', '.join([x, y, t])
