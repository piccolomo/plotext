# Plot class: main subplot container with signals, axes, legend, rulers, labels and canvas

from plotext._plotter.build import plot_build_class
from plotext._plotter.components.parts import parts_class
from plotext._plotter.components.subplot import subplot_class
from plotext._plotter.components.legend import legend_class
from plotext._plotter.components.timer import timer_class
from plotext._plotter.components.cycler import color_cycler
from plotext._plotter.draw import draw_class

from plotext._plotter.frame.labels import labels_class
from plotext._plotter.frame.ruler.rulers import rulers_class
from plotext._plotter.frame.axis.axes import axes_class

from plotext._signal.signal import signal_class
from plotext._signal.signals import signals_class

from plotext._correct import data as correct_data
from plotext._correct import bool as correct_bool
from plotext._correct import pixel as correct_pixel
from plotext._correct import marker as correct_marker
from plotext._correct import axis as correct_axis

from plotext._settings import defaults
from plotext._settings.constants.numerical import binary

from plotext._methods.matrix import join_matrices
from plotext._primitives.marker import marker as marker_class


# Master plot class: composes subplot, draw and build behavior
class plot_class(subplot_class, draw_class, plot_build_class):

    # Initialize all plot components
    def __init__(self, parent):
        self._parts = parts_class()
        self._labels = labels_class()
        self._rulers = rulers_class()
        self._axes = axes_class()
        self._signals = signals_class()
        self._legend = legend_class()
        self._timer = timer_class()
        self._cycler = color_cycler(defaults.color_sequence)

        subplot_class.__init__(self, parent)
        draw_class.__init__(self)
        plot_build_class.__init__(self)

        self.canvas_pixel()

    # Apply method to each subplot when subplots exist
    def _for_each_subplot(self, method_name, *args, **kwargs):
        if self._has_subplots():
            for pos in self._get_slots_range():
                getattr(self._get_subplot(*pos), method_name)(*args, **kwargs)

    # Create grid of subplots and clone settings into each
    def subplots(self, rows = None, cols = None):
        subplot_class._subplots(self, rows, cols)
        self._for_each_subplot("_clone", self)
        return self

    # Clear size and parts
    def clear_size(self):
        self._parts.clear()
        subplot_class._clear(self)
        self._set_size(*self.get_terminal().get_size(update = True)) if self._is_master() else None
        self._for_each_subplot("clear_size")
        return self

    # Clear signals and legend data
    def clear_data(self):
        self._signals._clear()
        self._legend.clear_signals()
        self._for_each_subplot("clear_data")
        return self

    # Clear all settings
    def clear_settings(self):
        self._rulers.clear_settings()
        self._axes.clear_settings()
        self._labels.clear_settings()
        self._legend.clear_settings()
        self._for_each_subplot("clear_settings")
        return self

    # Reset all pixels to defaults
    def clear_pixels(self):
        self._labels.clear_pixel()
        self._rulers.clear_pixels()
        self._axes.clear_pixels()
        self._legend.clear_pixel()
        self._canvas_pixel.clone(defaults.pixels["canvas"])
        self._cycler.reset()
        self._for_each_subplot("clear_pixels")
        return self

    # Clear ruler and axis styles
    def clear_styles(self):
        self._rulers.clear_styles()
        self._axes.clear_styles()
        self._for_each_subplot("clear_styles")
        return self

    # Clear the whole plot
    def clear(self):
        self.clear_size()
        self.clear_data()
        self.clear_settings()
        self.clear_pixels()
        self.clear_styles()
        return self

    clf = clear

    # Clone state from another plot
    def _clone(self, plot):
        self._labels.clone(plot._labels)
        self._rulers._clone(plot._rulers)
        self._axes.clone(plot._axes)
        self._signals._clone(plot._signals)
        self._legend.clone(plot._legend)
        return self

    # Set size and propagate to parts
    def _set_size(self, width = None, height = None):
        subplot_class._set_size(self, width, height)
        self._parts.set_size(*self.get_size())
        return self

    # Produce next marker with next color from cycler
    def next_marker(self):
        return marker_class(defaults.marker, self._cycler.next_color())

    # Build a signal from raw args; lines / fillx / filly / label are set on
    # the returned signal via its public fluent methods (see signal_class)
    def signal(self, *args, marker = None, xside = None, yside = None):
        x, y = correct_data.data(*args)
        xside = correct_axis.side(0, xside)   # "lower"/0/False/None -> 0, "upper"/1/True -> 1
        yside = correct_axis.side(1, yside)   # "left"/0/False/None  -> 0, "right"/1/True -> 1

        m = correct_marker.markers(marker, self.next_marker(), len(x))

        x = self.convert(x, "timestamp") if self._is_date_active(0, xside) else x
        y = self.convert(y, "timestamp") if self._is_date_active(1, yside) else y

        signal = signal_class(len(x))
        signal._append_points(x, y, m)
        signal._set_xside(xside)._set_yside(yside)
        return signal

    # Set plot title
    def title(self, label = None):
        self._labels.set_title(label)
        self._for_each_subplot("title", label)
        return self

    # Set axis label
    def label(self, label = None, axis = None, side = None):
        self._labels.set(label, axis, side)
        self._for_each_subplot("label", label, axis, side)
        return self

    # Configure the plot legend: visibility, position, alignment, colour, axis anchoring
    def legend(self, status = None, x = None, y = None, ha = None, va = None, relative = None, pixel = None, xside = None, yside = None):
        self._legend.set(status = status, x = x, y = y, relative = relative,
                         ha = ha, va = va, pixel = pixel,
                         xside = xside, yside = yside)
        self._for_each_subplot("legend", status, x, y, ha, va, relative, pixel, xside, yside)
        return self

    # Set ruler alignment
    def alignment(self, alignment = None, axis = None, side = None):
        self._rulers.set_alignment(alignment, axis = axis, side = side)
        self._for_each_subplot("alignment", alignment, axis, side)
        return self

    # Set ruler direction
    def direction(self, direction = None, axis = None, side = None):
        self._rulers.set_direction(direction, axis, side)
        self._for_each_subplot("direction", direction, axis, side)
        return self

    # Set ruler scale
    def scale(self, scale = None, axis = None, side = None):
        self._rulers.set_scale(scale, axis, side)
        self._for_each_subplot("scale", scale, axis, side)
        return self

    # Set ruler limits
    def lim(self, lower = None, upper = None, axis = None, side = None):
        self._rulers.set_limits(lower, upper, axis, side)
        self._for_each_subplot("lim", lower, upper, axis, side)
        return self

    # Set ruler frequency
    def frequency(self, frequency = None, axis = None, side = None):
        self._rulers.set_frequency(frequency = frequency, axis = axis, side = side)
        self._for_each_subplot("frequency", frequency, axis, side)
        return self

    # Set ruler ticks
    def ticks(self, positions = None, labels = None, axis = 0, side = 0):
        self._rulers.set_ticks(positions = positions, labels = labels, axis = axis, side = side)
        self._for_each_subplot("ticks", positions, labels, axis, side)
        return self

    # Set grid
    def grid(self, active = None, style = None, pixel = None, axis = binary, side = binary):
        self._rulers.set_grid(active, style, pixel, axis, side)
        self._for_each_subplot("grid", active, style, pixel, axis, side)
        return self

    # Configure date axis
    def date(self, active = True, form = None, origin = None, axis = None, side = None):
        self._rulers.set_date(active, form, origin, axis, side)
        self._for_each_subplot("date", active, form, origin, axis, side)
        return self

    # Convert time value on axis
    def convert(self, time, output = "timestamp", axis = None, side = None):
        return self._rulers.convert(time, output, axis, side)

    # Check if date mode is active
    def _is_date_active(self, axis = None, side = None):
        return self._rulers.get(axis, side)._date.is_active()

    # Set axis properties
    def axis(self, status = None, style = None, pixel = None, axis = 0, side = 0):
        self._axes.set(axis = axis, side = side, status = status, style = style, pixel = pixel)
        self._for_each_subplot("axis", status, style, pixel, axis, side)
        return self

    # Set frame (all axes)
    def frame(self, status = True, style = None, pixel = None):
        self.axis(status = status, style = style, pixel = pixel, axis = binary, side = binary)
        return self

    # Set canvas pixel
    def canvas_pixel(self, pixel = None):
        self._canvas_pixel = correct_pixel.pixel(pixel, defaults.pixels["canvas"])
        self._for_each_subplot("canvas_pixel", pixel)
        return self

    # Start a timed event
    def _start_event(self, event):
        self._timer.start(event)
        return self

    # Stop a timed event
    def _stop_event(self, event):
        self._timer.stop(event)
        return self

    # Log timings
    def time(self, full = True):
        self._timer.log(full)
        return self

    # Build and print the plot
    def show(self, colorless = False, flush = False):
        out = self.build()
        self._start_event("print")
        out.print(colorless = colorless, flush = flush)
        self._stop_event("print")
        return out

    # Build the plot matrix
    def build(self):
        self._timer.clear()

        if self._no_subplots():
            return self._get_plot_matrix()

        self._start_event("create matrices")
        matrices = [[self._get_subplot(r, c)._get_plot_matrix() for c in self._get_cols_range()] for r in self._get_rows_range()]
        self._stop_event("create matrices")

        self._start_event("join matrices")
        out = join_matrices(matrices)
        self._stop_event("join matrices")

        return out