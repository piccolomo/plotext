# Limits validation and normalization utilities

from plotext._constants.enums import limit_alignments, scales
from plotext._methods.ruler import almost_equal
from plotext._methods.sequence import replace_none, safe_min, safe_max

# Validate limits alignment
def limits_alignment(alignment):
    return alignment if alignment in limit_alignments else limit_alignments[0]


# Expand one limit range to include another. None is treated as "no
# constraint" — that side defers to the other. When both have a value,
# the lower bound is the smaller and the upper bound is the greater.
# Returns a new list; inputs are never mutated.
def expand(limits, new_limits):
    m0, M0 = limits
    m1, M1 = new_limits
    m = safe_min([m0, m1])
    M = safe_max([M0, M1])
    [m, M] = [m - 1, M + 1] if m is not None and almost_equal(m, M, 5) else [m, M]
    return [m, M]


# Merge two limit ranges into the smallest containing range. Defaults
# new_limits to limits when None is passed. When merge=True, both ranges
# are unioned via expand(); when merge=False (the default), only None
# entries in limits are filled from new_limits. Expands a single-point
# range (a almost-equal b) to (a-1, b+1) so the chart isn't degenerate.

def limits(limits, new_limits, merge = False):
    limits = replace_none(limits, new_limits)
    limits = expand(limits, new_limits) if merge else limits
    return limits


# Validate scale
def scale(scale):
    return scale if scale in scales else scales[0]