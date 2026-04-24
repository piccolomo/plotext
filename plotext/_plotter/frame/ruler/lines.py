# Lines: container of ruler line objects with batch add/rescale/filter operations

from plotext._plotter.frame.ruler.line import line_class, line_style


# Collection of ruler lines with batch operations
class lines_class:
    # Initialize empty lines list
    def __init__(self):
        self.clear()

    # Reset the lines collection
    def clear(self):
        self._lines = []
        return self

    # Clear settings on every line
    def clear_settings(self):
        [line.clear_settings() for line in self._lines]
        return self

    # Clear pixel on every line
    def clear_pixels(self):
        [line.clear_pixel() for line in self._lines]
        return self

    # Clear style on every line
    def clear_styles(self):
        [line.clear_style() for line in self._lines]
        return self

    # Add a line with specified attributes
    def add(self, position, relative, style, pixel):
        self._lines.append(line_class(position, relative, style, pixel))
        return self

    # Access a line by index
    def get(self, index):
        return self._lines[index]

    # Get positions of all lines
    def get_positions(self):
        return [line.get_position() for line in self._lines]

    # Set positions of all lines
    def set_positions(self, positions):
        [line.set_position(p) for line, p in zip(self._lines, positions)]
        return self

    # Get min and max positions of lines
    def get_limits(self):
        pos = self.get_positions()
        return min(pos, default = None), max(pos, default = None)

    # Get number of lines
    def get_length(self):
        return len(self._lines)

    # Check if any lines exist
    def is_active(self):
        return self.get_length() > 0

    # Clone lines from another lines object
    def clone(self, lines):
        self._lines = [el.copy() for el in lines._lines]
        return self

    # Rescale line positions within limits
    def rescale(self, limits, bins, delta):
        [line.rescale(limits, bins, delta) for line in self]
        self.filter(bins)
        return self

    # Apply logarithm to all line positions
    def log(self):
        [line.log() for line in self]
        return self

    # Filter lines within bins
    def filter(self, bins):
        self._lines = [line for line in self if line.is_within_bins(bins)]
        return self

    # Return summary log string
    def get_log(self):
        return f'{self.get_length()} Lines'

    # Get the private list of line objects
    def get_lines(self):
        return self._lines

    # String representation
    def __repr__(self):
        return f"Plotext Lines: " + self.get_log() + ' ' + ', '.join([str(round(el, 2)) for el in self.get_positions()])

    # Iterate over lines
    def __iter__(self):
        return iter(self._lines)
