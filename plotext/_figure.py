from plotext._terminal import terminal_class
from plotext._default import default_figure, default_axis
from plotext._axes import xaxis_class, yaxis_class, correct_xside, correct_yside
from plotext._matrix import matrix_class, join_matrices
from plotext._canvas import canvas_class
from plotext._color import no_color
from plotext._log import log
from plotext._signal import signals_class

class _figure_class():
    def __init__(self, parent = None, width = None, height = None):
        self.set_parent(parent)

        self.set_limit_size()
        self.set_size(width, height)
        
        self.update_subplots_max()
        self.set_subplots(1, 1)
        self.take_maximum_size()
        self.set_size_direction()

        self.create_axes()
        self.canvas = canvas_class()
        self.signals = signals_class()

##############################################
#########    Family Functions    #############
##############################################

    def set_parent(self, parent = None):
        self.parent = parent
        self.is_master = isinstance(parent, terminal_class)
        self.set_active(self) if self.is_master else None

    def get_parent(self, level = 1):
        return self if level == 0 or self.is_master else self.parent if level == 1 else self.get_parent(1).get_parent(level - 1)

    def get_master(self):
        return self.get_parent(-1)

    def set_position(self, row = None, col = None):
        self.row = row
        self.col = col
        self.position = (row, col)

    def get_position(self):
        return 'main()' if self.is_master else self.get_parent().get_position() + '.subplot' + str(self.position)

    def set_active(self, figure = None):
        self.get_master().active = figure 

    def get_active(self):
        return self.get_master().active

##############################################
###########    Size Functions    #############
##############################################

    def set_limit_size(self, width = None, height = None):
        self.limit_width = True if not self.is_master else default_figure.limit_width if width is None else bool(width)
        self.limit_height = True if not self.is_master else default_figure.limit_height if height is None else bool(height)
        self._limit_size = [self.limit_width, self.limit_height]

    def set_size(self, width = None, height = None):
        width_max, height_max = self.parent.size
        width_none, height_none = width is None, height is None
        self.width = width_max if width_none or (width >  width_max and self.limit_width) else int(width)
        self.height = height_max if height_none or (height >  height_max and  self.limit_height) else int(height)
        self.size = [self.width, self.height]

    def update_size(self):
        self.set_size(*self.size)

    def get_size_string(self):
        return "{:<5}{} ".format(self.width, self.height)

    def set_size_direction(self, direction = None):
        self._size_direction = default_figure.size_direction if direction is None else 1 if int(direction) > 0 else -1

##############################################
#########    Subplots Functions    ###########
##############################################

    def update_subplots_max(self):
        self.rows_max = self.height // 3
        self.cols_max = self.width // 3
        self.slots_max = [self.cols_max, self.rows_max]

    def set_subplots(self, rows = None, cols = None):
        self.set_subplots_grid(rows, cols)
        self.create_subplots()
        
    def set_subplots_grid(self, rows = None, cols = None):
        rows = 1 if rows is None else int(abs(rows))
        cols = 1 if cols is None else int(abs(cols))
        (rows, cols) = (0, 0) if rows * cols == 1 else (rows, cols)
        self.rows = min(rows, self.rows_max)
        self.cols = min(cols, self.cols_max)
        self.slots = [self.cols, self.rows]
        self.Rows = list(range(1, self.rows + 1))
        self.Cols = list(range(1, self.cols + 1))
        self.Positions = [(row, col) for row in self.Rows for col in self.Cols]
        self.subplots_absent = self.rows * self.cols == 0 
        self.subplots_present = not self.subplots_absent

    def update_subplots_grid(self):
        self.set_subplots_grid(self.rows, self.cols)

    def create_subplots(self):
        widths, heights = get_sizes(self.width, self.cols), get_sizes(self.height, self.rows)
        self.figure = [[_figure_class(self, widths[col - 1], heights[row - 1]) for col in self.Cols] for row in self.Rows]
        [self.get_subplot(row, col).set_position(row, col) for col in self.Cols for row in self.Rows]

    def harmonize_subplots(self):
        widths = [self.max_or_min([self.get_subplot(row, col).width for row in self.Rows]) for col in self.Cols]
        heights = [self.max_or_min([self.get_subplot(row, col).height for col in self.Cols]) for row in self.Rows]
        widths = fit_sizes(widths, self.width, self._size_direction)
        heights = fit_sizes(heights, self.height, self._size_direction) 
        [self.get_subplot(row, col).set_size(widths[col - 1], heights[row - 1]) for col in self.Cols for row in self.Rows]

    def get_subplot(self, row = None, col = None):
        valid = self.subplots_present and row in self.Rows and col in self.Cols
        log.warning('dummy figure accessed') if not valid else None
        return self.figure[row - 1][col - 1] if valid else _figure_class(self)

    def print_subplots(self):
        print(self.get_size_string(), self.get_position())
        [self.get_subplot(*pos).print_subplots() for pos in self.Positions]

    def refresh_subplots(self):
        self.update_subplots_max()
        self.update_subplots_grid()
        self.clear_sizes()
        [self.get_subplot(*pos).refresh_subplots() for pos in self.Positions]
        #self.harmonize_subplots()

##############################################
############   Axes Functions    #############
##############################################

    def create_axes(self):
        self.xaxis_lower = xaxis_class('lower') if self.is_master else self.parent.xaxis_lower.copy()
        self.xaxis_upper = xaxis_class('upper') if self.is_master else self.parent.xaxis_upper.copy()
        self.yaxis_left  = yaxis_class('left') if self.is_master else self.parent.yaxis_left.copy()
        self.yaxis_right = yaxis_class('right') if self.is_master else self.parent.yaxis_right.copy()
        self.r2 = [1, 2]

    def get_xaxis(self, xside = None):
        xside = correct_xside(xside)
        return self.xaxis_lower if xside == default_axis.xside else self.xaxis_upper

    def get_yaxis(self, yside = None):
        yside = correct_yside(yside)
        return self.yaxis_left if yside == default_axis.yside else self.yaxis_right

    def backup_axes(self):
        self.xaxis_lower.backup()
        self.xaxis_upper.backup()
        self.yaxis_left.backup()
        self.yaxis_right.backup()

    def restore_axes(self):
        self.xaxis_lower.restore()
        self.xaxis_upper.restore()
        self.yaxis_left.restore()
        self.yaxis_right.restore()
        
##############################################
###########    User Functions    #############
##############################################

    def limit_size(self, width = None, height = None):
        self.set_limit_size(width, height)
        self.update_size()
        return self
        
    def plot_size(self, width = None, height = None, direction = None):
        self.set_size(width, height)
        self.set_size_direction(direction)
        self.parent.harmonize_subplots() if not self.is_master else None
        self.refresh_subplots()
        return self
    plotsize = plot_size

    def take_minimum_size(self): # in a matrix of subplots the minimum height/width will be considered for each row/column
        self.max_or_min = lambda data: min(data, default = 0)

    def take_maximum_size(self): # in a matrix of subplots the minimum height/width will be considered for each row/column
        self.max_or_min = lambda data: max(data, default = 0)

    def subplots(self, rows = None, cols = None):
        self.set_subplots(rows, cols)
        return self

    def subplot(self, row = None, col = None):
        row = 1 if row is None else int(abs(row))
        col = 1 if col is None else int(abs(col))
        row = min(row, self.rows_max)
        col = min(col, self.cols_max)
        plot = self.get_subplot(row, col)
        self.set_active(plot)
        return plot

    def xaxes(self, lower = None, upper = None):
        self.get_xaxis(1).set_show_axis(lower)
        self.get_xaxis(2).set_show_axis(upper)
        [self.get_subplot(*pos).xaxes(lower, upper) for pos in self.Positions]
        return self

    def yaxes(self, left = None, right = None):
        self.get_yaxis(1).set_show_axis(left)
        self.get_yaxis(2).set_show_axis(right)
        [self.get_subplot(*pos).yaxes(left, right) for pos in self.Positions]
        return self
 
    def axis_color(self, color = None):
        [self.get_xaxis(xside).set_axis_color(color) for xside in self.r2]
        [self.get_yaxis(yside).set_axis_color(color) for yside in self.r2]
        return self

    def canvas_color(self, color = None):
        self.canvas.set_canvas_color(color)
        return self

##############################################
###########    Clear Functions    ############
##############################################

    def clear_sizes(self):
        widths, heights = get_sizes(self.width, self.cols), get_sizes(self.height, self.rows)
        [self.get_subplot(row, col).set_size(widths[col - 1], heights[row - 1]) for col in self.Cols for row in self.Rows]

    def clear_subplots(self):
        self.subplots(0, 0)

    def clear_axes(self):
        self.xaxis_lower.clear() 
        self.xaxis_upper.clear() 
        self.yaxis_left.clear() 
        self.yaxis_right.clear() 
        [self.get_subplot(*pos).clear_axes() for pos in self.Positions]

    def clear_canvas(self):
        self.canvas.clear()
        [self.get_subplot(*pos).clear_canvas() for pos in self.Positions]

    def clear_settings(self):
        self.clear_axes()
        self.clear_canvas()

    def clear_color(self):
        pass

    def clear_figure(self):
        self.clear_subplots()
        self.clear_settings()
        self.clear_color()
        return self

    clf = clear_figure
        
##############################################
###########    Draw Functions    #############
##############################################

    def draw(self, *args, **kwargs): # from draw() comes directly the functions scatter() and plot()
        self.signals.add_normal_signal(*args, **kwargs)
        # xside = kwargs.get("xside")
        # yside = kwargs.get("yside")
        
        # lines = kwargs.get("lines")
        # fillx = kwargs.get("fillx")
        # filly = kwargs.get("filly")
        # marker = kwargs.get("marker")
        # color = kwargs.get("color")
        # style = kwargs.get("style")
        # label = kwargs.get("label")

##############################################
###########    Build Functions    ############
##############################################

    def show(self):
        self.build()
        print(self.matrix.get_string())

    def build(self):
        self.build_plot() if self.subplots_absent else None
        self.build_subplots() if self.subplots_present else None

    def build_plot(self):
        self.backup_axes()
        self.set_parts()
        self.update_parts_matrices()
        self.join_parts_matrices()
        self.restore_axes()

    def build_subplots(self):
        [self.get_subplot(*pos).build() for pos in self.Positions]
        self.join_subplots_matrices()
        
##############################################
##########    Build Utilities    #############
##############################################

    def set_parts(self):

        # show x axis
        self.xaxis_lower.set_show_axis(False) if self.height < 1 else None
        self.xaxis_upper.set_show_axis(False) if self.height < 2 else None

        self.xaxis_lower.update_height()
        self.xaxis_upper.update_height()

        # show x ticks

        # show x labels

        # height canvas
        height_canvas = self.height - self.xaxis_lower.height - self.xaxis_upper.height

        # set y axis height
        self.yaxis_left.set_height(height_canvas)
        self.yaxis_right.set_height(height_canvas)

        # set y ticks height

        # yticks

        # show y axis
        self.yaxis_left.set_show_axis(False) if self.width < 1 else None
        self.yaxis_right.set_show_axis(False) if self.width < 2 else None

        self.yaxis_left.update_width()
        self.yaxis_right.update_width()
        

        # show y ticks

        # left, canvas, right widths
        width_left = self.yaxis_left.width
        width_right = self.yaxis_right.width
        width_canvas = self.width - width_left - width_right

        # x axis widths
        self.xaxis_upper.set_widths(width_left, width_canvas, width_right)
        self.xaxis_lower.set_widths(width_left, width_canvas, width_right)
        
        # canvas_size
        self.canvas.set_size(width_canvas, height_canvas)

        # restore axes
        

    def update_parts_matrices(self):
        # x labels matrix
        self.xaxis_lower.update_matrix()
        self.xaxis_upper.update_matrix()

        # x ticks matrix

        # x axis matrix
        
        # y ticks matrix
        
        # y axis matrix
        self.yaxis_left.update_matrix()
        self.yaxis_right.update_matrix()

        # canvas matrix
        self.canvas.update_matrix()

    def join_parts_matrices(self):
        upper = self.xaxis_upper.matrix
        middle = self.yaxis_left.matrix.horizontal_stack(self.canvas.matrix)
        middle = middle.horizontal_stack(self.yaxis_right.matrix)
        lower = self.xaxis_lower.matrix
        self.matrix = upper.vertical_stack(middle).vertical_stack(lower)
        
    def join_subplots_matrices(self):
        matrices = [[self.get_subplot(row, col).matrix for col in self.Cols] for row in self.Rows]
        self.matrix = join_matrices(matrices) if self.subplots_present else self.matrix

        
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
        
    # def verify_sizes(self):
    #     widths = [[self.get_subplot(row, col).width for row in self.Rows] for col in self.Cols]
    #     heights = [[self.get_subplot(row, col).height for col in self.Cols] for row in self.Rows]
    #     widths_constant = all(map(is_constant, widths)) 
    #     heights_constant = all(map(is_constant, heights))
    #     widths_less = sum([el[0] for el in widths]) == self.width
    #     heights_less = sum([el[0] for el in heights]) == self.height
    #     return not self.subplots_present or all([widths_constant, widths_less, heights_constant, heights_less])

##############################################
##############    Utilities    ###############
##############################################
from math import ceil, floor

def fit_sizes(sizes, size_max, direction = 1): # given certain widths (or heights) it sets them so to equate max value
    sizes = sizes[::direction]
    bins = len(sizes)
    current_bin = bins - 1
    while sum(sizes) != size_max and current_bin >= 0:
        other_sizes = sum([sizes[b] for b in range(bins) if b != current_bin])
        sizes[current_bin] = max(size_max - other_sizes, 0)
        current_bin -= 1
    return sizes[::direction]

def get_sizes(size_max, bins):
    return fit_sizes([size_max // bins if bins != 0 else size_max] * bins, size_max)

def is_constant(data):
    return all([el == data[0] for el in data])


   # def set_title(self, label = None):
   #      self.get_xaxis(2).set_title(label)

   #  def set_xlabel(self, label = None, xside = None):
   #      self.get_xaxis(xside).set_label(label)
        
   #  def set_ylabel(self, label = None, yside = None):
   #      self.get_yaxis(yside).set_label(label)

   #  def set_xlim(self, left = None, right = None, xside = None):
   #      self.get_xaxis(xside).set_lim(left, right)
        
   #  def set_ylim(self, lower = None, upper = None):
   #      self.get_yaxis(yside).set_lim(lower, upper)

   #  def set_xscale(self, scale = None, xside = None):
   #      self.get_xaxis(xside).set_scale(scale)

   #  def set_yscale(self, scale = None, yside = None):
   #      self.get_yaxis(yside).set_scale(scale)

   #  def set_xticks(self, ticks = None, labels = None, xside = None):
   #      self.get_xaxis(xside).set_ticks(ticks, labels)

   #  def set_yticks(self, ticks = None, labels = None, yside = None):
   #      self.get_yaxis(yside).set_ticks(ticks, labels)

   #  def set_xfrequency(self, frequency = None, xside = None):
   #      self.get_xaxis(xside).set_frequency(frequency)

   #  def set_yfrequency(self, frequency = None, yside = None):
   #      self.get_yaxis(yside).set_frequency(frequency)

   #  def set_xdirection(self, direction = None, xside = None):
   #      self.get_xaxis(xside).set_direction(direction)

   #  def set_ydirection(self, direction = None, yside = None):
   #      self.get_yaxis(yside).set_direction(direction)

   #  def set_xgrid(self, grid = None, xside = None):
   #      self.get_xaxis(xside).set_grid(grid)

   #  def set_ygrid(self, grid = None, yside = None):
   #      self.get_yaxis(yside).set_grid(grid)


   #          def set_ticks_color(self, color = None):
   #      [self.get_xaxis(xside).set_ticks_color(color) for xside in self.r2]
   #      [self.get_yaxis(yside).set_ticks_color(color) for yside in self.r2]

   #  def set_ticks_style(self, color = None):
   #      [self.get_xaxis(xside).set_ticks_style(color) for xside in self.r2]
   #      [self.get_yaxis(yside).set_ticks_style(color) for yside in self.r2]
