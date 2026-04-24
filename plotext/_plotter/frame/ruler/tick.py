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
        self.position = position
        return self

    # Set label
    def set_label(self, label):
        self.label = label
        return self

    # Get (position, label)
    def get_tuple(self):
        return self.position, self.label

    # Get position
    def get_position(self):
        return self.position

    # Get label
    def get_label(self):
        return self.label

    # Check if tick is within given bins
    def is_within_bins(self, bins):
        return 0 <= self.position < bins

    # Rescale tick position according to limits and bins
    def rescale(self, limits, bins, delta):
        pos = self.get_position()
        pos = int(rescale(pos, *limits, bins, delta))
        self.set_position(pos)
        return self

    # Apply logarithm to position
    def log(self):
        self.position = log(self.position)
        return self

    # Return a copy
    def copy(self):
        return tick_class(self.position, self.label)

    # Clone another tick's position
    def clone(self, tick):
        self.position = tick.position
        return self

    # String representation
    def __repr__(self):
        return str((round(self.position, 2), self.label))
