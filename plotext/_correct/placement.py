# Validation utilities for placement parameters (alignment and orientation)

from plotext._constants.enums import horizontal_alignments, horizontal_alignments_short, vertical_alignments, vertical_alignments_short, alignments_int, orientations


# Validate the alignment for the given orientation: left, center, right when horizontal, top, center, bottom when vertical, short forms and the codes -1, 0, 1 accepted; anything else gives the caller default.
def alignment(value = None, orientation = 0, default = -1):
    names  = horizontal_alignments       if orientation == 0 else vertical_alignments
    shorts = horizontal_alignments_short if orientation == 0 else vertical_alignments_short
    if value in names:
        return alignments_int[names.index(value)]
    if value in shorts:
        return alignments_int[shorts.index(value)]
    if value in alignments_int:
        return value
    return default


# Validate and normalize orientation: 'horizontal'/'h' -> 0; 'vertical'/'v' -> 1; 0/1 unchanged; anything else -> default
def orientation(value = None, default = 0):
    if value in ('horizontal', 'h', 0):
        return 0
    if value in ('vertical', 'v', 1):
        return 1
    return default
