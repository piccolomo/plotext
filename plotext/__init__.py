# Plotext package entry point: exposes public primitives and plot API

# Core metadata
from plotext._settings.system import platform, __version__, version

# Fundamental types
from plotext._primitives.pixel import pixel
from plotext._primitives.colorize import colorize
from plotext._primitives.matrix import matrix
from plotext._primitives.marker import marker
from plotext._primitives.box import line

# The public methods and attributes: figure, terminal, sin, image, colors, and the others listed in the api page.
from plotext._kernel.api import *

# Phase-driven text effects (shimmer, ...)
from plotext._methods.effects import effect

# File I/O helpers exposed as plotext.file (correct, read, write, exists, delete, parent, join)
from plotext._methods.file import file

# Pretty documentation container (loaded after the API so plotext is fully initialized)
from plotext._doc.doc import docs as doc