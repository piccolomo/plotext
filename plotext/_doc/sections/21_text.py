# Text section: the string tools (uncolorize, effect)

from plotext._doc.tools import *
from plotext._settings import defaults
from plotext import effect, uncolorize


section('text')


add(uncolorize)
doc("Removes all color and style codes, returning a plain string.")
source("plotext")
par("item", "The string, colorized object or matrix to strip", explanation("label"))
out("String without the color and style codes", explanation("string"))


add(effect)
doc("Colors each character of the text with the chosen effect, returning a single-row matrix; increase step between calls to animate, for example on a title updated in a loop.")
source("plotext")
par("text", "The string to style", explanation("string"))
par("name", "Effect name: one of shimmer, pulse, rainbow, gradient", explanation("string"), "shimmer")
par("step", "Animation phase; advance between frames to animate", explanation("float"), 0.0)
par("period", "Number of step units after which the effect repeats; if None, it defaults to 10 for pulse and rainbow, and to the text length for shimmer and gradient", explanation("float"), None)
out("Styled 1-row matrix", explanation("matrix"))
