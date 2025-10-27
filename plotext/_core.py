# Terminal utilities and classes
from plotext._terminal import terminal_class as _terminal_class
from plotext._methods.list import sin as _sin
from plotext._methods.string import uncolorize as _uncolorize


# Initialize terminal and master canvas
_terminal = _terminal_class() 

for name in dir(_terminal):
    if not name.startswith("_"):
        attr = getattr(_terminal, name)
        if callable(attr):
            globals()[name] = attr


_master = _terminal._master

for name in dir(_master):
    if not name.startswith("_"):
        attr = getattr(_master, name)
        if callable(attr):
            globals()[name] = attr


master = _master
active = _master._active


# Trigonometric utility
sin = _sin
uncolorize = _uncolorize


# def draw(signal):
#     _master._active.draw(signal)
#     return _master._active

# def draw(*args, marker = None, plot = None, fillx = None, filly = None, xside = None, yside = None, label = None):
#     _master._active.scatter(*args, marker = marker, plot = plot, fillx = fillx, filly = filly, xside = xside, yside = yside, label = label)
#     return _master._active 

# def plot(*args, marker = None, fillx = None, filly = None, xside = None, yside = None, label = None):
#     _master._active.plot(*args, marker = marker, fillx = fillx, filly = filly, xside = xside, yside = yside, label = label)
#     return _master._active 

# def plot(*args, marker = None, fillx = None, filly = None, xside = None, yside = None, label = None):
#     _master._active.plot(*args, marker = marker, fillx = fillx, filly = filly, xside = xside, yside = yside, label = label)
#     return _master._active


# # Terminal utility functions
# terminal_size = _terminal.get_size 

# def clear_terminal():
#     _terminal.clear()
#     return _master

# def clear_figure():
#     _master._active.clear()
#     return _master._active

# clf = clear_figure

# def structure():
#     _terminal.log()
#     return _master


# def active():
#     return _master._active



# def title(label):
#     _master._active.title(label)
#     return _master._active

# def xlabel(label):
#     _master._active.xlabel(label)
#     return _master._active

# def ylabel(label):
#     _master._active.ylabel(label)
#     return _master._active

# def ruler(axis = None, side = None, frequency = None, scale = None, alignment = None, direction = None, pixel = None):
#     _master._active.ruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, axis = axis, side = side)
#     return _master._active

# def xruler(frequency = None, scale = None, alignment = None, direction = None, pixel = None, side = None):
#     _master._active.xruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, side = side)
#     return _master._active

# def yruler(frequency = None, scale = None, alignment = None, direction = None, pixel = None, side = None):
#     _master._active.yruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, side = side)
#     return _master._active

# def date(axis = None, side = None):
#     return _master._active.date(axis, side)


# def xaxis(status = None, style = None, pixel = None, side = 0):
#     _master._active.xaxis(status = status, style = style, pixel = pixel)
#     return _master._active

# def yaxis(status = None, style = None, pixel = None, side = 0):
#     _master._active.yaxis(status = status, style = style, pixel = pixel)
#     return _master._active

# def frame(frame = True, style = None, pixel = None):
#     _master._active.xaxis(frame, style = style, pixel = pixel, side = r2)
#     _master._active.yaxis(frame, style = style, pixel = pixel, side = r2)
#     return _master._active

# def canvas_pixel(pixel = None):
#     _master._active.canvas_pixel(pixel)
#     return _master._active

# def legend(x = 0, y = 0, relative = None, status = True, ha = None, va = None, pixel = None, xside = None, yside = None):
#     _master._active.legend(x = x, y = y, relative = relative, status = status, ha = ha, va = va, pixel = pixel, xside = xside, yside = yside)
#     return _master._active

# def convert(time, output = "timestamp", axis = None, side = None):
#     return _master._active.convert(time, output)

# def date(form = None, active = True, axis = None, side = None):
#     _master._active.date(form, active, axis, side)
#     return _master._active 





# def show():
#     _master.show()



