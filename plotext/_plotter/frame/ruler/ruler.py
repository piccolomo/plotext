# Ruler: one axis/side ruler owning ticks, limits, lines, grid, date, scale and pixel

from plotext._plotter.frame.ruler.ticks import ticks_class
from plotext._plotter.frame.ruler.limits import limits_class
from plotext._plotter.frame.ruler.lines import lines_class, line_style
from plotext._correct import limits as correct_limits
from plotext._correct import label as correct_labels
from plotext._correct import pixel as correct_pixel

from plotext._settings import defaults
from plotext._methods import ruler as ruler_methods
from plotext._methods import string
from plotext._plotter.frame.ruler.date import date_class


# One ruler (axis + side): ticks, limits, lines, grid, date and pixel
class ruler_class:
    # Initialize the ruler with default components and settings
    def __init__(self):
        self._ticks = ticks_class()
        self._limits = limits_class()
        self._lines = lines_class()
        self._date = date_class()

        self.set_alignment()
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
        self._lines.clear_settings()
        self._date.clear()
        self._grid.clear_settings()
        return self

    # Reset pixels of ruler, grid and lines
    def _clear_pixels(self):
        self._pixel.clone(defaults.pixels["ruler"])
        self._grid.clear_pixel(defaults.pixels["grid"])
        self._lines.clear_pixels()
        return self

    # Reset styles of lines and grid
    def _clear_styles(self):
        self._lines.clear_styles()
        self._grid.clear_style()
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

    # Create the grid line_style container
    def create_grid(self):
        self._grid = line_style(False, None, None, defaults.pixels["grid"])
        return self

    # Set grid active flag, style and pixel
    def set_grid(self, active, style, pixel):
        self._grid.set_active(active, True)
        self._grid.set_style(style) if style is not None else None
        self._grid.set_pixel(pixel) if pixel is not None else None
        return self

    # Set pixel configuration for the ruler
    def set_pixel(self, pixel = None):
        self._pixel = correct_pixel.pixel(pixel, defaults.pixels["ruler"])
        return self

    # Clear grid settings, style and pixel
    def _clear_grid(self):
        self._grid.clear()
        return self

    # Fix the grid pixel against another pixel
    def _fix_grid_pixel(self, pixel):
        self._grid.get_pixel()._fix(pixel)
        return self

    # Fix the ruler pixel against another pixel
    def _fix_pixel(self, pixel):
        self._pixel._fix(pixel)
        return self

    # Configure date mode
    def set_date(self, active = True, form = None, origin = None, axis = None, side = None):
        self._date.set_form(form)._set_active(active).set_origin(origin)
        return self

    # Update limits based on provided limits
    def _update_limits(self, limits):
        self._limits.update(limits)
        return self

    # Update limits based on current ticks
    def _update_ticks_limits(self):
        self._update_limits(self._ticks.get_limits())
        return self

    # Update limits based on lines
    def _update_lines_limits(self):
        self._limits.update(self._lines.get_limits())
        return self

    # Rescale ticks and lines according to limits
    def _rescale(self, bins):
        lims = self._limits.get(direction = True)
        delta = self._limits.get_delta()
        self._ticks.rescale(lims, bins, delta)
        self._lines.rescale(lims, bins, delta)
        self._ticks.filter(bins)
        self._lines.filter(bins)
        return self

    # Materialize grid lines from current tick positions
    def _add_grid_lines(self):
        [self._lines.add(pos, False, self._grid.get_style(), self._grid.get_pixel()) for pos in self._ticks.get_positions()] if self._grid.is_active() else None
        return self

    # Get current tick (position, label) tuples
    def _get_ticks_tuples(self):
        return self._ticks.get_tuples()

    # Get scale
    def _get_scale(self):
        return self._scale

    # Get pixel
    def _get_pixel(self):
        return self._pixel

    # Get current limits
    def _get_limits(self, direction = False):
        return self._limits.get(direction = direction)

    # Get lines object
    def _get_lines(self):
        return self._lines

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

    # Update lines, honoring log scale
    def _update_lines(self):
        self._lines.log() if self._get_scale() == "log" else None
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
        self._pixel = ruler._pixel
        self._frequency = ruler._frequency
        self._lines.clone(ruler._lines)
        self._date.clone(ruler._date)
        self._grid = ruler._grid
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
        out += f"\n direction: {self._limits._direction}"
        out += f"\n Lines: {self._lines.get_length()}"
        out += f"\n Grid: {self._grid.get_log()}"
        out += "\n Date: " + self._date.get_log()
        return out


# X-axis ruler with x-specific default frequency
class xruler_class(ruler_class):
    # Set X-axis default frequency
    def set_frequency(self, frequency = None):
        super().set_frequency(frequency, defaults.frequency["x"])
        return self


# Y-axis ruler with y-specific default frequency
class yruler_class(ruler_class):
    # Set Y-axis default frequency
    def set_frequency(self, frequency = None):
        super().set_frequency(frequency, defaults.frequency["y"])
        return self
