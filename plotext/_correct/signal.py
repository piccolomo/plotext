# Signal validation utilities

from plotext._settings.constants.enums import line_methods
from plotext._settings.constants.numerical import binary


# Validate and normalize line method: 'simple'/'full' -> 0/1; 0/1 unchanged; anything else -> 0
def line_method(method = None):
    if method in line_methods:
        return line_methods.index(method)
    if method in binary:
        return int(method)
    return 0
