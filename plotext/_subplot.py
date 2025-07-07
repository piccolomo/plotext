from plotext._default import default_size_direction
from plotext._methods import *
#from plotext._log import log_class


class subplot_class:
    def __init__(self):
        self.clear()

    # Reset all settings and initialize subplots
    def clear(self):
        self.set_parent()
        self.set_size()
        self.set_position()
        self.set_size_direction()
        self.take_maximum_size()
        self.subplots()
        self.set_active()

    # Set parent subplot (None for master)
    def set_parent(self, parent = None):
        self.parent = parent
        return self

    # Set size with constraints based on parent and master status
    def set_size(self, width = None, height = None):
        width = None if width is None else max(0, width)
        height = None if height is None else max(0, height)

        self.width = width if width is None or (self.is_master() or self.parent.width is None) else min(width, self.parent.width)
        self.height = height if height is None or (self.is_master() or self.parent.height is None) else min(height, self.parent.height)
        return self

    # Set plot size and harmonize subplots sizes
    def plot_size(self, width = None, height = None):
        self.set_size(width, height)
        if self.has_subplots() and self.has_size():
            self.harmonize_sizes()
        if self.is_not_master():
            self.parent.harmonize_sizes()
        if self.has_size():
            self.initialize_subplots_sizes()
        return self

    # Harmonize widths and heights of subplots according to size direction
    def harmonize_sizes(self):
        widths = fit_sizes(self.get_widths(), self.width, self.size_direction)
        heights = fit_sizes(self.get_heights(), self.height, self.size_direction)
        for row, col in self.get_slots_range():
            self.get_subplot(row, col).set_size(widths[col - 1], heights[row - 1])

    # Initialize subplots sizes recursively
    def initialize_subplots_sizes(self):
        for pos in self.get_slots_range():
            self.get_subplot(*pos).set_size(None, None)
        widths = subplot_methods.set_none_sizes(self.get_widths(), self.width)
        heights = subplot_methods.set_none_sizes(self.get_heights(), self.height)
        for row, col in self.get_slots_range():
            self.get_subplot(row, col).set_size(widths[col - 1], heights[row - 1])
        for pos in self.get_slots_range():
            self.get_subplot(*pos).initialize_subplots_sizes()
        return self

    # Set position (row, col)
    def set_position(self, row = None, col = None):
        self.row = row
        self.col = col
        return self

    # Set size direction (+1 or -1)
    def set_size_direction(self, direction = None):
        self.size_direction = default_size_direction if direction is None else 1 if int(direction) > 0 else -1
        return self

    # Take maximum sizes when harmonizing
    def take_maximum_size(self):
        self.take_max = True
        return self

    # Take minimum sizes when harmonizing
    def take_minimum_size(self):
        self.take_max = False
        return self

    # Setup subplots grid and update
    def subplots(self, rows = None, cols = None):
        self.set_slots(rows, cols)
        self.update_subplots()
        if self.has_size():
            self.initialize_subplots_sizes()
        return self

    # Access a specific subplot and set it active
    def subplot(self, row = None, col = None):
        row = 1 if row is None else int(abs(row))
        col = 1 if col is None else int(abs(col))
        plot = self.get_subplot(row, col)
        self.set_active(plot)
        return plot

    # Set rows and columns with constraints
    def set_slots(self, rows = None, cols = None):
        rows = None if rows is None or self.height is None else min(rows, self.height // 3)
        cols = None if cols is None or self.width is None else min(cols, self.width // 3)
        if rows is not None and cols is not None and rows * cols == 1:
            rows, cols = 0, 0
        self.rows, self.cols = rows, cols
        self.slots = [rows, cols]
        return self

    # Set active subplot (master holds active)
    def set_active(self, plot = None):
        if self.is_master():
            self.active = plot
        else:
            self.get_master().set_active(plot)
        return self

    # Get active subplot
    def get_active(self):
        return self.active if self.is_master() else self.get_master().active

    # Update subplot panels grid
    def update_subplots(self):
        if self.no_subplots():
            self.panels = None
        else:
            self.panels = [[self.create_subplot(row, col) for col in self.get_cols_range()] for row in self.get_rows_range()]
        return self

    # Get parent at given level (0=self, 1=parent, etc.)
    def get_parent(self, level = 1):
        if level == 0:
            return self
        if level == 1:
            return self.parent
        if self.is_not_master():
            return self.get_parent(1).get_parent(level - 1)
        return self

    # Get master subplot (top-level parent)
    def get_master(self):
        return self.get_parent(-1)

    # Get nesting level (0 for master)
    def get_nest_level(self):
        return 0 if self.is_master() else self.get_parent().get_nest_level() + 1

    # Get (row, col) position
    def get_position(self):
        return self.row, self.col

    # Get (width, height) size
    def get_size(self):
        return self.width, self.height

    # Get range of rows
    def get_rows_range(self):
        rows = 0 if self.rows is None else self.rows
        return range(1, rows + 1)

    # Get range of columns
    def get_cols_range(self):
        cols = 0 if self.cols is None else self.cols
        return range(1, cols + 1)

    # Get list of all subplot positions (row, col)
    def get_slots_range(self):
        return [(row, col) for row in self.get_rows_range() for col in self.get_cols_range()]

    # Check if no subplots exist
    def no_subplots(self):
        return self.rows is None or self.cols is None or self.rows * self.cols == 0

    # Check if subplots exist
    def has_subplots(self):
        return not self.no_subplots()

    # Check if position is not set
    def no_position(self):
        return self.row is None or self.col is None

    # Check if size is not set
    def no_size(self):
        return self.width is None or self.height is None

    # Check if size is set
    def has_size(self):
        return not self.no_size()

    # Check if this is master subplot
    def is_master(self):
        return self.parent is None

    # Check if not master
    def is_not_master(self):
        return not self.is_master()

    # Create a new subplot instance
    def create_subplot(self, row = None, col = None):
        plot = self.__class__()
        plot.set_parent(self)
        plot.set_position(row, col)
        return plot

    # Get subplot at (row, col)
    def get_subplot(self, row, col):
        return self.panels[row - 1][col - 1]

    # Get widths of columns
    def get_widths(self):
        return [self.get_column_width(col) for col in self.get_cols_range()]

    # Get width of a specific column
    def get_column_width(self, col):
        if col in self.get_cols_range():
            return list_methods.get_extreme([self.get_subplot(row, col).width for row in self.get_rows_range()], self.take_max)
        return None

    # Get heights of rows
    def get_heights(self):
        return [self.get_row_height(row) for row in self.get_rows_range()]

    # Get height of a specific row
    def get_row_height(self, row):
        if row in self.get_rows_range():
            return list_methods.get_extreme([self.get_subplot(row, col).height for col in self.get_cols_range()], self.take_max)
        return None

    # Get sizes as nested list by rows and cols
    def get_sizes(self):
        widths = self.get_widths()
        heights = self.get_heights()
        return [[(widths[col - 1], heights[row - 1]) for col in self.get_cols_range()] for row in self.get_rows_range()]

    # Get unique ID string for this subplot
    def get_id(self, digits = None):
        digits = 100 if digits is None else digits
        return hex(id(self))[-digits:]

    # Get log string representing this subplot and subplots recursively
    def get_log(self):
        out = str(self)
        for row in self.get_rows_range():
            for col in self.get_cols_range():
                panel = self.get_subplot(row, col)
                out += '\n' + '   ' * self.get_nest_level() + '└──' + panel.get_log()
        return out

    # Print the log string
    def log(self):
        print(self.get_log())
        return self

    def __repr__(self):
        title = 'Master' if self.is_master() else 'Subplot'
        pos = None if self.no_position() else f'row {self.row}, col {self.col}'
        slots = None if self.no_subplots() else f'rows {self.rows}, cols {self.cols}'
        size = None if self.no_size() else f'height {self.height}, width {self.width}'
        id_str = f'id {self.get_id(4)}'
        parts = [el for el in [pos, size, slots, id_str] if el is not None]
        return f'{title}({", ".join(parts)})'