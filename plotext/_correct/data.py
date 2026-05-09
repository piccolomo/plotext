# Data formatting utilities for x/y inputs and list normalization

from plotext._methods import object as object_methods


# Format x and y data lists into aligned pairs
def data(x=None, y=None):
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

