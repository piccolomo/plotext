# Signal: factory method (plot_class.signal) + signal_class instance methods

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class
from plotext._signal.signal import signal_class


add(plot_class.signal, name = "signal")
doc("Creates a signal, a sequence of points to be plotted. Line drawing is configured on the returned signal via its fluent methods (lines, point_lines); line_method and fill_method are construction-time parameters here; label and stem fills (fillx, filly) are also set fluently on the signal.")
par("args", "Input data: x, y coordinates, or a single y sequence; date values are also supported"); spec(type.data_multiple)
par("marker", "Symbol used to represent each data point"); spec(type.marker_par_draw, repr("hd"))
par("line_method", "How densely the connecting lines are drawn (simple or full); applies only when lines have been turned on via signal.lines() or signal.point_lines()"); spec(type.line_method, repr("simple"))
par("fill_method", "How densely fills are drawn for points carrying fill data (simple or full)"); spec(type.line_method, repr("simple"))
par("xside", "Which x axis to plot against"); spec(type.xside, repr('lower'))
par("yside", "Which y axis to plot against"); spec(type.yside, repr('left'))
out("The signal itself", type.signal)


# Signal methods

add(signal_class.clear, name = "signal.clear")
doc("Removes all points from the signal, making it empty.")
past_out("signal")

add(signal_class.label, name = "signal.label")
doc("Sets the signal label shown on the legend. If left empty, the default label is 'signal[N]', where N is the signal index in the plot.")
par("label", "The label to display on the legend"); spec(type.label, repr(None))
past_out("signal")

add(signal_class.lines, name = "signal.lines")
doc("Connects every point of the signal uniformly. Pass True to draw lines between all consecutive points (line plot), False to leave the signal as a scatter. Use signal.point_lines() to toggle a single segment instead.")
par("value", "True to connect all points, False to disconnect them"); spec(type.bool, True)
past_out("signal")

add(signal_class.point_lines, name = "signal.point_lines")
doc("Toggles the connection from the previous point to the one at index, allowing a single segment of the signal to be turned on or off without touching the others. The effective range is 1..N-1; out-of-range indices are silently ignored (index 0 has no predecessor and is therefore always a no-op).")
par("index", "Position of the point whose incoming segment is toggled"); spec(type.int)
par("value", "True to draw the line into this point, False to break the segment"); spec(type.bool, True)
past_out("signal")

add(signal_class.fillx, name = "signal.fillx")
doc("Fills a vertical stem from each point down to the x axis.")
par("active", "Whether to draw the vertical fill lines"); spec(type.bool, True)
past_out("signal")

add(signal_class.filly, name = "signal.filly")
doc("Fills a horizontal stem from each point across to the y axis.")
par("active", "Whether to draw the horizontal fill lines"); spec(type.bool, True)
past_out("signal")

add(signal_class.fill, name = "signal.fill")
doc("Copies fill levels from another signal, useful when building custom stem plots or filled regions.")
par("signal", "Signal to copy the fill information from"); spec(type.signal)
past_out("signal")

add(signal_class.line_method, name = "signal.line_method")
doc("Sets how densely connecting lines are drawn between points. Pass 'simple' for evenly-spaced points along each segment (light, fast, may leave small gaps on steep segments) or 'full' to fill every cell crossed by the line (denser, visually continuous). Applies only when lines have been turned on via signal.lines() or signal.point_lines(). The same setting can also be passed at construction via the line_method parameter on signal().")
par("method", "Line drawing method"); spec(type.line_method, repr("simple"))
past_out("signal")

add(signal_class.fill_method, name = "signal.fill_method")
doc("Sets how densely fills are drawn for points carrying fill data. Pass 'simple' for evenly-spaced points (faster, may leave small gaps on steep stems) or 'full' to fill every cell crossed (denser, visually continuous). The same setting can also be passed at construction via the fill_method parameter on signal().")
par("method", "Fill drawing method"); spec(type.line_method, repr("simple"))
past_out("signal")

add(signal_class.get_length, name = "signal.get_length")
doc("Returns the number of points currently in the signal.")
out("Number of points", type.int)

add(signal_class.copy, name = "signal.copy")
doc("Creates and returns a deep copy of the signal.")
past_out("signal")

add(signal_class.clone, name = "signal.clone")
doc("Replaces this signal's points with those from another signal.")
par("signal", "Signal whose points are copied into this one"); spec(type.signal)
past_out("signal")

add(signal_class.log, name = "signal.log")
doc("Prints a text-based description of the signal and its points, for debugging or inspection. "
    "The output can be long for large signals.")
par("fill", "If True, includes the filled-point information in the output"); spec(type.bool, False)
past_out("signal")
