# Numerical constants: discrete sets, deltas, tolerances and bounds

# Discrete numeric sets
binary = [0, 1]
directions = [-1, 1]

limit_delta = 10 ** (-4)
limit_deltas = [0.5, limit_delta]

# Bounds
infinity = float('inf')

# How many different pixels are looked at in one signal, when taking the colors already in use; an image holds thousands of them, and this keeps the search short.
max_unique_pixels = 64
