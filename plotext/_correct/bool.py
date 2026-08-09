# Validation utilities for boolean and binary flag parameters: booleans, directions, line methods, size policies.

from plotext._constants.numerical import binary, directions
from plotext._constants.enums import line_methods, line_method_scopes, size_policies, size_policies_short


# Keep value as-is, returning the default when None
def status(value, default):
    return value if value is not None else default


# Coerce input to boolean, falling back to the default when not bool-like
def boolean(element = None, default = False):
    return bool(element) if isinstance(element, bool) or element in binary else default


# Validate a direction: +1 or -1 pass, anything else gives +1.
def direction(value):
    return value if value in directions else directions[1]


# Validate a subplot size policy: accepts 'minimum' or 'maximum' (short 'min', 'max'), or the integers 0 or 1 in that order; falls back to size_policies[1] ('maximum') for any other input.
def size_policy(value):
    if value in size_policies:
        return value
    if value in size_policies_short:
        return size_policies[size_policies_short.index(value)]
    if value in binary:
        return size_policies[int(value)]
    return size_policies[1]


# Validate and normalize line method: 'simple'/'full' -> 0/1; 0/1 unchanged; anything else -> 0.
def line_method(method = None):
    if method in line_methods:
        return line_methods.index(method)
    if method in binary:
        return int(method)
    return 0


# Validate the scope a line method applies to. Accepts 'line', 'fill', or 'both'; anything else (including None) falls back to 'both'.
def line_method_scope(scope = None):
    return scope if scope in line_method_scopes else 'both'
