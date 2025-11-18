from plotext._default import default_size_direction
from plotext._methods.subplot import *
#from plotext._log import log_class


class subplot_class:
    def __init__(self, parent):
        self._set_parent(parent)
        self._clear()

    # Reset all settings and initialize subplots
    def _clear(self):
        self._set_size()
        self._set_position()
        self._set_size_direction()
        self._take_maximum_size()
        self._subplots()
        self._set_active(self)

    # Set parent subplot (None for master)
    def _set_parent(self, parent = None):
        self._parent = parent
        return self

    # Set size with constraints based on parent and master status
    def _set_size(self, width = None, height = None):
        width = None if width is None else max(0, round(width))
        height = None if height is None else max(0, round(height))

        self._width = width if width is None or (self._is_master() or self._parent._width is None) else min(width, self._parent._width)
        self._height = height if height is None or (self._is_master() or self._parent._height is None) else min(height, self._parent._height)

        self._size = [self._width, self._height]
        return self

    # Set plot size and harmonize subplots sizes
    def plot_size(self, width = None, height = None):
        self._set_size(width, height)
        if self._has_subplots() and self._has_size():
            self._harmonize_sizes()
        if self._is_sub_master():
            self._parent.harmonize_sizes()
        if self._has_size():
            self._initialize_subplots_sizes()
        return self

    # Harmonize widths and heights of subplots according to size direction
    def _harmonize_sizes(self):
        widths = fit_sizes(self._get_widths(), self._width, self._size_direction)
        heights = fit_sizes(self._get_heights(), self._height, self._size_direction)
        for row, col in self._get_slots_range():
            self._get_subplot(row, col)._set_size(widths[col - 1], heights[row - 1])

    # Initialize subplots sizes recursively
    def _initialize_subplots_sizes(self):
        for pos in self._get_slots_range():
            self._get_subplot(*pos)._set_size(None, None)
        widths = set_none_sizes(self._get_widths(), self._width)
        heights = set_none_sizes(self._get_heights(), self._height)
        for row, col in self._get_slots_range():
            self._get_subplot(row, col)._set_size(widths[col - 1], heights[row - 1])
        for pos in self._get_slots_range():
            self._get_subplot(*pos)._initialize_subplots_sizes()
        return self

    # Set position (row, col)
    def _set_position(self, row = None, col = None):
        self._row = row
        self._col = col
        return self

    # Set size direction (+1 or -1)
    def _set_size_direction(self, direction = None):
        self._size_direction = default_size_direction if direction is None else 1 if int(direction) > 0 else -1
        return self

    # Take maximum sizes when harmonizing
    def _take_maximum_size(self):
        self._take_max = True
        return self

    # Take minimum sizes when harmonizing
    def _take_minimum_size(self):
        self._take_max = False
        return self

    # Setup subplots grid and update
    def _subplots(self, rows = None, cols = None):
        self._set_slots(rows, cols)
        self._create_subplots()
        if self._has_size():
            self._initialize_subplots_sizes()
        self._set_active(self)
        return self

    # Access a specific subplot and set it active
    def subplot(self, row = None, col = None):
        row = 1 if row is None else int(abs(row))
        col = 1 if col is None else int(abs(col))
        plot = self._get_subplot(row, col)
        self._set_active(plot)
        return plot

    # Set rows and columns with constraints
    def _set_slots(self, rows = None, cols = None):
        rows = None if rows is None or self._height is None else min(rows, self._height // 3)
        cols = None if cols is None or self._width is None else min(cols, self._width // 3)
        if rows is not None and cols is not None and rows * cols == 1:
            rows, cols = 0, 0
        self._rows, self._cols = rows, cols
        self._slots = [rows, cols]
        return self

    # Set active subplot (master holds active)
    def _set_active(self, plot = None):
        if self._is_master():
            self._active = plot
        else:
            self.get_master()._set_active(plot)
        return self

    # Get active subplot
    def get_active(self):
        return self._active if self._is_master() else self.get_master()._active

    # Update subplot panels grid
    def _create_subplots(self):
        if self._no_subplots():
            self._panels = None
        else:
            self._panels = [[self._create_subplot(row, col) for col in self._get_cols_range()] for row in self._get_rows_range()]
        return self

    # Get parent at given level (0=self, 1=parent, etc.)
    def get_parent(self, level = 1):
        if level == 0:
            return self
        if level == 1:
            return self._parent
        parent = self.get_parent(1)
        #print("--", self, parent)
        if parent is None:
            return self
        else:
            return parent.get_parent(level - 1)
            

    # Get master subplot (top-level parent)
    def get_master(self):
        current = self
        for i in range(100):
            parent = current.get_parent(1)
            if parent._is_terminal():
                return current
            current = parent

    def get_terminal(self):
        return self.get_master().get_parent(1)


    # Get nesting level (0 for master)
    def _get_nest_level(self):
        return 1 if self._is_master() else self._get_parent()._get_nest_level() + 1

    # Get (row, col) position
    def get_position(self):
        return self._row, self._col

    # Get (width, height) size
    def get_size(self):
        return self._width, self._height

    # Get range of rows
    def _get_rows_range(self):
        rows = 0 if self._rows is None else self._rows
        return range(1, rows + 1)

    # Get range of columns
    def _get_cols_range(self):
        cols = 0 if self._cols is None else self._cols
        return range(1, cols + 1)

    # Get list of all subplot positions (row, col)
    def _get_slots_range(self):
        return [(row, col) for row in self._get_rows_range() for col in self._get_cols_range()]

    # Check if no subplots exist
    def _no_subplots(self):
        return self._rows is None or self._cols is None or self._rows * self._cols == 0

    # Check if subplots exist
    def _has_subplots(self):
        return not self._no_subplots()

    # Check if position is not set
    def _no_position(self):
        return self._row is None or self._col is None

    # Check if size is not set
    def _no_size(self):
        return self._width is None or self._height is None

    # Check if size is set
    def _has_size(self):
        return not self._no_size()

    # Check if this is master subplot
    def _is_terminal(self):
        return False

    # Check if this is master subplot
    def _is_master(self):
        return self._parent._is_terminal()

    # Check if not master
    def _is_sub_master(self):
        return not self._is_terminal() and not self._is_master()

    # Create a new subplot instance
    def _create_subplot(self, row = None, col = None):
        plot = self.__class__(parent = self)
        plot._set_position(row, col)
        return plot

    # Get subplot at (row, col)
    def _get_subplot(self, row, col):
        return self._panels[row - 1][col - 1]

    # Get widths of columns
    def _get_widths(self):
        return [self._get_column_width(col) for col in self._get_cols_range()]

    # Get width of a specific column
    def _get_column_width(self, col):
        if col in self._get_cols_range():
            return list_methods.get_extreme([self._get_subplot(row, col)._width for row in self._get_rows_range()], self._take_max)
        return None

    # Get heights of rows
    def _get_heights(self):
        return [self._get_row_height(row) for row in self._get_rows_range()]

    # Get height of a specific row
    def _get_row_height(self, row):
        if row in self._get_rows_range():
            return list_methods.get_extreme([self._get_subplot(row, col)._height for col in self._get_cols_range()], self._take_max)
        return None

    # Get sizes as nested list by rows and cols
    def _get_sizes(self):
        widths = self._get_widths()
        heights = self._get_heights()
        return [[(widths[col - 1], heights[row - 1]) for col in self._get_cols_range()] for row in self._get_rows_range()]

    # Get unique ID string for this subplot
    def _get_id(self, digits = None):
        digits = 100 if digits is None else digits
        return hex(id(self))[-digits:]

    # Get log string representing this subplot and subplots recursively
    def _get_log(self, pad = None):
        out = str(self)
        current_level = self._get_nest_level()
        for row in self._get_rows_range():
            for col in self._get_cols_range():
                panel = self._get_subplot(row, col)
                out += '\n' + '  ' * current_level + '└─' + panel.get_log()
        return out

    # Print the log string
    def _log(self):
        print(self._get_log())
        return self

    def __repr__(self):
        title = 'Master' if self._is_master() else 'Subplot'
        pos = None if self._no_position() else f'row {self._row}, col {self._col}'
        slots = None if self._no_subplots() else f'rows {self._rows}, cols {self._cols}'
        size = None if self._no_size() else f'height {self._height}, width {self._width}'
        id_str = f'id {self._get_id(4)}'
        parts = [el for el in [pos, size, slots, id_str] if el is not None]
        return f'{title}({", ".join(parts)})'