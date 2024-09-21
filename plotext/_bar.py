from ._matrix import *
from ._pixel import *
from ._colorize import *


class bar(matrix):
    def __init__(self, width = 0, pixel = None):
        matrix.__init__(self, width, 1, pixel)

    def is_empty(self):
        return self._is_empty(0, self.get_width(), 0, 1)

    def insert(self, col, label, ha):
        change_color = 1 if isinstance(label, colorize) else 0
        return self._insert_string_aligned(col, 0, label, ha = ha, check_space = 1, change_color = change_color)

    def set_left(self, label = None):
        return self.insert(0, label, -1)

    def set_center(self, label = None):
        return self.insert(self.get_width() // 2, label, 0)

    def set_right(self, label = None):
        return self.insert(self.get_width() - 1, label, 1)

    def set_title(self, label = None):
        return True if self.set_center(label) else self.set_left(label)