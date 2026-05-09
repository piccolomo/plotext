# Bar plot geometry helpers

from plotext._constants.enums import orientations, orientations_short


# Compute bar edges from centres and bounds; returns (x_edges, y_edges) as lists of [lo, hi] pairs.
def bar_edges(x, y_min, y_max, width):
    bins = len(x)
    half_w = width / 2
    if bins > 1:
        half_w *= (max(x) - min(x)) / (bins - 1)
    x_edges = [[x[i] - half_w, x[i] + half_w] for i in range(bins)]
    y_edges = [[y_min[i],      y_max[i]]      for i in range(bins)]
    return x_edges, y_edges


# True if orientation is vertical ('vertical' or 'v').
def is_vertical(orientation):
    return orientation in (orientations[0], orientations_short[0])
