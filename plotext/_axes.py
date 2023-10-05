from plotext._default import default_axis, correct_side
from plotext._color import is_color
from plotext._style import is_style
from plotext._matrix import matrix_class
from plotext._marker import space, border, line, tick
from plotext._canvas import digitize
from copy import deepcopy as copy

class axis_class():
    def set_axis_color(self, color = None):
        color = color if is_color(color) else None
        self.axis_color = default_axis.axis_color if color is None else color

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
        if self.height == 0:
            return
        axis = line.h * self.width_canvas
        self.matrix.insert_horizontal_string(0, self.width_left, axis)
        self.matrix.insert_element(0, self.width_left - 1, self.border_left) if self.width_left > 0 else None
        self.matrix.insert_element(0, self.width_left + self.width_canvas, self.border_right) if self.width_right > 0 else None



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

space = ' '

def only_spaces(string): # it returns True if string is made of only empty spaces or is None or ''
    return (type(string) == str) and (string == len(string) * space) # and len(string) != 0

# def insert(data, index, element):
#     data[index] = element



def correct_xside(side = None):
    return correct_side('x', side)

def correct_yside(side = None):
    return correct_side('y', side)




# def add_horizontal_string(self, col, row, string, fullground = None, style = None, background = None, alignment = "left", check_space = False, check_canvas = False):
#         l = len(string); L = range(l)
#         col = col if alignment == "left" else col - l // 2 if alignment == "center" else col - l + 1 if alignment == "right" else ut.correct_coord(self.get_marker_row(row), string, col) # if dynamic
#         b, e = max(col - 1, 0), min(col + l + 1, self.cols)
#         test_space = all([self.get_marker(c, row) == ut.space for c in range(b, e)]) and col >= 0 and col + l <= self.cols if check_space else True
#         [self.insert_element(col + i, row, string[i], fullground, style, background, check_canvas) for i in L] if test_space else None
#         return test_space


