# Plot components section: terminal, figure and the figure component getters (subplot, ruler, date, clear)

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class
from plotext._kernel.api import figure, terminal


section('plot components')


add(terminal, name = "terminal")
doc("Controls the terminal: its interaction and sizing inside plotext. This is an attribute. Its methods read and limit the terminal size, wipe printed rows and check key presses.")
source("plotext")
out("A terminal object", explanation("terminal"))


add(figure, name = "figure")
doc("Accesses the master figure: the plot object on which every drawing and dressing method is called. This is an attribute. Its methods create the signals to plot (signal, bar, hist, box, candlestick, error, event, heatmap, cmatrix, rectangle, polygon, segment, line, text, image), draw and render them (draw, show, build), dress it up (title, label, axes, canvas, legend), divide the figure into subplots (subplots, subplot, plot_size), configure its look (theme, interactive), reach its components (clear, ruler, date) and inspect its state (size, position, master, parent, time, log). The subplots, returned by its subplot() method, offer the same methods.")
source("plotext")
out("The master figure", explanation("figure"))


add(plot_class.subplot)
doc("Returns the subplot at the given position within the grid of subplots, to be used like the figure itself.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("row", "Row index of the subplot", explanation("int"), 1)
par("col", "Column index of the subplot", explanation("int"), 1)
out("The subplot at (row, col)", explanation("figure"))


add(plot_class.ruler)
doc("Returns the ruler relative to the selected axis and side. A ruler is the area alongside its axis where the numerical ticks and their labels appear: it sets which range of data is on display (lim), where the ticks fall and what they read (ticks, frequency), how values grow along it (scale, direction), and how it is drawn (alignment, pixel, grid).")
source(["plotext.figure", "plotext.figure.subplot()"])
par("axis", "Axis to access: x, y, or both", explanation("axis_multiple"), repr('x'))
par("side", "Axis side to access: one or both", explanation("side_multiple"), 0)
out("The selection of the chosen rulers", explanation("ruler"))


add(plot_class.date)
doc("Returns the date converter relative to the selected axis and side. A date converter adds date and time support to the selected axis: its methods turn the support on and off (activate, active, clear), convert dates between forms (convert), and report reference dates (today, origin).")
source(["plotext.figure", "plotext.figure.subplot()"])
past_par("axis", "plotext.figure.ruler")
past_par("side", "plotext.figure.ruler")
out("The selection of the chosen date converters", explanation("date_converter"))


add(figure.clear, name = "clear")
doc("Controls the clearing of the plot. This is both an attribute and a method. Its methods reset one aspect of the plot each (data, settings, pixels, styles, size, subplots). Calling it as a method, like clear(), resets everything, is equivalent to clear.all(), and returns the figure.")
source(["plotext.figure", "plotext.figure.subplot()"])
out("The clear component of the plot", explanation("clear"))
