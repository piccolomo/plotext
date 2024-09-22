# /usr/bin/env python3
# -*- coding: utf-8 -*-

# This file contains all the main plotext functions available externally to the user

##############################################
###########    Initialisation    #############
##############################################

import plotext._doc
from plotext._doc_utils import documentation as doc
from plotext._doc_utils import add

from ._figure import _figure_class
from time import sleep as _sleep
import plotext._global as _glob
from plotext import __version__
import plotext._utility as _ut

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
    size = _figure._active.plot_size(width, height)
    _figure.show() if _figure._interactive else None
    return size
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

def scatter(*args, marker = None, color = None, style = None, fillx = None, filly = None, xside = None, yside = None, label = None):
    _figure._active.scatter(*args, xside = xside, yside = yside, marker = marker, color = color, style = style, fillx = fillx, filly = filly, label = label)
    _figure.show() if _figure._interactive else None

def plot(*args, marker = None, color = None, style = None, fillx = None, filly = None, xside = None, yside = None, label = None):
    _figure._active.plot(*args, xside = xside, yside = yside, marker = marker, color = color,  fillx = fillx, filly = filly, label = label)
    _figure.show() if _figure._interactive else None

def candlestick(dates, data, xside = None, yside = None, orientation = None, colors = None, label = None):
    _figure._active.candlestick(dates, data, xside = xside, yside = yside, orientation = orientation, colors = colors, label = label)
    _figure.show() if _figure._interactive else None

def bar(*args, marker = None, color = None, fill = None, width = None, orientation = None, minimum = None, reset_ticks = None, xside = None, yside = None, label = None):
    _figure._active.bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum, reset_ticks = reset_ticks)
    _figure.show() if _figure._interactive else None

def simple_bar(*args, marker = None, color = None, title = None, width = None):
    _glob.simple_bar(*args, width = width, marker = marker, color = color, title = title)
    _figure.show() if _figure._interactive else None

def multiple_bar(*args, marker = None, color = None, fill = None, width = None, orientation = None, minimum = None, reset_ticks = None, xside = None, yside = None, labels = None):
    _figure._active.multiple_bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, labels = labels, minimum = minimum, reset_ticks = reset_ticks)
    _figure.show() if _figure._interactive else None

def simple_multiple_bar(*args, marker = None, colors = None, title = None, width = None, labels = None):
    _glob.simple_multiple_bar(*args, width = width, marker = marker, colors = colors, title = title, labels = labels)
    _figure.show() if _figure._interactive else None

def stacked_bar(*args, marker = None, color = None, fill = None, width = None, orientation = None, minimum = None, reset_ticks = None, xside = None, yside = None, labels = None):
    _figure._active.stacked_bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, labels = labels, minimum = minimum, reset_ticks = reset_ticks)
    _figure.show() if _figure._interactive else None

def simple_stacked_bar(*args, marker = None, colors = None, title = None, width = None, labels = None):
    _glob.simple_stacked_bar(*args, width = width, marker = marker, colors = colors, title = title, labels = labels)
    _figure.show() if _figure._interactive else None

def hist(data, bins = None, marker = None, color = None, fill = None, norm = None, width = None, orientation = None, minimum = None, xside = None, yside = None, label = None):
    _figure._active.hist(data, bins = bins, norm = norm, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum)
    _figure.show() if _figure._interactive else None

def candlestick(dates, data, colors = None, orientation = None, xside = None, yside = None, label = None):
    _figure._active.candlestick(dates, data, xside = xside, yside = yside, orientation = orientation, colors = colors, label = label)
    _figure.show() if _figure._interactive else None

def box(*args, quintuples = None, colors = None,  fill = None, width = None, orientation = None, minimum = None, reset_ticks = None, xside = None, yside = None, label = None):
    _figure._active.box(*args, xside = xside, yside = yside, orientation = orientation, colors = colors, label = label, fill=fill, width = width, minimum = minimum, reset_ticks = reset_ticks, quintuples = quintuples)
    _figure.show() if _figure._interactive else None

##############################################
###########    Plotting Tools    #############
##############################################

def error(*args, xerr = None, yerr = None, color = None, xside = None, yside = None, label = None):
    _figure.error(*args, xerr = xerr, yerr = yerr, xside = xside, yside = yside, color = color, label = label)
    _figure.show() if _figure._interactive else None

def event_plot(data, marker = None, color = None, orientation = None, side = None):
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

def text(label, x, y, color = None, background = None, style = None, orientation = None, alignment = None, xside = None, yside = None):
    _figure._active.text(label, x, y, xside = xside, yside = yside, color = color, background = background, style = style, orientation = orientation, alignment = alignment)
    _figure.show() if _figure._interactive else None

def rectangle(x = None, y = None, marker = None, color = None, lines = None, fill = None, xside = None, yside = None, label = None):
    _figure._active.rectangle(x = x, y = y, xside = xside, yside = yside, lines = lines, marker = marker, color = color, fill = fill, label = label)
    _figure.show() if _figure._interactive else None
    
def polygon(x = None, y = None,  radius = None, sides = None, marker = None, color = None, lines = None, fill = None, xside = None, yside = None, label = None):
    _figure._active.polygon(x = x, y = y, radius = radius, sides = sides, xside = xside, yside = yside, lines = lines, marker = marker, color = color, fill = fill, label = label)
    _figure.show() if _figure._interactive else None

def confusion_matrix(actual, predicted, color = None, style = None, labels = None):
    _figure._active.confusion_matrix(actual, predicted, labels = labels, color = color, style = style)
    _figure.show() if _figure._interactive else None

cmatrix = confusion_matrix

def indicator(value, label = None, color = None, style = None):
    _figure._active.indicator(value, label = label, color = color, style = style)
    _figure.show() if _figure._interactive else None

##############################################
##############    2D Plots    ################
############################################## 
    
def matrix_plot(matrix, marker = None, style = None, fast = False):
    _figure._active.matrix_plot(matrix, marker = marker, style = style, fast = fast)
    _figure.show() if _figure._interactive else None

def heatmap(dataframe, color = None, style=None):
    _figure._active.heatmap(dataframe, color = color, style = style)
    _figure.show() if _figure._interactive else None

def image_plot(path, marker = None, style = None, fast = False, grayscale = False):
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
    _glob.get_youtube(url, path, log)

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
    _glob.from_matplotlib(fig, marker = marker)

##############################################
##########     Date Functions    #############
##############################################

def date_form(input_form = None, output_form = None):
    _figure._active.date_form(input_form, output_form)
    
def set_time0(string, input_form = None):
    _figure._active.set_time0(string, input_form = input_form)

def today_datetime():
    return _figure._active.today_datetime()

def today_string(output_form = None):
    return _figure._active.today_string(output_form)

def datetime_to_string(datetime, output_form = None):
    return _figure._active.datetime_to_string(datetime, output_form = output_form)

def datetimes_to_strings(datetimes, output_form = None):
    return _figure._active.datetimes_to_strings(datetimes, output_form = output_form)

datetimes_to_string = datetimes_to_strings

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
    _ut.save_text(text, path, log = log)

def read_data(path, delimiter = None, columns = None, first_row = None, log = True):
    return _ut.read_data(path, delimiter = delimiter, columns = columns, first_row = first_row, log = log)

def write_data(data, path, delimiter = None, columns = None, log = True):
    _ut.write_data(data, path, delimiter = delimiter, columns = columns, log = log)

def download(url, path, log = True):
    _ut.download(url, path, log)

def delete_file(path, log = True):
    _ut.delete_file(path, log = log)

test_data_url     =  _glob.test_data_url
test_bar_data_url =  _glob.test_bar_data_url
test_image_url    =  _glob.test_image_url
test_gif_url      =  _glob.test_gif_url
test_video_url    =  _glob.test_video_url
test_youtube_url  =  _glob.test_youtube_url

##############################################
##########     Other Functions    ############
##############################################

def colorize(string, color = None, style = None, background = None, show = False):
    return _ut.colorize(string, color = color, style = style, background = background, show = show)

def uncolorize(string):
    return _ut.uncolorize(string)

def terminal_size():
    return _ut.terminal_size()

ts = terminal_size

def terminal_width():
    return _ut.terminal_width()

tw = terminal_width

def terminal_height():
    return _ut.terminal_height()

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

add(subplots)
add(subplot)
add(main)
add(active)

add(interactive)
add(plot_size)
add(limit_size)
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
add(candlestick)
add(bar)
add(simple_bar)
add(multiple_bar)
add(simple_multiple_bar)
add(stacked_bar)
add(simple_stacked_bar)
add(simple_bar)
add(hist)
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

add(play_gif)
add(play_video)
add(play_youtube)
add(get_youtube)

add(show)
add(build)
add(sleep)
add(time)
add(save_fig)
add(from_matplotlib)

add(date_form)
add(set_time0)
add(today_datetime)
add(today_string)
add(datetime_to_string)
add(datetimes_to_strings)
add(string_to_datetime)

add(script_folder)
add(parent_folder)
add(join_paths)
add(save_text)
add(read_data)
add(write_data)
add(download)
add(delete_file)

add(colorize)
add(uncolorize)
add(terminal_size)
add(terminal_width)
add(terminal_height)
add(sin)
add(square)
add(transpose)

add(colors)
add(styles)
add(markers)
add(themes)
add(test)