# Plot class: main subplot container with signals, axes, legend, rulers, labels and canvas

from plotext._plotter.build import plot_build_class
from plotext._plotter.utils.parts import parts_class
from plotext._plotter.subplot import subplot_class
from plotext._plotter.canvas.legend import legend_class
from plotext._plotter.utils.timer import timer_class
from plotext._plotter.utils.cycler import color_cycler
from plotext._plotter.canvas.texts import texts_class
from plotext._plotter.draw import draw_class

from plotext._plotter.frame.labels import labels_class
from plotext._plotter.frame.rulers import rulers_class
from plotext._plotter.frame.axes import axes_class

from plotext._signal.signal import signal_class
from plotext._signal.signals import signals_class

from plotext._correct import data as correct_data
from plotext._correct import bool as correct_bool
from plotext._correct import pixel as correct_pixel
from plotext._correct import marker as correct_marker
from plotext._correct import axis as correct_axis
from plotext._correct import placement as correct_placement

from plotext._settings import defaults
from plotext._constants.numerical import binary

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
        self._texts = texts_class()
        self._legend = legend_class()
        self._timer = timer_class()
        self._cycler = color_cycler(defaults.color_sequence)

        subplot_class.__init__(self, parent)
        draw_class.__init__(self)
        plot_build_class.__init__(self)

        self.canvas_pixel()

    # Create grid of subplots and clone settings into each
    def subplots(self, rows = None, cols = None):
        subplot_class._subplots(self, rows, cols)
        self._for_each_subplot("_clone", self)
        return self

    # Clear size and parts; reset subplot sizes to None so harmonization can redistribute them on the next plot_size call. On the master also reset the terminal's sizing state (prompt height + per-axis limit flags) since those are size-domain settings.
    def clear_size(self):
        self._parts.clear()
        if self._is_master():
            self.get_terminal().clear()
            self._set_size(*self.get_terminal().get_size())
        else:
            self._set_size()
        self._for_each_subplot("clear_size")
        return self

    clz = clear_size

    # Clear subplots tree (rebuilds an empty 0×0 grid; leaves size, position, settings, etc. untouched)
    def clear_subplots(self):
        self._subplots()
        return self

    clss = clear_subplots

    # Clear signals, texts, lines and legend data
    def clear_data(self):
        self._signals._clear()
        self._texts.clear()
        self._rulers.clear_lines()
        self._legend.clear_signals()
        self._cycler.reset()
        self._for_each_subplot("clear_data")
        return self

    cld = clear_data

    # Clear all settings
    def clear_settings(self):
        self._rulers.clear_settings()
        self._axes.clear_settings()
        self._labels.clear_settings()
        self._legend.clear_settings()
        self._for_each_subplot("clear_settings")
        return self

    cls = clear_settings

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

    clp = clear_pixels

    # Clear ruler and axis styles
    def clear_styles(self):
        self._rulers.clear_styles()
        self._axes.clear_styles()
        self._for_each_subplot("clear_styles")
        return self

    # Clear the whole plot
    def clear(self):
        self.clear_size()
        self.clear_subplots()
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
    def _next_marker(self):
        return marker_class(defaults.marker, self._cycler.next_pixel())

    # Build a signal from raw args. Decorations (label, lines, line_method, fill_method, fillx, filly, fill)
    # are set on the returned signal via its public fluent methods (see signal_class).
    def signal(self, *args, marker = None, xside = None, yside = None):
        x, y = correct_data.data(*args)
        xside = correct_axis.side(0, xside)   # "lower"/0/False/None -> 0, "upper"/1/True -> 1
        yside = correct_axis.side(1, yside)   # "left"/0/False/None  -> 0, "right"/1/True -> 1

        m = correct_marker.markers(marker, self._next_marker(), len(x))

        x = self.convert(x, "timestamp", axis = 0, side = xside) if self._is_date_active(0, xside) else x
        y = self.convert(y, "timestamp", axis = 1, side = yside) if self._is_date_active(1, yside) else y

        signal = signal_class(len(x))
        signal._append_points(x, y, m)
        signal._set_marker(m[0] if m else correct_marker.marker(marker, self._next_marker()))   # ensure the master marker is set even when data is empty (legend reads it)
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

    # Configure the plot legend: visibility, position, alignment, colour, axis anchoring.
    # status defaults to True so any call (including bare legend()) activates the legend.
    def legend(self, status = True, x = None, y = None, ha = None, va = None, relative = None, pixel = None, xside = None, yside = None):
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

    # Set ruler pixel (colour/style of tick labels). Recolours existing ticks
    # in place — call after ticks() to restyle labels without resetting them.
    def ruler_pixel(self, pixel = None, axis = binary, side = binary):
        self._rulers.set_pixel(pixel, axis, side)
        self._for_each_subplot("ruler_pixel", pixel, axis, side)
        return self

    # Set tick label alignment along the chosen axis ticks region. None resets to the per-side default.
    def tick_alignment(self, alignment = None, axis = 0, side = 0):
        axis = correct_axis.axis(axis)
        alignment = correct_placement.alignment(alignment, orientation = 1 - axis, default = None)
        self._rulers.set_tick_alignment(alignment, axis, side)
        self._for_each_subplot("tick_alignment", alignment, axis, side)
        return self

    # Set grid
    def grid(self, active = None, style = None, pixel = None, axis = binary, side = binary):
        active = correct_bool.boolean(active, True)
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
        axis = correct_axis.axis(axis)
        side = correct_axis.side(axis, side)
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

    # Log timings; recurses into subplots (when full=True) so each one prints its own report indented right after the parent's `create matrices` event — the place where its work logically happened. Subplot events are indented one more level than their `Subplot(r, c)` header so the hierarchy reads naturally. Returns the master's total elapsed time in milliseconds — handy for assertions / perf gating.
    def time(self, full = True):
        indent = (self._get_nest_level() - 1) * 3
        event_pad = ' ' * (indent + (1 if not self._is_master() else 0))
        pad = ' ' * indent
        header = "Plotext Timing Report" if self._is_master() else f"Subplot({self.get_position()[0]}, {self.get_position()[1]}) timing"
        print(f"{pad}{header} {self._timer.to_string(self._timer.get_total_duration())}")
        if full:
            for label in self._timer.get_labels():
                print(f"{event_pad}└─ {label} {self._timer.to_string(self._timer.get_event_duration(label))}")
                if label == "create matrices" and self._has_subplots():
                    for r, c in self._get_slots_range():
                        self._get_subplot(r, c).time(full)
        return self._timer.get_total_duration()

    # Build and print the plot
    def show(self, colorless = False, flush = False):
        out = self.build()
        self._start_event("print")
        out.print(colorless = colorless, flush = flush)
        self._stop_event("print")
        return out

    # Build the plot matrix; recurses into nested subplots so containers
    # render their full subtree. Harmonization runs once at the master.
    def build(self):
        self._timer.clear()

        # Resolve any None subplot sizes top-down before rendering
        if self._is_master():
            self._harmonize_sizes()

        if self._no_subplots():
            return self._get_plot_matrix()

        self._start_event("create matrices")
        matrices = [[self._get_subplot(r, c).build() for c in self._get_cols_range()] for r in self._get_rows_range()]
        self._stop_event("create matrices")

        self._start_event("join matrices")
        out = join_matrices(matrices)
        self._stop_event("join matrices")

        return out