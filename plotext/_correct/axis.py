# Axis validation and normalization utilities

from plotext._constants.enums import axis_names, xsides, ysides
from plotext._methods.object import is_list_like
from plotext._methods.sequence import unique


# Normalize axis representation
def axis(axis):
    return boolean_string(axis, axis_names) 


# Normalize list of axes; the word both selects the two axes
def axes(axes):
    axes = [0, 1] if axes == 'both' else correct_list(axes, [0])
    return [axis(a) for a in axes]


# Normalize axis side
def side(axis, side):
    sides = ysides if axis else xsides
    return boolean_string(side, sides)


# Normalize list of sides across axes; the word both selects the two sides
def sides(axes, sides):
    sides = [0, 1] if sides == 'both' else correct_list(sides, [0])
    return sorted(unique([side(axis, s) for axis in axes for s in sides]))


# Normalize boolean/string side to integer index
def boolean_string(side, sides, sides_short = None):
    if side is None:
        side = sides[0]
    elif isinstance(side, str):
        side = side.strip()
    if side in sides:
        side = sides.index(side)
    if sides_short and side in sides_short:
        side = sides_short.index(side)
    if not (isinstance(side, int) and side in range(2)):
        side = 0
    return side


# Normalize input into a list with fallback default
def correct_list(data = None, default = None):
    return default if data is None else list(data) if is_list_like(data) else [data]