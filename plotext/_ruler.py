from plotext._ticks import ticks_class
from plotext._limits import limits_class
from plotext._lines import lines_class
from plotext._correct import correct_class as correct
from plotext._derived import *
from plotext._methods.list import linspace
from plotext._methods.ruler import *
from plotext._date import date_class


class ruler_class:
    def __init__(self):
        self.ticks = ticks_class()
        self.limits = limits_class()
        self.lines = lines_class()
        self.date = date_class()
        self.set_pixel()
        self.set_frequency()

    # --- Reset ruler ---
    def clear(self):
        self.ticks.clear()
        self.limits.clear()
        self.set_pixel()
        self.set_frequency()
        self.lines.clear()
        self.date.clear()
        return self

    # --- Set properties ---
    def set(self, frequency = None, scale = None, alignment = None, direction = None, pixel = None, default_frequency = None):
        self.set_frequency(frequency)
        self.set_alignment(alignment)
        self.set_direction(direction)
        self.set_scale(scale)
        self.set_pixel(pixel)
        return self

    def set_alignment(self, alignment = None):
        alignment = correct.limits_alignment(alignment)
        self.limits.set_alignment(alignment)
        return self

    def set_direction(self, direction = None):
        self.limits.set_direction(direction)
        return self

    def invert_direction(self):
        self.limits.invert_direction()
        return self

    def set_scale(self, scale = None):
        self.limits.set_scale(scale)
        return self

    def set_pixel(self, pixel = None):
        self.pixel = correct.pixel(pixel, default_ruler_pixel)
        return self

    def set_limits(self, lower = None, upper = None):
        self.limits.set(lower, upper)
        return self

    def set_frequency(self, frequency = None, default_frequency = None):
        self.frequency = default_frequency if frequency is None else frequency
        return self

    def set_ticks(self, positions = None, labels = None):
        positions = [] if positions is None else positions
        if labels is None:
            labels = get_labels(positions) if not self.date._active else self.date.convert(positions, "string")
        labels = correct.labels(labels, self.pixel)
        self.ticks.set(positions, labels)
        return self

    def set_date_form(self, form = None, active = True):
        self.date.set_form(form)._set_active(active)
        return self

    # --- Update limits and ticks ---
    def update_ticks_limits(self, limits):
        self.limits.update(limits)
        return self

    def update_lines_limits(self):
        self.limits.update(self.lines.get_limits())
        return self

    def update_ticks(self):
        self.ticks.clone(self.get_ticks())
        return self

    def rescale(self, bins):
        lims = self.limits.get(scaled = True, direction = True)
        delta = self.limits.get_delta()
        self.ticks.rescale(lims, bins, delta)
        self.lines.rescale(lims, bins, delta)
        return self

    # --- Getters ---
    def get(self):
        return self.ticks.get()

    def get_limits(self, scaled = False, direction = False):
        return self.limits.get(scaled = scaled, direction = direction)

    def get_lines(self):
        return self.lines

    def get_direction(self):
        return self.limits.get_direction()

    def get_delta(self):
        return self.limits.get_delta()

    def get_ticks(self):
        selected = self.ticks.select(self.get_limits())
        return selected if selected.is_active() else self.get_auto_ticks()

    def get_auto_ticks(self):
        if not self.limits.is_active():
            return ticks_class().set([], [])
        positions_scaled = linspace(*self.get_limits(scaled = True), self.frequency)
        positions_unscaled = reverse_scale(positions_scaled, self.limits.scale)
        labels = get_labels(positions_unscaled) if not self.date._active else self.date.convert(positions_unscaled, "string")
        labels = correct.labels(labels, self.pixel)
        return ticks_class().set(positions_scaled, labels)

    def is_active(self):
        return self.ticks.is_active()

    # --- Logging ---
    def get_log(self):
        return f'Frequency {self.frequency}, Pixel {self.pixel}, {self.ticks.get_log()}, {self.limits.get_log()}, {self.lines.get_log()}' + self.date._get_log()

    def log(self):
        print(self.get_log())
        return self

    # --- Clone ---
    def clone(self, ruler):
        self.ticks.clone(ruler.ticks)
        self.limits.clone(ruler.limits)
        self.pixel = ruler.pixel
        self.frequency = ruler.frequency
        self.lines.clone(ruler.lines)
        self.date._clone(ruler.date)
        return self

    def __repr__(self):
        return self.get_log()


# --- Ruler subclasses with default frequencies ---
class xruler_class(ruler_class):
    def set_frequency(self, frequency = None):
        super().set_frequency(frequency, default_xfrequency)
        return self


class yruler_class(ruler_class):
    def set_frequency(self, frequency = None):
        super().set_frequency(frequency, default_yfrequency)
        return self
