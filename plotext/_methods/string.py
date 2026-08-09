# String utilities and stdout helpers for rendering and formatting

import sys
from plotext._constants.text import space, new_line, empty, ansi_begin


# Write string to stdout with optional flush
def write(string, flush = True):
    sys.stdout.write(string)
    sys.stdout.flush() if flush else None
    return string


# Remove ANSI color codes from a string, colorize or matrix object, returning a plain string
def uncolorize(item):
    from plotext._primitives.colorize import colorize
    from plotext._primitives.matrix import matrix
    if isinstance(item, colorize):
        return item.string(1)
    if isinstance(item, matrix):
        return item.string(colorless = True)
    while ansi_begin in item:
        b = item.index(ansi_begin)
        e = item[b:].index('m') + b + 1
        item = item.replace(item[b:e], '')
    return item


# The given number of new lines, joined in one text.
def new_lines(number = 2):
    return new_line * number


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


# A whole web page around a block of text: the character set is named, so that a browser does not guess it and the box drawing characters survive, and the font is monospaced, so that the columns line up
def get_page(canvas):
    return ('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n'
            '<style>pre {font-family: monospace; line-height: 1.05}</style>\n'
            '</head>\n<body>\n' + canvas + '\n</body>\n</html>\n')


# A message from plotext itself, prefixed by the method saying it: a log for something done, a warning for something refused, an error for something wrong; the last two go on the error stream. Imports at call time, to avoid import cycles
def note(prefix, message, kind = "log"):
    from plotext._primitives.colorize import colorize
    from plotext._settings import defaults
    prefix_pixel = {"log": defaults.log_prefix_pixel, "warning": defaults.warning_prefix_pixel, "error": defaults.error_prefix_pixel}[kind]
    stream = sys.stdout if kind == "log" else sys.stderr
    print(colorize(prefix + ':', pixel = prefix_pixel).string() + ' ' + message, file = stream)
