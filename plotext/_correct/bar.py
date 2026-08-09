# Validation utilities for bar-plot parameters and data shapes.

from plotext._settings import defaults
from plotext._correct.data import data


# Validate a bar width as a fraction of the inter-bar spacing (clamped to [0, 1]); falls back to defaults.bar_width for None or non-numeric input.
def width(value = None):
    if value is None: return defaults.bar_width
    try: return max(0.0, min(1.0, float(value)))
    except (TypeError, ValueError): return defaults.bar_width


# Format bar plot data into (x, y_min, y_max) aligned lists: () gives empty, (y_max,) gives x = 1..N and y_min = 0, (x, y_max) gives y_min = 0, (x, y_min, y_max) is all explicit; extra arguments are ignored.
def bar_data(*args):
    if len(args) <= 2:
        x, y_max = data(*args)
        y_min = [0] * len(y_max)
    else:
        x, y_min = data(args[0], args[1])
        _, y_max = data(args[0], args[2])
        length = min(len(x), len(y_min), len(y_max))
        x, y_min, y_max = x[:length], y_min[:length], y_max[:length]
    return x, y_min, y_max


# Format multiple bar plot data into (x, heights): (heights,) gives x = 1..N, (x, heights) is explicit; every row is truncated to the shortest one.
def multiple_bar_data(*args):
    if len(args) == 1:
        heights = [list(row) for row in args[0]]
        length = min((len(row) for row in heights), default = 0)
        x = list(range(1, length + 1))
    else:
        x = list(args[0])
        heights = [list(row) for row in args[1]]
        length = min(len(x), *(len(row) for row in heights)) if heights else 0
    return x[:length], [row[:length] for row in heights]
