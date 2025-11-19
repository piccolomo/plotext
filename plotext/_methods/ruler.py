import math
from plotext._constants import limit_delta, limit_alignments
from plotext._methods.list import log, power10

def apply_scale(data, scale):
    return log(data) if scale == "log" else data

# Reverse scaling of data; supports "log" scale

def reverse_scale(data, scale):
    return power10(data) if scale == "log" else data

# Generate string labels for ticks with appropriate decimal precision

def get_labels(ticks):
    d = distinguishing_digit(ticks)
    fmt = f"{{:.{d}f}}"
    return [fmt.format(el) for el in ticks]

# Determine minimum decimal digits needed to distinguish all values

def distinguishing_digit(data):
    d = [_distinguishing_digit(data[i], data[i + 1]) for i in range(len(data) - 1)]
    return max(d, default = 1)

# Compute digits needed to distinguish two float values

def _distinguishing_digit(a, b):
    d = abs(a - b)
    d = 0 if d == 0 else -math.log10(2 * d)
    d = 0 if d < 0 else math.ceil(d)
    return d + 1 if round(a, d) == round(b, d) else d

# Get the delta adjustment for a given alignment
def get_limit_delta(alignment):
    return limit_delta[limit_alignments.index(alignment)]