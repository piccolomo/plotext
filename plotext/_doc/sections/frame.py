# Frame elements: labels (title/label/legend), frame axes (axis/frame), tick rulers (alignment/direction/scale/lim/frequency/ticks/ruler_pixel/tick_alignment/grid/date/convert)

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class
from plotext._constants.numerical import binary
from plotext._settings import defaults


# Labels

add(plot_class.title, name = "title")
doc("Sets the title of this plot.")
par("label", "the title label"); spec(type.label)
out("this plot", type.plot)


add(plot_class.legend, name = "legend")
doc("Configures the plot legend: visibility, position, alignment, colour, and axis anchoring.")
par("status", "Whether the legend is visible"); spec(type.bool, True)
par("x", "X position of the legend anchor"); spec(type.value, repr(None))
par("y", "Y position of the legend anchor"); spec(type.value, repr(None))
par("ha", "Horizontal alignment of the legend: left, center, or right"); spec(type.alignment_h, repr('left'))
par("va", "Vertical alignment of the legend: top, center, or bottom"); spec(type.alignment_v, repr('top'))
par("relative", "If True, x and y are fractions of the canvas; if False, they are absolute positions"); spec(type.bool, False)
par("pixel", "Pixel used to paint the legend"); spec(type.pixel_par, None)
past("xside", "signal")
past("yside", "signal")
out("This plot", type.plot)


add(plot_class.label, name = "label")
doc("Sets the label of the selected axis and side.")
par("label", "the axis label"); spec(type.label)
par("axis", "Axis to control, x, y, or both"); spec(type.axis_multiple, repr('x'))
par("side", "Axis side to control"); spec(type.side_multiple, 0)
past_out("title")


# Axes and frame

add(plot_class.axis, name = "axis")
doc("Controls the status, style and pixel of one or more frame axes.")
par("status", "Whether the axis is visible"); spec(type.bool, True)
par("style", "Axis line style. " + type.axis_styles); spec(type.style, repr('default'))
par("pixel", "Pixel used to paint the axis"); spec(type.pixel_par, None)
past("axis", "label")
past("side", "label")
past_out("title")


add(plot_class.frame, name = "frame")
doc("Shortcut to set status, style and pixel on all four frame axes at once.")
past("status", "axis")
past("style", "axis")
past("pixel", "axis")
past_out("title")


# Ruler settings

add(plot_class.alignment, name = "alignment")
doc("Defines whether axis limits fall on the center or the edge of the outermost bins. "
    "With 'center' (default), the lower and upper limits sit at the middle of the first and last bins; "
    "with 'edge', they sit at the outer edge. Applies equally to the x and y axes.")
par("alignment", "Determines how the numerical limits are positioned within the outermost bins. It can be either center or edge."); spec(type.alignment, repr('center'))
past("axis", "label")
past("side", "label")
past_out("title")


add(plot_class.direction, name = "direction")
doc("Sets the direction in which values increase along one or more axes. "
    "Use 1 for the standard direction (left→right on x, bottom→top on y) or -1 to reverse it.")
par("direction", "Direction of the axis"); spec(type.direction, 1)
past("axis", "label")
past("side", "label")
past_out("title")


add(plot_class.scale, name = "scale")
doc("Sets the scale type of one or more axes.")
par("scale", "Scale of the axis: linear or logarithmic scale"); spec(type.scale, repr('linear'))
past("axis", "label")
past("side", "label")
past_out("title")


add(plot_class.lim, name = "lim")
doc("Sets the visible numerical range of one or more axes. "
    "Data values outside this range are clipped. "
    "Limits may be specified as numbers or date strings.")
par("lower",
    "Lower (minimum) plot limit relative to the selected axis. " + type.dates_accepted + " " + type.limits); spec(type.value, None)
par("upper",
    "Upper (maximum) plot limit relative to the selected axis. " + type.dates_accepted + " " + type.limits); spec(type.value, None)
past("axis", "label")
past("side", "label")
past_out("title")


add(plot_class.frequency, name = "frequency")
doc("Sets the number of automatically-placed ticks along one or more axes. "
    "To specify exact tick positions instead, use ticks() — it overrides this setting.")
par("frequency", "The integer number of numerical ticks along the selected axis"); spec(type.value, "7 for x axis; 5 for y axis")
past("axis", "label")
past("side", "label")
past_out("title")


add(plot_class.ticks, name = "ticks")
doc("Sets explicit tick positions (and optionally their labels) along one or more axes. "
    "If labels are omitted, the numeric positions are shown as labels.")
par("positions", "A list of numerical tick positions along the selected axis. " + type.dates_accepted); spec(type.data_single, None)
par("labels", "Optional list of string labels to display at the tick positions."); spec(type.strings, None)
past("axis", "label")
past("side", "label")
past_out("title")


add(plot_class.ruler_pixel, name = "ruler_pixel")
doc("Sets the ruler pixel — the foreground colour, background colour and style applied to tick labels along one or more axes. "
    "Already-placed tick labels are recoloured in place, so this can be called either before or after ticks() / frequency(). "
    "When ticks() is given already-colorized labels, those labels keep their own foreground and style (only their background is harmonised with the ruler) until ruler_pixel() is called again, which overwrites them.")
par("pixel", "Pixel used to paint the tick labels"); spec(type.pixel_par, defaults.pixels["ruler"])
past("axis", "label"); spec(type.axis_multiple, binary)
past("side", "label"); spec(type.side_multiple, binary)
past_out("title")


add(plot_class.tick_alignment, name = "tick_alignment")
doc("Sets the alignment of tick labels: y-axis ticks use horizontal naming (left, center, right) while x-axis ticks use vertical naming (top, center, bottom).")
par("alignment", "Tick label alignment"); spec(type.alignment_text, repr(None))
past("axis", "label")
past("side", "label")
past_out("title")


add(plot_class.grid, name = "grid")
doc("Controls the grid lines along one or more axes.")
par("active", "Whether the grid is visible or not"); spec(type.bool, True)
par("style", "Line style for the grid. " + type.line_styles); spec(type.style, repr('default'))
par("pixel", "Pixel used to paint the grid"); spec(type.pixel_par, defaults.pixels["grid"])
past("axis", "label"); spec(type.axis_multiple, binary)
past("side", "label"); spec(type.side_multiple, binary)
past_out("title")


add(plot_class.date, name = "date")
doc("Returns the date converter (date_class instance) bound to the selected ruler. All date operations live on the returned object: activate(...) to enable date handling and set form/origin, convert(time, output) to translate between string / datetime / timestamp, today(output) for today's date, clear() to reset.")
past("axis", "label"); spec(type.axis_multiple, 0)
past("side", "label"); spec(type.side_multiple, 0)
out("Date converter for the selected ruler", type.string)
