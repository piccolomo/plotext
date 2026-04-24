# Subplot class: manages subplot grid, sizes, positions and active subplot

from plotext._settings import defaults
from plotext._methods.subplot import fit_sizes, set_none_sizes
from plotext._methods.sequence import get_extreme


# Subplot container: handles parent/child nesting, slots and active subplot
class subplot_class:

    # Initialize with parent and clear settings
    def __init__(self, parent):
        self._set_parent(parent)
        self._clear()

    # Reset internal subplot state
    def _clear(self):
        self._set_size()
        self._set_position()
        self._set_size_direction()
        self._take_maximum_size()
        self._subplots()
        self._set_active(self)

    # Set parent object (None for top-level)
    def _set_parent(self, parent = None):
        self._parent = parent
        return self

    # Set width and height, clamped by parent when needed
    def _set_size(self, width = None, height = None):
        width = None if width is None else max(0, round(width))
        height = None if height is None else max(0, round(height))

        self._width = width if width is None or (self._is_master() or self._parent._width is None) else min(width, self._parent._width)
        self._height = height if height is None or (self._is_master() or self._parent._height is None) else min(height, self._parent._height)

        self._size = [self._width, self._height]
        return self

    # Set row and column for this subplot
    def _set_position(self, row = None, col = None):
        self._row = row
        self._col = col
        return self

    # Set size direction (+1 or -1)
    def _set_size_direction(self, direction = None):
        self._size_direction = defaults.size_direction if direction is None else 1 if int(direction) > 0 else -1
        return self

    # Prefer taking maximum sizes when harmonizing
    def _take_maximum_size(self):
        self._take_max = True
        return self

    # Prefer taking minimum sizes when harmonizing
    def _take_minimum_size(self):
        self._take_max = False
        return self

    # Set the number of rows and columns (with constraints)
    def _set_slots(self, rows = None, cols = None):
        rows = None if rows is None or self._height is None else min(rows, self._height // 3)
        cols = None if cols is None or self._width is None else min(cols, self._width // 3)
        if rows is not None and cols is not None and rows * cols == 1:
            rows, cols = 0, 0
        self._rows, self._cols = rows, cols
        self._slots = [rows, cols]
        return self

    # Set the active subplot (master stores the active)
    def _set_active(self, plot = None):
        if self._is_master():
            self._active = plot
        else:
            self.get_master()._set_active(plot)
        return self

    # Create the nested panels structure
    def _create_subplots(self):
        if self._no_subplots():
            self._panels = None
        else:
            self._panels = [[self._create_subplot(row, col) for col in self._get_cols_range()] for row in self._get_rows_range()]
        return self

    # Create a new subplot instance (row/col provided)
    def _create_subplot(self, row = None, col = None):
        plot = self.__class__(parent = self)
        plot._set_position(row, col)
        return plot

    # Set plot size and harmonize child sizes when needed
    def plot_size(self, width = None, height = None):
        self._set_size(width, height)
        if self._has_subplots() and self._has_size():
            self._harmonize_sizes()
        if self._is_sub_master():
            self._parent.harmonize_sizes()
        if self._has_size():
            self._initialize_subplots_sizes()
        return self

    # Activate and return a specific subplot
    def subplot(self, row = None, col = None):
        row = 1 if row is None else int(abs(row))
        col = 1 if col is None else int(abs(col))
        plot = self._get_subplot(row, col)
        self._set_active(plot)
        return plot

    # Create/update subplots structure and initialize sizes when needed
    def _subplots(self, rows = None, cols = None):
        self._set_slots(rows, cols)
        self._create_subplots()
        if self._has_size():
            self._initialize_subplots_sizes()
        self._set_active(self)
        return self

    # Harmonize widths and heights for child panels
    def _harmonize_sizes(self):
        widths = fit_sizes(self._get_widths(), self._width, self._size_direction)
        heights = fit_sizes(self._get_heights(), self._height, self._size_direction)
        for row, col in self._get_slots_range():
            self._get_subplot(row, col)._set_size(widths[col - 1], heights[row - 1])

    # Initialize sizes for children recursively
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

    # Return the active subplot
    def get_active(self):
        return self._active if self._is_master() else self.get_master()._active

    # Get parent at a given level (0 = self, 1 = immediate parent)
    def get_parent(self, level = 1):
        if level == 0:
            return self
        if level == 1:
            return self._parent
        parent = self.get_parent(1)
        if parent is None:
            return self
        else:
            return parent.get_parent(level - 1)

    # Find the master (top) subplot by walking parents
    def get_master(self):
        current = self
        for i in range(100):
            parent = current.get_parent(1)
            if parent._is_terminal():
                return current
            current = parent

    # Return terminal (the master parent's parent)
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

    # Range of rows
    def _get_rows_range(self):
        rows = 0 if self._rows is None else self._rows
        return range(1, rows + 1)

    # Range of columns
    def _get_cols_range(self):
        cols = 0 if self._cols is None else self._cols
        return range(1, cols + 1)

    # List of all (row, col) slots
    def _get_slots_range(self):
        return [(row, col) for row in self._get_rows_range() for col in self._get_cols_range()]

    # True when there are no subplots configured
    def _no_subplots(self):
        return self._rows is None or self._cols is None or self._rows * self._cols == 0

    # True when subplots exist
    def _has_subplots(self):
        return not self._no_subplots()

    # Check if position is unset
    def _no_position(self):
        return self._row is None or self._col is None

    # Check if size is unset
    def _no_size(self):
        return self._width is None or self._height is None

    # Check if size is set
    def _has_size(self):
        return not self._no_size()

    # Placeholder: whether this is terminal (override in terminal subclass)
    def _is_terminal(self):
        return False

    # Check if this is master (parent is terminal)
    def _is_master(self):
        return self._parent._is_terminal()

    # Check if this is a sub-master (neither terminal nor master)
    def _is_sub_master(self):
        return not self._is_terminal() and not self._is_master()

    # Return subplot at given (row, col)
    def _get_subplot(self, row, col):
        return self._panels[row - 1][col - 1]

    # Get column widths for all columns
    def _get_widths(self):
        return [self._get_column_width(col) for col in self._get_cols_range()]

    # Get width for a specific column
    def _get_column_width(self, col):
        if col in self._get_cols_range():
            return get_extreme([self._get_subplot(row, col)._width for row in self._get_rows_range()], self._take_max)
        return None

    # Get heights for all rows
    def _get_heights(self):
        return [self._get_row_height(row) for row in self._get_rows_range()]

    # Get height for a specific row
    def _get_row_height(self, row):
        if row in self._get_cols_range():
            return get_extreme([self._get_subplot(row, col)._height for col in self._get_cols_range()], self._take_max)
        return None

    # Get sizes as nested (rows x cols) list of (width, height)
    def _get_sizes(self):
        widths = self._get_widths()
        heights = self._get_heights()
        return [[(widths[col - 1], heights[row - 1]) for col in self._get_cols_range()] for row in self._get_rows_range()]

    # Return a short unique id for this subplot
    def _get_id(self, digits = None):
        digits = 100 if digits is None else digits
        return hex(id(self))[-digits:]

    # Get a log string including nested subplots
    def get_log(self, pad = None):
        out = str(self)
        current_level = self._get_nest_level()
        for row in self._get_rows_range():
            for col in self._get_cols_range():
                panel = self._get_subplot(row, col)
                out += '\n' + '  ' * current_level + '└─' + panel.get_log()
        return out

    # Print the log string
    def log(self):
        print(self.get_log())
        return self

    # Readable representation of the subplot
    def __repr__(self):
        title = 'Master' if self._is_master() else 'Subplot'
        pos = None if self._no_position() else f'row {self._row}, col {self._col}'
        slots = None if self._no_subplots() else f'rows {self._rows}, cols {self._cols}'
        size = None if self._no_size() else f'height {self._height}, width {self._width}'
        id_str = f'id {self._get_id(4)}'
        parts = [el for el in [pos, size, slots, id_str] if el is not None]
        return f'{title}({", ".join(parts)})'