class tick_class:

    # Initialize with position and label
    def __init__(self, position, label):
        self.set(position, label)

    # Set both position and label
    def set(self, position, label):
        self.set_position(position)
        self.set_label(label)
        return self

    # Set tick position
    def set_position(self, position):
        self.position = position
        return self

    # Set tick label
    def set_label(self, label):
        self.label = label
        return self


    # Return (position, label) tuple
    def get(self):
        return self.position, self.label

    # Get tick position
    def get_position(self):
        return self.position

    # Get tick label
    def get_label(self):
        return self.label


    # Check if tick is within the given limits
    def is_within_limits(self, limits):
        return limits[0] <= self.position <= limits[1]

    # Return a new copy of the tick
    def copy(self):
        return tick_class(self.get_position(), self.get_label())

    # Clone another tick's position
    def clone(self, tick):
        self.position = tick.position
        return self

    # String representation of the tick
    def __repr__(self):
        return str(self.get())
