# Public API: the terminal, the master figure, and a handful of standalone helpers.
# Plot methods (signal, draw, title, ...) are reached through plt.figure
# (e.g. plt.figure.subplot(1, 2).draw(plt.figure.signal(y))).

from plotext._kernel.terminal import terminal as _terminal_class
from plotext._methods.sequence import sin as _sin
from plotext._methods.string import uncolorize as _uncolorize
from plotext._examples.demo import colors as _colors, styles as _styles, markers as _markers
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
uncolorize = _uncolorize

# Reference tables
colors = _colors
styles = _styles
markers = _markers

# Test runner
test = _run_tests
