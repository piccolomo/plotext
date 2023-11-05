from plotext._default import default_figure_class
from plotext._monitor import monitor_class
from plotext._matrix import join_matrices
from plotext._date import date_class
from plotext._doc_utils import add
from time import time as _time
import plotext._utility as ut
from time import time
import os

# A figure is a general container of either a plot (called monitor) or another figure, when subplots are nested
# This creates a hierarchy of figures, where master is the main/initial global figure, and parent is the figure containing (or above) the one considered
# The active figure is the one that can be accessed with further plotext commands - like plot(), limitsize() etc .. 
# If a figure has no sub figures, then it is used for plotting, otherwise its sub figures are checked

class _figure_class():
    
    def __init__(self, master = None, parent = None):
        self._set_family(master, parent) # it sets master, parent and active figure
        self.default = default_figure_class() # default values of figure class
        self.date = date_class()

        self._set_size(None, None) # no initial size for general figure
        self.max_or_min = max # in a matrix of subplots the maximum height/width is considered (by default) for each row/column
        
        self.monitor = monitor_class() if self._is_master else self._parent.monitor.copy() # each figure has a monitor for plotting; which by default is deep copied from its parent figure monitor, so that a figure with multiple sub plots can have easily the same plot and plot settings and preferences (without rewriting code)
        self.monitor.set_date(self.date) # to make sure that the date settings of a figure are the same for its subplots

        self._set_master() if self._is_master else None # it sets the master figure size and other utilities 

        self._set_slots_max(*self._master._size) # sets the maximum number of sub figures in the current figure (from master figure size)
        self.subplots(0, 0) # no sub figures added by default, so that the current figure is used for plotting
        
    def _set_family(self, master = None, parent = None):
        self._parent = self if parent is None else parent # the figure just above this one
        self._master = self if master is None else master # the figure above all others
        self._is_master = self is self._master
        self._active = self if self._is_master else self._master._active # the active figure, such that further plotting or settings commands refer to it

    def _set_master(self):
        self._limit_size(True, True)  # limit size (only available for master, as sub figures are by default limited by parent figure)
        self._set_terminal_size(*ut.terminal_size()) # get and set terminal size
        self._set_master_size()  # set master size to terminal
        self._time = None # computational time of show() method, only available for global figure
        self._dummy = _figure_class(self._master, self._master) # the master has a dumm container for subplots that do not actually exist (anymore due to change of size)
        self._master.monitor.set_size(self._size)
        self._dummy.monitor.set_size(self._size)
        self._set_interactive() # if to make the final figure interactive: every command gets directly printed

##############################################
###########    Size Functions    #############
##############################################

    def _set_interactive(self, interactive = None):
        self._interactive = self.default.interactive if interactive is None else bool(interactive)

    def _set_size(self, width = None, height = None):
        self._width = None if width is None else int(width)
        self._height = None if height is None else int(height)
        self._size = [self._width, self._height]

    def _limit_size(self, width = None, height = None):
        self._limit_width = self.default.limit_width if width is None else bool(width)
        self._limit_height = self.default.limit_height if height is None else bool(height)
        self._limit = [self._limit_width, self._limit_height]

    def _set_terminal_size(self, width = None, height = None):
        self._width_term = self.default._width_term if width is None else width
        extra_lines = 2 if ut.is_ipython() else 1
        self._height_term = self.default._height_term if height is None else max(height - extra_lines, 0)
        self._size_term = [self._width_term, self._height_term]

    def _set_master_size(self):
        width = self._width_term if self._width is None or (self._width > self._width_term and self._limit_width) else self._width
        height = self._height_term if self._height is None or (self._height > self._height_term and self._limit_height) else self._height
        self._set_size(width, height)
        
##############################################
#########    Subplots Functions    ###########
##############################################

    def _set_slots_max(self, width = None, height = None):
        self._rows_max = height # (height + 1) // 3 
        self._cols_max = width # (width + 1) // 3 
        self._slots_max = [self._rows_max, self._cols_max]

    def _set_slots(self, rows = None, cols = None):
        rows = 1 if rows is None else int(abs(rows))
        cols = 1 if cols is None else int(abs(cols))
        self._rows = min(rows, self._rows_max)
        self._cols = min(cols, self._cols_max)
        self._Rows = list(range(1, self._rows + 1))
        self._Cols = list(range(1, self._cols + 1))
        self._slots = [self._rows, self._cols]
        self._no_plots = 0 in self._slots #or self._is_master
        
    def _set_subplots(self):
        self.subfig = [[_figure_class(self._master, self) for col in self._Cols] for row in self._Rows]
        
    def _get_subplot(self, row = None, col = None):
        return self.subfig[row - 1][col - 1] if row in self._Rows and col in self._Cols else self._master._dummy

    def subplot(self, row = None, col = None):
        row = 1 if row is None else int(abs(row))
        col = 1 if col is None else int(abs(col))
        active = self._get_subplot(row, col)
        self._active = active
        self._master._active = active
        return self._master._active

    def subplots(self, rows = None, cols = None):
        self._set_slots(rows, cols)
        self._set_subplots()
        return self

##############################################
#######    External Set Functions    #########
##############################################

    def title(self, label = None):
        self.monitor.set_title(label) if self._no_plots else [[self._get_subplot(row, col).title(label) for col in self._Cols] for row in self._Rows]

    def xlabel(self, label = None, xside = None):
        self.monitor.set_xlabel(label = label, xside = xside) if self._no_plots else [[self._get_subplot(row, col).xlabel(label = label, xside = xside) for col in self._Cols] for row in self._Rows]
        
    def ylabel(self, label = None, yside = None):
        self.monitor.set_ylabel(label = label, yside = yside) if self._no_plots else [[self._get_subplot(row, col).ylabel(label = label, yside = yside) for col in self._Cols] for row in self._Rows]

    def xlim(self, left = None, right = None, xside = None):
        self.monitor.set_xlim(left = left, right = right, xside = xside) if self._no_plots else [[self._get_subplot(row, col).xlim(left = left, right = right, xside = xside) for col in self._Cols] for row in self._Rows]

    def ylim(self, lower = None, upper = None, yside = None):
        self.monitor.set_ylim(lower = lower, upper = upper, yside = yside) if self._no_plots else [[self._get_subplot(row, col).ylim(lower = lower, upper = upper, yside = yside) for col in self._Cols] for row in self._Rows]
        
    def xscale(self, scale = None, xside = None):
        self.monitor.set_xscale(scale = scale, xside = xside) if self._no_plots else [[self._get_subplot(row, col).xscale(scale = scale, xside = xside) for col in self._Cols] for row in self._Rows]
        
    def yscale(self, scale = None, yside = None):
        self.monitor.set_yscale(scale = scale, yside = yside) if self._no_plots else [[self._get_subplot(row, col).yscale(scale = scale, yside = yside) for col in self._Cols] for row in self._Rows]
        
    def xticks(self, ticks = None, labels = None, xside = None):
        self.monitor.set_xticks(ticks = ticks, labels = labels, xside = xside) if self._no_plots else [[self._get_subplot(row, col).xticks(ticks = ticks, labels = labels, xside = xside) for col in self._Cols] for row in self._Rows]

    def yticks(self, ticks = None, labels = None, yside = None):
        self.monitor.set_yticks(ticks = ticks, labels = labels, yside = yside) if self._no_plots else [[self._get_subplot(row, col).yticks(ticks = ticks, labels = labels, yside = yside) for col in self._Cols] for row in self._Rows]

    def xfrequency(self, frequency = None, xside = None):
        self.monitor.set_xfrequency(frequency = frequency, xside = xside) if self._no_plots else [[self._get_subplot(row, col).xfrequency(frequency = frequency, xside = xside) for col in self._Cols] for row in self._Rows]

    def yfrequency(self, frequency = None, yside = None):
        self.monitor.set_yfrequency(frequency = frequency, yside = yside) if self._no_plots else [[self._get_subplot(row, col).yfrequency(frequency = frequency, yside = yside) for col in self._Cols] for row in self._Rows]

    def xreverse(self, reverse = None, xside = None):
        self.monitor.set_xreverse(reverse = reverse, xside = xside) if self._no_plots else [[self._get_subplot(row, col).xreverse(reverse = reverse, xside = xside) for col in self._Cols] for row in self._Rows]

    def yreverse(self, reverse = None, yside = None):
        self.monitor.set_yreverse(reverse = reverse, yside = yside) if self._no_plots else [[self._get_subplot(row, col).yreverse(reverse = reverse, yside = yside) for col in self._Cols] for row in self._Rows]

    def xaxes(self, lower = None, upper = None):
        self.monitor.set_xaxes(lower = lower, upper = upper) if self._no_plots else [[self._get_subplot(row, col).xaxes(lower = lower, upper = upper) for col in self._Cols] for row in self._Rows]

    def yaxes(self, left = None, right = None):
        self.monitor.set_yaxes(left = left, right = right) if self._no_plots else [[self._get_subplot(row, col).yaxes(left = left, right = right) for col in self._Cols] for row in self._Rows]

    def frame(self, frame = None):
        self.monitor.set_frame(frame = frame) if self._no_plots else [[self._get_subplot(row, col).frame(frame = frame) for col in self._Cols] for row in self._Rows]
        
    def grid(self, horizontal = None, vertical = None):
        self.monitor.set_grid(horizontal = horizontal, vertical = vertical) if self._no_plots else [[self._get_subplot(row, col).grid(horizontal = horizontal, vertical = vertical) for col in self._Cols] for row in self._Rows]

    def canvas_color(self, color = None):
        self.monitor.set_canvas_color(color) if self._no_plots else [[self._get_subplot(row, col).canvas_color(color) for col in self._Cols] for row in self._Rows]

    def axes_color(self, color = None):
        self.monitor.set_axes_color(color) if self._no_plots else [[self._get_subplot(row, col).axes_color(color) for col in self._Cols] for row in self._Rows]

    def ticks_color(self, color = None):
        self.monitor.set_ticks_color(color) if self._no_plots else [[self._get_subplot(row, col).ticks_color(color) for col in self._Cols] for row in self._Rows]
        
    def ticks_style(self, style = None):
        self.monitor.set_ticks_style(style) if self._no_plots else [[self._get_subplot(row, col).ticks_style(style) for col in self._Cols] for row in self._Rows]
        
    def theme(self, theme = None):
        self.monitor.set_theme(theme) if self._no_plots else [[self._get_subplot(row, col).theme(theme) for col in self._Cols] for row in self._Rows]

##############################################
###########    Clear Functions    ############
###########################x##################

    def clear_figure(self):
        self.__init__()# if self._no_plots else [[self._get_subplot(row, col).clear_figure() for col in self._Cols] for row in self._Rows]
    clf = clear_figure
    
    def clear_data(self):
        self.monitor.data_init() if self._no_plots else [[self._get_subplot(row, col).clear_data() for col in self._Cols] for row in self._Rows]
    cld = clear_data

    def clear_color(self):
        self.monitor.clear_color() if self._no_plots else [[self._get_subplot(row, col).clear_color() for col in self._Cols] for row in self._Rows]
    clc = clear_color

    def clear_terminal(self, lines = None):
        ut.clear_terminal(lines = lines)
    clt = clear_terminal

##############################################
###########    Plot Functions    #############
##############################################

    def _draw(self, *args, **kwargs):
        self.monitor.draw(*args, **kwargs) if self._no_plots else [[self._get_subplot(row, col)._draw(*args, **kwargs) for col in self._Cols] for row in self._Rows]

    def scatter(self, *args, marker = None, color = None, style = None, fillx = None, filly = None, xside = None, yside = None, label = None):
        self._draw(*args, xside = xside, yside = yside, lines = False, marker = marker, color = color, style = style, fillx = fillx, filly = filly, label = label)

    def plot(self, *args, marker = None, color = None, style = None, fillx = None, filly = None, xside = None, yside = None, label = None):
        self._draw(*args, xside = xside, yside = yside, lines = True, marker = marker, color = color,  fillx = fillx, filly = filly, label = label)
        
    def bar(self, *args, marker = None, color = None, fill = None, width = None, orientation = None, minimum = None, reset_ticks = None, xside = None, yside = None, label = None):
        self.monitor.draw_bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum, reset_ticks = reset_ticks) if self._no_plots else [[self._get_subplot(row, col).bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum, reset_ticks = reset_ticks) for col in self._Cols] for row in self._Rows]

    def multiple_bar(self, *args, marker = None, color = None, fill = None, width = None, orientation = None, minimum = None, reset_ticks = None, xside = None, yside = None, labels = None):
        self.monitor.draw_multiple_bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, labels = labels, minimum = minimum, reset_ticks = reset_ticks) if self._no_plots else [[self._get_subplot(row, col).multiple_bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum, reset_ticks = reset_ticks) for col in self._Cols] for row in self._Rows]
    
    def stacked_bar(self, *args, marker = None, color = None, fill = None, width = None, orientation = None, minimum = None, reset_ticks = None, xside = None, yside = None, labels = None):
        self.monitor.draw_stacked_bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, labels = labels, minimum = minimum, reset_ticks = reset_ticks) if self._no_plots else [[self._get_subplot(row, col).stacked_bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum, reset_ticks = reset_ticks) for col in self._Cols] for row in self._Rows]

    def hist(self, data, bins = None, marker = None, color = None, fill = None, norm = None, width = None, orientation = None, minimum = None, xside = None, yside = None, label = None):
        self.monitor.draw_hist(data, bins = bins, norm = norm, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum) if self._no_plots else [[self._get_subplot(row, col).hist(data, bins = bins, norm = norm, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum) for col in self._Cols] for row in self._Rows]

    def candlestick(self, dates, data, colors = None, orientation = None, xside = None, yside = None, label = None):
        self.monitor.draw_candlestick(dates, data, xside = xside, yside = yside, orientation = orientation, colors = colors, label = label) if self._no_plots else [[self._get_subplot(row, col).candlestick(dates, data, orientation = orientation, colors = colors, label = label) for col in self._Cols] for row in self._Rows]

    def box(self, *args, quintuples = None, colors = None,  fill = None, width = None, orientation = None, minimum = None, reset_ticks = None, xside = None, yside = None, label = None):
        self.monitor.draw_box(*args, xside = xside, yside = yside, orientation = orientation, colors = colors, label = label, fill = fill, width = width, minimum = minimum, reset_ticks = reset_ticks, quintuples = quintuples) if self._no_plots else [[self._get_subplot(row, col).box(*args, orientation = orientation, colors = colors, label = label, fill = fill, width = width, minimum = minimum, reset_ticks = reset_ticks, quintuples = quintuples) for col in self._Cols] for row in self._Rows]

##############################################
###########    Plotting Tools    #############
##############################################

    def error(self, *args, xerr = None, yerr = None, color = None, xside = None, yside = None, label = None):
        self.monitor.draw_error(*args, xerr = xerr, yerr = yerr, xside = xside, yside = yside, color = color, label = label) if self._no_plots else [[self._get_subplot(row, col).error(*args, xerr = xerr, yerr = yerr, xside = xside, yside = yside, color = color, label = label) for col in self._Cols] for row in self._Rows]

    def event_plot(self, data, marker = None, color = None, orientation = None, side = None):
        self.monitor.draw_event_plot(data, orientation = orientation, marker = marker, color = color, side = side) if self._no_plots else [[self._get_subplot(row, col).event_plot(data, orientation = orientation, marker = marker, color = color, side = side) for col in self._Cols] for row in self._Rows]
    eventplot = event_plot

    def vertical_line(self, coordinate, color = None, xside = None):
        self.monitor.draw_vertical_line(coordinate, color = color, xside = xside) if self._no_plots else [[self._get_subplot(row, col).vertical_line(coordinate, color = color, xside = xside) for col in self._Cols] for row in self._Rows]
    vline = vertical_line
        
    def horizontal_line(self, coordinate, color = None, yside = None):
        self.monitor.draw_horizontal_line(coordinate, color = color, yside = yside) if self._no_plots else [[self._get_subplot(row, col).horizontal_line(coordinate, color = color, yside = yside) for col in self._Cols] for row in self._Rows]     
    hline = horizontal_line

    def text(self, label, x, y, color = None, background = None, style = None, orientation = None, alignment = None, xside = None, yside = None):
        self.monitor.draw_text(label, x, y, xside = xside, yside = yside, color = color, background = background, style = style, orientation = orientation, alignment = alignment) if self._no_plots else [[self._get_subplot(row, col).text(label, x, y, xside = xside, yside = yside, color = color, background = background, style = style, orientation = orientation, alignment = alignment) for col in self._Cols] for row in self._Rows]

    def rectangle(self, x = None, y = None, marker = None, color = None, lines = None, fill = None, xside = None, yside = None, label = None):
        self.monitor.draw_rectangle(x = x, y = y, xside = xside, yside = yside, lines = lines, marker = marker, color = color, fill = fill, label = label) if self._no_plots else [[self._get_subplot(row, col).rectangle(x = x, y = y, xside = xside, yside = yside, lines = lines, marker = marker, color = color, fill = fill, label = label) for col in self._Cols] for row in self._Rows]

    def polygon(self, x = None, y = None,  radius = None, sides = None, marker = None, color = None, lines = None, fill = None, xside = None, yside = None, label = None):
        self.monitor.draw_polygon(x = x, y = y, radius = radius, sides = sides, xside = xside, yside = yside, lines = lines, marker = marker, color = color, fill = fill, label = label) if self._no_plots else [[self._get_subplot(row, col).polygon(x = x, y = y, radius = radius, sides = sides, xside = xside, yside = yside, lines = lines, marker = marker, color = color, fill = fill, label = label) for col in self._Cols] for row in self._Rows]

    def confusion_matrix(self, actual, predicted, color = None, style = None, labels = None):
        self.monitor.draw_confusion_matrix(actual, predicted, labels = labels, color = color, style = style) if self._no_plots else [[self._get_subplot(row, col).confusion_matrix(actual, predicted, labels = labels, color = color, style = style) for col in self._Cols] for row in self._Rows]

    cmatrix = confusion_matrix

    def indicator(self, value, label = None, color = None, style = None):
        self.monitor.draw_indicator(value, label = label, color = color, style = style) if self._no_plots else [[self._get_subplot(row, col).confusion_matrix(value, label = label, color = color, style = style) for col in self._Cols] for row in self._Rows]

##############################################
##############    2D Plots    ################
############################################## 

    def matrix_plot(self, matrix, marker = None, style = None, fast = False):
        self.monitor.draw_matrix(matrix, marker = marker, style = style, fast = fast) if self._no_plots else [[self._get_subplot(row, col).matrix_plot(matrix, marker = marker, style = style, fast = fast) for col in self._Cols] for row in self._Rows]

    def heatmap(self, dataframe, color = None, style = None):
        self.monitor.draw_heatmap(dataframe, color = color, style = style) if self._no_plots else [[self._get_subplot(row, col).heatmap(dataframe, color = color, style = style) for col in self._Cols] for row in self._Rows]

    def image_plot(self, path, marker = None, style = None, fast = False, grayscale = False):
        self.monitor.draw_image(path, marker = marker, style = style, grayscale = grayscale, fast = fast) if self._no_plots else [[self._get_subplot(row, col).image_plot(path, marker = marker, style = style, grayscale = grayscale, fast = fast) for col in self._Cols] for row in self._Rows]
        
##############################################
###########    Date Functions    #############
##############################################

    def date_form(self, input_form = None, output_form = None):
        self._master._dummy.date.date_form(input_form, output_form)
        if self._no_plots:
            self.monitor.date.date_form(input_form, output_form)
        else:
            [[self._get_subplot(row, col).date_form(input_form, output_form) for col in self._Cols] for row in self._Rows]
        
    def set_time0(self, string, input_form = None):
        self.monitor.date.set_time0(string, form) if self._no_plots else [[self._get_subplot(row, col).set_time0(string, form) for col in self._Cols] for row in self._Rows]

    def today_datetime(self):
        return self.monitor.date.today_datetime()
    
    def today_string(self, output_form = None):
        return self.monitor.date.today_string(output_form)
    
    def datetime_to_string(self, datetime, output_form = None):
        return self.monitor.date.datetime_to_string(datetime, output_form = output_form)
    
    def datetimes_to_strings(self, datetimes, output_form = None):
        return self.monitor.date.datetimes_to_strings(datetimes, output_form = output_form)
        
    def string_to_datetime(self, string, input_form = None):
        return self.monitor.date.string_to_datetime(string, input_form = input_form)
    
    def string_to_time(self, string, input_form = None):
        return self.monitor.date.string_to_time(string, input_form = input_form)
    
    def strings_to_time(self, string, input_form = None):
        return self.monitor.date.strings_to_time(string, input_form = input_form)

##############################################
###########    Build Functions    ############
##############################################

    def show(self): # it build and shows the overall figure
        t = time()
        self.build() 
        ut.write(self.monitor.matrix.canvas) # it prints the final canvas
        self._time = time() - t # computational time of build + print (it does not include any pre-processing time, which is gets more important for bar and image plots)
        self.main() if not self._master._interactive else None# it returns control to main figure on top level

    def build(self): # it build the current figure without showing it
        self._set_sizes()
        self._build_matrix()
        self.monitor.matrix.set_canvas() if not self.monitor.fast_plot else None
        return self.monitor.matrix.get_canvas() 

    def _build_matrix(self):
        if self._no_plots:
            self.monitor.build_plot() if not self.monitor.fast_plot else None
        else:
            [[self._get_subplot(row, col)._build_matrix() for col in self._Cols] for row in self._Rows]
            matrices = [[self._get_subplot(row, col).monitor.matrix for col in self._Cols] for row in self._Rows]
            self.monitor.matrix = join_matrices(matrices)

##############################################
#########    Set Size Utilities    ###########
##############################################

    def _set_sizes(self): # it properly sets coherent sub figure dimensions
        self._set_slots_max(*self._size) 
        self._set_slots(*self._slots)
        widths = self._get_widths()
        widths = ut.set_sizes(widths, self._width) # it sets the free subplots widths in accord with the parent figure width
        widths = ut.fit_sizes(widths, self._width) # it fits the subplots widths to the parent figure width 
        heights = self._get_heights()
        heights = ut.set_sizes(heights, self._height) # it sets the free subplots height in accord with the parent figure height 
        heights = ut.fit_sizes(heights, self._height) # it fits the subplots heights to the parent figure height
        width = sum(widths) if len(widths) > 1 else self._width
        height = sum(heights) if len(widths) > 1 else self._height

        self.monitor.set_size(self._size)
        # self._set_size(width, height)
        [[self._set_subplot_size(row, col, widths[col - 1], heights[row - 1]) for col in self._Cols] for row in self._Rows] if (not self._no_plots) else None # to make sure that all sub figures have internal dimensions set as well 

    def _get_widths(self): # the subplots max/min widths for each column
        widths = [[self._get_subplot(row, col)._width for row in self._Rows] for col in self._Cols]
        widths = [self.max_or_min([sub for sub in el if sub is not None], default = None) for el in widths]
        return widths

    def _get_heights(self): # the subplots max/min heights for each row
        heights = [[self._get_subplot(row, col)._height for col in self._Cols] for row in self._Rows]
        heights = [self.max_or_min([sub for sub in el if sub is not None], default = None) for el in heights]
        return heights

    def _set_subplot_size(self, row = None, col = None, width = None, height = None):
        self._get_subplot(row, col)._set_size(width, height)
        self._get_subplot(row, col)._set_sizes() 

##############################################
######    Externally Called Utility    #######
##############################################

    def _get_time(self, show = True): # it returns the computational time of latest show or build function
        time = ut.format_time(self._time)
        print(ut.format_strings("plotext time:", time, ut.title_color)) if show else None
        return self._time

    def main(self): # returns the master figure and sets the active figure to the master
        self._master._active = self._master
        return self._master

    def plot_size(self, width = None, height = None):
        width = self._width if width is None else width
        height = self._height if height is None else height
        self._set_size(width, height)
        self._set_master_size() if self._is_master else None
        self.monitor.size = self._size
        return self._width, self._height
        
    plotsize = plot_size

    def take_min(self): # in a matrix of subplots the maximum height/width will be considered for each row/column
        self.max_or_min = min

    def save_fig(self, path = None, append = False, keep_colors = False): # it saves the plot as text or html, keep_colors = True preserves ansi colors for texts
        path = 'plotext.txt' if path is None or not ut.correct_path(path) else path
        _, extension = os.path.splitext(path)
        canvas = self.monitor.matrix.get_canvas()
        if extension == ".html":
            canvas = self.monitor.matrix.to_html()
        elif not keep_colors:
            canvas = ut.uncolorize(canvas)
        ut.save_text(canvas, path, append)
    savefig = save_fig
    
##############################################
############     Docstrings    ###############
##############################################
    add(subplots) 
    add(subplots)
    add(subplot)
    add(main)
    
    add(plot_size)
    add(take_min)
    
    add(title)
    add(xlabel)
    add(ylabel)
    add(xlim)
    add(ylim)
    add(xscale)
    add(yscale)
    add(xticks)
    add(yticks)
    add(xfrequency)
    add(yfrequency)
    add(xreverse)
    add(yreverse)
    add(xaxes)
    add(yaxes)
    add(frame)
    add(grid)
    add(canvas_color)
    add(axes_color)
    add(ticks_color)
    add(ticks_style)
    add(theme)
    
    add(clear_figure)
    add(clear_data)
    add(clear_color)
    add(clear_terminal)
    
    add(scatter)
    add(plot)
    add(bar)
    add(multiple_bar)
    add(stacked_bar)
    add(hist)
    add(candlestick)
    add(box)

    add(error)
    add(event_plot)
    add(vertical_line)
    add(horizontal_line)
    add(text)
    add(rectangle)
    add(polygon)
    add(confusion_matrix)
    add(indicator)

    add(matrix_plot)
    add(image_plot)
    
    add(show)
    add(build)
    add(save_fig)
    
    add(date_form)
    add(set_time0)
    add(today_datetime)
    add(today_string)
    add(datetime_to_string)
    add(datetimes_to_strings)
    add(string_to_datetime)