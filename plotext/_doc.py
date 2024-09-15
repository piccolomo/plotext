from .prettydoc import *
from ._core import *


pd = docs(1, ': ')
#pd = docs()
add = pd.add_function
alias = pd.add_alias
doc = pd.add_doc
par = pd.add_parameter
spec = pd.add_parameter_spec
past = pd.add_past_parameter
out = pd.add_output

class type:
	float = 'float'; 
	floats = 'floats'; 
	int = 'int'; 
	bool = 'bool'; 
	string = 'string'
	pixel = "plotext.pixel"
	colorize = "plotext.colorize"
	colorize_plus = "plotext.colorize or string"
	matrix = "plotext.matrix"
	matrix_plus = "plotext.matrix or plotext.colorize or string"
	color = "string color code, integer (lower than 256), a tuple of 3 integers (each lower than 256)"
	alignment = "string or integer"

class message:
	colors = "access the plotext.colors() method for the available color codes."
	styles = "access the plotext.styles() method for the available style codes."


add(sin)
doc("It returns a sinusoidal signal useful, for example, to quickly test some plotext methods")
par("periods", "the number of periods in the signal"); spec(type.float, 2)
par("length", "the number of data points"); spec(type.int, 200)
par("amplitude", "the amplitude of the signal"); spec(type.float, 1)
par("phase", "the phase of the sinusoidal (in pi units); 0.5 returns a cosine signal, while 1 a negative sinusoidal"); spec(type.float, 0)
par("decay", "the relative exponential decay rate of the signal (in units of length)"); spec(type.float, 0)
out('the sinusoidal signal', type.floats)

add(colors) 
doc("It displays the available string, integer and RGB color codes available in plotext.")

add(styles) 
doc("It displays the available string style codes available in plotext.")

add(pixel)
doc("It encaplusates color settings (or coloring), including both foreground and background colors, as well as style.")
par("foreground", "the foreground color; " + message.colors); spec(type.color)
par("background", "the background color; " + message.colors); spec(type.color)
par("style", "the style; " + message.styles); spec(type.string)
out("an object representing the coloring", type.pixel)

add(pixel.set)
doc("It sets colors and styling of the pixel.")
past("foreground", "pixel")
past("background", "pixel")
past("style", "pixel")
out("itself, updated", type.pixel)

add(pixel.copy)
doc("It returns a copy of the pixel object.")
out( "the pixel copy", type.pixel)

add(colorize)
doc("It adds colors and styling to a string.")
past("foreground", "pixel")
past("background", "pixel")
past("style", "pixel")
out("an object representing the colorized string", type.colorize)

add(colorize.copy)
doc("It returns a copy of the colorize object.")
out("the copy", type.colorize)

add(colorize.assign)
doc("It copies another colorize object to itself, without creating a new object.")
par('string', 'the object to copy'); spec(type.colorize_plus)
out("itself, updated", type.colorize)

add(colorize.get_length)
doc("It returns the colorless string length")
out("the length of the string, with no ascii codes", type.int)

add(colorize.get_matrix)
doc("It returns the matrix object version of itself")
out("the matrix version", type.matrix)

add(colorize.get_string)
doc("It returns the string version of itself")
par('colorless', 'whether to return the colorless version'); spec(type.bool, False)
out("the string version, with ascii codes, if present", type.string)

add(colorize.get_pixel)
doc("It returns the pixel representing its coloring.")
out("the coloring pixel", type.pixel)

add(colorize.set_pixel)
doc("It copies the coloring from a pixel object.")
par("pixel", "the pixel object to copy coloring from"); spec(type.pixel, type.pixel)
out("the colorize object with updated settings", type.colorize)

add(colorize.set_string)
doc("It copies a string, without affecting the coloring.")
par("string", "the string to copy"); spec(type.string)
out("the colorize object with updated settings", type.colorize)

add(colorize.print)
doc("It prints the colorized string.")
par('colorless', 'whether to print its colorless version'); spec(type.bool, False)
par('end', 'string printed at the end'); spec(type.string, repr('\n'))
par('flush', 'whether to forcibly flush the stream'); spec(type.bool, True)
out("itself", type.colorize)

add(colorize.hstack)
doc("It stacks two colorize objects horizontally.")
par('string', 'the object to stack'); spec(type.colorize_plus)
par('adapt', 'the height of the two objects must be the same, unless this parameter is set to True'); spec(type.bool, 1)
out("the matrix result", type.matrix)

add(colorize.vstack)
doc("It stacks two colorize objects vertically.")
par('string', 'the object to stack'); spec(type.colorize_plus)
par('adapt', 'the width of the two objects must be the same, unless this parameter is set to True'); spec(type.bool, 1)
out("colorize.hstack")

add(uncolorize)
doc("It remove any asci codes from a string.")
out("the string with no ascii coloring or styles.", type.string)

add(matrix)
doc("It creates a colored matrix")
par("width", "the matrix width"); spec(type.int, 0)
par("height", "the matrix height"); spec(type.int, 0)
past("pixel", "colorize.set_pixel"); spec(type.pixel, "a white pixel")
out("the matrix.", type.matrix)

add(matrix.get_width)
doc("It returns the matrix width")
out("the width", type.int)

add(matrix.get_height)
doc("It returns the matrix height")
out("the height", type.int)

add(matrix.print)
doc("It prints the matrix.")
past('colorless', 'colorize.print')
past('end', 'colorize.print')
past('flush', 'colorize.print'); 
out("itself", type.matrix)

add(matrix.get_string)
doc("It returns the string version of itself")
past('colorless', 'colorize.get_string')
out("the string version, with ascii codes, if present", type.string)

add(matrix.hstack)
doc("It stacks two matrix objects horizontally.")
par('object', 'the object to stack'); spec(type.matrix_plus)
par('adapt', 'the height of the two objects must be the same, unless this parameter is set to True'); spec(type.bool, 0)
out("itself", type.matrix)

add(matrix.vstack)
doc("It stacks two matrix objects vertically.")
par('object', 'the object to stack'); spec(type.matrix_plus)
par('adapt', 'the width of the two objects must be the same, unless this parameter is set to True'); spec(type.bool, 0)
out("itself", type.matrix)

add(matrix.copy)
doc("It returns a copy of the matrix object.")
out("the copy", type.matrix)


add(matrix.insert)
doc("Inserts an object at the specified coordinates inside itself.")
par("col", "The column coordinate where the element should be placed."); spec(type.int)
par("row", "The row coordinate where the element should be placed."); spec(type.int)
par("object", "The element to be inserted."); spec(type.matrix_plus)
par("ha", "The horizontal alignment, which can be 'left', 'center', 'right', or, equivalently, -1, 0, 1."); spec(type.alignment, -1)
par("va", "The vertical alignment, which can be 'top', 'center', 'bottom', or, equivalently, -1, 0, 1."); spec(type.alignment, -1)
par('adapt', "Allows objects to be inserted outside the matrix border without causing an error. The inserted object may be trimmed to ensure it does not exceed the matrix boundaries."); spec(type.bool, 1)
out("The updated matrix", type.matrix)

add(test)
doc("It performs unit tests for the plotext package.")

pd.update()
