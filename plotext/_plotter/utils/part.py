# This module defines a `part` class that represents a part with a name, position, and size.

class part_class:
    # Initialize the part
    def __init__(self, name):
        self._name = name
        self.clear()

    # Reset position and size
    def clear(self):
        self.set_position()
        self.set_size()
        return self

    # Set column and row position
    def set_position(self, col = None, row = None):
        self._col = None if col is None else int(col)
        self._row = None if row is None else int(row)
        return self

    # Set width
    def set_width(self, width = None):
        self._width = None if width is None else int(width)
        return self

    # Set height
    def set_height(self, height = None):
        self._height = None if height is None else int(height)
        return self

    # Set size (width and height)
    def set_size(self, width = None, height = None):
        self.set_width(width)
        self.set_height(height)
        return self

    # Check if both width and height are set
    def has_size(self):
        return self.has_width() and self.has_height()

    # Check if width is set
    def has_width(self):
        return self._width not in (None, 0)

    # Check if height is set
    def has_height(self):
        return self._height not in (None, 0)

    # Get column considering optional side offset
    def get_col(self, side = 0):
        return self._col + (self._width if side else 0)

    # Get row considering optional side offset
    def get_row(self, side = 0):
        return self._row + (self._height if side else 0)

    # Get position (col, row) considering offsets
    def position(self, xside = 0, yside = 0):
        return self.get_col(xside), self.get_row(yside)

    # Get width
    def width(self):
        return self._width

    # Get height
    def height(self):
        return self._height

    # Get size (width, height)
    def size(self):
        return self._width, self._height

    # Public getter for name
    def get_name(self):
        return self._name

    # Return a log string describing the part
    def _get_log(self):
        return f"{self._name.title()}: position: {(self._col, self._row)}, size: {(self._width, self._height)}"

    # String representation
    def __repr__(self):
        return "PlotextPart(" + self._get_log() + ")"
