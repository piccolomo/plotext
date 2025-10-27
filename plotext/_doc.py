from plotext.prettydoc import docs
from plotext import *
from plotext.prettydoc._doc import type, message
from plotext._plot import plot_class


pd = docs(1, ': ')
#pd = docs()
add = pd.add_function
alias = pd.add_alias
doc = pd.add_doc
par = pd.add_parameter
spec = pd.add_parameter_spec
past = pd.add_past_parameter
out = pd.add_output
past_out = pd.add_past_output


add(pixel)
doc("Encapsulates color and style settings for a pixel, including foreground and background colors, as well as styling attributes.")
par("foreground", "the foreground color; " + message.colors); spec(type.color)
par("background", "the background color; " + message.colors); spec(type.color)
par("style", "The styling attributes of the pixel.  " + message.styles); spec(type.style)
out("an object representing the pixel's color and style configuration", type.pixel)

add(pixel.set)
doc("Sets the color and style properties of the pixel.")
past("foreground", "pixel") 
past("background", "pixel")
past("style", "pixel")
out("The updated source pixel", type.pixel)

add(pixel.copy)
doc("It returns a copy of the pixel object.")
out("the pixel copy", type.pixel)

add(pixel.clone)
doc("It clones a pixel by copying the properties of the provided pixel to the source pixel.")
par("pixel", "the pixel to clone"); spec(type.pixel)
out("The updated source pixel", type.pixel)

add(pixel.get_string) 
doc("Generates a string representation of the pixel, incorporating its color and style attributes.") 
out("A string representing the pixel's properties, including ASCII codes if applicable", type.string)


add(colorize) 
doc("Applies color and style attributes to a string, enhancing its visual representation.") 
past("foreground", "pixel") 
past("background", "pixel") 
past("style", "pixel") 
out("An object encapsulating the colorized string", type.colorize)

add(colorize.copy) 
doc("Creates and returns a duplicate of the colorize object.") 
out("The duplicated colorize object", type.colorize)

add(colorize.clone) 
doc("Copies the properties of another colorize object into the current object") 
par('colorized', 'The colorize object to copy from'); spec(type.colorize) 
out("The updated source colorize object", type.colorize)

add(colorize.get_length) 
doc("Returns the length of the string, excluding any color or style ASCII codes.") 
out("The length of the colorless string", type.int)

add(colorize.get_matrix) 
doc("Converts the colorize object into its matrix representation.") 
out("The matrix representation of the colorize object", type.matrix)

add(colorize.get_string) 
doc("Returns the string representation of the colorize object.") 
par('colorless', 'If True, returns the string without color or style codes'); spec(type.bool, False) 
out("The string representation, including ASCII codes if present", type.style)

add(colorize.get_pixel) 
doc("Returns the pixel object representing the color and style settings of the colorize object.") 
out("The pixel object encapsulating the color settings", type.pixel)

add(colorize.set_pixel) 
doc("Applies color and style settings from a pixel object to the source colorize object.") 
par("pixel", "The pixel object from which to copy color and style settings"); spec(type.pixel, type.pixel) 
past_out("colorize.clone")

add(colorize.set_string) 
doc("Replaces the string content while preserving existing color and style settings.") 
par("string", "The new string"); spec(type.style) 
past_out("colorize.clone")

add(colorize.print) 
doc("Outputs the colorized string to the console.") 
par('colorless', 'If True, prints the string without color or style codes'); spec(type.bool, False) 
par('end', 'The string to append just before printing'); spec(type.style, repr('\n')) 
par('flush', 'If True, forces immediate flushing of the output stream'); spec(type.bool, True) 
past_out("colorize.clone")

add(colorize.hstack) 
doc("Horizontally combines two colorize objects into a single matrix.") 
par('colorized', 'The colorize object to stack horizontally'); spec(type.colorize) 
par('adapt', 'If True, adjusts the height of the objects to match; otherwise, heights must be identical'); spec(type.bool, True) 
out("The resulting matrix from horizontal stacking", type.matrix)

add(colorize.vstack) 
doc("Vertically combines two colorize objects into a single matrix.") 
par('colorized', 'The colorize object to stack vertically'); spec(type.colorize) 
par('adapt', 'If True, adjusts the width of the objects to match; otherwise, widths must be identical'); spec(type.bool, True) 
out("The resulting matrix from vertical stacking", type.matrix)


add(uncolorize)
doc("It remove any asci codes from a string.")
out("the string with no ascii coloring or styles.", type.string)



add(matrix) 
doc("Creates a matrix with specified dimensions and optional color settings.") 
par("width", "The width of the matrix in columns"); spec(type.int, 0) 
par("height", "The height of the matrix in rows"); spec(type.int, 0) 
past("pixel", "colorize.set_pixel"); spec(type.pixel, "an empty pixel") 
out("The initialized matrix object", type.matrix) 

add(matrix.clear) 
doc("Clears all content within the matrix, resetting it to an empty state.") 
past_out("matrix")

add(matrix.get_width) 
doc("Returns the width of the matrix in columns.") 
out("The matrix width", type.int)

add(matrix.get_height) 
doc("Returns the height of the matrix in rows.") 
out("The matrix height", type.int)

add(matrix.get_size) 
doc("Returns the matrix size as the tuple (width, height).") 
out("The matrix size", type.tuple)

add(matrix.print) 
doc("Displays the matrix content in the console.") 
past('colorless', 'colorize.print') 
past('end', 'colorize.print') 
past('flush', 'colorize.print') 
out("The source matrix object", type.colorize)

add(matrix.get_string) 
doc("Generates a string representation of the matrix.") 
past('colorless', 'colorize.get_string') 
out("The string representation, including ASCII codes if present", type.string)

add(matrix.hstack) 
doc("Horizontally combines two matrix objects side by side.") 
par('matrix', 'The matrix object to stack horizontally'); spec(type.matrix) 
par('adapt', 'If True, adjusts the height of the matrices to match; otherwise, heights must be identical'); spec(type.bool, False) 
out("The resulting matrix from horizontal stacking", type.matrix)

add(matrix.vstack) 
doc("Vertically combines two matrix objects one above the other.") 
par('matrix', 'The matrix object to stack vertically'); spec(type.matrix) 
par('adapt', 'If True, adjusts the width of the matrices to match; otherwise, widths must be identical'); spec(type.bool, False)
out("The resulting matrix from vertical stacking", type.matrix)

add(matrix.copy) 
doc("Returns a duplicate of the matrix object.") 
out("The duplicated matrix object", type.matrix)

add(matrix.insert) 
doc("Inserts an object at the specified coordinates within the matrix.") 
par("col", "The column index where the object will be inserted"); spec(type.int) 
par("row", "The row index where the object will be inserted"); spec(type.int) 
par("matrix", "The object to insert into the matrix"); spec(type.matrix) 
par("ha", "Horizontal alignment: 'left', 'center', 'right', or equivalently -1, 0, 1"); spec(type.alignment, -1) 
par("va", "Vertical alignment: 'top', 'center', 'bottom', or equivalently -1, 0, 1"); spec(type.alignment, 1) 
par('adapt', "If True, allows insertion beyond matrix boundaries, trimming the object to fit within the matrix"); spec(type.bool, True) 
out("The updated source matrix with the inserted object", type.matrix)


add(plot_class.draw) 
doc("Creates a scatter plot using the coordinates provided in the x and y lists.\n\n"
    "Multiple data sets can be plotted by calling consecutive plotting functions.")
par("args", "The x and y coordinates of the data points to be plotted (or just y). String-formatted dates are also supported."); spec(type.data)
par("marker", "The symbol used to represent each data point. It can be: a single character (e.g. 'x', '*'), a predefined marker code (e.g. 'hd'), available via the markers() method a marker object or a list of any of the above, one per data point."); spec(type.marker, "hd");
par("plot", "Whenever to plot lines between data points"); spec(type.bool, False);
par("fillx", "If True, draws a vertical line from each data point to the x-axis (y = 0). If a numeric value is provided, the line ends at that y-coordinate. If False, no vertical lines are drawn."); spec(type.bool, False)
par("filly", "If True, draws a horizontal line from each data point to the y-axis (x = 0). If a numeric value is provided, the line ends at that x-coordinate. If False, no horizontal lines are drawn."); spec(type.bool, False)
par("xside", "Specifies which x-axis to use: 'lower' or 'upper'."); spec(type.xside, 'lower')
par("yside", "Specifies which y-axis to use: 'left' or 'right'."); spec(type.yside, 'left')
par("label", "the label for the current data set. It appears in the legend menu in the top-left corner of the plot canvas. If None, no label is displayed."); spec(type.label, None)


add(plot_class.ruler)
doc("Controls the settings of the plot rulers, which display numerical values.")
par("scale", "The ruler scale: linear or logarithmic (base 10)"); spec("'linear' or 'log'", 'linear')
par("axis", "The axis (x or y) to select the ruler for"); spec(type.axis, 'x')
par("side", "Specifies which axis to use: 'lower' or 'upper'."); spec(type.side, 0)

add(plot_class.xruler)
doc("Controls the settings of the plot rulers, which display numerical values, relative to the x axis.")
past("scale", "plot_class.ruler")
past("side", "plot_class.ruler")

add(plot_class.yruler)
doc("Controls the settings of the plot rulers, which display numerical values, relative to the y axis.")
past("scale", "plot_class.ruler")
past("side", "plot_class.ruler")


add(colors)
doc("Displays the available color codes for use in plotext, including string names, integer codes, and RGB tuples.")

add(styles)
doc("Displays the available style codes for use in plotext, represented as string identifiers.")

add(sin, name = "sin")
doc("Generates a sinusoidal signal, useful for testing plotting methods in libraries like plotext.")
par("periods", "The number of complete sinusoidal cycles in the signal. Must be positive."); spec(type.float, 2)
par("length", "The number of data points in the signal. Higher values produce smoother signals. Must be a positive integer."); spec(type.int, 200)
par("amplitude", "The maximum height of the signal. Must be non-negative."); spec(type.float, 1)
par("phase", "The phase shift of the signal in pi units. Use 0 for sine, 0.5 for cosine, or 1 for negative sine."); spec(type.float, 0)
par("decay", "The exponential decay rate relative to length. Use 0 for no decay, positive values for amplitude reduction."); spec(type.float, 0)
par("offset", "An offset added to the final signal."); spec(type.float, 0)
out("A list of floats representing the sinusoidal signal.", type.floats)

add(test, name = 'test')
doc("It performs unit tests for the plotext package.")


pd.update()