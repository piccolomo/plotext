# Ruler: one axis/side ruler owning ticks, limits, lines, grid, date, scale and pixel

from plotext._plotter.frame.ticks import ticks_class
from plotext._plotter.frame.limits import limits_class
from plotext._plotter.frame.lines import lines_class
from plotext._plotter.frame.grid_line import grid_line_class
from plotext._plotter.frame.line_signal import line_signal
from plotext._primitives.matrix import matrix as matrix_class
from plotext._primitives.matrix_marker import matrix_marker
from plotext._signal.point import point_class
from plotext._correct import limits as correct_limits
from plotext._correct import label as correct_labels
from plotext._correct import pixel as correct_pixel
from plotext._correct import placement as correct_placement

from plotext._settings import defaults
from plotext._methods import ruler as ruler_methods
from plotext._methods import string
from plotext._plotter.frame.date import date_class


# One ruler (axis + side): ticks, limits, lines, grid, date and pixel
class ruler_class:
    # Initialize the ruler with default components and settings
    def __init__(self):
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

    # Clear settings and pixels
    def clear(self):
        self._clear_settings()
        self._clear_pixels()
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

    # Set lower and upper limits
    def set_limits(self, lower = None, upper = None):
        self._limits.set(lower, upper)
        return self

    # Invert the direction of limits
    def _invert_direction(self):
        self._limits.invert_direction()
        return self

    # Set frequency of ticks
    def set_frequency(self, frequency = None, default_frequency = None):
        self._frequency = default_frequency if frequency is None else frequency
        return self

    # Set tick positions and labels
    def set_ticks(self, positions = None, labels = None):
        positions = [] if positions is None else positions
        if labels is None:
            labels = ruler_methods.get_labels(positions) if not self._date._active else self._date.convert(positions, "string")
        labels = correct_labels.labels(labels, self._pixel)
        self._ticks.set(positions, labels)
        return self

    # Create the grid (style + pixel + active flag)
    def create_grid(self):
        self._grid = grid_line_class(style=None, pixel=defaults.pixels["grid"], active=False)
        return self

    # Set grid active flag, style and pixel
    def set_grid(self, active, style, pixel):
        self._grid.set_active(active)
        self._grid.set_style(style) if style is not None else None
        self._grid.set_pixel(pixel) if pixel is not None else None
        return self

    # Set pixel configuration for the ruler and recolour any existing tick
    # labels in place so the change is reflected on already-placed ticks.
    def set_pixel(self, pixel = None):
        self._pixel = correct_pixel.pixel(pixel, defaults.pixels["ruler"])
        for tick in self._ticks.ticks:
            lbl = tick.get_label()
            if lbl is not None:
                lbl.set_pixel(self._pixel)
        return self

    # Fix the grid pixel against another pixel; round-trip via set_pixel because box_style_get_pixel returns a copy.
    def _fix_grid_pixel(self, pixel):
        p = self._grid.get_pixel()
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
        labels = self._date.convert(positions, "string") if self._date.is_active() else ruler_methods.get_labels(positions)
        labels = correct_labels.labels(labels, self._pixel)
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
        print(self.get_log())
        return self

    # Clone another ruler into this one
    def _clone(self, ruler):
        self._scale = ruler._scale
        self._ticks.clone(ruler._ticks)
        self._limits.clone(ruler._limits)
        self._pixel.clone(ruler._pixel)
        self._frequency = ruler._frequency
        self._date.clone(ruler._date)
        self._grid = ruler._grid
        self._lines = ruler._lines.copy()
        self._tick_alignment = ruler._tick_alignment
        return self

    # String representation
    def __repr__(self):
        out = f"Plotext Ruler()"
        out += f"\n Frequency {self._frequency}"
        out += f"\n Pixel {self._pixel}"
        out += f"\n Ticks: {self._ticks.get_length()}"
        out += f"\n scale: {self._scale}"
        out += f"\n limits: {string.log_limits(self._limits._limits)}"
        out += f"\n alignment: {self._limits._alignment}"
        out += f"\n tick alignment: {self._tick_alignment}"
        out += f"\n direction: {self._limits._direction}"
        out += f"\n Grid: {self._grid.get_log()}"
        return out


    # Add a user-defined line at the given coord (orientation set by the ruler subclass).
    def add_line(self, coord, relative = False, pixel = None, style = None, label = None, orientation = 0):
        self._lines.add(line_signal(coord, orientation, relative, pixel, style, label))
        return self

    # If grid is active, append a line_signal per tick position to _lines (data-space coords).
    # Subclasses pin orientation based on axis (x-ruler → vertical, y-ruler → horizontal).
    def update_grid_lines(self, orientation):
        if self._grid.is_active():
            pixel = self._grid.get_pixel()
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
    def add_line(self, coord, relative = False, pixel = None, style = None, label = None):
        super().add_line(coord, relative, pixel, style, label, orientation = 1)
        return self

    # X-ruler grid lines are vertical
    def update_grid_lines(self):
        super().update_grid_lines(orientation = 1)
        return self

    # Paint x-ticks (single-row strip, dynamic-alignment labels). Returns canvas cols where labels actually landed.
    def draw_ticks(self, matrix, ticks_col, ticks_row, ticks_width):
        out = matrix_class(ticks_width, 1, self._get_pixel())
        ticks = [int(t.get_position()) for t in self._ticks if out._insert_point(point_class(t.get_position(), 0, matrix_marker(t.get_label(), ha = 2)))]
        matrix._insert_matrix(ticks_col, ticks_row, out)
        return ticks


# Y-axis ruler with y-specific default frequency
class yruler_class(ruler_class):
    # Set Y-axis default frequency
    def set_frequency(self, frequency = None):
        super().set_frequency(frequency, defaults.frequency["y"])
        return self

    # Y-ruler lines are horizontal (cross x axis)
    def add_line(self, coord, relative = False, pixel = None, style = None, label = None):
        super().add_line(coord, relative, pixel, style, label, orientation = 0)
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
        ticks = [int(t.get_position()) for t in self._ticks if out._insert_point(point_class(oc, t.get_position(), matrix_marker(t.get_label(), ha = ta)))]
        matrix._insert_matrix(ticks_col, ticks_row, out)
        return ticks
