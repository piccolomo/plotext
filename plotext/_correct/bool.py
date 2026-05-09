# Validation utilities for boolean and binary-flag parameters
# (booleans, ±1 direction, line method, subplot size policy, etc.).

from plotext._constants.numerical import binary, directions
from plotext._constants.enums import line_methods, size_policies


# Keep value as-is, returning the default when None
def status(value, default):
    return value if value is not None else default


# Coerce input to boolean, falling back to the default when not bool-like
def boolean(element = None, default = False):
    return bool(element) if isinstance(element, bool) or element in binary else default


# Validate a direction flag: accepts +1 or -1, falls back to directions[1] (+1)
# for any other input (None, 0, non-binary int, strings, etc.).
def direction(value):
    return value if value in directions else directions[1]


# Validate a subplot size policy: accepts 'minimum' or 'maximum',
# falls back to size_policies[1] ('maximum') for any other input.
def size_policy(value):
    return value if value in size_policies else size_policies[1]


# Validate and normalize line method: 'simple'/'full' -> 0/1; 0/1 unchanged; anything else -> 0.
def line_method(method = None):
    if method in line_methods:
        return line_methods.index(method)
    if method in binary:
        return int(method)
    return 0
