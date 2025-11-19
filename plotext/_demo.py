from math import ceil
from plotext._colorize import colorize
from plotext._methods.string import pad
from plotext._constants import color_codes, style_codes
from plotext._methods.list import unique

# Background and layout defaults
bg = 'default'
pad_length = 10
m = 256
cols = 18
rows = ceil(m / cols)
color_index = lambda col, row: row * cols + col if row * cols + col < m else ''


# Display color codes
def colors():
    # Prepare color codes with and without '+'
    colors_no_plus = unique([el.replace('+', '') for el in color_codes if el not in ['default', 'black', 'white']])
    colors_plus = [el + '+' for el in colors_no_plus]

    # Colorize strings
    colors_no_plus = [colorize(pad(color, pad_length), foreground=color, background=bg) for color in colors_no_plus]
    colors_plus = [colorize(pad(color, pad_length), foreground=color, background=bg) for color in colors_plus]
    color_codes_colorized = [c + cp for c, cp in zip(colors_no_plus, colors_plus)]

    # Print string color codes
    colorize("String Color Codes", style='bold').print()
    [c.print() for c in color_codes_colorized]
    colorize(pad('black', pad_length), 'black', 'gray+').print(end=''); colorize(pad('white', pad_length), 'white', 'gray+').print()
    colorize(pad('default', pad_length * 2)).print()

    # Print integer color codes
    colorize("\nInteger Color Codes", style='bold').print()
    [[colorize(pad(color_index(col, row), 5), color_index(col, row)).print(end='' if col != cols - 1 else '\n') 
      for col in range(cols)] for row in range(rows)]

    # Print RGB example
    rgb = (10, 123, 150)
    colorize("\nRGB Tuples like", style="bold").print(end=': ')
    colorize(rgb, rgb, "bold", style="bold").print()

# Pre-create colorized style codes
styles_colorized = [colorize(el, style=el) for el in style_codes]


# Display available text styles
def styles():
    [c.print() for c in styles_colorized]
    style = 'bold italic dim'
    print()
    eg = colorize('multiple styles are accepted', 'cyan+')
    eg += ", eg: "; eg += colorize(style, style=style)
    eg.print()
