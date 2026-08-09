# Plot inspection section: size, parent, master, position, log and time

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class


section('plot inspection')


add(plot_class.size)
doc("Returns the figure or subplot's size in terminal cells.")
source(["plotext.figure", "plotext.figure.subplot()"])
out("A (width, height) tuple", explanation("int_tuple"))


add(plot_class.parent)
doc("Climbs the hierarchy of nested subplots and returns the plot at the given nesting level: 0 is this plot itself, 1 its immediate parent, and so on. The parent of the master is the terminal, which is its own parent, so every climb ends there.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("level", "How many steps to climb, each step moving to the parent plot", explanation("int"), 1)
out("The parent at the requested level", explanation("figure") + " up to the master, then " + explanation("terminal"))


add(plot_class.master)
doc("Returns the master plot, the top-level plot that owns this subtree of subplots.")
source(["plotext.figure", "plotext.figure.subplot()"])
out("The master figure", explanation("figure"))


add(plot_class.position)
doc("Returns this subplot's position within its parent grid.")
source(["plotext.figure", "plotext.figure.subplot()"])
out("The subplot's position tuple", explanation("int_tuple"))


add(plot_class.log)
doc("Prints the tree of nested subplots, one indented line per plot, showing its position, its size, and the rows and columns of subplots it is divided into.")
source(["plotext.figure", "plotext.figure.subplot()"])
past_out("plotext.figure.plot_size")


add(plot_class.time)
doc("Prints a timing report of the most recent show or build, total elapsed time and, optionally, the time spent in each step, recursing into subplots (if present). Useful when investigating slow renders.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("full", "whether to include the time spent in each step; when False, only the total elapsed time is shown", explanation("bool"), True)
par("full", "includes the time spent in each build step and recurses into subplots, otherwise prints only this plot's total", explanation("bool"), True)
out("Total elapsed time of this plot in milliseconds", explanation("float"))
