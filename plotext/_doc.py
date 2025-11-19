from plotext.prettydoc import docs
from plotext import *
from plotext.prettydoc._doc import type, message
from plotext._plot import plot_class

# Initialize docs
pd = docs(1, ': ')
add, alias, doc = pd.add_function, pd.add_alias, pd.add_doc
par, spec, past = pd.add_parameter, pd.add_parameter_spec, pd.add_past_parameter
out, past_out = pd.add_output, pd.add_past_output

# --------------------
# Pixel
# --------------------
add(pixel)
doc("Encapsulates color and style settings for a pixel, including foreground, background, and styling attributes.")
par("foreground", f"Foreground color; {message.colors}"); spec(type.color)
par("background", f"Background color; {message.colors}"); spec(type.color)
par("style", f"Styling attributes; {message.styles}"); spec(type.style)
out("Pixel object with color and style configuration", type.pixel)

add(pixel.set)
doc("Sets the color and style properties of the pixel.")
past("foreground", "pixel")
past("background", "pixel")
past("style", "pixel")
out("Updated pixel", type.pixel)

add(pixel.copy)
doc("Returns a copy of the pixel object.")
out("Pixel copy", type.pixel)

add(pixel.clone)
doc("Clones properties from another pixel to the current pixel.")
par("pixel", "Pixel to clone"); spec(type.pixel)
out("Updated source pixel", type.pixel)

add(pixel.get_string)
doc("Generates a string representation including color and style attributes.")
out("String representing the pixel", type.string)

# --------------------
# Colorize
# --------------------
add(colorize)
doc("Applies color and style attributes to a string.")
past("foreground", "pixel")
past("background", "pixel")
past("style", "pixel")
out("Colorized string object", type.colorize)

add(colorize.copy)
doc("Returns a duplicate of the colorize object.")
out("Duplicated colorize object", type.colorize)

add(colorize.clone)
doc("Copies properties from another colorize object.")
par("colorized", "Colorize object to copy from"); spec(type.colorize)
out("Updated colorize object", type.colorize)

add(colorize.get_length)
doc("Returns the string length excluding color/style ASCII codes.")
out("Length of colorless string", type.int)

add(colorize.get_matrix)
doc("Converts colorize object to a matrix representation.")
out("Matrix representation", type.matrix)

add(colorize.get_string)
doc("Returns string representation.")
par("colorless", "If True, excludes color/style codes"); spec(type.bool, False)
out("String with ASCII codes if present", type.style)

add(colorize.get_pixel)
doc("Returns pixel object representing the color/style of the colorize object.")
out("Pixel object", type.pixel)

add(colorize.set_pixel)
doc("Applies color/style from a pixel to the colorize object.")
par("pixel", "Pixel to copy from"); spec(type.pixel, type.pixel)
past_out("colorize.clone")

add(colorize.set_string)
doc("Replaces string content, preserving existing color/style.")
par("string", "New string"); spec(type.style)
past_out("colorize.clone")

add(colorize.print)
doc("Prints the colorized string to the console.")
par("colorless", "If True, prints without color/style codes"); spec(type.bool, False)
par("end", "String to append at end"); spec(type.style, repr('\n'))
par("flush", "Force flush output"); spec(type.bool, True)
past_out("colorize.clone")

add(colorize.hstack)
doc("Horizontally stacks two colorize objects into a matrix.")
par("colorized", "Object to stack"); spec(type.colorize)
par("adapt", "Adjust heights if True"); spec(type.bool, True)
out("Resulting matrix", type.matrix)

add(colorize.vstack)
doc("Vertically stacks two colorize objects into a matrix.")
par("colorized", "Object to stack"); spec(type.colorize)
par("adapt", "Adjust widths if True"); spec(type.bool, True)
out("Resulting matrix", type.matrix)

add(uncolorize)
doc("Removes all ASCII color and style codes from a string.")
out("String without color/style", type.string)

# --------------------
# Matrix
# --------------------
add(matrix)
doc("Creates a matrix with optional dimensions and pixel settings.")
par("width", "Matrix width in columns"); spec(type.int, 0)
par("height", "Matrix height in rows"); spec(type.int, 0)
past("pixel", "colorize.set_pixel"); spec(type.pixel, "empty pixel")
out("Initialized matrix", type.matrix)

add(matrix.clear)
doc("Clears all content in the matrix.")
past_out("matrix")

add(matrix.get_width)
doc("Returns matrix width in columns.")
out("Width", type.int)

add(matrix.get_height)
doc("Returns matrix height in rows.")
out("Height", type.int)

add(matrix.get_size)
doc("Returns matrix size as (width, height).")
out("Size tuple", type.tuple)

add(matrix.print)
doc("Prints the matrix content.")
past("colorless", "colorize.print")
past("end", "colorize.print")
past("flush", "colorize.print")
out("Source matrix object", type.colorize)

add(matrix.get_string)
doc("Generates a string representation of the matrix.")
past("colorless", "colorize.get_string")
out("String with ASCII codes if present", type.string)

add(matrix.hstack)
doc("Horizontally stacks two matrices.")
par("matrix", "Matrix to stack"); spec(type.matrix)
par("adapt", "Adjust heights if True"); spec(type.bool, False)
out("Resulting matrix", type.matrix)

add(matrix.vstack)
doc("Vertically stacks two matrices.")
par("matrix", "Matrix to stack"); spec(type.matrix)
par("adapt", "Adjust widths if True"); spec(type.bool, False)
out("Resulting matrix", type.matrix)

add(matrix.copy)
doc("Returns a duplicate of the matrix.")
out("Matrix copy", type.matrix)

add(matrix.insert)
doc("Inserts an object at specified coordinates in the matrix.")
par("col", "Column index"); spec(type.int)
par("row", "Row index"); spec(type.int)
par("matrix", "Object to insert"); spec(type.matrix)
par("ha", "Horizontal alignment"); spec(type.alignment, -1)
par("va", "Vertical alignment"); spec(type.alignment, 1)
par("adapt", "Trim if out-of-bounds"); spec(type.bool, True)
out("Updated matrix", type.matrix)

# --------------------
# Plot
# --------------------
add(plot_class.draw)
doc("Creates a scatter plot from x and y coordinates; supports multiple datasets.")
par("args", "Data points (x, y) or just y; strings with dates supported"); spec(type.data)
par("marker", "Symbol for each point; char, code, marker object, or list"); spec(type.marker, "hd")
par("plot", "Draw lines between points"); spec(type.bool, False)
par("fillx", "Draw vertical lines to x-axis or value"); spec(type.bool, False)
par("filly", "Draw horizontal lines to y-axis or value"); spec(type.bool, False)
par("xside", "Which x-axis: 'lower' or 'upper'"); spec(type.xside, 'lower')
par("yside", "Which y-axis: 'left' or 'right'"); spec(type.yside, 'left')
par("label", "Dataset label for legend; None disables"); spec(type.label, None)

add(plot_class.ruler)
doc("Controls plot rulers displaying numerical values.")
par("scale", "Ruler scale: linear or logarithmic"); spec("'linear' or 'log'", 'linear')
par("axis", "Axis to select: x or y"); spec(type.axis, 'x')
par("side", "Axis side: lower or upper"); spec(type.side, 0)

add(plot_class.xruler)
doc("Controls x-axis rulers.")
past("scale", "plot_class.ruler")
past("side", "plot_class.ruler")

add(plot_class.yruler)
doc("Controls y-axis rulers.")
past("scale", "plot_class.ruler")
past("side", "plot_class.ruler")

# --------------------
# Utilities
# --------------------
add(colors)
doc("Displays all available colors: string names, integers, RGB tuples.")

add(styles)
doc("Displays all available styles as string identifiers.")

add(sin, name="sin")
doc("Generates a sinusoidal signal for testing plotting methods.")
par("periods", "Number of sinusoidal cycles"); spec(type.float, 2)
par("length", "Number of points"); spec(type.int, 200)
par("amplitude", "Max height"); spec(type.float, 1)
par("phase", "Phase shift in pi units"); spec(type.float, 0)
par("decay", "Exponential decay rate"); spec(type.float, 0)
par("offset", "Added offset"); spec(type.float, 0)
out("List of floats representing the signal", type.floats)

add(test, name='test')
doc("Performs unit tests for plotext.")

# Finalize documentation
pd.update()
