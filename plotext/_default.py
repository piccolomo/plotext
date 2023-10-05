from plotext._global import platform
from plotext._marker import default_marker
from plotext._color import default_color, default_color_sequence
from plotext._style import default_style


class default_terminal():
    def __init__(self):
        self.set_size()
        self.prompt_height = 3

    def set_size(self, width = None, height = None):
        self.width = 211 * 2 // 3 if width is None else int(width)
        self.height = 53 * 2 // 3 if height is None else int(height)
        self.size = [self.width, self.height]

        
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
        self.style = default_style
        self.fills = [False, True, 'internal']
        self.fill = self.fills[0] # same for x and y
        self.xsides = ["lower", "upper"] # the two possibilities, the first is default
        self.ysides = ["left", "right"] # the two possibilities, the first is default
        self.xside = self.xsides[0]
        self.yside = self.ysides[0]
        self.lines = False

class default_placement():
    def __init__(self):
        self.orientations = ['horizontal', 'vertical']
        self.orientations_short = ['h', 'v']
        self.orientation = self.orientations[0]
        
        self.horizontal_alignments = ['left', 'center', 'right']
        self.horizontal_alignments_short = ['l', 'c', 'r']
        self.horizontal_alignment = self.horizontal_alignments[1]
        
        self.vertical_alignments = ['lower', 'center', 'upper']
        self.vertical_alignments_short = ['l', 'c', 'u']
        self.vertical_alignment = self.vertical_alignments[1]

        
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
        self.ticks_style = "default"

        self.direction = 1 
        self.scales = ['linear', 'log']
        self.scale = 'linear'
        self.grid = False
        self.show_axis = True
        self.show_ticks = True


default_terminal = default_terminal()
default_figure = default_figure()
default_signal = default_signal()
default_placement = dp = default_placement()
default_axis = default_axis()
default_xfrequency = 5
default_yfrequency = 7
default_canvas_color = "white"


def correct_side(axis = None, side = None): 
    sides = default_axis.xsides if axis == 'x' else default_axis.ysides
    is_integer = isinstance(side, int) and 1 <= side <= 2
    not_correct = side is None or (isinstance(side, str) and side.strip() not in sides)
    return sides[side - 1] if is_integer else sides[0] if not_correct else side.strip()

def correct_orientation(orientation = None):
    orientation = dp.orientation if orientation is None else orientation
    orientation = dp.orientations[dp.orientations_short.index(orientation)] if orientation in dp.orientations_short else orientation
    return dp.orientation if orientation not in dp.orientations else orientation

def correct_horizontal_alignment(alignment = None):
    alignment = dp.horizontal_alignment if alignment is None else alignment
    alignment = dp.horizontal_alignments[dp.horizontal_alignments_short.index(alignment)] if alignment in dp.horizontal_alignments_short else alignment
    return dp.horizontal_alignment if alignment not in dp.horizontal_alignments else alignment

def correct_vertical_alignment(alignment = None):
    alignment = dp.vertical_alignment if alignment is None else alignment
    alignment = dp.vertical_alignments[dp.vertical_alignments_short.index(alignment)] if alignment in dp.vertical_alignments_short else alignment
    return dp.vertical_alignment if alignment not in dp.vertical_alignments else alignment


