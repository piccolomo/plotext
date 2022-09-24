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
        self.force_size = None

        self.title = None
        self.xlabel = None
        self.ylabel = None

        self.axes = [None, None]
        self.ticks = [None, None] 
        self.grid = [None, None]
        self.xticks = None
        self.xlabels = []
        self.yticks = None
        self.ylabels = []

        self.fill = []
        self.point_marker = []
        self.line_marker = []

        self.facecolor = None
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
        self.legend = []

class _constants():
    def __init__(self):
        self.default_marker = "•"

        self.matrix = [[]]
        self.canvas = ""

par = _parameters()
con = _constants()

def _platform():
    if "win" in _sys.platform:
        par.platform = "windows"
    else:
        par.platform = "linux"

def _nocolor():
    if 'idlelib.run' in _sys.modules:
        par.nocolor = True
    else:
        par.nocolor = False

_platform()
if par.platform == "windows":
    from shutil import get_terminal_size as get_terminal_size_windows
    import subprocess
    subprocess.call('', shell = True)

_nocolor()

##############################################
########    Draw Basic Function    ###########
##############################################
def _draw(*args, **kwargs):
    width(kwargs.get("width"))
    height(kwargs.get("height"))
    force_size(kwargs.get("force_size"))

    title(kwargs.get("title"))
    xlabel(kwargs.get("xlabel"))
    ylabel(kwargs.get("ylabel"))
    _label(kwargs.get("label"))

    axes(kwargs.get("axes"))
    ticks(kwargs.get("ticks"))
    grid(kwargs.get("grid"))
    
    _fill(kwargs.get("fill"))
    _point_marker(kwargs.get("point_marker"))
    _line_marker(kwargs.get("line_marker"))

    facecolor(kwargs.get("facecolor"))
    ticks_color(kwargs.get("ticks_color"))
    canvas_color(kwargs.get("canvas_color"))
    _point_color(kwargs.get("point_color"))
    _line_color(kwargs.get("line_color"))

    _data(*args)
    xlim(kwargs.get("xlim"))
    ylim(kwargs.get("ylim"))
    
##############################################
########    Draw Called Functions     ########
##############################################
def width(width = None):
    par.width = width

def height(height = None):
    par.height = height

def force_size(x = None, y = None):
    x, y = set_first_to_both(x, y)
    x, y = set_list_to_both(x, y)
    x = set_var_if_none(x, False)
    y = set_var_if_none(y, False)
    par.force_size = [x, y]

def axes(x = None, y = None):
    x, y = set_first_to_both(x, y)
    x, y = set_list_to_both(x, y)
    x = set_var_if_none(x, True)
    y = set_var_if_none(y, True)
    par.axes = [x, y]

def ticks(x = None, y = None):
    x, y = set_first_to_both(x, y)
    x, y = set_list_to_both(x, y)
    x = set_var_if_none(x, 7)
    y = set_var_if_none(y, 5)
    par.ticks = [x, y]

def grid(x = None, y = None):
    x, y = set_first_to_both(x, y)
    x, y = set_list_to_both(x, y)
    x = set_var_if_none(x, False)
    y = set_var_if_none(y, False)
    par.grid = [x, y]

def _fill(x = None):
    x = set_var_if_none(x, False)
    if x == " ":
        x = ""
    par.fill.append(x)

def _point_marker(x = None):
    x = set_var_if_none(x, con.default_marker)
    if x == " ":
        x = ""
    par.point_marker.append(x)

def _line_marker(x = None):
    x = set_var_if_none(x, con.default_marker)
    if x == " ":
        x = ""
    par.line_marker.append(x)

def facecolor(x = None):
    x = set_var_if_none(x, "norm")
    par.facecolor = x

def ticks_color(x = None):
    x = set_var_if_none(x, "norm")
    par.ticks_color = x
    
def canvas_color(x = None):
    x = set_var_if_none(x, "norm")
    par.canvas_color = x

def _point_color(x = None):
    x = set_var_if_none(x, "norm")
    par.point_color.append(x)

def _line_color(x = None):
    x = set_var_if_none(x, "norm")
    par.line_color.append(x)

def title(x = None):
    x = set_var_if_none(x, "")
    par.title = x

def xlabel(x = None):
    x = set_var_if_none(x, "")
    par.xlabel = x

def ylabel(x = None):
    x = set_var_if_none(x, "")
    par.ylabel = x
    
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

def xlim(x = None, y = None):
    x, y = set_first_to_both(x, y)
    x, y = set_list_to_both(x, y)
    par.xlim_plot = [x, y]

def ylim(x = None, y = None):
    x, y = set_first_to_both(x, y)
    x, y = set_list_to_both(x, y)
    par.ylim_plot = [x, y]

def _label(x = None):
    x = set_var_if_none(x, "")
    par.legend.append(x)
    
##############################################
########    Other Set Functions     ##########
##############################################
def canvas_size(x = None, y = None):
    x, y = set_first_to_both(x, y)
    x, y = set_list_to_both(x, y)
    width(x)
    height(y)

def legend(legend = None):
    legend = list(legend)
    if legend == None:
        legend = [None] * len(par.legend)
    par.label = legend

def xticks(x = None, y = None):
    x, y = list(x), list(y)
    x, y = set_first_to_both(x, y)
    x = set_var_if_none(x, [])
    y = set_var_if_none(y, [])
    y = list(map(str, y))
    par.xticks, par.xlabels = x, y
    par.ticks[0] = len(x)

def yticks(x = None, y = None):
    x, y = list(x), list(y)
    x, y = set_first_to_both(x, y)
    x = set_var_if_none(x, [])
    y = set_var_if_none(y, [])
    y = list(map(str, y))
    par.yticks, par.ylabels = x, y
    par.ticks[1] = len(y)

##############################################
#############   Get Function    ##############
##############################################
def get_parameters():
    print("width", par.width)
    print("height", par.height)
    print("force_size", par.force_size)
    print()
    print("axes", par.axes)
    print("ticks", par.ticks)
    print("grid", par.grid)
    print()
    print("point_marker", par.point_marker)
    print("line_marker", par.line_marker)
    print()
    print("facecolor", par.facecolor)
    print("ticks_color", par.ticks_color)
    print("canvas_color", par.canvas_color)
    print("point_color", par.point_color)
    print("line_color", par.line_color)
    print()
    print("title", par.title)
    print("xlabel", par.xlabel)
    print("ylabel", par.ylabel)
    print()
    print("x[:5]", par.x[:5])
    print("y[:5]", par.y[:5])
    print("xlim", par.xlim_plot)
    print("ylim", par.ylim_plot)
    print("legend", par.label)
    
##############################################
############    Show Function     ############
##############################################
def show():
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

    _yaxis()
    _xaxis()
    
    _legend()
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
    height_title = int(par.title != "")
    height_xaxis = int(par.axes[0])
    height_xticks = bool(par.ticks[0])
    height_labels = int(par.xlabel != "" or par.ylabel != "")
    #(par.xlabel != "" or par.ylabel != "")
    par.height_extra = height_title + height_xaxis + height_xticks + height_labels
    par.height_min = 1 + par.height_extra

def _height():
    height = set_var_if_none(par.height, par.height_max)
    height = abs(int(height))
    if height > par.height_max and not par.force_size[0]:
        height = par.height_max
    if height < par.height_min:
        height = par.height_min
    par.height = height
    par.rows = height - par.height_extra

def _ylim_data():
    par.ylim_data = get_lim_data(par.y)

def _ylim_plot():
    par.ylim_plot[0] = set_var_if_none(par.ylim_plot[0], par.ylim_data[0])
    par.ylim_plot[1] = set_var_if_none(par.ylim_plot[1], par.ylim_data[1])
    par.dy = (par.ylim_plot[1] - par.ylim_plot[0]) / par.rows

def _yticks():
    if par.yticks == None and par.ticks[1]:
        y = par.ylim_plot
        y = linspace(min(y), max(y), par.ticks[1])
        y = [int(el) if el == int(el) else el for el in y]
        par.yticks, par.ylabels = y, get_labels(y)
    par.rticks = get_matrix_data(par.yticks, par.ylim_plot, par.rows)

def _width_min():
    par.width_yaxis = 2 * int(par.axes[1])
    par.width_yticks = max(map(len, par.ylabels), default = 0) * bool(par.ticks[1])
    par.width_extra = par.width_yaxis + par.width_yticks
    par.width_min = 1 + par.width_extra

def _width():
    width = set_var_if_none(par.width, par.width_max)
    width = abs(int(width))
    if width > par.width_max and not par.force_size[0]:
        width = par.width_max
    if width < par.width_min:
        width = par.width_min
    par.width = width
    par.cols = width - par.width_extra

def _xlim_data():
    par.xlim_data = get_lim_data(par.x)

def _xlim_plot():
    par.xlim_plot[0] = set_var_if_none(par.xlim_plot[0], par.xlim_data[0])
    par.xlim_plot[1] = set_var_if_none(par.xlim_plot[1], par.xlim_data[1])
    par.dx = (par.xlim_plot[1] - par.xlim_plot[0]) / par.cols

def _xticks():
    if par.xticks == None and par.ticks[0]:
        x = [par.xlim_plot[0], par.xlim_plot[1]]
        x = linspace(min(x), max(x), par.ticks[0])
        x = [int(el) if el == int(el) else el for el in x]
        par.xticks, par.xlabels = x, get_labels(x)
    par.cticks = get_matrix_data(par.xticks, par.xlim_plot, par.cols)

def _matrix():
    space_marker = add_color(" ", "norm", par.canvas_color)
    par.matrix = [[space_marker for c in range(par.cols)] for r in range(par.rows)]

def _grid():
    grid_color = "iron"
    grid_color = par.ticks_color
    if par.grid[0]:
        for c in par.cticks[1:-1]:
            y = list(range(par.rows))
            x = [c] * par.rows
            marker = add_color("│", grid_color, par.canvas_color)
            par.matrix = update_matrix(par.matrix, x, y, marker)
    if par.grid[1]:
        for r in par.rticks[1:-1]:
            x = list(range(par.cols))
            y = [r] * par.cols
            marker = add_color("─", grid_color, par.canvas_color)
            par.matrix = update_matrix(par.matrix, x, y, marker)
            if par.grid[0]:
                x = par.cticks[1:-1]
                y = [r] * len(x)
                marker = add_color("┼", grid_color, par.canvas_color)
                par.matrix = update_matrix(par.matrix, x, y, marker)

def _add_data():
    for s in range(len(par.x)):
        x, y = par.x[s], par.y[s]
        point_marker, point_color = par.point_marker[s], par.point_color[s]
        line_marker, line_color = par.line_marker[s], par.line_color[s]
        if line_marker != "":
            x, y = par.x[s], par.y[s]
            x, y = get_line(x, y, par.dx)
            if par.fill[s]:
                x, y = fill(x, y, par.dy)
            x = get_matrix_data(x, par.xlim_plot, par.cols)
            y = get_matrix_data(y, par.ylim_plot, par.rows)
            line_marker = add_color(line_marker, line_color, par.canvas_color)
            par.matrix = update_matrix(par.matrix, x, y, line_marker)
        if point_marker != "":
            x, y = par.x[s], par.y[s]
            if par.fill[s]:
                x, y = fill(x, y, par.dy)
            x = get_matrix_data(x, par.xlim_plot, par.cols)
            y = get_matrix_data(y, par.ylim_plot, par.rows)
            point_marker = add_color(point_marker, point_color, par.canvas_color)
            par.matrix = update_matrix(par.matrix, x, y, point_marker)

def _yaxis():
    l = par.width_yticks
    labels = [" " * l for r in range(par.rows)]
    for i in range(len(par.rticks)):
        r = par.rticks[i]
        if r in range(par.rows):
            labels[r] = str(par.ylabels[i])[:l]
    labels = [el + " " * (l - len(el)) for el in labels]
    labels = [list(el) for el in labels]
    labels = [[add_color(sub_el, par.ticks_color, par.facecolor) for sub_el in el] for el in labels]
    if par.axes[1]:
        ytick = "┼ " if par.grid[1] else "├ "
        axis = [ytick if r in par.rticks else "│ " for r in range(par.rows)]
    else:
        axis = [""] * par.rows
    axis = [list(el) for el in axis]
    axis = [[add_color(sub_el, par.ticks_color, par.facecolor) for sub_el in el] for el in axis]

    for r in range(par.rows):
        if par.axes[1]:
            par.matrix[r] += axis[r]
        if par.ticks[1]:
            par.matrix[r] += labels[r]

def _xaxis():
    axis = ["─" for r in range(par.cols)] + ["┘"] * par.axes[1] + [" "] * (par.width_extra - 1)
    labels = [" "  for r in range(par.width)]
    lc = len(par.cticks)
    xtick = "┼" if par.grid[1] else "┬"
    for i in range(lc):
        c = par.cticks[i]
        new_label = str(par.xlabels[i])
        l = len(new_label)
        if labels[c - 1] == " ":
            if c + l + 1 <= par.width:
                new_label += " " * (l + 1 - len(new_label))
                labels[c : c + l + 1] = list(new_label)
            elif labels[-l - 1] == " ":
                labels[-l :] = list(new_label)
            if c == par.cols:
                axis[c] = "┤"
            else:
                axis[c] = xtick
    labels = [add_color(el, par.ticks_color, par.facecolor) for el in labels]
    axis = [add_color(el, par.ticks_color, par.facecolor) for el in axis]
    if par.axes[0]:
        par.matrix.insert(0, axis) 
    if par.ticks[0]:
        par.matrix.insert(0, labels)
        
def _legend():
    if (par.legend == [""] * len(par.legend)):
        return
    legend = par.legend
    l = len(legend)
    legend = [" " + legend[i] if legend[i] != "" else " signal " + str(i + 1) for i in range(l)]
    legend = [list(el) for el in legend]
    legend = [[add_color(sub_el, par.ticks_color, par.canvas_color) for sub_el in el] for el in legend]
    markers = []
    for i in range(l):
        point_marker = par.point_marker[i] if par.point_marker[i] != "" else par.line_marker[i]
        point_color = par.point_color[i] if par.point_marker[i] != "" else par.line_color[i]
        point_marker = add_color(point_marker, point_color, par.canvas_color)
        
        line_marker = par.line_marker[i] if par.line_marker[i] != "" else par.point_marker[i]
        line_color = par.line_color[i] if par.line_marker[i] != "" else par.point_color[i]
        line_marker = add_color(line_marker, line_color, par.canvas_color)
        
        marker = [line_marker] * 2 + [point_marker] + [line_marker] * 2
        markers += [marker]
    legend = [markers[i] + legend[i] for i in range(l)]
    #legend = [[add_color(sub_el, "bold", "white") for sub_el in el] for el in legend]
    if len(legend) > par.rows:
        return
    for i in range(l):
        li = len(legend[i])
        if li > par.cols:
            return
        par.matrix[-(i+1)][0:li] = legend[i]

def _title():
    if par.title == "":
        return
    title = par.title[:par.width]
    space1 = " " * int((par.cols - len(title)) /2)
    space2 = " " * (par.width - len(title + space1))
    title = space1 + title + space2
    title = list(title)
    title = [add_color(el, par.ticks_color, par.facecolor) for el in title]
    #title = [add_color(el, "bold") for el in title]
    par.matrix += [title]

def _axes_label():
    if par.xlabel == "" and par.ylabel == "":
        return
    xlabel = "[x] " + par.xlabel + " "
    ylabel = par.ylabel + " [y]"
    if len(xlabel) + len(ylabel) > par.width:
        return
    space = " " * (par.width - len(xlabel) - len(ylabel))
    label = xlabel + space + ylabel
    label = list(label)
    label = [add_color(el, par.ticks_color, par.facecolor) for el in label]
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
        print("color removed")
    _write(canvas)
    
##############################################
##########    Utility Functions    ###########
##############################################
def set_first_to_both(x = None, y = None):# by setting one parameter to a value, both are set
    if x != None and y == None:
        y = x
    return [x, y]

def set_list_to_both(x = None, y = None): # by setting a parameter to a list, both are set
    if type(x) == list:
        x, y = x[0], x[1]
    return [x, y]

def set_var_if_none(x = None, x_none = None): # set a parameter when none is provided. 
    if x == None:
        x = x_none
    elif x_none != None:
        x = type(x_none)(x)
    return x

def get_lim_data(data):
    m = min([min(el, default = 0) for el in data])
    M = max([max(el, default = 0) for el in data])
    return [m, M]
    
def linspace(lower, upper, length):
    if length == 1:
        return [0.5*(lower+upper)]
    return [lower + x*(upper-lower)/(length-1) for x in range(length)]

def get_labels(ticks):
    if len(ticks)==1:
        l=len(str(ticks[0]))
    else:
        l = max([distinguish(ticks[i], ticks[i+1]) for i in range(len(ticks)-1)])
    labels = [round_to_character(el, l) for el in ticks]
    labels = [str(el) for el in labels]
    return labels

def distinguish(a, b):
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

def round_to_character(n, c):
    int_len = len(str(int(n)))
    d = c - int_len - 1
    if d < 0:
        d = 0
    return round(n, d)

def get_matrix_data(data, plot_lim, bins):
    if data == None:
        data = []
    dz = (plot_lim[1] - plot_lim[0]) / bins
    data = [int((el - plot_lim[0]) / dz) if el != plot_lim[1] else bins - 1 for el in data]
    #data = [el for el in data if el in range(bins)]
    return data

color_code = {'norm': 0, 'black': 30, 'iron': 90, 'gray': 2, 'cloud': 37, 'white': 97, 'red': 31, 'tomato': 91, 'basil': 32, 'green': 92, 'yellow': 93, 'gold': 33, 'blue': 34, 'indigo': 94, 'sapphire': 36, 'artic': 96, 'lilac': 95, 'violet': 35, 'italic': 3, 'bold': 1, 'flash': 5}
background_code = {'norm': 28, 'black': 40, 'iron': 100, 'cloud': 47, 'white': 107, 'red': 41, 'tomato': 101, 'basil': 42, 'green': 102, 'yellow': 103, 'gold': 43, 'blue': 44, 'indigo': 104, 'sapphire': 46, 'artic': 106, 'lilac': 105, 'violet': 45}

def apply_color(text, code):
    if code == 0 or code == 28:
        return text
    return '\033[' + str(code) + 'm' + text + '\033[0m'
    
def add_color(text = "", color = "norm", background = "norm"):
    color = color_code[color]
    background = background_code[background]
    text = apply_color(text, color)
    text = apply_color(text, background)
    return text

def get_line(x, y, dx): 
    x_line = []
    y_line = []
    for n in range(len(x) - 1):
        Dy, Dx = y[n + 1] - y[n], x[n + 1] - x[n]
        l = int((x[n + 1] - x[n]) / dx)
        x_line_n = [x[n] + i * dx for i in range(l + 1)]
        y_line_n = [y[n] + i * dx * Dy / Dx for i in range(l + 1)]
        x_line.extend(x_line_n)
        y_line.extend(y_line_n)
    return x_line, y_line

def update_matrix(matrix, x, y, marker):
    cols, rows = len(matrix[0]), len(matrix)
    for i in range(len(x)):
        c, r = x[i], y[i] 
        if 0 <= r < rows and 0 <= c < cols:
            matrix[r][c] = marker
    return matrix

def fill(x, y, dy):
    y_new = y
    x_new = x
    for i in range(len(y)):
        y0 = 0 + 0*dy / 2
        yi = y[i] -0* dy / 2
        l = int(abs(y[i]) / dy)
        y_temp = arange(min(y0, yi), max(y0, yi), dy/2)
        y_new += y_temp
        x_new += [x[i]] * len(y_temp)
    return [x, y]

def arange(start, stop, step = 1):
    res = []
    i = start
    while i < stop:
        res.append(i)
        i = i + step
        #i=_round(i,14)
    return res

def _write(string):
    _sys.stdout.write(string)

def _check_path(path):
    basedir = _os.path.dirname(path)
    if _os.path.exists(basedir):
        return path
    else:
        print("warning: parent directory doesn't exists.")
        home = _os.path.expanduser("~") 
        path = _os.path.join(home, _os.path.basename(path))
    return path

def _remove_color(string):
    for c in list(color_code.values()) + list(background_code.values()):
        string = string.replace('\x1b[' + str(c) + 'm', '')
    return string

##############################################
##########    Basic Functions    #############
##############################################
def scatter(*args,
        width = None,
        height = None,
        force_size = None,

        title = None,
        xlabel = None,
        ylabel = None,

        axes = None,
        ticks = None,
        grid = None,

        fill = None,
        point_marker = con.default_marker,
        line_marker = "",

        axes_color = None,
        canvas_color = None,
        point_color = None,
        line_color = None,

        xlim = None,
        ylim = None,
        label = None):
    _draw(*args,
            width = width,
            height = height,
            force_size = force_size,

            title = title,
            xlabel = xlabel,
            ylabel = ylabel,
            
            axes = axes,
            ticks = ticks,
            grid = None,

            fill = fill,
            point_marker = point_marker,
            line_marker = line_marker,
            
            axes_color = axes_color,  
            canvas_color = canvas_color,
            point_color = point_color,
            line_color = line_color,
            label = label)
    
def plot(*args,
        width = None,
        height = None,
        force_size = None,

        title = None,
        xlabel = None,
        ylabel = None,

        axes = None,
        ticks = None,
        grid = None,

        fill = None,
        point_marker = "",
        line_marker = con.default_marker,

        axes_color = None,
        canvas_color = None,
        point_color = None,
        line_color = None,

        xlim = None,
        ylim = None,
        label = None):
    _draw(*args,
            width = width,
            height = height,
            force_size = force_size,

            title = title,
            xlabel = xlabel,
            ylabel = ylabel,
            label = label,
          
            axes = axes,
            ticks = ticks,
            grid = grid,
            
            fill = fill,
            point_marker = point_marker,
            line_marker = line_marker,
            
            axes_color = axes_color,  
            canvas_color = canvas_color,
            point_color = point_color,
            line_color = line_color)

def clear_terminal():
    _write('\033c')

clt = clear_terminal

def clear_plot():
    par.__init__()

clp = clear_plot

def sleep(time):
    [i for i in range(int(time * 15269989))]
       
def terminal_size():
    if par.platform == "windows":
        return get_terminal_size_windows()
    elif par.nocolor:
        return [185, 45]
    else:
        return list(_os.get_terminal_size())
    
def savefig(path):
    path = _check_path(path)
    with open(path , "w+", encoding = "utf-8") as file:
        file.write(_remove_color(par.canvas))
    _write("plot saved as " + path)
    
def colors():
    color = [add_color(c, c, "norm") for c in list(color_code.keys())]
    _write("\nFullground colors: " + ", ".join(color))
    background = [add_color(b, "norm", b) for b in list(background_code.keys())]
    _write("\nBackground colors: " + ", ".join(background) + '\n')
    
def version():
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
scatter.__doc__ = """\nIt creates a scatter plot of coordinates given by the x and y lists. Optionally, a single y list could be provided. Here is a basic example:

\x1b[32mimport plotext as plt
plt.scatter(x, y)
plt.show()\x1b[0m

Multiple data sets could be plotted using consecutive scatter functions:

\x1b[32mplt.scatter(x1, y1)
plt.scatter(y2)
plt.show()\x1b[0m

Here are all the parameters of the scatter function: 

\x1b[33mwidth\x1b[0m
It sets the number of columns of the figure. By default, it is the highest value allowed by the terminal size. Alternatively use width(width) or canvas_size(width, height) after the scatter function.

\x1b[33mheight\x1b[0m
It sets the number of rows of the figure. By default, it is the highest value allowed by the terminal size. Alternatively use height(height) or canvas_size(width, height) after the scatter function.

\x1b[33mforce_size\x1b[0m
By default, the plot dimensions are limited by the terminal size. Set force_size to True in order to allow bigger plots. Alternatively use force_size(True) after the scatter function (but before the cols() and rows() functions, if present).
Note: plots bigger then the terminal size may not be readable. 

\x1b[33mtitle\x1b[0m
It sets the title of the plot. Alternatively use title(label) after the scatter function. 

\x1b[33mxlabel\x1b[0m
It sets the label of the x axis. Alternatively use xlabel(label) after the scatter function. 

\x1b[33mylabel\x1b[0m
It sets the label of the y axis. Alternatively use ylabel(label) after the scatter function. 

\x1b[33mlabel\x1b[0m
It sets the label of the current data set, which will appear in the legend at the end of the plot. The default value is an empty string. If all labels are an empty string no legend is printed. Alternatively use legend(labels) to set all labels (as a list of strings) after the scatter function. 

\x1b[33maxes\x1b[0m
When set to True (as by default), the x and y axes are added to the plot. A list of two Booleans will set the x and y axis independently (eg: axes = [True, False]). Alternatively, use axes(axes) after the scatter function.  

\x1b[33mticks\x1b[0m
It sets the number of data ticks printed on each axis. If a list of two values is provided, the number of ticks for each axis is set independently (eg: ticks_number = [5, 6]). If set to 0, no ticks are printed. The default value is [7, 5]. Alternatively use ticks(ticks) after the scatter function.
Note: you could also set directly the ticks coordinates and labels for each axis using the functions xticks() and yticks(). Access their docstrings for further guidance. 

\x1b[33mgrid\x1b[0m
When set to True, the x and y grid lines are added to the plot. A list of two Booleans will set the x and y grid lines independently (eg: grid = [True, False]). The default value is False. Alternatively, use grid(grid) after the scatter function.  

\x1b[33mfill\x1b[0m
When set to True, the plot will fill the space between the data points and the y=0 level. The default value is False. Alternatively, use fill(fill) after the scatter function.  

\x1b[33mpoint_marker\x1b[0m 
It sets the marker used to identify each data point plotted. It should be a single character and it could be a different value for each data set. If an empty string is provided (or the space character), no data point is plotted. The default value is '•'. This parameter can only be set internally, because it is associated to the current data set plotted. 

\x1b[33mline_marker\x1b[0m 
It sets the marker used to identify the lines between two consecutive data points. It should be a single character and it could be a different value for each data set. If an empty or the space string is provided, as by default, no lines are plotted. This parameter can only be set internally, because it is associated to the current data set plotted.

\x1b[33mfacecolor\x1b[0m
It sets the background color of the axes, ticks, title and axes labels, when present, without affecting the canvas background color. Use colors() to find the available background color codes. The default value is 'norm'. Alternatively use facecolor(color) after the scatter function. 

\x1b[33mticks_color\x1b[0m
It sets the color of the axes, ticks, grid, title, axes labels, and legend labels, when present, without affecting the canvas color. Use colors() to find the available full-ground color codes. The default value is 'norm'. Alternatively use ticks_color(color) after the scatter function. 

\x1b[33mcanvas_color\x1b[0m
It sets the canvas background color, without affecting the rest of the figure colors. Alternatively use canvas_color(color) after the scatter function. Use colors() to find the available background color codes. The default value is 'norm'.

\x1b[33mpoint_color\x1b[0m
It sets the color of the data points. Use colors() to find the available full-ground color codes. The default value is 'norm'. This parameter can only be set internally, because it is associated to the current data set plotted.

\x1b[33mline_color\x1b[0m
It sets the color of the lines, if plotted. Use colors() to find the available full-ground color codes. The default value is 'norm'. This parameter can only be set internally, because it is associated to the current data set plotted.

\x1b[33mxlim\x1b[0m
It sets the minimum and maximum limits of the plot in the x axis. It requires a list of two numbers, where the first sets the left (minimum) limit and the second the right (maximum) limit. If one or both values are not provided, they are calculated automatically. Alternatively use xlim(xlim) after the scatter function. 

\x1b[33mylim\x1b[0m
It sets the minimum and maximum limits of the plot in the y axis. It requires a list of two numbers, where the first sets the lower (minimum) limit and the second the upper (maximum) limit. If one or both values are not provided, they are calculated automatically. Alternatively use ylim(ylim) after the scatter function."""
 
plot.__doc__ = """It plots y versus x as lines and it is equivalent to the scatter function with the point_marker set to the empty string and the line_marker set to '•'. This means that no data points will be plotted, and the lines between consecutive points will be plotted instead. Here is a basic example: 

\x1b[32mimport plotext as plt
plt.plot(x, y)
plt.show()\x1b[0m

Access the scatter function docstring for further documentation.\n"""

xticks.__doc__ = """\nIt sets the data ticks on the x axis. The ticks should be provided as a list of values. If two lists are provided, the second is intended as the list of labels to be printed at the coordinates given by the first list. Here is an example:

\x1b[32mplt.scatter(data)
plt.xticks(xticks, xlabels)
plt.show()\x1b[0m

If no list are provided, the ticks will be calculated automatically.\n"""

yticks.__doc__ = """\nSimilar to the function xticks but relative to the y axis instead. Access its docstrings for further guidance.\n"""

legend.__doc__ = """It sets the labels for each data set (as a list of strings) to be printed as a legend on the top left corner of the canvas. If all labels are an empty string, no legend is printed.\n"""

show.__doc__ = """\nIt prints on terminal the plot created by the scatter or plot function.\n"""

clear_terminal.__doc__ = """\nIt clears the terminal and it is generally useful when plotting a continuous stream of data. The function clt() is equivalent.\n"""

clear_plot.__doc__ = """\nIt resets all the plot parameters to their default value, including all x and y coordinates. The function clp() is equivalent.\n"""

sleep.__doc__ = """\nIt adds a sleeping time to the computation and it is useful when continuously plotting a stream of data, in order to decrease a possible screen flickering. An input of, for example, 0.01 would add approximately 0.01 secs to the computation. Manually tweak this value to reduce the flickering.\n"""

savefig.__doc__ = """\nIt saves the plot canvas (without colors) as a text file, at the address provided in input.\n"""

colors.__doc__ = """\nIt shows the available full-ground and background color codes.\n"""

version.__doc__ = """\nIt returns the version of the installed plotext package.\n"""

if par.nocolor:
    functions = [scatter, plot, xticks, yticks, show, clear_terminal, clear_plot, sleep, savefig, colors, version]
    for fun in functions:
        fun.__doc__ = _remove_color(fun.__doc__)

if __name__ == "__main__":
    import plot as plt

