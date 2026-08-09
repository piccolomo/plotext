# Drawing and rendering section: draw, build, show, interactive and sleep

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class
from plotext import sleep


section('drawing and rendering')


add(plot_class.draw)
doc("Registers a signal to be rendered when plotext.show() or plotext.build() is called. Signals are the objects returned by methods like signal(), bar(), text() or candlestick().")
source(["plotext.figure", "plotext.figure.subplot()"])
par("signal", "The signal to render", explanation("signal"))
out("The figure itself", explanation("figure"))


add(plot_class.build)
doc("Builds the final figure as a matrix, without printing it. Use show() to both build and print.")
source(["plotext.figure", "plotext.figure.subplot()"])
out("The final figure matrix", explanation("matrix"))

add(plot_class.show)
doc("Builds and prints the final figure to the terminal: equivalent to build().print(), with the same parameters passed along.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("colorless", "renders the output without colors", explanation("bool"), False)
par("flush", "flushes the terminal after printing", explanation("bool"), False)
past_out("plotext.figure.draw")

add(plot_class.interactive)
doc("Toggles the interactive mode: when on, every method that changes the figure (draw, title, theme, ...) reprints the whole figure immediately, so each change shows without calling show(). The mode persists across clear(), until interactive(False) is called.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("active", "turns interactive mode on or off", explanation("bool"), True)
past_out("plotext.figure.draw")


add(sleep)
doc("Pauses execution for the given number of seconds, useful between frames when streaming a continuous flow of data, to reduce screen flickering. Tweak the value manually to balance smoothness against responsiveness.")
source("plotext")
par("seconds", "Seconds to pause; may be fractional", explanation("float"), 0)
