"""\nplotext plots directly on terminal"""

from plotext._system import platform, __name__, __version__, version

# Internal imports: classes and constants
from plotext._pixel import pixel
from plotext._colorize import colorize
from plotext._matrix import matrix

# Mathematical and marker utilities
from plotext._marker import marker

from plotext._core import *

from plotext._demo import colors, styles

from plotext._test import run_tests as test

from plotext._doc import pd as doc

import plotext.prettydoc 

#from plotext._signal import signal_class as signal

#from plotext._color_cycler import * 

#from plotext._import import *

