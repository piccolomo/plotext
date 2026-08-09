# The markers demo: the named character codes and the higher resolution ones.

from math import ceil
from plotext._primitives.colorize import colorize
from plotext._primitives.marker import marker as marker_class
from plotext._methods.string import pad
from plotext._constants.enums import symbol_codes, hd_markers_codes
from plotext._demos.tools import blank, indent_pad, title, note


# Display available marker codes (higher-resolution codes and named character symbols)
def markers():
    marker_pad = 12
    grid_cols = 4

    # Named character symbol codes
    sym_block = title("Named Character Codes").matrix() / blank
    for row in range(ceil(len(symbol_codes) / grid_cols)):
        line = ""
        for column in range(grid_cols):
            index = row * grid_cols + column
            if index >= len(symbol_codes): break
            code = symbol_codes[index]
            line += f"{indent_pad}{pad(code, marker_pad)} {marker_class(code)._get_model()}  "
        sym_block = sym_block / colorize(line)
    sym_block = sym_block / blank / note("any single character can also be used as a marker.", indented = True)

    # Higher-resolution marker codes: each splits one character cell into sub-cells for finer plotting
    hd_codes = hd_markers_codes
    hd_block = title("Higher Resolution Codes").matrix() / blank
    for code in hd_codes:
        default = '  [default]' if code == 'hd' else ''
        hd_block = hd_block / colorize(f"{indent_pad}{pad(code, marker_pad)} {marker_class(code)._get_model()}{default}")

    block = sym_block / blank / blank / hd_block
    block.print()
