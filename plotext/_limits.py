from plotext._correct import correct_class as correct 
from plotext._constants import directions, scales
from plotext._methods import *


class limits_class:
    def __init__(self):
        self.clear()

    # Reset all settings to default
    def clear(self):
        self.set()
        self.set_alignment()
        self.set_direction()
        self.set_scale()

    # Set lower and upper limits
    def set(self, lower = None, upper = None):
        self.limits = [lower, upper]
        return self

    # Update limits with corrections
    def update(self, limits = None):
        self.limits = correct.limits(self.limits, limits)
        return self


    # Set alignment for limits
    def set_alignment(self, alignment = "center"):
        self.alignment = alignment
        return self

    # Set direction for limits
    def set_direction(self, direction = 1):
        self.direction = direction
        return self

    # Invert current direction
    def invert_direction(self):
        self.direction *= -1
        return self

    # Set scale for limits
    def set_scale(self, scale = "linear"):
        self.scale = scale
        return self


    # Get current limits, optionally scaled and/or reversed by direction
    def get(self, scaled = False, direction = False):
        limits = self.limits[::self.direction] if direction else self.limits
        limits = ruler_methods.apply_scale(limits, self.scale) if scaled else limits
        return limits

    # Get alignment
    def get_alignment(self):
        return self.alignment

    # Get alignment delta
    def get_delta(self):
        return ruler_methods.get_limit_delta(self.alignment)

    # Get direction
    def get_direction(self):
        return self.direction

    # Get scale
    def get_scale(self):
        return self.scale

    # Check if limits are defined
    def is_active(self):
        return None not in self.limits

    # Clone attributes from another limits object
    def clone(self, limits):
        self.limits = limits.limits
        self.alignment = limits.alignment
        self.direction = limits.direction
        self.scale = limits.scale
        return self


    # Return log string
    def get_log(self):
        return 'Limits ' + log_methods.limits(self.limits) + ', Alignment ' + str(self.alignment) + ', Direction ' + str(self.direction) + ', Scale ' + str(self.scale)

    # Print log string
    def log(self):
        print(self.get_log())

    # Return string representation
    def __repr__(self):
        return self.get_log()





