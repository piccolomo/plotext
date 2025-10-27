from plotext._constants import space, new_line, empty, ansi_begin, limit_delta, limit_alignments


def write(string, flush = True):
    sys.stdout.write(string)
    if flush:
        sys.stdout.flush()

# Lambda for creating multiple new lines (default 2)
new_lines = staticmethod(lambda n = 2: new_line * n)

# Add prefix to string if prefix and doc exist

def add_prefix(doc, prefix):
    return None if doc is None else doc if prefix is None else prefix + doc

# Pad string with spaces up to specified length

def pad(string, length = None):
    string = str(string)
    l = len(string)
    length = l if length is None else int(length)
    return string + ' ' * (length - l)

# Check if string contains only spaces

def only_spaces(string):
    return string == len(string) * space

# Join list of docstrings with delimiter, ignoring None

def connect_strings(docs, delimiter = empty):
    docs = [el for el in docs if el is not None]
    return delimiter.join(docs) if docs else None

# Remove ANSI color codes from a string or colorize object

def uncolorize(string):
    from plotext._colorize import colorize
    if isinstance(string, colorize):
        return string.get_string(1)
    colored = lambda string: ansi_begin in string
    while colored(string):
        b = string.index(ansi_begin)
        e = string[b:].index('m') + b + 1
        string = string.replace(string[b:e], '')
    return string