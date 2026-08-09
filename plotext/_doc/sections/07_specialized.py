# Specialized plots section: candlestick, error, event, heatmap and cmatrix signals

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class
from plotext._signal.point_filled import point


section('specialized plots')


add(plot_class.candlestick)
doc("Creates a candlestick plot signal. Each candle summarizes prices over one time interval using a rectangle from the opening to the closing price, and a thin vertical line spanning from the lowest to the highest price; the candle is green when the price rose and red when it fell.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("data", "A dictionary containing date, open, close, high, low keys and values; dates are interpreted automatically once plotext.date() has been called on the relevant axis", explanation("ohlc_dict"))
par("style", "Candle drawing style. With candle (default), a thick body is drawn from the opening to the closing price. With ohlc, the body is replaced by two short horizontal lines: one to the left of the vertical line at the opening price, one to the right at the closing price; lighter, useful when many candles are packed together", explanation("string"), repr("candle"))
par("tick", "Length, in character cells, of the ohlc style's short horizontal lines; ignored for candle style", explanation("int"), 2)
par("orientation", "Candlestick orientation, either vertical (or v) or horizontal (or h)", explanation("orientation"), repr("vertical"))
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
out("The candlestick signal", explanation("signal"))


add(plot_class.error)
doc("Creates an error bar plot: each point is drawn with a vertical and a horizontal line centered on it, whose lengths are the given vertical and horizontal errors, showing the uncertainty around the point. Dates are not accepted at this stage.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("*args", "Error input data, given as positional sequences. One sequence sets the vertical coordinates of the points, with the horizontal ones automatically ranging from 1 onwards; two sequences set the horizontal and vertical coordinates, with no errors; three sequences add the vertical errors; four sequences add the vertical and horizontal errors, in this order. Each error can be given as a single number, applied to every point, or as a sequence with one value per point.", explanation("data_error"))
par("pixel", "Pixel used for every stroke of the error bars; if None, a fresh color is taken from the cycler", explanation("pixel_par"), None)
par("style", "Line drawing style applied to the bars. " + explanation("line_styles"), explanation("line_style"), repr('default'))
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
out("The composed error-bar signal", explanation("signal"))


add(plot_class.event)
doc("Draws a line spanning the whole canvas at every event coordinate, vertical or horizontal depending on orientation. The lines are added directly to the plot's draw sequence.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("data", "Sequence of event coordinates along the chosen orientation", explanation("data_single"))
par("orientation", "Line orientation, either vertical (or v) or horizontal (or h)", explanation("orientation"), repr("vertical"))
par("pixel", "Pixel used for every line; if None, a fresh color is taken from the color cycler", explanation("pixel_par"), None)
par("style", "Line drawing style. " + explanation("line_styles"), explanation("line_style"), repr('default'))
par("side", "Axis side the events are anchored to (x axis side if vertical, y axis side if horizontal)", explanation("side"), 0)
par("label", "Legend label for the event series (only the first line carries the label so the legend stays a single entry)", explanation("label"), None)
past_out("plotext.figure.draw")


add(plot_class.heatmap)
doc("Creates a heatmap plot signal: a 2D data grid drawn as colored cells.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("data", "A 2D sequence; either numeric values (colormap applied) or (r, g, b) integer triples (used as cell color directly)", explanation("data_2d"))
par("map", "Color scale used to turn numeric values into cell colors; ignored when the input is already RGB", explanation("colormap"), repr("gray"))
par("fill", "stretches each cell into a rectangle, otherwise each cell is a single character", explanation("bool"), False)
par("symbol", "Symbol used to render every cell; high resolution codes are accepted but not recommended", explanation("cell_symbol"), repr('█'))
past_par("xside", "plotext.figure.signal")
past_par("yside", "plotext.figure.signal")
out("The composed heatmap signal", explanation("signal"))


add(plot_class.cmatrix)
doc("Creates a confusion matrix signal, comparing predicted labels against true ones: each cell counts how many samples with a given true label received a given predicted label, and is drawn as a filled rectangle whose color scales with the count, with the count itself as a centered label.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("actual",    "The list of true labels", explanation("data_single"))
par("predicted", "The list of predicted labels, same length as actual", explanation("data_single"))
par("labels",    "The labels to show on the matrix, in the given row/column order; pairs with labels outside this list are ignored. If None, every distinct label found in actual or predicted is used, in sorted order", explanation("data_single"), None)
par("norm",      "cell labels show percentages relative to their row total instead of raw counts; cell colors always use raw counts", explanation("bool"), False)
par("map",       "Color scale used to turn the counts into cell colors", explanation("colormap"), repr("gray"))
out("The composite confusion-matrix signal", explanation("signal"))
