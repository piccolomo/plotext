# Ruler and date selections: returned by figure.ruler(axis, side); setters repeat on every selected item and chain, getters read from the first selected item.

from plotext._plotter.utils.selection import selection_class
from plotext._plotter.utils.interactive import reprint_after


# Selection of several rulers: the same setters as a single ruler, repeated on each one
class ruler_selection_class(selection_class):

    # Master plot lookup, required by the reprint_after decorator
    def master(self):
        return self._items[0].master()

    # Set the number of automatically-placed ticks on every selected ruler
    @reprint_after
    def frequency(self, frequency = None):
        self._repeat("frequency", frequency)
        return self

    # Set explicit tick positions and optionally their labels on every selected ruler
    @reprint_after
    def ticks(self, positions = None, labels = None):
        self._repeat("ticks", positions, labels)
        return self

    # Set the visible numerical range on every selected ruler
    @reprint_after
    def lim(self, lower = None, upper = None):
        self._repeat("lim", lower, upper)
        return self

    # Set the scale, linear or log, on every selected ruler
    @reprint_after
    def scale(self, scale = None):
        self._repeat("scale", scale)
        return self

    # Set the direction in which values increase, 1 or -1, on every selected ruler
    @reprint_after
    def direction(self, direction = None):
        self._repeat("direction", direction)
        return self

    # Set the two alignments, lim for the numerical limits and tick for the tick labels, on every selected ruler
    @reprint_after
    def alignment(self, lim = None, tick = None):
        self._repeat("alignment", lim, tick)
        return self

    # Set the pixel used to paint the tick areas of every selected ruler
    @reprint_after
    def pixel(self, pixel = None):
        self._repeat("pixel", pixel)
        return self

    # Control the grid lines of every selected ruler
    @reprint_after
    def grid(self, active = True, style = None, pixel = None):
        self._repeat("grid", active, style, pixel)
        return self

    # Clear settings and pixels of every selected ruler
    @reprint_after
    def clear(self):
        self._repeat("clear")
        return self

    # Print the log of every selected ruler
    def _log(self):
        self._repeat("_log")
        return self

    # Print as the list of the selected rulers, like PlotextRulers(lower x, upper x)
    def __repr__(self):
        names = ", ".join([ruler._name() for ruler in self._items])
        return f"PlotextRulers({names})"


# Selection of several date converters: setters repeat and chain, getters read from the first selected converter
class date_selection_class(selection_class):

    # Bind the selection to its converters and to the names of their rulers, like lower x
    def __init__(self, converters, names):
        selection_class.__init__(self, converters)
        self._names = names

    # Print as the list of the selected rulers, like PlotextDates(lower x, upper x)
    def __repr__(self):
        names = ", ".join(self._names)
        return f"PlotextDates({names})"

    # Activate (or deactivate) date handling on every selected converter, with optional form, origin and zone
    def activate(self, active = True, form = None, origin = None, zone = None):
        self._repeat("activate", active, form, origin, zone)
        return self

    # Reset every selected converter to default settings
    def clear(self):
        self._repeat("clear")
        return self

    # The origin of the first selected converter, in the requested output type
    def origin(self, output = "datetime"):
        return self._items[0].origin(output)

    # Today in the requested form, from the first selected converter
    def today(self, output = "datetime"):
        return self._items[0].today(output)

    # The active state of the first selected converter
    def active(self):
        return self._items[0].active()

    # Convert dates with the first selected converter
    def convert(self, time, output = "timestamp"):
        return self._items[0].convert(time, output)
