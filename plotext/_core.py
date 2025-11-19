# Terminal and utilities
from plotext._terminal import terminal_class as _terminal_class
from plotext._methods.list import sin as _sin
from plotext._methods.string import uncolorize as _uncolorize

# Initialize terminal and master canvas
_terminal = _terminal_class()
_master = _terminal._master
active = _master._active

# Expose terminal methods globally
for name in dir(_terminal):
    if not name.startswith("_"):
        attr = getattr(_terminal, name)
        if callable(attr):
            globals()[name] = attr

# Expose master methods globally
for name in dir(_master):
    if not name.startswith("_"):
        attr = getattr(_master, name)
        if callable(attr):
            globals()[name] = attr

# Master canvas reference
master = _master

# Trigonometric and string utilities
sin = _sin             # Sine function
uncolorize = _uncolorize  # Remove ANSI color codes from string
