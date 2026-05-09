# Ticks: container of tick_class instances with batch get/set/rescale operations

from plotext._plotter.frame.tick import tick_class
from plotext._primitives.text import text as text_class


# Collection of ruler ticks with batch operations
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

    # Build a text_class per tick: position maps to col (axis 0) or row (axis 1); other_coord is the orthogonal coordinate. alignment=2 (dynamic) lets the matrix search for a free spot when inserting; non-dynamic callers (e.g. y-axis labels) override via _set_alignment before insert.
    def get_texts(self, axis = 0, other_coord = 0):
        return [text_class(t.get_position(), other_coord, t.get_label(), alignment=2) if axis == 0
                else text_class(other_coord, t.get_position(), t.get_label(), alignment=2) for t in self.ticks]

    # Get only tick positions
    def get_positions(self):
        return [t.get_position() for t in self.ticks]

    # Get (min, max) of tick positions, or (None, None) if empty
    def get_limits(self):
        pos = self.get_positions()
        return min(pos, default = None), max(pos, default = None)

    # Get only tick labels
    def get_labels(self):
        return [t.get_label() for t in self.ticks]

    # Get maximum width of tick labels
    def get_labels_width(self):
        return max([len(l) for l in self.get_labels()], default=0)

    # Get number of ticks
    def get_length(self):
        return len(self.ticks)

    # Check if ticks are empty
    def inactive(self):
        return self.get_length() == 0

    # Check if ticks are present
    def active(self):
        return not self.inactive()

    # Filter to ticks within bins
    def filter(self, bins):
        self.ticks = [line for line in self if line.is_within_bins(bins)]
        return self

    # Rescale tick positions within limits
    def rescale(self, limits, bins, delta):
        positions = [tick.rescale(limits, bins, delta) for tick in self]
        return self

    # Apply logarithm to all tick positions
    def log(self):
        [tick.log() for tick in self]
        return self

    # Clone another ticks object
    def clone(self, ticks):
        self.ticks = [t.copy() for t in ticks.ticks]
        return self

    # Short log string
    def get_log(self):
        return str(self.get_length())

    # String representation
    def __repr__(self):
        return "Ticks: " + self.get_log() + ' ' + ', '.join([str(el) for el in self.ticks])

    # Iterate over ticks
    def __iter__(self):
        return iter(self.ticks)
