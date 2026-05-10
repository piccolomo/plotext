# Bar plot geometry helpers

from plotext._constants.enums import orientations, orientations_short
from plotext._methods.ruler import linspace


# Compute the q-th quantile of a flat sequence (linear interpolation between adjacent samples).
def quantile(data, q):
    data = sorted(data)
    index = q * (len(data) - 1)
    return data[int(index)] if index.is_integer() else (data[int(index)] + data[int(index) + 1]) / 2


# Compute box-plot summaries from per-category data lists. Returns parallel (min, q1, median, q3, max) lists in ascending order.
def box_data(data):
    return tuple(zip(*((min(d), quantile(d, 0.25), quantile(d, 0.50), quantile(d, 0.75), max(d)) for d in data)))


# Bin a flat data sequence into a histogram. Returns (histx, histy) — bin centres and counts.
# norm=True returns densities (each bin divided by total count) so all bins sum to 1.
def hist_data(data, bins = 10, norm = False):
    bins = 0 if len(data) == 0 else bins
    m, M = (min(data, default = 0), max(data, default = 0))
    indices = [(el - m) / (M - m) * bins if el != M else bins - 1 for el in data]
    indices = [int(el) for el in indices]
    histx = linspace(m, M, bins)
    histy = [0] * bins
    for i in indices:
        histy[i] += 1
    if norm and data:
        histy = [el / len(data) for el in histy]
    return histx, histy


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
