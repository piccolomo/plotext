# Labels container: title plus x/y labels with pixel styling

from plotext._primitives.colorize import colorize
from plotext._primitives.matrix import matrix as matrix_class
from plotext._primitives.matrix_marker import matrix_marker
from plotext._signal.point import point_class
from plotext._constants.numerical import binary
from plotext._correct import label as correct_label
from plotext._correct import pixel as correct_pixel
from plotext._correct import axis as correct_axis
from plotext._settings import defaults


# Labels container: holds title, x labels and y labels plus a pixel
class labels_class:

    # Initialize settings and pixel
    def __init__(self):
        self.clear_settings()
        self.set_pixel()

    # Reset all labels
    def clear_settings(self):
        self._x = [None, None]
        self._y = [None, None]
        self._title = None
        return self

    # Reset pixel to label default
    def clear_pixel(self):
        self._pixel.clone(defaults.pixels["label"])
        return self

    # Get label for given axis and side
    def get(self, axis = 0, side = 0):
        return self._y[side] if axis else self._x[side]

    # Public getter for x labels
    def get_x(self, side = 0):
        return self._x[side]

    # Public getter for y labels
    def get_y(self, side = 0):
        return self._y[side]

    # Public getter for title
    def get_title(self):
        return self._title

    # Public getter for pixel
    def get_pixel(self):
        return self._pixel

    # Set label on an axis and side
    def set_label(self, label = None, axis = 0, side = 0):
        if axis:
            self._y[side] = label
        else:
            self._x[side] = label
        return self

    # Batch setter across axes and sides
    def set(self, label = None, axes = 0, sides = 0):
        label = correct_label.label(label, self._pixel)
        axes = correct_axis.axes(axes)
        sides = correct_axis.sides(axes, sides)
        [self.set_label(label = label, axis = axis, side = side) for axis in axes for side in sides]
        return self

    # Set plot title
    def set_title(self, label):
        self._title = correct_label.label(label, self._pixel)
        return self

    # Set pixel for labels
    def set_pixel(self, pixel = None, default_pixel = None):
        self._pixel = correct_pixel.pixel(pixel, defaults.pixels["label"])
        return self

    # Check if upper region is present
    def upper_present(self):
        return self._title is not None or self._x[1] is not None

    # Check if lower region is present
    def lower_present(self):
        return self._x[0] is not None or self._y[0] is not None or self._y[1] is not None

    # Paint title + upper x-label onto the matrix at (bar_col, bar_row), spanning bar_width.
    def draw_upper_bar(self, matrix, bar_col, bar_row, bar_width):
        part = matrix_class(bar_width, 1, self._pixel)
        p = point_class(bar_width // 2, 0, matrix_marker(self.get(0, 1), ha = 0)) if self.get(0, 1) is not None else None
        part._insert_point(p) if p is not None else None
        p = point_class(bar_width // 2, 0, matrix_marker(self._title,     ha = 0)) if self._title is not None else None
        title_centered = part._insert_point(p) if p is not None else False
        p = point_class(0, 0, matrix_marker(self._title, ha = -1)) if self._title is not None and not title_centered else None
        part._insert_point(p) if p is not None else None
        matrix._insert_matrix(bar_col, bar_row, part)
        return self

    # Paint y-labels (corners) + lower x-label onto the matrix at (bar_col, bar_row), spanning bar_width.
    def draw_lower_bar(self, matrix, bar_col, bar_row, bar_width):
        part = matrix_class(bar_width, 1, self._pixel)
        p = point_class(0,              0, matrix_marker(self.get_y(0),   ha = -1)) if self.get(1, 0)  is not None else None
        part._insert_point(p) if p is not None else None
        p = point_class(bar_width // 2, 0, matrix_marker(self.get(0, 0),  ha =  0)) if self.get_x(0)   is not None else None
        part._insert_point(p) if p is not None else None
        p = point_class(bar_width - 1,  0, matrix_marker(self.get(1, 1),  ha =  1)) if self.get_y(1)   is not None else None
        part._insert_point(p) if p is not None else None
        matrix._insert_matrix(bar_col, bar_row, part)
        return self

    # Clone label values from another labels_class
    def clone(self, labels):
        [self.set_label(labels.get(a, s), a, s) for s in binary for a in binary]
        self.set_title(labels._title)
        return self

    # Representation string with all attributes in one line
    def __repr__(self):
        return f"Plotext Labels: x: {self._x}, y: {self._y}, title: {self._title}, pixel: {self._pixel}"