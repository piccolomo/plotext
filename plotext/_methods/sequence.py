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


# Generate a square-wave signal alternating between +amplitude and -amplitude
def square(periods = 2, length = 200, amplitude = 1):
    T = length / periods
    return [amplitude if i % T <= T / 2 else -amplitude for i in range(length)]


# Generate Gaussian noise samples (mean `offset`, standard deviation `amplitude`). seed=None for fresh randomness.
def noise(length = 200, amplitude = 1, offset = 0, seed = None):
    import random
    rng = random.Random(seed)
    return [rng.gauss(offset, amplitude) for _ in range(length)]


# Folder holding the bundled sample files
def sample_folder():
    import os
    folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_data')
    return folder


# Names of the bundled sample files, without extension
def sample_names():
    import os
    names = sorted(set(os.path.splitext(file_name)[0] for file_name in os.listdir(sample_folder())))
    return names


# Return the full path of a bundled sample file, found by name without extension
def sample(name = "puppy"):
    import os
    for file_name in sorted(os.listdir(sample_folder())):
        if os.path.splitext(file_name)[0] == name:
            return os.path.join(sample_folder(), file_name)
    raise ValueError("unknown sample name '" + str(name) + "'; available: " + ', '.join(sample_names()))


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


# Tabulate counts of (actual, predicted) categorical pairs. Returns (labels, counts) where counts[r][c] = number of pairs with actual == labels[r] and predicted == labels[c]. labels defaults to the sorted union of values in actual + predicted; pass labels to pin order or restrict the universe (unknown values are silently dropped).
def _crosstab(actual, predicted, labels = None):
    labels = sorted(set(actual) | set(predicted)) if labels is None else list(labels)
    index = {v: i for i, v in enumerate(labels)}
    n = len(labels)
    counts = [[0] * n for _ in range(n)]
    for a, p in zip(actual, predicted):
        if a in index and p in index:
            counts[index[a]][index[p]] += 1
    return labels, counts

