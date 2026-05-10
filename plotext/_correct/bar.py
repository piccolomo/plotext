# Validation utilities for bar-plot parameters and data shapes.

from plotext._settings import defaults
from plotext._correct.data import data


# Validate a bar width as a fraction of the inter-bar spacing (clamped to [0, 1]); falls back to defaults.bar_width for None or non-numeric input.
def width(value = None):
    if value is None: return defaults.bar_width
    try: return max(0.0, min(1.0, float(value)))
    except (TypeError, ValueError): return defaults.bar_width


# Format bar plot data into (x, y_min, y_max) aligned lists. Accepts:
#   ()                  → empty
#   (y_max,)            → x = 1..N, y_min = 0
#   (x, y_max)          → y_min = 0
#   (x, y_min, y_max)   → all explicit
# Reuses data() so scalar broadcasting, truncation and missing-arg
# defaults match the rest of plotext. Extra args (n > 3) are ignored.
def bar_data(*args):
    if len(args) <= 2:
        x, y_max = data(*args)
        y_min = [0] * len(y_max)
    else:
        x, y_min = data(args[0], args[1])
        _, y_max = data(args[0], args[2])
        l = min(len(x), len(y_min), len(y_max))
        x, y_min, y_max = x[:l], y_min[:l], y_max[:l]
    return x, y_min, y_max


# Format multiple bar plot data into (x, Y) where Y is a list of equal-length sequences. Accepts:
#   (Y,)        → list of height sequences; x defaults to 1..N
#   (x, Y)      → explicit x and a list of height sequences
# All Y rows are truncated to a common length (the shortest), and x is aligned to that.
def multiple_bar_data(*args):
    if len(args) == 1:
        Y = [list(y) for y in args[0]]
        n = min((len(y) for y in Y), default=0)
        x = list(range(1, n + 1))
    else:
        x = list(args[0])
        Y = [list(y) for y in args[1]]
        n = min(len(x), *(len(y) for y in Y)) if Y else 0
    return x[:n], [y[:n] for y in Y]
