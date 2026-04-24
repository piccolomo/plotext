# Boolean and status validation utilities

from plotext._settings.constants.numerical import binary


# Keep value as-is, returning the default when None
def status(value, default):
    return value if value is not None else default


# Coerce input to boolean, falling back to the default when not bool-like
def boolean(element=None, default=False):
    return bool(element) if isinstance(element, bool) or element in binary else default
