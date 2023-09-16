from plotext._default import default_axis, default_xfrequency, default_yfrequency
from plotext._color import is_color
from plotext._style import clean_styles, is_style
from plotext._ticks import get_labels, brush
from plotext._matrix import matrix_class
from plotext._marker import border, line

class axis_class():
    def __init__(self):
        self.set_left_label()
        self.set_center_label()
        self.set_right_label()
        self.set_lim()
        self.set_scale()
        
        self.set_ticks()
        self.set_direction()
        
        self.set_grid()
        
        self.set_axis_color()
        self.set_ticks_color()
        self.set_ticks_style()
        self.set_show_axis()

        self.set_size()

        # self.data = []
        # self.data_type = None
        # self.lines = []

##############################################
#######    External Set Functions    #########
##############################################

    def set_show_axis(self, show = None):
        self.show_axis = default_axis.show if show is None else bool(show)

    def set_left_label(self, label = None):
        self.left_label = self.correct_label(label)
        self.show_left_label = self.left_label is not None

    def set_center_label(self, label = None):
        self.center_label = self.correct_label(label)
        self.show_center_label = self.center_label is not None

    def set_right_label(self, label = None):
        self.right_label = self.correct_label(label)
        self.show_right_label = self.right_label is not None

    def set_lim(self, minimum = None, maximum = None):
        minimum = None if minimum is None else float(minimum)
        maximum = None if maximum is None else float(maximum)
        xlim = [minimum, maximum]
        xlim = xlim if None in xlim else [min(xlim), max(xlim)]
        self.lim = xlim

    def set_scale(self, scale = None):
        default_case = (scale is None or scale not in default_axis.scales)
        scale = default_axis.scale if default_case else scale
        self.scale = scale

    def set_ticks(self, ticks = None, labels = None):
        ticks = [] if ticks is None else list(ticks)
        labels = get_labels(ticks) if labels is None else list(map(str, labels))
        ticks, labels = brush(ticks, labels)
        self.ticks = ticks
        self.labels = labels
        self.labels_width = 0 if len(labels) == 0 else len(labels[0])
        self.set_frequency(len(ticks))

    def set_frequency(self, frequency = None):
        self.frequency = self.default_frequency if frequency is None else int(frequency)
        self.show_ticks = self.frequency != 0

    def set_direction(self, reverse = None):
        self.direction = default_axis.direction if reverse is None else 2 * int(not reverse) - 1

    def set_grid(self, grid = None):
        self.grid = default_axis.grid if grid is None else bool(horizontal)

    def set_axis_color(self, color = None):
        color = color if is_color(color) else None
        self.axis_color = default_axis.axis_color if color is None else color
        
    def set_ticks_color(self, color = None):
        color = color if is_color(color) else None
        self.ticks_color = default_axis.ticks_color if color is None else color

    def set_ticks_style(self, style = None):
        style = style if is_style(style) else None
        self.ticks_style = default_axis.ticks_style if style is None else clean_styles(style)

    def correct_label(self, label = None): 
        label = None if label is None else str(label).strip()
        spaces = only_spaces(label)
        label = None if spaces else label 
        return label
    
    def set_size(self, width = None, height = None):
        [self.width, self.height] = [width, height]
        self.update_size()

    def update_size(self):
        self.size = [self.width, self.height]

    def set_height(self, height = None):
        self.height = int(height) if height is not None else None
        self.update_size()

    def set_width(self, width = None):
        self.width = int(width) if width is not None else None
        self.update_size()

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def create_matrix(self):
        self.matrix = matrix_class(self.width, self.height)
        

class xaxis_class(axis_class):
    def __init__(self, side = None):
        self.axis = 'x'
        self.side = self.correct_side(side)
        self.default_frequency = default_xfrequency
        super().__init__()
        self.update_borders()

    def correct_side(self, side = None): 
        sides = default_axis.xsides
        is_integer = isinstance(side, int) and 1 <= side <= 2
        not_correct = side is None or (isinstance(side, str) and side.strip() not in sides)
        return sides[side - 1] if is_integer else sides[0] if not_correct else side.strip()

    def update_borders(self):
        self.left_border = border.upper_left if self.side == default_axis.xside else border.lower_left
        self.right_border = border.upper_right if self.side == default_axis.xside else border.lower_right
        
    def update_height(self):
        show_label = self.show_left_label or self.show_center_label or self.show_right_label
        self.height = int(show_label) + int(self.show_ticks) + int(self.show_axis)

    def set_width_canvas(self, width = None):
        self.width_canvas = int(width) if width is not None else None

    def get_axis(self):
        axis = [line.h] * self.width
        insert(axis, 0, self.left_border) if self.width_canvas > 1 else None
        insert(axis, -1, self.right_border) if self.width_canvas > 2 else None
        return axis
    
    def build_matrix(self):
        self.create_matrix()
        self.matrix.insert_row(0, self.get_axis())

    

class yaxis_class(axis_class):
    def __init__(self, side = None):
        self.axis = 'y'
        self.side = self.correct_side(side)
        self.default_frequency = default_yfrequency
        super().__init__()

    def correct_side(self, side = None): 
        sides = default_axis.ysides
        is_integer = isinstance(side, int) and 1 <= side <= 2
        not_correct = side is None or (isinstance(side, str) and side.strip() not in sides)
        return sides[side - 1] if is_integer else sides[0] if not_correct else side.strip()

    def update_width(self):
        self.width = self.labels_width + int(self.show_axis)

    def get_axis(self):
        axis = [line.v] * self.height
        return axis
    
    def build_matrix(self):
        self.create_matrix()
        self.matrix.insert_col(0, self.get_axis())

space = ' '
def only_spaces(string): # it returns True if string is made of only empty spaces or is None or ''
    return (type(string) == str) and (string == len(string) * space) #and len(string) != 0

def insert(data, index, element):
    data[index] = element



