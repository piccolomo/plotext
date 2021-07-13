# /usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################
##############    Importing    ###############
##############################################
import utility as _utility
import docstrings as _docstrings
import subprocess as _subprocess

##############################################
###########    Initialization    #############
##############################################
_platform = _utility.platform()
#_platform = "windows"

if _platform == "windows":
    _subprocess.call('', shell = True)
    _utility.marker.pop('small')
    _utility.marker_sequence.remove('small')

_shell = _utility.shell()

##############################################
##########    Basic Containers    ############
##############################################
class _figure():
    def __init__(self):
        self.width = None
        self.height = None
        
        self.rows = 1
        self.cols = 1
        self.set_subplots()
        
        self.row = 0
        self.col = 0
        self.set_subplot()

        self.canvas = ""

    def set_subplots(self):
        self.subplots = [[_subplot(r, c) for c in range(self.cols)] for r in range(self.rows)]
        
    def get_subplot(self, row = 0 , col = 0):
        return self.subplots[row - 1][col - 1]

    def set_subplot(self):
        self.subplot = self.subplots[self.row][self.col]

class _subplot():
    def __init__(self, row, col):
        self.row = row
        self.col = col

        self.yaxis = []

        self.label = []
        self.label_show = []  

        self.point_marker = []
        self.line_marker = []
        self.point_color = []
        self.line_color = []

        self.x = []
        self.y = []
        self.signals = 0
        
        self.fillx = []
        self.filly = []

        self.width = None
        self.height = None
        
        self.width_set = None
        self.height_set = None

        self.title = ""
        self.xlabel = ""
        self.ylabel = ["", ""]
        
        self.xaxes = [True, True]
        self.yaxes = [True, True]
        self.grid = [False, False]

        self.axes_color = "white"
        self.ticks_color = "black"
        self.canvas_color = "white"

        self.xlim_plot = [None, None]
        self.ylim_plot_left = [None, None]
        self.ylim_plot_right = [None, None]
        
        self.xticks, self.xlabels = [], []
        self.yticks_left, self.ylabels_left = [], []
        self.yticks_right, self.ylabels_right = [], []
        self.ticks = [5, 7]

        self.xscale = "linear"
        self.yscale = ["linear", "linear"]


_fig = _figure()
#figure = _fig
#utility = _utility

##############################################
#########    Subplots Function    ############
##############################################
def subplots(rows = None, cols = None, ):
    rows, cols = _utility.set_first_to_both(rows, cols)
    _set_rows(rows)
    _set_cols(cols)
    _fig.set_subplots()
    subplot(1, 1)
subplots.__doc__ = _docstrings.subplots_doc

def _set_cols(cols = None):
    cols = _utility.set_if_none(cols, 1)
    _fig.cols = cols
    
def _set_rows(rows = None):
    rows = _utility.set_if_none(rows, 1)
    _fig.rows = rows

def subplot(row = 1, col = 1):
    _set_row(row)
    _set_col(col)
    _fig.set_subplot()
subplot.__doc__ = _docstrings.subplot_doc

def _set_col(col = None):
    col = _utility.set_if_none(col, 1)
    _fig.col = col - 1

def _set_row(row = None):
    row = _utility.set_if_none(row, 1)
    _fig.row = row - 1

subplots(1, 1)
subplot(1, 1)

##############################################
#######    Draw Related Functions    #########
##############################################
def _draw(*args, **kwargs):
    _yaxis(kwargs.get("yaxis"))
    
    _label(kwargs.get("label"))
        
    _point_marker(kwargs.get("point_marker"))
    _line_marker(kwargs.get("line_marker"))
        
    _point_color(kwargs.get("point_color"))
    _line_color(kwargs.get("line_color"))
        
    _data(*args)
    
    _fillx(kwargs.get("fillx"))
    _filly(kwargs.get("filly"))

def _yaxis(axis = None):
    axis_none = "left"
    axis = _utility.set_if_none(axis, axis_none)
    axis = "left" if axis != "left" and axis != "right" else axis
    _fig.subplot.yaxis.append(axis)

def _label(label = None):
    label_none = ""
    label = _utility.set_if_none(label, label_none)
    label_show = True
    _fig.subplot.label.append(label)
    _fig.subplot.label_show.append(label_show)
    #To-do: data with same label

def _point_marker(marker = None):
    index = len(set(_fig.subplot.point_marker)) % len(_utility.marker_sequence)
    marker_none = _utility.marker_sequence[index]
    marker = "" if marker == "" else marker
    marker = _utility.set_if_none(marker, marker_none)
    small_test = marker == "small" and _platform == "linux"
    marker = _utility.marker[marker] if marker in _utility.marker and not small_test else marker
    marker = "small" if small_test else (marker[0] if len(marker) > 0 else marker)
    _fig.subplot.point_marker.append(marker)
    
def _line_marker(marker = None):
    index = len(set(_fig.subplot.line_marker)) % len(_utility.marker_sequence)
    marker_none = _utility.marker_sequence[index]
    marker = "" if marker == "" else marker
    marker = _utility.set_if_none(marker, marker_none)
    small_test = marker == "small" and _platform == "linux"
    marker = _utility.marker[marker] if marker in _utility.marker and not small_test else marker
    marker = "small" if small_test else (marker[0] if len(marker) > 0 else marker)
    _fig.subplot.line_marker.append(marker)

def _point_color(color = None):
    color = None if color not in _utility.color_sequence else color
    index = len(set(_fig.subplot.point_color)) % len(_utility.color_sequence)
    color_none = _utility.color_sequence[index]
    color = _utility.set_if_none(color, color_none)
    _fig.subplot.point_color.append(color)
    
def _line_color(color = None):
    color = None if color not in _utility.color_sequence else color
    index = len(set(_fig.subplot.line_color)) % len(_utility.color_sequence)
    color_none = _utility.color_sequence[index]
    color = _utility.set_if_none(color, color_none)
    _fig.subplot.line_color.append(color)

def _data(*args):
    x, y = _utility.get_data(*args)
    _fig.subplot.x.append(x)
    _fig.subplot.y.append(y)
    _fig.subplot.signals += 1

def _fillx(fill = None):
    fill = _utility.set_if_none(fill, False)
    fill = bool(fill)
    _fig.subplot.fillx.append(fill)

def _filly(fill = None):
    fill = _utility.set_if_none(fill, False)
    fill = bool(fill)
    _fig.subplot.filly.append(fill)

##############################################
###########    Clear Functions    ############
##############################################
def clear_terminal():
    _utility.write('\033c')
    _utility._terminal_printed_lines_cnt = 0
clear_terminal.__doc__ = _docstrings.clear_terminal_doc
clt = clear_terminal

def clear_terminal_printed_lines():
    # clear the lines that plotext had printed
    # (plus 1 because the last line would not has an \n at the end)
    n = _utility._terminal_printed_lines_cnt + 1
    for i in range(n):
        _utility.write("\033[2K")
        if i < n - 1:
            _utility.write("\033[A")
            _utility.write("\033[2K")
    _utility._terminal_printed_lines_cnt = 0

def clear_figure():
    _fig.__init__()
clear_figure.__doc__ = _docstrings.clear_figure_doc
clf = clear_figure

def clear_plot():
    _fig.subplot.__init__(_fig.row, _fig.col)
clear_plot.__doc__ = _docstrings.clear_plot_doc
clp = clear_plot

def clear_data():
    _fig.subplot.x = []
    _fig.subplot.y = []
    _fig.subplot.signals = 0
clear_data.__doc__ = _docstrings.clear_data_doc
cld = clear_data
    
##############################################
############    Set Functions    #############
##############################################
def plotsize(width = None, height = None):
    width, height = _utility.set_first_to_both(width, height)
    width, height = _utility.set_list_to_both(width, height)
    _fig.subplot.width_set = width
    _fig.subplot.height_set = height
plotsize.__doc__ = _docstrings.plotsize_doc
plot_size = plotsize


def title(label = None):
    label = _utility.set_if_none(label, _fig.subplot.title)
    label = None if label == "" else label
    _fig.subplot.title = label
title.__doc__ = _docstrings.title_doc

def xlabel(label = ""):
    label = _utility.set_if_none(label, _fig.subplot.xlabel)
    _fig.subplot.xlabel = label
xlabel.__doc__ = _docstrings.xlabel_doc
    
def ylabel(label_left = "", label_right = ""):
    label_left = _utility.set_if_none(label_left, _fig.subplot.ylabel[0])
    label_right = _utility.set_if_none(label_right, _fig.subplot.ylabel[1])
    _fig.subplot.ylabel = [label_left, label_right]
ylabel.__doc__ = _docstrings.ylabel_doc

def xaxes(x = None, y = None):
    x, y = _utility.set_first_to_both(x, y)
    y = bool(y)
    x, y = _utility.set_list_if_none([x, y], _fig.subplot.xaxes)
    x = bool(x)
    x, y = _utility.set_list_to_both(x, y)
    _fig.subplot.xaxes = [x, y]
xaxes.__doc__ = _docstrings.xaxes_doc

def yaxes(x = None, y = None):
    x, y = _utility.set_first_to_both(x, y)
    y = bool(y)
    x, y = _utility.set_list_if_none([x, y], _fig.subplot.yaxes)
    x = bool(x)
    x, y = _utility.set_list_to_both(x, y)
    _fig.subplot.yaxes = [x, y]
yaxes.__doc__ = _docstrings.yaxes_doc

def grid(x = None, y = None):
    x, y = _utility.set_first_to_both(x, y)
    y = bool(y)
    x, y = _utility.set_list_if_none([x, y], _fig.subplot.grid)
    x = bool(x)
    x, y = _utility.set_list_to_both(x, y)
    _fig.subplot.grid = [x, y]
grid.__doc__ = _docstrings.grid_doc


def axes_color(color = "white"):
    color = _utility.set_if_none(color, _fig.subplot.axes_color)
    color = "white" if color not in list(_utility.background_color.keys()) else color
    _fig.subplot.axes_color = color
axes_color.__doc__ = _docstrings.axes_color_doc

def ticks_color(color = "black"):
    color = _utility.set_if_none(color, _fig.subplot.ticks_color)
    color = "black" if color not in list(_utility.fullground_color.keys()) else color
    _fig.subplot.ticks_color = color
ticks_color.__doc__ = _docstrings.ticks_color_doc

def canvas_color(color = "white"):
    color = _utility.set_if_none(color, _fig.subplot.canvas_color)
    color = "white" if color not in list(_utility.background_color.keys()) else color
    _fig.subplot.canvas_color = color
canvas_color.__doc__ = _docstrings.canvas_color_doc

def _colorless_subplot(subplot):
    subplot.point_color = ["none"] * len(subplot.point_color)
    subplot.line_color = ["none"] * len(subplot.line_color)
    subplot.axes_color = "none"
    subplot.ticks_color = "none"
    subplot.canvas_color = "none"

def colorless():
    _colorless_subplot(_fig.subplot)
colorless.__doc__ = _docstrings.colorless_doc
cls = colorless


def xlim(left = None, right = None):
    left, right = _utility.set_list_to_both(left, right)
    left, right = min(left, right), max(left, right)
    _fig.subplot.xlim_plot = [left, right]
xlim.__doc__ = _docstrings.xlim_doc

def ylim(lower = None, upper = None, yaxis = "left"):
    lower, upper = _utility.set_list_to_both(lower, upper)
    lower, upper = min(lower, upper), max(lower, upper)
    if yaxis == "left":
        _fig.subplot.ylim_plot_left = [lower, upper]
    elif yaxis == "right":
        _fig.subplot.ylim_plot_right = [lower, upper]
ylim.__doc__ = _docstrings.ylim_doc


def ticks(x = None, y = None):
    x, y = _utility.set_first_to_both(x, y)
    x, y = _utility.set_list_to_both(x, y)
    x_none, y_none = 5, 7
    x = _utility.set_if_none(x, x_none)
    y = _utility.set_if_none(y, y_none)
    _fig.subplot.ticks = [x, y]
ticks.__doc__ = _docstrings.ticks_doc

def xticks(ticks = [], labels = None):
    ticks, labels = _utility.set_first_to_both(list(ticks), labels)
    labels = list(map(str, list(labels)))
    ticks, labels = _utility.sort_data(ticks, labels)
    _fig.subplot.xticks, _fig.subplot.xlabels = ticks, labels
    _fig.subplot.ticks[0] = len(ticks)
xticks.__doc__ = _docstrings.xticks_doc

def yticks(ticks = [], labels = None, yaxis = "left"):
    ticks, labels = _utility.set_first_to_both(list(ticks), labels)
    labels = list(map(str, list(labels)))
    ticks, labels = _utility.sort_data(ticks, labels)
    if yaxis == "left":
        _fig.subplot.yticks_left, _fig.subplot.ylabels_left = ticks, labels
    elif yaxis == "right":
        _fig.subplot.yticks_right, _fig.subplot.ylabels_right = ticks, labels
    _fig.subplot.ticks[1] = len(ticks)
yticks.__doc__ = _docstrings.yticks_doc

def xscale(scale = None):
    scale = _utility.set_if_none(scale, _fig.subplot.xscale)
    scale = "linear" if not (scale in ["linear", "log"]) else scale
    _fig.subplot.xscale = scale
xscale.__doc__ = _docstrings.xscale_doc

def yscale(scale = None, yaxis = "left"):
    scale = _utility.set_if_none(scale, _fig.subplot.xscale)
    scale = "linear" if not (scale in ["linear", "log"]) else scale
    if yaxis == "right":
        _fig.subplot.yscale[1] = scale
    else:
        _fig.subplot.yscale[0] = scale
yscale.__doc__ = _docstrings.yscale_doc

##############################################
###########    Show Functions    #############
##############################################
def show(hide = False):
    _figure_size_max()
    _figure_size()

    #_plots_size()
    _coherent_sizes()

    for r in range(_fig.rows):
        for c in range(_fig.cols):
            
            subplot = _fig.subplots[r][c]

            _previous_size(subplot)
            
            _sort_data(subplot)

            _height(subplot)

            _ylim_data(subplot)
            _ylim_plot(subplot)
            _yticks(subplot)

            _width(subplot)
            
            _xlim_data(subplot)
            _xlim_plot(subplot)
            _xticks(subplot)
            
            _matrix(subplot)

            _add_xgrid(subplot)
            _add_ygrid(subplot)
            
            _add_data(subplot)

            _add_legend(subplot)
            _add_yaxis(subplot)
            _add_xaxis(subplot)
            _add_title(subplot)
            _add_labels(subplot)
            
    _join_matrices()

    _fig.canvas = _utility.get_canvas(_fig.matrix)
    if hide:
        return
    _utility.write(_fig.canvas)
        
show.__doc__ = _docstrings.show_doc

def _figure_size_max():
    _fig.width_max, _fig.height_max = terminal_size()
    _fig.height_max -= 3
    _fig.width_max -= (_fig.cols - 1)
    _fig.height_max -= (_fig.rows - 1)

def _figure_size():
    # width = _utility.set_if_none(_fig.width, _fig.width_max)
    # height = _utility.set_if_none(_fig.height, _fig.height_max)

    # width = abs(int(width))
    # height = abs(int(height))

    # width = _fig.width_max if width > _fig.width_max else width
    # height = _fig.height_max if height > _fig.height_max else height

    _fig.width = _fig.width_max
    _fig.height = _fig.height_max

def _coherent_sizes():
    width = []
    for c in range(_fig.cols):
        w = [_fig.subplots[r][c].width for r in range(_fig.rows)]
        w = [el for el in w if el  is not None]
        w = max(w, default = None)
        width.append(w)
    height = []
    for r in range(_fig.rows):
        h = [_fig.subplots[r][c].height for c in range(_fig.cols)]
        h = [el for el in h if el  is not None]
        h = max(h, default = None)
        height.append(h)
    for c in range(_fig.cols):
        for r in range(_fig.rows):
            subplot = _fig.subplots[r][c]
            subplot.width = width[c]
            subplot.height = height[r]

def _previous_size(subplot):
    row, col = subplot.row, subplot.col
    width, height = 0, 0
    for r in range(row):
        height += _fig.subplots[r][0].height
    for c in range(col):
        width += _fig.subplots[0][c].width
    _fig.previous_width = width
    _fig.previous_height = height

def _sort_data(subplot):
    subplot.x_left = [subplot.x[i] for i in range(len(subplot.x)) if subplot.yaxis[i] == "left"]
    subplot.y_left = [subplot.y[i] for i in range(len(subplot.x)) if subplot.yaxis[i] == "left"]
    subplot.signals_left = len(subplot.y_left)

    subplot.x_right = [subplot.x[i] for i in range(len(subplot.x)) if subplot.yaxis[i] == "right"]
    subplot.y_right = [subplot.y[i] for i in range(len(subplot.x)) if subplot.yaxis[i] == "right"]
    subplot.signals_right = len(subplot.y_right)

    subplot.data_left = subplot.x_left != [] and subplot.y_left != []
    subplot.data_right = subplot.x_right != [] and subplot.y_right != []
    subplot.data = subplot.data_left or subplot.data_right
    
def _height(subplot):
    subplot.height_max = _fig.height - _fig.previous_height
    height_none = subplot.height_max // (_fig.rows - subplot.row)
    height = _utility.set_if_none(subplot.height_set, height_none)
    height = abs(int(height))
    
    height = subplot.height_max if height > subplot.height_max else height
    subplot.height = height

    subplot.xaxes[0] = 0 if height < 2 else subplot.xaxes[0]
    subplot.xaxes[1] = 0 if height < 3 else subplot.xaxes[1]
    subplot.ticks[0] = 0 if height < 4 else subplot.ticks[0]

    subplot.title = "" if height < 5 else subplot.title
    subplot.xlabel = "" if height < 6 else subplot.xlabel
    subplot.ylabel = ["", ""] if height < 6 else subplot.ylabel

    xaxis_low = int(subplot.xaxes[0] and subplot.data)
    xaxis_up = int(subplot.xaxes[1] and subplot.data)
    xticks = bool(subplot.ticks[0] and subplot.data)
    title = int(subplot.title != "")
    labels = int(subplot.xlabel != "" or subplot.ylabel != ["", ""])
    tot = title + xaxis_low + xaxis_up + xticks + labels
    
    subplot.height_canvas = subplot.height - tot

def _ylim_data(subplot):
    y_left = [_utility.log(subplot.y_left[s]) if subplot.yscale[0] == "log" else subplot.y_left[s] for s in range(subplot.signals_left)]
    y_right = [_utility.log(subplot.y_right[s]) if subplot.yscale[1] == "log" else subplot.y_right[s] for s in range(subplot.signals_right)]
    subplot.ylim_data_left = _utility.get_lim_data(y_left)
    subplot.ylim_data_right = _utility.get_lim_data(y_right)

def _ylim_plot(subplot):
    subplot.ylim_plot_left = _utility.set_list_if_none(subplot.ylim_plot_left, subplot.ylim_data_left)
    subplot.ylim_plot_right = _utility.set_list_if_none(subplot.ylim_plot_right, subplot.ylim_data_right)
    #subplot.dy = (subplot.ylim_plot[1] - subplot.ylim_plot[0]) / subplot.height_canvas

def _yticks(subplot):
    if subplot.yticks_left == [] and subplot.ticks[1] and subplot.data_left:
        if subplot.yscale[0] == "linear":
            subplot.yticks_left = _utility.get_ticks(subplot.ylim_plot_left, subplot.ticks[1])
            subplot.ylabels_left = _utility.get_labels(subplot.yticks_left)
        if subplot.yscale[0] == "log":
            subplot.yticks_left, subplot.ylabels_left = _utility.get_log_ticks(subplot.ylim_plot_left, subplot.ticks[1])
    subplot.yticks_rows_left = _utility.get_matrix_data(subplot.yticks_left, subplot.ylim_plot_left, subplot.height_canvas)

    if subplot.yticks_right == [] and subplot.ticks[1] and subplot.data_right:
        if subplot.yscale[1] == "linear":
            subplot.yticks_right = _utility.get_ticks(subplot.ylim_plot_right, subplot.ticks[1])
            subplot.ylabels_right = _utility.get_labels(subplot.yticks_right)
        if subplot.yscale[1] == "log":
            subplot.yticks_right, subplot.ylabels_right = _utility.get_log_ticks(subplot.ylim_plot_right, subplot.ticks[1])
    subplot.yticks_rows_right = _utility.get_matrix_data(subplot.yticks_right, subplot.ylim_plot_right, subplot.height_canvas)

def _width(subplot):
    subplot.width_max = _fig.width - _fig.previous_width
    width_none = subplot.width_max // (_fig.cols - subplot.col)
    width = _utility.set_if_none(subplot.width_set, width_none)
    width = abs(int(width))
    
    width = subplot.width_max if width > subplot.width_max else width
    subplot.width = width

    subplot.yaxes[0] = 0 if width < 2 else subplot.yaxes[0]
    subplot.yaxes[1] = 0 if width < 3 else subplot.yaxes[1]

    ylabels_width_left = max(map(len, subplot.ylabels_left), default = 0) * bool(subplot.ticks[1] and subplot.data_left)
    subplot.ticks[1] = 0 if width < 3 + ylabels_width_left else subplot.ticks[1]
    ylabels_width_left = 0 if width < 3 + ylabels_width_left else ylabels_width_left

    ylabels_width_right = max(map(len, subplot.ylabels_right), default = 0) * bool(subplot.ticks[1] and subplot.data_right)
    ylabels_width_right = 0 if width < ylabels_width_right + ylabels_width_left + 3 else ylabels_width_right

    yaxis_left = int(subplot.yaxes[0] and subplot.data)
    yaxis_right = int(subplot.yaxes[1] and subplot.data)
    tot = ylabels_width_left + yaxis_left + yaxis_right + ylabels_width_right 
    
    subplot.width_canvas = subplot.width - tot
    subplot.ylabels_width_left = ylabels_width_left
    subplot.ylabels_width_right = ylabels_width_right

    ylabel_length = len(subplot.ylabel[0]) + 3
    if subplot.width < ylabel_length:
        subplot.height_canvas += 1

def _xlim_data(subplot):
    x = [_utility.log(subplot.x[s]) if subplot.xscale == "log" else subplot.x[s] for s in range(subplot.signals)]
    subplot.xlim_data = _utility.get_lim_data(x)

def _xlim_plot(subplot):
    subplot.xlim_plot = _utility.set_list_if_none(subplot.xlim_plot, subplot.xlim_data)
    #subplot.dy = (subplot.ylim_plot[1] - subplot.ylim_plot[0]) / subplot.height_canvas

def _xticks(subplot):
    if subplot.xticks == [] and subplot.ticks[0]:
        if subplot.xscale == "linear":
            subplot.xticks = _utility.get_ticks(subplot.xlim_plot, subplot.ticks[0])
            subplot.xlabels = _utility.get_labels(subplot.xticks)
        if subplot.xscale == "log":
            subplot.xticks, subplot.xlabels = _utility.get_log_ticks(subplot.xlim_plot, subplot.ticks[0])
    subplot.xticks_cols = _utility.get_matrix_data(subplot.xticks, subplot.xlim_plot, subplot.width_canvas)

def _matrix(subplot):
    marker = [" ", "none", subplot.canvas_color]
    subplot.matrix = [[marker[:] for c in range(subplot.width_canvas)] for r in range(subplot.height_canvas)]

def _add_xgrid(subplot):
    if not subplot.grid[0]:
        return 
    grid_color = subplot.ticks_color
    for c in subplot.xticks_cols:
        x, y = _utility.get_line([c, c], [0, subplot.height_canvas])
        marker = "│"
        subplot.matrix = _utility.update_matrix(subplot.matrix, x, y, marker, grid_color)

def _add_ygrid(subplot):
    if not subplot.grid[1]:
        return 
    grid_color = subplot.ticks_color
    for r in subplot.yticks_rows_left + subplot.yticks_rows_right:
        x, y = _utility.get_line([0, subplot.width_canvas], [r, r])
        marker = "─"
        subplot.matrix = _utility.update_matrix(subplot.matrix, x, y, marker, grid_color)
        if subplot.grid[0]:
            x = subplot.xticks_cols
            y = [r] * len(x)
            marker = "┼"
            subplot.matrix = _utility.update_matrix(subplot.matrix, x, y, marker, grid_color)

def _add_data(subplot):
    for s in range(len(subplot.x)):
        point_marker, point_color = subplot.point_marker[s], subplot.point_color[s]
        line_marker, line_color = subplot.line_marker[s], subplot.line_color[s]
        
        x, y = subplot.x[s], subplot.y[s]
        x_test = subplot.xscale == "log"
        x = _utility.log(x) if x_test else x
        y_test = (subplot.yscale[0] == "log" and subplot.yaxis[s] == "left") or (subplot.yscale[1] == "log" and subplot.yaxis[s] == "right")
        y = _utility.log(y) if y_test else y
        mf = 2 if point_marker == "small" or line_marker == "small" else 1 # small marker factor
        ylim_plot = subplot.ylim_plot_left if subplot.yaxis[s] == "left" else subplot.ylim_plot_right
        x_point = _utility.get_matrix_data(x, subplot.xlim_plot, mf * subplot.width_canvas)
        y_point = _utility.get_matrix_data(y, ylim_plot, mf * subplot.height_canvas)

        x_line, y_line = [], []
        if line_marker != "":
            x_line, y_line = _utility.get_line(x_point, y_point)
        
        if subplot.fillx[s]:
            height0 = _utility.get_matrix_data([0], ylim_plot, mf * subplot.height_canvas)[0]
            x_point, y_point = _utility.fill_data(x_point, y_point, height0)
            x_line, y_line = _utility.fill_data(x_line, y_line, height0)
        if subplot.filly[s]:
            width0 = _utility.get_matrix_data([0], subplot.xlim_plot, mf * subplot.width_canvas)[0] 
            y_point, x_point = _utility.fill_data(y_point, x_point, width0)
            y_line, x_line = _utility.fill_data(y_line, x_line, width0)
            
        x_line = [el / mf for el in x_line]
        y_line = [el / mf for el in y_line]
        if line_marker != "":
            subplot.matrix = _utility.update_matrix(subplot.matrix, x_line, y_line, line_marker, line_color)
            
        x_point = [el / mf for el in x_point]
        y_point = [el / mf for el in y_point]
        if point_marker != "":
            subplot.matrix = _utility.update_matrix(subplot.matrix, x_point, y_point, point_marker, point_color)

def _add_legend(subplot):
    label = subplot.label
    show = any([el != "" for el in label])
    side_test = subplot.data_left and subplot.data_right
    if not (show or side_test):
        return
    l = len(label)
    label = ["signal " + str(i + 1) if label[i] == "" and show else label[i] for i in range(l)]
    side_label = ["[" + subplot.yaxis[i] + "] " if side_test else "" for i in range(l)]
    label = [side_label[i] + label[i] for i in range(l)]
    label = [" " + el + " " for el in label]
    label = [list(el) for el in label]
    w = max(map(len, label))
    label = [el + [" "] * (w - len(el)) for el in label]
    legend = [[] for i in range(l)]
    legend_color = [[] for i in range(l)]
    for i in range(l):
        point_marker, line_marker = subplot.point_marker[i], subplot.line_marker[i]
        point_color, line_color = subplot.point_color[i], subplot.line_color[i]
        marker = point_marker if point_marker != "" else line_marker
        marker = "▄" if marker == "small" else marker
        color = point_color if point_marker != "" else line_color
        legend[i] += [marker] * 3
        legend[i] += label[i]
        legend_color[i] += [color] * 3
        legend_color[i] += [subplot.ticks_color] * w
    legend = [legend[i] for i in range(len(legend)) if subplot.label_show[i]]
    legend_color = [legend_color[i] for i in range(len(legend_color)) if subplot.label_show[i]]
    legend = _utility.frame_matrix(legend)
    legend_color = _utility.frame_matrix(legend_color, subplot.ticks_color)
    legend = [[ [legend[i][j], legend_color[i][j], subplot.canvas_color] for j in range(len(legend[0]))] for i in range(len(legend))]
    subplot.matrix = _utility.insert(legend, subplot.matrix) if show or side_test else subplot.matrix
    # To do: Legend frame interferes with grid lines  

def _add_yaxis(subplot):
    if subplot.x == []:
        return
    labels_left = [" " * subplot.ylabels_width_left for r in range(subplot.height_canvas)]
    for i in range(len(subplot.yticks_rows_left)):
        r = subplot.yticks_rows_left[i]
        if r in range(subplot.height_canvas):
            labels_left[r] = str(subplot.ylabels_left[i])[ : subplot.ylabels_width_left]
    labels_left = [" " * (subplot.ylabels_width_left - len(el)) + el for el in labels_left]
    labels_left = [list(el) for el in labels_left]
    labels_left = [[[sub_el, subplot.ticks_color, subplot.axes_color] for sub_el in el] for el in labels_left]
    labels_left = labels_left[::-1]
    

    ytick = "┼" if subplot.grid[1] else "┤"
    ytick = "│" if subplot.ylabels_width_right == 0 and subplot.grid[1] == False else ytick

    ytick =  ("┼" if subplot.ylabels_width_left != 0 else "├") if subplot.grid[1] else ("┤" if subplot.ylabels_width_left != 0 else "│")
    axis_left = [(ytick  if r in subplot.yticks_rows_right + subplot.yticks_rows_left else "│") for r in range(subplot.height_canvas)]
    axis_left = [list(el) for el in axis_left]
    axis_left = [[[sub_el, subplot.ticks_color, subplot.axes_color] for sub_el in el] for el in axis_left]
    axis_left = axis_left[::-1]

    labels_right = [" " * subplot.ylabels_width_right for r in range(subplot.height_canvas)]
    for i in range(len(subplot.yticks_rows_right)):
        r = subplot.yticks_rows_right[i]
        if r in range(subplot.height_canvas):
            labels_right[r] = str(subplot.ylabels_right[i])[ : subplot.ylabels_width_right]
    labels_right = [el + " " * (subplot.ylabels_width_right - len(el)) for el in labels_right]
    labels_right = [list(el) for el in labels_right]
    labels_right = [[[sub_el, subplot.ticks_color, subplot.axes_color] for sub_el in el] for el in labels_right]
    labels_right = labels_right[::-1]

    ytick =  ("┼" if subplot.ylabels_width_right != 0 else "┤")  if subplot.grid[1] else ("├" if subplot.ylabels_width_right != 0 else "│") 
    axis_right = [(ytick if r in subplot.yticks_rows_right + subplot.yticks_rows_left else "│") for r in range(subplot.height_canvas)]
    axis_right = [list(el) for el in axis_right]
    axis_right = [[[sub_el, subplot.ticks_color, subplot.axes_color] for sub_el in el] for el in axis_right]
    axis_right = axis_right[::-1]
    
    if subplot.yaxes[0]:
        for r in range(subplot.height_canvas):
            subplot.matrix[r] = axis_left[r] + subplot.matrix[r]
    if subplot.yaxes[1]:
        for r in range(subplot.height_canvas):
            subplot.matrix[r] = subplot.matrix[r] + axis_right[r]
    if subplot.ticks[1]:
        for r in range(subplot.height_canvas):
            subplot.matrix[r] = labels_left[r] + subplot.matrix[r] + labels_right[r]

def _add_xaxis(subplot):
    if subplot.x == []:
        return
    axis_lower = [" "] * subplot.ylabels_width_left + ["└"] * subplot.yaxes[0]
    axis_lower += ["─" for r in range(subplot.width_canvas)]
    axis_lower += ["┘"] * subplot.yaxes[1] + [" "] * subplot.ylabels_width_right

    axis_up = [" "] * subplot.ylabels_width_left + ["┌"] * subplot.yaxes[0]
    axis_up += ["─" for r in range(subplot.width_canvas)]
    axis_up += ["┐"] * subplot.yaxes[1] + [" "] * subplot.ylabels_width_right
    
    labels_lower =  [" "] * subplot.ylabels_width_left + [" "] * subplot.yaxes[0]
    iniz_length = len(labels_lower)
    labels_lower +=  [" " for r in range(subplot.width_canvas)]
    labels_lower += [" "] * subplot.yaxes[0] + [" "] * subplot.ylabels_width_right
    

    xtick_lower = "┼" if subplot.grid[0] else "┬"
    xtick_up = "┬" if subplot.grid[0] else "─"
    l = len(subplot.xticks_cols)
    for i in range(l):
         col = subplot.xticks_cols[i] + iniz_length
         #if col >= subplot.width:
         #    continue
         label = str(subplot.xlabels[i])
         label_length = len(label)
         label_col = list(range(max(col - label_length, 0), min(col + label_length + 1, subplot.width)))
         label_col = [c for c in label_col if c + label_length <= subplot.width]
         if label_col == []:
             continue
         label_col = min(label_col, key = lambda x : abs(x - (col - (label_length - 2) / 2)))
         if label_col + label_length > subplot.width:
             continue
         label_prev = labels_lower[label_col - 1: label_col + label_length + 1]
         label_prev = list(set(label_prev))
         
         if label_prev == [" "] or label_prev == []:
             labels_lower[label_col: label_col + label_length] = list(label)
             axis_lower[col] = xtick_lower
             axis_up[col] = xtick_up
         elif axis_lower[col] == "─":
             axis_lower[col] = "┴" if subplot.grid[0] else "─"
             axis_up[col] = "┬" if subplot.grid[0] else "─"
             
    axis_up = [[el, subplot.ticks_color, subplot.axes_color] for el in axis_up]
    axis_lower = [[el, subplot.ticks_color, subplot.axes_color] for el in axis_lower]
    labels_lower = [[el, subplot.ticks_color, subplot.axes_color] for el in labels_lower]
         
    if subplot.xaxes[0]:
        subplot.matrix += [axis_lower]
    if subplot.xaxes[1]:
        subplot.matrix = [axis_up] + subplot.matrix
    if subplot.ticks[0]:
        subplot.matrix += [labels_lower]

def _add_title(subplot):
    if subplot.title == "":
        return
    width_left = subplot.ylabels_width_left + int(subplot.yaxes[0])
    title = subplot.title[ : subplot.width_canvas]
    space1 = " " * (width_left + int((subplot.width_canvas - len(title)) / 2))
    space2 = " " * (subplot.width - len(title + space1))
    title = space1 + title + space2
    title = list(title)
    title = [[el, subplot.ticks_color, subplot.axes_color] for el in title]
    subplot.matrix = [title] + subplot.matrix

def _add_labels(subplot):
    if subplot.xlabel == "" and subplot.ylabel == ["", ""]:
        return
    width_max = subplot.width - 4 * 3
    
    ylabel_left = "[y] " + subplot.ylabel[0]
    width_left = subplot.ylabels_width_left + int(subplot.yaxes[0])
    ylabel_left = ylabel_left + " " * (width_left - len(ylabel_left))

    ylabel_left = ylabel_left[ : width_max // 3]

    ylabel_right = ""
    if subplot.ylabel[1] != "":
        ylabel_right = subplot.ylabel[1] + " [y]"
    xlabel = " " + subplot.xlabel + " [x] "
    l_left = len(ylabel_left)

    l_tot = len(ylabel_left + xlabel + ylabel_right)
    if l_tot > subplot.width:
        xlabel = ""
    l_tot = len(ylabel_left + xlabel + ylabel_right)
    if l_tot > subplot.width:
        ylabel_right = ""
    l_tot = len(ylabel_left + xlabel + ylabel_right)
    if l_tot > subplot.width:
        ylabel_left = ""

    space1 = " " * (width_left + int((subplot.width_canvas - len(xlabel)) / 2) - l_left)
    if space1 == '':
        return
    space1 = " " * subplot.width if space1 == '' else space1
    space2 = " " * (subplot.width - l_tot - len(space1))
    label = ylabel_left + space1 + xlabel + space2 + ylabel_right
    label = list(label)
    label = [[el, subplot.ticks_color, subplot.axes_color] for el in label]
    subplot.matrix += [label]
    #ToDo: a bit messy, need reordering

def _join_matrices():
    sep = " "
    sep = [sep, "none", "none"]
    matrix = []
    for c in range(_fig.cols):
        matrix_c = []
        for r in range(_fig.rows):
            matrix_c = _utility.join(matrix_c, _fig.subplots[r][c].matrix, sep, "vertical")
        matrix = _utility.join(matrix, matrix_c, sep, "horizontal")
        
    _fig.matrix = matrix
    size = [0, 0] if matrix == [] else [len(matrix[0]), len(matrix)]
    _fig.width, _fig.height = size


##############################################
#########    Plotting Functions    ###########
##############################################
def scatter(*args,
            yaxis = "left",
            label = "",
            marker = None,
            color = None,
            fillx = None,
            filly = None):
    _draw(
        *args,
        yaxis = yaxis,
        label = label,
        point_marker = marker,
        line_marker = "",
        point_color = color,
        line_color = "none",
        fillx = fillx,
        filly = filly)
scatter.__doc__ = _docstrings.scatter_doc

def plot(*args,
         yaxis = "left",
         label = "",
         marker = None,
         color = None,
         fillx = None,
         filly = None):
    _draw(
        *args,
        yaxis = yaxis,
        label = label,
        point_marker = "",
        line_marker = marker,
        point_color = "none",
        line_color = color,          
        fillx = fillx,
        filly = filly)
plot.__doc__ = _docstrings.plot_doc

def bar(*args,
        yaxis = "left",
        label = "",
        marker = "small",
        color = None,
        fill = True,
        width = 4 / 5,
        orientation = 'vertical'):
    x, y = _utility.get_data(*args)
    x, x_labels = _utility.bar_xdata(x)
    xbar, ybar = _utility.bars(x, y, width)
    if orientation in ['vertical', 'v']:
         fillx, filly = fill, False
         x_ticks = _fig.subplot.xticks + x
         x_labels = _fig.subplot.xlabels + x_labels
         xticks(x_ticks, x_labels)
    elif orientation in ['horizontal', 'h']:
         xbar, ybar = ybar, xbar
         fillx, filly = False, fill
         y_ticks = x + (_fig.subplot.yticks_left if yaxis == "left" else _fig.subplot.yticks_right)
         y_labels = x_labels + (_fig.subplot.ylabels_left if yaxis == "left" else _fig.subplot.ylabels_right)
         yticks(y_ticks, y_labels, yaxis = yaxis)
    for b in range(len(x)):
        xb, yb = xbar[b][1:3] + xbar[b][3:5], ybar[b][1:3] + ybar[b][3:5]
        if not fill:
            xb, yb = xbar[b], ybar[b]
            fillx, filly = False, False
        if list(set(yb)) != [0]:
            plot(xb, yb, yaxis = yaxis, label = label, marker = marker, color = color, fillx = fillx, filly = filly)
            if b != 0:
                _fig.subplot.point_color[-1] = _fig.subplot.point_color[-2]
                _fig.subplot.line_color[-1] = _fig.subplot.line_color[-2]
                _fig.subplot.label_show[-1] = False
    # _sort_data(_fig.subplot)
    # y_plot = _fig.subplot.y_left if yaxis == "left" else _fig.subplot.y_right
    # if orientation in ['horizontal', 'h']:
    #     y_plot = _fig.subplot.x_left if yaxis == "left" else _fig.subplot.x_right
    # m, M = _utility.get_lim_data(y_plot)
    # if m * M > 0:
    #     m = 0
    # if orientation in ['vertical', 'v']:
    #     #ylim(m, M, yaxis = yaxis)
    #     pass
    # else:
    #     xlim(m, M)

bar.__doc__ =  _docstrings.bar_doc

def hist(data,
         bins = 10,
         yaxis = "left",
         label = "",
         marker = "small",
         color = None,
         fill = True,
         width = 4 / 5,
         orientation = 'vertical'):
    x, y = _utility.hist_data(data, bins)
    bar(x, y, yaxis = yaxis, label = label, marker = marker, color = color, fill = fill, width = width, orientation= orientation)
hist.__doc__ = _docstrings.plot_doc

##############################################
##########    Other Functions    #############
##############################################
string_to_time = _utility.string_to_time
string_to_time.__doc__ = _docstrings.string_to_time_doc

def get_canvas():
    return _fig.canvas
get_canvas.__doc__ = _docstrings.get_canvas_doc

sleep = _utility.sleep
sleep.__doc__ = _docstrings.sleep_doc

def savefig(path = None):
    path = _utility.check_path(path)
    with open(path , "w+", encoding = "utf-8") as file:
        file.write(_utility.remove_color(_fig.canvas))
    print("plot saved as " + path)
savefig.__doc__ = _docstrings.savefig_doc
save_fig = savefig

terminal_size = _utility.terminal_size
terminal_size.__doc__ = _docstrings.terminal_size_doc

version = _utility.version
version.__doc__ = _docstrings.version_doc

docstrings = _utility.docstrings
docstrings.__doc__ = _docstrings.docstrings_doc

colors = _utility.colors
colors.__doc__ = _docstrings.colors_doc

markers = _utility.markers
markers.__doc__ = _docstrings.markers_doc

sin = _utility.sin
sin.__doc__ = _docstrings.sin_doc


if __name__ == "__main__":
    #test()
    import plotext as plt
    plt.test()



