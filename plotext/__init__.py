"""\nplotext plots directly on terminal"""
    
__name__ = "plotext"
__version__ = "6.0.0beta"

from ._core import *
#from .prettydoc import *
#from .prettydoc import _doc as pdoc
from ._doc import pd as doc
from ._tests import run_tests as test