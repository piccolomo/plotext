# Alignment, orientation, slice and matrix normalization utilities

from builtins import slice as _slice
from plotext._primitives.colorize import colorize as colorize_class
from plotext._settings.constants.enums import (
    orientations,
    orientations_short,
    ha as ha_values,
    va as va_values,
    ha_short)


# Convert input into a matrix representation
def matrix(obj):
    if isinstance(obj, colorize_class):
        return obj.get_matrix()
    if isinstance(obj, str):
        return colorize_class(obj).get_matrix()
    return obj


# Normalize slice object for given number of bins
def slice(key, bins):
    if isinstance(key, int):
        key = _slice(key, key + 1)
    if key.start is None:
        key = _slice(0, key.stop)
    if key.stop is None:
        key = _slice(key.start, bins)
    return key


# Validate orientation
def orientation(orientation):
    return orientation if orientation in orientations + orientations_short else orientations[0]


# Horizontal alignment normalization
def ha(alignement):
    if alignement in ha_values:
        return ha_values.index(alignement) - 1
    if alignement in ha_short:
        return alignement
    return -1


# Vertical alignment normalization
def va(alignement):
    if alignement in va_values:
        return va_values.index(alignement) - 1
    if alignement in ha_short:
        return alignement
    return 1