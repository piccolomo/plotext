# Ticks: container of tick_class instances with batch get/set/rescale operations

from plotext._plotter.frame.tick import tick_class


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
    def set(self, positions = [], labels = []):
        self.ticks = [tick_class(p, l) for p, l in zip(positions, labels)]
        return self

    # Set only tick positions
    def set_positions(self, positions):
        [t.set_position(p) for t, p in zip(self.ticks, positions)]
        return self

    # Get only tick positions
    def get_positions(self):
        return [t.position() for t in self.ticks]

    # Get (min, max) of tick positions, or (None, None) if empty
    def get_limits(self):
        pos = self.get_positions()
        return min(pos, default = None), max(pos, default = None)

    # Get only tick labels
    def get_labels(self):
        return [t.label() for t in self.ticks]

    # Get maximum width of tick labels (labels are now 1-row matrices, so width = number of columns)
    def get_labels_width(self):
        return max([l.width() for l in self.get_labels()], default = 0)

    # Get number of ticks
    def length(self):
        return len(self.ticks)

    # Check if ticks are empty
    def inactive(self):
        return self.length() == 0

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
    def _get_log(self):
        return str(self.length())

    # String representation
    def __repr__(self):
        return "PlotextTicks(" + self._get_log() + ' ' + ', '.join([str(el) for el in self.ticks]) + ")"

    # Iterate over ticks
    def __iter__(self):
        return iter(self.ticks)
