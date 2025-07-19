from plotext._colorize import colorize
from plotext._methods import *
from plotext._constants import color_codes, style_codes
from math import ceil


bg = 'default'
pad_length = 10
m = 256
cols = 18
rows = ceil(m / cols)
color_index = lambda col, row: row * cols + col if row * cols + col < m else ''

pad = string_methods.pad

def colors():
    colors_no_plus = list_methods.unique([el.replace('+', '') for el in color_codes if el not in ['default', 'black', 'white']])
    colors_plus = [el + '+' for el in colors_no_plus]
    colors_no_plus = [colorize(pad(color, pad_length), foreground = color, background = bg) for color in colors_no_plus]
    colors_plus = [colorize(pad(color, pad_length), foreground = color, background = bg) for color in colors_plus]
    color_codes_colorized = [c  + cp for c, cp in zip(colors_no_plus, colors_plus)]

    colorize("String Color Codes", style = 'bold').print()
    [c.print() for c in color_codes_colorized]
    colorize(pad('black', pad_length), 'black', 'gray+').print(end = ''); colorize(pad('white', pad_length), 'white', 'gray+').print()
    colorize(pad('default', pad_length * 2)).print()
    
    colorize("\nInteger Color Codes", style = 'bold').print()
    [[colorize(pad(color_index(col, row), 5), color_index(col, row)).print(end = '' if col != cols - 1 else '\n') for col in range(cols)] for row in range(rows)]
    
    rgb = (10, 123, 150)
    colorize("\nRGB Tuples like", style = "bold").print(end = ': '); colorize(rgb, rgb, "bold", style = "bold").print()


styles_colorized = [colorize(el, style = el) for el in style_codes]

def styles():
    [c.print() for c in styles_colorized]
    style = 'bold italic dim'
    print()
    eg = colorize('multiple styles are accepted', 'cyan+')
    eg +=", eg: "; eg += colorize(style, style = style)
    eg.print()


# def themes():
#     themes = list(_themes.keys())[::]
#     l = len(themes)
#     rows = int(sqrt(l))
#     cols = ceil(l / rows)
#     y1 = sin(periods = 1)
#     y2 = sin(periods = 1, phase = -1)
#     figure.clf()
#     figure.subplots(rows, cols)
#     for row in range(1, rows + 1):
#         for col in range(1, cols + 1):
#             i = (row - 1) * cols + col - 1
#             if i < l:
#                 subplot = figure.subplot(row, col)
#                 subplot.theme(themes[i])
#                 subplot.title(themes[i])
#                 subplot.scatter(y1); subplot.plot(y2)
#     figure.show()
#     figure.clf()