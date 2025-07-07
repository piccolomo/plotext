# from plotext._pixel import pixel_class
# from plotext._marker import marker_class

# Binary choices range
r2 = [0, 1]

# Axis names
axis_names = ['x', 'y']

# Sides per axis
xsides = ['lower', 'upper']
ysides = ['left', 'right']

# Common text symbols
space = ' '
new_line = '\n'
comma = ', '
colon = ': '
empty = ''
period = '.'
ansi_begin = '\x1b['

# Marker types and default marker
hd_markers = ["hd", "fhd", "braille"]
default_marker = "hd"

# Plot limit alignments and adjustment delta
limit_alignments = ["center", "edge"]
delta = 10 ** (-4)
limit_delta = [0.5 + delta, 0 + delta]

# Directions for movement or orientation
directions = [-1, 1]

# Available scale types
scales = ["linear", "log"]

# Orientations and their shorthand forms
orientations = ["vertical", "horizontal"]
orientations_short = ["v", "h"]

# Styles for axes and lines
axis_styles = ["default", "double", "dotted", "rounded"]
line_styles = axis_styles[:-2]

# Alignment constants for text
ha = ['left', 'center', 'right']      # Horizontal alignments
va = ['top', 'center', 'bottom']      # Vertical alignments
ha_short = [-1, 0, 1]                  # Numeric codes for horizontal alignments


color_codes = ['black', 'white', 'gray', 'gray+', 'red', 'red+', 'green', 'green+', 'orange', 'orange+', 'blue', 'blue+', 'magenta', 'magenta+', 'cyan', 'cyan+']
style_codes = ['bold', 'dim', 'italic', 'underline', 'double-underline', 'strike', 'inverted', 'flash']


# # Basic Pixels
# empty_pixel = pixel_class()  # Create an empty pixel
# white_pixel = pixel_class("", "white")  # Create an empty pixel

# # Default marker instance with default attributes
# default_marker = marker_class()



