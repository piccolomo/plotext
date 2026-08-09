# Tools section: matplotlib conversion and the test runner

from plotext._doc.tools import *
from plotext import matplotlib, test


section('tools')


add(matplotlib)
doc("Converts a matplotlib Figure into the plotext figure. Matplotlib is only imported by this method, so plotext does not require it.")
source("plotext")
par("figure", "A matplotlib figure object to convert", explanation("matplotlib_figure"))
out("The figure itself", explanation("figure"))


add(test)
doc("Runs the bundled unit test suite, a quick check that plotext works after a change or installation.")
source("plotext")
