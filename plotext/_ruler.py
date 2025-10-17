# Ruler Class: Extends bounded_ticks to include line management for plotting

from plotext._ticks import ticks_class  # Base class for bounded ticks
from plotext._limits import limits_class
from plotext._lines import lines_class  # Manages lines associated with the ruler

from plotext._correct import correct_class as correct
from plotext._derived import *
from plotext._methods import *


class ruler_class:
    def __init__(self):
        self.ticks = ticks_class()
        self.limits = limits_class()
        self.lines = lines_class()
        self.set_pixel()
        self.set_frequency()

    # Reset ruler to defaults
    def clear(self):
        self.ticks.clear()
        self.limits.clear()
        self.set_pixel()
        self.set_frequency()
        self.lines.clear()
        return self

    # Set alignment, direction, scale, and pixel
    def set(self, frequency = None, scale = None, alignment = None, direction = None, pixel = None, default_frequency = None):
        self.set_frequency(frequency)
        self.set_alignment(alignment)
        self.set_direction(direction)
        self.set_scale(scale)
        self.set_pixel(pixel)
        return self


    # Set alignment of limits
    def set_alignment(self, alignment = None):
        alignment = correct.limits_alignment(alignment)
        self.limits.set_alignment(alignment)
        return self

    # Set direction of limits
    def set_direction(self, direction = None):
        self.limits.set_direction(direction)
        return self

    # Invert the direction
    def invert_direction(self):
        self.limits.invert_direction()
        return self

    # Set scale of limits
    def set_scale(self, scale = None):
        self.limits.set_scale(scale)
        return self

    # Set pixel style
    def set_pixel(self, pixel = None):
        pixel = correct.pixel(pixel, default_ruler_pixel)
        self.pixel = pixel
        return self

    # Set lower and upper limits
    def set_limits(self, lower = None, upper = None):
        self.limits.set(lower, upper)
        return self

    # # Set default frequency for ticks
    # def set_default_frequency(self, frequency = None):
    #     self.default_frequency = frequency
    #     return self

    # Set frequency for ticks
    def set_frequency(self, frequency = None, default_frequency = None):
        self.frequency = default_frequency if frequency is None else frequency 
        return self

    # Set ticks positions and labels
    def set_ticks(self, positions = None, labels = None):
        positions = [] if positions is None else positions
        labels = ruler_methods.get_labels(positions) if labels is None else labels
        labels = correct.labels(labels, self.pixel)
        self.ticks.set(positions, labels)
        return self


    # Update limits with new limits object
    def update_ticks_limits(self, limits):
        self.limits.update(limits)
        return self

    # Update limits based on line limits
    def update_lines_limits(self):
        self.limits.update(self.lines.get_limits())
        return self

    # Update ticks based on selected ticks
    def update_ticks(self):
        self.ticks.clone(self.get_ticks())
        return self


    # Rescale ticks and lines based on bins
    def rescale(self, bins):
        lims = self.limits.get(scaled = True, direction = True)
        delta = self.limits.get_delta()
        self.ticks.rescale(lims, bins, delta)
        self.lines.rescale(lims, bins, delta)
        return self


    # Get ticks positions and labels
    def get(self):
        return self.ticks.get()

    def get_limits(self, scaled = False, direction = False):
        return self.limits.get(scaled = scaled, direction = direction)

    # Get lines object
    def get_lines(self):
        return self.lines

    # Get direction of limits
    def get_direction(self):
        return self.limits.get_direction()

    # Get delta of limits
    def get_delta(self):
        return self.limits.get_delta()

    # Get selected ticks or auto ticks
    def get_ticks(self):
        selected = self.ticks.select(self.get_limits())
        return selected if selected.is_active() else self.get_auto_ticks()

    # Get automatically generated ticks
    def get_auto_ticks(self):
        if not self.limits.is_active():
            return ticks_class().set([], [])
        positions_scaled = list_methods.linspace(*self.get_limits(scaled = True), self.frequency)
        positions_unscaled = ruler_methods.reverse_scale(positions_scaled, self.limits.scale)
        labels = ruler_methods.get_labels(positions_unscaled)
        labels = correct.labels(labels, self.pixel)
        return ticks_class().set(positions_scaled, labels)


    # Check if ruler is active
    def is_active(self):
        return self.ticks.is_active() 


    # Get a log string representing current state
    def get_log(self):
        return f'Frequency {self.frequency}, Pixel {self.pixel}, {self.ticks.get_log()}, {self.limits.get_log()}, {self.lines.get_log()}'

    # Print the log string
    def log(self):
        print(self.get_log())


    # Clone the state from another ruler
    def clone(self, ruler):
        self.ticks.clone(ruler.ticks)
        self.limits.clone(ruler.limits)
        self.pixel = ruler.pixel
        self.frequency = ruler.frequency
        self.lines.clone(ruler.lines)
        return self


    # String representation of the ruler
    def __repr__(self):
        return self.get_log()


class xruler_class(ruler_class):
    def set_frequency(self, frequency = None):
        ruler_class.set_frequency(self, frequency, default_xfrequency)
        return self


class yruler_class(ruler_class):
    def set_frequency(self, frequency = None):
        ruler_class.set_frequency(self, frequency, default_yfrequency)
        return self





