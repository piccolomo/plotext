# Internal imports: classes and constants
from plotext._cimport import pixel_class, colorize_class as colorize, matrix_class as matrix

# Terminal utilities and classes
from plotext._terminal import terminal_class as _terminal_class

# Mathematical and marker utilities
from plotext._methods import list_methods as _list_methods
from plotext._marker import marker_class as marker

from plotext._demo import colors, styles
from plotext._methods import string_methods as _string_methods

class pixel(pixel_class):
	pass


# Initialize terminal and master canvas
terminal = _terminal_class()
master = terminal.master

# Terminal utility functions
terminal_size = terminal.get_size
clear_terminal = terminal.clear

# Trigonometric utility
sin = _list_methods.sin
uncolorize = _string_methods.uncolorize


# Docsrings
#from plotext._doc import docs