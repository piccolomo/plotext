# /usr/bin/env python3
# -*- coding: utf-8 -*-

# This file contains all the main plotext functions available externally to the user

##############################################
###########    Initialisation    #############
##############################################

from plotext._figure import _figure_class
from time import sleep as _sleep
import plotext._global as _glob
from plotext import __version__
import plotext._utility as _ut
import plotext._doc as doc

_figure = _glob.figure # the main figure at top level (defined in _global.py because it is useful also there)

##############################################
#########    Subplots Functions    ###########
##############################################

def subplots(rows = None, cols = None):
    sub = _figure._active.subplots(rows, cols)
    _figure.show() if _figure._interactive else None
    return sub

def subplot(row = None, col = None):
    sub = _figure.subplot(row, col)
    _figure.show() if _figure._interactive else None
    return sub

def main():
    return _figure.main()

def active():
    return _figure._active

##############################################
#######    Outside Set Functions    ##########
##############################################

def interactive(interactive = None):
    _figure._set_interactive(interactive)

def plot_size(width = None, height = None):
    _figure._active.plot_size(width, height)
    _figure.show() if _figure._interactive else None
plotsize = plot_size

def limit_size(width = None, height = None):
    #_figure._master._set_size()
    _figure._master._limit_size(width, height)
limitsize = limit_size

def take_min():
    _figure._active.take_min()
takemin = take_min

def title(label):
    _figure._active.title(label)
    _figure.show() if _figure._interactive else None

def xlabel(label = None, xside = None):
    _figure._active.xlabel(label = label, xside = xside)
    _figure.show() if _figure._interactive else None

def ylabel(label = None, yside = None):
    _figure._active.ylabel(label = label, yside = yside)
    _figure.show() if _figure._interactive else None

def xlim(left = None, right = None, xside = None):
    _figure._active.xlim(left = left, right = right, xside = xside)
    _figure.show() if _figure._interactive else None

def ylim(lower = None, upper = None, yside = None):
    _figure._active.ylim(lower = lower, upper = upper, yside = yside)
    _figure.show() if _figure._interactive else None

def xscale(scale = None, xside = None):
    _figure._active.xscale(scale = scale, xside = xside)
    _figure.show() if _figure._interactive else None

def yscale(scale = None, yside = None):
    _figure._active.yscale(scale = scale, yside = yside)
    _figure.show() if _figure._interactive else None

def xticks(ticks = None, labels = None, xside = None):
    _figure._active.xticks(ticks = ticks, labels = labels, xside = xside)
    _figure.show() if _figure._interactive else None

def yticks(ticks = None, labels = None, yside = None):
    _figure._active.yticks(ticks = ticks, labels = labels, yside = yside)
    _figure.show() if _figure._interactive else None

def xfrequency(frequency = None, xside = None):
    _figure._active.xfrequency(frequency = frequency, xside = xside)
    _figure.show() if _figure._interactive else None

def yfrequency(frequency = None, yside = None):
    _figure._active.yfrequency(frequency = frequency, yside = yside)
    _figure.show() if _figure._interactive else None

def xreverse(reverse = None, xside = None):
    _figure._active.xreverse(reverse = reverse, xside = xside)
    _figure.show() if _figure._interactive else None

def yreverse(reverse = None, yside = None):
    _figure._active.yreverse(reverse = reverse, yside = yside)
    _figure.show() if _figure._interactive else None

def xaxes(lower = None, upper = None):
    _figure._active.xaxes(lower = lower, upper = upper)
    _figure.show() if _figure._interactive else None

def yaxes(left = None, right = None):
    _figure._active.yaxes(left = left, right = right)
    _figure.show() if _figure._interactive else None

def frame(frame = None):
    _figure._active.frame(frame = frame)
    _figure.show() if _figure._interactive else None

def grid(horizontal = None, vertical = None):
    _figure._active.grid(horizontal = horizontal, vertical = vertical)
    _figure.show() if _figure._interactive else None

def canvas_color(color = None):
    _figure._active.canvas_color(color)
    _figure.show() if _figure._interactive else None

def axes_color(color = None):
    _figure._active.axes_color(color)
    _figure.show() if _figure._interactive else None

def ticks_color(color = None):
    _figure._active.ticks_color(color)
    _figure.show() if _figure._interactive else None

def ticks_style(style = None):
    _figure._active.ticks_style(style)
    _figure.show() if _figure._interactive else None

def theme(theme = None):
    _figure._active.theme(theme)
    _figure.show() if _figure._interactive else None

##############################################
###########    Clear Functions    ############
##############################################

def clear_figure(): 
    _figure._active.clear_figure()
    _figure.show() if _figure._interactive else None
clf = clear_figure

def clear_data(): 
    _figure._active.clear_data()
    _figure.show() if _figure._interactive else None
cld = clear_data

def clear_color(): 
    _figure._active.clear_color()
    _figure.show() if _figure._interactive else None
clc = clear_color

def clear_terminal(lines = None):
    _figure._active.clear_terminal(lines = lines)
clt = clear_terminal

##############################################
######    Main Plotting Functions    #########
##############################################

def scatter(*args, xside = None, yside = None, marker = None, color = None, style = None, fillx = None, filly = None, label = None):
    _figure._active.scatter(*args, xside = xside, yside = yside, marker = marker, color = color, style = style, fillx = fillx, filly = filly, label = label)
    _figure.show() if _figure._interactive else None

def plot(*args, xside = None, yside = None, marker = None, color = None, style = None, fillx = None, filly = None, label = None):
    _figure._active.plot(*args, xside = xside, yside = yside, marker = marker, color = color,  fillx = fillx, filly = filly, label = label)
    _figure.show() if _figure._interactive else None

def candlestick(dates, data, xside = None, yside = None, orientation = None, colors = None, label = None):
    _figure._active.candlestick(dates, data, xside = xside, yside = yside, orientation = orientation, colors = colors, label = label)
    _figure.show() if _figure._interactive else None

def bar(*args, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None, reset_ticks = None):
    _figure._active.bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum, reset_ticks = reset_ticks)
    _figure.show() if _figure._interactive else None

def simple_bar(*args, width = None, marker = None, color = None, title = None, bar_texts = None):
    _glob.simple_bar(*args, width = width, marker = marker, color = color, title = title, bar_texts = bar_texts)
    _figure.show() if _figure._interactive else None

def multiple_bar(*args, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None, reset_ticks = None, bar_texts = None):
    _figure._active.multiple_bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum, reset_ticks = reset_ticks, bar_texts = bar_texts)
    _figure.show() if _figure._interactive else None

def simple_multiple_bar(*args, width = None, marker = None, colors = None, title = None, labels = None, bar_texts = None):
    _glob.simple_multiple_bar(*args, width = width, marker = marker, colors = colors, title = title, labels = labels, bar_texts = bar_texts)
    _figure.show() if _figure._interactive else None

def stacked_bar( *args, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None, reset_ticks = None):
    _figure._active.stacked_bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum, reset_ticks = reset_ticks)
    _figure.show() if _figure._interactive else None

def simple_stacked_bar(*args, width = None, marker = None, colors = None, title = None, labels = None, bar_texts = None):
    _glob.simple_stacked_bar(*args, width = width, marker = marker, colors = colors, title = title, labels = labels, bar_texts = bar_texts)
    _figure.show() if _figure._interactive else None

def hist(data, bins = None, norm = None, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None):
    _figure._active.hist(data, bins = bins, norm = norm, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum)
    _figure.show() if _figure._interactive else None

##############################################
###########    Plotting Tools    #############
##############################################

def error(*args, xerr = None, yerr = None, xside = None, yside = None, color = None, label = None):
    _figure.error(*args, xerr = xerr, yerr = yerr, xside = xside, yside = yside, color = color, label = label)
    _figure.show() if _figure._interactive else None

def event_plot(data, orientation = None, marker = None, color = None, side = None):
    _figure._active.event_plot(data, orientation = orientation, marker = marker, color = color, side = side)
    _figure.show() if _figure._interactive else None

eventplot = event_plot

def vertical_line(coordinate, color = None, xside = None):
    _figure._active.vertical_line(coordinate, color = color, xside = xside)
    _figure.show() if _figure._interactive else None
vline = vertical_line

def horizontal_line(coordinate, color = None, yside = None):
    _figure._active.horizontal_line(coordinate, color = color, yside = yside)
    _figure.show() if _figure._interactive else None
hline = horizontal_line

def text(text, x, y, xside = None, yside = None, color = None, background = None, style = None, orientation = None, alignment = None):
    _figure._active.text(text, x, y, xside = xside, yside = yside, color = color, background = background, style = style, orientation = orientation, alignment = alignment)
    _figure.show() if _figure._interactive else None

def rectangle(x = None, y = None, xside = None, yside = None, lines = None, marker = None, color = None, fill = None, label = None):
    _figure._active.rectangle(x = x, y = y, xside = xside, yside = yside, lines = lines, marker = marker, color = color, fill = fill, label = label)
    _figure.show() if _figure._interactive else None
    
def polygon(x = None, y = None, radius = None, sides = None, xside = None, yside = None, lines = None, marker = None, color = None, fill = None, label = None):
    _figure._active.polygon(x = x, y = y, radius = radius, sides = sides, xside = xside, yside = yside, lines = lines, marker = marker, color = color, fill = fill, label = label)
    _figure.show() if _figure._interactive else None

def confusion_matrix(actual, predicted, labels = None, color = None, style = None):
    _figure._active.confusion_matrix(actual, predicted, labels = labels, color = color, style = style)
    _figure.show() if _figure._interactive else None

cmatrix = confusion_matrix

def indicator(value, label = None, trend = None, color = None, style = None):
    _figure._active.indicator(value, label = label, trend = trend, color = color, style = style)
    _figure.show() if _figure._interactive else None

##############################################
##############    2D Plots    ################
############################################## 
    
def matrix_plot(matrix, marker = None, style = None, fast = False):
    _figure._active.matrix_plot(matrix, marker = marker, style = style, fast = fast)
    _figure.show() if _figure._interactive else None

def image_plot(path, marker = None, style = None, grayscale = False, fast = False):
    _figure._active.image_plot(path, marker = marker, style = style, grayscale = grayscale, fast = fast)
    _figure.show() if _figure._interactive else None
    
def play_gif(path):
    _glob.play_gif(path)
    _figure.show() if _figure._interactive else None

def play_video(path, from_youtube = False):
    _glob.play_video(path, from_youtube)
    _figure.show() if _figure._interactive else None

def play_youtube(url):
    _glob.play_youtube(url)
    _figure.show() if _figure._interactive else None

def get_youtube(url, path = None, log = True):
    return _glob.get_youtube(url, path, log)

##############################################
##########    Build Functions    #############
##############################################

def show():
    _figure.show()

def build():
    return _figure.build()

def sleep(time = 0):
    _sleep(time)

def time(show = True):
    return _figure._get_time(show)

def save_fig(path = None, append = False, keep_colors = False):
    _figure.save_fig(path, append, keep_colors)
savefig = save_fig

def from_matplotlib(fig, marker = None):
    return _glob.from_matplotlib(fig, marker = marker)

##############################################
##########     Date Functions    #############
##############################################

def date_form(input_form = None, output_form = None):
    _figure._active.date_form(input_form, output_form)
    
def set_time0(string, input_form = None):
    return _figure._active.set_time0(string, input_form = input_form)

def today_datetime():
    return _figure._active.today_datetime()

def today_string(output_form = None):
    return _figure._active.today_string(output_form)

def datetime_to_string(datetimes, output_form = None):
    return _figure._active.datetime_to_string(datetimes, output_form = output_form)

def datetimes_to_string(datetimes, output_form = None):
    return _figure._active.datetimes_to_string(datetimes, output_form = output_form)

def string_to_datetime(string, input_form = None):
    return _figure._active.string_to_datetime(string, input_form = input_form)

def string_to_time(string, input_form = None):##########ADD DOC############
    return _figure._active.string_to_time(string, input_form = input_form)

def strings_to_time(string, input_form = None):##########ADD DOC############
    return _figure._active.strings_to_time(string, input_form = input_form)

##############################################
##########     File Functions    ############
##############################################

script_folder = _ut.script_folder

def parent_folder(path, level = 1):
    return _ut.parent_folder(path, level = level)

def join_paths(*args):
    return _ut.join_paths(*args)

def save_text(text, path, log = True):
    return _ut.save_text(text, path, log = log)

def read_data(path, delimiter = None, columns = None, skip_rows = 0):
    return _ut.read_data(path, delimiter = delimiter, columns = columns, skip_rows = skip_rows)

def write_data(data, path, delimiter = None, columns = None, log = True):
    return _ut.write_data(data, path, delimiter = delimiter, columns = columns, log = log)

def download(url, path, log = True):
    return _ut.download(url, path, log)

def delete_file(path, log = True):
    return _ut.delete_file(path, log = log)

test_data_url     =  _glob.test_data_url
test_bar_data_url =  _glob.test_bar_data_url
test_image_url    =  _glob.test_image_url
test_gif_url      =  _glob.test_gif_url
test_video_url    =  _glob.test_video_url
test_youtube_url  =  _glob.test_youtube_url

##############################################
##########     Other Functions    ############
##############################################

def colorize(string, fullground = None, style = None, background = None, show = False):
    return _ut.colorize(string, fullground = fullground, style = style, background = background, show = show)

def uncolorize(string):
    return _ut.uncolorize(string)

terminal_size = _ut.terminal_size
ts = terminal_size

terminal_width = _ut.terminal_width
tw = terminal_width

terminal_height = _ut.terminal_height
th = terminal_height

def sin(periods = 2, length = 200, amplitude = 1, phase = 0, decay = 0):
    return _ut.sin(periods = periods, length = length, amplitude = amplitude, phase = phase, decay = decay)

def square(periods = 2, length = 200, amplitude = 1):
    return _ut.square(periods = periods, length = length, amplitude = amplitude)

def transpose(data):
    return _ut.transpose(data)

colors = _glob.colors

styles = _glob.styles

markers = _glob.markers

themes = _glob.themes

test = _glob.test

version = __version__

platform = _ut.platform
        
##############################################
############     Docstrings    ###############
##############################################        

subplots.__doc__ = doc._subplots
subplot.__doc__ = doc._subplot
main.__doc__ = doc._main
active.__doc__ = doc._active

interactive.__doc__ = doc._interactive
plot_size.__doc__ = doc._plot_size
limit_size.__doc__ = doc._limit_size
take_min.__doc__ = doc._take_min

title.__doc__ = doc._title
xlabel.__doc__ = doc._xlabel
ylabel.__doc__ = doc._ylabel
xlim.__doc__ = doc._xlim
ylim.__doc__ = doc._ylim
xscale.__doc__ = doc._xscale
yscale.__doc__ = doc._yscale
xticks.__doc__ = doc._xticks
yticks.__doc__ = doc._yticks
xfrequency.__doc__ = doc._xfrequency
yfrequency.__doc__ = doc._yfrequency
xreverse.__doc__ = doc._xreverse
yreverse.__doc__ = doc._yreverse
xaxes.__doc__ = doc._xaxes
yaxes.__doc__ = doc._yaxes
frame.__doc__ = doc._frame
grid.__doc__ = doc._grid
canvas_color.__doc__ = doc._canvas_color
axes_color.__doc__ = doc._axes_color
ticks_color.__doc__ = doc._ticks_color
ticks_style.__doc__ = doc._ticks_style
theme.__doc__ = doc._theme

clear_figure.__doc__ = doc._clear_figure
clear_data.__doc__ = doc._clear_data
clear_color.__doc__ = doc._clear_color
clear_terminal.__doc__ = doc._clear_terminal

scatter.__doc__ = doc._scatter
plot.__doc__ = doc._plot
candlestick.__doc__ = doc._candlestick
bar.__doc__ = doc._bar
simple_bar.__doc__ = doc._simple_bar
multiple_bar.__doc__ = doc._multiple_bar
simple_multiple_bar.__doc__ = doc._simple_multiple_bar
stacked_bar.__doc__ = doc._stacked_bar
simple_stacked_bar.__doc__ = doc._simple_stacked_bar
simple_bar.__doc__ = doc._simple_bar
hist.__doc__ = doc._hist

error.__doc__ = doc._error
event_plot.__doc__ = doc._event_plot
vertical_line.__doc__ = doc._vertical_line
horizontal_line.__doc__ = doc._horizontal_line
text.__doc__ = doc._text
rectangle.__doc__ = doc.rectangle
polygon.__doc__ = doc.polygon
confusion_matrix.__doc__ = doc.confusion_matrix
indicator.__doc__ = doc.indicator

matrix_plot.__doc__ = doc._matrix_plot
image_plot.__doc__ = doc._image_plot

play_gif.__doc__ = doc._play_gif
play_video.__doc__ = doc._play_video
play_youtube.__doc__ = doc._play_youtube
get_youtube.__doc__ = doc._get_youtube

show.__doc__ = doc._show
build.__doc__ = doc._build
sleep.__doc__ = doc._sleep
time.__doc__ = doc._time
save_fig.__doc__ = doc._save_fig
from_matplotlib.__doc__ = doc._from_matplotlib

date_form.__doc__ = doc._date_form
set_time0.__doc__ = doc._set_time0
today_datetime.__doc__ = doc._today_datetime
today_string.__doc__ = doc._today_string
datetime_to_string.__doc__ = doc._datetime_to_string
datetimes_to_string.__doc__ = doc._datetimes_to_string
string_to_datetime.__doc__ = doc._string_to_datetime

script_folder.__doc__ = doc._script_folder
parent_folder.__doc__ = doc._parent_folder
join_paths.__doc__ = doc._join_paths
save_text.__doc__ = doc._save_text
read_data.__doc__ = doc._read_data
write_data.__doc__ = doc._write_data
download.__doc__ = doc._download
delete_file.__doc__ = doc._delete_file

colorize.__doc__ = doc._colorize
uncolorize.__doc__ = doc._uncolorize
terminal_size.__doc__ = doc._terminal_size
terminal_width.__doc__ = doc._terminal_width
terminal_height.__doc__ = doc._terminal_height
sin.__doc__ = doc._sin
square.__doc__ = doc._square
transpose.__doc__ = doc._transpose

colors.__doc__ = doc._colors
styles.__doc__ = doc._styles
markers.__doc__ = doc._markers
themes.__doc__ = doc._themes
test.__doc__ = doc.test
