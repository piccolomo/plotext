# Limits validation and normalization utilities

from plotext._constants.enums import limit_alignments, scales
from plotext._methods.ruler import almost_equal
from plotext._methods.sequence import replace_none, safe_min, safe_max

# Validate limits alignment
def limits_alignment(alignment):
    return alignment if alignment in limit_alignments else limit_alignments[0]


# Expand one limit range to include another, None meaning no constraint on that side; a new list is returned, the inputs untouched.
def expand(limits, new_limits):
    lower, upper = limits
    new_lower, new_upper = new_limits
    lower = safe_min([lower, new_lower])
    upper = safe_max([upper, new_upper])
    [lower, upper] = [lower - 1, upper + 1] if lower is not None and almost_equal(lower, upper, 5) else [lower, upper]
    return [lower, upper]


# Merge two limit ranges into the smallest containing one: with merge, both are united; without it, only the None sides are filled; a single point range is widened by one on each side.
def merge_limits(limits, new_limits, merge = False):
    limits = replace_none(limits, new_limits)
    limits = expand(limits, new_limits) if merge else limits
    return limits


# Validate scale
def scale(scale):
    return scale if scale in scales else scales[0]