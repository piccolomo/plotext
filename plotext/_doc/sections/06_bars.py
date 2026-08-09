# Bar plots section: bar, hist and box signals

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class


section('bar plots')


add(plot_class.bar)
doc("Creates a bar plot signal, optionally grouped or stacked.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("*args", "Bar input data: a single sequence sets the bar heights, with the bar coordinates automatically ranging from 1 onwards; two sequences set the bar coordinates and heights; three sequences set the bar coordinates, baselines and heights (for floating bars). String labels or dates are accepted as bar coordinates. The heights may also be a list of sequences, one per group, for grouped or stacked bars", explanation("data_bar"))
par("marker", "Symbol used to render the bars; its color is taken automatically from the color cycler.\nA list gives one marker per bar, or one per group when the bars are grouped or stacked, and is repeated when shorter", explanation("marker_par"), repr("full"))
par("width", "Bar width as a fraction of the (smallest) spacing between bar coordinates. For grouped bars this value is divided by the number of groups", explanation("float"), 4/5)
par("orientation", "Bar orientation, either vertical (v in short) or horizontal (h in short)", explanation("orientation"), repr("vertical"))
par("lines", "draws the bar outline", explanation("bool"), True)
par("fill", "fills the bar body with markers", explanation("bool"), True)
par("labeled", "text written in the middle of each bar: True writes the bar height, a list writes your own text, one entry per bar. " + explanation("label_colors"), explanation("bar_labeled"), False)
par("stacked", "stacks grouped bars on top of each other, so heights add up cumulatively per coordinate, instead of placing them side by side; only meaningful when the heights are a list of sequences", explanation("bool"), False)
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
out("The bar signal", explanation("signal"))


add(plot_class.hist)
doc("Creates a histogram plot signal.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("data", "The flat numerical sequence to bin", explanation("data_single"))
par("bins", "Number of evenly-spaced buckets", explanation("int"), 10)
par("marker", "Symbol used to render the bars", explanation("marker_par"), repr("full"))
par("width", "Bar width as a fraction of the bin size, 1 makes adjacent bins touch", explanation("float"), 1)
past_par("orientation", "plotext.figure.bar")
par("norm", "divides each bin count by the total number of points so all bins sum to 1 (density form), otherwise bin heights are raw counts", explanation("bool"), False)
past_par("lines", "plotext.figure.bar")
past_par("fill", "plotext.figure.bar")
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
out("The histogram bar signal", explanation("signal"))


add(plot_class.box)
doc("Creates a box plot signal: each category's values are summarized by a rectangle stretching from the 25% value to the 75% value of the sorted data, with a line at the median, and thin lines reaching out to the minimum and maximum.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("*args", "Two sequences: categorical labels (or numeric x positions) and a list of per-category value lists", explanation("data_multiple"))
par("marker", "Symbol used for the box outline / fill; the median and minimum/maximum lines inherit color from this marker", explanation("marker_par"), repr("full"))
par("width", "Box width as a fraction of the smallest spacing between box coordinates", explanation("float"), 4/5)
par("orientation", "Box orientation, either vertical (v in short) or horizontal (h in short)", explanation("orientation"), repr("vertical"))
par("lines", "Draws the box outline", explanation("bool"), True)
par("fill", "Fills the box body with markers", explanation("bool"), True)
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
out("The composed box-plot signal", explanation("signal"))
