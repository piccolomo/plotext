from plotext._global import platform
from plotext._marker import default_marker
from plotext._color import default_color, default_color_sequence, no_color
from plotext._style import default_style

class default_terminal():
    def __init__(self):
        self.set_size()
        self.set_infinite_size()

    def set_size(self, width = None, height = None):
        self.width = 211 * 2 // 3 if width is None else int(width)
        self.height = 53 * 2 // 3 if height is None else int(height)
        self.size = [self.width, self.height]

    def set_infinite_size(self, width = None, height = None):
        m = 5
        self.infinite_width = m * self.width if width is None else int(width)
        self.infinite_height = m * self.height if height is None else int(height)
        self.infinite_size = [self.infinite_width, self.infinite_height]

class default_figure():
    def __init__(self):
        self.set_limitsize()
        self.size_direction = 1

    def set_limitsize(self, limit_width = None, limit_height = None):
        self.limit_width = True if limit_width is None else bool(limit_width)
        self.limit_height = True if limit_height is None else bool(limit_height)
        self.limit_size = [self.limit_width, self.limit_height]

class default_signal():
    def __init__(self):
        self.marker = default_marker
        self.color = default_color
        self.color_sequence = default_color_sequence
        self.style = default_style
        self.fills = [False, True, 'internal']
        self.fill = self.fills[0] # same for x and y
        self.xsides = ["lower", "upper"] # the two possibilities, the first is default
        self.ysides = ["left", "right"] # the two possibilities, the first is default
        self.xside = self.xsides[0]
        self.yside = self.ysides[0]
        self.lines = False

class default_axis():
    def __init__(self):
        self.axes = ['x', 'y']
        self.xsides = ["lower", "upper"] 
        self.ysides = ["left", "right"]
        
        self.axis = self.axes[0]
        self.xside = self.xsides[0]
        self.yside = self.ysides[0]
        
        self.axis_color = "white"
        self.ticks_color = "black"
        self.ticks_style = no_color

        self.direction = 1 
        self.scales = ['linear', 'log']
        self.scale = 'linear'
        self.grid = False
        self.show = True


default_terminal = default_terminal()
default_figure = default_figure()
default_signal = default_signal()
default_axis = default_axis()
default_xfrequency = 5
default_yfrequency = 7
default_canvas_color = "white"



