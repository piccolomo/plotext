# Plot class: main subplot container with signals, axes, legend, rulers, labels and canvas

from plotext._plotter.build import plot_build_class
from plotext._plotter.utils.parts import parts_class
from plotext._plotter.subplot import subplot_class
from plotext._plotter.legend import legend_class
from plotext._plotter.clear import clear_class
from plotext._plotter.utils.timer import timer_class
from plotext._plotter.utils.cycler import color_cycler
from plotext._plotter.utils.interactive import interactive_class, reprint_after
from plotext._plotter.draw import draw_class

from plotext._plotter.frame.labels import labels_class
from plotext._plotter.frame.rulers import rulers_class
from plotext._plotter.frame.selection import ruler_selection_class, date_selection_class
from plotext._plotter.frame.axes import axes_class

from plotext._signal.signal import signal_class
from plotext._signal.signals import signals_class

from plotext._correct import data as correct_data
from plotext._correct import bool as correct_bool
from plotext._correct import pixel as correct_pixel
from plotext._correct import marker as correct_marker
from plotext._correct import axis as correct_axis
from plotext._correct import enums as correct_line

from plotext._methods.string import pad
from plotext._primitives.colorize import colorize
from plotext._primitives.pixel import pixel
from plotext._correct import placement as correct_placement

from plotext._settings import defaults
from plotext._settings.themes import themes
from plotext._constants.numerical import binary

from plotext._methods.matrix import join_matrices
from plotext._primitives.marker import marker as marker_class


# Master plot class: composes subplot, draw, build and interactive behavior
class plot_class(subplot_class, draw_class, plot_build_class, interactive_class):

    # Initialize all plot components
    def __init__(self, parent):
        interactive_class.__init__(self)          # set first: decorated setters run during the init below and read this state on the master
        self._parts = parts_class()
        self._labels = labels_class()
        self._rulers = rulers_class(self)
        self._axes = axes_class()
        self._signals = signals_class()
        self._legend = legend_class()
        self.clear = clear_class(self)
        self._timer = timer_class()
        self._cycler = color_cycler(defaults.pixel_sequence)

        subplot_class.__init__(self, parent)
        draw_class.__init__(self)
        plot_build_class.__init__(self)

        self.canvas()

    # Create the grid of subplots, each taking a copy of the settings; on a subplot, the sizes are harmonized first, since a subplot with no size of its own cannot hold a grid.
    @reprint_after
    def subplots(self, rows = None, cols = None):
        if not self._is_master():
            self.master()._harmonize_sizes()
        subplot_class._set_subplots(self, rows, cols)
        self._propagate("_clone", self)
        return self

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
        self._parts.set_size(*self.size())
        return self

    # Produce next marker with next color from cycler
    def _next_marker(self):
        return marker_class(defaults.marker)._set_pixel(self._cycler.next_pixel())

    # Build a signal from the given data; its label, lines, density and fills are set afterwards, on the signal itself.
    def signal(self, *args, marker = None, xside = None, yside = None):
        x, y = correct_data.data(*args)
        xside = correct_axis.side(0, xside)   # "lower"/0/False/None -> 0, "upper"/1/True -> 1
        yside = correct_axis.side(1, yside)   # "left"/0/False/None  -> 0, "right"/1/True -> 1

        m = correct_marker.markers(marker, self._next_marker(), len(x))

        x = self._rulers.get(0, xside)._date.convert(x, "timestamp") if self._rulers.get(0, xside)._date.active() else x
        y = self._rulers.get(1, yside)._date.convert(y, "timestamp") if self._rulers.get(1, yside)._date.active() else y

        signal = signal_class(len(x))
        signal._append_points(x, y, m)
        signal._set_marker(m[0] if m else correct_marker.marker(marker, self._next_marker()))   # ensure the master marker is set even when data is empty (legend reads it)
        signal._set_xside(xside)._set_yside(yside)
        return signal

    # Return the selection of the rulers of the chosen axes and sides (lists or the word both grab several at once); its methods configure ticks, limits, scale, direction, alignments, pixel and dates.
    def ruler(self, axis = None, side = None):
        return ruler_selection_class(self._rulers.select(axis, side))

    # Return the date converter of the rulers of the chosen axes and sides, the only access to date support
    def date(self, axis = None, side = None):
        rulers = self._rulers.select(axis, side)
        return date_selection_class([ruler._date for ruler in rulers], [ruler._name() for ruler in rulers])

    # Set the plot title
    @reprint_after
    def title(self, label = None):
        self._labels.set_title(label)
        self._propagate("title", label)
        return self

    # Set the label of the selected axis and side
    @reprint_after
    def label(self, label = None, axis = None, side = None):
        self._labels.set(label, axis, side)
        self._propagate("label", label, axis, side)
        return self

    # Set visibility, style and pixel of the selected frame axes, all four by default
    @reprint_after
    def axes(self, active = True, style = None, pixel = None, axis = binary, side = binary):
        style = correct_line.line_style(style) if style is not None else None
        self._axes.set(axis = axis, side = side, status = active, style = style, pixel = pixel)
        self._propagate("axes", active, style, pixel, axis, side)
        return self

    # Set the background color of the plot canvas
    @reprint_after
    def canvas(self, background = None):
        # The color "default" leaves the canvas unpainted, so whatever the terminal shows stays behind the plot; any other value, None included, falls back to the default canvas pixel
        if background == "default":
            self._canvas_pixel = pixel()
        else:
            canvas_pixel = pixel(background = background) if background is not None else None
            self._canvas_pixel = correct_pixel.pixel(canvas_pixel, defaults.pixels["canvas"])
        self._propagate("canvas", background)
        return self

    # Configure the plot legend: visibility, position, alignment, color and the line style of its box
    @reprint_after
    def legend(self, active = True, x = None, y = None, ha = None, va = None, relative = None, pixel = None, style = None, xside = None, yside = None):
        style = correct_line.line_style(style) if style is not None else None
        self._legend.set(status = active, x = x, y = y, relative = relative,
                         ha = ha, va = va, pixel = pixel, style = style,
                         xside = xside, yside = yside)
        self._propagate("legend", active, x, y, ha, va, relative, pixel, style, xside, yside)
        return self

    # Apply a named colour preset (canvas + frame + ruler + label + legend + cycler sequence) in one call; unknown names fall back to the default theme, which holds the package default pixels, the out-of-the-box look
    @reprint_after
    def theme(self, name = "default"):
        t = themes[name if name in themes else "default"]
        # Clone the theme pixels in directly (authoritative, no merge with package defaults, so the colorless theme stays genuinely colourless)
        self._canvas_pixel.clone(t["canvas"])
        [a._pixel.clone(t["axes"]) for a in self._axes.get_multiple(binary, binary)]
        [r._pixel.clone(t["ruler"]) for r in self._rulers.select(binary, binary)]
        [r._grid.set_pixel(t["grid"]) for r in self._rulers.select(binary, binary)]
        [a._pixel.clone(t["legend"]) for a in self._legend._axes.get_multiple(binary, binary)]
        self._labels._pixel.clone(t["label"])
        self._legend._pixel.clone(t["legend"])
        self._cycler.set_sequence(t["sequence"])
        self._propagate("theme", name)
        return self

    # Start a timed event
    def _start_event(self, event):
        self._timer.start(event)
        return self

    # Stop a timed event
    def _stop_event(self, event):
        self._timer.stop(event)
        return self

    # Print the timing report, every subplot included when full, each one indented under its parent, and each line starting with its duration in a fixed width, so the labels line up.
    def time(self, full = True):
        format_duration = lambda t: f"{round(t, 2)} ms"
        styled = lambda text, key: colorize(text).fill(defaults.time_report[key]).string()
        labels = list(self._timer.get_labels())
        label_width = max((len(label) for label in labels), default = 0)
        indent = (self._get_nest_level() - 1) * 3
        event_pad = ' ' * indent
        header_pad = ' ' * indent
        header = "Plotext Timing Report" if self._is_master() else f"Subplot({self.position()[0]}, {self.position()[1]})"
        header_padding = ' ' * max(0, 3 + label_width - len(header))
        print(f"{header_pad}{styled(header, 'header')}{header_padding} {styled(format_duration(self._timer.get_total_duration()), 'header time')}")
        if full:
            for label in labels:
                print(f"{event_pad}{styled('└─', 'arrow')} {styled(label, 'label')}{' ' * (label_width - len(label))} {styled(format_duration(self._timer.get_event_duration(label)), 'time')}")
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
        return self

    # Build the plot matrix, every nested subplot included; the sizes are harmonized once, on the master figure.
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