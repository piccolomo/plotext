# Matrix section: the matrix object methods

from plotext._doc.tools import *
from plotext._primitives.matrix import matrix as matrix_class


section('matrix')


# Setters

add(matrix_class.fill)
doc("Applies the given pixel to every cell of the matrix, preserving each cell's existing glyph (only color and style are overwritten).")
source("plotext.matrix()")
par("pixel", "Pixel whose color and style are copied onto every cell", explanation("pixel_par"))
out("The matrix object itself", explanation("matrix"))

add(matrix_class.clear)
doc("Clears the content of every cell in the matrix; its size remains unchanged.")
source("plotext.matrix()")
past_out("plotext.matrix().fill")

add(matrix_class.insert)
doc("Inserts a matrix, colorize, or raw string at the given position.")
source("plotext.matrix()")
par("col", "Column index position where to insert the item", explanation("int"))
par("row", "Row index position where to insert the item", explanation("int"))
par("item", "Object to insert", explanation("matrix_insertable"))
par("ha", "Horizontal alignment anchor", explanation("alignment_h"), -1)
par("va", "Vertical alignment anchor", explanation("alignment_v"), -1)
past_out("plotext.matrix().fill")

add(matrix_class.transpose)
doc("Transposes the matrix in place: rows become columns.")
source("plotext.matrix()")
past_out("plotext.matrix().fill")


# Getters

add(matrix_class.width)
doc("Returns the matrix width in columns.")
source("plotext.matrix()")
out("Matrix width", explanation("int"))

add(matrix_class.height)
doc("Returns the matrix height in rows.")
source("plotext.matrix()")
out("Matrix height", explanation("int"))

add(matrix_class.size)
doc("Returns the matrix size as a (width, height) tuple.")
source("plotext.matrix()")
out("A (width, height) tuple", explanation("int_tuple"))

add(matrix_class.get)
doc("Returns the pixel coloring the character at the given row and column; negative indexes count from the end, and an index outside the matrix raises an error.")
source("plotext.matrix()")
par("row", "Row index of the character", explanation("int"))
par("col", "Column index of the character", explanation("int"))
out("The pixel of that character", explanation("pixel"))


# Combiners

add(matrix_class.hstack)
doc("Horizontally stacks this matrix with another item (a matrix, colorize, or raw string). The + operator between any such pair is a shortcut for this method (with adapt = True).")
source("plotext.matrix()")
par("item", "Object to stack horizontally: a matrix, colorize, or raw string", explanation("matrix_insertable"))
par("adapt", "adjusts heights to match", explanation("bool"), False)
out("Resulting matrix", explanation("matrix"))

add(matrix_class.vstack)
doc("Vertically stacks this matrix with another item (a matrix, colorize, or raw string). The / operator between any such pair is a shortcut for this method (with adapt = True).")
source("plotext.matrix()")
par("item", "Object to stack vertically: a matrix, colorize, or raw string", explanation("matrix_insertable"))
par("adapt", "adjusts widths to match", explanation("bool"), False)
out("Resulting matrix", explanation("matrix"))


# Output

add(matrix_class.string)
doc("Returns the rendered matrix as a multi-line string, one line per row.")
source("plotext.matrix()")
past_par("colorless", "plotext.colorize().string")
out("Rendered matrix string", explanation("string"))

add(matrix_class.html)
doc("Returns the HTML representation of the matrix.")
source("plotext.matrix()")
out("html string for the matrix, the colored block alone, ready to sit inside a page of your own", explanation("string"))

add(matrix_class.print)
doc("Prints the matrix.")
source("plotext.matrix()")
past_par("colorless", "plotext.colorize().print")
past_par("flush", "plotext.colorize().print")
past_out("plotext.matrix().fill")

add(matrix_class.save)
doc("Saves the matrix to a file. The file extension determines the format: .html saves a whole web page, naming the character set and a monospaced font so that a browser draws it correctly, .ansi saves text with ANSI color codes, anything else saves plain uncolored text.")
source("plotext.matrix()")
par("path", "Output file path", explanation("string"))
par("colorless", "overrides the extension default: True forces plain text, False keeps color codes/spans", explanation("bool"), None)
par("append", "appends to the file instead of overwriting", explanation("bool"), False)
par("log", "prints a confirmation of the operation", explanation("bool"), False)
past_out("plotext.matrix().fill")


# Copy / clone

add(matrix_class.copy)
doc("Returns a copy of the matrix.")
source("plotext.matrix()")
out("Matrix copy", explanation("matrix"))

add(matrix_class.clone)
doc("Copies the contents of another matrix into this one in place.")
source("plotext.matrix()")
par("matrix", "Matrix whose contents are to be copied", explanation("matrix"))
past_out("plotext.matrix().fill")
