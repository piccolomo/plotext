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

