from ._matrix import *
from ._pixel import *

class bar(matrix):
    def __init__(self, width = 0, background = None):
        matrix.__init__(self, width, 1, pixel(background = background))

    def set_left(self, label = None):
        return self._insert_colorize(0, 0, label, ha = -1, check_space = 1) if label is not None else None

    def set_center(self, label = None):
        return self._insert_colorize(self.get_width() // 2, 0, label, ha = 0, check_space = 1) if label is not None else None

    def set_right(self, label = None):
        return self._insert_colorize(self.get_width() - 1, 0, label, ha = 1, check_space = 1) if label is not None else None

    def set_title(self, label = None):
        self.set_left(label)  if not self.set_center(label) else None