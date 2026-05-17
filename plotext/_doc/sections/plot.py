# Plot class user methods: lifecycle (clear, build, show) and timing inspection (time)

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class


add(plot_class.clear, name = "clear")
alias("clf")
doc("Clears all signals, settings and sizes from this plot, resetting it to an empty state. Equivalent to calling clear_data(), clear_settings(), clear_pixels(), clear_styles(), clear_size() and clear_subplots() in turn. On the master plot, clear_size() also resets the terminal's sizing state (prompt height + per-axis limit flags) so no terminal-level state leaks across calls.")
out("This plot", type.plot)

add(plot_class.clear_data, name = "clear_data")
alias("cld")
doc("Drops every signal previously added via draw() and removes the corresponding entries from the legend. Settings, sizes, pixels and styles are preserved.")
past_out("clear")

add(plot_class.clear_settings, name = "clear_settings")
alias("cls")
doc("Resets the plot's settings — title, axis labels, limits, frequencies, manual ticks, scale, alignment, direction, grid, frame status, legend status — back to defaults. Signals, pixels, styles and sizes are preserved.")
past_out("clear")

add(plot_class.clear_pixels, name = "clear_pixels")
alias("clp")
doc("Resets every pixel on this plot — labels, rulers, axes, legend and the canvas itself — to the package defaults, and rewinds the per-signal colour cycler to the start. Signals, settings, styles and sizes are preserved.")
past_out("clear")

add(plot_class.clear_styles, name = "clear_styles")
doc("Resets the line styles of the rulers (grid lines) and axes (frame sides) to the default style. Signals, settings, pixels and sizes are preserved.")
past_out("clear")

add(plot_class.clear_size, name = "clear_size")
alias("clz")
doc("Drops any explicit plot_size() value and resets every subplot's size to None so the next harmonization redistributes proportionally. On the master plot it also resets the terminal's sizing state by calling terminal.clear() — prompt height and per-axis limit flags revert to their defaults, and the master size snaps back to the current terminal dimensions. Signals, subplots, settings, pixels and styles are preserved.")
past_out("clear")

add(plot_class.clear_subplots, name = "clear_subplots")
alias("clss")
doc("Wipes the subplot grid configured via subplots() so the plot becomes a single-panel layout again. Signals, settings, pixels, styles and size are preserved.")
past_out("clear")

add(plot_class.build, name = "build")
doc("Builds the final figure as a matrix, without printing it. Use show() to both build and print.")
out("The final figure matrix", type.matrix)

add(plot_class.show, name = "show")
doc("Builds and prints the final figure to the terminal.")
par("colorless", "If True, render the output without colors"); spec(type.bool, False)
par("flush", "If True, flush the terminal after printing"); spec(type.bool, False)
past_out("clear")


# Inspection

add(plot_class.time, name = "time")
doc("Prints a timing report of the most recent build — total elapsed time and, optionally, the per-step breakdown for each profiled section, recursing into subplots so each one prints its own indented sub-report. Useful when investigating slow renders.")
par("full", "If True (default), include the per-step breakdown and recurse into subplots; if False, print only the master total"); spec(type.bool, True)
out("Total elapsed time of the master plot in milliseconds — handy for assertions or perf gating", type.float)
