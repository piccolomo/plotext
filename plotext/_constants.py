# Binary choices
r2 = [0, 1]

# Axis names
axis_names = ['x', 'y']

# Sides per axis
xsides = ['lower', 'upper']
ysides = ['left', 'right']

# Common text symbols
space = ' '                 # Single space
new_line = '\n'             # New line character
comma = ', '                # Comma with space
colon = ': '                # Colon with space
empty = ''                  # Empty string
period = '.'                # Period
ansi_begin = '\x1b['        # ANSI escape sequence start

# Marker types and default marker
hd_markers_codes = ["none", "hd", "fhd", "braille"]

# Colors (basic palette)
color_codes = ['black', 'white', 'gray', 'gray+', 'red', 'red+', 'green', 'green+', 
'orange', 'orange+', 'blue', 'blue+', 'magenta', 'magenta+', 'cyan', 'cyan+']

# Plot limit alignments and adjustment delta
limit_alignments = ["center", "edge"]
delta = 10 ** (-4)
limit_delta = [0.5, delta]

# Directions for movement or orientation
directions = [-1, 1]

# Available scale types
scales = ["linear", "log"]

# Orientations and shorthand
orientations = ["vertical", "horizontal"]
orientations_short = ["v", "h"]

# Styles for axes and lines
axis_styles = ["default", "double", "dotted", "rounded"]
line_styles = axis_styles[:-2]

# Alignment constants for text
ha = ['left', 'center', 'right']   # Horizontal alignments
va = ['top', 'center', 'bottom']   # Vertical alignments
ha_short = [-1, 0, 1]              # Numeric codes for horizontal alignments

# Styles
style_codes = ['bold', 'dim', 'italic', 'underline', 'double-underline', 'strike', 'inverted', 'flash']

# Floats
inf = float('inf')

# Line drawing methods
line_methods = ["simple", "full"]
