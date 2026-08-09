# Clear component: groups the figure clearing methods; calling the component itself clears everything, like all()

from plotext._plotter.utils.propagator import propagator_class
from plotext._plotter.utils.interactive import reprint_after
from plotext._settings import defaults


class clear_class(propagator_class):

    # Repeat a method on the clear component of every direct subplot
    def _counterpart(self, subplot):
        return subplot.clear

    # Clear the size, so that every subplot takes a fresh share at the next plot_size call; on the master, the terminal size is read again, while the terminal own settings, its prompt height and its size limits, are left as they were set.
    @reprint_after
    def size(self):
        self._plot._parts.clear()
        if self._plot._is_master():
            from plotext._kernel.api import terminal
            terminal._update_size()
            self._plot._set_size(*terminal.size())
        else:
            self._plot._set_size()
        self._propagate("size")
        return self

    # Clear subplots tree (rebuilds an empty 0x0 grid; leaves size, position, settings, etc. untouched)
    @reprint_after
    def subplots(self):
        self._plot._set_subplots()
        return self

    # Clear signals, lines and legend data
    @reprint_after
    def data(self):
        self._plot._signals._clear()
        self._plot._rulers.clear_lines()
        self._plot._legend.clear_signals()
        self._plot._cycler.reset()
        self._propagate("data")
        return self

    # Clear all settings
    @reprint_after
    def settings(self):
        self._plot._rulers.clear_settings()
        self._plot._axes.clear_settings()
        self._plot._labels.clear_settings()
        self._plot._legend.clear_settings()
        self._propagate("settings")
        return self

    # Reset all pixels to defaults
    @reprint_after
    def pixels(self):
        self._plot._labels.clear_pixel()
        self._plot._rulers.clear_pixels()
        self._plot._axes.clear_pixels()
        self._plot._legend.clear_pixel()
        self._plot._canvas_pixel.clone(defaults.pixels["canvas"])
        self._plot._cycler.reset()
        self._propagate("pixels")
        return self

    # Clear ruler and axis styles
    @reprint_after
    def styles(self):
        self._plot._rulers.clear_styles()
        self._plot._axes.clear_styles()
        self._propagate("styles")
        return self

    # Clear the whole plot
    @reprint_after
    def all(self):
        self.size()
        self.subplots()
        self.data()
        self.settings()
        self.pixels()
        self.styles()
        return self

    # Calling the component clears everything, then returns the figure for chaining
    def __call__(self):
        self.all()
        return self._plot

    def __repr__(self):
        return "PlotextClear()"
