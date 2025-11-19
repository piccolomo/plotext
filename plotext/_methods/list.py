# Utility functions for list and numerical operations


from plotext._clink import clink
from copy import copy
import math

# ------------------------
# Type / structure checks
# ------------------------

# Check if object is list-like
def is_list_like(obj):
    return hasattr(obj, '__iter__') and hasattr(obj, '__len__') and hasattr(obj, '__getitem__') and not isinstance(obj, (str, bytes)) and not callable(obj)

# ------------------------
# List processing
# ------------------------

# Remove None values from list
remove_none = staticmethod(lambda data: [el for el in data if el is not None])

# Get maximum or minimum from list (ignores None)
def get_extreme(data, maximum=True):
    method = max if maximum else min
    return method(remove_none(data), default=None)

# Repeat elements of a list up to given length, preserving copies
def repeat(data, length):
    original = data.copy()
    make_copy = lambda: [copy(el) for el in original]
    l = (length + 1) // len(data)
    [data.extend(make_copy()) for _ in range(l)]
    return data[:length]

# Transpose a 2D list (matrix)
def transpose(data, length=1):
    return [[]] * length if data == [] else list(map(list, zip(*data)))

# Replace None elements in list with values from alternative list
def replace_none(data, alternative):
    return [a if d is None and a is not None else d for (d, a) in zip(data, alternative)]

# Remove duplicates from list
def unique(data):
    return list(set(list(data)))

# Insert an element after each item in a list
def insert_after_each(lst, element):
    return [x for item in lst for x in (item, element)]

# Insert an element before each item in a list
def insert_before_each(lst, element):
    return [x for item in lst for x in (element, item)]

# ------------------------
# Numerical operations
# ------------------------

# Rescale a list within boundaries (from clink)
rescale = clink.rescale

# Compute cumulative sum of a list of numbers
def cumulative_sum(numbers):
    s = 0
    res = []
    for num in numbers:
        s += num
        res.append(s)
    return res

# Apply log base 10 to data list
def log(data):
    return [math.log10(el) for el in data]

# Apply inverse of log (power 10) to data list
def power10(data):
    return [10 ** el for el in data]

# Convert data list to integers
def to_integers(data):
    return list(map(int, data))

# ------------------------
# Data generation
# ------------------------

# Generate sinusoidal data with parameters
def sin(periods=2, length=200, amplitude=1, phase=0, decay=0, offset=0):
    f = 2 * math.pi * periods / (length - 1)
    phase = math.pi * phase
    d = decay / length
    return [amplitude * math.sin(f * el + phase) * math.exp(-d * el) + offset for el in range(length)]

# Generate list of evenly spaced values from lower to upper
def linspace(lower, upper, length=10):
    slope = (upper - lower) / (length - 1) if length > 1 else 0
    return [lower + x * slope for x in range(length)]
