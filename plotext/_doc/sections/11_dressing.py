# Plot dressing section: title, label, axes, canvas and legend

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class
from plotext._settings import defaults


section('plot dressing')


add(plot_class.title)
doc("Sets the title of this plot.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("label", "the title label", explanation("label"))
out("The figure itself", explanation("figure"))


add(plot_class.label)
doc("Sets the label of the selected axis and axis side.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("label", "the axis label", explanation("label"))
par("axis", "Axis to access: x, y, or both", explanation("axis_multiple"), repr('x'))
par("side", "Axis side to access", explanation("side_multiple"), 0)
past_out("plotext.figure.title")


add(plot_class.axes)
doc("Controls the visibility, style and pixel of the selected axes, all four by default.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("active", "Whether the axis is visible", explanation("bool"), True)
par("style", "Axis line style. " + explanation("line_styles"), explanation("axis_style"), repr('default'))
par("pixel", "Pixel used to paint the axis", explanation("pixel_par"), defaults.pixels["axis"])
par("axis", "Axis to access: x, y, or both", explanation("axis_multiple"), repr('both'))
par("side", "Axis side to access: one or both", explanation("side_multiple"), repr('both'))
past_out("plotext.figure.title")



add(plot_class.canvas)
doc("Sets the background color of the plot canvas: the central area of the plot where points are drawn. The canvas holds no characters of its own: the foreground colors and styles on it come from the drawn signals, each through its marker. These markers are colored automatically, unless explicitly set by the user.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("background", "Canvas background color; the color default leaves it unpainted, so whatever the terminal shows stays behind the plot. " + explanation("colors"), explanation("color"), repr('white'))
past_out("plotext.figure.title")


add(plot_class.legend)
doc("Configures the plot legend in the canvas: visibility, position, alignment and color. The legend appears on its own as soon as a signal, or a line, carries a label, listing only what is labelled; this method is needed to move it, color it, or switch it off with active = False.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("active", "Whether the legend is visible; False keeps it hidden even when labels are present", explanation("bool"), True)
par("x", "X position of the legend anchor", explanation("value"), 0)
par("y", "Y position of the legend anchor", explanation("value"), 0)
par("ha", "Horizontal alignment of the legend: left, center, or right", explanation("alignment_h"), repr('left'))
par("va", "Vertical alignment of the legend: top, center, or bottom", explanation("alignment_v"), repr('top'))
par("relative", "x and y are read in the ruler numerical units, otherwise as character positions inside the canvas", explanation("bool"), False)
par("pixel", "Pixel used to paint the legend: its border, background and plain text labels; colorized labels and the marker samples keep their own colors", explanation("pixel_par"), defaults.pixels["legend"])
par("style", "Line style of the legend box. " + explanation("line_styles"), explanation("axis_style"), repr('default'))
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
past_out("plotext.figure.title")
