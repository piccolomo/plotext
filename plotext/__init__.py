"""\nplotext plots directly on terminal"""
    
__name__ = "plotext"
__version__ = "5.0.0"

from plotext._core import *
from plotext._test import test

def themes():
    import plotext as plt
    from plotext._utility import themes
    from math import sqrt
    themes = list(themes.keys())[::]
    l = len(themes)
    rows = int(sqrt(l))
    cols = l // rows
    y = plt.sin()
    plt.clf()
    plt.subplots(rows, cols)
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            i = (row - 1) * cols + col - 1
            if i < l:
                plt.subplot(row, col)
                plt.theme(themes[i])
                plt.title(themes[i])
                plt.scatter(y)
    plt.show()
    plt.clf()

def markers():
    import plotext as plt
    from plotext._utility import marker_codes, hd_symbols
    from math import sqrt
    markers = list(hd_symbols.keys()) + list(marker_codes.keys())
    l = len(markers)
    rows = int(sqrt(l))
    cols = l // rows
    y = plt.sin(1)
    plt.clf(); plt.theme('pro'); plt.xfrequency(0); plt.yfrequency(0); plt.frame(1)
    plt.subplots(rows, cols)
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            i = (row - 1) * cols + col - 1
            if i < l:
                plt.subplot(row, col)
                plt.title(markers[i])
                plt.scatter(y, marker = markers[i])
    plt.show()
    plt.clf()

def colors():
    from plotext._utility import colors, no_duplicates, colorize, pad_string
    print(colorize("String Color Codes", style = ''))
    colors = no_duplicates([el.replace('+', '') for el in colors if el not in ['default', 'black', 'white']])
    c = [colorize(pad_string(el, 10), el) for el in colors]
    cp = [colorize(el + '+', el + '+') for el in colors]
    c = [' ' + c[i]  + cp[i] for i in range(len(c))]
    c = '\n'.join(c)
    print(' default')
    print(colorize(' ' + pad_string('black', 10), 'black') + colorize('white', 'white'))
    print(c)
    print(colorize("\n\nInteger Color Codes:", style = ''))
    c = ''
    for row in range(16):
        cr = ' '
        for col in range(16):
            i = row * 16 + col
            cr += colorize(pad_string(i, 5), i)
        c += cr + '\n'
    print(c)

    

