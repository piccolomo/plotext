# Public API bindings: terminal, master canvas and plot methods

from plotext._kernel.terminal import terminal as _terminal_class
from plotext._methods.sequence import sin as _sin
from plotext._methods.string import uncolorize as _uncolorize
from plotext._examples.demo import colors as _colors, styles as _styles, markers as _markers
from plotext._examples.test import run_tests as _run_tests

# Initialize terminal and master canvas
_terminal = _terminal_class()
_master = _terminal._master
_active = _master._active


# Public terminal instance
terminal = _terminal

# Data helpers
sin = _sin
uncolorize = _uncolorize

# Reference tables
colors = _colors
styles = _styles
markers = _markers

# Test runner
test = _run_tests

# Plot lifecycle
clf = _active.clf
clear = _active.clear
build = _active.build
show = _active.show

# Signal creation and drawing
signal = _active.signal
draw = _active.draw

# Compound drawing primitives
candlestick = _active.candlestick

# Labels
title = _active.title
label = _active.label

# Legend
legend = _active.legend

# Axes / frame
axis = _active.axis
frame = _active.frame

# Ruler settings
alignment = _active.alignment
direction = _active.direction
scale = _active.scale
lim = _active.lim
frequency = _active.frequency
ticks = _active.ticks
grid = _active.grid
date = _active.date
convert = _active.convert

# Canvas / size
canvas_pixel = _active.canvas_pixel
plot_size = _active.plot_size

# Subplots
subplot = _active.subplot
subplots = _active.subplots