# # /usr/bin/env python3
# # -*- coding: utf-8 -*-

# # This file contains all the main plotext functions available externally to the user

from ._terminal import terminal as _terminal
from ._figure import _figure_class
from ._log import log as _log

_master = _figure_class(_terminal)

##############################################
###########    Size Functions    #############
##############################################

def limit_size(width = None, height = None):
    return _master.limit_size(width, height)
limitsize = limit_size

def plot_size(width = None, height = None, direction = None):
    return _master.plot_size(width, height, direction)
plotsize = plot_size

def take_minimum_size():
    _master.take_minimum_size()
take_min = take_minimum_size

def take_maximum_size():
    _master.take_maximum_size()
take_max = take_maximum_size

def prompt_size(height = None):
    _terminal.set_prompt_height(height)
    _master._update_terminal_size()

##############################################
#########    Subplots Functions    ###########
##############################################

def main():
    return _master

def active():
    return _master._get_active()

def subplots(rows = None, cols = None):
    return _master.subplots(rows, cols)

def subplot(row = None, col = None):
    return _master.subplot(row, col)

##############################################
#########    Settings Functions    ###########
##############################################

def ticks_color(color = None):
    return _master.ticks_color(color)

def axes_color(color = None):
    return _master.axes_color(color)

def title(label = None):
    return _master.title(label)

def xlabel(label = None, xside = None):
    return _master.xlabel(label, xside)

def ylabel(label = None, yside = None):
    return _master.ylabel(label, yside)

##############################################
######    Main Plotting Functions    #########
##############################################

# def scatter(*args, marker = None, color = None, style = None, fillx = None, filly = None, xside = None, yside = None, label = None):
#     active().scatter(*args, xside = xside, yside = yside, marker = marker, color = color, style = style, fillx = fillx, filly = filly, label = label)

##############################################
##########    Build Functions    #############
##############################################

def show():
    _master._show()

##############################################
##########    Clear Functions    #############
##############################################

def clear_sizes():
    _master.clear_sizes()

def clear_subplots():
    _master.clear_subplots()

def clear_settings():
    _master.clear_settings()

def clear_figure():
    _master.clear_figure()
clf = clear_figure

def clear_terminal(lines = None):
    _terminal.clear(lines)
clt = clear_terminal

##############################################
#########    Utility Functions    ############
##############################################

def log(show = True):
    _log.on() if show else _log.off()

def terminal_size():
    return _terminal.get_size()
ts = terminal_size

def terminal_width():
    return terminal_size()[0]
tw = terminal_width

def terminal_height():
    return terminal_size()[1]
th = terminal_height
