from plotext._default import default_axis
from plotext._color import is_color
from plotext._matrix import matrix_class
from plotext._marker import space, border, line
from copy import deepcopy

class axis_class():
    def __init__(self):
        self.set_show()
        self.set_axis_color()
        self.set_size()

    def set_show(self, show = None):
        self.show = default_axis.show if show is None else bool(show)

    def set_axis_color(self, color = None):
        color = color if is_color(color) else None
        self.axis_color = default_axis.axis_color if color is None else color

    def set_size(self, width = None, height = None):
        self.width = width
        self.height = height
        self.size = [width, height]
        
    def update_size(self):
        self.set_size(self.width, self.height)

    def copy(self): # to deep copy 
        return deepcopy(self)


class xaxis_class(axis_class):
    def __init__(self, side = None):
        super().__init__()
        self.axis = 'x'
        self.side = self.correct_side(side)
        self.update_borders()

    def correct_side(self, side = None): 
        sides = default_axis.xsides
        is_integer = isinstance(side, int) and 1 <= side <= 2
        not_correct = side is None or (isinstance(side, str) and side.strip() not in sides)
        return sides[side - 1] if is_integer else sides[0] if not_correct else side.strip()

# Size  Functions

    def set_widths(self, left = None, canvas = None, right = None):
        self.width_left = left
        self.width_canvas = canvas
        self.width_right = right
        self.width = left + canvas + right
        self.update_size()

    def update_height(self):
        self.height = int(self.show)
        self.update_size()


# Build Functions
    
    def update_borders(self):
        self.left_border = border.upper_left if self.side == default_axis.xside else border.lower_left
        self.right_border = border.upper_right if self.side == default_axis.xside else border.lower_right
    
    def get_axis_string(self):
        axis  = space * (self.width_left - 1) 
        axis += self.left_border * int(self.width_left > 0)
        axis += line.h * self.width_canvas
        axis += self.right_border * int(self.width_right > 0)
        axis += space * (self.width_right - 1) 
        return axis
    
    def update_matrix(self):
        self.matrix = matrix_class(self.width, self.height)
        self.matrix.insert_row(self.get_axis_string(), 0) if self.show else None


class yaxis_class(axis_class):
    def __init__(self, side = None):
        self.axis = 'y'
        self.side = self.correct_side(side)
        super().__init__()

    def correct_side(self, side = None): 
        sides = default_axis.ysides
        is_integer = isinstance(side, int) and 1 <= side <= 2
        not_correct = side is None or (isinstance(side, str) and side.strip() not in sides)
        return sides[side - 1] if is_integer else sides[0] if not_correct else side.strip()

    def set_height(self, height = None):
        self.height = int(height) if height is not None else None

    def update_width(self):
        self.width = int(self.show)
        self.update_size()

    def get_axis_string(self):
        axis = line.v * self.height
        return axis
    
    def update_matrix(self):
        self.matrix = matrix_class(self.width, self.height)
        self.matrix.insert_col(self.get_axis_string(), 0) if self.show else None

space = ' '
def only_spaces(string): # it returns True if string is made of only empty spaces or is None or ''
    return (type(string) == str) and (string == len(string) * space) #and len(string) != 0

def insert(data, index, element):
    data[index] = element



