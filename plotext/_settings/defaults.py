# Default settings: terminal size, axis/grid/colors/pixels, subplot, legend, marker and miscellaneous defaults

from plotext._primitives.pixel import pixel
from plotext._settings.system import platform
from datetime import datetime, timezone


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
    "status": None,
    "relative": False,
    "x position": 0,
    "y position": 0,
    "axis status": True,
    "axis style": "default"}


# Marker: the four quarter blocks of hd draw on every system tried, windows included, so hd is the default everywhere; version 5 used a single dot on windows, whose terminals could not always draw them
marker = "hd"


# Color sequence
pixel_sequence = [pixel(foreground = c) for c in [12, 10, 9, 14, 13, 11, 0, 15, 8, 7, 1, 2, 3, 4, 5, 6]]


# The decimals added to the tick labels, on top of the ones needed to tell one tick from the next; raise it to keep the labels steady while the data moves
tick_extra_decimals = 0


# Misc
date_origin_datetime = datetime(1900, 1, 1, tzinfo = timezone.utc)   # the moment counting as time zero, read as it is, so it fits any date format


# Candlestick wick + body foreground colors (override globally for custom themes)
candlestick_up_color   = "green"
candlestick_down_color = "red"


# Documentation text: the title above the interactive menu and its three column headers; the prettydoc defaults take them from here.
doc_pixels = {
    "title":  pixel(foreground = "green+", style = "bold"),
    "header": pixel()}


# Coloring for the time() timing report. The header takes the documentation title pixel, so the timing report reads consistently with docstrings.
time_report = {
    "header":      doc_pixels["title"],
    "header time": pixel(                       style = "bold"),
    "arrow":       pixel(                       style = "dim"),
    "label":       pixel(foreground = "blue+"),
    "time":        pixel()}


# Coloring for the prefix of every log parameter output, matching the documentation title
log_prefix_pixel = doc_pixels["title"]


# Coloring for the prefix of every error message
error_prefix_pixel = pixel(foreground = "red+", style = "bold")


# Coloring for the prefix of every warning, something refused with nothing going wrong
warning_prefix_pixel = pixel(foreground = "orange+", style = "bold")
