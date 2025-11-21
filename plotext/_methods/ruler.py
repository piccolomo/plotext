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
    digit = distinguishing_digit(ticks)
    return [shorter_format(el, digit) for el in ticks]

# Return the shortest representation between fixed-point and exponential formats
def shorter_format(value, distinguishing_digit):
    decimal_form = get_decimal_form(value, distinguishing_digit)

    exp_digit = distinguishing_digit - first_decimal_digit_position(value)
    exp_digit = max(1, exp_digit)
    exp_form = get_exponential_form(value, exp_digit)

    return exp_form if len(exp_form) < len(decimal_form) else decimal_form

def get_decimal_form(value, digit):
    f_string = f"{{:.{digit}f}}"
    return f_string.format(value)

def get_exponential_form(value, digit):
    f_string = f"{{:.{digit}e}}" 
    return f_string.format(value)

# it returns the position of first number in a decimal part of a float; eg: 0.000245 → position = 4 
def first_decimal_digit_position(x):
    return - math.floor(math.log10(abs(x + 1e-8))) # if x != 0 else 0

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