# Shapes and text section: rectangle, polygon, segment, line and text signals

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class
from plotext._settings import defaults


section('shapes and text')


add(plot_class.rectangle)
doc("Creates a rectangle signal between the given x and y ranges.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("x", "x coordinates of the rectangle corners", explanation("couple"), (0, 1))
par("y", "y coordinates of the rectangle corners", explanation("couple"), (0, 1))
par("marker", "Symbol used to render the rectangle", explanation("marker_par"), explanation("marker_default"))
par("lines", "draws the rectangle's outline; otherwise only the four corner vertices are drawn", explanation("bool"), True)
par("fill", "fills the rectangle's body with markers", explanation("bool"), True)
par("label", "Optional label drawn at the rectangle's center. " + explanation("label_colors"), explanation("label"), None)
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
out("The rectangle signal", explanation("signal"))


add(plot_class.polygon)
doc("Creates a polygon signal centered at the given coordinates.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("x", "The polygon center x coordinate", explanation("float"), 0)
par("y", "The polygon center y coordinate", explanation("float"), 0)
par("radius", "Distance of each vertex from the center; for a circle it is the actual radius", explanation("float"), 1)
par("sides", "Number of polygon sides; values above ~50 approximate a circle", explanation("int"), 3)
par("up", "1 places a vertex at the top, 0 places a flat side at the top, any value in between produces a custom tilt", explanation("float"), 0)
par("marker", "Symbol used to render the polygon vertices", explanation("marker_par"), explanation("marker_default"))
par("lines", "draws the polygon outline between consecutive vertices, otherwise only the vertex points are drawn", explanation("bool"), True)
par("fill", "connects each vertex to the polygon center (x, y) with a line; with lines=True the polygon appears filled, with lines=False only the vertex-to-center fills are drawn", explanation("bool"), False)
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
out("The polygon signal", explanation("signal"))


add(plot_class.segment)
doc("Creates a straight line segment between two endpoints.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("x", "x coordinates of the segment endpoints", explanation("couple"))
par("y", "y coordinates of the segment endpoints", explanation("couple"))
par("marker", "Symbol used to render the segment", explanation("marker_par"), explanation("marker_default"))
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
out("The segment signal", explanation("signal"))


add(plot_class.line)
doc("Adds a horizontal or vertical line spanning the whole plot canvas at the given coordinate. The line is added directly to the plot's draw sequence.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("position", "Position of the line along the perpendicular axis: a y value when horizontal, an x value when vertical", explanation("value"))
par("orientation", "Line orientation, either horizontal (or h) or vertical (or v)", explanation("orientation"), repr("horizontal"))
par("relative", "measures position relative to the axis units and limits, otherwise in character cells", explanation("bool"), True)
par("pixel", "Pixel used to draw the line", explanation("pixel_par"), defaults.pixels["line"])
par("style", "Line drawing style. " + explanation("line_styles"), explanation("line_style"), repr('default'))
par("label", "Legend label for the line", explanation("label"), None)
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
past_out("plotext.figure.draw")


add(plot_class.text)
doc("Creates a text annotation signal at the given coordinates.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("x", "X coordinate of the text", explanation("value"))
par("y", "Y coordinate of the text", explanation("value"))
par("label", "Text content", explanation("label"))
par("orientation", "Text orientation, horizontal or vertical", explanation("orientation"), repr("horizontal"))
par("alignment", "Alignment along the writing direction", explanation("alignment_text"), repr("left"))
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
out("The text signal", explanation("signal"))
