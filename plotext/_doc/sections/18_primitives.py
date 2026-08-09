# Primitives section: the creation methods of every plotext primitive

from plotext._doc.tools import *
from plotext._signal.point_filled import point
from plotext._primitives.pixel import pixel as pixel_class
from plotext._primitives.colorize import colorize as colorize_class
from plotext._primitives.marker import marker as marker_class
from plotext._primitives.matrix import matrix as matrix_class
from plotext._primitives.box import line as line_class


section('primitives')


add(pixel_class)
doc("A pixel bundles a foreground color, background color and style into one object.")
source("plotext")
par("foreground", "Foreground color; " + explanation("colors"), explanation("color"))
par("background", "Background color; " + explanation("colors"), explanation("color"))
par("style", "Styling attributes; " + explanation("styles"), explanation("style"))
out("A pixel object", explanation("pixel"))


add(colorize_class)
doc("Wraps a string with color and style attributes.")
source("plotext")
par("string", "The string to colorize", explanation("string"), repr(""))
par("pixel", "Pixel that determines the color and style", explanation("pixel_par"))
out("A colorized object", explanation("colorize"))


add(matrix_class)
doc("Creates a matrix of the given dimensions, with an optional default pixel.")
source("plotext")
par("width", "Matrix width in columns", explanation("int"))
par("height", "Matrix height in rows", explanation("int"))
par("pixel", "Default pixel used for every cell", explanation("pixel_par"), doc_default_pixel)
out("A matrix object", explanation("matrix"))


add(marker_class)
doc("Creates a marker used to render a point on the plot canvas. This is a symbol with an optional pixel that carries its color and style.")
source("plotext")
par("symbol", "The symbol to use to represent the point on canvas. It could be a single character; a string code from plotext.markers(), a raw string or a plotext.matrix / plotext.colorize (ha and va parameters apply)", explanation("marker_symbol"), explanation("marker_default"))
par("pixel", "Pixel that determines the marker's color and style", explanation("pixel_par"))
par("ha", "Horizontal alignment of a matrix/colorize marker around the data point. Ignored for single-cell markers", explanation("alignment_h"), -1)
par("va", "Vertical alignment of a matrix/colorize marker around the data point. Ignored for single-cell markers", explanation("alignment_v"), -1)
out("A marker object", explanation("marker"))


add(line_class)
doc("Creates a line marker: a single character drawn as a horizontal or vertical line, matching the plot axes styles. Useful as a signal marker to draw straight lines across the canvas.")
source("plotext")
par("orientation", "Line orientation: 0 for horizontal, 1 for vertical", explanation("int"), 0)
par("pixel", "Pixel that determines the line color and style", explanation("pixel_par"))
par("style", "Line style. " + explanation("line_styles"), explanation("line_style"), repr('default'))
out("A line object", explanation("line"))
