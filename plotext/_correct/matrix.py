# Alignment, orientation, slice and matrix normalization utilities

from builtins import slice as _slice
from plotext._primitives.colorize import colorize as colorize_class
from plotext._constants.enums import (
    orientations,
    orientations_short,
    horizontal_alignments,
    horizontal_alignments_short,
    vertical_alignments,
    vertical_alignments_short,
    alignments_int)


# Convert input into a matrix representation
def matrix(obj):
    if isinstance(obj, colorize_class):
        return obj.matrix()
    if isinstance(obj, str):
        return colorize_class(obj).matrix()
    return obj


# Normalize slice object for given number of bins
def slice(key, bins):
    if isinstance(key, int):
        key = key + bins if key < 0 else key
        if not 0 <= key < bins:
            raise IndexError("matrix index out of range")
        key = _slice(key, key + 1)
    start = 0 if key.start is None else key.start
    stop = bins if key.stop is None else key.stop
    return _slice(min(start, bins), min(stop, bins))


# Validate orientation
def orientation(orientation):
    return orientation if orientation in orientations + orientations_short else orientations[0]


# Horizontal alignment normalization
def ha(alignement):
    if alignement in horizontal_alignments:
        return horizontal_alignments.index(alignement) - 1
    if alignement in horizontal_alignments_short:
        return horizontal_alignments_short.index(alignement) - 1
    if alignement in alignments_int:
        return alignement
    return -1


# Vertical alignment normalization
def va(alignement):
    if alignement in vertical_alignments:
        return vertical_alignments.index(alignement) - 1
    if alignement in vertical_alignments_short:
        return vertical_alignments_short.index(alignement) - 1
    if alignement in alignments_int:
        return alignement
    return 1