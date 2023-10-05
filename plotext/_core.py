# # /usr/bin/env python3
# # -*- coding: utf-8 -*-

# # This file contains all the main plotext functions available externally to the user

from ._terminal import terminal
from ._figure import _figure_class
from ._log import log

master = _figure_class(terminal)

##############################################
###########    Size Functions    #############
##############################################

def limit_size(width = None, height = None):
    return master.limit_size(width, height)
limitsize = limit_size

def plot_size(width = None, height = None, direction = None):
    return master.plot_size(width, height, direction)
plotsize = plot_size

def take_minimum_size():
    master.take_minimum_size()
take_min = take_minimum_size

def take_maximum_size():
    master.take_maximum_size()
take_max = take_maximum_size

def prompt_size(height = None):
    terminal.set_prompt_height(height)
    terminal.update_size()
    #master.plot_size(*master.size, master._size_direction)

##############################################
#########    Subplots Functions    ###########
##############################################

def main():
    return master

def active():
    return master._active

def subplots(rows = None, cols = None):
    return master.subplots(rows, cols)
    #_figure.show() if _figure._interactive else None
    #return sub

def subplot(row = None, col = None):
    return master.subplot(row, col)

##############################################
#########    Settings Functions    ###########
##############################################

def xaxes(lower = None, upper = None):
    return master.xaxes(lower, upper)

def yaxes(left = None, right = None):
    return master.yaxes(left, right)

def xlim(left = None, right = None, xside = None):
    return master.xlim(left, right, xside)

def ylim(lower = None, upper = None, yside = None):
    return master.ylim(lower, upper, yside)

def axis_color(self, color = None):
    return master.axis_color(color)

def canvas_color(self, color = None):
    return master.canvas_color(color)

##############################################
###########    Clear Functions    ############
##############################################
# clear size, subplots, settings (labels, axes, ticks), color, signals, canvas

def clear_subplots():
    return master.clear_subplots()

def reset_sizes():
    return master.reset_sizes()

def clear_settings():
    return master.clear_settings()
cls = clear_settings

def clear_figure():
    return master.clear()
clf = clear_figure
        
##############################################
######    Main Plotting Functions    #########
##############################################

def scatter(*args, marker = None, color = None, style = None, fillx = None, filly = None, xside = None, yside = None, label = None):
    active().scatter(*args, xside = xside, yside = yside, marker = marker, color = color, style = style, fillx = fillx, filly = filly, label = label)
#     _figure.show() if _figure._interactive else None

##############################################
##########    Build Functions    #############
##############################################

def show():
    master.show()

