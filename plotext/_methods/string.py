# String utilities and stdout helpers for rendering and formatting

import sys
from plotext._settings.constants.text import space, new_line, empty, ansi_begin


# Write string to stdout with optional flush
def write(string, flush = True):
    sys.stdout.write(string)
    sys.stdout.flush() if flush else None
    return string


# Remove ANSI color codes from a string or colorize object
def uncolorize(string):
    from plotext._primitives.colorize import colorize
    if isinstance(string, colorize):
        return string.get_string(1)
    while ansi_begin in string:
        b = string.index(ansi_begin)
        e = string[b:].index('m') + b + 1
        string = string.replace(string[b:e], '')
    return string


# Generate multiple new lines
def new_lines(n = 2):
    return new_line * n


# Add prefix to string if both exist
def add_prefix(doc, prefix):
    return None if doc is None else doc if prefix is None else prefix + doc


# Pad string with spaces to target length
def pad(string, length = None):
    string = str(string)
    l = len(string)
    length = l if length is None else int(length)
    return string + ' ' * (length - l)


# Check if string contains only spaces
def only_spaces(string):
    return string == len(string) * space


# Join list of strings with delimiter, ignoring None
def connect_strings(docs, delimiter = empty):
    docs = [el for el in docs if el is not None]
    return delimiter.join(docs) if docs else None


# Format a [lower, upper] limits pair for logging
def log_limits(limits):
    limits = ['None' if limit is None else str(round(limit, 2)) for limit in limits]
    return '[' + ', '.join(limits) + ']'
