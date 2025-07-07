# This module defines a `part` class that represents a part with a name, position, and size.

class part_class:
    def __init__(self, name):
        self.name = name
        self.clear()


    # Reset position and size
    def clear(self):
        self.set_position()
        self.set_size()


    # Set column and row position
    def set_position(self, col = None, row = None):
        self.col = None if col is None else int(col)
        self.row = None if row is None else int(row)
        return self


    # Set width
    def set_width(self, width):
        self.width = None if width is None else int(width)
        return self

    # Set height
    def set_height(self, height):
        self.height = None if height is None else int(height)
        return self

    # Set size (width and height)
    def set_size(self, width = None, height = None):
        self.set_width(width)
        self.set_height(height)
        return self


    # Check if both width and height are set (non-zero)
    def has_size(self):
        return self.has_width() and self.has_height()

    # Check if height is non-zero
    def has_height(self):
        return self.height != 0

    # Check if width is non-zero
    def has_width(self):
        return self.width != 0


    # Get column considering side offset
    def get_col(self, side = 0):
        return self.col + (self.width if side else 0)

    # Get row considering side offset
    def get_row(self, side = 0):
        return self.row + (self.height if side else 0)

    # Get position (col, row) considering offsets
    def get_position(self, xside = 0, yside = 0):
        return self.get_col(xside), self.get_row(yside)


    # Get width
    def get_width(self):
        return self.width

    # Get height
    def get_height(self):
        return self.height

    # Get size (width, height)
    def get_size(self):
        return self.width, self.height


    # Return a log string describing the part
    def get_log(self):
        return f"{self.name}: position: {(self.col, self.row)}, size: {(self.width, self.height)}"

    def __str__(self):
        return self.get_log()

    def __repr__(self):
        return str(self)

