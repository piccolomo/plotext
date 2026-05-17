# Data primitives: pixel, colorize (+ uncolorize, colors/styles/markers reference printers), marker, matrix

from plotext._doc.tools import *
from plotext._primitives.pixel import pixel as pixel_class
from plotext._primitives.colorize import colorize as colorize_class
from plotext._primitives.marker import marker as marker_class
from plotext._primitives.matrix import matrix as matrix_class
from plotext import uncolorize, colors, styles, markers


# Pixel

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


# Colorize

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


# Marker

add(marker_class, name = "marker")
doc("Creates a marker: a symbol with optional foreground, background and style, used to render points on the plot canvas.")
par("marker", "The marker to use. Possible entries: a single character; one of the character codes available via plotext.markers(); or a higher-resolution code ('hd', 'fhd', 'braille') that splits each character cell into sub-cells"); spec(type.marker_par)
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


# Matrix

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

add(matrix_class.get_html, name = "matrix.get_html")
doc("Returns the rendered HTML representation of the matrix — a run-length-compressed sequence of coloured ``<span>`` elements wrapped in ``<pre>`` so whitespace is preserved without ``&nbsp;``.")
out("HTML string ready to be embedded in a web page", type.string)

add(matrix_class.save, name = "matrix.save")
doc("Saves the matrix to disk. Dispatches by file extension: ``.html`` writes HTML via get_html(); ``.ansi`` writes colored text with ANSI escape codes; any other extension writes plain colorless text.")
par("path", "Output file path"); spec(type.string)
par("append", "If True, appends to the file instead of overwriting"); spec(type.bool, False)
past_out("matrix")

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
