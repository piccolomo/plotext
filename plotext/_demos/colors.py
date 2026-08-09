# The colors demo: the string codes, the integer codes and the rgb tuples.

from plotext._primitives.colorize import colorize
from plotext._methods.string import pad
from plotext._constants.enums import color_codes
from plotext._demos.tools import background, pad_length, rows_number, columns_number, color_index, blank, indent_pad, title, note


# The string color codes block: every code beside its + variant, then black, white, default and the yellow note.
def get_string_colors_block():
    names = []
    for code in color_codes:
        name = code.replace('+', '')
        if name not in names + ['default', 'black', 'white']:
            names.append(name)
    colors_no_plus, colors_plus = names, [name + '+' for name in names]
    colors_no_plus = [colorize(indent_pad + pad(color, pad_length), pixel = (color, background)) for color in colors_no_plus]
    colors_plus = [colorize(pad(color, pad_length), pixel = (color, background)) for color in colors_plus]

    block = title("String Color Codes").matrix() / blank
    for color, color_plus in zip(colors_no_plus, colors_plus):
        block = block / (color + color_plus)

    black_white = colorize(indent_pad + pad('black', pad_length), pixel = ('black', 'gray+')) + colorize(pad('white', pad_length), pixel = 'white')
    default_row = colorize(indent_pad + pad('default', pad_length))
    yellow_note = note(colorize("yellow", "yellow") + " is alias for " + colorize("orange+", "orange+"), indented = True)
    return block / black_white / default_row / blank / yellow_note


# The integer color codes block: the 256 codes in a grid, each row built by joining its cells.
def get_integer_colors_block():
    block = title("Integer Color Codes").matrix() / blank
    for row in range(rows_number):
        cells = [colorize(pad(color_index(column, row), 5), color_index(column, row)) for column in range(columns_number)]
        row_matrix = colorize(indent_pad) + cells[0]
        for cell in cells[1:]:
            row_matrix = row_matrix + cell
        block = block / row_matrix
    return block


# The rgb tuples block: two colored examples and the note on their range.
def get_rgb_block():
    first, second = (10, 123, 150), (150, 12, 120)
    line = (title("RGB Tuples") + " like "
            + colorize(str(first), pixel = (first, None, 'bold')) + " or "
            + colorize(str(second), pixel = (second, None, 'bold')))
    return line / blank / note("each integer in the tuple should be between 0 and 255")


# Display color codes
def colors():
    block = get_string_colors_block() / blank / blank / get_integer_colors_block() / blank / blank / get_rgb_block()
    block.print()
