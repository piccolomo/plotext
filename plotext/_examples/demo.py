# Demo: reference tables of plotext colors, styles and markers, printed with live styling

from math import ceil
from plotext._primitives.colorize import colorize
from plotext._primitives.marker import marker as marker_class
from plotext._methods.string import pad
from plotext._constants.enums import color_codes, style_codes, symbol_codes, hd_markers_codes
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

    # Colorize.
    colors_no_plus = [colorize(pad(c, pad_length), foreground=c, background=bg) for c in colors_no_plus]
    colors_plus = [colorize(pad(c, pad_length), foreground=c, background=bg) for c in colors_plus]
    color_codes_colorized = [c + cp for c, cp in zip(colors_no_plus, colors_plus)]

    # Build the whole string-codes block as one stacked matrix; one print, no buffer reordering.
    header = colorize("String Color Codes", style='bold')
    black_white = colorize(pad('black', pad_length), 'black', 'gray+') + colorize(pad('white', pad_length), 'white')
    default_row = colorize(pad('default', pad_length))
    note = colorize("Note: ") + colorize("yellow", "yellow") + " is alias for " + colorize("orange+", "orange+")
    blank = colorize("")

    block = header.get_matrix()
    for r in color_codes_colorized:
        block = block / r
    block = block / black_white / default_row / blank / note / blank

    # Integer color codes: each row is the horizontal concat of cols cells
    int_header = colorize("Integer Color Codes", style='bold')
    block = block / blank / int_header
    for row in range(rows):
        row_cells = [colorize(pad(color_index(col, row), 5), color_index(col, row)) for col in range(cols)]
        row_matrix = row_cells[0]
        for cell in row_cells[1:]:
            row_matrix = row_matrix + cell
        block = block / row_matrix

    # RGB tuples row
    rgb1, rgb2 = (10, 123, 150), (150, 12, 120)
    rgb_line = (colorize("RGB Tuples", style='bold') + " like "
                + colorize(str(rgb1), foreground=rgb1, style='bold') + " or "
                + colorize(str(rgb2), foreground=rgb2, style='bold'))
    rgb_note = colorize("Note: each integer in the tuple should be between 0 and 255")
    block = block / blank / rgb_line / rgb_note
    block.print()


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


# Display available marker codes (higher-resolution codes and named character symbols)
def markers():
    marker_pad = 12
    grid_cols = 4

    # Higher-resolution marker codes (each splits one character cell into sub-cells for finer plotting)
    colorize("Higher Resolution Marker Codes", style='bold').print()
    hd_codes = [c for c in hd_markers_codes if c != 'none']
    for code in hd_codes:
        default = '  [default]' if code == 'hd' else ''
        print(f"  {pad(code, marker_pad)} {marker_class(code)._get_model()}{default}")

    # Named character symbol codes
    print()
    colorize("Character Symbol Codes", style='bold').print()
    for row in range(ceil(len(symbol_codes) / grid_cols)):
        line = ""
        for col in range(grid_cols):
            i = row * grid_cols + col
            if i >= len(symbol_codes): break
            code = symbol_codes[i]
            line += f"  {pad(code, marker_pad)} {marker_class(code)._get_model()}  "
        print(line)

    print()
    note = colorize("Note: ") + "any single character can also be used as a marker."
    note.print()


# Display available colour themes as a grid of mini-plots, one cell per theme
def themes():
    from math import sqrt, ceil
    from plotext._kernel.api import figure
    from plotext._settings.themes import themes as theme_registry
    from plotext._methods.sequence import sin

    names = list(theme_registry)
    rows = int(sqrt(len(names)))
    cols = ceil(len(names) / rows)
    y1, y2 = sin(periods = 1), sin(periods = 1.5)

    figure.clear()
    figure.subplots(rows, cols)
    for i, name in enumerate(names):
        sub = figure.subplot(i // cols + 1, i % cols + 1)
        sub.theme(name)
        sub.title(name)
        sub.draw(sub.signal(y1).label("sin"))
        sub.draw(sub.signal(y2).lines(True).label("-sin"))
    figure.show()
    figure.clear()
