# Helpers for plotext text drawables


# Aggregated limits across a list of texts on the given axis (0 = x, 1 = y) and side
# (0 / 1). Relative texts are skipped because their coordinates are in canvas
# space, not data space. Returns (lo, hi) or None when no text matches.
def text_limits(texts, axis, side):
    values = [(t._get_x() if axis == 0 else t._get_y())
              for t in texts if not t._is_relative()
              and (t._get_xside() if axis == 0 else t._get_yside()) == side]
    return (min(values), max(values)) if values else None
