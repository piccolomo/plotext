# Terminal utilities and classes
from plotext._terminal import terminal_class as _terminal_class
from plotext._methods import list_methods as _list_methods
from plotext._methods import string_methods as _string_methods


# Initialize terminal and master canvas
_terminal = _terminal_class() 
_master = _terminal._master


def draw(signal):
    _master._active.draw(signal)
    return _master._active

def scatter(*args, marker = None, fillx = None, filly = None, xside = None, yside = None, label = None):
    _master._active.scatter(*args, marker = marker, fillx = fillx, filly = filly, xside = xside, yside = yside, label = label)
    return _master._active 

def plot(*args, marker = None, fillx = None, filly = None, xside = None, yside = None, label = None):
    _master._active.plot(*args, marker = marker, fillx = fillx, filly = filly, xside = xside, yside = yside, label = label)
    return _master._active 

# def plot(*args, marker = None, fillx = None, filly = None, xside = None, yside = None, label = None):
#     _master._active.plot(*args, marker = marker, fillx = fillx, filly = filly, xside = xside, yside = yside, label = label)
#     return _master._active


# Terminal utility functions
terminal_size = _terminal.get_size

def clear_terminal():
    _terminal.clear()
    return _master

def structure():
    _terminal.log()
    return _master


def active():
    return _master._active



def title(label):
    _master._active.title(label)
    return _master._active

def xlabel(label):
    _master._active.xlabel(label)
    return _master._active

def ylabel(label):
    _master._active.ylabel(label)
    return _master._active

def ruler(frequency = None, scale = None, alignment = None, direction = None, pixel = None, axis = None, side = None):
    _master._active.ruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, axis = axis, side = side)
    return _master._active

def xruler(frequency = None, scale = None, alignment = None, direction = None, pixel = None, side = 0):
    _master._active.xruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, side = side)
    return _master._active

def yruler(frequency = None, scale = None, alignment = None, direction = None, pixel = None, side = 0):
    _master._active.yruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, side = side)
    return _master._active

def xaxis(status = None, style = None, pixel = None, side = 0):
    _master._active.xaxis(status = status, style = style, pixel = pixel)
    return _master._active

def yaxis(status = None, style = None, pixel = None, side = 0):
    _master._active.yaxis(status = status, style = style, pixel = pixel)
    return _master._active

def frame(frame = True, style = None, pixel = None):
    _master._active.xaxis(frame, style = style, pixel = pixel, side = r2)
    _master._active.yaxis(frame, style = style, pixel = pixel, side = r2)
    return _master._active

def canvas_pixel(pixel = None):
    _master._active.canvas_pixel(pixel)
    return _master._active

def legend(x = 0, y = 0, relative = None, status = True, ha = None, va = None, pixel = None, xside = None, yside = None):
    _master._active.legend(x = x, y = y, relative = relative, status = status, ha = ha, va = va, pixel = pixel, xside = xside, yside = yside)
    return _master._active





def show():
    _master.show()



# Trigonometric utility
sin = _list_methods.sin
uncolorize = _string_methods.uncolorize
