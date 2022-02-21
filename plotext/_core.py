# /usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################
###########    Initialization    #############
##############################################

from plotext._utility.plot import terminal_size as _terminal_size
from plotext._utility.color import uncolorize as _uncolorize
from plotext._utility.color import colorize as _colorize
from plotext._utility.color import colors as _colors
from plotext._utility.marker import markers as _markers
from plotext._utility.platform import version as _version
from plotext._figure import figure_class as _figure_class
from plotext._utility.data import set_data as _set_data
from plotext._subplot import datetime as _datetime
from plotext._utility.data import sleep as _sleep
from plotext._utility.platform import _platform as platform 
from plotext._utility.data import sin as _sin
from plotext._utility.data import linspace
from plotext._utility import doc
import plotext._utility.file as file

##############################################
#########    Initialize Figure    ############
##############################################

figure = _figure_class()

##############################################
#########    Subplots Functions    ###########
##############################################

subplots = figure.set_subplots

subplot = figure.set_subplot

##############################################
###########    Clear Functions    ############
##############################################

clear_figure = figure.clear_figure
clf = clear_figure

colorless = figure.colorless
cls = colorless

clear_plot = figure.clear_plot
clp = clear_plot

clear_data = figure.clear_data
cld = clear_data

clear_color = figure.clear_color
clc = clear_color

clear_terminal = figure.clear_terminal
clt = clear_terminal

##############################################
#######    Outside Set Functions    ##########
##############################################

plot_size = figure.plot_size
plotsize = plot_size

limit_size = figure.limitsize
limitsize = limit_size

span = figure.span

title = figure.title
xlabel = figure.xlabel
ylabel = figure.ylabel

xaxis = figure.xaxis
yaxis = figure.yaxis
frame = figure.frame

grid = figure.grid

canvas_color = figure.canvas_color
ticks_color = figure.ticks_color
axes_color = figure.axes_color

xlim = figure.xlim
ylim = figure.ylim

xscale = figure.xscale
yscale = figure.yscale

xfrequency = figure.xfrequency
yfrequency = figure.yfrequency

xticks = figure.xticks
yticks = figure.yticks

##############################################
######    Main Plotting Functions    #########
##############################################

def scatter(*args,
    xside = None,
    yside = None,
    marker = None,
    color = None,
    fillx = None,
    filly = None,
    label = None):
    figure.subplot.draw(*args,
    xside = xside, 
    yside = yside,
    lines = False,
    marker = marker,
    color = color,
    fillx = fillx,
    filly = filly,
    label = label)

def plot(*args,
    xside = None,
    yside = None,
    marker = None,
    color = None,
    fillx = None,
    filly = None,
    label = None):
    figure.subplot.draw(*args,
    xside = xside, 
    yside = yside,
    lines = True,
    marker = marker,
    color = color,
    fillx = fillx,
    filly = filly,
    label = label)

build = figure.build
show = figure.show

##############################################
########     DateTime Functions    ###########
##############################################

datetime = _datetime # to make it explicit

def scatter_date(x, y,
    xside = None,
    yside = None,
    marker = None,
    color = None,
    fillx = None,
    filly = None,
    label = None):
    figure.subplot.draw_date(x, y,
    xside = xside, 
    yside = yside,
    lines = False,
    marker = marker,
    color = color,
    fillx = fillx,
    filly = filly,
    label = label)
    
def plot_date(x, y,
    xside = None,
    yside = None,
    marker = None,
    color = None,
    fillx = None,
    filly = None,
    label = None):
    figure.subplot.draw_date(x, y,
    xside = xside, 
    yside = yside,
    lines = True,
    marker = marker,
    color = color,
    fillx = fillx,
    filly = filly,
    label = label)

##############################################
###########     Bar Functions    #############
##############################################

def bar(x, y,
    xside = None, 
    yside = None,
    marker = None,
    color = None,
    fill = None,
    width = None,
    orientation = None,
    label = None,
    minimum = None):
    figure.subplot.draw_single_bar(x, y,
    xside = xside, 
    yside = yside,
    marker = marker,
    color = color,
    fill = fill,
    width = width,
    orientation = orientation,
    label = label,
    minimum = minimum)

def multiple_bar(x, y,
    xside = None, 
    yside = None,
    marker = None,
    color = None,
    fill = None,
    width = None,
    orientation = None,
    label = None,
    minimum = None):
    figure.subplot.draw_multiple_bar(x, y,
    xside = xside, 
    yside = yside,
    marker = marker,
    color = color,
    fill = fill,
    width = width,
    orientation = orientation,
    label = label,
    minimum = minimum)

def stacked_bar(x, y,
    xside = None, 
    yside = None,
    marker = None,
    color = None,
    fill = None,
    width = None,
    orientation = None,
    label = None,
    minimum = None):
    figure.subplot.draw_stacked_bar(x, y,
    xside = xside, 
    yside = yside,
    marker = marker,
    color = color,
    fill = fill,
    width = width,
    orientation = orientation,
    label = label,
    minimum = minimum)

def hist(data,
    bins = None,
    width = None,
    norm = False,
    yside = None,
    xside = None,
    marker = None,
    color = None,
    fill = True,
    orientation = None,
    label = None):
    figure.subplot.draw_hist(data,
    bins = bins,
    width = width,
    norm = norm,
    xside = xside,
    yside = yside,
    marker = marker,
    color = color,
    fill = fill,
    orientation = orientation,
    label = label)

##############################################
######     Matrix/Image Functions    #########
##############################################

def matrix_plot(matrix,
    yside = None,
    xside = None,
    marker = None):
    figure.subplot.draw_matrix(
    matrix = matrix,
    xside = xside,
    yside = yside,
    marker = marker)

def image_plot(path,
    size = [None, None],
    marker = None,
    grayscale = False,
    keep_ratio = False,
    resample = True):
    return figure.subplot.draw_image(path,
    size = size,
    marker = marker,
    grayscale = grayscale,
    keep_ratio = keep_ratio,
    resample = resample)
    
##############################################
#############     Line Plot    ###############
##############################################

def vertical_line(coordinate,
    xside = None,
    color = None):
    figure.subplot.draw_vertical_line(
    coordinate = coordinate,
    xside = xside,
    color = color)

def horizontal_line(coordinate,
    yside = None,
    color = None):
    figure.subplot.draw_horizontal_line(
    coordinate = coordinate,
    yside = yside,
    color = color)

##############################################
##########     Other Functions    ############
##############################################

save_fig = figure.save_fig
savefig = save_fig

terminal_size = _terminal_size # to make it explicit

markers = _markers

colors = _colors

sleep = _sleep  

time = figure.get_time

sin = _sin 

colorize = _colorize

uncolorize = _uncolorize

version = _version

##############################################
############     Docstrings    ###############
##############################################        

figure.__doc__ = doc._figure

subplots.__func__.__doc__ = doc._subplots
subplot.__func__.__doc__ = doc._subplot

clear_figure.__func__.__doc__ = doc._clear_figure
colorless.__func__.__doc__ = doc._colorless
clear_plot.__func__.__doc__ = doc._clear_plot
clear_data.__func__.__doc__ = doc._clear_data
clear_color.__func__.__doc__ = doc._clear_color
clear_terminal.__func__.__doc__ = doc._clear_terminal

plot_size.__func__.__doc__ = doc._plot_size
limit_size.__func__.__doc__ = doc._limit_size
span.__func__.__doc__ = doc._span

title.__func__.__doc__ = doc._title

xlabel.__func__.__doc__ = doc._xlabel
ylabel.__func__.__doc__ = doc._ylabel

xaxis.__func__.__doc__ = doc._xaxis
yaxis.__func__.__doc__ = doc._yaxis
frame.__func__.__doc__ = doc._frame

grid.__func__.__doc__ = doc._grid

canvas_color.__func__.__doc__ = doc._canvas_color
ticks_color.__func__.__doc__ = doc._ticks_color
axes_color.__func__.__doc__ = doc._axes_color

xlim.__func__.__doc__ = doc._xlim
ylim.__func__.__doc__ = doc._ylim

xscale.__func__.__doc__ = doc._xscale
yscale.__func__.__doc__ = doc._yscale

xfrequency.__func__.__doc__ = doc._xfrequency
yfrequency.__func__.__doc__ = doc._yfrequency

xticks.__func__.__doc__ = doc._xticks
yticks.__func__.__doc__ = doc._yticks

scatter.__doc__ = doc._scatter
plot.__doc__ = doc._plot

build.__func__.__doc__ = doc._build
show.__func__.__doc__ = doc._show

datetime.__doc__ = doc._datetime
datetime.today.__doc__ = doc._today
datetime.set_time0.__func__.__doc__ = doc._set_time0
datetime.set_datetime_form.__func__.__doc__ = doc._set_datetime_form
datetime.clear.__func__.__doc__ = doc._clear
datetime.string_to_datetime.__func__.__doc__ = doc._string_to_datetime
datetime.datetime_to_timestamp.__func__.__doc__ = doc._datetime_to_timestamp
datetime.string_to_timestamp.__func__.__doc__ = doc._string_to_timestamp
datetime.datetime_to_string.__func__.__doc__ = doc._datetime_to_string

scatter_date.__doc__ = doc._scatter_date
plot_date.__doc__ = doc._plot_date

bar.__doc__ = doc._bar
multiple_bar.__doc__ = doc._multiple_bar
stacked_bar.__doc__ = doc._stacked_bar
hist.__doc__ = doc._hist

matrix_plot.__doc__ = doc._matrix_plot
image_plot.__doc__ = doc._image_plot

file.__doc__ = doc._file
file.parent_folder.__doc__ = doc._parent_folder
file.script_folder.__doc__ = doc._script_folder
file.join_paths.__doc__ = doc._join_paths
file.save_text.__doc__ = doc._save_text
file.read_data.__doc__ = doc._read_data
file.write_data.__doc__ = doc._write_data

save_fig.__func__.__doc__ = doc._save_fig
terminal_size.__doc__ = doc._terminal_size
markers.__doc__ = doc._markers
colors.__doc__ = doc._colors
sleep.__doc__ = doc._sleep
time.__func__.__doc__ = doc._time
sin.__doc__ = doc._sin
colorize.__doc__ = doc._colorize
uncolorize.__doc__ = doc._uncolorize
version.__doc__ = doc._version
