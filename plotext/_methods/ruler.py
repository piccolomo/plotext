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

# Generate string labels for ticks with appropriate precision, every label of an axis taking the same form and the same decimals
def get_labels(ticks):
    digit = distinguishing_digit(ticks) + defaults.tick_extra_decimals
    whole_ticks = all(tick == int(tick) for tick in ticks)
    largest = max([abs(tick) for tick in ticks], default = 0)
    decimal_digit = max(0, math.ceil(digit)) + (0 if whole_ticks else 1)   # fractional ticks always keep one decimal, so a tick at 17.5 is never written as 18
    exponential_digit = 0 if largest == 0 else max(0, math.ceil(digit + math.log10(largest)))   # the point sits just after the leading digit, so that many places fewer are needed
    decimal_labels = [get_decimal_form(tick, decimal_digit) for tick in ticks]
    exponential_labels = [get_exponential_form(tick, exponential_digit) for tick in ticks]
    return exponential_labels if longest(exponential_labels) < longest(decimal_labels) else decimal_labels


# The length of the longest label of a list, as 8 for ['1.0e-09', '-1.0e-09']
def longest(labels):
    return max([len(label) for label in labels], default = 0)


# Format value in fixed decimal notation
def get_decimal_form(value, digit):
    return f"{value:.{digit}f}"


# Format value in exponential notation, as 1.3e18 or 1.3e-9: the plus adds nothing and the exponent carries no leading zero
def get_exponential_form(value, digit):
    text = f"{value:.{digit}e}"
    return text.replace("e+0", "e").replace("e+", "e").replace("e-0", "e-")


# The decimals needed to tell every tick from its neighbour, left unrounded so the two forms can round once each, and negative when whole digits before the point do not matter either
def distinguishing_digit(data):
    d = [_distinguishing_digit(data[i], data[i + 1]) for i in range(len(data) - 1)]
    return max(d, default = 0)


# Compute digits needed to distinguish two float values
def _distinguishing_digit(a, b):
    d = abs(a - b)
    return 0 if d == 0 else -math.log10(2 * d)


# Compare two floats using relative tolerance
def almost_equal(a, b, relative = 3):
    return abs(a - b) <= 10 ** (-relative) * (abs(a + b)) / 2



