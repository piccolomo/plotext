# Short names for the prettydoc methods, used by every section file.

from plotext.prettydoc import docs
from plotext._primitives.pixel import pixel as _pixel
from plotext._doc.types import explanation


# Initialize docs
pd = docs(colorless = 1)
pd.title("Plotext Documentation")
add, doc = pd.function, pd.description
par, past_par = pd.parameter, pd.past_parameter
source = pd.source
out, past_out = pd.output, pd.past_output

section = pd.section

# Display-only stand-in for a (default, white) pixel: the ansi "default" foreground reads as light-on-white in dark terminals and vanishes, so docs render it as black-on-white instead.
doc_default_pixel = _pixel("black", "white")
