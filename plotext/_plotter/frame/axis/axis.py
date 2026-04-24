# Axis: single frame axis (one axis / one side), with status, style and pixel

from plotext._primitives.colorize import colorize
from plotext._correct import bool as correct_bool
from plotext._correct import axis as correct_axis
from plotext._correct import pixel as correct_pixel
from plotext._settings import defaults
from plotext._methods import borders as border_methods


# Frame axis: one axis (x or y) on one side (lower/upper or left/right)
class axis_class:
    # Initialize axis with axis and side
    def __init__(self, axis = 0, side = 0):
        self.set_axis(axis, side)
        self.set_status().set_style().set_pixel()

    # Set axis and side attributes
    def set_axis(self, axis = 0, side = 0):
        self._axis = axis
        self._side = side
        return self

    # Set status, style, and pixel attributes
    def set(self, status = None, style = None, pixel = None):
        self.set_status(status)
        self.set_style(style) if style is not None else None
        self.set_pixel(pixel) if pixel is not None else None
        return self

    # Clear all settings, pixel and style
    def clear(self):
        self.clear_settings()
        self.clear_pixel()
        self.clear_style()
        return self

    # Reset status to default
    def clear_settings(self):
        self.set_status()
        return self

    # Reset pixel to default axis pixel
    def clear_pixel(self):
        self._pixel.clone(defaults.pixels["axis"])
        return self

    # Reset style to default
    def clear_style(self):
        self.set_style()
        return self

    # Set axis status status
    def set_status(self, status = True):
        status = correct_bool.boolean(status, defaults.axis["status"])
        self._status = status
        return self

    # Set style of axis symbols
    def set_style(self, style = None):
        style = correct_axis.axis_style(style)
        self._style = style
        return self

    # Set pixel, default if none provided
    def set_pixel(self, pixel = None, default_pixel = None):
        pixel = correct_pixel.pixel(pixel, defaults.pixels["axis"])
        self._pixel = pixel
        return self

    # Build the list of symbols making up the axis line, with tick and grid-line markers
    def get_string(self, height, ticks = [], lines = []):
        line = border_methods.get_line_symbol(self._axis, self._style)
        number_tick = border_methods.get_tick_symbol(self._axis, self._side, self._style)
        line_tick = border_methods.get_tick_symbol(self._axis, not self._side, self._style)
        number_line_tick = border_methods.get_symbol(border_methods.full_node, self._style)

        out = [
            number_line_tick if i in ticks and i in lines
            else number_tick if i in ticks
            else line_tick if i in lines
            else line
            for i in range(height)]

        return out

    # Clone properties from another axis instance
    def clone(self, axis):
        self._axis = axis._axis
        self._side = axis._side
        self._status = axis._status
        self._style = axis._style
        self._pixel.clone(axis._pixel)
        return self

    # Get axis index (0 for x, 1 for y)
    def get_axis(self):
        return self._axis

    # Get side index
    def get_side(self):
        return self._side

    # Get axis status
    def get_status(self):
        return self._status

    # Get axis style
    def get_style(self):
        return self._style

    # Get axis pixel
    def get_pixel(self):
        return self._pixel

    # Build a compact log line for the axis
    def get_log(self):
        return f"side {self._side},  {self._status}, style {self._style}, pixel {self._pixel}"

    # Represent axis in Plotext style
    def __repr__(self):
        return f"Plotext Axis: " + self.get_log()
