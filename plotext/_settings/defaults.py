# Default settings: terminal size, axis/grid/colors/pixels, subplot, legend, marker and miscellaneous defaults

from plotext._primitives.pixel import pixel


# Terminal
terminal = {
    "width": 211 * 2 // 3,
    "height": 53 * 2 // 3,
    "prompt height": 2,
    "limit width": True,
    "limit height": True}


# Axis
axis = {
    "status": True,
    "style": "default"}


# Grid
frequency = {
    "x": 7,
    "y": 5}


# Colors (foreground, background)
colors = {
    "matrix":  ("default", "white"),
    "label":   ("blue+",   "white"),
    "axis":    ("black",   "white"),
    "grid":    ("blue",    "white"),
    "ruler":   ("blue+",   "white"),
    "canvas":  ("default", "white"),
    "line":    ("orange",  "white"),
    "legend":  ("black",   "white")}


# Pixels (derived)
pixels = {k: pixel(*v) for k, v in colors.items()}


# Subplot
size_direction = 1
size_policy = "maximum"

# Bar plots
bar_width = 4 / 5

# Legend
legend = {
    "status": False,
    "relative": False,
    "x position": 0,
    "y position": 0,
    "axis status": True,
    "axis style": "default"}

# Marker
marker = "hd"

# Color sequence
color_sequence = [12, 10, 9, 14, 13, 11, 0, 15, 8, 7, 1, 2, 3, 4, 5, 6]

# Misc
date_origin_string = '01/01/1900'
