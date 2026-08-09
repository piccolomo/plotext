# Tick: single ruler tick with a position and a label

from plotext._methods.ruler import rescale, log


# A single ruler tick tying a position to a label
class tick_class:
    # Initialize with position and label
    def __init__(self, position, label):
        self.set(position, label)

    # Set position and label
    def set(self, position, label):
        self.set_position(position)
        self.set_label(label)
        return self

    # Set position
    def set_position(self, position):
        self._position = position
        return self

    # Set label
    def set_label(self, label):
        self._label = label
        return self

    # Get position
    def position(self):
        return self._position

    # Get label
    def label(self):
        return self._label

    # Check if tick is within given bins
    def is_within_bins(self, bins):
        return 0 <= self._position < bins

    # Rescale tick position according to limits and bins
    def rescale(self, limits, bins, delta):
        pos = self._position
        pos = int(rescale(pos, *limits, bins, delta))
        self.set_position(pos)
        return self

    # Apply logarithm to position
    def log(self):
        self._position = log(self._position)
        return self

    # Return a copy
    def copy(self):
        return tick_class(self._position, self._label)

    # Clone another tick's position
    def clone(self, tick):
        self._position = tick._position
        return self

    # String representation
    def __repr__(self):
        return str((round(self._position, 2), self._label))
