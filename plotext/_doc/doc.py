# Aggregator: each section file registers its docstrings via the shared prettydoc manager from tools.py; this module imports them in order then triggers a single update().

from plotext._doc.tools import pd
from plotext._doc.sections import plot, signal, draw, frame, subplots, terminal, primitives, file, prettydoc

docs = pd.update()
