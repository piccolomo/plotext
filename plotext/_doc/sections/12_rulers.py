# Rulers section: the ruler methods

from plotext._doc.tools import *
from plotext._plotter.frame.ruler import ruler_class
from plotext._settings import defaults


section('rulers')


add(ruler_class.frequency)
doc("Sets the number of automatically-placed ticks along the axis. "
    "To specify exact tick positions instead, use ticks(), which overrides this setting.")
source(["plotext.figure.ruler()", "plotext.figure.subplot().ruler()"])
par("frequency", "The number of ticks along the axis", explanation("int"), "7 for x axis; 5 for y axis")
out("The ruler selection itself", explanation("ruler"))


add(ruler_class.ticks)
doc("Sets explicit tick positions, and optionally their labels, along the axis; when no labels are given, each tick shows its own position value.")
source(["plotext.figure.ruler()", "plotext.figure.subplot().ruler()"])
par("positions", "A list of numerical tick positions along the axis; an empty list removes the ticks, as frequency(0) does. " + explanation("dates_accepted"), explanation("data_single"), None)
par("labels", "Optional list of labels to display at the tick positions.", explanation("labels"), None)
past_out("plotext.figure.ruler().frequency")


add(ruler_class.lim)
doc("Sets the visible numerical range of the axis. "
    "Data values outside this range are clipped. "
    "Limits may be specified as numbers or date strings.")
source(["plotext.figure.ruler()", "plotext.figure.subplot().ruler()"])
par("lower",
    "Lower (minimum) plot limit of the axis. " + explanation("dates_accepted") + " " + explanation("limits"), explanation("value"), None)
par("upper",
    "Upper (maximum) plot limit of the axis. " + explanation("dates_accepted") + " " + explanation("limits"), explanation("value"), None)
past_out("plotext.figure.ruler().frequency")


add(ruler_class.scale)
doc("Sets the scale of the axis: with linear (default), equal value differences take equal space; with log, each multiplication by 10 takes equal space, so small and large values stay readable on the same plot.")
source(["plotext.figure.ruler()", "plotext.figure.subplot().ruler()"])
par("scale", "Scale of the axis", explanation("scale"), repr('linear'))
past_out("plotext.figure.ruler().frequency")


add(ruler_class.direction)
doc("Sets the direction in which values increase along the axis. "
    "Use 1 for the standard direction (left to right on x, bottom to top on y) or -1 to reverse it.")
source(["plotext.figure.ruler()", "plotext.figure.subplot().ruler()"])
par("direction", "Direction of the axis", explanation("direction"), 1)
past_out("plotext.figure.ruler().frequency")


add(ruler_class.alignment)
doc("Sets the two ruler alignments, which refer to two different settings:\n"
    "the limits alignment (lim), controlling where an axis numerical limit sits within its dedicated character cell;\n"
    "the ticks alignment (tick), controlling how the tick labels are placed relative to their actual positions.")
source(["plotext.figure.ruler()", "plotext.figure.subplot().ruler()"])
par("lim", "Numerical limits alignment: with center (default), the lower (or upper) limit sits at the middle of the first (or last) cell; with edge, at its left (or right) on the x axis, and at its bottom (or top) on the y axis", explanation("alignment"), repr('center'))
par("tick", "Tick label alignment relative to the tick position: left, center or right, or dynamic, which finds an intermediate position between the left and right anchors, depending on the space available, aiming at the center one", explanation("alignment_tick"), repr('default'))
past_out("plotext.figure.ruler().frequency")


add(ruler_class.pixel)
doc("Sets the pixel used to paint the tick area of the axis: the tick labels and the whole strip they sit in, beside the axes frame.")
source(["plotext.figure.ruler()", "plotext.figure.subplot().ruler()"])
par("pixel", "Pixel used to paint the tick labels", explanation("pixel_par"), defaults.pixels["ruler"])
past_out("plotext.figure.ruler().frequency")


add(ruler_class.grid)
doc("Controls the grid lines drawn from the ruler ticks, spanning the whole canvas at every numerical tick position: vertical lines for an x ruler, horizontal for a y ruler.")
source(["plotext.figure.ruler()", "plotext.figure.subplot().ruler()"])
par("active", "Whether the grid is visible or not", explanation("bool"), True)
par("style", "Line style for the grid. " + explanation("line_styles"), explanation("line_style"), repr('default'))
par("pixel", "Pixel used to paint the grid", explanation("pixel_par"), defaults.pixels["grid"])
past_out("plotext.figure.ruler().frequency")


add(ruler_class.clear)
doc("Resets the selected rulers only: their settings (limits, ticks, frequency, scale, direction, alignments, date support, grid) and their pixels return to defaults, leaving the rest of the plot untouched.")
source(["plotext.figure.ruler()", "plotext.figure.subplot().ruler()"])
past_out("plotext.figure.ruler().frequency")
