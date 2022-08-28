"""\nplotext plots directly on terminal"""
    
__name__ = "plotext"
__version__ = "5.1.0"

from ._core import *
from ._test import test
from .plotext_cli import build_parser


def themes():
    import plotext as plt
    from plotext._utility import themes
    from math import sqrt, ceil
    themes = list(themes.keys())[::]
    l = len(themes)
    rows = int(sqrt(l))
    cols = ceil(l / rows)
    y1 = plt.sin(periods = 1)
    y2 = [-el for el in plt.sin(periods = 1)]
    plt.clf()
    plt.subplots(rows, cols)
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            i = (row - 1) * cols + col - 1
            if i < l:
                plt.subplot(row, col)
                plt.theme(themes[i])
                plt.title(themes[i])
                plt.scatter(y1); plt.scatter(y2)
    plt.show()
    plt.clf()

def markers():
    import plotext as plt
    from plotext._utility import marker_codes, hd_symbols
    from math import sqrt, ceil
    markers = list(hd_symbols.keys())[::-1] + list(marker_codes.keys())
    l = len(markers)
    rows = int(sqrt(l))
    cols = ceil(l / rows)
    y = plt.sin(1)
    plt.clf(); plt.theme('pro'); plt.xfrequency(0); plt.yfrequency(0); plt.frame(1)
    plt.subplots(rows, cols)
    plt.frame(0)
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            i = (row - 1) * cols + col - 1
            if i < l:
                plt.subplot(row, col)
                plt.frame(1)
                default = ' [default]' if markers[i] == 'hd' else ''
                plt.title(markers[i] + default)
                plt.scatter(y, marker = markers[i])
                plt.ticks_style('bold')
                #plt.ticks_color(plt._utility.title_color)
    plt.show()
    plt.clf()

