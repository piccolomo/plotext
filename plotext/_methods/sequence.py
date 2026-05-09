# Sequence utilities for list operations and basic numerical generation

import math
from copy import copy


# Remove duplicates from a list
def unique(data):
    return list(set(list(data)))


# Generate sinusoidal data with optional decay and offset
def sin(periods = 2, length = 200, amplitude = 1, phase = 0, decay = 0, offset = 0):
    f = 2 * math.pi * periods / (length - 1)
    phase = math.pi * phase
    d = decay / length
    return [amplitude * math.sin(f * el + phase) * math.exp(-d * el) + offset for el in range(length)]


# Transpose a 2D list (matrix)
def transpose(data, length = 1):
    return [[]] * length if data == [] else list(map(list, zip(*data)))


# Remove None values from list
def remove_none(data):
    return [el for el in data if el is not None]


# Get maximum or minimum from list (ignores None)
def get_extreme(data, maximum = True):
    method = max if maximum else min
    return method(remove_none(data), default = None)


# Repeat elements of a list up to a target length, preserving copies
def repeat(data, length):
    original = data.copy()
    make_copy = lambda: [copy(el) for el in original]
    l = (length + 1) // len(data)
    [data.extend(make_copy()) for _ in range(l)]
    return data[:length]


# Replace None elements in a list with values from a fallback list at matching positions
def replace_none(data, new_data):
    return [new_data[i] if el is None else el for i, el in enumerate(data)]


def remove_none(data):
    return [el for el in data if el is not None]

def safe_min(data):
    return min(remove_none(data), default = None)

def safe_max(data):
    return max(remove_none(data), default = None)

