# Signal section: the signal creation method and the signal object methods

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class
from plotext._signal.signal import signal_class
from plotext._signal.point_filled import point


section('signal')


add(plot_class.signal)
doc("Creates a signal, a sequence of points to be plotted.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("*args", "Input data: x, y coordinates, or a single y sequence, whose points are counted along x from 1 to their number; date values are also supported", explanation("data_multiple"))
par("marker", "Symbol used to represent each data point", explanation("marker_par"), explanation("marker_default"))
par("xside", "Which x axis to plot against", explanation("xside"), repr('lower'))
par("yside", "Which y axis to plot against", explanation("yside"), repr('left'))
out("A signal object", explanation("signal"))


# Signal methods

add(signal_class.clear)
doc("Removes all points from the signal, making it empty.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
out("The signal object itself", explanation("signal"))

add(signal_class.label)
doc("Sets the signal label shown on the legend. Labelling a signal is enough to make the legend appear, so legend() is needed only to place it, color it, or switch it off. A signal left unlabelled stays out of the legend.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
par("label", "The label to display on the legend", explanation("label"), None)
past_out("plotext.figure.signal().clear")

add(signal_class.lines)
doc("Draw lines between all consecutive points. Use signal.line() to draw a single segment at a given point instead.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
par("active", "True to connect all points, False to disconnect them", explanation("bool"), True)
past_out("plotext.figure.signal().clear")

add(signal_class.line)
doc("Draw a line from a point to the one before.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
par("index", "Position of the point whose segment to toggle. Out-of-range indices are silently ignored. The first point (index 0) has no predecessor and is therefore always ignored", explanation("int"))
par("active", "True to draw the segment, False to break it", explanation("bool"), True)
past_out("plotext.figure.signal().clear")

add(signal_class.fillx)
doc("Draws a vertical line from each point down to the x axis.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
par("active", "Whether to draw the vertical line", explanation("bool"), True)
past_out("plotext.figure.signal().clear")

add(signal_class.filly)
doc("Draws a horizontal line from each point across to the y axis.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
par("active", "Whether to draw the horizontal line", explanation("bool"), True)
past_out("plotext.figure.signal().clear")

add(signal_class.fill)
doc("Uses the points of another signal as fill points on the current one, useful when building custom stem plots or filled regions.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
par("signal", "Signal to copy the fill information from", explanation("signal"))
past_out("plotext.figure.signal().clear")

add(signal_class.density)
doc("Sets how densely the connecting or filling lines are drawn. Use simple for evenly-spaced points (light and fast, may leave small gaps on steep segments) or full to fill every cell crossed (denser, visually continuous). Connecting lines are turned on via lines() or line() while filling lines are activated using fillx(), filly(), fill().")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
par("method", "Line drawing method for connecting lines or filling lines", explanation("line_method"), repr("simple"))
par("scope", "Which lines to apply the method to: connecting, filling, or both", explanation("line_method_scope"), repr("both"))
past_out("plotext.figure.signal().clear")


# Getters

add(signal_class.length)
doc("Returns the number of points currently in the signal.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
out("Number of points", explanation("int"))

add(signal_class.get)
doc("Returns the point at the given index.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
par("index", "Position of the point in the signal", explanation("int"))
out("The point at that position", explanation("point"))


# Output

add(signal_class.log)
doc("Prints a text summary of the signal and of every point. The ↑ symbol next to a point indicates that it is connected to the previous point by a line.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
past_out("plotext.figure.signal().clear")


# Copy / clone

add(signal_class.copy)
doc("Creates and returns a deep copy of the signal.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
out("A deep copy of the signal", explanation("signal"))

add(signal_class.clone)
doc("Overwrites this signal in place with a copy of another: both its points and its settings. Useful to update a signal already registered with the draw() method, which keeps its place in the plot while taking the new content.")
source(["plotext.figure.signal()", "plotext.figure.subplot().signal()"])
par("signal", "Signal copied into this one", explanation("signal"))
past_out("plotext.figure.signal().clear")
