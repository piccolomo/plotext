# Demo section: colors, styles, markers, line_styles and themes reference printers

from plotext._doc.tools import *
from plotext import colors, styles, markers, line_styles, themes, add_theme


section('demo')


add(colors)
doc("Prints every available color: the named string codes, the 256 integer codes, and the RGB tuple form. Each entry is rendered in its own color.")
source("plotext")

add(styles)
doc("Prints every available text style code (bold, italic, and so on), each rendered in its own style.")
source("plotext")

add(markers)
doc("Prints every available marker code: the named character codes and the higher resolution codes (hd, fhd, braille), each shown next to the characters it renders with.")
source("plotext")

add(line_styles)
doc("Prints every available line and axis style, each shown as a box with a middle horizontal and vertical line, with a note on which methods accept which styles.")
source("plotext")


add(themes)
doc("Displays every available color theme as a grid of mini-plots, one plot per theme, each titled with its name. Use a theme name in plotext.figure.theme() or plotext.figure.subplot().theme() to apply it.")
source("plotext")


add(add_theme)
doc("Registers a custom color theme under the given name, overwriting any existing one. The theme is then applied by name with the theme() method, and shown by plotext.themes().")
source("plotext")
par("name", "The theme name", explanation("string"))
par("canvas", "Canvas background color; " + explanation("colors"), explanation("color"))
par("text", "Pixel shared by the axes, rulers, labels and legend", explanation("pixel_par"))
par("sequence", "The signal colors, completed with the standard palette", "a list of color codes or pixel objects")
par("grid", "Grid lines pixel; if None, they take the text one", explanation("pixel_par"))
