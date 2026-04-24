# Limits validation and normalization utilities

from plotext._settings.constants.enums import limit_alignments, scales
from plotext._settings.constants.numerical import directions
from plotext._methods.sequence import replace_none
from plotext._methods.ruler import almost_equal


# Validate limits alignment
def limits_alignment(alignment):
    return alignment if alignment in limit_alignments else limit_alignments[0]


# Validate limits direction
def limits_direction(direction):
    return direction if direction in directions else directions[1]


# Normalize and adjust limits
def limits(limits, new_limits):
    new_limits = limits if new_limits is None else new_limits
    limits = replace_none(limits, new_limits)
    a, b = limits
    return [a - 1, b + 1] if a is not None and almost_equal(a, b, 5) else limits


# Validate scale
def scale(scale):
    return scale if scale in scales else scales[0]