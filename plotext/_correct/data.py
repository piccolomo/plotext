# Data formatting utilities for x/y inputs and list normalization

from plotext._methods import object as object_methods


# Format x and y data lists into aligned pairs
def data(x = None, y = None):
    if x is None and y is None:
        x, y = [], []
    elif x is not None and y is None:
        y, x = x, list(range(1, len(x) + 1))
    elif object_methods.is_numerical(x) and not object_methods.is_numerical(y):
        x = [x] * len(y)
    elif object_methods.is_numerical(y) and not object_methods.is_numerical(x):
        y = [y] * len(x)
    l = min(len(x), len(y))
    return [list(x[:l]), list(y[:l])]


# Format error bar data into (x, y, xerr, yerr) aligned lists: (y,), (x, y), (x, y, yerr) or (x, y, yerr, xerr); extra arguments are ignored.
def error_data(*args):
    if len(args) == 0:
        return [], [], [], []
    if len(args) == 1:
        x, y = data(args[0])
    else:
        x, y = data(args[0], args[1])
    _, yerr = data(x, args[2] if len(args) > 2 else 0)
    _, xerr = data(x, args[3] if len(args) > 3 else 0)
    return x, y, xerr, yerr


# Normalize a 2D matrix input to (rows, cols, list-of-lists), truncating ragged rows.
def matrix(data):
    if not data: return 0, 0, []
    cols = min(len(row) for row in data)
    return len(data), cols, [list(row[:cols]) for row in data]
