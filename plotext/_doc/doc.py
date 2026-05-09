# Docstrings for the public plotext API, grouped by logical sections via prettydoc

from plotext._doc.tools import *
from plotext import *
from plotext._plotter.plot import plot_class
from plotext._kernel.terminal import terminal as terminal_class
from plotext._signal.signal import signal_class
from plotext._primitives.pixel import pixel as pixel_class
from plotext._primitives.colorize import colorize as colorize_class
from plotext._primitives.marker import marker as marker_class
from plotext._primitives.matrix import matrix as matrix_class
from plotext import prettydoc
from plotext._constants.numerical import binary
from plotext._settings import defaults


# -----------------------------
# Plot lifecycle
# -----------------------------

add(plot_class.clear, name = "clear")
alias("clf")
doc("Clears all signals, settings and sizes from this plot, resetting it to an empty state. Equivalent to calling clear_data(), clear_settings(), clear_pixels(), clear_styles(), clear_size() and clear_subplots() in turn.")
out("This plot", type.plot)

add(plot_class.clear_data, name = "clear_data")
alias("cld")
doc("Drops every signal previously added via draw() and removes the corresponding entries from the legend. Settings, sizes, pixels and styles are preserved.")
past_out("clear")

add(plot_class.clear_settings, name = "clear_settings")
alias("cls")
doc("Resets the plot's settings — title, axis labels, limits, frequencies, manual ticks, scale, alignment, direction, grid, frame status, legend status — back to defaults. Signals, pixels, styles and sizes are preserved.")
past_out("clear")

add(plot_class.clear_pixels, name = "clear_pixels")
alias("clp")
doc("Resets every pixel on this plot — labels, rulers, axes, legend and the canvas itself — to the package defaults, and rewinds the per-signal colour cycler to the start. Signals, settings, styles and sizes are preserved.")
past_out("clear")

add(plot_class.clear_styles, name = "clear_styles")
doc("Resets the line styles of the rulers (grid lines) and axes (frame sides) to the default style. Signals, settings, pixels and sizes are preserved.")
past_out("clear")

add(plot_class.clear_size, name = "clear_size")
alias("clz")
doc("Drops any explicit plot_size() value. On the master plot the size reverts to the current terminal dimensions. Signals, subplots, settings, pixels and styles are preserved.")
past_out("clear")

add(plot_class.clear_subplots, name = "clear_subplots")
alias("clss")
doc("Wipes the subplot grid configured via subplots() so the plot becomes a single-panel layout again. Signals, settings, pixels, styles and size are preserved.")
past_out("clear")

add(plot_class.build, name = "build")
doc("Builds the final figure as a matrix, without printing it. Use show() to both build and print.")
out("The final figure matrix", type.matrix)

add(plot_class.show, name = "show")
doc("Builds and prints the final figure to the terminal.")
par("colorless", "If True, render the output without colors"); spec(type.bool, False)
par("flush", "If True, flush the terminal after printing"); spec(type.bool, False)
past_out("clear")


# -----------------------------
# Signal creation and drawing
# -----------------------------

add(sin)
doc("Generates a sinusoidal signal for testing plotting routines.")
par("periods", "Number of complete sinusoidal cycles"); spec(type.float, 2)
par("length", "Total number of sample points"); spec(type.int, 200)
par("amplitude", "Half the peak-to-peak value of the sine wave"); spec(type.float, 1)
par("phase", "Phase shift in units of π"); spec(type.float, 0)
par("decay", "Exponential decay factor applied to the signal"); spec(type.float, 0)
par("offset", "Additional vertical offset"); spec(type.float, 0)
out("List of floats representing the generated signal", type.floats)


add(plot_class.signal, name = "signal")
doc("Creates a signal, a sequence of points to be plotted. Line drawing is configured on the returned signal via its fluent methods (lines, point_lines); line_method and fill_method are construction-time parameters here; label and stem fills (fillx, filly) are also set fluently on the signal.")
par("args", "Input data: x, y coordinates, or a single y sequence; date values are also supported"); spec(type.data_multiple)
par("marker", "Symbol used to represent each data point"); spec(type.marker_par_draw, repr("hd"))
par("line_method", "How densely the connecting lines are drawn (simple or full); applies only when lines have been turned on via signal.lines() or signal.point_lines()"); spec(type.line_method, repr("simple"))
par("fill_method", "How densely fills are drawn for points carrying fill data (simple or full)"); spec(type.line_method, repr("simple"))
par("xside", "Which x axis to plot against"); spec(type.xside, repr('lower'))
par("yside", "Which y axis to plot against"); spec(type.yside, repr('left'))
out("The signal itself", type.signal)


add(plot_class.draw, name = "draw")
doc("Adds a drawable to the plot queue. Accepts either a signal (from signal(), candlestick(), rectangle(), polygon(), bar()) or a text annotation (from text()). All queued drawables are rendered when plotext.show() or plotext.build() is called.")
par("drawable", "The signal or text to be added to the plot queue"); spec(type.signal + " or " + type.text)
out("This plot", type.plot)


add(plot_class.candlestick, name = "candlestick")
doc("Creates a candlestick signal from OHLC market data. The returned signal must be passed to draw().")
par("data", "A dictionary containing date, open, close, high, low values for each candle; dates are interpreted automatically once plotext.date() has been called on the relevant axis"); spec(type.ohlc_dict)
par("colors", "The two colors used for positive and negative candles; see plotext.colors for available color codes"); spec(type.color_pair, repr(["green", "red"]))
par("orientation", "Candlestick orientation, either vertical (or v) or horizontal (or h)"); spec(type.orientation, repr("vertical"))
past("xside", "signal")
past("yside", "signal")
out("The candlestick signal", type.signal)


add(plot_class.rectangle, name = "rectangle")
doc("Creates a rectangle signal between the given x and y ranges. The returned signal must be passed to draw().")
par("x", "The x range of the rectangle"); spec(type.couple, repr((0, 1)))
par("y", "The y range of the rectangle"); spec(type.couple, repr((0, 1)))
par("marker", "Symbol used to render the rectangle"); spec(type.marker_par_draw, repr("hd"))
par("lines", "If True the rectangle's outline is drawn (and densified for body filling when fill is also True); if False only the corner pairs are placed"); spec(type.bool, True)
par("fill", "If True the rectangle's body is filled with markers; if False only the clockwise outline is drawn"); spec(type.bool, True)
past("xside", "signal")
past("yside", "signal")
out("The rectangle signal", type.signal)


add(plot_class.polygon, name = "polygon")
doc("Creates a regular polygon signal centered at the given coordinates. The returned signal must be passed to draw().")
par("x", "The polygon center x coordinate"); spec(type.float, 0)
par("y", "The polygon center y coordinate"); spec(type.float, 0)
par("radius", "Distance from the center to each vertex; for a circle it is the actual radius"); spec(type.float, 1)
par("sides", "Number of polygon sides; values above ~50 approximate a circle"); spec(type.int, 3)
par("up", "If True, rotates the polygon by half a side angle (a flat edge faces up for even sides; a vertex faces up for odd sides)"); spec(type.bool, False)
par("marker", "Symbol used to render the polygon vertices"); spec(type.marker_par_draw, repr("hd"))
par("lines", "If True, the polygon outline is drawn between consecutive vertices; if False only the vertex points are placed"); spec(type.bool, True)
par("fill", "If True, every vertex gets a fill point at (x, y) — the polygon center, producing radial spokes from each vertex inward"); spec(type.bool, False)
past("xside", "signal")
past("yside", "signal")
out("The polygon signal", type.signal)


add(plot_class.segment, name = "segment")
doc("Creates a straight line segment between two endpoints. The returned signal must be passed to draw().")
par("x", "The x range of the segment, as a two-value tuple or list — first endpoint, then second"); spec(type.couple, repr((0, 1)))
par("y", "The y range of the segment, same format as x"); spec(type.couple, repr((0, 1)))
par("marker", "Symbol used to render the segment"); spec(type.marker_par_draw, repr("hd"))
past("xside", "signal")
past("yside", "signal")
out("The segment signal", type.signal)


add(plot_class.bar, name = "bar")
doc("Creates a bar plot signal. The returned signal must be passed to draw().")
par("args", "Bar input data: a single sequence sets the bar heights and uses 1..N as coordinates; two sequences set the bar coordinates and heights with the baseline at zero; three sequences set the bar coordinates, baselines and heights (floating bars)"); spec(type.data_bar)
par("marker", "Symbol used to render the bars"); spec(type.marker_par_draw, repr("hd"))
par("width", "Bar width as a fraction of the inter-bar spacing"); spec(type.float, 4/5)
par("orientation", "Bar orientation, either vertical (or v) or horizontal (or h)"); spec(type.orientation, repr("vertical"))
par("lines", "If True, draws the bar outline"); spec(type.bool, True)
par("fill", "If True, fills the bar body"); spec(type.bool, True)
past("xside", "signal")
past("yside", "signal")
out("The bar signal", type.signal)


add(plot_class.multiple_bar, name = "multiple_bar")
doc("Creates a grouped bar plot where multiple bars are placed side-by-side (along the bar width axis) at the same coordinate. The returned signal must be passed to draw().")
par("args", "The coordinates x and Y (or just Y), of the bars, where Y is a list of lists, each containing the bar heights of the corresponding bar plot; string labels or dates are accepted (but only as x values)"); spec(type.data_multiple_bar)
par("marker", "Symbol used to render the bars; a list of markers (with same length as Y) can also be provided to separately set the marker of each group"); spec(type.marker_par_draw)
par("width", "Outer width of each group as a fraction of the inter-group spacing; per-bar width is this divided by the number of groups"); spec(type.float, 4/5)
past("orientation", "bar")
past("lines", "bar")
past("fill", "bar")
past("xside", "signal")
past("yside", "signal")
out("The composed bar signal", type.signal)


add(plot_class.stacked_bar, name = "stacked_bar")
doc("Creates a stacked bar plot where multiple bars are placed on top of each other (along the bar height axis) at the same coordinate. Each group's bar starts where the previous group's bar ended, so heights add up cumulatively per coordinate. The returned signal must be passed to draw().")
past("args", "multiple_bar")
past("marker", "multiple_bar")
par("width", "Bar width as a fraction of the inter-bar spacing"); spec(type.float, 4/5)
past("orientation", "bar")
past("lines", "bar")
past("fill", "bar")
past("xside", "signal")
past("yside", "signal")
out("The composed bar signal", type.signal)


add(plot_class.text, name = "text")
doc("Creates a text annotation at the given x and y coordinates. The returned text must be passed to draw() to register it on the plot.")
par("x", "X coordinate of the text anchor"); spec(type.value)
par("y", "Y coordinate of the text anchor"); spec(type.value)
par("label", "Text content: a plain string or a plotext.colorize for explicit styling"); spec(type.label)
par("alignment", "Alignment along the writing direction"); spec(type.alignment_text, repr("left"))
par("orientation", "Text orientation, horizontal or vertical"); spec(type.orientation, repr("horizontal"))
past("xside", "signal")
past("yside", "signal")
par("relative", "If True, x and y are absolute canvas-cell coordinates instead of data coordinates"); spec(type.bool, False)
out("The text object", type.text)


# -----------------------------
# Labels
# -----------------------------

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


# -----------------------------
# Axes and frame
# -----------------------------

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


# -----------------------------
# Ruler settings
# -----------------------------

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
doc("Enables date handling on one or more axes: parses date strings, displays dates on ticks, and optionally sets a time origin.")
par("active", "Whether to activate date conversion."); spec(type.bool, True)
par("form", "Specifies how strings are interpreted as datetime objects. " + type.date_form); spec(type.string, repr('%d/%m/%Y'))
par("origin", "Sets the origin of time: useful with logarithmic scales in date plots to avoid applying a log transformation to the 0 timestamp."); spec(type.date_single_time_par, None)
past("axis", "label"); spec(type.axis_multiple, 0)
past("side", "label"); spec(type.side_multiple, 0)
past_out("title")


add(plot_class.convert, name = "convert")
doc("Converts the given time value (or values) to the specified output format, using the date converter from the specified axis. "
    "The input type is detected automatically.")
par("time", "The time value to convert (or list thereof)."); spec(type.date_time_par)
par("output", "Specifies the output format."); spec(type.convert_output_par, repr("timestamp"))
past("axis", "label"); spec(type.axis_multiple, 0)
past("side", "label"); spec(type.side_multiple, 0)
out("Converted date/time value, or list thereof", type.convert_output)


# -----------------------------
# Canvas, sizing and subplots
# -----------------------------

add(plot_class.canvas_pixel, name = "canvas_pixel")
doc("Sets the pixel (color and style) of the plot canvas background.")
par("pixel", "Pixel used to paint the canvas"); spec(type.pixel_par, None)
past_out("title")


add(plot_class.plot_size, name = "plot_size")
doc("Sets the size (width and height) of this plot, in terminal cells.")
par("width", "Plot width in terminal columns"); spec(type.int, None)
par("height", "Plot height in terminal rows"); spec(type.int, None)
past_out("title")


add(plot_class.subplots, name = "subplots")
doc("Divides this plot into a grid of subplots with the given number of rows and columns.")
par("rows", "Number of subplot rows"); spec(type.int, None)
par("cols", "Number of subplot columns"); spec(type.int, None)
past_out("title")


add(plot_class.subplot, name = "subplot")
doc("Returns the subplot at the given row and column, so it can be addressed directly (for example to draw a signal on it).")
par("row", "Row index of the subplot"); spec(type.int, None)
par("col", "Column index of the subplot"); spec(type.int, None)
out("The subplot at (row, col)", type.plot)


add(plot_class.get_parent, name = "get_parent")
doc("Returns the parent plot at the given nesting level — 0 returns this plot, 1 returns the immediate parent, and so on. Higher levels stop at the master and continue returning it.")
par("level", "Nesting level (0 = self, 1 = immediate parent, ...)"); spec(type.int, 1)
out("The plot at the requested level", type.plot)


add(plot_class.get_master, name = "get_master")
doc("Returns the master plot — the top-level plot that owns this subtree of subplots.")
out("The master plot", type.plot)


add(plot_class.get_terminal, name = "get_terminal")
doc("Returns the terminal object that owns the master plot.")
out("The terminal object", type.terminal)


add(plot_class.get_position, name = "get_position")
doc("Returns this subplot's (row, col) position within its parent grid; (None, None) for the master.")
out("A (row, col) tuple", type.tuple)


add(plot_class.get_log, name = "get_log")
doc("Returns a multi-line string describing this subplot and every nested subplot, indented to reflect the tree.")
out("The log string", type.string)


add(plot_class.size_direction, name = "size_direction")
doc("Controls how subplot widths (and heights) are redistributed within the maximum available canvas size. With +1 the redistribution runs left-to-right across widths and top-to-bottom across heights, and the last subplot (rightmost column or bottom row) absorbs whatever space is left. With -1 the order is reversed, so the first subplot (leftmost column or top row) absorbs the leftover instead.")
par("direction", "+1 runs the redistribution left-to-right (widths) and top-to-bottom (heights); -1 reverses it"); spec(type.direction, 1)
past_out("title")


add(plot_class.size_policy, name = "size_policy")
doc("Controls how nested subplot widths (and heights) are harmonized when they disagree. With 'maximum' each column/row takes the largest requested size across nested subplots, growing the canvas to accommodate; with 'minimum' it takes the smallest, shrinking everyone to fit.")
par("policy", "maximum (columns/rows take the largest nested size) or minimum (they take the smallest)"); spec(type.size_policy, repr("maximum"))
past_out("title")


# -----------------------------
# Signal methods
# -----------------------------

add(signal_class.clear, name = "signal.clear")
doc("Removes all points from the signal, making it empty.")
past_out("signal")

add(signal_class.label, name = "signal.label")
doc("Sets the signal label shown on the legend. If left empty, the default label is 'signal[N]', where N is the signal index in the plot.")
par("label", "The label to display on the legend"); spec(type.label, repr(None))
past_out("signal")

add(signal_class.lines, name = "signal.lines")
doc("Connects every point of the signal uniformly. Pass True to draw lines between all consecutive points (line plot), False to leave the signal as a scatter. Use signal.point_lines() to toggle a single segment instead.")
par("value", "True to connect all points, False to disconnect them"); spec(type.bool, True)
past_out("signal")

add(signal_class.point_lines, name = "signal.point_lines")
doc("Toggles the connection from the previous point to the one at index, allowing a single segment of the signal to be turned on or off without touching the others. The effective range is 1..N-1; out-of-range indices are silently ignored (index 0 has no predecessor and is therefore always a no-op).")
par("index", "Position of the point whose incoming segment is toggled"); spec(type.int)
par("value", "True to draw the line into this point, False to break the segment"); spec(type.bool, True)
past_out("signal")

add(signal_class.fillx, name = "signal.fillx")
doc("Fills a vertical stem from each point down to the x axis.")
par("active", "Whether to draw the vertical fill lines"); spec(type.bool, True)
past_out("signal")

add(signal_class.filly, name = "signal.filly")
doc("Fills a horizontal stem from each point across to the y axis.")
par("active", "Whether to draw the horizontal fill lines"); spec(type.bool, True)
past_out("signal")

add(signal_class.fill, name = "signal.fill")
doc("Copies fill levels from another signal, useful when building custom stem plots or filled regions.")
par("signal", "Signal to copy the fill information from"); spec(type.signal)
past_out("signal")

add(signal_class.line_method, name = "signal.line_method")
doc("Sets how densely connecting lines are drawn between points. Pass 'simple' for evenly-spaced points along each segment (light, fast, may leave small gaps on steep segments) or 'full' to fill every cell crossed by the line (denser, visually continuous). Applies only when lines have been turned on via signal.lines() or signal.point_lines(). The same setting can also be passed at construction via the line_method parameter on signal().")
par("method", "Line drawing method"); spec(type.line_method, repr("simple"))
past_out("signal")

add(signal_class.fill_method, name = "signal.fill_method")
doc("Sets how densely fills are drawn for points carrying fill data. Pass 'simple' for evenly-spaced points (faster, may leave small gaps on steep stems) or 'full' to fill every cell crossed (denser, visually continuous). The same setting can also be passed at construction via the fill_method parameter on signal().")
par("method", "Fill drawing method"); spec(type.line_method, repr("simple"))
past_out("signal")

add(signal_class.get_length, name = "signal.get_length")
doc("Returns the number of points currently in the signal.")
out("Number of points", type.int)

add(signal_class.copy, name = "signal.copy")
doc("Creates and returns a deep copy of the signal.")
past_out("signal")

add(signal_class.clone, name = "signal.clone")
doc("Replaces this signal's points with those from another signal.")
par("signal", "Signal whose points are copied into this one"); spec(type.signal)
past_out("signal")

add(signal_class.log, name = "signal.log")
doc("Prints a text-based description of the signal and its points, for debugging or inspection. "
    "The output can be long for large signals.")
par("fill", "If True, includes the filled-point information in the output"); spec(type.bool, False)
past_out("signal")


# -----------------------------
# Inspection
# -----------------------------

add(plot_class.time, name = "time")
doc("Prints a timing report of the most recent build — total elapsed time and, optionally, per-step breakdown for each profiled section. Useful when investigating slow renders.")
par("full", "If True (default), include the per-step breakdown; if False, print only the total"); spec(type.bool, True)
past_out("title")


# -----------------------------
# Terminal
# -----------------------------

add(terminal_class, name = "terminal")
doc("High-level manager for terminal interaction and sizing inside plotext.")
out("A terminal object", type.terminal)

add(terminal_class.clean, name = "terminal.clean")
alias("clt")
doc("Clears the visible terminal output — either entirely, or by a specific number of lines above the prompt. Useful when plotting a continuous stream of data. Note that, depending on the terminal shell used, a few extra lines may be printed after the plot.")
par("lines", "If an integer, that many printed lines are removed from the terminal, plus the prompt height; if None (default), the terminal is fully cleared."); spec(type.int, None)
out("The terminal itself", type.terminal)

add(terminal_class.clear, name = "terminal.clear")
doc("Resets terminal settings, including prompt height, limit settings, and current terminal size.")
past_out("terminal.clean")

add(terminal_class.prompt, name = "terminal.prompt")
doc("Sets the height of the terminal prompt (the area reserved for user input).")
par("height", "Number of lines reserved for the terminal prompt; if None, defaults to the standard prompt height."); spec(type.int, 2)
past_out("terminal.clean")

add(terminal_class.limit, name = "terminal.limit")
doc("Sets whether to limit the master plot size to the terminal's plottable area.")
par("width", "If False, the plot width is not limited by the terminal width."); spec(type.bool, True)
par("height", "If False, the plot height is not limited by the terminal height."); spec(type.bool, True)
past_out("terminal.clean")

add(terminal_class.get_size, name = "terminal.get_size")
doc("Returns the current terminal size as a (width, height) tuple.")
par("update", "If True, updates the terminal size before returning it; if False (default), returns the last known size."); spec(type.bool, False)
par("plottable", "If True, returns only the plottable size (excluding prompt lines); if False, returns the total size."); spec(type.bool, True)
out("A tuple (width, height).", type.tuple)

add(terminal_class.log, name = "terminal.log")
doc("Prints a detailed log of the terminal, its master plot, and any subplots.")
past_out("terminal.clean")


# -----------------------------
# Primitives: pixel
# -----------------------------

add(pixel_class, name = "pixel")
doc("A pixel: holds a foreground color, a background color, and a style attribute.")
par("foreground", "Foreground color; " + type.colors); spec(type.color)
par("background", "Background color; " + type.colors); spec(type.color)
par("style", "Styling attributes; " + type.styles); spec(type.style)
out("Pixel object with the specified color and style", type.pixel)

add(pixel_class.clear, name = "pixel.clear")
doc("Clears all color and style properties of the pixel.")
past_out("pixel")

add(pixel_class.set, name = "pixel.set")
doc("Updates the color and style properties of the pixel.")
past("foreground", "pixel")
past("background", "pixel")
past("style", "pixel")
past_out("pixel")

add(pixel_class.copy, name = "pixel.copy")
doc("Creates and returns a copy of the pixel object.")
out("New pixel object identical to the original", type.pixel)

add(pixel_class.clone, name = "pixel.clone")
doc("Copies the properties from another pixel into this pixel.")
par("pixel", "Pixel object whose properties are to be cloned"); spec(type.pixel)
out("Pixel object updated with the cloned properties", type.pixel)


# -----------------------------
# Primitives: colorize
# -----------------------------

add(colorize_class, name = "colorize")
doc("Wraps a string with color and style attributes, producing a terminal-renderable object.")
par("string", "The string to colorize"); spec(type.string, None)
past("foreground", "pixel")
past("background", "pixel")
past("style", "pixel")
out("Colorized string object", type.colorize)

add(colorize_class.copy, name = "colorize.copy")
doc("Returns a duplicate of the colorize object.")
out("Duplicated colorize object", type.colorize)

add(colorize_class.clone, name = "colorize.clone")
doc("Copies properties from another colorize object.")
par("colorized", "Colorize object to copy from"); spec(type.colorize)
out("Updated colorize object", type.colorize)

add(colorize_class.get_length, name = "colorize.get_length")
doc("Returns the string length excluding color/style ASCII codes.")
out("Length of colorless string", type.int)

add(colorize_class.get_string, name = "colorize.get_string")
doc("Returns the string, optionally stripping color and style ASCII codes.")
par("colorless", "If True, excludes color/style codes"); spec(type.bool, False)
out("String, optionally including ASCII color codes", type.string)

add(colorize_class.get_pixel, name = "colorize.get_pixel")
doc("Returns the pixel object representing the color/style of the colorize object.")
out("Pixel object", type.pixel)

add(colorize_class.set_pixel, name = "colorize.set_pixel")
doc("Applies color/style from a pixel to the colorize object.")
par("pixel", "Pixel whose color/style is copied"); spec(type.pixel)
past_out("colorize.clone")

add(colorize_class.set_string, name = "colorize.set_string")
doc("Replaces the string content, preserving the existing color/style.")
par("string", "New string content"); spec(type.string)
past_out("colorize.clone")

add(colorize_class.print, name = "colorize.print")
doc("Prints the colorized string to stdout.")
par("colorless", "If True, prints without color/style codes"); spec(type.bool, False)
par("flush", "If True, flushes stdout after printing"); spec(type.bool, False)
past_out("colorize.clone")

add(colorize_class.get_matrix, name = "colorize.get_matrix")
doc("Converts the colorize object to a single-row matrix.")
out("Matrix representation of the colorize", type.matrix)

add(colorize_class.hstack, name = "colorize.hstack")
doc("Horizontally stacks this colorize with another object into a matrix.")
par("colorized", "Object to stack (colorize or matrix)"); spec(type.colorize)
par("adapt", "If True, adjusts heights to match"); spec(type.bool, True)
out("Resulting matrix", type.matrix)

add(colorize_class.vstack, name = "colorize.vstack")
doc("Vertically stacks this colorize with another object into a matrix.")
par("colorized", "Object to stack (colorize or matrix)"); spec(type.colorize)
par("adapt", "If True, adjusts widths to match"); spec(type.bool, True)
out("Resulting matrix", type.matrix)


add(uncolorize)
doc("Removes all ASCII color and style codes from a string.")
par("string", "The string or colorize object to strip"); spec(type.string)
out("String without color/style", type.string)


add(colors, name = "colors")
doc("Prints every available color: the named string codes, the 256-entry integer palette, and an example RGB tuple. Each entry is rendered in its own color.")

add(styles, name = "styles")
doc("Prints every available text style code ('bold', 'italic', and so on), each rendered in its own style.")

add(markers, name = "markers")
doc("Prints every available marker code: the HD sub-character codes ('hd', 'fhd', 'braille') and the named character codes, each shown next to its rendered glyph.")


# -----------------------------
# Primitives: marker
# -----------------------------

add(marker_class, name = "marker")
doc("Creates a marker: a symbol with optional foreground, background and style, used to render points on the plot canvas.")
par("marker", "The marker to use. Possible entries: a single character; one of the character codes available via plotext.markers(); or an HD marker code ('hd', 'fhd', 'braille') for sub-character resolution"); spec(type.marker_par)
past("foreground", "pixel")
past("background", "pixel")
past("style", "pixel")
out("A marker object", type.marker)

add(marker_class.get_pixel, name = "marker.get_pixel")
doc("Returns the pixel holding the marker's color and style.")
past_out("marker")

add(marker_class.copy, name = "marker.copy")
doc("Creates and returns a copy of the marker object.")
past_out("marker")


# -----------------------------
# Primitives: matrix
# -----------------------------

add(matrix_class, name = "matrix")
doc("Creates a matrix of the given dimensions, with an optional default pixel.")
par("width", "Matrix width in columns"); spec(type.int, 0)
par("height", "Matrix height in rows"); spec(type.int, 0)
par("pixel", "Default pixel used for every cell"); spec(type.pixel_par, None)
out("A matrix object", type.matrix)

add(matrix_class.clear, name = "matrix.clear")
doc("Clears all content in the matrix.")
past_out("matrix")

add(matrix_class.get_width, name = "matrix.get_width")
doc("Returns the matrix width in columns.")
out("Matrix width", type.int)

add(matrix_class.get_height, name = "matrix.get_height")
doc("Returns the matrix height in rows.")
out("Matrix height", type.int)

add(matrix_class.get_size, name = "matrix.get_size")
doc("Returns the matrix size as a (width, height) tuple.")
out("Size tuple", type.tuple)

add(matrix_class.print, name = "matrix.print")
doc("Prints the matrix to stdout.")
past("colorless", "colorize.print")
past("flush", "colorize.print")
past_out("matrix")

add(matrix_class.get_string, name = "matrix.get_string")
doc("Returns the string representation of the matrix.")
past("colorless", "colorize.get_string")
out("String, optionally including ASCII color codes", type.string)

add(matrix_class.hstack, name = "matrix.hstack")
doc("Horizontally stacks this matrix with another.")
par("other", "Matrix to stack horizontally"); spec(type.matrix)
par("adapt", "If True, adjusts heights to match"); spec(type.bool, False)
out("Resulting matrix", type.matrix)

add(matrix_class.vstack, name = "matrix.vstack")
doc("Vertically stacks this matrix with another.")
par("other", "Matrix to stack vertically"); spec(type.matrix)
par("adapt", "If True, adjusts widths to match"); spec(type.bool, False)
out("Resulting matrix", type.matrix)

add(matrix_class.copy, name = "matrix.copy")
doc("Returns a copy of the matrix.")
out("Matrix copy", type.matrix)

add(matrix_class.insert, name = "matrix.insert")
doc("Inserts a matrix, colorize, or raw string at the given (col, row) position.")
par("col", "Column index"); spec(type.int)
par("row", "Row index"); spec(type.int)
par("matrix", "Object to insert"); spec(type.matrix_insertable)
par("ha", "Horizontal alignment anchor"); spec(type.alignment, -1)
par("va", "Vertical alignment anchor"); spec(type.alignment, 1)
past_out("matrix")


# -----------------------------
# Pretty documentation
# -----------------------------

add(prettydoc.docs, name = "prettydoc.docs")
doc("Initializes a PrettyDoc object that manages visually styled docstrings.")
par("colorless", "If True, rendered docstrings will have no color formatting."); spec(type.bool, False)
par("separator", "Separator placed between a labelled field's label and value."); spec(type.string, repr(': '))
out("The PrettyDoc manager itself", type.docs)

add(prettydoc.docs.set_default_pixel, name = "prettydoc.docs.set_default_pixel")
doc("Configures the default color and style of one PrettyDoc component. "
    "Call plotext.prettydoc.components() to see the available component names.")
par("component", "Component to modify"); spec(type.string)
par("pixel", "Pixel carrying the desired color and style"); spec(type.pixel_par, None)
past_out("prettydoc.docs")

add(prettydoc.docs.register_type, name = "prettydoc.docs.register_type")
doc("Registers a new data type name and its human-readable explanation in the shared type registry.")
par("type", "Type name"); spec(type.string)
par("doc", "Explanation of the type"); spec(type.string)
past_out("prettydoc.docs")

add(prettydoc.components, name = "prettydoc.components")
doc("Prints the list of available PrettyDoc components with a short description of each.")

add(prettydoc.docs.add_function, name = "prettydoc.docs.add_function")
doc("Registers a function to be documented. All subsequent PrettyDoc calls apply to the most recently added function until another is registered.")
par("function", "The function (or list of aliased functions) to document"); spec(type.function)
par("name", "Optional explicit name; defaults to the function's __qualname__"); spec(type.string, None)
past_out("prettydoc.docs")

add(prettydoc.docs.add_doc, name = "prettydoc.docs.add_doc")
doc("Adds the main body of documentation for the most recently added function.")
par("doc", "Description of what the function does"); spec(type.label)
past_out("prettydoc.docs")

add(prettydoc.docs.add_alias, name = "prettydoc.docs.add_alias")
doc("Adds an alias name for the most recently added function.")
par("alias", "Alias name"); spec(type.label)
past_out("prettydoc.docs")

add(prettydoc.docs.add_parameter, name = "prettydoc.docs.add_parameter")
doc("Adds a parameter to the most recently added function.")
par("name", "Parameter name"); spec(type.label)
par("doc", "Parameter description"); spec(type.label)
past_out("prettydoc.docs")

add(prettydoc.docs.add_parameter_spec, name = "prettydoc.docs.add_parameter_spec")
doc("Sets the type and default value of the most recently added parameter.")
par("type", "Parameter type"); spec(type.label, None)
par("default", "Parameter default value"); spec(type.label, None)
past_out("prettydoc.docs")

add(prettydoc.docs.add_past_parameter, name = "prettydoc.docs.add_past_parameter")
doc("Copies a parameter from a previously documented function onto the current one.")
par("name", "Name of the parameter to copy"); spec(type.string)
par("function", "Name of the function that already defines this parameter"); spec(type.string)
past_out("prettydoc.docs")

add(prettydoc.docs.add_output, name = "prettydoc.docs.add_output")
doc("Documents the output of the most recently added function.")
par("doc", "Description of the output"); spec(type.label)
par("type", "Output type"); spec(type.label, None)
past_out("prettydoc.docs")

add(prettydoc.docs.add_past_output, name = "prettydoc.docs.add_past_output")
doc("Copies the output specification from a previously documented function.")
par("function", "Name of the function whose output should be reused"); spec(type.string)
past_out("prettydoc.docs")

add(prettydoc.docs.update, name = "prettydoc.docs.update")
doc("Finalizes the manager: applies every registered docstring to its function's __doc__ and returns a container that exposes every docstring by attribute name.")
out("A docs_output container with one callable attribute per registered function", type.docs)

add(prettydoc.docs.show, name = "prettydoc.docs.show")
doc("Prints every registered docstring, one after another.")
past_out("prettydoc.docs")


# -----------------------------
# Utilities
# -----------------------------

add(test, name = "test")
doc("Runs the plotext unit test suite and prints a summary of the results.")

add(prettydoc.test, name = "prettydoc.test")
doc("Runs only the prettydoc unit test suite and prints a summary of the results.")


# Apply all updates
docs = pd.update()
