# Limits: ruler lower/upper bounds with alignment and direction

from plotext._correct import limits as correct
from plotext._correct import bool as correct_bool
from plotext._constants.numerical import directions
from plotext._constants.enums import scales

from plotext._methods.ruler import log, get_limit_delta
from plotext._methods import string


# Ruler limits container: lower/upper bounds with alignment and direction
class limits_class:
    # Initialize object
    def __init__(self):
        self.clear()

    # Reset all settings to default
    def clear(self):
        self.set()
        self.set_alignment()
        self.set_direction()
        return self

    # Set the lower and upper limits asked for, None leaving that side to the plot content
    def set(self, lower = None, upper = None):
        self._limits = [lower, upper]
        self._content_limits = [None, None]
        return self

    # Update the limits the plot content needs, leaving the asked ones untouched. merge=False just fills None entries from `limits`; merge=True unions the current range with `limits` so neither side gets discarded.
    def update(self, limits = None, merge = False):
        self._content_limits = correct.merge_limits(self._content_limits, limits, merge)
        return self

    # Set alignment for limits
    def set_alignment(self, alignment = "center"):
        self._alignment = alignment
        return self

    # Set direction for limits
    def set_direction(self, direction = 1):
        direction = correct_bool.direction(direction)
        self._direction = direction
        return self

    # Invert current direction
    def invert_direction(self):
        self._direction *= -1
        return self

    # Apply logarithm to both bounds
    def log(self):
        self._limits = [None if limit is None else log(limit) for limit in self._limits]
        self._content_limits = [None if limit is None else log(limit) for limit in self._content_limits]
        return self

    # Get the limits in use, optionally reversed by direction: the asked ones on each side where one was given, those needed by the plot content elsewhere
    def get(self, direction = False):
        limits = [asked if asked is not None else content for asked, content in zip(self._limits, self._content_limits)]
        limits = limits[::self._direction] if direction else limits
        return limits

    # Get alignment
    def get_alignment(self):
        return self._alignment

    # Get alignment delta
    def get_delta(self):
        return get_limit_delta(self._alignment)

    # Get direction
    def get_direction(self):
        return self._direction

    # Check if limits are undefined
    def inactive(self):
        return None in self.get()

    # Check if both limits are defined
    def active(self):
        return not self.inactive()

    # Clone attributes from another limits object
    def clone(self, limits):
        self._limits = limits._limits
        self._content_limits = limits._content_limits
        self._alignment = limits._alignment
        self._direction = limits._direction
        return self

    # Return log string
    def _get_log(self):
        return f"limits: {string.log_limits(self.get())}, alignment: {self._alignment}, direction: {self._direction}"

    # Return string representation
    def __repr__(self):
        return "PlotextLimits(" + self._get_log() + ")"
