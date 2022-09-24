# /usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################
###########    Initialization    #############
##############################################
import sys as _sys
import os as _os
_sys.path.append(_os.path.abspath(_os.path.dirname(__file__)))
import utility as ut

class _variables():
    def __init__(self):
        self.x = []
        self.y = []

        self.plot_xmin = None
        self.plot_xmax = None
        self.plot_ymin = None
        self.plot_ymax = None

        self.force_size = [False, False]
        self.cols = None
        self.rows = None

        self.point_marker = []
        self.line_marker = []

        self.canvas_color = []
        self.point_color = []
        self.line_color = []

        self.axes = [True, True]
        self.axes_color = []
        self.ticks_number = [5, 5]
        self.ticks_length = [4, 4]

        self.title = ""
        self.xlabel = ""
        self.ylabel = ""
        
        self.label = []

        # Constants
        self.default_marker = "•"
        self.empty_marker = ""

        self.xticks = None
        self.yticks = None
        self.abx = [1, 0]
        self.aby = [1, 0]
        
        self.grid = [[]]
        self.canvas = ""
        

var = _variables()

def _set_platform():
    var.platform = "linux"
    var.nocolor = False
    if "win" in _sys.platform:
        var.platform = "windows"
        import subprocess
        subprocess.call('', shell = True)       
    if ('idlelib.run' in _sys.modules):
        var.nocolor = True

_set_platform()
if var.platform == "windows":
    from shutil import get_terminal_size as get_terminal_size_windows


##############################################
#########    Scatter Function    #############
##############################################
def scatter(*args, **kwargs):
    _set_data(*args)
    set_xlim(kwargs.get("xlim"))
    set_ylim(kwargs.get("ylim"))

    set_force_size(kwargs.get("force_size"))
    set_cols(kwargs.get("cols"))
    set_rows(kwargs.get("rows"))
    
    _set_point_marker(kwargs.get("point_marker"))
    _set_line_marker(kwargs.get("line_marker"))

    set_canvas_color(kwargs.get("canvas_color"))
    _set_point_color(kwargs.get("point_color"))
    _set_line_color(kwargs.get("line_color"))

    set_axes(kwargs.get("axes"))
    set_axes_color(kwargs.get("axes_color"))

    set_ticks_number(kwargs.get("ticks_number"))
    set_ticks_length(kwargs.get("ticks_length"))

    set_title(kwargs.get("title"))
    set_xlabel(kwargs.get("xlabel"))
    set_ylabel(kwargs.get("ylabel"))
    
    _set_label(kwargs.get("label"))
    
    
##############################################
######    Scatter Called Functions     #######
##############################################
def _set_data(*args):
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
    var.x.append(x)
    var.y.append(y)



def set_xlim(*plot_xlim):
    plot_xmin, plot_xmax = ut.set_vars(plot_xlim)
    if plot_xmin != None:
        var.plot_xmin = plot_xmin
    if plot_xmax != None:
        var.plot_xmax = plot_xmax
    var.plot_xlim = [var.plot_xmin, var.plot_xmax]

def set_ylim(*plot_ylim):
    plot_ymin, plot_ymax = ut.set_vars(plot_ylim)
    if plot_ymin != None:
        var.plot_ymin = plot_ymin
    if plot_ymax != None:
        var.plot_ymax = plot_ymax
    var.plot_ylim = [var.plot_ymin, var.plot_ymax]

def set_force_size(*force_size):
    force_xsize, force_ysize = ut.set_vars(force_size)
    if force_xsize != None:
        var.force_size[0] = bool(force_xsize)
    if force_ysize != None:
        var.force_size[1] = bool(force_ysize)

def set_cols(cols = None):
    var.cols = cols

def set_rows(rows = None):
    var.rows = rows
    
def _set_point_marker(point_marker = None):
    if point_marker == None:
        point_marker = var.default_marker
    var.point_marker.append(point_marker[0:1])

def _set_line_marker(line_marker = None):
    if line_marker == None:
        line_marker = var.empty_marker
    var.line_marker.append(line_marker[0:1])

def set_canvas_color(canvas_color = None):
    if canvas_color == None:
        canvas_color = "norm"
    var.canvas_color = canvas_color

def _set_point_color(point_color = None):
    if point_color == None:
        point_color = "norm"
    var.point_color.append(point_color)

def _set_line_color(line_color = None):
    if line_color == None:
        line_color = "norm"
    var.line_color.append(line_color)

def set_axes(*axes):
    xaxis, yaxis = ut.set_vars(axes)
    if xaxis != None:
        var.axes[0] = bool(xaxis)
    if yaxis != None:
        var.axes[1] = bool(yaxis)

def set_axes_color(*axes_color):
    axes_color = ut.set_vars(axes_color, "norm")
    var.axes_color = axes_color

def set_ticks_number(*ticks_number):
    xticks_number, yticks_number = ut.set_vars(ticks_number)
    if xticks_number != None:
        var.ticks_number[0] = xticks_number
    if yticks_number != None:
        var.ticks_number[1] = yticks_number

def set_ticks_length(*ticks_length):
    xticks_length, yticks_length = ut.set_vars(ticks_length)
    if xticks_length != None:
        var.ticks_length[0] = xticks_length
    if yticks_length != None:
        var.ticks_length[1] = yticks_length

def set_title(label = None):
    if label == None:
        label = ""
    var.title = label

def set_xlabel(label = None):
    if label == None:
        label = ""
    var.xlabel = label

def set_ylabel(label = None):
    if label == None:
        label = ""
    var.ylabel = label

def _set_label(label = None):
    if label == None:
        label = ""
    var.label.append(label)


##############################################
########    Other Set Functions     ##########
##############################################
def set_canvas_size(*size):
    cols, rows = ut.set_vars(size)
    set_cols(cols)
    set_rows(rows)

def set_legend(legend = None):
    if legend == None:
        legend = [None] * len(var.legend)
    var.label = legend

##############################################
############    Show Function     ############
##############################################
def show():
    _set_terminal_size()
    _set_cols_max()
    _set_rows_max()
    _set_cols()
    _set_rows()

    _set_data_lim()
    _set_xlim()
    _set_ylim()

    _set_grid()

    _get_yticks()
    _get_xticks()
    _add_yaxis()
    _add_xaxis()

    _set_canvas()
    
    _add_title()
    _add_axes_labels()
    _add_legend()
    _add_equations()

    _print_canvas()
    #clear_plot()
    
##############################################
########    Show Called Functions     ########
##############################################
def _set_terminal_size():
    var.cols_term, var.rows_term = get_terminal_size()
    
def _set_cols_max():
     var.cols_yaxis = int(var.axes[1])
     var.cols_yticks = var.ticks_length[1] * bool(var.ticks_number[1])
     var.cols_yticks += bool(var.ticks_length[1] *var.ticks_number[1])
     var.cols_max = var.cols_term - var.cols_yaxis - var.cols_yticks
    
def _set_rows_max():
    var.rows_xaxis = int(var.axes[0])
    var.rows_xticks = bool(var.ticks_number[0] * var.ticks_length[0])
    var.rows_equations = 1
    var.rows_legend = not (var.label == [""] * len(var.label))
    var.rows_axes_labels = not (var.xlabel == "")
    var.rows_title = not (var.title == "")
    var.rows_max = var.rows_term - var.rows_xaxis - var.rows_xticks - var.rows_equations - var.rows_legend - var.rows_axes_labels - var.rows_title - 1

def _set_cols():
    cols = var.cols
    if cols == None:
        cols = var.cols_max
    cols = abs(int(cols))
    if cols > var.cols_max and not var.force_size[0]:
        cols = var.cols_max
    var.cols = cols
    var.cols_plot = var.cols + var.cols_yaxis + var.cols_yticks
    
def _set_rows():
    rows = var.rows
    if rows == None:
        rows = var.rows_max
    rows = abs(int(rows))
    if rows > var.rows_max and not var.force_size[1]:
        rows = var.rows_max
    var.rows = rows
    var.rows_plot = var.rows + var.rows_xaxis + var.rows_xticks + var.rows_equations + var.rows_legend + var.rows_axes_labels

def _set_data_lim():
    var.xmin = min(map(min, var.x))
    var.xmax = max(map(max, var.x))
    var.xlim = [var.xmin, var.xmax]
    
    var.ymin = min(map(min, var.y))
    var.ymax = max(map(max, var.y))
    var.ylim = [var.ymin, var.ymax]

def _set_xlim(xlim = None):
    var.plot_xlim = ut.set_lim(var.xlim, var.plot_xlim, var.cols)
    var.dx = (var.plot_xlim[1] - var.plot_xlim[0]) / var.cols

def _set_ylim(ylim = None):
    var.plot_ylim = ut.set_lim(var.ylim, var.plot_ylim, var.rows)
    var.dy =  (var.plot_ylim[1] - var.plot_ylim[0]) / var.rows
    
def _set_grid():
    space = ut.add_color(" ", ["norm", var.canvas_color])
    var.grid = [[space for c in range(var.cols)] for r in range(var.rows)]
    for s in range(len(var.x)):
        
        if var.line_marker[s] != var.empty_marker:
            x, y = ut.get_line(var.x[s], var.y[s], var.dx)
            marker = ut.add_color(var.line_marker[s], [var.line_color[s], var.canvas_color])
            x = ut.discretization(x, var.plot_xlim, var.cols)
            y = ut.discretization(y, var.plot_ylim, var.rows)
            var.grid = ut.update_grid(var.grid, x, y, marker)
            
        if var.point_marker[s] != var.empty_marker:
            x, y = var.x[s], var.y[s]
            marker = ut.add_color(var.point_marker[s], [var.point_color[s], var.canvas_color])
            x = ut.discretization(x, var.plot_xlim, var.cols)
            y = ut.discretization(y, var.plot_ylim, var.rows)
            var.grid = ut.update_grid(var.grid, x, y, marker)

def _get_xticks():
    if var.xticks == None:
        inp = var.ticks_number[0], var.ticks_length[0], var.plot_xlim, var.dx
        ticks, labels, ab =ut.get_ticks(*inp)
        set_xticks(ticks, labels)
        var.abx = ab

def _get_yticks():
    if var.yticks == None:
        inp = [var.ticks_number[1], var.ticks_length[1], var.plot_ylim, var.dy]
        ticks, labels, ab =ut.get_ticks(*inp)
        set_yticks(ticks, labels)
        var.aby = ab

def set_xticks(ticks = None, labels = None):
    if ticks == None:
        ticks = []
    if labels == None:
        labels = ticks
    var.xticks, var.xlabels = ticks, labels

def set_yticks(ticks = None, labels = None):
    if ticks == None:
        ticks = []
    if  labels == None:
        labels = ticks
    var.yticks, var.ylabels = ticks, labels

def _add_yaxis():
    axis = ["│" for r in range(var.rows)]
    l = var.ticks_length[1]
    ticks = [" " * (l + 1) for r in range(var.rows)]
    rticks = ut.discretization(var.yticks, var.plot_ylim, var.rows)

    for i in range(len(rticks)):
        r = rticks[i]
        if 0 <= r < var.rows and var.ylabels != []:
            axis[r] = "├"
            ticks[r] = str(var.ylabels[i])[:l]
            ticks[r] = " " + ticks[r] + " " * (l - len(ticks[r]))

    axis = [ut.add_color(el, var.axes_color) for el in axis]
    ticks = [ut.add_color(el, var.axes_color) for el in ticks]

    for r in range(var.rows):
        if var.axes[1]:
            var.grid[r].append(axis[r]) 
        if bool(var.ticks_length[1] * var.ticks_number[1]):
            var.grid[r].append(ticks[r])
            
def _add_xaxis():
    axis = ["─" for r in range(var.cols)]
    axis += ["┘"]
    axis += [" "] * (var.cols_plot - len(axis))
    
    l = var.ticks_length[0]
    labels = [str(el)[:l] for el in var.xlabels]
    labels = [el + " " * (l + 1 - len(el)) for el in labels]
    labels = [list(el) for el in labels]
    ticks = [" " for r in range(var.cols_plot)]
    cticks = ut.discretization(var.xticks, var.plot_xlim, var.cols)
    
    for i in range(len(cticks)):
        c = cticks[i]
        if c <= var.cols and c + l + 1 <= var.cols_plot and ticks[c - 1] == " ":
            ticks[c:c+l+1] = labels[i]
            if c < var.cols:
                axis[c] = "┬"
            if c == var.cols:
               axis[c] = "┤"

    axis = [ut.add_color(el, var.axes_color) for el in axis]
    ticks = [ut.add_color(el, var.axes_color) for el in ticks]

    if var.axes[0]:
        var.grid.insert(0, axis) 
    if bool(var.ticks_length[0] * var.ticks_number[0]):
        var.grid.insert(0, ticks)

def _set_canvas():
    canvas = ''
    for r in range(len(var.grid) -1, -1, -1):
        canvas += "".join(var.grid[r]) + '\n'
    var.canvas = canvas

def _add_equations():
    label = ["x", "y"]
    ab = [var.abx, var.aby]
    eq = []
    for i in  range(2):
        eq.append(ut.get_equation(label[i], *ab[i], 7))
    eq = ut.get_opposite_labels(eq, var.cols_plot, var.axes_color)
    var.canvas = var.canvas + eq

def _add_title():
    if var.rows_title == 1:
        label = ut.get_centered_label(var.title, var.cols_plot, var.axes_color)
        var.canvas = ''.join(label) + '\n' + var.canvas 

def _add_axes_labels():
    labels = [var.xlabel, var.ylabel]
    labels = ut.get_opposite_labels(labels, var.cols_plot, var.axes_color)
    var.canvas = var.canvas + labels

def _add_legend():
    if var.rows_legend == 1:
        legend = "legend: "
        legend_string_length = len(legend)
        axes_color = var.axes_color
        canvas_color = var.canvas_color
        legend = ut.add_color(legend, axes_color)
        sep = 4
        legend_length = len(var.label) 
        for i in range(legend_length):
            label = var.label[i]
            if label == "":
                label = "signal" + str(i + 1)
            label_length = len(label)
            label_color = var.line_color[i]
            if var.line_marker[i] == "":
                label_color = var.point_color[i]
            label_color = [label_color, canvas_color]
            label = ut.add_color(label, label_color)
            legend_string_length += label_length
            if i != legend_length - 1:
                legend_string_length += sep
                label += ut.add_color(" " * sep, axes_color)
            legend += label
        space = " " * (var.cols_plot - legend_string_length)
        space = ut.add_color(space, axes_color)
        legend += space
        var.canvas = var.canvas + legend + '\n'

def _get_canvas():
    return var.canvas
    
def _print_canvas():
    canvas = _get_canvas()
    if var.nocolor:
        canvas = ut.remove_color(canvas)
        print("color removed")
    ut.print(canvas)
    
##############################################
##########    Basic Function    ##############
##############################################

def plot(*args,
         xlim = None,
         ylim = None,
         force_size = None,
         cols = None,
         rows = None,
         point_marker = var.empty_marker,
         line_marker = var.default_marker,
         canvas_color = None,
         point_color = None,
         line_color = None,
         axes = None,
         axes_color = None,
         ticks_number = None,
         ticks_length = None,
         title = None,
         xlabel = None,
         ylabel = None,
         label = None):
    scatter(*args,
            xlim = xlim,
            ylim = ylim,
            force_size = force_size,
            cols = cols,
            rows = rows,
            point_marker = point_marker,
            line_marker = line_marker,
            canvas_color = canvas_color,
            point_color = point_color,
            line_color = line_color,
            axes = axes,
            axes_color = axes_color,  
            ticks_number = ticks_number,
            ticks_length = ticks_length,
            title = title,
            xlabel = xlabel,
            ylabel = ylabel,
            label = label)

def clear_terminal():
    ut.print('\033c')
    
def clear_plot():
    var.__init__()

def sleep(time):
    [i for i in range(int(time * 15269989))]
       
def get_terminal_size():
    if var.platform == "windows":
        return get_terminal_size_windows()
    elif var.nocolor:
        return [185, 45]
    else:
        return list(_os.get_terminal_size())
    
def savefig(path):
    path = ut.check_path(path)
    with open(path , "w+", encoding = "utf-8") as file:
        file.write(ut.remove_color(_get_canvas()))
    ut.print("plot saved as " + path)
    
def get_colors():
    fg_colors = [ut.add_color(fg_c, [fg_c, "norm"]) for fg_c in ut.fg_colors]
    ut.print("\nFullground colors: " + ", ".join(fg_colors))
    bg_colors = [ut.add_color(bg_c, ["norm", bg_c]) for bg_c in ut.bg_colors]
    ut.print("\nBackground colors: " + ", ".join(bg_colors) + '\n')
    
def get_version():
    init_path = "__init__.py"
    here = _os.path.abspath(_os.path.dirname(__file__))
    with open(_os.path.join(here, init_path), 'r') as fp:
        lines = fp.read()
    for line in lines.splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            version = line.split(delim)[1]
            print("plotext version:", version)
            return version
    else:
        print("Unable to find version string.")

        
##############################################
############     Docstrings     ##############
##############################################
scatter.__doc__ = """
It creates a scatter plot of coordinates given by the x and y lists. Optionally, a single y list could be provided. Here is a basic example:

   \x1b[92mimport plotext as plt\x1b[0m
   \x1b[92mplt.scatter(x, y)\x1b[0m
   \x1b[92mplt.show()\x1b[0m

Multiple data sets could be plotted using consecutive scatter functions. Here is an example:

   \x1b[92mplt.scatter(x1, y1)\x1b[0m
   \x1b[92mplt.scatter(y2)\x1b[0m
   \x1b[92mplt.show()\x1b[0m

Here are all the parameters of the scatter function: 

\x1b[94mxlim\x1b[0m
It sets the minimum and maximum limits of the plot in the x axis. It requires a list of two numbers, where the first sets the left (minimum) limit and the second the right (maximum) limit. If one or both values are not provided, they are calculated automatically. Alternatively use set_xlim(xlim) after the scatter function. 

\x1b[94mylim\x1b[0m
It sets the minimum and maximum limits of the plot in the y axis. It requires a list of two numbers, where the first sets the lower (minimum) limit and the second the upper (maximum) limit. If one or both values are not provided, they are calculated automatically. Alternatively use set_ylim(ylim) after the scatter function. 

\x1b[94mcols\x1b[0m
It sets the number of columns of the plot. By default, it is the highest value allowed by the terminal size. Alternatively use set_cols(cols) or set_canvas_size(cols, rows) after the scatter function.

\x1b[94mrows\x1b[0m
It sets the number of rows of the plot. By default, it is the highest value allowed by the terminal size. Alternatively use set_rows(rows) or set_canvas_size(cols, rows) after the scatter function.

\x1b[94mforce_size\x1b[0m
By default, the plot dimensions are limited by the terminal size. Set force_size to True in order to allow bigger plots. Alternatively use set_force_size(True) after the scatter function (but before the functions set_cols and set_rows, if present).
Note: plots bigger then the terminal size may not be readable. 

\x1b[94mpoint_marker\x1b[0m 
It sets the marker used to identify each data point plotted. It should be a single character and it could be a different value for each data set. If an empty string is provided, no data point is plotted. The default value is '•'. This parameter can only be set internally, because it is associated to the current data set plotted. 

\x1b[94mline_marker\x1b[0m 
It sets the marker used to identify the lines between two consecutive data points. It should be a single character and it could be a different value for each data set. If an empty string is provided (as by default), no lines are plotted. This parameter can only be set internally, because it is associated to the current data set plotted.

\x1b[94mcanvas_color\x1b[0m
It sets the canvas background color, without affecting the axes color. Alternatively use set_canvas_color(color) after the scatter function. Use get_colors() to find the available color codes. The default value is 'norm'.

\x1b[94mpoint_color\x1b[0m
It sets the color of the data points. Use get_colors() to find the available color codes. The default value is 'norm'. This parameter can only be set internally, because it is associated to the current data set plotted.

\x1b[94mline_color\x1b[0m
It sets the color of the lines, if plotted. Use get_colors() to find the available color codes. The default value is 'norm'. This parameter can only be set internally, because it is associated to the current data set plotted.

\x1b[94maxes\x1b[0m
When set to True (as by default), the x and y axes are added to the plot. A list of two Booleans will set the x and y axis independently (eg: axes = [True, False]). Alternatively, use set_axes(axes) after the scatter function.  

\x1b[94maxes_color\x1b[0m
It sets the axes color, without affecting the canvas. The same color is applied to the axes ticks, labels, equations, legend and title, if present. Use get_colors() to find the available color codes. The default value is 'norm'. If a list of two colors is provided, the second is interpreted as a background color. Alternatively use set_axes_color(color) after the scatter function. 

\x1b[94mticks_number\x1b[0m
It sets the number of data ticks printed on each axis. If a list of two values is provided, the number of ticks for each axis is set independently (eg: ticks_number = [5, 6]). If set to 0, no ticks are printed. The default value is 5. Alternatively use set_ticks_number(num) after the scatter function.
Note: you could also directly provide all ticks coordinates and labels for each axis using the functions set_xticks and set_yticks. Access their docstrings for further guidance. In this case the value of ticks_number would not affect what is printed. 

\x1b[94mticks_length\x1b[0m
It sets the maximum allowed number of characters of all data ticks on each axes. If the number of characters of any of the ticks coordinates is longer then this value, the ticks are re-scaled and an equation would appear at the end of the plot to clarify the conversion. If a list of two values is provided, the ticks length are set independently (eg: ticks_length = [5, 6]). If set to 0, no ticks are printed. The default value is 4. Alternatively use set_ticks_length(num) after the scatter function. 
Note: you could also directly provide all ticks coordinates and labels for each exes using the functions set_xticks and set_yticks. Access their docstrings for further guidance. 

\x1b[94mtitle\x1b[0m
It sets the title of the plot. Alternatively use set_title(label) after the scatter function. 

\x1b[94mxlabel\x1b[0m
It sets the label of the x axis. Alternatively use set_xlabel(label) after the scatter function. 

\x1b[94mylabel\x1b[0m
It sets the label of the y axis. Alternatively use set_ylabel(label) after the scatter function. 

\x1b[94mlabel\x1b[0m
It sets the label of the current data set, which will appear in the legend at the end of the plot. The default value is an empty string. If all labels are an empty string no legend is printed. Alternatively use set_legend(labels) to set all labels (as a list of strings) after the scatter function. 
"""
 
plot.__doc__ = """
It is equivalent to the scatter function with the point_marker option set to "" and the line option set to True. This means that no data points will be plotted, and the lines between consecutive points will be plotted instead. Here is a basic example: 

   \x1b[92mimport plotext as plt\x1b[0m
   \x1b[92mplt.plot(x, y)\x1b[0m
   \x1b[92mplt.show()\x1b[0m

Access the scatter function docstring for further documentation. 
"""

set_xticks.__doc__ = """
It sets the data ticks on the x axis. The ticks should be provided as a list of values. If two lists are provided, the second is intended as the list of labels to be printed at the coordinates given by the first list. Here is an example:

   \x1b[92mplt.scatter(data)\x1b[0m
   \x1b[92mplt.set_xticks(xticks, xlabels)\x1b[0m
   \x1b[92mplt.show()\x1b[0m

If no list is provided, the ticks will be calculated automatically.
If the ticks are not calculated automatically, any value given to the ticks_number parameter of the scatter or plot function will not affect the ticks plotted. On the contrary, the value of the ticks_length parameter needs to be higher that the maximum number of characters of the chosen ticks (or labels if present), otherwise some or all of the characters could be cut out of the plot. 
"""

set_yticks.__doc__ = """
It sets the data ticks on the y axis. The ticks should be provided as a list of values. If two lists are provided, the second is intended as the list of labels to be printed at the coordinates given by the first list. Here is an example:

   \x1b[92mplt.scatter(data)\x1b[0m
   \x1b[92mplt.set_yticks(yticks, ylabels)\x1b[0m
   \x1b[92mplt.show()\x1b[0m

If no list is provided, the ticks will be calculated automatically.
If the ticks are not calculated automatically, any value given to the ticks_number parameter of the scatter or plot function will not affect the ticks plotted. On the contrary, the value of the ticks_length parameter needs to be higher that the maximum number of characters of the chosen ticks (or labels if present), otherwise some or all of the characters could be cut out of the plot. 
"""


set_legend.__doc__ = """
It sets the labels of each plot (as a list of strings) to be printed as a legend. If all labels are an empty string, no legend will be printed. 
"""

show.__doc__ = """
It prints on terminal the plot created by the scatter or plot function. 
"""

clear_terminal.__doc__ = """
It clears the terminal. 
"""

clear_plot.__doc__ = """
It resets all the plot parameters to their default value, including the data coordinates. 
"""

sleep.__doc__ = """
 It adds a sleeping time to the computation and it is useful when continuously plotting  updating data in order to decrease a possible screen flickering. An input of, for example, 0.01 would add approximately 0.01 secs to the computation. Manually tweak this value to reduce the possible flickering. 
"""

savefig.__doc__ = """
It saves the plot canvas (without colors) as a text file, at the file address provided as input. 
"""

get_colors.__doc__ = """
It shows the available color codes.
"""

get_version.__doc__ = """
It returns the version_ of current plotext package.
"""

if var.nocolor:
    functions = [scatter, plot, set_xticks, set_yticks, show, clear_terminal, clear_plot, sleep, savefig, get_colors, get_version]
    for fun in functions:
        fun.__doc__ = ut.remove_color(fun.__doc__)


if __name__=="__main__":
    pass
    import plot as plt
    print(plt.set_yticks.__doc__)
