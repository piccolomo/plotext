# Canvas, sizing and subplots: canvas_pixel, plot_size, subplots/subplot tree, navigation helpers, size policies

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class


add(plot_class.canvas_pixel, name = "canvas_pixel")
doc("Sets the pixel (color and style) of the plot canvas background.")
par("pixel", "Pixel used to paint the canvas"); spec(type.pixel_par, None)
past_out("title")


add(plot_class.theme, name = "theme")
doc("Applies a named colour preset that covers canvas background, frame foreground, ruler foreground/style, and the cycler's pixel sequence in one call. Available names: default, simple, colorless, dusk, sand, wine, garden, dark, dreamland, retro, windows, matrix. Unknown names raise ValueError.")
par("name", "Theme name"); spec(type.string, repr("default"))
past_out("title")


add(plot_class.plot_size, name = "plot_size")
doc("Sets the size (width and height) of this plot, in terminal cells.")
par("width", "Plot width in terminal columns"); spec(type.int, None)
par("height", "Plot height in terminal rows"); spec(type.int, None)
past_out("title")


add(plot_class.subplots, name = "subplots")
doc("Divides this plot into a grid of subplots with the given number of rows and columns.")
par("rows", "Number of subplot rows"); spec(type.int, None)
par("cols", "Number of subplot columns"); spec(type.int, None)
past_out("title")


add(plot_class.subplot, name = "subplot")
doc("Returns the subplot at the given row and column, so it can be addressed directly (for example to draw a signal on it).")
par("row", "Row index of the subplot"); spec(type.int, None)
par("col", "Column index of the subplot"); spec(type.int, None)
out("The subplot at (row, col)", type.plot)


add(plot_class.get_parent, name = "get_parent")
doc("Returns the parent plot at the given nesting level — 0 returns this plot, 1 returns the immediate parent, and so on. Higher levels stop at the master and continue returning it.")
par("level", "Nesting level (0 = self, 1 = immediate parent, ...)"); spec(type.int, 1)
out("The plot at the requested level", type.plot)


add(plot_class.get_master, name = "get_master")
doc("Returns the master plot — the top-level plot that owns this subtree of subplots.")
out("The master plot", type.plot)


add(plot_class.get_terminal, name = "get_terminal")
doc("Returns the terminal object that owns the master plot.")
out("The terminal object", type.terminal)


add(plot_class.get_position, name = "get_position")
doc("Returns this subplot's (row, col) position within its parent grid; (None, None) for the master.")
out("A (row, col) tuple", type.tuple)


add(plot_class.get_log, name = "get_log")
doc("Returns a multi-line string describing this subplot and every nested subplot, indented to reflect the tree.")
out("The log string", type.string)


add(plot_class.size_direction, name = "size_direction")
doc("Controls how subplot widths (and heights) are redistributed within the maximum available canvas size. With +1 the redistribution runs left-to-right across widths and top-to-bottom across heights, and the last subplot (rightmost column or bottom row) absorbs whatever space is left. With -1 the order is reversed, so the first subplot (leftmost column or top row) absorbs the leftover instead.")
par("direction", "+1 runs the redistribution left-to-right (widths) and top-to-bottom (heights); -1 reverses it"); spec(type.direction, 1)
past_out("title")


add(plot_class.size_policy, name = "size_policy")
doc("Controls how nested subplot widths (and heights) are harmonized when they disagree. With 'maximum' each column/row takes the largest requested size across nested subplots, growing the canvas to accommodate; with 'minimum' it takes the smallest, shrinking everyone to fit.")
par("policy", "maximum (columns/rows take the largest nested size) or minimum (they take the smallest)"); spec(type.size_policy, repr("maximum"))
past_out("title")
