# Ruler: one axis/side ruler owning ticks, limits, lines, grid, date, scale and pixel

from plotext._plotter.frame.ticks import ticks_class
from plotext._plotter.frame.limits import limits_class
from plotext._plotter.frame.lines import lines_class
from plotext._plotter.frame.grid_line import grid_line_class
from plotext._plotter.frame.line_signal import line_signal
from plotext._primitives.matrix import matrix as matrix_class
from plotext._primitives.marker import marker as marker_class
from plotext._signal.point import point_class
from plotext._correct import bool as correct_bool
from plotext._correct import limits as correct_limits
from plotext._correct import label as correct_labels
from plotext._correct import pixel as correct_pixel
from plotext._correct import placement as correct_placement

from plotext._settings import defaults
from plotext._constants.enums import axis_names, xsides, ysides
from plotext._methods import ruler as ruler_methods
from plotext._methods import string
from plotext._plotter.frame.date import date_class
from plotext._plotter.utils.propagator import propagator_class
from plotext._plotter.utils.interactive import reprint_after


# One ruler (axis + side): ticks, limits, lines, grid, date and pixel
class ruler_class(propagator_class):
    # Initialize the ruler with its plot, axis, side, default components and settings
    def __init__(self, plot = None, axis = 0, side = 0):
        propagator_class.__init__(self, plot)
        self._axis = axis
        self._side = side
        self._ticks = ticks_class()
        self._limits = limits_class()
        self._lines = lines_class()
        self._date = date_class()

        self.set_alignment()
        self.set_tick_alignment()
        self.set_direction()
        self.set_scale()

        self.set_limits()
        self.set_frequency()

        self.create_grid()

        self.set_pixel()

    # Reset all ruler components and settings
    def _clear_settings(self):
        self.set_scale()
        self._ticks.clear()
        self._limits.clear()
        self.set_frequency()
        self.set_tick_alignment()
        self._date.clear()
        self._grid.set_active(False)
        return self

    # Reset pixels of ruler and grid
    def _clear_pixels(self):
        self._pixel.clone(defaults.pixels["ruler"])
        self._grid.set_pixel(defaults.pixels["grid"])
        return self

    # Reset style of grid
    def _clear_styles(self):
        self._grid.set_style(None)
        return self

    # Public setters and getters, reachable via figure.ruler(axis, side); each mirrors the behavior of the old figure-level method for a single ruler.

    # My counterpart: the same axis and side ruler of the given subplot
    def _counterpart(self, subplot):
        return subplot.ruler(self._axis, self._side)

    # Set the number of automatically-placed ticks
    @reprint_after
    def frequency(self, frequency = None):
        self.set_frequency(frequency)
        self._propagate("frequency", frequency)
        return self

    # Set explicit tick positions and optionally their labels
    @reprint_after
    def ticks(self, positions = None, labels = None):
        self.set_ticks(positions, labels)
        self._propagate("ticks", positions, labels)
        return self

    # Set the visible numerical range
    @reprint_after
    def lim(self, lower = None, upper = None):
        self.set_limits(lower, upper)
        self._propagate("lim", lower, upper)
        return self

    # Set the scale: linear or log
    @reprint_after
    def scale(self, scale = None):
        self.set_scale(scale)
        self._propagate("scale", scale)
        return self

    # Set the direction in which values increase: 1 or -1
    @reprint_after
    def direction(self, direction = None):
        self.set_direction(direction)
        self._propagate("direction", direction)
        return self

    # Set the two ruler alignments: lim for the numerical limits, tick for the tick labels; a None parameter leaves that aspect unchanged
    @reprint_after
    def alignment(self, lim = None, tick = None):
        if lim is not None:
            self.set_alignment(lim)
        if tick is not None:
            tick_value = None if tick in ('dynamic', 2) else correct_placement.alignment(tick, orientation = 0, default = None)
            self.set_tick_alignment(tick_value)
        self._propagate("alignment", lim, tick)
        return self

    # Set the pixel used to paint the tick areas
    @reprint_after
    def pixel(self, pixel = None):
        self.set_pixel(pixel)
        self._propagate("pixel", pixel)
        return self

    # Control the grid lines drawn from this ruler ticks
    @reprint_after
    def grid(self, active = True, style = None, pixel = None):
        active = correct_bool.boolean(active, True)
        self.set_grid(active, style, pixel)
        self._propagate("grid", active, style, pixel)
        return self

    # Clear settings and pixels
    def clear(self):
        self._clear_settings()
        self._clear_pixels()
        self._clear_styles()
        return self

    # Set alignment of limits
    def set_alignment(self, alignment = None):
        alignment = correct_limits.limits_alignment(alignment)
        self._limits.set_alignment(alignment)
        return self

    # Store tick label alignment (already corrected by the caller); used by build.py during tick rendering
    def set_tick_alignment(self, alignment = None):
        self._tick_alignment = alignment
        return self

    # Get tick label alignment (or None if unset)
    def _get_tick_alignment(self):
        return self._tick_alignment

    # Set direction of limits
    def set_direction(self, direction = None):
        self._limits.set_direction(direction)
        return self

    # Set scale for limits
    def set_scale(self, scale = "linear"):
        scale = correct_limits.scale(scale)
        self._scale = scale
        return self

    # Turn a date, given as string or datetime object, into the number the axis works with; numbers, and anything given while date support is off, are left alone
    def _to_number(self, value):
        date_given = self._date.active() and value is not None and not isinstance(value, (int, float))
        return self._date.convert(value) if date_given else value

    # Set lower and upper limits, dates accepted
    def set_limits(self, lower = None, upper = None):
        self._limits.set(self._to_number(lower), self._to_number(upper))
        return self

    # Invert the direction of limits
    def _invert_direction(self):
        self._limits.invert_direction()
        return self

    # Set frequency of ticks
    def set_frequency(self, frequency = None, default_frequency = None):
        self._frequency = default_frequency if frequency is None else frequency
        return self

    # Set tick positions and labels, dates accepted as positions; an empty list of positions asks for no ticks at all, exactly as frequency(0) does
    def set_ticks(self, positions = None, labels = None):
        self.set_frequency(0) if positions is not None and len(positions) == 0 else None
        positions = [] if positions is None else positions
        positions = [self._to_number(position) for position in positions]
        if labels is None:
            labels = ruler_methods.get_labels(positions) if not self._date._active else self._date.convert(positions, "string")
        labels = correct_labels.labels(labels)          # kept as given, the ruler pixel paints them when they are drawn
        self._ticks.set(positions, labels)
        return self

    # Create the grid (style + pixel + active flag)
    def create_grid(self):
        self._grid = grid_line_class(style = None, pixel = defaults.pixels["grid"], active = False)
        return self

    # Set grid active flag, style and pixel
    def set_grid(self, active, style, pixel):
        self._grid.set_active(active)
        self._grid.set_style(style) if style is not None else None
        self._grid.set_pixel(pixel) if pixel is not None else None
        return self

    # Set the pixel painting the tick area; the tick labels take it when they are drawn, keeping any color they were given
    def set_pixel(self, pixel = None):
        self._pixel = correct_pixel.pixel(pixel, defaults.pixels["ruler"])
        return self

    # Fix the grid pixel against another pixel; round-trip via set_pixel because box_style_get_pixel returns a copy.
    def _fix_grid_pixel(self, pixel):
        p = self._grid.pixel()
        p._fix(pixel)
        self._grid.set_pixel(p)
        return self

    # Fix the ruler pixel against another pixel
    def _fix_pixel(self, pixel):
        self._pixel._fix(pixel)
        return self

    # Update limits based on provided limits
    def _update_limits(self, limits, merge = False):
        self._limits.update(limits, merge = merge)
        return self

    # Update limits based on current ticks
    def _update_ticks_limits(self, merge = False):
        self._update_limits(self._ticks.get_limits(), merge = merge)
        return self

    # Update limits based on the registered relative lines, so a line can define or extend the axis range even with no data drawn
    def _update_lines_limits(self):
        positions = [line.get_position() for line in self._lines if line.is_relative()]
        if positions:
            self._update_limits([min(positions), max(positions)], merge = True)
        return self

    # Rescale ticks and lines according to limits
    def _rescale(self, bins):
        lims = self._limits.get(direction = True)
        delta = self._limits.get_delta()
        self._ticks.rescale(lims, bins, delta)
        self._ticks.filter(bins)
        self._lines.rescale(self, bins)
        return self

    # Get scale
    def _get_scale(self):
        return self._scale

    # Get pixel
    def _get_pixel(self):
        return self._pixel

    # Get current limits
    def _get_limits(self, direction = False):
        return self._limits.get(direction = direction)

    # Get limits direction
    def _get_direction(self):
        return self._limits.get_direction()

    # Get alignment delta
    def _get_delta(self):
        return self._limits.get_delta()

    # Get date manager
    def _get_date(self):
        return self._date

    # Get ticks object
    def _get_ticks(self):
        return self._ticks

    # Compute automatic tick positions from current limits and frequency
    def _get_auto_positions(self):
        positions = ruler_methods.linspace(*self._get_limits(), self._frequency)
        return positions

    # Compute automatic labels for a set of positions
    def _get_auto_labels(self, positions):
        labels = self._date.convert(positions, "string") if self._date.active() else ruler_methods.get_labels(positions)
        labels = correct_labels.labels(labels)
        return labels

    # Update ticks, honoring log scale and automatic computation when needed
    def _update_ticks(self):
        log_scale = self._get_scale() == "log"

        if self._active_ticks():
            self._ticks.log() if log_scale else None

        elif self._active_limits():
            self._limits.log() if log_scale else None
            positions_scaled = self._get_auto_positions()
            positions_unscaled = ruler_methods.power10_data(positions_scaled) if log_scale else positions_scaled
            labels_unscaled = self._get_auto_labels(positions_unscaled)
            self._ticks.set(positions_scaled, labels_unscaled)

        return self

    # Check if ticks are active
    def _active_ticks(self):
        return self._ticks.active()

    # Check if limits are active
    def _active_limits(self):
        return self._limits.active()

    # Print the log
    def _log(self):
        print(self)
        return self

    # Clone another ruler into this one
    def _clone(self, ruler):
        self._scale = ruler._scale
        self._ticks.clone(ruler._ticks)
        self._limits.clone(ruler._limits)
        self._pixel.clone(ruler._pixel)
        self._frequency = ruler._frequency
        self._date._clone(ruler._date)
        self._grid = ruler._grid
        self._lines = ruler._lines.copy()
        self._tick_alignment = ruler._tick_alignment
        return self

    # The axis and side this ruler belongs to, like lower x
    def _name(self):
        side = (ysides if self._axis else xsides)[self._side]
        return f"{side} {axis_names[self._axis]}"

    # String representation, naming the axis and side this ruler belongs to
    def __repr__(self):
        out = f"Plotext Ruler({self._name()} axis)"
        out += f"\n Frequency {self._frequency}"
        out += f"\n Pixel {self._pixel}"
        out += f"\n Ticks: {self._ticks.length()}"
        out += f"\n scale: {self._scale}"
        out += f"\n limits: {string.log_limits(self._limits._limits)}"
        out += f"\n alignment: {self._limits._alignment}"
        out += f"\n tick alignment: {self._tick_alignment}"
        out += f"\n direction: {self._limits._direction}"
        out += f"\n Grid: {self._grid._get_log()}"
        return out


    # Add a user-defined line at the given position (orientation set by the ruler subclass).
    def add_line(self, position, relative = False, pixel = None, style = None, label = None, orientation = 0):
        self._lines.add(line_signal(position, orientation, relative, pixel, style, label))
        return self

    # With the grid active, add one line at each tick position, vertical on an x ruler and horizontal on a y one.
    def update_grid_lines(self, orientation):
        if self._grid.is_active():
            pixel = self._grid.pixel()
            style = self._grid.get_style()
            for pos in self._ticks.get_positions():
                self._lines.add(line_signal(pos, orientation, True, pixel, style, None))
        return self

    # Render every registered line onto the canvas matrix at canvas_part. Lines must be rescaled first (via _rescale).
    def draw_lines(self, matrix, canvas_part):
        for line_sig in self._lines:
            line_sig.draw(matrix, canvas_part)
        return self

    # Cached canvas-space positions of all registered lines (rescale must have run).
    def get_line_positions(self):
        return [l.get_canvas_position() for l in self._lines]

    # Drop every registered user/grid-derived line.
    def clear_lines(self):
        self._lines.clear()
        return self


# X-axis ruler with x-specific default frequency
class xruler_class(ruler_class):
    # Set X-axis default frequency
    def set_frequency(self, frequency = None):
        super().set_frequency(frequency, defaults.frequency["x"])
        return self

    # X-ruler lines are vertical (cross y axis)
    def add_line(self, position, relative = False, pixel = None, style = None, label = None):
        super().add_line(position, relative, pixel, style, label, orientation = 1)
        return self

    # X-ruler grid lines are vertical
    def update_grid_lines(self):
        super().update_grid_lines(orientation = 1)
        return self

    # Paint x-ticks (single-row strip); labels justify per tick_alignment, defaulting to a dynamic placement that adapts near the edges. Returns canvas cols where labels actually landed.
    def draw_ticks(self, matrix, ticks_col, ticks_row, ticks_width):
        ta = self._get_tick_alignment() if self._get_tick_alignment() is not None else 2
        out = matrix_class(ticks_width, 1, self._get_pixel())
        ticks = [int(t.position()) for t in self._ticks if out._insert_point(point_class(t.position(), 0, marker_class(t.label(), ha = ta)._fix(self._get_pixel())), check_space = True)]
        matrix._insert_matrix(ticks_col, ticks_row, out)
        return ticks


# Y-axis ruler with y-specific default frequency
class yruler_class(ruler_class):
    # Set Y-axis default frequency
    def set_frequency(self, frequency = None):
        super().set_frequency(frequency, defaults.frequency["y"])
        return self

    # Y-ruler lines are horizontal (cross x axis)
    def add_line(self, position, relative = False, pixel = None, style = None, label = None):
        super().add_line(position, relative, pixel, style, label, orientation = 0)
        return self

    # Y-ruler grid lines are horizontal
    def update_grid_lines(self):
        super().update_grid_lines(orientation = 0)
        return self

    # Paint y-ticks (multi-col strip, side-based alignment). side: 0=left, 1=right. Returns canvas rows where labels actually landed.
    def draw_ticks(self, matrix, ticks_col, ticks_row, ticks_width, ticks_height, side):
        default_ta = 1 if side == 0 else -1
        ta = self._get_tick_alignment() if self._get_tick_alignment() is not None else default_ta
        oc = 0 if ta == -1 else (ticks_width - 1 if ta == 1 else (ticks_width - 1) // 2)
        out = matrix_class(ticks_width, ticks_height, self._get_pixel())
        ticks = [int(t.position()) for t in self._ticks if out._insert_point(point_class(oc, t.position(), marker_class(t.label(), ha = ta)._fix(self._get_pixel())))]
        matrix._insert_matrix(ticks_col, ticks_row, out)
        return ticks
