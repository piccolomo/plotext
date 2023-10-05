from plotext._default import default_axis, default_xfrequency, default_yfrequency, correct_side
from plotext._color import is_color
from plotext._style import is_style
from plotext._matrix import matrix_class
from plotext._marker import space, border, line, tick
from plotext._ticks import get_labels, linspace, brush, insert_labels
from plotext._canvas import digitize


class axis_class():
    def __init__(self):
        self.set_show_axis()
        self.set_axis_color()
        self.set_size()
        self.backup()

        self.create_lim()
        self.create_ticks()
        self.set_scale()
        self.set_grid()
        self.set_ticks_color()
        self.set_ticks_style()

    def set_show_axis(self, show = None):
        self.show_axis = default_axis.show_axis if show is None else bool(show)

    def set_axis_color(self, color = None):
        color = color if is_color(color) else None
        self.axis_color = default_axis.axis_color if color is None else color

    def set_size(self, width = None, height = None):
        self.width = width
        self.height = height
        self.size = [self.width, self.height]

    def set_width(self, width = None):
        self.set_size(width, self.height)
        
    def set_height(self, height = None):
        self.set_size(self.width, height)
        
    def update_size(self):
        self.set_size(self.width, self.height)

    def copy(self): # to deep copy
        return deepcopy(self)

    def backup(self):
        self.show_axis_backup = self.show_axis

    def restore(self):
        self.show_axis = self.show_axis_backup

    # Ticks Function

    def set_show_ticks(self, show = None):
        self.show_ticks = default_axis.show_ticks if show is None else bool(show)

    def update_show_ticks(self):
        self.show_ticks = not (None in self.lim or self.frequency == 0)

    def set_scale(self, scale = None):
        default_case = (scale is None or scale not in default_axis.scales)
        scale = default_axis.scale if default_case else scale
        self.scale = scale

    def create_lim(self):
        self.min = None; self.max = None
        self.update_lim()
        self.update_show_ticks()

    def set_lim(self, minimum = None, maximum = None):
        self.min = self.min if self.min is not None else minimum
        self.max = self.max if self.max is not None else maximum
        self.update_lim()
        self.update_show_ticks()

    def update_lim(self):
        self.lim = (self.min, self.max)

    def create_ticks(self):
        ticks = linspace(*self.lim, self.frequency) if None not in self.lim else []
        self.set_ticks(ticks)

    def set_ticks(self, ticks = None, labels = None):
        ticks = [] if ticks is None else list(ticks)
        labels = get_labels(ticks) if labels is None else list(map(str, labels))
        ticks, labels = brush(ticks, labels)
        self.ticks = ticks
        self.labels = labels
        self.labels_width = 0 if len(labels) == 0 else len(labels[0])
        self.set_frequency(len(ticks))

    def set_default_frequency(self, frequency = None):
        self.default_frequency = frequency
        
    def set_frequency(self, frequency = None):
        self.frequency = self.default_frequency if frequency is None else int(frequency)
        self.update_show_ticks()

    def set_direction(self, reverse = None):
        self.direction = default_axis.direction if reverse is None else 2 * int(not reverse) - 1

    def set_grid(self, grid = None):
        self.grid = default_axis.grid if grid is None else bool(horizontal)

    def set_ticks_color(self, color = None):
        color = color if is_color(color) else None
        self.ticks_color = default_axis.ticks_color if color is None else color

    def set_ticks_style(self, style = None):
        style = style if is_style(style) else None
        self.ticks_style = default_axis.ticks_style if style is None else clean_styles(style)


        
class xaxis_class(axis_class):
    def __init__(self, side = None):
        super().__init__()
        self.axis = 'x'
        self.side = correct_xside(side)
        self.update_borders()
        self.update_ticks()

        self.set_default_frequency(default_xfrequency)
        self.set_frequency()

        self.set_widths()
        self.update_relative_ticks()


# Size  Functions

    def set_widths(self, left = None, canvas = None, right = None):
        self.width_left = left
        self.width_canvas = canvas
        self.width_right = right
        self.width = left + canvas + right if None not in [left, canvas, right] else None
        self.update_size()

    def update_height(self):
        self.set_height(int(self.show_axis) + int(self.show_axis))

# Build Functions
    
    def update_borders(self):
        self.border_left = border.upper_left if self.side == default_axis.xside else border.lower_left
        self.border_right = border.upper_right if self.side == default_axis.xside else border.lower_right

    def update_ticks(self):
        self.tick_partial = tick.upper if self.side == default_axis.xside else tick.lower
        self.tick_full = tick.cross
    
    def get_axis_string(self):
        left_axis = space * (self.width_left - 1) + self.border_left * int(self.width_left > 0)
        axis = line.h * self.width_canvas
        axis = insert_labels(axis, [self.tick_full] * self.frequency, self.rticks)
        right_axis = self.border_right * int(self.width_right > 0) + space * (self.width_right - 1) 
        return left_axis + axis + right_axis
    
    def update_relative_ticks(self):
        self.rticks = digitize(self.ticks, self.lim, self.width_canvas)

    def get_ticks_string(self):
        axis = space * self.width
        rticks = [el + self.width_left for el in self.rticks]
        axis = insert_labels(axis, self.labels, rticks)
        return axis
        
    def update_matrix(self):
        self.matrix = matrix_class(self.width, self.height)
        self.matrix.insert_row(self.get_axis_string(), 0) if self.show_axis else None
        self.matrix.insert_row(self.get_ticks_string(), 1) if self.show_ticks else None

    def clear(self):
        self.__init__(self.side)


class yaxis_class(axis_class):
    def __init__(self, side = None):
        self.axis = 'y'
        self.side = correct_yside(side)
        super().__init__()

        self.set_default_frequency(default_yfrequency)
        self.set_frequency()

        #self.update_relative_ticks()

    def set_height(self, height = None):
        self.height = int(height) if height is not None else None

    def update_width(self):
        self.set_width(int(self.show_axis))

    def get_axis_string(self):
        axis = line.v * self.height
        return axis

    def update_matrix(self):
        self.matrix = matrix_class(self.width, self.height)
        self.matrix.insert_col(self.get_axis_string(), 0) if self.show_axis else None

    def clear(self):
        self.__init__(self.side)


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
