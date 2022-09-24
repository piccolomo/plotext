# /usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################
###########    Initialization    #############
##############################################
import sys as _sys
import os as _os

class _parameters():
    def __init__(self):
        self.width = None
        self.height = None
        #self.force_size = None

        self.title = None
        self.xlabel = None
        self.ylabel = None
        self.legend = []

        self.axes = [None, None]
        self.ticks = [None, None] 
        self.xticks = None
        self.xlabels = []
        self.yticks = None
        self.ylabels = []
        self.grid = [None, None]
        self.frame = None

        self.point_marker = []
        self.line_marker = []

        self.axes_color = None
        self.ticks_color = None
        self.canvas_color = None
        self.point_color = []
        self.line_color = []

        self.x = []
        self.y = []
        self.xlim_data = [None, None]
        self.ylim_data = [None, None]
        self.xlim_plot = [None, None]
        self.ylim_plot = [None, None]

        self.fill = []

class _constants():
    def __init__(self):
        self.default_marker = "•"

        self.matrix = [[]]
        self.canvas = ""

par = _parameters()
con = _constants()

def _platform():
    if "win" in _sys.platform:
        return "windows"
    else:
        return "linux"

def _shell():
    if 'idlelib.run' in _sys.modules:
        return "idle"
    elif "spyder" in _sys.modules:
        return "spyder"
    else:
        return "regular"
    
def _nocolor():
    shl = shell()
    if shl == "idle" or shl == "spyder":
        return True
    else:
        return False

par.platform = _platform()   
par.shell = _shell()
par.nocolor = False

if par.platform == "windows":
    import subprocess
    subprocess.call('', shell = True)

if par.shell == "idle" or par.shell == "spyder":
    par.nocolor = True


##############################################
########    Draw Basic Function    ###########
##############################################
def _draw(*args, **kwargs):
    width()
    height()
    #force_size()

    title()
    xlabel()
    ylabel()
    _label(kwargs.get("label"))

    axes()
    grid()
    frame()

    _point_marker(kwargs.get("point_marker"))
    _line_marker(kwargs.get("line_marker"))
    
    axes_color()
    ticks_color()
    canvas_color()
    
    _point_color(kwargs.get("point_color"))
    _line_color(kwargs.get("line_color"))

    _data(*args)
    ticks()
    xlim()
    ylim()
    
    _fill(kwargs.get("fill"))
    
##############################################
########    Draw Called Functions     ########
##############################################
def _point_marker(x = None):
    if type(x) == int:
        x = _marker[x]
    x_none = [el for el in _marker if el not in (par.point_marker + par.line_marker)]
    x_none = "none" if x_none == [] else x_none[0]
    x = _set_var_if_none(x, x_none)
    if x == " ":
        x = ""
    par.point_marker.append(x[:1])

def _line_marker(x = None):
    if type(x) == int:
        x = _marker[x]
    x_none = [el for el in _marker if el not in (par.point_marker + par.line_marker)]
    x_none = "none" if x_none == [] else x_none[0]
    x = _set_var_if_none(x, x_none)
    if x == " ":
        x = ""
    par.line_marker.append(x[:1])

def _point_color(x = None):
    x_none = [el for el in _color_sequence if el not in (par.point_color + par.line_color)]
    x_none = "none" if x_none == [] else x_none[0]
    x = _set_var_if_none(x, x_none)
    par.point_color.append(x)

def _line_color(x = None):
    x_none = [el for el in _color_sequence if el not in (par.point_color + par.line_color)]
    x_none = "none" if x_none == [] else x_none[0]
    x = _set_var_if_none(x, x_none)
    par.line_color.append(x)

def _label(x = None):
    x = _set_var_if_none(x, "")
    par.legend.append(x)

def _data(*args):
    if len(args) == 0:
        x, y = [], []
    elif len(args) == 1:
        y = args[0]
        x = list(range(len(y)))
    else:
        x = args[0]
        y = args[1]
    x, y = list(x), list(y)
    length = min(len(x), len(y))
    if len(x) != len(y):
        x = x[ : length]
        y = y[ : length]
    par.x.append(x)
    par.y.append(y)

def _fill(x = None):
    x = _set_var_if_none(x, False)
    if x == " ":
        x = ""
    par.fill.append(x)

##############################################
########    Other Set Functions     ##########
##############################################
def width(width = None):
    """\nIt sets the figure width.\n"""
    par.width = width

def height(height = None):
    """\nIt sets the figure height.\n"""
    par.height = height

def figsize(x = None, y = None):
    """\nIt changes the figure size. It requires two parameters: the width and height of the desired figure. 
Note that figsize(width, height) is equivalent to figsize([width, height]) and that figsize(integer) is equivalent to figsize(integer, integer).\n"""
    x, y = _set_first_to_both(x, y)
    x, y = _set_list_to_both(x, y)
    width(x)
    height(y)

def axes(x = None, y = None):
    """\nIt sets whatever or not to show the x and y axis respectively. It requires two Boolean parameters, one for each axis. 
Note that axes(bool_x, bool_y) is equivalent to axes([bool_x, bool_y]) and that axes(bool) is equivalent to axes(bool, bool).\n"""
    x, y = _set_first_to_both(x, y)
    x, y = _set_list_to_both(x, y)
    x = _set_var_if_none(x, True)
    y = _set_var_if_none(y, True)
    par.axes = [x, y]
    
def ticks(x = None, y = None):
    """\nIt sets the number of numerical ticks to show on the x and y ticks respectively. It requires two parameters, one for each axis. 
Note that ticks(width, height) is equivalent to ticks([width, height]) and that ticks(integer) is equivalent to ticks(integer, integer).\n"""
    x, y = _set_first_to_both(x, y)
    x, y = _set_list_to_both(x, y)
    xl = max(map(len, par.x))
    yl = max(map(len, par.y))
    x = _set_var_if_none(x, min(7, xl))
    y = _set_var_if_none(y, min(5, yl))
    par.ticks = [x, y]
    
def grid(x = None, y = None):
    """\nIt sets whatever or not to show the x and y grid lines respectively. It requires two Boolean parameters, one for each axis. 
Note that grid(bool_x, bool_y) is equivalent to grid([bool_x, bool_y]) and that grid(bool) is equivalent to grid(bool, bool).\n"""
    x, y = _set_first_to_both(x, y)
    x, y = _set_list_to_both(x, y)
    x = _set_var_if_none(x, False)
    y = _set_var_if_none(y, False)
    par.grid = [x, y]

def frame(x = None):
    """\nIt sets whatever or not to show the frame around the plot and it requires a Boolean parameter. Note that frame(False) doesn't remove the primary axes. For that, use the function axes() instead. \n"""
    x = _set_var_if_none(x, True)
    par.frame = x

def axes_color(x = None):
    """\nIt sets the color relative to the figure background. Access the function plt.colors() to check the available color codes.\n"""
    x = _set_var_if_none(x, "white")
    par.axes_color = x
    
def canvas_color(x = None):
    """\nIt sets the canvas color. Access the function plt.colors() to check the available color codes.\n"""
    x = _set_var_if_none(x, "white")
    par.canvas_color = x
    
def ticks_color(x = None):
    """\nIt sets the color relative to any writing in the plot (title, axes labels, ticks and legend). Access the function plt.colors() to check the available color codes.\n"""
    x = _set_var_if_none(x, "black")
    par.ticks_color = x

def nocolor():
    """\nIt removes all color settings from the plot so that the final plot will be colorless.\n"""
    par.axes_color = "none"
    par.canvas_color = "none"
    par.ticks_color = "none"
    par.point_color = ["none"] * len(par.point_color)
    par.line_color = ["none"] * len(par.line_color)

def title(x = None):
    """\nIt set the plot title and it requires a string.\n"""
    x = _set_var_if_none(x, "")
    par.title = x

def xlabel(x = None):
    """\nIt set the plot x label and it requires a string.\n"""
    x = _set_var_if_none(x, "")
    par.xlabel = x

def ylabel(x = None):
    """\nIt set the plot y label and it requires a string.\n"""
    x = _set_var_if_none(x, "")
    par.ylabel = x

def legend(legend = None):
    """\nIt sets the plot legend and it requires a list of strings. If all strings are empty no legend is printed.\n"""
    legend = list(legend)
    if legend == None:
        legend = [None] * len(par.legend)
    par.label = legend

def xlim(x = None, y = None):
    """\nIt sets the minimum and maximum limits of the plot on the x axis. It requires a list of two numbers, where the first sets the left (minimum) limit and the second the right (maximum) limit. If one or both values are not provided, they are calculated automatically.\n"""
    x, y = _set_first_to_both(x, y)
    x, y = _set_list_to_both(x, y)
    par.xlim_plot = [x, y]

def ylim(x = None, y = None):
    """\nIt sets the minimum and maximum limits of the plot in the y axis. It requires a list of two numbers, where the first sets the lower (minimum) limit and the second the upper (maximum) limit. If one or both values are not provided, they are calculated automatically.\n"""
    x, y = _set_first_to_both(x, y)
    x, y = _set_list_to_both(x, y)
    par.ylim_plot = [x, y]
    
def xticks(x = None, y = None):
    """\nIt sets the data ticks on the x axis. The ticks should be provided as a list of values. If two lists are provided, the second is intended as the list of labels to be printed at the coordinates given by the first list. Here is an example:

\x1b[32mplt.scatter(data)
plt.xticks(xticks, xlabels)
plt.show()\x1b[0m

If no list is provided, the ticks are calculated automatically.\n"""
    x, y = _set_first_to_both(list(x), y)
    x, y = list(x), list(y)
    x = _set_var_if_none(x, [])
    y = _set_var_if_none(y, [])
    y = list(map(str, y))
    par.xticks, par.xlabels = x, y
    par.ticks[0] = len(x)

def yticks(x = None, y = None):
    """\nSimilar to the function xticks but relative to the y axis instead. Access its docstrings for further guidance.\n"""
    x, y = _set_first_to_both(list(x), y)
    x, y = list(x), list(y)
    x = _set_var_if_none(x, [])
    y = _set_var_if_none(y, [])
    y = list(map(str, y))
    par.yticks, par.ylabels = x, y
    par.ticks[1] = len(y)

##############################################
############    Show Function     ############
##############################################
def show():
    """\nIt prints the final figure on terminal.\n"""
    _size_max()

    _height_min()
    _height()

    _ylim_data()
    _ylim_plot()
    _yticks()
    
    _width_min()
    _width()
    
    _xlim_data()
    _xlim_plot()
    _xticks()

    _matrix()
    _grid()
    _add_data()
    _legend()

    _yaxis()
    _xaxis()
    
    _title()
    _axes_label()

    _canvas()
    _print_canvas()

##############################################
########    Show Called Functions     ########
##############################################
def _size_max():
    par.width_max, par.height_max = terminal_size()
    par.height_max -= 2

def _height_min():
    par.height_title = int(par.title != "")
    par.height_xaxis = int(par.axes[0] or par.frame)
    par.height_xticks = bool(par.ticks[0])
    par.height_labels = int(par.xlabel != "" or par.ylabel != "")
    #(par.xlabel != "" or par.ylabel != "")
    height_frame = int(par.frame)
    par.height_extra = par.height_title + par.height_xaxis + par.height_xticks + par.height_labels + height_frame
    par.height_min = 1 + par.height_extra

def _height():
    height = _set_var_if_none(par.height, par.height_max)
    height = abs(int(height))
    if height > par.height_max: # and not par.force_size[0]:
        height = par.height_max
    if height < par.height_min:
        height = par.height_min
    par.height = height
    par.rows = height - par.height_extra

def _ylim_data():
    par.ylim_data = _get_lim_data(par.y)

def _ylim_plot():
    par.ylim_plot[0] = _set_var_if_none(par.ylim_plot[0], par.ylim_data[0])
    par.ylim_plot[1] = _set_var_if_none(par.ylim_plot[1], par.ylim_data[1])
    par.dy = (par.ylim_plot[1] - par.ylim_plot[0]) / par.rows

def _yticks():
    if par.yticks == None and par.ticks[1]:
        y = par.ylim_plot
        y = _linspace(min(y), max(y), par.ticks[1])
        y = [int(el) if el == int(el) else el for el in y]
        par.yticks, par.ylabels = y, _get_labels(y)
    par.rticks = _get_matrix_data(par.yticks, par.ylim_plot, par.rows)

def _width_min():
    par.width_yaxis = int(par.axes[1] or par.frame)
    par.width_yticks = max(map(len, par.ylabels), default = 0) * bool(par.ticks[1])
    par.width_frame = int(par.frame)
    par.width_extra = par.width_yaxis + par.width_yticks + par.width_frame
    par.width_min = 1 + par.width_extra

def _width():
    width = _set_var_if_none(par.width, par.width_max)
    width = abs(int(width))
    if width > par.width_max:# and not par.force_size[0]:
        width = par.width_max
    if width < par.width_min:
        width = par.width_min
    par.width = width
    par.cols = width - par.width_extra

def _xlim_data():
    par.xlim_data = _get_lim_data(par.x)

def _xlim_plot():
    par.xlim_plot[0] = _set_var_if_none(par.xlim_plot[0], par.xlim_data[0])
    par.xlim_plot[1] = _set_var_if_none(par.xlim_plot[1], par.xlim_data[1])
    par.dx = (par.xlim_plot[1] - par.xlim_plot[0]) / par.cols

def _xticks():
    if par.xticks == None and par.ticks[0]:
        x = [par.xlim_plot[0], par.xlim_plot[1]]
        x = _linspace(min(x), max(x), par.ticks[0])
        x = [int(el) if el == int(el) else el for el in x]
        par.xticks, par.xlabels = x, _get_labels(x)
    par.cticks = _get_matrix_data(par.xticks, par.xlim_plot, par.cols)

def _matrix():
    space_marker = _add_color(" ", "none", par.canvas_color)
    par.matrix = [[space_marker for c in range(par.cols)] for r in range(par.rows)]

def _grid():
    grid_color = "iron"
    grid_color = par.ticks_color
    if par.grid[0]:
        for c in par.cticks:
            y = list(range(par.rows))
            x = [c] * par.rows
            marker = _add_color("│", grid_color, par.canvas_color)
            par.matrix = _update_matrix(par.matrix, x, y, marker)
    if par.grid[1]:
        for r in par.rticks:
            x = list(range(par.cols))
            y = [r] * par.cols
            marker = _add_color("─", grid_color, par.canvas_color)
            par.matrix = _update_matrix(par.matrix, x, y, marker)
            if par.grid[0]:
                x = par.cticks
                y = [r] * len(x)
                marker = _add_color("┼", grid_color, par.canvas_color)
                par.matrix = _update_matrix(par.matrix, x, y, marker)

def _add_data():
    for s in range(len(par.x)):
        point_marker, point_color = par.point_marker[s], par.point_color[s]
        line_marker, line_color = par.line_marker[s], par.line_color[s]
        x, y = par.x[s], par.y[s]
        x_point = _get_matrix_data(x, par.xlim_plot, par.cols)
        y_point = _get_matrix_data(y, par.ylim_plot, par.rows)
        x_line, y_line = [], []
        if line_marker != "":
            x_line, y_line = _get_line(x_point, y_point)
        if par.fill[s]:
            c0 = _get_matrix_data([0], par.ylim_plot, par.rows)[0]
            x_point, y_point = _fill_data(x_point, y_point, c0)
            x_line, y_line = _fill_data(x_line, y_line, c0)
        if line_marker != "":
            line_marker = _add_color(line_marker, line_color, par.canvas_color)
            par.matrix = _update_matrix(par.matrix, x_line, y_line, line_marker)
        if point_marker != "":
            point_marker = _add_color(point_marker, point_color, par.canvas_color)
            par.matrix = _update_matrix(par.matrix, x_point, y_point, point_marker)

def _legend():
    if (par.legend == [""] * len(par.legend)):
        return
    legend = par.legend
    l = len(legend)
    legend = [" " + legend[i] if legend[i] != "" else " signal " + str(i + 1) for i in range(l)]
    legend = [list(el) for el in legend]
    legend = [[_add_color(sub_el, par.ticks_color, par.canvas_color) for sub_el in el] for el in legend]
    markers = []
    space = _add_color(" ", "none", par.canvas_color)
    for i in range(l):
        point_marker = par.point_marker[i] if par.point_marker[i] != "" else par.line_marker[i]
        point_color = par.point_color[i] if par.point_marker[i] != "" else par.line_color[i]
        point_marker = _add_color(point_marker, point_color, par.canvas_color)
        line_marker = par.line_marker[i] if par.line_marker[i] != "" else par.point_marker[i]
        line_color = par.line_color[i] if par.line_marker[i] != "" else par.point_color[i]
        line_marker = _add_color(line_marker, line_color, par.canvas_color)
        marker = [line_marker] * 2 + [point_marker] + [line_marker] * 2
        markers += [marker]
    legend = [[space] + markers[i] + legend[i] +  [space] for i in range(l)]
    #legend = [[add_color(sub_el, "bold", "white") for sub_el in el] for el in legend]
    if len(legend) > par.rows:
        return
    for i in range(l):
        li = len(legend[i])
        if li > par.cols-1:
            return
        par.matrix[-(i+1)][0:li] = legend[i]

def _yaxis():
    l = par.width_yticks
    labels = [" " * l for r in range(par.rows)]
    for i in range(len(par.rticks)):
        r = par.rticks[i]
        if r in range(par.rows):
            labels[r] = str(par.ylabels[i])[:l]
    labels = [" " * (l - len(el)) + el for el in labels]
    labels = [list(el) for el in labels]
    labels = [[_add_color(sub_el, par.ticks_color, par.axes_color) for sub_el in el] for el in labels]
    #labels = [[_add_color(sub_el, "bold", "none") for sub_el in el] for el in labels]
    ytick = "┼" if par.grid[1] else "┤"
    axis = [ytick if r in par.rticks else "│" for r in range(par.rows)]
    axis = [list(el) for el in axis]
    ytick = "┤" if par.grid[1] else "│"
    right_axis = [ytick if r in par.rticks else "│" for r in range(par.rows)]
    right_axis = [list(el) for el in right_axis]
    if not par.grid[1]:
        right_axis = ["│" for r in range(par.rows)]
    axis = [[_add_color(sub_el, par.ticks_color, par.axes_color) for sub_el in el] for el in axis]
    right_axis = [[_add_color(sub_el, par.ticks_color, par.axes_color) for sub_el in el] for el in right_axis]
    for r in range(par.rows):
        if par.axes[1] or par.frame:
            par.matrix[r] = axis[r] + par.matrix[r]
        if par.ticks[1]:
            par.matrix[r] = labels[r] + par.matrix[r]
        if par.frame:
            par.matrix[r] = par.matrix[r] + right_axis[r]

def _xaxis():
    xtick = "┼" if par.grid[1] else "┬"
    xtick_upper = "┬" if par.grid[1] else "─"
    axis = [" "] * par.width_yticks + ["└"] * par.width_yaxis
    axis += ["─" for r in range(par.cols)] + ["┘"] * par.width_frame
    upper_axis = axis[:]
    upper_axis[par.width_yticks] = "┌"
    upper_axis[-1] =  "┐"
    labels_iniz = [" "] * par.width_yticks + [" "] * par.width_yaxis
    iniz_length = len(labels_iniz)
    labels = labels_iniz + [" "  for r in range(par.cols)] + [" "] * par.frame
    lc = len(par.cticks)
    #print(_remove_color(''.join(upper_axis)))
    #print(_remove_color(''.join(axis)))
    for i in range(lc):
        c = par.cticks[i] + iniz_length
        new_label = str(par.xlabels[i])
        l = len(new_label)
        pc = c - int((l - 1) / 2)
        pp = max([r for r in range(par.width) if labels[r] != " "], default = -2)
        pf = par.width - l
        pl = min(pc, pf)
        pl = max(pl, pp + 2)
        pr = pl + l
        if pr <= c + l and pr <= par.width and c < par.width:
            labels[pl : pr] = list(new_label)
            axis[c] = xtick
            upper_axis[c] = xtick_upper
            if c == par.width-1:
                axis[c] = "┤" if par.frame else "┬"
                upper_axis[c] = "┐"
                print(c)
    axis = [_add_color(el, par.ticks_color, par.axes_color) for el in axis]
    upper_axis = [_add_color(el, par.ticks_color, par.axes_color) for el in upper_axis]
    labels = [_add_color(el, par.ticks_color, par.axes_color) for el in labels]
    #labels = [_add_color(el, "bold", "none") for el in labels]
    if par.axes[0] or par.frame:
        par.matrix.insert(0, axis) 
    if par.ticks[0]:
        par.matrix.insert(0, labels)
    if par.frame:
        par.matrix.insert(len(par.matrix), upper_axis)

def _title():
    if par.title == "":
        return
    title = par.title[:par.cols]
    space1 = " " * int(par.width_extra + (par.cols - len(title)) /2)
    space2 = " " * (par.width - len(title + space1))
    title = space1 + title + space2
    title = list(title)
    title = [_add_color(el, par.ticks_color, par.axes_color) for el in title]
    #title = [_add_color(el, "bold") for el in title]
    par.matrix += [title]

def _axes_label():
    if par.xlabel == "" and par.ylabel == "":
        return
    ylabel = "[y] " + par.ylabel + " "
    xlabel = par.xlabel + " [x]"
    if len(xlabel) + len(ylabel) > par.width:
        return
    space = " " * (par.width - len(xlabel) - len(ylabel))
    label = ylabel + space + xlabel
    label = list(label)
    label = [_add_color(el, par.ticks_color, par.axes_color) for el in label]
    #label = [add_color(el, "bold") for el in label]
    par.matrix = [label] + par.matrix

def _canvas():
    canvas = ''
    for r in range(len(par.matrix) -1, -1, -1):
        canvas += "".join(par.matrix[r]) + '\n'
    par.canvas = canvas
  
def _print_canvas():
    canvas = par.canvas
    if par.nocolor:
        canvas = _remove_color(canvas)
        #print("color removed")
    _write(canvas)

##############################################
##########    Utility Functions    ###########
##############################################
def _set_first_to_both(x = None, y = None):# by setting one parameter to a value, both are set
    if x != None and y == None:
        y = x
    return [x, y]

def _set_list_to_both(x = None, y = None): # by setting a parameter to a list, both are set
    if type(x) == list:
        x, y = x[0], x[1]
    return [x, y]

def _set_var_if_none(x = None, x_none = None): # set a parameter when none is provided. 
    if x == None:
        x = x_none
    elif x_none != None:
        x = type(x_none)(x)
    return x

def _get_lim_data(data):
    m = min([min(el, default = 0) for el in data])
    M = max([max(el, default = 0) for el in data])
    return [m, M]

def _linspace(lower, upper, length):
    if length == 1:
        return [0.5*(lower+upper)]
    return [lower + x * (upper - lower) / (length - 1) for x in range(length - 1)] + [upper]

def _get_labels(ticks):
    if len(ticks) == 1:
        l = len(str(ticks[0]))
    else:
        l = max([_distinguish(ticks[i], ticks[i+1]) for i in range(len(ticks) - 1)])
    labels = [_round_to_character(el, l) for el in ticks]
    labels = [str(el) for el in labels]
    return labels

def _distinguish(a, b):
    d = abs(a-b)
    d = str(d)
    r = [r for r in range(len(d)) if d[r] != "." and d[r] != "0"]
    if r == []:
        r = 0
    else:
        r = r[0]
    ca, cb = len(str(int(a))), len(str(int(b)))
    if a != int(a):
        ca += 2
    if b != int(b):
        cb += 2
    return max(ca, cb, r + 1)

def _round_to_character(n, c):
    int_len = len(str(int(n)))
    d = c - int_len - 1
    if d < 0:
        d = 0
    return round(n, d)

def _get_matrix_data(data, plot_lim, bins):
    if data == None:
        data = []
    dz = (plot_lim[1] - plot_lim[0]) / bins
    data = [int((el - plot_lim[0]) / dz) if el != plot_lim[1] else bins - 1 for el in data]
    #data = [el for el in data if el in range(bins)]
    return data

_fullground_color = {'none': 0, 'black': 30, 'iron': 90, 'gray': 2, 'cloud': 37, 'white': 97, 'red': 31, 'tomato': 91, 'basil': 32, 'green': 92, 'yellow': 93, 'gold': 33, 'blue': 34, 'indigo': 94, 'teal': 36, 'artic': 96, 'lilac': 95, 'violet': 35, 'italic': 3, 'bold': 1, 'flash': 5}
_background_color = {'none': 28, 'black': 40, 'iron': 100, 'cloud': 47, 'white': 107, 'red': 41, 'tomato': 101, 'basil': 42, 'green': 102, 'yellow': 103, 'gold': 43, 'blue': 44, 'indigo': 104, 'teal': 46, 'artic': 106, 'lilac': 105, 'violet': 45}
_color_sequence = ["blue", "tomato", "basil", "gold", "lilac", "black", "artic", "red", "green", "yellow", "violet"]

def _apply_color(text, code):
    if code == 0 or code == 28:
        return text
    return '\033[' + str(code) + 'm' + text + '\033[0m'

def _add_color(text = "", color = "none", background = "none"):
    color = _fullground_color[color]
    background = _background_color[background]
    if color != "none":
        text = _apply_color(text, color)
    if background != "none":
        text = _apply_color(text, background)
    return text

def _get_line(x, y): 
    x_line = []
    y_line = []
    for n in range(len(x) - 1):
        Dy, Dx = y[n + 1] - y[n], x[n + 1] - x[n]
        l = x[n + 1] - x[n]
        x_line_n = [x[n] + i           for i in range(l)]
        y_line_n = [int(y[n] + i * Dy / Dx) for i in range(l)]
        x_line.extend(x_line_n)
        y_line.extend(y_line_n)
    x_line += [x[-1]]
    y_line += [y[-1]]
    return x_line, y_line

def _update_matrix(matrix, x, y, marker):
    cols, rows = len(matrix[0]), len(matrix)
    for i in range(len(x)):
        c, r = x[i], y[i] 
        if 0 <= r < rows and 0 <= c < cols:
            matrix[r][c] = marker
    return matrix

def _fill_data(x, y, y0):
    y_new = y
    x_new = x
    for i in range(len(y)):
        yi = y[i]
        y_temp = range(min(y0, yi), max(y0, yi))
        y_new += y_temp
        x_new += [x[i]] * len(y_temp)
    return [x, y]

def _arange(start, stop, step = 1):
    res = []
    i = start
    while i < stop:
        res.append(i)
        i = i + step
    return res

def _write(string):
    _sys.stdout.write(string)

def _check_path(path):
    home = _os.path.expanduser("~") 
    if path == None:
        path = _os.path.join(home, "plot.txt")
    basedir = _os.path.dirname(path)
    if _os.path.exists(basedir):
        return path
    else:
        print("warning: parent directory doesn't exists.")
        path = _os.path.join(home, _os.path.basename(path))
    return path

def _remove_color(string):
    for c in list(_fullground_color.values()) + list(_background_color.values()):
        string = string.replace('\x1b[' + str(c) + 'm', '')
    return string

##############################################
##########    Basic Functions    #############
##############################################
def scatter(*args,
        #width = None,
        #height = None,
        #force_size = None,

        #title = None,
        #xlabel = None,
        #ylabel = None,
        label = None,

        #axes = None,
        #ticks = None,
        #grid = None,
        #frame = None,

        point_marker = None,
        line_marker = "",

        #axes_color = None,
        #ticks_color = None,
        #canvas_color = None,
        point_color = None,
        line_color = "none",

        #xlim = None,
        #ylim = None,
            
        fill = None):
    """\nIt creates a scatter plot of coordinates given by the x and y lists. Optionally, a single y list could be provided. Here is a basic example:

\x1b[32mimport plotext as plt
plt.scatter(x, y)
plt.show()\x1b[0m

Multiple data sets could be plotted using consecutive scatter functions:

\x1b[32mplt.scatter(x1, y1)
plt.scatter(y2)
plt.show()\x1b[0m

Here are the parameters of the scatter function: 

\x1b[33mlabel\x1b[0m
It sets the label of the current data set, which will appear in the legend at the top left of the plot. The default value is an empty string. If all labels are an empty string no legend is printed. Alternatively use legend(labels) to set all labels (as a list of strings) after the scatter function. 

\x1b[33mpoint_marker\x1b[0m 
It sets the marker used to identify each data point plotted. It should be a single character and it could be a different value for each data set. If an empty string is provided (or the space character), no data point is plotted. The default value is '•'. An integer value will set the marker according to the marker codes accessible using plt.markers().

\x1b[33mline_marker\x1b[0m 
It sets the marker used to identify the lines between two consecutive data points. It should be a single character and it could be a different value for each data set. If an empty or the space string is provided, as by default, no lines are plotted. An integer value will set the marker according to the marker codes accessible using plt.markers().

\x1b[33mpoint_color\x1b[0m
It sets the color of the data points. Use the function plt.colors() to find the available full-ground color codes. 

\x1b[33mline_color\x1b[0m
It sets the color of the lines, if plotted. Use the function plt.colors() to find the available full-ground color codes.\n"""
    _draw(*args,
          #width = width,
          #height = height,
          #force_size = force_size,
          
          #title = title,
          #xlabel = xlabel,
          #ylabel = ylabel,
          label = label,
          
          #axes = axes,
          #ticks = ticks,
          #grid = grid,
          #frame = frame,
          
          point_marker = point_marker,
          line_marker = line_marker,
          
          #axes_color = axes_color,  
          #ticks_color = ticks_color,  
          #canvas_color = canvas_color,
          point_color = point_color,
          line_color = line_color,
          
          #xlim = xlim,
          #ylim = ylim,
          
          fill = fill)

def plot(*args,
        #width = None,
        #height = None,
        #force_size = None,

        #title = None,
        #xlabel = None,
        #ylabel = None,
        label = None,
         
        #axes = None,
        #ticks = None,
        #grid = None,
        frame = None,

        point_marker = "",
        line_marker = None,

        #axes_color = None,
        #ticks_color = None,
        #canvas_color = None,
        point_color = "none",
        line_color = None,

        #xlim = None,
        #ylim = None,

        fill = None):
    """\nIt plots y versus x as lines and it is equivalent to the scatter function with the point_marker set to the empty string and the line_marker set to '•'. This means that no data points will be plotted, and the lines between consecutive points will be plotted instead. Here is a basic example: 

\x1b[32mimport plotext as plt
plt.plot(x, y)
plt.show()\x1b[0m

Access the scatter function docstring for further documentation.\n"""
    _draw(*args,
          #width = width,
          #height = height,
          #force_size = force_size,
          
          #title = title,
          #xlabel = xlabel,
          #ylabel = ylabel,
          label = label,
          
          #axes = axes,
          #ticks = ticks,
          #grid = grid,
          frame = frame,
          
          point_marker = point_marker,
          line_marker = line_marker,
          
          #axes_color = axes_color,
          #ticks_color = ticks_color,
          #canvas_color = canvas_color,
          point_color = point_color,
          line_color = line_color,
          
          #xlim = xlim,
          #ylim = ylim,
          
          fill = fill)

def clear_terminal():
    """\nIt clears the terminal and it is generally useful when plotting a continuous stream of data. The function clt() is equivalent.\n"""
    if par.nocolor:
        print("\n" * 100)
    else:
        _write('\033c')

clt = clear_terminal

def clear_plot():
    """\nIt resets all the plot parameters, including all x and y coordinates. The function clp() is equivalent.\n"""
    par.__init__()

clp = clear_plot

def sleep(time):
    """\nIt adds a sleeping time to the computation and it is useful when continuously plotting a stream of data, in order to decrease a possible screen flickering. An input of, for example, 0.01 would add approximately 0.01 secs to the computation. Manually tweak this value to reduce the flickering.\n"""
    [i for i in range(int(time * 15269989))]

def terminal_size():
    """\nIt returns the terminal size\n"""
    if par.nocolor:
        return [100, 45]
    else:
        return list(_os.get_terminal_size())

def savefig(path = None):
    """\nIt saves the plot canvas (without colors) as a text file, at the address provided in input.\n"""
    path = _check_path(path)
    with open(path , "w+", encoding = "utf-8") as file:
        file.write(_remove_color(par.canvas))
    print("plot saved as " + path)

def colors():
    """\nIt shows the available full-ground and background color codes.\n"""
    key = list(_fullground_color.keys())
    title = "fullground\tbackground"
    #title = _add_color(title, "none", "black")
    title = _add_color(title, "bold")
    #title = _apply_color(title, 4)
    out = "\n" + title
    for i in range(len(key)):
        full_color = ""
        if key[i] in _fullground_color.keys():
            back = "none" if key[i] not in ["black"] else "cloud"
            full_color = _add_color(key[i]+ "\t\t" , key[i], back)
        back_color = _add_color("-", "italic")
        if key[i] in _background_color.keys():
            full = "black" if key[i] not in ["none", "black", "iron"] else "white"
            back_color = _add_color(key[i], full, key[i])
        out += "\n" + full_color + back_color
    out += "\n\n" + "Fullground colors can be set to point_color and line_color or given as input to plt.ticks_color()."
    out += "\n" + "Background colors can be given as input to plt.canvas_color() and plt.axes_color()."
    if par.nocolor:
        out = _remove_color(out)
    print(out)
     
_marker = '•*~¤◗©™¶☺♥'
def markers():
    """\nIt shows the optional integer codes to quickly access special point or line markers.\n"""
    print()
    marker = list(_marker)
    title = "code\tmarker"
    #title = _add_color(title, "none", "black")
    title = _add_color(title, "bold")
    #title = _apply_color(title, 4)
    print(title)
    for i in range(len(marker)):
        print(str(i) + '\t' + marker[i])
    print("\nThese codes can be set to point_marker and line_marker.")
    
def version():
    """\nIt returns the version of the current installed plotext package.\n"""
    init_path = "__init__.py"
    here = _os.path.abspath(_os.path.dirname(__file__))
    with open(_os.path.join(here, init_path), 'r') as fp:
        lines = fp.read()
    for line in lines.splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            version = line.split(delim)[1]
            print()
            print("plotext version:", version)
            return version
    else:
        print("Unable to find version string.")

def parameters():
    """\nIt returns all the internal plot parameters.\n"""
    dic = par.__dict__
    key = list(dic.keys())
    value = list(dic.values())
    print()
    for i in range(len(key)):
        if key[i] in ["canvas", "matrix", "x", "y"]:
            continue
        print(key[i] + "\t\t" + str(value[i]))

def docstrings():
    """\nIt prints all the available docstrings\n"""    
    functions = [width, height, figsize, axes, ticks, scatter, plot, xticks, yticks, show, clear_terminal, clear_plot, sleep, savefig, colors, version]
    functions = [width, height, figsize, axes, ticks, grid, frame, axes_color, canvas_color, ticks_color, nocolor, title, xlabel, ylabel, legend, xlim, ylim, xticks, yticks, show, scatter, plot, clt, clp, sleep, terminal_size, savefig, colors, markers, version, parameters, docstrings]
    for fun in functions:
        name = _add_color(_add_color(fun.__name__, "bold"), "indigo")
        if par.nocolor:
            fun.__doc__ = _remove_color(fun.__doc__)
            name = _remove_color(name)
        print()
        print(name)
        print(fun.__doc__)

if __name__ == "__main__":
    import plot as plt
    #plt.docstrings()
    pass
