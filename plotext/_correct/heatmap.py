# Convert a 2D grid of numbers into a 2D of (r, g, b) triples for heatmap rendering.

from plotext._constants.enums import viridis, symbol_codes


# Validate a heatmap cell symbol; falls back to '█' on None or invalid. Higher-resolution codes rejected: a single character carries only one foreground colour, so sub-cell rendering can't show distinct per-data-point colours within one cell.
def symbol(value):
    if value is None: return '█'
    if isinstance(value, str) and (len(value) == 1 or value in symbol_codes): return value
    return '█'


# Sample an (r, g, b) colour from a stops list at fractional position t in [0, 1] via linear interpolation between adjacent stops.
def _sample(stops, t):
    n = len(stops) - 1
    i = min(int(t * n), n - 1)
    f = t * n - i
    a, b = stops[i], stops[i + 1]
    return tuple(int(a[k] + (b[k] - a[k]) * f) for k in range(3))


# Map every cell of a 2D grid of numbers to an (r, g, b) triple via the named colormap; values are normalized by the grid min/max. Supported names: 'gray', 'viridis'.
def colormap(data, name = 'gray'):
    flat = [v for row in data for v in row]
    vmin, vmax = min(flat), max(flat)
    if vmin == vmax: return [[(127, 127, 127)] * len(row) for row in data]
    span = vmax - vmin
    if name == 'viridis':
        return [[_sample(viridis, (v - vmin) / span) for v in row] for row in data]
    return [[(int((v - vmin) / span * 255),) * 3 for v in row] for row in data]
