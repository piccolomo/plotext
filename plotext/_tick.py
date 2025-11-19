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
    def get(self):
        return self.position, self.label

    # Get position
    def get_position(self):
        return self.position

    # Get label
    def get_label(self):
        return self.label

    # Check if tick is within given limits
    def is_within_limits(self, limits):
        return limits[0] <= self.position <= limits[1]

    # Return a copy
    def copy(self):
        return tick_class(self.position, self.label)

    # Clone another tick's position
    def clone(self, tick):
        self.position = tick.position
        return self

    # String representation
    def __repr__(self):
        return str(self.get())