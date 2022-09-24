# /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

##############################################
###########    Basic Functions    ############
##############################################
    
def scatter(*args, **kwargs):
    _set_platform()
    _set_data(*args)

    _set_axes(kwargs.get("axes"))
    _set_ticks(kwargs.get("ticks"))
    _set_equations(kwargs.get("equations"))

    _set_terminal_size()
    _set_cols_max()
    _set_rows_max()
    
    set_force_size(kwargs.get("force_size"))
    set_cols(kwargs.get("cols"))
    set_rows(kwargs.get("rows"))

    set_xlim(kwargs.get("xlim"))
    set_ylim(kwargs.get("ylim"))
    
    _set_point(kwargs.get("point"))
    _set_point_marker(kwargs.get("point_marker"))
    _set_point_color(kwargs.get("point_color"))
    _set_line(kwargs.get("line"))
    _set_line_marker(kwargs.get("line_marker"))
    _set_line_color(kwargs.get("line_color"))
    set_background(kwargs.get("background"))

    set_axes_color(kwargs.get("axes_color"))
    set_spacing(kwargs.get("spacing"))
    set_decimals(kwargs.get("decimals"))

def plot(*args, force_size = None, cols = None, rows = None, xlim = None, ylim = None, point = False, point_marker = None, point_color = None, line = True, line_marker = None, line_color = None, background = None, axes = None, axes_color = None, ticks = None, spacing = None, equations = None, decimals = None):
    
    scatter(*args, cols = cols, rows = rows, xlim = xlim, ylim = ylim, point = point, point_marker = point_marker, point_color = point_color, line = line, line_marker = line_marker, line_color = line_color, background = background, axes = axes, ticks = ticks, axes_color = axes_color, spacing = spacing, equations = equations, decimals = decimals)    

def show():
    _set_xlim()
    _set_ylim()
    _set_grid()
    _add_yaxis()
    _add_xaxis()
    _set_canvas()
    _add_equations()
    _print_canvas()
    #clear_plot()
    
def clear_terminal():
    _print('\033c')
    
def clear_plot():
    _vars.__init__()

def sleep(time):
    [i for i in range(int(time*15269989))]
    
def savefig(path):
    with open(path , "w+", encoding = "utf-8") as file:
        file.write(_remove_color(_get_canvas()))
    print("plot saved as", path)

def get_colors():
    fg_colors = [_set_color(fg_c, fg_c, "norm") for fg_c in _fg_colors]
    _print("\nFullground colors: " + ", ".join(fg_colors))
    bg_colors = [_set_color(bg_c, "norm", bg_c) for bg_c in _bg_colors]
    _print("\n\nBackground colors: " + ", ".join(bg_colors) + '\n')
    
def get_version():
    init_path = "__init__.py"
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, init_path), 'r') as fp:
        lines = fp.read()
    for line in lines.splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        print("Unable to find version string.")

def get_x_from_col(col=0):
    return 1. * _vars.dx * col + _vars.xmin + _vars.dx/2.

def get_y_from_row(row=0):
    return 1. * _vars.dy * row + _vars.ymin + _vars.dy/2.

def run_test():
    clear_terminal()
    l = 7
    y1 = list(range(7)) + list(range(7, 0, -1))
    y2 = list(range(7, 0, -1)) + list(range(7))
    scatter(y1, point_color = "red", point_marker = "o")
    plot(y2, line_color = "blue", line_marker = '=', ticks=1, axes=1)
    #set_force_size(True)
    set_cols(300)
    set_rows(300)
    set_xlim([-1, 2 * l + 1])
    set_ylim([-1, l + 1])
    set_spacing([10, 5])
    set_axes_color("green")
    set_background("black")
    show()
    #savefig(r"test.txt")
    clear_plot()

##############################################
#########    Internal Variables    ###########
##############################################
    
class _vars_class():
    def __init__(self):
        self.ip = 6 #internal precision
        self.x = []
        self.y = []
        self.xmin = 0
        self.xmax = 0
        self.dx = 0
        self.ymin = 0
        self.ymax = 0
        self.dy = 0

        self.cols_term = None
        self.rows_term = None
        self.cols_max = None
        self.rows_max = None
        self.force_size = False
        self.cols = None
        self.rows = None
        
        self.point = []
        self.point_marker = []
        self.point_color = []
        self.line = []
        self.line_marker = []
        self.line_color = []
        self.background = "norm"

        self.axes = [True, True]
        self.axes_color = "norm"
        self.ticks = [True, True]
        self.spacing = [10, 5]
        self.equations = False
        self.decimals = 2

        self.grid = [[]]
        self.no_color = False
        self.canvas = ""

_vars = _vars_class()

##############################################
##########    Called Functions     ###########
##############################################

def _set_platform():
    if "win" in sys.platform:
        import subprocess
        subprocess.call('', shell = True)
    if ('idlelib.run' in sys.modules):
        _vars.no_color = True
       # _vars.force_size = True

def _print(string):
    sys.stdout.write(string)

def _set_data(*args):
    if len(args) == 0:
        x, y = [], []
    elif len(args) == 1:
        y = args[0]
        x = list(range(len(y)))
    else:
        x = args[0]
        y = args[1]
    length = min(len(x), len(y))
    if len(x) != len(y):
        x = x[ : length]
        y = y[ : length]
    _vars.x.append(x)
    _vars.y.append(y)

def _set_axes(axes = None):
    axes =_set_var_if_none(axes, [True, True])
    if type(axes) == list:
        axes = [axes[0], axes[1]]
    else: 
        axes = [axes, axes]
    _vars.axes = axes
    
def _set_var_if_none(var, value):
    if var == None:
        return value
    else:
        return var
    
def _set_ticks(ticks = None):
    ticks =_set_var_if_none(ticks, [True, True])
    if type(ticks) == list:
        ticks = [ticks[0], ticks[1]]
    else: 
        ticks = [ticks, ticks]
    _vars.ticks = ticks
    
def _set_equations(equations = None):
    _vars.equations =_set_var_if_none(equations, False)

def _set_terminal_size():
    _vars.cols_term, _vars.rows_term = get_terminal_size()

def get_terminal_size():
    if "win" in sys.platform:
        import shutil
        return shutil.get_terminal_size()
    elif 'idlelib.run' in sys.modules:
        return [185, 45]
    else:
        return os.get_terminal_size()

def _set_cols_max():
    _vars.cols_max = _vars.cols_term - 2 * _vars.ticks[1] - 1 * _vars.axes[1] - 0
    
def _set_rows_max():
    _vars.rows_max = _vars.rows_term - 1 * _vars.ticks[0] - 1 * _vars.axes[0] - 2 * _vars.equations - 2

def set_force_size(force_size = False):
    _vars.force_size = _set_var_if_none(force_size, False)
    
def set_cols(cols = None):
    cols = _set_var_if_none(cols, _vars.cols_max)
    if cols <= 0:
        cols = 1
    if cols > _vars.cols_max and not _vars.force_size:
       _vars.cols = _vars.cols_max
    else:
       _vars.cols = max(1, abs(int(cols)))

def set_rows(rows = None):
    rows = _set_var_if_none(rows, _vars.rows_max)
    if rows <= 0:
        rows = 1
    if rows > _vars.rows_max and not _vars.force_size:
       _vars.rows = _vars.rows_max
    else:
       _vars.rows = max(1, abs(int(rows)))

def set_xlim(xlim = None):
    _vars.xmin, _vars.xmax = _set_var_if_none(xlim, [None, None])

def set_ylim(ylim = None):
    _vars.ymin, _vars.ymax = _set_var_if_none(ylim, [None, None])

def _set_point(point = None):
    _vars.point.append(_set_var_if_none(point, True))

def _set_point_marker(point_marker = None):
    point_marker = _set_var_if_none(point_marker, "•")
    _vars.point_marker.append(point_marker[0])

def _set_point_color(point_color = None):
    _vars.point_color.append(_set_var_if_none(point_color, "norm"))

def _set_line(line = None):
    _vars.line.append(_set_var_if_none(line, False))

def _set_line_marker(line_marker = None):
    line_marker = _set_var_if_none(line_marker, "•")
    _vars.line_marker.append(line_marker[0])

def _set_line_color(line_color = None):
    _vars.line_color.append(_set_var_if_none(line_color, "norm"))

def set_background(background = None):
    _vars.background = _set_var_if_none(background, "norm")

def set_axes_color(axes_color = None):
    _vars.axes_color = _set_var_if_none(axes_color, "norm")

def set_spacing(spacing = None):
    spacing = _set_var_if_none(spacing, [10, 5])
    if type(spacing) == list:
        spacing = [spacing[0], spacing[1]]
    else: 
        spacing = [spacing, spacing]
    _vars.spacing = spacing

def set_decimals(decimals = None):
    _vars.decimals = _set_var_if_none(decimals, 2)

def _set_xlim(xlim = None):
    _vars.xmin, _vars.xmax =_set_lim(_vars.x, _vars.xmin, _vars.xmax, _vars.cols)
    _vars.dx = 1. * (_vars.xmax - _vars.xmin) / _vars.cols
    _vars.dx = round(_vars.dx, _vars.ip)

# the set minimum (maximum) value should be inside the first (last) data bin
# this changes the actual minimum (maximum) value by a bin_offset 
def _set_lim(z = [], zmin = None, zmax = None, bins = 2):
    dzmin, dzmax = zmin == None, zmax == None
    zmin = _set_var_if_none(zmin, min(map(min, z)))
    zmax = _set_var_if_none(zmax, max(map(max, z)))
    if zmin == zmax:
        zm = [0.5 * zmin, 1.5 * zmax]
        zm.sort()
        zmin, zmax = zm
    if bins - 1 == 0:
        bins += 1
    dz = (zmax - zmin) / (bins - 1)
    return zmin - dzmin * dz / 2, zmax + dzmax * dz / 2

def _set_ylim(ylim = None):
    _vars.ymin, _vars.ymax = _set_lim(_vars.y, _vars.ymin, _vars.ymax, _vars.rows)
    _vars.dy = 1.*(_vars.ymax - _vars.ymin) / _vars.rows
    _vars.dy = round(_vars.dy, _vars.ip)

def _set_grid():
    space = _set_color(" ", background = _vars.background)
    _vars.grid = [[space for c in range(_vars.cols)] for r in range(_vars.rows)]
    for s in range(len(_vars.x)):
        if _vars.line[s]:
            _add_to_grid(*_get_line(_vars.x[s], _vars.y[s]), _vars.line_marker[s], _vars.line_color[s])
        if _vars.point[s]:
            _add_to_grid(_vars.x[s], _vars.y[s], _vars.point_marker[s], _vars.point_color[s])

_fg_colors = ['norm', 'black', 'gray', 'red', 'green', 'yellow', 'orange', 'blue', 'violet', 'cyan', 'bold']
_fg_color_codes = [0, 30, 2, 91, 92, 93, 33, 94, 95, 96, 1]
_bg_colors = ['norm', 'black', 'gray', 'red', 'green', 'yellow', 'orange', 'blue', 'violet', 'cyan', 'white']
_bg_color_codes = [28, 40, 100, 41, 42, 103, 43, 44, 45, 106, 47]
    
# it applies the proper color codes to a string
def _set_color(text = "", color = "norm", background = "norm"):
    code = '\033['
    if type(color) == str:
        for c in range(len(_fg_colors)):
            if color == _fg_colors[c]:
                code += str(_fg_color_codes[c])
    code += 'm'
    code += '\033['
    if type(background) == str:
        for c in range(len(_bg_colors)):
            if background == _bg_colors[c]:
                code += str(_bg_color_codes[c])
    code += 'm'
    return code + text + '\033[0m'

def _add_to_grid(x, y, marker, color):
    for n in range(len(x)):
        c = int(round((x[n] - _vars.xmin) / _vars.dx, _vars.ip))
        r = int(round((y[n] - _vars.ymin) / _vars.dy, _vars.ip))
        if 0 <= r < _vars.rows and 0 <= c < _vars.cols:
            _vars.grid[r][c] = _set_color(marker, color, _vars.background)
    return _vars.grid

# it returns all the lines connecting the data points 
def _get_line(x, y): 
    x_line = []
    y_line = []
    for n in range(len(x) - 1):
        slope = 1. * (y[n + 1] - y[n]) / (x[n + 1] - x[n])
        dy = slope * _vars.dx
        x_line_n = _range(x[n], x[n + 1], _vars.dx)
        if dy == 0:
            y_line_n = [y[n]] * len(x_line_n)
        else:
            #y_line_n = _range(y[n], y[n + 1], dy)
            y_line_n = [(x_line_n[i]-x[n])*slope+y[n] for i in range(len(x_line_n))]
        x_line.extend(x_line_n)
        y_line.extend(y_line_n)
    return x_line, y_line

def _range(start, stop, step = 1):
    res = []
    i = start
    while i < stop:
        res.append(i)
        i = i+step
        #i=_round(i,14)
    return res

def _round(n, dec):
    return round(n * 10 ** dec) / 10 ** dec

def _add_yaxis():
    spacing = _vars.spacing[1] * _vars.ticks[1]
    axis = ["│" for r in range(_vars.rows)]
    dr = len(str(_vars.rows))
    ticks = [" " * dr for r in range(_vars.rows)]
    for r in range(_vars.rows):
        if spacing != 0 and r % spacing == 0:
            axis[r] = "├"
            space = " " * (dr - len(str(r)))
            ticks[r] = num_to_string(_vars.ymin + r * _vars.dy +   _vars.dy / 2) + space
            ticks[r] = str(r) + space
        axis[r] = _set_color(axis[r], _vars.axes_color, _vars.background)
        ticks[r] = _set_color(ticks[r], _vars.axes_color, _vars.background)
        if _vars.axes[1]:
            _vars.grid[r].append(axis[r]) 
        if _vars.ticks[1] * _vars.spacing[1]:
            _vars.grid[r].append(ticks[r])

def num_to_string(num):
    if abs(num) < 10 ** 5:
        num = str(round(num, 1))
    else:
        exp = len(str(abs(num))) - 1
        num = num / 10 ** exp
        num = str(num) + 'e' + str(exp)
    return num
            
def _add_xaxis():
    spacing = _vars.spacing[0] * _vars.ticks[0]
    axis = ["─" for r in range(_vars.cols)]
    ticks = [" " for r in range(_vars.cols)]
    final_spaces = " " * _vars.ticks[1] * len(str(_vars.rows))
    axis += "┘" * _vars.axes[1] + final_spaces
    ticks += " " * _vars.axes[1] + final_spaces
    c = 0
    while c < _vars.cols:
        dc = 1 
        if spacing != 0 and c % spacing == 0:
            new = list(num_to_string(_vars.xmin + c * _vars.dx +   _vars.dx / 2))
            new = list(str(c))
            dc = len(new)
            if c + dc <= _vars.cols :
                ticks[c : c + dc] = new
                axis[c : c + dc] = "┬" + "─" * (dc - 1)
        c += dc
    axis = [_set_color(el, _vars.axes_color, _vars.background) for el in axis]
    ticks = [_set_color(el, _vars.axes_color, _vars.background) for el in ticks]
    if _vars.axes[0]:
        _vars.grid.insert(0, axis) 
    if _vars.ticks[0] * _vars.spacing[0]:
        _vars.grid.insert(0, ticks) 

def _set_canvas():
    canvas = '\n'
    for r in range(len(_vars.grid) -1, -1, -1):
        canvas += "".join(_vars.grid[r]) + '\n'
    _vars.canvas = canvas[:-1]

def _add_equations():
    dx, dy = _add_spaces(_vars.dx, _vars.dy, _vars.decimals, True)
    cx, cy = _add_spaces(_vars.xmin + _vars.dx / 2, _vars.ymin + _vars.dy / 2, _vars.decimals)
    ex, ey = _add_spaces(_vars.dx / 2, _vars.dy / 2, _vars.decimals)
    x_eq = "x = " + dx + " × col " + cx + " " + chr(177) + " " + ex[2:]
    y_eq = "y = " + dy + " × row " + cy + " " + chr(177) + " " + ey[2:]
    final_spaces = " " * (_vars.cols + _vars.axes[1] + _vars.ticks[1] * len(str(_vars.rows)) - len(x_eq))
    x_eq =  '\n' + _set_color(x_eq + final_spaces, _vars.axes_color, _vars.background)
    y_eq =  '\n' + _set_color(y_eq + final_spaces, _vars.axes_color, _vars.background)
    if _vars.equations:
        _vars.canvas += x_eq + y_eq

def _add_spaces(a, b, decimals = 2, negative_only = False):
    a_round, b_round = _round_with_zeros(a, decimals), _round_with_zeros(b, decimals)
    space = int_length(a) - int_length(b)
    a = sign(a, negative_only) + ' ' * (0 - space) + a_round
    b = sign(b, negative_only) + ' ' * (0 + space) + b_round
    return a, b

def _round_with_zeros (num, decimals): #It rounds to the specified decimal points
    num = str(round(num, decimals))
    if decimals == 0:
        num = str(int(float(num_round)))
    floats = "0"
    if float(num) != int(float(num)):
        floats = num[num.index(".") + 1 : num.index(".") + 1 + decimals]
    zeros = "0" * (decimals-len(floats))
    return num + zeros

def sign(num, negative_only = False): # Similar to to str(numpy.sign)
    if num == 0:
        return "+ "
    elif num / abs(num) > 0:
        if negative_only:
            return ""
        else:
            return "+ "
    else:
        return "- "

def int_length(num):  
    return len(str(int(abs(float(num)))))

def _get_canvas():
    return _vars.canvas
    
def _print_canvas():
    canvas = _get_canvas()
    if _vars.no_color:
        canvas=_remove_color(canvas)
    _print(canvas+"\n")
    
def _remove_color(string):
    for color_code in _fg_color_codes + _bg_color_codes:
        string = string.replace('\x1b[' + str(color_code) + 'm', '')
    return string

##############################################
############     Docstrings     ##############
##############################################

scatter.__doc__ = """
It creates a scatter plot of coordinates given by x and y lists. Here is a basic example:

   \x1b[92mimport plotext as plx\x1b[0m
   \x1b[92mplx.scatter(x, y)\x1b[0m
   \x1b[92mplx.show()\x1b[0m

Optionally, a single y list could be provided. Multiple data set could be plotted with consecutive scatter functions. Here are all other parameters: 

\x1b[94mcols\x1b[0m
It sets the number of columns of the plot. Only integers are allowed. By default, it is set to the highest value allowed by the the terminal size. Alternatively you could set the number of rows using set_cols(cols) after the scatter function.

\x1b[94mrows\x1b[0m
It sets the number of rows of the plot. Only integers are allowed. By default, it is set to the highest value allowed by the the terminal size. Alternatively you could set the number of columns using set_rows(rows) after the scatter function.

\x1b[94mforce_size\x1b[0m
The plot dimensions are limited by the terminal size, when force_size is False and are allowed to be bigger otherwise. The default value is False. Alternatively you could set force_size using set_force_size(force_size) after the scatter function but before set_cols(cols) and set_rows(rows).

\x1b[94mxlim\x1b[0m
It sets the minimum and maximum limits of the plot in the x axis. It requires a list of two numbers, where the first sets the left (minimum) limit and the second the right (maximum) limit. If one or both values are not provided, they are calculated automatically. Alternatively you could use set_xlim(xlim) after the scatter function. 

\x1b[94mylim\x1b[0m
It sets the minimum and maximum limits of the plot in the y axis. It requires a list of two numbers, where the first sets the lower (minimum) limit and the second the upper (maximum) limit. If one or both values are not provided, they are calculated automatically. Alternatively you could use set_ylim(ylim) after the scatter function. 

\x1b[94mpoint\x1b[0m 
When True, the plot shows the scatter data points. The default value is True.

\x1b[94mpoint_marker\x1b[0m 
It sets the marker used to identify each data point on the plot. Only single characters are allowed (eg: '*'). The default value is '•'.

\x1b[94mpoint_color\x1b[0m
It sets the color used for the point marker. Use get_colors() to find the available color codes. The default value is 'norm'.

\x1b[94mline\x1b[0m
When True, the plot shows the lines between each data points. The default value is False.

\x1b[94mline_marker\x1b[0m 
It sets the marker used to identify the lines between data points. Only single characters are allowed (eg: '*'). The default value is '•'.

\x1b[94mline_color\x1b[0m
It sets the color used for the line marker. Use get_colors() to find the available color codes. The default value is 'norm'.

\x1b[94mbackground\x1b[0m
It sets the plot background color. Use get_colors() to find the available color codes. The default value is 'norm'. Alternatively you could set the background color using set_background(background) after the scatter function.

\x1b[94maxes\x1b[0m
When True, the x and y axes are added to the plot. A list of two Booleans will set the x and y axes separately (eg: axes=[True, False]). The default value is True. 

\x1b[94maxes_color\x1b[0m
It sets the color of the axes, ticks and equations, when present. Use get_colors() to find the available color codes. The default value is 'norm'. Alternatively you could set the axes color using set_axes_color(axes_color) after the scatter function.

\x1b[94mticks\x1b[0m
When True, the x and y ticks are added to the respective axes (even when absent). A list of two Booleans will set the x and y ticks separately (eg: ticks=[True, False]). The default value is True.

\x1b[94mspacing\x1b[0m
It sets the spacing between the x and y ticks. When a list of two numbers is given, the spacing of the x and y ticks are set separately (eg: spacing=[5, 8]). Only positive integers are allowed. The default value is [10, 5]. Alternatively you could use set_spacing(spacing) after the scatter function. 

\x1b[94mequations\x1b[0m
When True, the equations - needed to to find the real x and y values from the plot coordinates - are added at the end of the plot. The default value is False.

\x1b[94mdecimals\x1b[0m
It sets the number of decimal points shown in the equations. Only positive integers are allowed. The default value is 2. Alternatively you could set the decimal points using set_decimals(decimals) after the scatter function.
"""
 
plot.__doc__ = """
It is equivalent to the scatter function with the point option set to False and the line option set to True. See the scatter function docstring for further documentation. 

   \x1b[92mimport plotext as plx\x1b[0m
   \x1b[92mplx.scatter(x, y)\x1b[0m
   \x1b[92mplx.show()\x1b[0m
"""

show.__doc__ = """
It prints on terminal the plot created by the scatter or plot function. 
"""

clear_terminal.__doc__ = """
It clears the terminal. 
"""

clear_plot.__doc__ = """
It clears the plot canvas. 
"""

sleep.__doc__ = """
It adds a sleeping time to the computation and it is useful when plotting continuously updating data to remove screen flickering. An input of, for example, 0.01 would add approximately 0.01 secs to the computation. Manually tweak this value to reduce the flickering. 
"""

savefig.__doc__ = """
It saves the plot canvas (without colors) as a text file, at the file address provided as input. 
"""

get_colors.__doc__ = """
It shows the available color codes.
"""

get_version.__doc__ = """
It returns the version of current plotext package.
"""

get_x_from_col.__doc__ = """
It returns the estimated x value from the column in which it is plotted, provided as input. 
"""

get_y_from_row.__doc__ = """
It returns the estimated y value from the row in which it is plotted, provided as input. 
"""

run_test.__doc__ = """
It runs a simple test of the plotext package.
"""

if 'idlelib.run' in sys.modules:
    functions = [scatter, plot, show, clear_terminal, clear_plot, sleep, savefig, get_colors, get_version, get_x_from_col, get_y_from_row, run_test]
    for fun in functions:
        fun.__doc__ = _remove_color(fun.__doc__)

##############################################

if __name__=="__main__":
    pass
    #run_test()

    import matplotlib.pyplot as plt
    import numpy as np
    
    l1=3*10**10
    l2=3.0000000000001*10**10
    y=np.linspace(l1,l2,10)
    plt.cla()
    plt.plot(y)
    #plt.show(block=0)

    scatter(y, cols=170, rows=200, spacing=[2,1])
    for i in range(1):
        clear_terminal()
        show()

