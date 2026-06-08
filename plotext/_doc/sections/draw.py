# Drawing methods: signal generators (sin/square), direct media (image/gif/video — video handles local files, URLs and YouTube URLs natively), the sleep streaming helper, and plot-level draw helpers (draw, candlestick, error, event, rectangle, polygon, segment, bar family, hist, box, heatmap, fig.image, text, effect)

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class
from plotext import sin, square, noise, image, gif, video, effect, sleep

section('drawing')


add(sin)
doc("Generates a sinusoidal signal for testing plotting routines.")
par("periods", "Number of complete sinusoidal cycles"); spec(type.float, 2)
par("length", "Total number of sample points"); spec(type.int, 200)
par("amplitude", "Half the peak-to-peak value of the sine wave"); spec(type.float, 1)
par("phase", "Phase shift in units of π"); spec(type.float, 0)
par("decay", "Exponential decay factor applied to the signal"); spec(type.float, 0)
par("offset", "Additional vertical offset"); spec(type.float, 0)
out("List of floats representing the generated signal", type.floats)


add(square)
doc("Generates a square-wave signal alternating between +amplitude and -amplitude — a discrete companion to sin() for testing plotting routines.")
par("periods", "Number of complete square-wave cycles"); spec(type.float, 2)
par("length", "Total number of sample points"); spec(type.int, 200)
par("amplitude", "Half the peak-to-peak value of the square wave"); spec(type.float, 1)
out("List of floats representing the generated signal", type.floats)


add(noise)
doc("Generates Gaussian noise samples (mean offset, standard deviation amplitude). Useful for histogram demos and stress-testing plot rendering. Pass seed=None (default) for fresh random output each call, or an integer for reproducibility.")
par("length", "Total number of sample points"); spec(type.int, 200)
par("amplitude", "Standard deviation of the Gaussian distribution"); spec(type.float, 1)
par("offset", "Mean of the Gaussian distribution (shifts every sample by this amount)"); spec(type.float, 0)
par("seed", "Integer seed for reproducible output; None (default) draws fresh values each call"); spec(type.int, None)
out("List of floats representing the noise samples", type.floats)


add(image)
doc("Open an image file (local path, '~/…', or http/https URL — URLs are downloaded once into a temp folder and cached for subsequent calls) via Pillow and paint it into a plotext.matrix. Direct rendering — no figure pipeline; call .print() on the returned matrix. Roughly 5-10x faster than fig.image because there are no axes, ticks, or signal harmonization.")
par("path", "Local filesystem path, '~/…', or http/https URL of the image (any format Pillow can read)"); spec(type.string)
par("gray", "If True, convert the image to grayscale before rendering"); spec(type.bool, False)
par("ratio", "If True (default), preserve the source aspect ratio (with cell-aspect compensation); if False, stretch to exactly (width, height)"); spec(type.bool, True)
par("width", "Target width in canvas chars. None falls back to the terminal width; otherwise clamped to the terminal width when plt.terminal.limit's width flag is on, or passed through when the limit has been disabled"); spec(type.int, None)
par("height", "Target height in canvas chars. None falls back to the terminal height; otherwise clamped to the terminal height when plt.terminal.limit's height flag is on, or passed through when the limit has been disabled"); spec(type.int, None)
out("A painted plotext.matrix ready to print", type.matrix)


add(gif)
doc("Animate a GIF in the terminal: decodes each frame on the fly (no upfront pre-decode wait), paints, prints, and sleeps only the remainder of the GIF's per-frame duration so playback runs at the GIF's natural speed and degrades gracefully when paint is slow. Adapts to terminal resize automatically. A 'press q to exit' hint (q in bold red, on a discrete black label) is stamped onto the bottom-left of each frame, overwriting those cells in place so the frame keeps its size; pressing q exits. Side-effect-only — no return value. The source may be a local filesystem path, a '~/…' user-home path, or an http/https URL; URLs are downloaded once into the per-user temp folder (<tempfile.gettempdir()>/plotext/) and reused on subsequent calls.")
par("path", "Local filesystem path, '~/…' user-home path, or http/https URL of the GIF"); spec(type.string)
par("gray", "If True, convert each frame to grayscale before rendering"); spec(type.bool, False)
par("ratio", "If True (default), preserve the source aspect ratio (with cell-aspect compensation); if False, stretch each frame to exactly (width, height)"); spec(type.bool, True)
par("loop", "If True (default), replay forever until q is pressed; if False, play once and return"); spec(type.bool, True)
par("width", "Target width in canvas chars. None falls back to the terminal width; otherwise clamped to the terminal width when plt.terminal.limit's width flag is on, or passed through when the limit has been disabled"); spec(type.int, None)
par("height", "Target height in canvas chars. None falls back to the terminal height; otherwise clamped to the terminal height when plt.terminal.limit's height flag is on, or passed through when the limit has been disabled"); spec(type.int, None)


add(video)
doc("Play a video in the terminal with synchronised audio and video. A single ffpyplayer.MediaPlayer owns both streams — pushing audio on its own thread and yielding video frames paired with the seconds-to-sleep value that keeps the visible frames locked to the audio clock. A 'press q to exit' hint (q in bold red, on a discrete black label) is stamped onto the bottom-left of each frame, overwriting those cells in place so the frame keeps its size; pressing q exits. Side-effect-only — no return value. The source may be a local file, '~/…', a direct http/https media URL, or a YouTube URL: direct URLs are downloaded once into a temp folder (<tempfile.gettempdir()>/plotext/) and reused on subsequent calls; YouTube URLs (host matches youtube.com / youtu.be) are routed through yt-dlp internally to obtain a time-limited stream URL and played directly without caching.")
par("path", "Local filesystem path, '~/…', http/https media URL, or YouTube URL"); spec(type.string)
par("gray", "If True, convert each frame to grayscale before rendering"); spec(type.bool, False)
par("ratio", "If True (default), preserve the source aspect ratio (with cell-aspect compensation); if False, stretch each frame to exactly (width, height)"); spec(type.bool, True)
par("loop", "If True, replay forever until q is pressed; if False (default), play once and return"); spec(type.bool, False)
par("width", "Target width in canvas chars. None falls back to the terminal width; otherwise clamped per terminal.limit's width flag"); spec(type.int, None)
par("height", "Target height in canvas chars. None falls back to the terminal height; otherwise clamped per terminal.limit's height flag"); spec(type.int, None)


add(plot_class.draw, name = "draw")
doc("Adds a drawable to the plot queue. Accepts either a signal (from signal(), candlestick(), rectangle(), polygon(), bar()) or a text annotation (from text()). All queued drawables are rendered when plotext.show() or plotext.build() is called.")
par("drawable", "The signal or text to be added to the plot queue"); spec(type.signal + " or " + type.text)
out("This plot", type.plot)


add(plot_class.candlestick, name = "candlestick")
doc("Creates a candlestick signal from OHLC market data. The returned signal must be passed to draw().")
par("data", "A dictionary containing date, open, close, high, low values for each candle; dates are interpreted automatically once plotext.date() has been called on the relevant axis"); spec(type.ohlc_dict)
par("style", "Candle body style: 'candle' (default) draws a filled body between open and close; 'ohlc' replaces the body with two short ticks (open extending left of the wick, close extending right) — flatter, preferred for dense bars"); spec(type.string, repr("candle"))
par("tick", "OHLC tick half-width — number of dash cells flanking the wick on each side; ignored for 'candle' style"); spec(type.int, 2)
par("orientation", "Candlestick orientation, either vertical (or v) or horizontal (or h)"); spec(type.orientation, repr("vertical"))
past("xside", "signal")
past("yside", "signal")
out("The candlestick signal", type.signal)


add(plot_class.error, name = "error")
doc("Creates an error-bar plot: a scatter point at each (x, y), with a vertical bar of total length yerr[i] (centred on y[i]) and a horizontal bar of total length xerr[i] (centred on x[i]). The bars are drawn as box-line glyphs so the vertical and horizontal arms auto-merge into ┼ at the centre point. The returned signal must be passed to draw().")
par("args", "Error input data, given as positional sequences. One sequence sets the y values (x defaults to 1..N), two set x and y with no errors, three set x, y and y errors, four set x, y, y errors and x errors (yerr first mirrors matplotlib.errorbar's positional convention). Each error sequence may be a scalar (broadcast to every point) or a list."); spec(type.data_multiple)
par("pixel", "Pixel (colour and style) used for every stroke of the error bars; if None, a fresh colour is taken from the cycler"); spec(type.pixel_par, None)
par("style", "Line drawing style applied to the bars. " + type.line_styles); spec(type.style, repr('default'))
past("xside", "signal")
past("yside", "signal")
par("label", "Legend label for the error series"); spec(type.label, None)
out("The composed error-bar signal", type.signal)


add(plot_class.event, name = "event")
doc("Draws a stem at every event coordinate. Each stem is a ruler-registered line (│ vertical, ─ horizontal) that spans the full canvas and merges with the axes (┼ / ┴ / ┬ on the axis cells). The perpendicular axis is squashed to [0, 1] with no ticks since it carries no data. Side-effect: this method mutates the figure's lim and frequency on the perpendicular axis.")
par("data", "Sequence of event coordinates along the chosen orientation"); spec(type.data_single)
par("orientation", "Stem orientation, either vertical (or v) or horizontal (or h)"); spec(type.orientation, repr("vertical"))
par("pixel", "Pixel (colour and style) used for every stem; if None, a fresh colour is taken from the cycler"); spec(type.pixel_par, None)
par("style", "Line drawing style applied to the stems. " + type.line_styles); spec(type.style, repr('default'))
par("side", "Axis side the events are anchored to (xside if vertical, yside if horizontal)"); spec(type.side, 0)
par("label", "Legend label for the event series (only the first stem carries the label so the legend stays a single entry)"); spec(type.label, None)
past_out("draw")


add(plot_class.rectangle, name = "rectangle")
doc("Creates a rectangle signal between the given x and y ranges. The returned signal must be passed to draw().")
par("x", "The x range of the rectangle"); spec(type.couple, repr((0, 1)))
par("y", "The y range of the rectangle"); spec(type.couple, repr((0, 1)))
par("marker", "Symbol used to render the rectangle"); spec(type.marker_par, repr("hd"))
par("lines", "If True the rectangle's outline is drawn (and densified for body filling when fill is also True); if False only the corner pairs are placed"); spec(type.bool, True)
par("fill", "If True the rectangle's body is filled with markers; if False only the clockwise outline is drawn"); spec(type.bool, True)
par("label", "Optional text drawn centered inside the rectangle. Colours auto-derive from the rectangle marker: filled → label fg = canvas bg, label bg = rect fg; outlined → label fg = rect fg. Accepts a plain string, a plotext.colorize, or a plotext.matrix for full pixel control"); spec(type.label, None)
past("xside", "signal")
past("yside", "signal")
out("The rectangle signal", type.signal)


add(plot_class.polygon, name = "polygon")
doc("Creates a regular polygon signal centered at the given coordinates. The returned signal must be passed to draw().")
par("x", "The polygon center x coordinate"); spec(type.float, 0)
par("y", "The polygon center y coordinate"); spec(type.float, 0)
par("radius", "Distance from the center to each vertex; for a circle it is the actual radius"); spec(type.float, 1)
par("sides", "Number of polygon sides; values above ~50 approximate a circle"); spec(type.int, 3)
par("up", "If True, rotates the polygon by half a side angle (a flat edge faces up for even sides; a vertex faces up for odd sides)"); spec(type.bool, False)
par("marker", "Symbol used to render the polygon vertices"); spec(type.marker_par, repr("hd"))
par("lines", "If True, the polygon outline is drawn between consecutive vertices; if False only the vertex points are placed"); spec(type.bool, True)
par("fill", "If True, every vertex gets a fill point at (x, y) — the polygon center, producing radial spokes from each vertex inward"); spec(type.bool, False)
past("xside", "signal")
past("yside", "signal")
out("The polygon signal", type.signal)


add(plot_class.segment, name = "segment")
doc("Creates a straight line segment between two endpoints. The returned signal must be passed to draw().")
par("x", "The x range of the segment, as a two-value tuple or list — first endpoint, then second"); spec(type.couple, repr((0, 1)))
par("y", "The y range of the segment, same format as x"); spec(type.couple, repr((0, 1)))
par("marker", "Symbol used to render the segment"); spec(type.marker_par, repr("hd"))
past("xside", "signal")
past("yside", "signal")
out("The segment signal", type.signal)


add(plot_class.bar, name = "bar")
doc("Creates a bar plot signal. The returned signal must be passed to draw().")
par("args", "Bar input data: a single sequence sets the bar heights and uses 1..N as coordinates; two sequences set the bar coordinates and heights with the baseline at zero; three sequences set the bar coordinates, baselines and heights (floating bars)"); spec(type.data_bar)
par("marker", "Symbol used to render the bars"); spec(type.marker_par, repr("hd"))
par("width", "Bar width as a fraction of the inter-bar spacing"); spec(type.float, 4/5)
par("orientation", "Bar orientation, either vertical (or v) or horizontal (or h)"); spec(type.orientation, repr("vertical"))
par("lines", "If True, draws the bar outline"); spec(type.bool, True)
par("fill", "If True, fills the bar body"); spec(type.bool, True)
par("labelled", "If True, each bar carries its height value (y_max) as a centered label inside the rectangle (see rectangle's label parameter for colour rules)"); spec(type.bool, False)
past("xside", "signal")
past("yside", "signal")
out("The bar signal", type.signal)


add(plot_class.multiple_bar, name = "multiple_bar")
doc("Creates a grouped bar plot where multiple bars are placed side-by-side (along the bar width axis) at the same coordinate. The returned signal must be passed to draw().")
par("args", "The coordinates x and Y (or just Y), of the bars, where Y is a list of lists, each containing the bar heights of the corresponding bar plot; string labels or dates are accepted (but only as x values)"); spec(type.data_multiple_bar)
par("marker", "Symbol used to render the bars; a list of markers (with same length as Y) can also be provided to separately set the marker of each group"); spec(type.marker_par)
par("width", "Outer width of each group as a fraction of the inter-group spacing; per-bar width is this divided by the number of groups"); spec(type.float, 4/5)
past("orientation", "bar")
past("lines", "bar")
past("fill", "bar")
past("labelled", "bar")
past("xside", "signal")
past("yside", "signal")
out("The composed bar signal", type.signal)


add(plot_class.stacked_bar, name = "stacked_bar")
doc("Creates a stacked bar plot where multiple bars are placed on top of each other (along the bar height axis) at the same coordinate. Each group's bar starts where the previous group's bar ended, so heights add up cumulatively per coordinate. The returned signal must be passed to draw().")
past("args", "multiple_bar")
past("marker", "multiple_bar")
par("width", "Bar width as a fraction of the inter-bar spacing"); spec(type.float, 4/5)
past("orientation", "bar")
past("lines", "bar")
past("fill", "bar")
past("labelled", "bar")
past("xside", "signal")
past("yside", "signal")
out("The composed bar signal", type.signal)


add(plot_class.box, name = "box")
doc("Creates a box-and-whisker plot per category: plotext computes the quartiles for each category and renders a Q1..Q3 rectangle, a median line across it, and whiskers extending from the box edges to min and max. The median is drawn as a perpendicular box-line whose colours are derived automatically — its foreground is set to the canvas pixel's background and its background to the box marker's foreground, so the median appears as a contrasting strip cut through the box (and adapts if the canvas pixel is overridden). The returned signal must be passed to draw().")
par("args", "Two sequences: categorical labels (or numeric x positions) and a list of per-category value lists"); spec(type.data_multiple)
par("marker", "Symbol used for the box outline / fill (the median line and whiskers inherit colour from this marker)"); spec(type.marker_par, repr("hd"))
par("width", "Box width as a fraction of the inter-bar spacing"); spec(type.float, 4/5)
past("orientation", "bar")
past("lines", "bar")
past("fill", "bar")
past("xside", "signal")
past("yside", "signal")
out("The composed box-plot signal", type.signal)


add(plot_class.hist, name = "hist")
doc("Creates a histogram from a flat data sequence: counts how many values fall into each of bins evenly-spaced buckets between the data minimum and maximum, then renders the result as a bar plot. The returned signal must be passed to draw().")
par("data", "The flat numerical sequence to bin"); spec(type.data_single)
par("bins", "Number of evenly-spaced buckets between min(data) and max(data)"); spec(type.int, 10)
par("marker", "Symbol used to render the bars"); spec(type.marker_par, repr("hd"))
par("width", "Bar width as a fraction of the inter-bar spacing"); spec(type.float, 4/5)
past("orientation", "bar")
par("norm", "If True, divide each bin count by the total number of points so all bins sum to 1 (density form); if False (default), bin heights are raw counts"); spec(type.bool, False)
past("lines", "bar")
past("fill", "bar")
past("xside", "signal")
past("yside", "signal")
out("The histogram bar signal", type.signal)


add(plot_class.confusion_matrix, name = "confusion_matrix")
doc("Builds a confusion matrix from tabulated (actual, predicted) counts: each cell is a gradient-coloured filled rectangle carrying its count (or row-normalized percentage) as a centered label. Returns a composite signal — pass it to draw(). Caller is responsible for ticks, axis labels and title.")
par("actual",    "Per-sample true labels"); spec(type.data_single)
par("predicted", "Per-sample predicted labels (same length as actual)"); spec(type.data_single)
par("labels",    "Optional explicit label order; if None, labels are inferred and sorted from actual ∪ predicted"); spec(type.data_single, None)
par("norm",      "If True, cell labels show row-normalized percentages (count / row_total · 100); if False (default), labels show raw counts. Cell colours always use raw counts so the gradient stays meaningful"); spec(type.bool, False)
par("map",       "Colormap name applied to the count grid"); spec(type.colormap, repr("gray"))
out("The composite confusion-matrix signal", type.signal)


add(plot_class.heatmap, name = "heatmap")
doc("Renders a 2D matrix as a coloured grid. Numeric input is normalized to the chosen colormap; RGB-tuple input passes through untouched. Row 0 of the matrix is drawn at the top of the canvas. The returned signal must be passed to draw().")
par("data", "A 2D sequence; either numeric values (colormap applied) or (r, g, b) integer triples (used as cell colour directly). Ragged input is truncated to the shortest row."); spec(type.data_2d)
par("map", "Colormap name applied to numeric input. Ignored when input is already RGB."); spec(type.colormap, repr("gray"))
par("fill", "If False (default), one symbol per cell — caller sizes the plot via plot_size so the canvas matches cols/rows or cells will be sparse. If True, each row is densified into a filled band that auto-scales to whatever canvas size is currently set (no plot_size hand-tuning needed)."); spec(type.bool, False)
par("symbol", "Symbol used to render every cell"); spec(type.symbol, repr('█'))
past("xside", "signal")
past("yside", "signal")
out("The composed heatmap signal", type.signal)


add(plot_class.image, name = "figure.image")
doc("Plot-integrated image renderer: opens the file via Pillow, optionally converts it to grayscale, resamples it to the current plot_size (or the terminal size when no plot_size has been set), and returns a heatmap signal mapping each pixel 1:1 to a canvas char rendered with the given symbol. Caller is responsible for plot_size, frame and tick frequency settings. The returned signal must be passed to draw(). Slower than the module-level plotext.image() but supports plot integration (axes, ticks, overlay with other signals).")
par("path", "Filesystem path to the image (any format supported by Pillow)"); spec(type.string)
par("gray", "If True, convert the image to grayscale before rendering"); spec(type.bool, False)
par("symbol", "Symbol used to render every pixel"); spec(type.symbol, repr('█'))
out("The composed image signal", type.signal)


add(plot_class.text, name = "text")
doc("Creates a text annotation at the given x and y coordinates. The returned text must be passed to draw() to register it on the plot.")
par("x", "X coordinate of the text anchor"); spec(type.value)
par("y", "Y coordinate of the text anchor"); spec(type.value)
par("label", "Text content: a plain string or a plotext.colorize for explicit styling"); spec(type.label)
par("alignment", "Alignment along the writing direction"); spec(type.alignment_text, repr("left"))
par("orientation", "Text orientation, horizontal or vertical"); spec(type.orientation, repr("horizontal"))
past("xside", "signal")
past("yside", "signal")
par("relative", "If True, x and y are absolute canvas-cell coordinates instead of data coordinates"); spec(type.bool, False)
out("The text object", type.text)


add(effect)
doc("Returns a single-row matrix where each character of `text` is colored by a phase-driven effect. Advancing `step` between calls animates the result; pass the matrix to fig.title() or fig.label() inside a streaming loop for live styling.")
par("text", "The string to style"); spec(type.string)
par("name", "Effect name: one of 'shimmer', 'pulse', 'rainbow', 'gradient'"); spec(type.string, "shimmer")
par("step", "Animation phase; advance between frames to animate"); spec(type.float, 0.0)
out("Styled 1-row matrix", type.matrix)


add(sleep)
doc("Pauses execution for the given number of seconds — useful between frames when streaming a continuous flow of data, to reduce screen flickering. Tweak the value manually to balance smoothness against responsiveness.")
par("seconds", "Seconds to pause; may be fractional"); spec(type.float, 0)
out("The seconds slept", type.float)
