from plotext._system import platform

warning_color = 'orange+'
default_marker = "hd" if platform == 'unix' else 'dot'




class default_terminal():
    width = 211 * 2 // 3
    height = 53 * 2 // 3
    prompt_height = 4

        
class default_figure():
    limit_width = True
    limit_height = True
    size_direction = 1
    interactive = False


class default_settings():
    ticks_color = "black"
    axes_color = "white"
    xaxes = [True, True]
    yaxes = [True, True]
    xfrequency = 5
    yfrequency = 7

    axes = ['x', 'y']
    xsides = ["lower", "upper"] 
    ysides = ["left", "right"]
        
    xside = xsides[0]
    yside = ysides[0]

    scales = ['linear', 'log']
    scale = scales[0]

        
class default_signal():
    marker = 'x'
    color = 'blue+'
    style = None
    fills = [False, True, 'internal']
    fill = fills[0] # same for x and y
    xsides = ["lower", "upper"] # the two possibilities, the first is default
    ysides = ["left", "right"] # the two possibilities, the first is default
    xside = xsides[0]
    yside = ysides[0]
    lines = False

        
class default_placement():
    orientations = ['horizontal', 'vertical']
    orientations_short = ['h', 'v']
    orientations_int = [0, 1]
    orientation = orientations[0]
        
    horizontal_alignments = ['left', 'center', 'right']
    horizontal_alignments_short = ['l', 'c', 'r']
    horizontal_alignments_int = [-1, 0, 1]
    horizontal_alignment = horizontal_alignments[1]
        
    vertical_alignments = ['lower', 'center', 'upper']
    vertical_alignments_short = ['l', 'c', 'u']
    vertical_alignments_int = [-1, 0, 1]
    vertical_alignment = vertical_alignments[1]

        
default_terminal = default_terminal()
default_figure = default_figure()
default_signal = default_signal()
default_placement = dp = default_placement()
default_canvas_color = "white"


def correct_side(axis = None, side = None): 
    sides = default_settings.xsides if axis == 'x' else default_settings.ysides
    is_integer = isinstance(side, int) and 1 <= side <= 2
    not_correct = side is None or (isinstance(side, str) and side.strip() not in sides)
    return sides[side - 1] if is_integer else sides[0] if not_correct else side.strip()

def correct_xside(side = None):
    return correct_side('x', side)

def correct_yside(side = None):
    return correct_side('y', side)

def xside_to_index(xside = None):
    xside = correct_xside(xside)
    return default_settings.xsides.index(xside)

def yside_to_index(yside = None):
    yside = correct_yside(yside)
    return default_settings.ysides.index(yside)


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

# def correct_vertical_alignment(alignment = None):
#     alignment = dp.vertical_alignment if alignment is None else alignment
#     alignment = dp.vertical_alignments[dp.vertical_alignments_short.index(alignment)] if alignment in dp.vertical_alignments_short else alignment
#     alignment = dp.vertical_alignments[dp.vertical_alignments_int.index(alignment)] if alignment in dp.vertical_alignments_int else alignment
#     return dp.vertical_alignment if alignment not in dp.vertical_alignments else alignment

# def get_vertical_alignment_index(alignment = None):
#     alignment = correct_vertical_alignment(alignment)
#     return dp.vertical_alignments.index(alignment)

    
# self.color_sequence = ["blue+", "green+", "red+", "cyan+"]
