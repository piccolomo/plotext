# Line: ruler line primitive with style, pixel and position

from plotext._correct import bool as correct_bool
from plotext._correct import pixel as correct_pixel
from plotext._correct import line as correct_line
from plotext._settings.constants.numerical import directions
from plotext._settings.constants.enums import scales

from plotext._methods import ruler as ruler_methods
from plotext._methods import string
from plotext._methods import borders as border_methods
from plotext._settings import defaults


# Base class owning active flag, style and pixel plus their defaults
class line_style:
    # Initialize active, style, and pixel
    def __init__(self, active = True, style = 'default', pixel = None, default_pixel = None):
        self.set_active(active)
        self.set_style(style)
        self.set_pixel(pixel, default_pixel)

    # Clear settings, style and pixel
    def clear(self):
        self.clear_settings()
        self.clear_style()
        self.clear_pixel()
        return self

    # Reset active flag
    def clear_settings(self):
        self.set_active(False)
        return self

    # Clone pixel from provided default, or from the default set at construction
    def clear_pixel(self, default = None):
        default = self._default_pixel if default is None else default
        self._pixel.clone(default)
        return self

    # Reset style
    def clear_style(self):
        self.set_style(None)
        return self

    # Set the active state
    def set_active(self, active, default = False):
        self._active = correct_bool.boolean(active, default)
        return self

    # Set the line style
    def set_style(self, style):
        self._style = correct_line.line_style(style)
        return self

    # Set the pixel type; if no default is given, reuse the one stored at construction
    def set_pixel(self, pixel, default = None):
        default = self._default_pixel if default is None else default
        self._pixel = correct_pixel.pixel(pixel, default)
        self._default_pixel = default
        return self

    # Get the line style
    def get_style(self):
        return self._style

    # Get the pixel type
    def get_pixel(self):
        return self._pixel

    # Check if the line is active
    def is_active(self):
        return self._active

    # Build a compact log line
    def get_log(self):
        return f"active {self._active}, style {self._style}, pixel {self._pixel}"

    # String representation
    def __repr__(self):
        return f"Plotext LineStyle: " + self.get_log()


# Ruler line at a position (absolute or relative) with style and pixel
class line_class(line_style):
    # Initialize line style and position
    def __init__(self, position, relative = True, style = 'default', pixel = None):
        super().__init__(relative, style, pixel, defaults.pixels["line"])
        self.set_position(position, relative)

    # Set the position of the line
    def set_position(self, position, relative = None):
        self._position = position
        self._relative = correct_bool.boolean(relative, True)
        return self

    # Get the position of the line
    def get_position(self):
        return self._position

    # Check if line is relative
    def get_relative(self):
        return self.is_active()

    # Rescale line positions based on limits, bins and delta
    def rescale(self, limits, bins, delta):
        pos = self.get_position()
        if self.get_relative():
            pos = int(ruler_methods.rescale(pos, *limits, bins, delta))
        else:
            pos = int(pos)
        self.set_position(pos, False)
        return self

    # Apply logarithm to position
    def log(self):
        self._position = ruler_methods.log(self._position)
        return self

    # Check if tick is within given bins
    def is_within_bins(self, bins):
        return 0 <= self._position < bins

    # Generate string representation of the line with crossings
    def get_string(self, width, orientation, crossings=None):
        crossings = set(crossings or [])
        line_symbol = border_methods.get_line_symbol(orientation, self._style)
        crossing_symbol = border_methods.get_symbol(border_methods.full_node, self._style)
        return [crossing_symbol if i in crossings else line_symbol for i in range(width)]

    # Create a copy of the line
    def copy(self):
        return line_class(self.get_position(), self.get_relative(),
                          self.get_style(), self.get_pixel())

    # String representation
    def __repr__(self):
        return (f"Plotext Line: position {round(self._position, 2)}, "
                f"relative {round(self._relative, 2)}, style {self._style}, "
                f"pixel {self._pixel}")
