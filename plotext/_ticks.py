from plotext._methods import *
from plotext._tick import tick_class


class ticks_class:

    # Initialize with empty ticks
    def __init__(self):
        self.clear()

    # Clear all ticks
    def clear(self):
        self.set()
        return self

    # Set ticks from positions and labels
    def set(self, positions = [], labels = []):
        self.ticks = [tick_class(t, l) for t, l in zip(positions, labels)]
        return self

    # Set only the tick positions
    def set_positions(self, positions):
        [t.set_position(p) for t, p in zip(self.ticks, positions)]
        return self


    # Return all (position, label) pairs
    def get(self):
        return [el.get() for el in self.ticks]

    # Return only tick positions
    def get_positions(self, limits = None):
        return [el.get_position() for el in self.ticks]

    # Return only tick labels
    def get_labels(self):
        return [el.get_label() for el in self.ticks]

    # Return the maximum width of tick labels
    def get_labels_width(self):
        return max([len(label) for label in self.get_labels()], default = 0)

    # Return number of ticks
    def get_length(self):
        return len(self.ticks)

    # Check if ticks are active (non-empty)
    def is_active(self):
        return self.get_length() > 0

    # Return a new ticks object with ticks within limits
    def select(self, limits):
        new = ticks_class()
        new.ticks = [el.copy() for el in self.ticks if el.is_within_limits(limits)]
        return new

    # Rescale tick positions within limits
    def rescale(self, limits, bins, delta):
        positions = self.get_positions()
        positions = [list_methods.rescale(el, *limits, bins, delta) for el in positions]
        positions = list_methods.to_integers(positions)
        self.set_positions(positions)
        return self

    # Clone ticks from another ticks object
    def clone(self, ticks):
        self.ticks = [el.copy() for el in ticks.ticks]
        return self


    # Return a short log string
    def get_log(self):
        return 'Ticks ' + str(self.get_length())

    # Print the log string
    def log(self):
        print(self.get_log())

    # String representation
    def __repr__(self):
        return self.get_log()

