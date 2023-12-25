from plotext._default import default_subplot
from plotext._subplots import subplots_class


class subplot_class(subplots_class):
    def __init__(self, parent = None, row = None, col = None):
        self._set_parent(parent)
        self._set_position(row, col)
        self._set_size()
        super(subplot_class, self).__init__()

# Family Functions

    def _set_parent(self, parent = None):
        self._parent = parent

    def _set_position(self, row = None, col = None):
        self._row = row; self._col = col
        self._pos = [self._row, self._col]

    def _get_position(self):
        return '(' + ', '.join(map(str, self._pos)) + ')'

    def _get_parent(self, level = 1):
        return self if level == 0 else self._parent if level == 1 else self._get_parent(1)._get_parent(level - 1) if self._parent is not None else self

    def _get_terminal(self):
        return self._get_parent(-1)

    def _get_master(self):
        return self._get_terminal()._master

    def _set_active(self, subplot):
        self._get_master()._set_active(subplot)

# Size Functions

    def plot_size(self, width = None, height = None):
        self._set_size(width, height)
        self._parent._harmonize_sizes()
        self.clear_sizes()
        return self

    def _set_size(self, width = None, height = None):
        self._width = None if width is None else max(0, min(width, self._parent._width))
        self._height = None if height is None else max(0, min(height, self._parent._height))
        self._size = self._width, self._height

    def update_size(self):
        self._set_size(*self._size)

# Subplots Functions

    def __del__(self):
       del self._subplots
       del self

    def __repr__(self):
        return self._parent.__repr__() + '.subplot' + self._get_position()
