from plotext._default import default_axis, correct_xside, correct_yside
from plotext._color import is_color
from plotext._style import is_style
from plotext._matrix import matrix_class
from plotext._marker import space, border, line, tick
from plotext._canvas import digitize
from plotext._system import copy


class axis_class():
    def set_axis_color(self, color = None):
        color = color if is_color(color) else None
        self.axis_color = default_axis.color if color is None else color

    def clear(self):
        self.__init__(self.side)

    def backup(self):
        self.width_backup = self.width
        self.height_backup = self.height

    def restore(self):
        self.width = self.width_backup
        self.height = self.height_backup

    def copy(self):
        return copy(self)


class xaxis_class(axis_class):
    def __init__(self, side = None):
        self.side = correct_xside(side)
        self.set_height(1)
        self.set_widths()
        
        self.set_axis_color()
        self.update_borders()
        self.update_ticks()

    def set_height(self, height = None):
        self.height = int(bool(height)) if height is not None else None

    def set_widths(self, left = None, canvas = None, right = None):
        self.width_left = left
        self.width_canvas = canvas
        self.width_right = right
        self.width = left + canvas + right if None not in [left, canvas, right] else None

    def update_borders(self):
        self.border_left = border.upper_left if self.side == default_axis.xside else border.lower_left
        self.border_right = border.upper_right if self.side == default_axis.xside else border.lower_right

    def update_ticks(self):
        self.tick_inner = tick.upper if self.side == default_axis.xside else tick.lower
        self.tick_outer = tick.lower if self.side == default_axis.xside else tick.upper
        self.tick_both = tick.cross

    def build(self):
        self.matrix = matrix_class(self.width, self.height)
        self.insert_left()
        self.insert_center()
        self.insert_right()

    def insert_left(self):
        just_do_it = self.height == 1 and self.width_left > 0
        self.matrix.insert_element(0, self.width_left - 1, self.border_left) if just_do_it else None
        
    def insert_center(self):
        just_do_it = self.height == 1
        self.matrix.insert_horizontal_string(0, self.width_left, line.h * self.width_canvas) if just_do_it else None
        
    def insert_right(self):
        just_do_it = self.height == 1 and self.width_right > 0
        self.matrix.insert_element(0, self.width_left + self.width_canvas, self.border_right) if just_do_it else None




class yaxis_class(axis_class):
    def __init__(self, side = None):
        self.side = correct_yside(side)
        self.set_height()
        self.set_width(1)

        self.set_axis_color()

    def set_height(self, height = None):
        self.height = int(height) if height is not None else None

    def set_width(self, width = None):
        self.width = int(bool(width)) if width is not None else None

    def update_ticks(self):
        self.tick_inner = tick.upper if self.side == default_axis.xside else tick.lower
        self.tick_outer = tick.lower if self.side == default_axis.xside else tick.upper
        self.tick_both = tick.cross
        
    def build(self):
        self.matrix = matrix_class(self.width, self.height)
        if self.width == 0:
            return
        axis = line.v * self.height
        self.matrix.insert_vertical_string(0, 0, axis)

