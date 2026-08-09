# Colorize section: the colorize object methods

from plotext._doc.tools import *
from plotext._primitives.colorize import colorize as colorize_class


section('colorize')


# Setters

add(colorize_class.fill)
doc("Applies the color and style settings of a pixel to the colorized object.")
source("plotext.colorize()")
par("pixel", "Pixel that determines the color and style", explanation("pixel_par"))
out("The colorized object itself", explanation("colorize"))

add(colorize_class.write)
doc("Replaces the string content, preserving the current pixel.")
source("plotext.colorize()")
par("string", "New string content", explanation("string"))
past_out("plotext.colorize().fill")


# Getters

add(colorize_class.pixel)
doc("Returns the pixel holding the colorized object's color and style.")
source("plotext.colorize()")
out("A pixel object", explanation("pixel"))

add(colorize_class.string)
doc("Returns the string, optionally stripping color and style ansi codes.")
source("plotext.colorize()")
par("colorless", "excludes the color and style ansi codes", explanation("bool"), False)
out("String, optionally including color codes", explanation("string"))

add(colorize_class.length)
doc("Returns the string length excluding the color and style ansi codes.")
source("plotext.colorize()")
out("Length of colorless string", explanation("int"))


# Transformers (in place)

add(colorize_class.upper)
doc("Uppercases the string in place, preserving the color and style.")
source("plotext.colorize()")
past_out("plotext.colorize().fill")

add(colorize_class.lower)
doc("Lowercases the string in place, preserving the color and style.")
source("plotext.colorize()")
past_out("plotext.colorize().fill")

add(colorize_class.title)
doc("Title-cases the string in place (first letter of every word uppercased), preserving the color and style.")
source("plotext.colorize()")
past_out("plotext.colorize().fill")


# Converters and combiners (return a matrix)

add(colorize_class.matrix)
doc("Converts the colorized object to a matrix. Newlines in the string split the result into multiple rows; the width matches the widest line.")
source("plotext.colorize()")
out("Matrix representation of the colorized object", explanation("matrix"))

add(colorize_class.hstack)
doc("Horizontally stacks this colorized object with another item (a colorize, matrix, or raw string), returning a matrix. The + operator between any such pair is a shortcut for this method (with adapt = True).")
source("plotext.colorize()")
par("item", "Object to stack: a colorize, matrix, or raw string", explanation("matrix_insertable"))
par("adapt", "adjusts heights to match", explanation("bool"), True)
out("Resulting matrix", explanation("matrix"))

add(colorize_class.vstack)
doc("Vertically stacks this colorized object with another item (a colorize, matrix, or raw string), returning a matrix. The / operator between any such pair is a shortcut for this method (with adapt = True).")
source("plotext.colorize()")
par("item", "Object to stack: a colorize, matrix, or raw string", explanation("matrix_insertable"))
par("adapt", "adjusts widths to match", explanation("bool"), True)
out("Resulting matrix", explanation("matrix"))


# Output

add(colorize_class.print)
doc("Prints the colorized string.")
source("plotext.colorize()")
par("colorless", "prints without the color and style ansi codes", explanation("bool"), False)
par("flush", "flushes the output after printing", explanation("bool"), False)
past_out("plotext.colorize().fill")


# Copy / clone

add(colorize_class.copy)
doc("Returns a copy of the colorized object.")
source("plotext.colorize()")
out("Colorized copy", explanation("colorize"))

add(colorize_class.clone)
doc("Copies properties from another colorized object.")
source("plotext.colorize()")
par("colorized", "Colorized object to copy from", explanation("colorize"))
past_out("plotext.colorize().fill")
