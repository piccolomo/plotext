# Numerical constants: discrete sets, deltas, tolerances and bounds

# Discrete numeric sets
binary = [0, 1]
directions = [-1, 1]

limit_delta = 10 ** (-4)
limit_deltas = [0.5, limit_delta]

# Numeric tolerances
infinitesimal = 1e-12

# Bounds
infinity = float('inf')

# Maximum number of unique pixels to scan per signal when feeding the colour cycler. Caps the per-draw dedup so image-style signals (thousands of RGB pixels that never match the cycler's palette pool) return in O(MAX_UNIQUE_PIXELS) instead of O(N).
max_unique_pixels = 64