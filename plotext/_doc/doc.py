# Aggregator: each section file registers its docstrings via the shared prettydoc manager from tools.py; this module imports them in order then triggers a single update().

from plotext._doc.tools import pd, section, add, doc, source, out
from plotext._doc.types import explanation
from pathlib import Path
from importlib import import_module

# Load every numbered section file in name order, which sets the menu order
for section_path in sorted(Path(__file__).parent.glob("sections/[0-9]*.py")):
    import_module("plotext._doc.sections." + section_path.stem)

docs = pd.update()

# Register the documentation container itself, then refresh it so its own entry applies
section('plotext components')
add(docs, name = "doc")
doc("Accesses the documentation of every plotext method and attribute. This is both an attribute and a method: calling it as a method, like doc(), opens the interactive menu of the whole documentation, while doc.<name>() prints the documentation of a single method or attribute; calling <name>.doc(), on any documented object, does the same.\nWhen several methods share a name, adding the source distinguishes them: doc.pixel.clone() and doc.signal.clone() print each their own clone() documentation.")
source("plotext")
out("The whole plotext documentation", explanation("documentation"))
pd.update(docs)
