from plotext._colorize import colorize
from plotext._symbols import *
from plotext._correct import correct_class as correct
from plotext._derived import *

class axis_class:
    # Initialize axis with axis and side
    def __init__(self, axis = 0, side = 0):
        self.set_axis(axis, side)
        self.set()
        self.update_tick()

    # Set axis and side attributes
    def set_axis(self, axis = 0, side = 0):
        # axis = correct.axis(axis)
        # side = correct.single_side(axis, side)
        self.axis = axis
        self.side = side
        return self

    # Set status, style, and pixel attributes
    def set(self, status = None, style = None, pixel = None):
        self.set_status(status)
        self.set_style(style)
        self.set_pixel(pixel)
        return self

    def clear_settings(self):
        self.set_status()
        self.set_style()
        return self

    # Set axis active status
    def set_status(self, status = True):
        status = correct.status(status, default_axis_status)
        self.status = status
        return self

    # Set style of axis symbols
    def set_style(self, style = None):
        style = correct.axis_style(style)
        self.style = style
        return self

    # Set pixel, default if none provided
    def set_pixel(self, pixel = None, default_pixel = None):
        pixel = correct.pixel(pixel, default_ruler_pixel)
        self.pixel = pixel
        return self

    # Update tick symbol based on axis and side
    def update_tick(self):
        if self.axis:
            self.tick = get_symbol(right_node, self.style) if self.side else get_symbol(left_node, self.style)
        else:
            self.tick = get_symbol(upper_node, self.style) if self.side else get_symbol(lower_node, self.style)

    # Generate string representation of the axis line
    def get_string(self, width, corners = True):
        if self.axis:
            line = get_symbol(vertical_line, self.style)
            return [line] * width
        else:
            line = get_symbol(horizontal_line, self.style)
            left = get_symbol(upper_left_corner, self.style) if self.side else get_symbol(lower_left_corner, self.style)
            right = get_symbol(upper_right_corner, self.style) if self.side else get_symbol(lower_right_corner, self.style)
            return [left] + [line] * (width - 2) + [right] if corners else [line] * width

    # Clone properties from another axis instance
    def clone(self, axis):
        self.axis = axis.axis
        self.side = axis.side
        self.status = axis.status
        self.style = axis.style
        self.pixel.clone(axis.pixel)
        self.update_tick()
        return self

    # Return a formatted log string of axis properties
    def get_log(self):
        return f"axis {self.axis}, side {self.side}, status {self.status}, style {self.style}, pixel {self.pixel}"

    # Print the axis log
    def log(self):
        print(self.get_log())

    # Representation returns the log string
    def __repr__(self): return self.get_log()
