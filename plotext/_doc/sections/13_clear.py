# Clear section: the clearing methods

from plotext._doc.tools import *
from plotext._plotter.clear import clear_class
from plotext._settings import defaults


section('clear')


add(clear_class.all)
doc("Clears all signals, subplots, sizes and settings (including colors and styles), reverting the plot to default: equivalent to calling all the methods within the clear attribute, or the attribute itself as a method, like clear().")
source(["plotext.figure.clear", "plotext.figure.subplot().clear"])
out("The clear component itself", explanation("clear"))

add(clear_class.data)
doc("Drops the plotted data: every signal added via draw(), the lines placed by line() and event(), and the corresponding legend entries; the color cycler rewinds to a full pool.")
source(["plotext.figure.clear", "plotext.figure.subplot().clear"])
past_out("plotext.figure.clear.all")

add(clear_class.settings)
doc("Resets the plot's settings back to defaults: the title, the axis labels, the axes visibility, the legend visibility, position and alignment, and the rulers (limits, ticks, frequency, scale, direction, alignments, date support, grid).")
source(["plotext.figure.clear", "plotext.figure.subplot().clear"])
past_out("plotext.figure.clear.all")

add(clear_class.pixels)
doc("Resets every pixel on this plot (labels, rulers, axes, legend and canvas) to the package defaults.")
source(["plotext.figure.clear", "plotext.figure.subplot().clear"])
past_out("plotext.figure.clear.all")

add(clear_class.styles)
doc("Resets the line styles of the axes and grid lines to the default style.")
source(["plotext.figure.clear", "plotext.figure.subplot().clear"])
past_out("plotext.figure.clear.all")

add(clear_class.size)
doc("Resets the plot size, so that every subplot takes a fresh share at the next plot_size call. On the master plot the terminal size is read again, while the terminal own settings, its prompt height and its size limits, are left as they were set: only plotext.terminal.clear() resets those.")
source(["plotext.figure.clear", "plotext.figure.subplot().clear"])
past_out("plotext.figure.clear.all")

add(clear_class.subplots)
doc("Wipes the subplot grid configured via subplots(), so the figure holds a single plot again.")
source(["plotext.figure.clear", "plotext.figure.subplot().clear"])
past_out("plotext.figure.clear.all")
