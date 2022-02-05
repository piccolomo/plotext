from plotext._utility.color import no_color_name, color_code
from plotext._utility.data import brush, transpose, replace
from plotext._utility.string import only_spaces
from plotext._utility.color import uncolorize
from plotext._matrices import figure_matrices
from plotext._default import figure_default
from plotext._utility.file import save_text
from plotext._subplot import datetime as _datetime
from plotext._subplot import subplot_class
from plotext._utility.plot import *
from time import time

##############################################
##########    Figure Container    ############
##############################################
class figure_class():
    def __init__(self):
        self.default = figure_default()
        self.matrices = figure_matrices()

        self.set_size(None, None) # the figure width and height
        self.limit_size = self.default.limit_size # if True, the figure can expand beyond terminal size
        
        self.rows, self.cols = [1, 1] # the number of rows and cols of the matrix of subplots
        self.set_subplots()
        
        self.row, self.col = [0, 0] # the active plot coordinates in the matrix 
        self.set_subplot(1, 1) # set the current subplot to work on

        self.canvas = ''
        self.time = None

    def set_size(self, width = None, height = None):
        self.width = None if width is None else int(width)
        self.height = None if height is None else int(height)
        self.size = [self.width, self.height]
        
    def set_subplots(self, rows = None, cols = None): # it sets the figure grid size
        rows = 1 if rows is None else rows
        cols = 1 if cols is None else cols
        if rows > self.default.rows_max:
            raise ValueError("Subplots rows above limit of " + str(self.default.rows_max))
        if cols > self.default.cols_max:
            raise ValueError("Subplots cols above limit of " + str(self.default.cols_max))
        rows = rows if rows < self.default.rows_max else self.default.rows_max
        cols = cols if cols < self.default.cols_max else self.default.cols_max
        self.rows, self.cols = [rows, cols]
        
        self.subplots = [[subplot_class(r, c) for c in range(self.cols)] for r in range(self.rows)]
        self.set_subplot(1, 1) # automatically sets the current subplot to work on to the first

    def set_subplot(self, row = None, col = None): # it sets the current subplot to work on
        row = 1 if row is None else row
        col = 1 if col is None else col
        self.row, self.col = [row - 1, col - 1]
        self.subplot = self.subplots[self.row][self.col]

    def save_fig(self, path):
        import os
        _, extension = os.path.splitext(path)
        if extension == ".html":
            text = self.matrices.to_html()
        else:
            text = uncolorize(self.matrices.to_canvas())
        save_text(path, text)
        
##############################################
###########    Clear Functions    ############
##############################################

    def clear_figure(self):
        self.__init__()

    def colorless(self):
        row, col = self.row, self.col
        for r in range(self.rows):
            for c in range(self.cols):
                self.set_subplot(r + 1, c + 1)
                self.clear_color()
        self.set_subplot(self.row, self.col)
        
    def clear_plot(self):
        self.subplot.__init__(self.row, self.col)

    def clear_data(self):
        self.subplot.data_init()
        #self.set_size(None, None) # usefull for streaming data
        self.subplot.set_size(None, None) # usefull for streaming data

    def clear_color(self):
        self.subplot.color_sequence = [no_color_name] * len(self.subplot.color_sequence)
        self.subplot.color = [no_color_name] * len(self.subplot.color)
        self.subplot.axes_color = no_color_name
        self.subplot.ticks_color = no_color_name
        self.subplot.canvas_color = no_color_name

    def clear_terminal(self, lines = None):
        if lines is None:
            write('\033c')
        else:
            for r in range(lines):
                write("\033[A") # moves the curson up
                write("\033[2K") # clear the entire line

##############################################
###########    Set Functions    ##############
##############################################

    def plot_size(self, width = None, height = None):
        width = None if width is None else width 
        height = None if height is None else height
        self.subplot.set_size(width, height)

    def limitsize(self, limit_xsize = None, limit_ysize = None): # can't call it limit_size here bacause of internal parameter named the same
        limit_xsize = self.default.limit_size[0] if limit_xsize is None else bool(limit_xsize)
        limit_ysize = limit_xsize if limit_ysize is None else bool(limit_ysize)
        self.limit_size = [limit_xsize, limit_ysize]

    def span(self, colspan = None, rowspan = None):
        colspan = 1 if colspan is None or colspan  <= 0 else colspan
        rowspan = 1 if rowspan is None or rowspan  <= 0 else rowspan
        colspan = min(colspan, self.cols - self.col)
        rowspan = min(rowspan, self.rows - self.row)
        self.subplot.rowspan = rowspan
        self.subplot.colspan = colspan
        
    def title(self, title = None):
        title = None if title is None else str(title).strip()
        spaces = only_spaces(title)
        title = None if spaces else title 
        self.subplot.title = title

    def xlabel(self, xlabel = None, xside = None):
        xlabel = None if xlabel is None else str(xlabel).strip()
        spaces = only_spaces(xlabel)
        xlabel = None if spaces else xlabel
        pos = self.subplot.xside_to_pos(xside)
        self.subplot.xlabel[pos] = xlabel

    def ylabel(self, ylabel = None, yside = None):
        ylabel = None if ylabel is None else str(ylabel).strip()
        spaces = only_spaces(ylabel)
        ylabel = None if spaces else ylabel
        pos = self.subplot.yside_to_pos(yside)
        self.subplot.ylabel[pos] = ylabel
        
    def xaxis(self, state = None, xside = None):
        pos = self.subplot.xside_to_pos(xside)
        state = self.subplot.default.xaxes[pos] if state is None else bool(state)
        self.subplot.xaxes[pos] = state

    def yaxis(self, state = None, yside = None):
        pos = self.subplot.yside_to_pos(yside)
        state = self.subplot.default.yaxes[pos] if state is None else bool(state)
        self.subplot.yaxes[pos] = state

    def frame(self, state = True):
        [self.xaxis(state, side) for side in self.subplot.default.xside]
        [self.yaxis(state, side) for side in self.subplot.default.yside]

    def grid(self, horizontal = None, vertical = None):
        horizontal = self.subplot.default.grid[0] if horizontal is None else bool(horizontal)
        vertical = horizontal if vertical is None else bool(vertical)
        self.subplot.grid = [horizontal, vertical]

    def canvas_color(self, color = None):
        code = color_code(color, 0)
        nocolor = code[0] == 3
        color = self.subplot.default.canvas_color if color is None or nocolor else color
        self.subplot.canvas_color = color

    def ticks_color(self, color = None):
        code = color_code(color, 1)
        nocolor = code[0] == 3
        color = self.subplot.default.ticks_color if color is None or nocolor else color
        self.subplot.ticks_color = color
        
    def axes_color(self, color = None):
        code = color_code(color, 0)
        nocolor = code[0] == 3
        color = self.subplot.default.axes_color if color is None or nocolor else color
        self.subplot.axes_color = color

    def xlim(self, lower = None, upper = None, xside = None):
        lower = None if lower is None else float(lower)
        upper = None if upper is None else float(upper)
        xlim = [lower, upper]
        xlim = xlim if xlim == [None] * 2 else [min(xlim), max(xlim)]
        pos = self.subplot.xside_to_pos(xside)
        self.subplot.xlim[pos] = xlim

    def ylim(self, left = None, right = None, yside = None):
        left = None if left is None else float(left)
        right = None if right is None else float(right)
        ylim = [left, right]
        ylim = ylim if ylim == [None] * 2 else [min(ylim), max(ylim)]
        pos = self.subplot.yside_to_pos(yside)
        self.subplot.ylim[pos] = ylim

    def xscale(self, scale = None, xside = None):
        default_case = (scale is None or scale not in self.subplot.default.xscale)
        scale = self.subplot.default.xscale[0] if default_case else scale
        pos = self.subplot.xside_to_pos(xside)
        self.subplot.xscale[pos] = scale

    def yscale(self, scale = None, yside = None):
        default_case = (scale is None or scale not in self.subplot.default.yscale)
        scale = self.subplot.default.yscale[0] if default_case else scale
        pos = self.subplot.yside_to_pos(yside)
        self.subplot.yscale[pos] = scale

    def xfrequency(self, frequency = None, xside = None):
        pos = self.subplot.xside_to_pos(xside)
        frequency = self.subplot.default.xfrequency[pos] if frequency is None else int(frequency)
        if frequency == 0:
            self.xticks([], [], xside)
        self.subplot.xfrequency[pos] = frequency

    def yfrequency(self, frequency = None, yside = None):
        pos = self.subplot.yside_to_pos(yside)
        frequency = self.subplot.default.yfrequency[pos] if frequency is None else int(frequency)
        if frequency == 0:
            self.yticks([], [], yside)
        self.subplot.yfrequency[pos] = frequency

    def xticks(self, ticks = None, labels = None, xside = None):
        pos = self.subplot.xside_to_pos(xside)
        ticks = self.subplot.default.xticks[pos] if ticks is None else list(ticks)
        labels = ticks if labels is None else list(labels)
        labels = list(map(str, labels))
        ticks = list(map(_datetime.string_to_timestamp, ticks)) if len(ticks) > 0 and type(ticks[0]) == str else ticks
        ticks, labels = brush(ticks, labels)
        self.subplot.xticks[pos] = ticks
        self.subplot.xlabels[pos] = labels
        self.subplot.xfrequency[pos] = self.subplot.xfrequency[pos] if ticks is None else len(ticks) 

    def yticks(self, ticks = None, labels = None, yside = None):
        pos = self.subplot.yside_to_pos(yside)
        ticks = self.subplot.default.yticks[pos] if ticks is None else list(ticks)
        labels = ticks if labels is None else list(labels)
        labels = list(map(str, labels))
        ticks, labels = brush(ticks, labels)
        self.subplot.yticks[pos] = ticks
        self.subplot.ylabels[pos] = labels
        self.subplot.yfrequency[pos] = self.subplot.yfrequency[pos] if ticks is None else len(ticks)

##############################################
###########    Show Functions    #############
##############################################

    def build(self):
        t = time()
        self.get_size_max()
        self.get_size_matrices()
        self.set_size(0, 0)
        for row in range(1, self.rows + 1):
             for col in range(1, self.cols + 1):
                 self.set_subplot(row, col)
                 self.set_subplot_size()
                 self.subplot.correct_frequency()
                 self.subplot.adjust_height()
                 self.subplot.set_scale()
                 self.subplot.get_xlim()
                 self.subplot.get_ylim()
                 self.subplot.get_height_canvas()
                 self.subplot.get_yticks()
                 self.subplot.get_width_canvas()
                 self.subplot.adjust_width()
                 self.subplot.get_xticks()
                 self.subplot.get_relative_ticks()
                 self.subplot.create_matrices()
                 self.subplot.add_grid()
                 self.subplot.add_extra_lines()
                 self.subplot.update_matrix()
                 self.subplot.add_legend()
                 self.subplot.add_yaxis()
                 self.subplot.add_xaxis()
                 self.subplot.add_labels()
        self.set_size(sum(self.widths[0]), sum(transpose(self.heights)[0]))
        self.join_matrices()
        self.to_canvas()
        self.time = time() - t
        return self.canvas
    
    def show(self):
        self.build()
        write(self.canvas)

    def get_size_max(self):
        term_size = replace(terminal_size(), self.default.terminal_size)
        self.width_max = term_size[0] if self.limit_size[0] else self.default.terminal_infinite_size[0] 
        self.height_max = term_size[1] if self.limit_size[1] else self.default.terminal_infinite_size[1]
        self.height_max -= 2 # last terminal row is always occupied the other one is for ipython

    def get_size_matrices(self):
        sub = lambda row, col: self.subplots[row][col]
        widths = [[sub(row, col).width for col in range(self.cols)] for row in range(self.rows)]
        colspan = [[sub(row, col).colspan for col in range(self.cols)] for row in range(self.rows)]
        heights = [[sub(row, col).height for col in range(self.cols)] for row in range(self.rows)]
        rowspan = [[sub(row, col).rowspan for col in range(self.cols)] for row in range(self.rows)]
        widths = modify_widths(widths, colspan, rowspan, self.width_max)
        heights = transpose(modify_widths(transpose(heights), transpose(rowspan), transpose(colspan), self.height_max))
        self.widths = widths
        self.heights = heights

    def set_subplot_size(self):
        r, c = self.row, self.col
        self.subplots[r][c].set_size(self.widths[r][c], self.heights[r][c])

    def join_matrices(self):
        self.matrices.marker = join_matrices([[self.subplots[r][c].matrices.marker for c in range(self.cols)] for r in range(self.rows)])
        self.matrices.color = join_matrices([[self.subplots[r][c].matrices.color for c in range(self.cols)] for r in range(self.rows)])
        self.matrices.background = join_matrices([[self.subplots[r][c].matrices.background for c in range(self.cols)] for r in range(self.rows)])

    def to_canvas(self): # turns the matrices to the plot canvas in string form
        self.matrices.to_canvas()
        self.canvas = self.matrices.canvas

    def get_time(self):
        return self.time
