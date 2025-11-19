from plotext._line import *
from plotext._methods import *


class lines_class:
    def __init__(self):
        self.clear()

    # Reset the lines collection
    def clear(self):
        self.lines = []
        return self

    # Add a line with specified attributes
    def add(self, position, orientation, style, pixel):
        self.lines.append(line_class(position, orientation, style, pixel))
        return self

    # Get positions of all lines
    def get_positions(self):
        return [line.get_position() for line in self.lines]

    # Set positions of all lines
    def set_positions(self, positions):
        [line.set_position(p) for line, p in zip(self.lines, positions)]
        return self

    # Get min and max positions of lines
    def get_limits(self):
        pos = self.get_positions()
        return min(pos, default = None), max(pos, default = None)

    # Get number of lines
    def get_length(self):
        return len(self.lines)

    # Check if any lines exist
    def is_active(self):
        return self.get_length() > 0

    # Clone lines from another lines object
    def clone(self, lines):
        self.lines = [el.copy() for el in lines.lines]
        return self

    # Rescale line positions based on limits, bins and delta
    def rescale(self, limits, bins, delta):
        positions = self.get_positions()
        positions = [int(list_methods.rescale(el, *limits, bins, delta)) for el in positions]
        self.set_positions(positions)
        return self

    # Return summary log string
    def get_log(self):
        return f'{self.get_length()} Lines'

    # Print the log
    def log(self):
        print(self.get_log())

    def __repr__(self):
        return self.get_log()
