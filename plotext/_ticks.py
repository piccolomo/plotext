from plotext._methods.list import rescale, to_integers
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
    def set(self, positions=[], labels=[]):
        self.ticks = [tick_class(p, l) for p, l in zip(positions, labels)]
        return self

    # Set only tick positions
    def set_positions(self, positions):
        [t.set_position(p) for t, p in zip(self.ticks, positions)]
        return self

    # Get all (position, label) pairs
    def get(self):
        return [t.get() for t in self.ticks]

    # Get only tick positions
    def get_positions(self, limits=None):
        return [t.get_position() for t in self.ticks]

    # Get only tick labels
    def get_labels(self):
        return [t.get_label() for t in self.ticks]

    # Get maximum width of tick labels
    def get_labels_width(self):
        return max([len(l) for l in self.get_labels()], default=0)

    # Get number of ticks
    def get_length(self):
        return len(self.ticks)

    # Check if ticks are active
    def is_active(self):
        return self.get_length() > 0

    # Return new ticks object within limits
    def select(self, limits):
        new = ticks_class()
        new.ticks = [t.copy() for t in self.ticks if t.is_within_limits(limits)]
        return new

    # Rescale tick positions within limits
    def rescale(self, limits, bins, delta):
        positions = self.get_positions()
        positions = [rescale(p, *limits, bins, delta) for p in positions]
        positions = to_integers(positions)
        self.set_positions(positions)
        return self

    # Clone another ticks object
    def clone(self, ticks):
        self.ticks = [t.copy() for t in ticks.ticks]
        return self

    # Short log string
    def get_log(self):
        return 'Ticks ' + str(self.get_length())

    # Print log
    def log(self):
        print(self.get_log())
        return self

    # String representation
    def __repr__(self):
        return self.get_log()
