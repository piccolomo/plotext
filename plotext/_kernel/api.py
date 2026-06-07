# Public API: the terminal, the master figure, and a handful of standalone helpers.
# Plot methods (signal, draw, title, ...) are reached through plt.figure
# (e.g. plt.figure.subplot(1, 2).draw(plt.figure.signal(y))).

from time import sleep as _time_sleep
from plotext._kernel.terminal import terminal as _terminal_class
from plotext._methods.sequence import sin as _sin, square as _square, noise as _noise
from plotext._methods.string import uncolorize as _uncolorize
from plotext._methods.image import image as _image, gif as _gif
from plotext._methods.video import video as _video
from plotext._methods.matplotlib import matplotlib as _matplotlib
from plotext._examples.demo import colors as _colors, styles as _styles, markers as _markers, themes as _themes
from plotext._examples.test import run_tests as _run_tests


# Initialize terminal and master canvas
_terminal = _terminal_class()
_master = _terminal._master


# Public terminal instance
terminal = _terminal

# Public master figure — entry point for the explicit-figure API style
# (e.g. plt.figure.subplot(1, 2).draw(...)).
figure = _master

# Data helpers
sin = _sin
square = _square
noise = _noise
uncolorize = _uncolorize

# Pause execution between frames when streaming — reduces flicker; returns the seconds slept
def sleep(seconds = 0):
    _time_sleep(seconds)
    return seconds

# Direct image painter — returns a plotext.matrix without touching the figure pipeline
image = _image

# Animate a GIF in the terminal — q to exit
gif = _gif

# Play a video in the terminal: local file, URL, or YouTube URL — q to exit
video = _video

# Convert a matplotlib Figure into plt.figure (rebuilds subplots, lines, scatters, patches as native plotext signals)
matplotlib = _matplotlib

# Reference tables
colors = _colors
styles = _styles
markers = _markers
themes = _themes

# Test runner
test = _run_tests
