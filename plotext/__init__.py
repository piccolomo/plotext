# Plotext package entry point: exposes public primitives and plot API

# Core metadata
from plotext._settings.system import platform, __version__, version

# Fundamental types
from plotext._primitives.pixel import pixel
from plotext._primitives.colorize import colorize
from plotext._primitives.matrix import matrix
from plotext._primitives.marker import marker

# Signal types (exposed under distinct names to avoid clashing with api.signal).
# signal_class itself is NOT re-exported: users must create signals through
# plotext.signal() rather than instantiating the class directly.
from plotext._signal.point_filled import point_filled_class as point
from plotext._signal.points import points_class as points

# Public plot API (signal, draw, title, label, sin, clf, show, ...)
from plotext._kernel.api import *

# Pretty documentation container (loaded after the API so plotext is fully initialized)
from plotext._doc.doc import docs as doc
