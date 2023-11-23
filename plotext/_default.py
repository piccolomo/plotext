from plotext._system import platform
#from plotext._marker import default_marker
#from plotext._style import no_style


class default_terminal():
    def __init__(self):
        self.set_size()
        self.prompt_height = 4

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


class default_settings():
    ticks_color = "black"
    axes_color = "white"
        
# self.color_sequence = ["blue+", "green+", "red+", "cyan+"]
        
class default_signal():
    def __init__(self):
        self.marker = 'x'
        self.color = 'blue+'
        self.style = None
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
        self.orientations_int = [0, 1]
        self.orientation = self.orientations[0]
        
        self.horizontal_alignments = ['left', 'center', 'right']
        self.horizontal_alignments_short = ['l', 'c', 'r']
        self.horizontal_alignments_int = [-1, 0, 1]
        self.horizontal_alignment = self.horizontal_alignments[1]
        
        self.vertical_alignments = ['lower', 'center', 'upper']
        self.vertical_alignments_short = ['l', 'c', 'u']
        self.vertical_alignments_int = [-1, 0, 1]
        self.vertical_alignment = self.vertical_alignments[1]

        
class default_axis():
    def __init__(self):
        self.axes = ['x', 'y']
        self.xsides = ["lower", "upper"] 
        self.ysides = ["left", "right"]
        
        self.axis = self.axes[0]
        self.xside = self.xsides[0]
        self.yside = self.ysides[0]
        
        self.color = "white"
        self.style = "default"

        self.grid = False


class default_ticks():
    def __init__(self):
        self.color = 'white'
        self.style = 'default'
        
        self.scales = ['linear', 'log']
        self.scale = 'linear'

        self.direction = 1 



default_terminal = default_terminal()
default_figure = default_figure()
default_signal = default_signal()
default_placement = dp = default_placement()
default_axis = default_axis()
default_ticks = default_ticks()
default_xfrequency = 5
default_yfrequency = 7
default_canvas_color = "white"


def correct_side(axis = None, side = None): 
    sides = default_axis.xsides if axis == 'x' else default_axis.ysides
    is_integer = isinstance(side, int) and 1 <= side <= 2
    not_correct = side is None or (isinstance(side, str) and side.strip() not in sides)
    return sides[side - 1] if is_integer else sides[0] if not_correct else side.strip()

def correct_xside(side = None):
    return correct_side('x', side)

def correct_yside(side = None):
    return correct_side('y', side)

def correct_orientation(orientation = None):
    orientation = dp.orientation if orientation is None else orientation
    orientation = dp.orientations[dp.orientations_short.index(orientation)] if orientation in dp.orientations_short else orientation
    return dp.orientation if orientation not in dp.orientations else orientation

def correct_horizontal_alignment(alignment = None):
    alignment = dp.horizontal_alignment if alignment is None else alignment
    alignment = dp.horizontal_alignments[dp.horizontal_alignments_short.index(alignment)] if alignment in dp.horizontal_alignments_short else alignment
    alignment = dp.horizontal_alignments[dp.horizontal_alignments_int.index(alignment)] if alignment in dp.horizontal_alignments_int else alignment
    return dp.horizontal_alignment if alignment not in dp.horizontal_alignments else alignment

def get_horizontal_alignment_index(alignment = None):
    alignment = correct_horizontal_alignment(alignment)
    return dp.horizontal_alignments.index(alignment)

def correct_vertical_alignment(alignment = None):
    alignment = dp.vertical_alignment if alignment is None else alignment
    alignment = dp.vertical_alignments[dp.vertical_alignments_short.index(alignment)] if alignment in dp.vertical_alignments_short else alignment
    alignment = dp.vertical_alignments[dp.vertical_alignments_int.index(alignment)] if alignment in dp.vertical_alignments_int else alignment
    return dp.vertical_alignment if alignment not in dp.vertical_alignments else alignment

def get_vertical_alignment_index(alignment = None):
    alignment = correct_vertical_alignment(alignment)
    return dp.vertical_alignments.index(alignment)


        




