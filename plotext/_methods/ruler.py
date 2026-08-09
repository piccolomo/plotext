# Ruler utilities for tick formatting, scaling, and numeric precision

import math
from plotext._kernel.clink import clink 
from plotext._constants.numerical import limit_deltas
from plotext._constants.enums import limit_alignments
from plotext._settings import defaults


# Apply log base 10 to a value
def log(data):
    return math.log10(data)

# Rescale a list within boundaries (delegated to clink)
rescale = clink.rescale


# Get delta adjustment for a given alignment
def get_limit_delta(alignment):
    return limit_deltas[limit_alignments.index(alignment)]


# Generate evenly spaced values between lower and upper
def linspace(lower, upper, length = 10):
    slope = (upper - lower) / (length - 1) if length > 1 else 0
    return [lower + x * slope for x in range(length)]


# Apply inverse of log (power of 10) to a list of values
def power10_data(data):
    return [10 ** el for el in data]

# Generate string labels for ticks with appropriate precision
def get_labels(ticks):
    digit = distinguishing_digit(ticks) + defaults.tick_extra_decimals
    return [shorter_format(el, digit) for el in ticks]


# Return shortest representation between fixed-point and exponential formats
def shorter_format(value, distinguishing_digit):
    decimal_form = get_decimal_form(value, distinguishing_digit)
    exp_digit = distinguishing_digit - first_decimal_digit_position(value)
    exp_digit = max(1, exp_digit)
    exp_form = get_exponential_form(value, exp_digit)
    return exp_form if len(exp_form) < len(decimal_form) else decimal_form


# Format value in fixed decimal notation
def get_decimal_form(value, digit):
    return f"{value:.{digit}f}"


# Format value in exponential notation
def get_exponential_form(value, digit):
    return f"{value:.{digit}e}"


# Return position of first significant digit in decimal part
def first_decimal_digit_position(x):
    return -math.floor(math.log10(abs(x + 1e-8)))


# Determine minimum decimal digits needed to distinguish all values; for ticks that are all integer-valued, return 0 so the labels print without trailing ".0".
def distinguishing_digit(data):
    d = [_distinguishing_digit(data[i], data[i + 1]) for i in range(len(data) - 1)]
    digit = max(d, default = 0)
    if not all(t == int(t) for t in data):
        digit += 1
    return digit


# Compute digits needed to distinguish two float values
def _distinguishing_digit(a, b):
    d = abs(a - b)
    d = 0 if d == 0 else -math.log10(2 * d)
    d = 0 if d < 0 else math.ceil(d)
    return d


# Compare two floats using relative tolerance
def almost_equal(a, b, relative = 3):
    return abs(a - b) <= 10 ** (-relative) * (abs(a + b)) / 2



