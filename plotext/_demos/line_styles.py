# The line styles demo: one box per style, with a middle horizontal and vertical line.

from plotext._primitives.colorize import colorize
from plotext._methods.string import pad
from plotext._demos.tools import blank, title, note


# One box per style, with a middle horizontal and vertical line inside; the glyphs mirror the C tables in utility/maps/high_def.cpp, where missing pieces borrow the default glyphs, as in real rendering
box_samples = [
    ('default', ['┌─┬─┐', '├─┼─┤', '└─┴─┘']),
    ('double',  ['╔═╦═╗', '╠═╬═╣', '╚═╩═╝']),
    ('heavy',   ['┏━┳━┓', '┣━╋━┫', '┗━┻━┛']),
    ('dotted',  ['┌┈┬┈┐', '├┈┼┈┤', '└┈┴┈┘']),
    ('rounded', ['╭─┬─╮', '├─┼─┤', '╰─┴─╯']),
]


# Display the available line and axis styles in a two column grid, each style as a box with a middle horizontal and vertical line
def line_styles():
    column = 12
    block = None
    for index in range(0, len(box_samples), 2):
        left_name, left_rows = box_samples[index]
        right = box_samples[index + 1] if index + 1 < len(box_samples) else None
        piece = title(pad(left_name, column) + (right[0] if right else '')).matrix()
        for row in range(len(left_rows)):
            line = pad(left_rows[row], column) + (right[1][row] if right else '')
            piece = piece / colorize(line)
        block = piece if block is None else block / blank / piece
    block = block / blank / note("rounded has no effect in line(), error(), event() and grid(), where it renders as default; axes() displays every style")
    block.print()
