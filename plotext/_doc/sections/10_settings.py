# Settings section: plot_size, theme and subplots

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class


section('settings')


add(plot_class.plot_size)
doc("Sets the size of this plot, in terminal cells, and optionally how subplot sizes are redistributed and harmonized.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("width", "Plot width in terminal columns", explanation("int"), None)
par("height", "Plot height in terminal rows", explanation("int"), None)
par("direction", "Direction of the redistribution of subplot sizes within the maximum available size: with +1 it runs left-to-right across widths and top-to-bottom across heights, and the last subplot absorbs whatever space is left; with -1 the order is reversed, so the first subplot absorbs the leftover instead. If None, the previously set direction remains unchanged", explanation("direction"), repr(None))
par("policy", "How nested subplot sizes among rows or columns are harmonized when they disagree: with maximum the subplot size along each column or row takes the largest requested one; with minimum it takes the smallest. If None, the previously set policy remains unchanged", explanation("size_policy"), repr(None))
out("The figure itself", explanation("figure"))


add(plot_class.theme)
doc("Colors the whole plot in one call, following the chosen theme: it sets the canvas background, the axes, the tick labels, the title and axis labels, the legend, and the sequence of colors given to successive signals. The default theme restores the out-of-the-box look, with every color back to its package default. Use plotext.themes() for a preview of the available themes.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("name", "Theme name; unknown names fall back to the default theme", explanation("theme"), repr("default"))
past_out("plotext.figure.plot_size")


add(plot_class.subplots)
doc("Divides this plot into a grid of subplots.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("rows", "Number of subplot rows", explanation("int"), None)
par("cols", "Number of subplot columns", explanation("int"), None)
past_out("plotext.figure.plot_size")
