# A figure is a general container of either a plot (called monitor) or nested figures (also called subplots)
# This creates a hierarchy of figures, where master is the main global figure, and parent is the figure containing (or above) the one considered
# The active figure is the one (in the hierarchy) that can be addressed with further plotext commands
# If a figure has no sub figures, then it is used for data plotting, otherwise its sub figures are checked for data plotting

import shutil
from plotext._default import default_figure, default_axis
from plotext._axes import xaxis_class, yaxis_class
from plotext._matrix import matrix_class, join_matrices
from plotext._canvas import canvas_class
# from plotext._signal import signals_class

class _figure_class():
    def __init__(self, parent = None, width = None, height = None):
        self.set_parent(parent)
        
        self.set_limit_size()
        self.update_size_max()
        self.set_size(width, height)
        
        self.update_slots_max()
        self.set_slots(1, 1)
        self.update_subplots()
        self.take_max()

        self.create_axes()
        self.canvas = canvas_class()
        # axes, canvas

##############################################
#########    Family Functions    #############
##############################################

    def set_parent(self, parent = None):
        self.parent = parent
        self.is_master = parent is None
        if self.is_master:
            self.active = self

    def set_position(self, row = None, col = None):
        self.row = row
        self.col = col
        self.position = (row, col)

    def get_position(self):
        return 'main()' if self.is_master else self.get_parent().get_position() + '.subplot' + str(self.position)

    def get_parent(self, level = 1):
        return self if level == 0 or self.is_master else self.parent if level == 1 else self.get_parent(1).get_parent(level - 1)

    def get_master(self):
        return self.get_parent(-1)

    def get_active(self):
        return self.get_master().active

    def set_active(self, figure = None):
        master = self.get_master()
        master.active = master.active if figure is None else figure 

##############################################
###########    Size Functions    #############
##############################################

    def set_limit_size(self, width = None, height = None):
        self.limit_width = True if not self.is_master else default_figure.limit_width if width is None else bool(width)
        self.limit_height = True if not self.is_master else default_figure.limit_height if height is None else bool(height)
        self.limit_size = [self.limit_width, self.limit_height]

    def update_size_max(self):
        width_parent, height_parent = terminal_size() if self.is_master else self.parent.size
        self.width_max = width_parent if self.limit_width else None
        self.height_max = height_parent if self.limit_height else None
        self.size_max = [self.width_max, self.height_max]

    def set_size(self, width = None, height = None):
        width_none = width is None; width_max_none = self.width_max is None
        height_none = height is None; height_max_none = self.height_max is None
        self.width = self.width_max if width_none or (not width_max_none and width > self.width_max) else int(width) if not width_none else None
        self.height = self.height_max if height_none or (not height_max_none and height > self.height_max) else int(height) if not height_none else None
        self.size = [self.width, self.height]

    def get_size(self):
        return ''.join([str(self.width).ljust(5), str(self.height).ljust(3)])

##############################################
#########    Subplots Functions    ###########
##############################################

    def update_slots_max(self):
        self.rows_max = self.height // 3
        self.cols_max = self.width // 3
        self.slots_max = [self.rows_max, self.cols_max]

    def set_slots(self, rows = None, cols = None):
        rows = 1 if rows is None else int(abs(rows))
        cols = 1 if cols is None else int(abs(cols))
        (rows, cols) = (0, 0) if rows * cols == 1 else (rows, cols)
        self.rows = min(rows, self.rows_max)
        self.cols = min(cols, self.cols_max)
        self.Rows = list(range(1, self.rows + 1))
        self.Cols = list(range(1, self.cols + 1))
        self.slots = [self.rows, self.cols]
        self.has_subplots = self.rows * self.cols != 0

    def refresh_slots(self):
        self.set_slots(self.rows, self.cols)

    def update_subplots(self):
        widths = get_sizes(self.width, self.cols)
        heights = get_sizes(self.height, self.rows)
        self.plot = [[_figure_class(self, widths[col - 1], heights[row - 1]) for col in self.Cols] for row in self.Rows]
        [[self.plot[row - 1][col - 1].set_position(row, col) for col in self.Cols] for row in self.Rows]

    def get_subplot(self, row = None, col = None):
        valid = self.has_subplots and row in self.Rows and col in self.Cols
        return self.plot[row - 1][col - 1] if valid else None

    def select_subplots(self):
        self.plot = [[self.plot[row - 1][col - 1] for col in self.Cols] for row in self.Rows]

    def print_subplots(self):
        #print('w    h') if self.is_master else None
        print(self.get_size(), self.get_position())
        [[f.print_subplots() for f in plots] for plots in self.plot] if self.has_subplots else None

##############################################
#####    Subplots / Size Functions    ########
##############################################

    def take_min(self): # in a matrix of subplots the minimum height/width will be considered for each row/column
        self.max_or_min = lambda data: min(data, default = 0)

    def take_max(self): # in a matrix of subplots the minimum height/width will be considered for each row/column
        self.max_or_min = lambda data: max(data, default = 0)

    def refresh_subplots_size_max(self):
        [self.get_subplot(row, col).update_size_max() for col in self.Cols for row in self.Rows]

    def harmonize_sizes(self):
        widths = [self.max_or_min([self.get_subplot(row, col).width for row in self.Rows]) for col in self.Cols]
        heights = [self.max_or_min([self.get_subplot(row, col).height for col in self.Cols]) for row in self.Rows]
        widths = fit_sizes(widths, self.width)
        heights = fit_sizes(heights, self.height)
        [self.get_subplot(row, col).set_size(widths[col - 1], heights[row - 1]) for col in self.Cols for row in self.Rows]

    def refresh_sizes(self):
        self.update_slots_max()
        self.refresh_slots()
        self.select_subplots()
        self.refresh_subplots_size_max()
        self.harmonize_sizes()

    def verify_sizes(self):
        widths = [[self.get_subplot(row, col).width for row in self.Rows] for col in self.Cols]
        heights = [[self.get_subplot(row, col).height for col in self.Cols] for row in self.Rows]
        widths_constant = all(map(is_constant, widths)) 
        heights_constant = all(map(is_constant, heights))
        widths_less = sum([el[0] for el in widths]) == self.width
        heights_less = sum([el[0] for el in heights]) == self.height
        return not self.has_subplots or all([widths_constant, widths_less, heights_constant, heights_less])

##############################################
########    User Size Functions    ###########
##############################################

    def limit_size(self, width = None, height = None):
        self.set_limit_size(width, height)
        self.update_size_max()

    def plot_size(self, width = None, height = None):
        self.set_size(width, height)
        self.parent.refresh_sizes() if self.parent is not None else None
        self.refresh_sizes()

##############################################
######    User Subplots Functions    #########
##############################################

    def subplots(self, rows, cols):
        self.set_slots(rows, cols)
        self.update_subplots()
        return self
        
    def subplot(self, row = None, col = None):
        row = 1 if row is None else int(abs(row))
        col = 1 if col is None else int(abs(col))
        row = min(row, self.rows_max)
        col = min(col, self.cols_max)
        plot = self.get_subplot(row, col)
        self.set_active(plot)
        return plot

##############################################
############   Axes Functions    #############
##############################################

    def create_axes(self):
        self.xaxis_lower = xaxis_class('lower')
        self.xaxis_upper = xaxis_class('upper')
        self.yaxis_left  = yaxis_class('left')
        self.yaxis_right = yaxis_class('right')
        self.r2 = [1, 2]

    def get_xaxis(self, xside = None):
        xside = self.correct_xside(xside)
        return self.xaxis_lower if xside == default_axis.xside else self.xaxis_upper

    def get_yaxis(self, yside = None):
        yside = self.correct_yside(yside)
        return self.yaxis_left if yside == default_axis.yside else self.yaxis_right

    def correct_xside(self, xside = None):
        return self.xaxis_lower.correct_side(xside)
    
    def correct_yside(self, yside = None):
        return self.yaxis_left.correct_side(yside)

    def set_xaxes(self, lower = None, upper = None):
        self.get_xaxis(1).set_show_axis(lower)
        self.get_xaxis(2).set_show_axis(upper)

    def set_yaxes(self, left = None, right = None):
        self.get_yaxis(1).set_show(left)
        self.get_yaxis(2).set_show(right)

    def set_title(self, label = None):
        self.get_xaxis(2).set_title(label)

    def set_xlabel(self, label = None, xside = None):
        self.get_xaxis(xside).set_label(label)
        
    def set_ylabel(self, label = None, yside = None):
        self.get_yaxis(yside).set_label(label)

    def set_xlim(self, left = None, right = None, xside = None):
        self.get_xaxis(xside).set_lim(left, right)
        
    def set_ylim(self, lower = None, upper = None):
        self.get_yaxis(yside).set_lim(lower, upper)

    def set_xscale(self, scale = None, xside = None):
        self.get_xaxis(xside).set_scale(scale)

    def set_yscale(self, scale = None, yside = None):
        self.get_yaxis(yside).set_scale(scale)

    def set_xticks(self, ticks = None, labels = None, xside = None):
        self.get_xaxis(xside).set_ticks(ticks, labels)

    def set_yticks(self, ticks = None, labels = None, yside = None):
        self.get_yaxis(yside).set_ticks(ticks, labels)

    def set_xfrequency(self, frequency = None, xside = None):
        self.get_xaxis(xside).set_frequency(frequency)

    def set_yfrequency(self, frequency = None, yside = None):
        self.get_yaxis(yside).set_frequency(frequency)

    def set_xdirection(self, direction = None, xside = None):
        self.get_xaxis(xside).set_direction(direction)

    def set_ydirection(self, direction = None, yside = None):
        self.get_yaxis(yside).set_direction(direction)

    def set_xgrid(self, grid = None, xside = None):
        self.get_xaxis(xside).set_grid(grid)

    def set_ygrid(self, grid = None, yside = None):
        self.get_yaxis(yside).set_grid(grid)
        
    def set_axis_color(self, color = None):
        [self.get_xaxis(xside).set_axis_color(color) for xside in self.r2]
        [self.get_yaxis(yside).set_axis_color(color) for yside in self.r2]

    def set_ticks_color(self, color = None):
        [self.get_xaxis(xside).set_ticks_color(color) for xside in self.r2]
        [self.get_yaxis(yside).set_ticks_color(color) for yside in self.r2]

    def set_ticks_style(self, color = None):
        [self.get_xaxis(xside).set_ticks_style(color) for xside in self.r2]
        [self.get_yaxis(yside).set_ticks_style(color) for yside in self.r2]

    def set_canvas_color(self, color = None):
        self.canvas.set_canvas_color(color)
        
##############################################
##########    Matrix Functions    ############
##############################################

    def get_matrix_string(self):
        return self.matrix.get_string()

    def join_matrices(self):
        matrices = [[self.get_subplot(row, col).matrix for col in self.Cols] for row in self.Rows]
        self.matrix = join_matrices(matrices) if self.has_subplots else self.matrix
        self.matrices = matrices

##############################################
###########    Plot Functions    #############
##############################################

    def update_canvas_size(self):
        [self.get_xaxis(i).update_height() for i in self.r2]
        heigth_xaxes = sum([self.get_xaxis(i).get_height() for i in self.r2])
        self.height_canvas = self.height - heigth_xaxes
        
        [self.get_yaxis(i).update_width() for i in self.r2]
        width_yaxes = sum([self.get_yaxis(i).get_width() for i in self.r2])
        self.width_canvas = self.width - width_yaxes
        self.canvas.set_size(self.width_canvas, self.height_canvas)

    def set_axes_sizes(self):
        [self.get_xaxis(i).set_width(self.width) for i in self.r2]
        [self.get_xaxis(i).set_width_canvas(self.width_canvas) for i in self.r2]
        [self.get_yaxis(i).set_height(self.height_canvas) for i in self.r2]
         
    def build_matrix(self):
        [self.get_xaxis(i).build_matrix() for i in self.r2]
        [self.get_yaxis(i).build_matrix() for i in self.r2]
        self.canvas.build_matrix()
        middle = self.yaxis_left.matrix.horizontal_stack(self.canvas.matrix)
        middle = middle.horizontal_stack(self.yaxis_right.matrix)
        matrix = self.xaxis_upper.matrix.vertical_stack(middle)
        self.matrix = matrix.vertical_stack(self.xaxis_lower.matrix)
        
         
    def build(self):
        self.update_canvas_size()
        self.set_axes_sizes()
        self.build_matrix()
         
        [[plot.build() for plot in row_plots] for row_plots in self.plot]
        self.join_matrices()
        
    def show(self):
        self.build()
        print(self.get_matrix_string())


    # def reset_subplots_sizes(self):
    #     [self.get_subplot(row, col).reset_size() for col in self.Cols for row in self.Rows]

    # def draw(self):
    #     [[f.draw() for f in plots] for plots in self.plot] if self.plot is not None else None
    #     self._draw() if self.plot is None else None
    


#     def _draw(self, *args, **kwargs):
#         self.monitor.draw(*args, **kwargs) if self._no_sub_figures else [[self.get_sub_figure(row, col)._draw(*args, **kwargs) for col in self._Cols] for row in self._Rows]

#     def scatter(self, *args, **kwargs):
#        self._draw(*args, **kwargs, lines = False)

#     def plot(self, *args, **kwargs):
#         self._draw(*args, **kwargs, lines = True)
        
##############################################
##############    Utilities    ###############
##############################################

def fit_sizes(sizes, size_max): # given certain widths (or heights) it sets them so to equate max value
    bins = len(sizes)
    current_bin = bins - 1
    while sum(sizes) != size_max and current_bin >= 0:
        other_sizes = sum([sizes[b] for b in range(bins) if b != current_bin])
        sizes[current_bin] = max(size_max - other_sizes, 0)
        current_bin -= 1
    return sizes

def get_sizes(size_max, bins):
    return fit_sizes([size_max // bins if bins != 0 else size_max] * bins, size_max)

def terminal_size(): # it returns the terminal size as [width, height]
    try:
        width, height = shutil.get_terminal_size()
        return width, height - 2
    except OSError:
        return [None, None]

def is_constant(data):
    return all([el == data[0] for el in data])


