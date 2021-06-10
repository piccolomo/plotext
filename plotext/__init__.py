"""\nplotext plots directly on terminal"""
import os as _os
import sys as _sys

_script_folder = _os.path.dirname(_os.path.realpath(__file__))
_sys.path.insert(0, _script_folder)


import utility as _utility 
import docstrings as _docstrings
from test import test

_sys.path.pop(0)

from plotext.plot import *

__name__ = "plotext"
__version__ = "3.1.2"