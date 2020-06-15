# /usr/bin/env python3
# -*- coding: utf-8 -*-
from time import time, sleep
import numpy as np
import sys
import os
import platform
import struct

class holder():
    def __init__(self):
        self.colors=['norm','bold','gray','red','green', 'yellow','orange','blue','violet','cyan','inorm','igray','ired','igreen','iyellow','iorange','iblue','iviolet','icyan']
        self.color_codes=[0,1,2,91,92,93,33,94,95,96,7,100,41,42,103,43,44,45,106]

        self.axes=[True, True]
        self.axes_color="norm"
        self.ticks=[True, True]
        self.spacing=[10, 5]
        self.equations=True
        self.decimals=3

        self.cols_min=1
        self.rows_min=1
        self.cols_terminal=1
        self.rows_terminal=1
        self.cols_max=1
        self.rows_max=1
        self.cols=1
        self.rows=1
        
        self.x=[]
        self.y=[]
        self.length=0
        self.xmin=0
        self.xmax=0
        self.dx=0
        self.ymin=0
        self.ymax=0
        self.dy=0

        self.point=True
        self.point_marker="*"
        self.point_color="norm"
        self.line=True
        self.line_marker="*"
        self.line_color="norm"

        self.clear=False
        self.sleep=False
        self.xplot=[]
        self.yplot=[]
        self.grid=[[]]
        self.canvas=""

h=holder()

def scatter(*args, **kwargs):
    """
It builds the scatter plot of data points whose coordinates are given by the x and y lists. Optionally, a single y list can be provided. 
 - The option 'axes', when True, adds the x and y axes to the plot. A list of two Booleans sets the x and y axes separately (eg: axes=[True, False]). The default value is True. 
 - The option 'axes_color' sets the color of the axes, ticks and equations, when present. Access the 'get_colors' function for the available color codes. The default value is 'norm'.
 - The option 'ticks', when True, adds the x and y ticks to the respective axes (even when absent). A list of two Booleans will set the x and y ticks separately (eg: ticks=[True, False]). The default value is True.
 - The option 'spacing' sets the spacing between x and y ticks. When a list of two numbers is given, the spacing of the x and y ticks are set separately (eg: spacing=[5, 8]). Only positive integers are allowed. The default values are [10, 5]. 
 - The option 'equations', when True, adds at the end of the plot, the equations needed to to find the real x and y values from the plot coordinates. The default value is True.
 - The option 'decimals' sets the number of decimal points in the equations. Only positive integers are allowed. The default value is 3.
 - The option 'cols' sets the number of columns of the plot. Only integers are allowed. The default value is the highest allowed by the the terminal dimension. 
 - The option 'rows' sets the number of rows of the plot. Only integers are allowed. The default value is the highest allowed by the the terminal dimension. 
 - The option 'xlim' sets the minimum and maximum limits of the plot in the x axis. It requires a list of two numbers, where the first sets the left (minimum) limit and the second the right (maximum) limit. If one or both values are not provided, they are calculated automatically.  
 - The option 'ylim' sets the minimum and maximum limits of the plot in the x axis. It requires a list of two numbers, where the first sets the lower (minimum) limit and the second the upper (maximum) limit. If one or both values are not provided, they are calculated automatically. 
 - The option 'point', when True, plots the scatter data points. The default value is True.
 - The option 'point_marker' sets the marker used for the scatter plot of each data point. Only single characters are allowed (eg: '*'). The default value is "•".
 - The option 'point_color' sets the color of the scatter data points and of the plot background. Access the 'get_colors' function for the available color codes. The default value is 'norm'.
 - The option 'line', when True, plots straight lines between each data points. The default value is False.
 - The option 'line_marker' sets the marker used to plot the lines between each data point. Only single characters are allowed (eg: '*'). The default value is "•".
 - The option 'line_color' sets the color of the lines between each data point. Access the 'get_colors' function for the available color codes. The default value is 'norm'.
"""
    set_axes(kwargs.get("axes"))
    set_axes_color(kwargs.get("axes_color"))
    set_ticks(kwargs.get("ticks"))
    set_spacing(kwargs.get("spacing"))
    set_equations(kwargs.get("equations"))
    set_decimals(kwargs.get("decimals"))
    
    get_terminal_size()
    set_cols_max()
    set_rows_max()
    set_cols(kwargs.get("cols"))
    set_rows(kwargs.get("rows"))
    
    set_data(*args)
    set_xlim(kwargs.get("xlim"))
    set_ylim(kwargs.get("ylim"))
    
    set_point(kwargs.get("point"))
    set_point_marker(kwargs.get("point_marker"))
    set_point_color(kwargs.get("point_color"))
    set_line(kwargs.get("line"))
    set_line_marker(kwargs.get("line_marker"))
    set_line_color(kwargs.get("line_color"))

def plot(*args, axes=None, axes_color=None, ticks=None, spacing=None, equations=None, decimals=None, cols=None, rows=None, xlim=None, ylim=None, point=False, point_marker="*", point_color=None, line=True, line_marker=None, line_color=None):
    """
This is equivalent to the 'scatter' function with the 'point' option set to False, the 'point_marker' option set to '*' and the 'line' option set to True. See the 'scatter' function docstring for more documentation. """
    scatter(*args, axes=axes, ticks=ticks, axes_color=axes_color, spacing=spacing, equations=equations, decimals=decimals, cols=cols, rows=rows, xlim=xlim, ylim=ylim, point=point, point_marker=point_marker, point_color=point_color, line=line, line_marker=line_marker, line_color=line_color)

def show(clear=False, sleep=False):
    """
It prints the plot built by the 'scatter' or 'plot' functions. 
 - When the option 'clear' is set to True, the terminal is clear before the plot is printed. The default value is False.
 - When the option 'sleep' is True, the computation is paused for 0.01 secs after plotting. Optionally, the sleeping time (in secs) can passed directly (eg: sleep=0.001). The default value is False.
"""
    set_clear(clear)
    _apply_clear()
    _set_grid()
    _add_yaxis()
    _add_xaxis()
    _set_canvas()
    _add_equations()
    _print_canvas()
    set_sleep(sleep)
    _apply_sleep()

def get_colors():
    """It shows the available color codes."""
    colors=[set_color(h.colors[i], h.color_codes[i]) for i in range(len(h.colors))]
    print("\nThese are the available color codes, with normal background:", ", ".join(colors[:10]))
    print("Here are the available color codes, with inverted background:", ", ".join(colors[10:]))
    print("Eg: set_point_color('blue')")
    print("Eg: plot(x,y, axes_color='igreen')")

def set_color(text="", color="norm"):
    """It apply to the string provided with the option 'text' the color defined by the option color'. Access the 'get_colors' function for the available color codes. The default value is 'norm'."""
    code='\033['
    if type(color)==str:
        for c in range(len(h.colors)):
            if color==h.colors[c]:
                code+=str(h.color_codes[c])
    elif type(color)==int:
        code+=str(color)
    return code+'m'+text+'\033[0m'

def set_axes(axes=None):
    """When True is passed, it adds the x and y axes to the plot. A list of two Booleans sets the x and y axes separately (eg: axes=[True, False]). The default value is True."""
    if axes==None:
        h.axes=[True, True]
    elif type(axes)==list:
        h.axes=list(map(bool, axes))
    else:
        h.axes=[bool(axes), bool(axes)]
    return h.axes

def get_axes():
    """It returns the value set for the option 'axes' of the plot."""
    return h.axes

def set_axes_color(color=None):
    """It sets the color of the axes, ticks and equations, when present. Access the 'get_colors' function for the available color codes. The default value is 'norm'."""
    if color==None:
        h.axes_color="norm"
    else:
        h.axes_color=color
    return h.axes_color

def get_axes_color():
    """It returns the value set for the option 'axes_color' of the plot."""
    return h.axes_color

def set_ticks(ticks=None):
    """When True is passed, It adds the x and y ticks to the respective axes (even when absent). A list of two Booleans will set the x and y ticks separately (eg: ticks=[True, False]). The default value is True."""
    if ticks==None:
        h.ticks=[True, True]
    elif type(ticks)==list:
        h.ticks=list(map(bool, ticks))
    else:
        h.ticks=[bool(ticks), bool(ticks)]
    return h.ticks

def get_ticks():
    """It returns the value set for the option 'ticks' of the plot."""
    return h.ticks

def set_spacing(spacing=None):
    """It sets the spacing between x and y ticks. When a list of two numbers is given, the spacing of the x and y ticks are set separately (eg: spacing=[5, 8]). Only positive integers are allowed. The default values are [10, 5]."""
    if spacing==None:
        spacing=[10, 5]
    if type(spacing)==list:
        h.spacing=list(map(int, spacing))
    else:
        if spacing==0:
            spacing=1
        h.spacing=[int(spacing), int(spacing)]
    return h.spacing

def get_spacing():
    """It returns the value set for the option 'line_spacing'."""
    return h.spacing

def set_equations(equations=None):
    """When True is passed, it adds at the end of the plot, the equations needed to to find the real x and y values from the plot coordinates. The default value is True."""
    if equations==None:
        h.equations=True
    else:
        h.equations=equations
    return h.equations

def get_equations():
    """It returns the value set for the option 'equations'."""
    return h.equations

def set_decimals(decimals=None):
    """It sets the number of decimal points in the equations. Only positive integers are allowed. The default value is 3."""
    if decimals==None:
        h.decimals=3
    else:
        h.decimals=decimals
    return h.decimals

def get_decimals():
    """It returns the value set for the option 'decimals'."""
    return h.decimals

def _get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass

def get_terminal_size():
    if platform.system() == "Windows":
        h.cols_terminal,h.rows_terminal = _get_terminal_size_windows()
        h.cols_terminal -= 1
    else:
        """It returns the size of the terminal as number of column x number of rows."""
        h.rows_terminal, h.cols_terminal=map(int, os.popen('stty size', 'r').read().split())
    return h.cols_terminal, h.rows_terminal

def set_cols_max():
    """It sets the maximum number of column allowed for the plot depending on the terminal size."""
    h.cols_max=max(1, h.cols_terminal-2*h.ticks[1]-1*h.axes[1])
    return h.cols_max

def get_cols_max():
    """It returns the maximum number of column allowed for the plot depending on the terminal size."""
    return h.cols_max
    
def set_rows_max():
    """It sets the maximum number of rows allowed for the plot depending on the terminal size."""
    h.rows_max=max(1, h.rows_terminal-1*h.axes[0]-1*h.ticks[0]-2*h.equations-1)
    return h.rows_max

def get_rows_max():
    """It returns the maximum number of rows allowed for the plot depending on the terminal size."""
    return h.cols_max

def set_cols(cols=None):
    """It sets the number of columns of the plot. Only integers are allowed. The default value is the highest allowed by the the terminal dimension."""
    if type(cols)==float:
        cols=int(cols)
    if cols==None or cols>h.cols_max:
        h.cols=h.cols_max
    elif cols<h.cols_min:
        h.cols=h.cols_min
    else:
        h.cols=abs(int(cols))
    return h.cols

def get_cols():
    """It returns the number of columns of the plot."""
    return h.cols

def set_rows(rows=None):
    """The option 'rows' sets the number of rows of the plot. Only integers are allowed. The default value is the highest allowed by the the terminal dimension.""" 
    if type(rows)==float:
        rows=int(rows)
    if rows==None or rows>h.rows_max:
        h.rows=h.rows_max
    elif rows<h.rows_min:
        h.rows=h.rows_min
    else:
        h.rows=abs(int(rows))
    return h.rows

def get_rows():
    """It returns the number of rows of the plot."""
    return h.rows

def set_data(*args):
    """It set the x and y lists correspondent to the coordinates of the data points to be plotted. Optionally, a single y list can be provided."""
    h.x=h.y=[]
    if len(args)==0:
        h.x, h.y=[], []
    elif len(args)==1:
        h.y=args[0]
        h.x=range(len(h.y))
    else:
        h.x=args[0]
        h.y=args[1]
    h.length=min(len(h.x), len(h.y))
    if len(h.x)!=len(h.y):
        h.x=h.x[:h.length]
        h.y=h.y[:h.length]
    return h.x, h.y

def get_data():
    """It returns the x and y data points of the plot."""
    return h.x, h.y

def get_length():
    """It returns the length of the data."""
    return h.length

def _set_lim(data=[], dmin=None, dmax=None, bins=2):
    """It sets the limits of the plot of a list of data depending on the number of bins of the plot and whatever or not the limits are explicitly provided. It is used by the 'set_xlim' and 'set_ylim' functions."""
    bins_offset=0
    if dmin==None:
        bins_offset+=0.5
        if data==[]:
            d_min=0
        else:
            d_min=min(data)
    else:
        d_min=dmin
    if dmax==None:
        bins_offset+=0.5
        if data==[]:
            d_max=0
        else:
            d_max=max(data)
    else:
        d_max=dmax
    if bins==1:
        bins_offset=0.5
    if d_min==d_max:
        span=0.1*d_min
    else:
        span=(d_max-d_min)/(bins-bins_offset)
    minimum=d_min
    if dmin==None:
        minimum-=0.5*span
    maximum=d_max
    if dmax==None:
        maximum+=0.5*span
    return minimum, maximum

def set_xlim(xlim=None):
    """It sets the minimum and maximum limits of the plot in the x axis. The option 'xmin' sets the left (minimum) limit, while the 'xmax' value sets the right (maximum) limit. If one or both values are not provided, they are calculated automatically."""
    if xlim!=None:
        xmin, xmax=xlim
    else:
        xmin, xmax=None, None
    h.xmin, h.xmax=_set_lim(h.x, xmin, xmax, h.cols)
    h.dx=1.*(h.xmax-h.xmin)/h.cols
    return h.xmin, h.xmax

def get_xlim():
    """It returns the minimum and maximum limits of the plot in the x axis."""
    return h.ymin, h.ymax

def set_ylim(ylim=None):
    """It sets the minimum and maximum limits of the plot in the y axis. The option 'xmin' sets the lower (minimum) limit, while the 'xmax' value sets the upper (maximum) limit. If one or both values are not provided, they are calculated automatically."""
    if ylim!=None:
        ymin, ymax=ylim
    else:
        ymin, ymax=None, None
    h.ymin, h.ymax=_set_lim(h.y, ymin, ymax, h.rows)
    h.dy=1.*(h.ymax-h.ymin)/h.rows
    return h.ymin, h.ymax

def get_ylim():
    """It returns the minimum and maximum limits of the plot in the y axis."""
    return h.ymin, h.ymax

def set_point(point=True):
    """When True, it plots the scatter data points. The default value is True."""
    if point==None:
        h.point=True
    else:
        h.point=point
    return h.point

def get_point():
    """It returns the value set for the option 'point'."""
    return h.point

def set_point_marker(point_marker=None):
    """It sets the marker used for the scatter plot of each data point. Only single characters are allowed (eg: '*'). The default value is "•"."""
    if point_marker==None:
        h.point_marker="•"
    else:
        h.point_marker=point_marker[0]
    return h.point_marker

def get_point_marker():
    """It returns the marker used for the scatter plot of each data point."""
    return h.point_marker

def set_point_color(color=None):
    """It sets the color of the scatter data points and of the plot background. Access the 'get_colors' function for the available color codes. The default value is 'norm'."""
    if color==None:
        h.point_color="norm"
    else:
        h.point_color=color
    return h.point_color

def get_point_color():
    """It returns the color of the point marker and of the plot background."""
    return h.point_color

def set_line(line=None):
    """When True, it plots straight lines between each data points. The default value is False"""
    if line==None:
        h.line=False
    else:
        h.line=line
    return h.line

def get_line():
    """It returns the value set for the option 'line'."""
    return h.line

def set_line_marker(line_marker=None):
    """It sets the marker used to plot the lines between each data point. Only single characters are allowed (eg: '*'). The default value is "•"."""
    if line_marker==None:
        h.line_marker="•"
    else:
        h.line_marker=line_marker[0]
    return h.line_marker

def get_line_marker():
    """It returns the marker used to plot the lines between each data point."""
    return h.line_marker

def set_line_color(color=None):
    """It sets the color of the lines between each data point. Access the 'get_colors' function for the available color codes. The default value is 'norm'."""
    if color==None:
        h.line_color="norm"
    else:
        h.line_color=color
    return h.line_color

def get_line_color():
    """It returns the color of the marker used to plot the lines between each data point."""
    return h.line_color

def set_clear(clear=None):
    """It sets the option 'clear'. The default value is True."""
    if clear==None:
        h.clear=False
    else:
        h.clear=clear
    return h.clear

def _print(string):
    """It prints a string using an internal method."""
    sys.stdout.write(string)

def _apply_clear():
    """When the option clear is set to True, it clears the terminal."""
    if h.clear:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            _print('\033c')
    return h.clear

def set_sleep(sleep=False):
    """When the option 'sleep' is True, after plotting the computation is paused for 0.01 secs. Optionally, the sleeping time (in secs) can be fixed if a the number is passed (eg: sleep=0.001). The default value is False."""
    if sleep==False and type(sleep)==bool:
        h.sleep=None
    if sleep==True and type(sleep)==bool:
        h.sleep=0.01
    else:
        h.sleep=sleep
    return h.sleep

def get_sleep():
    """It returns the value of the option 'sleep'."""
    return h.sleep

def _apply_sleep():
    """It pauses the computation with a time defined by the 'sleep' option."""
    if h.sleep!=None:
        sleep(h.sleep)
    return h.sleep

def _get_line():
    """It returns the data correspondent to the lines between each data point."""
    x_line=[]
    y_line=[]
    for i in range(h.length-1):
        s=1.*(h.y[i+1]-h.y[i])/(h.x[i+1]-h.x[i])
        dy=s*h.dx
        x=np.arange(h.x[i], h.x[i+1], h.dx)
        if dy==0:
            y=[h.y[i]]*len(x)
        else:
            y=np.arange(h.y[i], h.y[i+1], dy)
        x_line.extend(x)
        y_line.extend(y)
    return x_line, y_line

def _add_to_grid(x, y, marker, color):
    """It adds data to the plot grid."""
    h.xplot=[]
    h.yplot=[]
    for i in range(len(x)):
        c=int((x[i] - h.xmin)/h.dx)
        r=int((y[i] - h.ymin)/h.dy)
        if 0<=r<h.rows and 0<=c<h.cols:
            h.xplot.append(c)
            h.yplot.append(r)
            h.grid[r][c]=set_color(marker, color)
    return h.grid

def _set_grid():
    """It sets the grid from the data to be plotted."""
    space=set_color(" ", h.point_color)
    h.grid=[[space for c in range(h.cols)] for r in range(h.rows)]
    if h.line:
        _add_to_grid(*_get_line(), h.line_marker, h.line_color)
    if h.point:
        _add_to_grid(h.x, h.y, h.point_marker, h.point_color)

def _add_xaxis():
    """It adds the x axis and x ticks to the plot grid"""
    if h.axes[0] or h.ticks[0]:
        x_axis=[]
        x_ticks=[]
        l=0
        while l<h.cols:
            if l%(h.spacing[0])==0:
                new=list(str(l))
                if l + len(new)<=h.cols:
                    x_ticks+=new
                    x_axis+=["┬"]+["─"]*(len(new)-1)
                else:
                    x_ticks+=[" "]*(h.cols-l)
                    x_axis+=["─"]*(h.cols-l)
            else:
                x_ticks+=[" "]
                x_axis+=["─"]
            l=len(x_ticks)
        if h.axes[1]:
            x_axis+="┘"
            x_ticks+=" "
        if h.ticks[1]:
            x_axis+=" "*len(str(h.rows))
            x_ticks+=" "*len(str(h.rows))
        x_axis=[set_color(x_axis[i], h.axes_color) for i in range(len(x_axis))]
        x_ticks=[set_color(x_ticks[i], h.axes_color) for i in range(len(x_ticks))]
    if h.axes[0]:
        h.grid.insert(0, x_axis)
    if h.ticks[0]:
        h.grid.insert(0, x_ticks)
    return 0

def _add_yaxis():
    """It adds the y axis and ticks to the canvas"""
    if h.axes[1]:
        bar="│"
        tick="├"
        y_axis=[tick  if (r%(h.spacing[1]))==0 else bar for r in range(h.rows)]
        y_axis=[set_color(y_axis[i], h.axes_color) for i in range(len(y_axis))]
        h.grid=[h.grid[r] + [y_axis[r]] for r in range(h.rows)]
    if h.ticks[1]:
        y_ticks=[str(r)+" "*(len(str(h.rows))-len(str(r))) if (r%(h.spacing[1]))==0 else " "*len(str(h.rows)) for r in range(h.rows)]
        y_ticks=[set_color(y_ticks[i], h.axes_color) for i in range(len(y_ticks))]
        h.grid=[h.grid[r] + [y_ticks[r]] for r in range(h.rows)]
    return 0

def _set_canvas():
    """It creates the plot canvas from the plot grid"""
    canvas=""
    for r in range(len(h.grid)-1,-1,-1):
        canvas+="".join(h.grid[r])+"\n"
    h.canvas=canvas[:-1]
    h.canvas=set_color(h.canvas, h.point_color)
    return "canvas set"

def _myround(num, decimals):
    """It rounds a number to the number of decimals defined by option 'decimals'."""
    num=str(np.round(float(num), decimals))
    floats=str(num)[num.index(".")+1: num.index(".")+1+decimals]
    zeros="0"*(decimals-len(floats))
    return num+zeros

def _add_spaces(num1, num2, sign=False):
    """It returns the two numbers in input with the correct number of spaces before to allign them."""
    spaces=len(str(int(abs(num2))))-len(str(int(abs(num1))))
    signature=lambda num: "+ " if np.sign(num)==1 else "- "
    num_1, num_2=" "*spaces+_myround(abs(num1), h.decimals), " "*(-spaces)+_myround(abs(num2), h.decimals)
    if sign:
        num_1, num_2=signature(num1)+num_1, signature(num2)+num_2
#    num_1+=" "*(len(num_2)-len(num_1))
#    num_2+=" "*(len(num_1)-len(num_2))
    return num_1, num_2

def _add_equations():
    """It adds equations at the bottom of the canvas useful to map the points in the canvas to real data"""
    if h.equations:
        mx, my=_add_spaces(h.dx, h.dy)
        cx, cy=_add_spaces(h.xmin+h.dx/2, h.ymin+h.dy/2, sign=True)
        err_x, err_y=_add_spaces(h.dx/2, h.dy/2)
        x_eq="x = "+mx+" × x-axis "+cx+" "+chr(177)+" "+err_x
        y_eq="y = "+my+" × y-axis "+cy+" "+chr(177)+" "+err_y
        x_eq+=" "*(h.cols+len(str(h.rows))*int(h.ticks[1])+int(h.axes[1])-len(x_eq))
        y_eq+=" "*(h.cols+len(str(h.rows))*int(h.ticks[1])+int(h.axes[1])-len(y_eq))
        h.canvas+=set_color("\n"+x_eq+"\n"+y_eq, h.axes_color)
    return "equations set"

def get_x_from_xaxis(col=0):
    """It returns the real x data value from the x value plotted. It requires the x coordinate into the 'col' option."""
    return 1.*h.dx * col + h.xmin + h.dx/2.

def get_y_from_yaxis(row=0):
    """It returns the real y data value from the y value plotted. It requires the y coordinate into the 'row' option."""
    return 1.*h.dy * row + h.ymin + h.dy/2.

def get_xy_from_plot(col=0, row=0):
    """It returns the real x and y data values from respectively the x and y values plotted. The x value must be passed to the 'col' option, while the y value to the 'row' option."""
    return get_x_from_xaxis(col), get_y_from_yaxis(row)

def _print_canvas():
    """It prints the final canvas"""
    if platform.system() == "Windows":
        h.canvas = escape_ansi(h.canvas)
    _print(h.canvas+"\n")
    #myprint("\n")
    return "canvas printed"

def escape_ansi(line):
    """It removes the ansi codes from a string."""
    import re
    ansi_escape=re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('',line)

def get_canvas(color=True):
    """It returns the plot canvas. If 'color' option is set to True (as by default), the canvas colors are preserved."""
    if color:
        return h.canvas
    else:
        return escape_ansi(h.canvas)

def savefig(file_name):
    """It saves the plot canvas. \nIt takes as input the file address where to write. \nIt returns a text file representing the colorless plot canvas."""
    text_file=open(file_name, "w+")
    if get_canvas()=="":
        print("Warning: the canvas is empty. Try using the 'show' function before saving.")
    text_file.write(get_canvas(False))
    text_file.close()
    print("Plot saved as", file_name)

def get_version():
    """It returns the version of 'plotext' as a string."""
    init_path="__init__.py"
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, init_path), 'r') as fp:
        lines=fp.read()
    for line in lines.splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        print("Unable to find version string.")
