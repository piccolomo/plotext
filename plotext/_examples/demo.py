# Demo: reference tables of plotext colors, styles and markers, printed with live styling

from math import ceil
from plotext._primitives.colorize import colorize
from plotext._primitives.marker import marker as marker_class
from plotext._methods.string import pad
from plotext._settings.constants.enums import color_codes, style_codes, marker_codes, hd_markers_codes
from plotext._methods.sequence import unique


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
    print(colorize(pad('black', pad_length), 'black', 'gray+'), end='')
    colorize(pad('white', pad_length), 'white', 'gray+').print()
    colorize(pad('default', pad_length * 2)).print()
    note = colorize("Note: ") + colorize("yellow", "yellow") + " is alias for " + colorize("orange+", "orange+")
    print()
    note.print()

    # Print integer color codes
    colorize("\n\nInteger Color Codes", style='bold').print()
    for row in range(rows):
        for col in range(cols):
            end = '' if col != cols - 1 else '\n'
            print(colorize(pad(color_index(col, row), 5), color_index(col, row)), end=end)

    # Print RGB example
    rgb = (10, 123, 150)
    print(colorize("\n\nRGB Tuples", style='bold'), end=' like ')
    print(colorize(str(rgb), foreground=rgb, style='bold'), end=' or ')
    rgb = (150, 12, 120)
    colorize(str(rgb), foreground=rgb, style='bold').print()
    note = colorize("Note: each integer in the tuple should be between 0 and 255")
    note.print()


# Pre-create colorized style codes
styles_colorized = [colorize(el, style=el) for el in style_codes]


# Display available text styles
def styles():
    [c.print() for c in styles_colorized]
    style = 'bold italic dim'
    print()
    eg = colorize('multiple styles are accepted', 'cyan+')
    eg += ", eg: "
    eg += colorize(style, style=style)
    eg.print()


# Display available marker codes (HD codes and named character codes)
def markers():
    marker_pad = 12
    grid_cols = 4

    # HD marker codes (sub-character resolution)
    colorize("HD Marker Codes", style='bold').print()
    hd_codes = [c for c in hd_markers_codes if c != 'none']
    for code in hd_codes:
        default = '  [default]' if code == 'hd' else ''
        print(f"  {pad(code, marker_pad)} {marker_class(code)}{default}")

    # Named character marker codes
    print()
    colorize("Character Marker Codes", style='bold').print()
    for row in range(ceil(len(marker_codes) / grid_cols)):
        line = ""
        for col in range(grid_cols):
            i = row * grid_cols + col
            if i >= len(marker_codes): break
            code = marker_codes[i]
            line += f"  {pad(code, marker_pad)} {marker_class(code)}  "
        print(line)

    print()
    note = colorize("Note: ") + "any single character can also be used as a marker."
    note.print()
