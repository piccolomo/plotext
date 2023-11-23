from plotext._default import default_figure
from plotext._matrix import matrix_class, join_matrices, pixel_class
from plotext._terminal import terminal_class
from plotext._list import fit_sizes, get_sizes
from plotext._log import log
from plotext._terminal import terminal
from plotext._settings import settings_class

# temp
from plotext._colorize import colorize
from plotext._string import get_frame


class _figure_class():
    def __init__(self, parent = None, width = None, height = None):
        self._set_parent(parent)
        
        self._set_limit_size()
        self._set_size(width, height)
        
        self._update_slots_max()
        self._set_subplots(1, 1)
        
        self.take_maximum_size()
        self._set_size_direction()

        self._create_matrix()
        self._create_settings()
        
##############################################
#########    Family Functions    #############
##############################################

    def _set_parent(self, parent = None):
        self._parent = parent
        self._is_master = isinstance(parent, terminal_class)
        self._set_active(self) if self._is_master else None

    def get_parent(self, level = 1):
        return self if level == 0 or self._is_master else self._parent if level == 1 else self.get_parent(1).get_parent(level - 1)

    def _get_master(self):
        return self.get_parent(-1)

    def _set_position(self, row = None, col = None):
        self._row = row
        self._col = col
        self.position = (row, col)

    def _get_position(self):
        return 'main()' if self._is_master else self.get_parent().get_position() + '.subplot' + str(self.position)

    def _set_active(self, figure = None):
        self._get_master().active = figure 

    def _get_active(self):
        return self.get_master().active

##############################################
###########    Size Functions    #############
##############################################

    def _set_limit_size(self, width = None, height = None):
        self._limit_width = True if not self._is_master else default_figure.limit_width if width is None else bool(width)
        self._limit_height = True if not self._is_master else default_figure.limit_height if height is None else bool(height)
        self._limit_size = [self._limit_width, self._limit_height]

    def _set_size(self, width = None, height = None):
        self._size_called = [width, height]
        width_max, height_max = self._parent.size
        width_none, height_none = width is None, height is None
        self.width = width_max if width_none or (width >  width_max and self._limit_width) else int(width)
        self.height = height_max if height_none or (height >  height_max and  self._limit_height) else int(height)
        self.size = [self.width, self.height]

    def _update_size(self):
        self._set_size(*self._size_called)

    def _update_terminal_size(self):
        terminal_size = terminal.size
        terminal.update_size()
        self._update_size() if terminal_size != terminal.size else None
        self._clear_sizes() if terminal_size != terminal.size else None

    def _get_size_string(self):
        return "{:<5}{} ".format(self.width, self.height)

    def _set_size_direction(self, direction = None):
        self._size_direction = default_figure.size_direction if direction is None else 1 if int(direction) > 0 else -1

##############################################
#########    Subplots Functions    ###########
##############################################

    def _update_slots_max(self):
        self._rows_max = self.height // 3
        self._cols_max = self.width // 3
        self._slots_max = [self._cols_max, self._rows_max]

    def _set_subplots(self, rows = None, cols = None):
        self._set_slots(rows, cols)
        self._create_subplots()
        
    def _set_slots(self, rows = None, cols = None):
        rows = 1 if rows is None else int(abs(rows))
        cols = 1 if cols is None else int(abs(cols))
        (rows, cols) = (0, 0) if rows * cols == 1 else (rows, cols)
        self._rows = min(rows, self._rows_max)
        self._cols = min(cols, self._cols_max)
        self._slots = [self._cols, self._rows]
        self._Rows = list(range(1, self._rows + 1))
        self._Cols = list(range(1, self._cols + 1))
        self._Positions = [(row, col) for row in self._Rows for col in self._Cols]
        self._subplots_absent = self._rows * self._cols == 0
        self._subplots_present = not self._subplots_absent

    def _update_slots(self):
        self._set_slots(self._rows, self._cols)

    def _create_subplots(self):
        widths, heights = get_sizes(self.width, self._cols), get_sizes(self.height, self._rows)
        self._figure = [[_figure_class(self, widths[col - 1], heights[row - 1]) for col in self._Cols] for row in self._Rows]
        [self._get_subplot(row, col)._set_position(row, col) for col in self._Cols for row in self._Rows]

    def _harmonize_subplots(self):
        widths = [self._max_or_min([self._get_subplot(row, col).width for row in self._Rows]) for col in self._Cols]
        heights = [self._max_or_min([self._get_subplot(row, col).height for col in self._Cols]) for row in self._Rows]
        widths = fit_sizes(widths, self.width, self._size_direction)
        heights = fit_sizes(heights, self.height, self._size_direction) 
        [self._get_subplot(row, col)._set_size(widths[col - 1], heights[row - 1]) for col in self._Cols for row in self._Rows]

    def _get_subplot(self, row = None, col = None):
        valid = self._subplots_present and row in self._Rows and col in self._Cols
        log.warning('dummy figure accessed') if not valid else None
        return self._figure[row - 1][col - 1] if valid else _figure_class(self)

    def print_subplots(self):
        print(self.get_size_string(), self.get_position())
        [self._get_subplot(*pos).print_subplots() for pos in self._Positions]

    def _refresh_subplots(self):
        self._update_slots_max()
        self._update_slots()
        self._clear_sizes()
        [self._get_subplot(*pos)._refresh_subplots() for pos in self._Positions]
        #self.harmonize_subplots()

    def _refresh_matrix(self):
        if self._matrix.size() == self.size:
            self._matrix.clear()
        else:
            self._matrix = matrix_class(*self.size)
        p = pixel_class().set_background_color(self._settings.axes_color)
        self._matrix.fill(p)
        

##############################################
#########    Create Functions    #############
##############################################

    def _create_matrix(self):
        self._matrix = matrix_class(0, 0)

    def _create_settings(self):
        self._settings = settings_class() if self._is_master else self._parent._settings

##############################################
###########    User Functions    #############
##############################################

    def limit_size(self, width = None, height = None):
        self._set_limit_size(width, height)
        self._update_size()
        return self
        
    def plot_size(self, width = None, height = None, direction = None):
        self._set_size(width, height)
        self._set_size_direction(direction)
        self._parent.harmonize_subplots() if not self._is_master else None
        self._refresh_subplots()
        return self
    plotsize = plot_size

    def take_minimum_size(self):
        self._max_or_min = lambda data: min(data, default = 0)

    def take_maximum_size(self):
        self._max_or_min = lambda data: max(data, default = 0)

    def subplots(self, rows = None, cols = None):
        self._set_subplots(rows, cols)
        return self

    def subplot(self, row = None, col = None):
        row = 1 if row is None else int(abs(row))
        col = 1 if col is None else int(abs(col))
        row = min(row, self._rows_max)
        col = min(col, self._cols_max)
        plot = self._get_subplot(row, col)
        self._set_active(plot)
        return plot

    def ticks_color(self, color = None):
        self._settings.set_ticks_color(color)
        [self._get_subplot(*pos).ticks_color(label) for pos in self._Positions]
        return self

    def axes_color(self, color = None):
        self._settings.set_axes_color(color)
        [self._get_subplot(*pos).axes_color(label) for pos in self._Positions]
        return self
    
    def title(self, label = None):
        self._settings.title(label)
        [self._get_subplot(*pos).title(label) for pos in self._Positions]
        return self 

    def xlabel(self, label = None, yside = None):
        self._settings.xlabel(label, yside)
        [self._get_subplot(*pos).ylabel(label, yside) for pos in self._Positions]
        return self 

    def ylabel(self, label = None, yside = None):
        self._settings.ylabel(label, yside)
        [self._get_subplot(*pos).ylabel(label, yside) for pos in self._Positions]
        return self 

##############################################
###########    Clear Functions    ############
##############################################

    def _clear_matrix(self):
        self._matrix.clear()

    def clear_size(self):
        self._set_size()
        self._clear_sizes()
        
    def _clear_sizes(self):
        widths, heights = get_sizes(self.width, self._cols), get_sizes(self.height, self._rows)
        [self._get_subplot(row, col)._set_size(widths[col - 1], heights[row - 1]) for col in self._Cols for row in self._Rows]

    def clear_subplots(self):
        self.subplots(0, 0)

    def clear_settings(self):
        self._settings.clear()

    def clear_figure(self):
        self.clear_size()
        self.clear_subplots()
        self.clear_settings()
        return self
    clf = clear_figure
        
##############################################
###########    Draw Functions    #############
##############################################

    def _draw(self, *args, **kwargs):
        self.signals.add_normal_signal(*args, **kwargs)

##############################################
###########    Build Functions    ############
##############################################

    def _show(self):
        self._update_terminal_size()
        self._build()
        print(self._matrix.get_string())

    def _build(self):
        self._build_plot() if self._subplots_absent else None
        self._build_subplots() if self._subplots_present else None

    def _build_subplots(self):
        [self._get_subplot(*pos)._build() for pos in self._Positions]
        self._join_subplots()
        
    def _join_subplots(self):
        matrices = [[self._get_subplot(row, col)._matrix for col in self._Cols] for row in self._Rows]
        self._matrix = join_matrices(matrices) if self._subplots_present else self._matrix
        
    def _build_plot(self):
        # Tools
        self._refresh_matrix()
        self._settings.update()
        width_half = self.width // 2
        width_canvas = self.width
        height_canvas = self.height
        
        # Upper Bar 
        left = self._settings.bar_upper.left
        center = self._settings.bar_upper.center
        
        height_test = height_canvas > 0
        left_test = left is not None and height_test
        center_test = center is not None and height_test
        self._matrix.insert_m(0, 0, left, "left", check_space = True) if left_test  else None
        self._matrix.insert_m(width_half, 0, center, "center", check_space = True) if center_test else None
        
        bar_upper_height = int(left_test or center_test)
        height_canvas -= bar_upper_height

        # Lower Bar
        left = self._settings.bar_lower.left
        center = self._settings.bar_lower.center
        right = self._settings.bar_lower.right

        height_test = height_canvas > 0
        left_test = left is not None and height_test
        center_test = center is not None and height_test
        right_test = right is not None and height_test
        
        self._matrix.insert_m(0, self.height - 1, left, "left", check_space = True) if left_test  else None
        self._matrix.insert_m(width_half, self.height - 1, center, "center", check_space = True) if center_test else None
        self._matrix.insert_m(self.width - 1, self.height - 1, right, "right", check_space = True) if right_test else None

        bar_lower_height = int(left_test or center_test or right_test)
        height_canvas -= bar_lower_height 



