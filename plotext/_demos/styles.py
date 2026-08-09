# The styles demo: every style code printed in its own style.

from plotext._primitives.colorize import colorize
from plotext._constants.enums import style_codes
from plotext._demos.tools import blank, note


# Pre-create colorized style codes
styles_colorized = [colorize(el, pixel = (None, None, el)) for el in style_codes]


# Display available text styles
def styles():
    style = 'bold italic dim'
    block = styles_colorized[0].matrix()
    for c in styles_colorized[1:]:
        block = block / c
    block = block / blank / note("multiple styles are accepted, for example: " + colorize(style, pixel = (None, None, style)))
    block.print()
