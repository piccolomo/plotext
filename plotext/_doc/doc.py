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
from plotext._settings.constants.numerical import binary
from plotext._settings import defaults


# Extra types used across the primitive and terminal sections
add_type("terminal", "A plotext terminal object")
add_type("pixel", "A plotext pixel object")
add_type("colorize", "A plotext colorize object")
add_type("matrix", "A plotext matrix object")


# -----------------------------
# Plot lifecycle
# -----------------------------

add(plot_class.clear, name = "clear")
doc("Clears all signals, settings and sizes from the active plot, resetting it to an empty state.")
out("The active plot", type.plot)

add(plot_class.clf, name = "clf")
doc("Alias for clear().")
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
doc("Creates a signal, a sequence of points to be plotted. Line drawing, fills and label can be set on the returned signal via signal.lines(), signal.fillx(), signal.filly() and signal.label().")
par("args", "Input data: x, y coordinates, or a single y sequence; date values are also supported"); spec(type.data_multiple)
par("marker", "Symbol used to represent each data point"); spec(type.marker_par_draw, repr("hd"))
par("xside", "Which x axis to plot against"); spec(type.xside, repr('lower'))
par("yside", "Which y axis to plot against"); spec(type.yside, repr('left'))
out("The signal itself", type.signal)


add(plot_class.draw, name = "draw")
doc("Adds a signal to the plot queue. All queued signals are rendered when "
    "plotext.show() or plotext.build() is called.")
par("signal", "The signal to be added to the plot queue"); spec(type.signal)
out("The active plot", type.plot)


add(plot_class.candlestick, name = "candlestick")
doc("Creates a candlestick signal from OHLC market data. The returned signal must be passed to draw().")
par("data", "A dictionary containing date, open, close, high, low values for each candle; dates are interpreted automatically once plotext.date() has been called on the relevant axis"); spec(type.ohlc_dict)
par("colors", "The two colors used for positive and negative candles; see plotext.colors for available color codes"); spec(type.color_pair, repr(["green", "red"]))
par("orientation", "Candlestick orientation, either 'vertical' (or 'v') or 'horizontal' (or 'h')"); spec(type.orientation, repr("vertical"))
past("xside", "signal")
past("yside", "signal")
out("The candlestick signal", type.signal)


# -----------------------------
# Labels
# -----------------------------

add(plot_class.title, name = "title")
doc("Sets the title of the active plot.")
par("label", "the title label"); spec(type.label)
out("the active plot", type.plot)


add(plot_class.legend, name = "legend")
doc("Configures the plot legend: visibility, position, alignment, colour, and axis anchoring.")
par("status", "Whether the legend is visible"); spec(type.bool, True)
par("x", "X position of the legend anchor"); spec(type.value, repr(None))
par("y", "Y position of the legend anchor"); spec(type.value, repr(None))
par("ha", "Horizontal alignment of the legend: 'left', 'center', or 'right'"); spec(type.alignment_h, repr('left'))
par("va", "Vertical alignment of the legend: 'top', 'center', or 'bottom'"); spec(type.alignment_v, repr('top'))
par("relative", "If True, x and y are fractions of the canvas; if False, they are absolute positions"); spec(type.bool, False)
par("pixel", "Pixel used to paint the legend"); spec(type.pixel_par, None)
past("xside", "signal")
past("yside", "signal")
out("The active plot", type.plot)


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
par("alignment", "Determines how the numerical limits are positioned within the outermost bins. It can be either 'center' or 'edge'."); spec(type.alignment, repr('center'))
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
doc("Sets the size (width and height) of the active plot, in terminal cells.")
par("width", "Plot width in terminal columns"); spec(type.int, None)
par("height", "Plot height in terminal rows"); spec(type.int, None)
past_out("title")


add(plot_class.subplots, name = "subplots")
doc("Creates a subplot grid on the active plot, with the given number of rows and columns.")
par("rows", "Number of subplot rows"); spec(type.int, None)
par("cols", "Number of subplot columns"); spec(type.int, None)
past_out("title")


add(plot_class.subplot, name = "subplot")
doc("Selects the subplot at the given row and column. "
    "Subsequent calls affect this subplot until a different one is selected.")
par("row", "Row index of the subplot"); spec(type.int, None)
par("col", "Column index of the subplot"); spec(type.int, None)
past_out("title")


# -----------------------------
# Signal methods
# -----------------------------

add(signal_class.clear, name = "signal.clear")
doc("Removes all points from the signal, making it empty.")
past_out("signal")

add(signal_class.lines, name = "signal.lines")
doc("Toggles line drawing between consecutive points of the signal.")
par("value", "Whether to connect points with lines"); spec(type.bool, True)
past_out("signal")

add(signal_class.label, name = "signal.label")
doc("Sets the signal label shown on the legend. If left empty, the default label is 'signal[N]', where N is the signal index in the plot.")
par("label", "The label to display on the legend"); spec(type.label, repr(None))
past_out("signal")

add(signal_class.fillx, name = "signal.fillx")
doc("Fills a vertical stem from each point down to the x axis.")
par("active", "Whether to draw the vertical fill lines"); spec(type.bool, True)
past_out("signal")

add(signal_class.filly, name = "signal.filly")
doc("Fills a horizontal stem from each point across to the y axis.")
par("active", "Whether to draw the horizontal fill lines"); spec(type.bool, True)
past_out("signal")

add(signal_class.line_method, name = "signal.line_method")
doc("Sets the line drawing method used between consecutive points.")
par("method", "The method used to draw lines"); spec(type.line_method, repr("simple"))
past_out("signal")

add(signal_class.fill_method, name = "signal.fill_method")
doc("Sets the fill drawing method used for fillx / filly stems.")
par("method", "The method used to draw fills"); spec(type.line_method, repr("simple"))
past_out("signal")

add(signal_class.fill, name = "signal.fill")
doc("Copies fill levels from another signal, useful when building custom stem plots or filled regions.")
par("signal", "Signal to copy the fill information from"); spec(type.signal)
past_out("signal")

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
# Terminal
# -----------------------------

add(terminal_class, name = "terminal")
doc("High-level manager for terminal interaction and sizing inside plotext.")
out("A terminal object", type.terminal)

add(terminal_class.clean, name = "terminal.clean")
doc("Clears the visible terminal output — either entirely, or by a specific number of lines above the prompt.")
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
