# # /usr/bin/env python3
# # -*- coding: utf-8 -*-

# # This file contains all the main plotext functions available externally to the user

from ._figure import _figure_class

_main_figure = _figure_class()

##############################################
#########    Subplots Functions    ###########
##############################################

def main():
    return _main_figure

def active():
    return main()._active

def subplots(rows = None, cols = None):
    return main().subplots(rows, cols)
    #_figure.show() if _figure._interactive else None
    #return sub

def subplot(row = None, col = None):
    return main().subplot(row, col)


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
    pass
    #_figure.show()
