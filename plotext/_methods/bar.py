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


# Bin a data sequence into a histogram, giving the bin centers and their counts; with norm, each count is divided by the total, so they sum to 1.
def hist_data(data, bins = 10, norm = False):
    bins = 0 if len(data) == 0 else bins
    lower, upper = (min(data, default = 0), max(data, default = 0))
    indices = [(el - lower) / (upper - lower) * bins if el != upper else bins - 1 for el in data]
    indices = [int(el) for el in indices]
    histx = linspace(lower, upper, bins)
    histy = [0] * bins
    for i in indices:
        histy[i] += 1
    if norm and data:
        histy = [el / len(data) for el in histy]
    return histx, histy


# Compute bar edges from centres and bounds; returns (x_edges, y_edges) as lists of [lo, hi] pairs. The width fraction is applied to the smallest positive spacing between bar centres, so bars never overlap; with duplicate-only centres it falls back to the average spacing.
def bar_edges(x, y_min, y_max, width):
    bins = len(x)
    half_w = width / 2
    if bins > 1:
        x_sorted = sorted(x)
        gaps = [b - a for a, b in zip(x_sorted, x_sorted[1:]) if b > a]
        spacing = min(gaps) if gaps else (max(x) - min(x)) / (bins - 1)
        half_w *= spacing
    x_edges = [[x[i] - half_w, x[i] + half_w] for i in range(bins)]
    y_edges = [[y_min[i],      y_max[i]]      for i in range(bins)]
    return x_edges, y_edges


# True if orientation is vertical ('vertical' or 'v').
def is_vertical(orientation):
    return orientation in (orientations[0], orientations_short[0])
