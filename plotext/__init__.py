"""\nplotext plots directly on terminal"""

__name__ = "plotext"
__version__ = "6.0.0beta"

from ._core import *
from ._doc import pd as doc

# TEMP
# from ._bar import bar
# from ._utility import *
# from ._ticks import *
# from ._axis import *
# from ._ticks import *
from ._marker import marker
from ._plot import *
from ._system import get_terminal_size, clear_terminal