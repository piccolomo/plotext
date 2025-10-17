from re import sub

from plotext._methods import *
#from plotext._default import default_labels_pixel, default_axis_pixel, default_ruler_pixel
from plotext._constants import *
from plotext._colorize import colorize as colorize_class
from plotext._marker import marker as marker_class
from plotext._pixel import pixel


class correct_class:

    # Correct the pixel object, filling missing properties with defaults
    @staticmethod
    def pixel(pixel, default_pixel):
        if pixel is None:
            return default_pixel
        if isinstance(pixel, str):
            return pixel_class(pixel)
        if isinstance(pixel, list):
            return pixel_class(*pixel)
        return pixel


    # Correct matrix object by checking its type and converting if necessary
    @staticmethod
    def matrix(obj):
        if isinstance(obj, colorize_class):
            return obj.get_matrix()
        if isinstance(obj, str):
            return colorize_class(obj).get_matrix()
        return obj


    # Adjust slice depending on key type and slice boundaries
    @staticmethod
    def slice(key, bins):
        if isinstance(key, int):
            key = slice(key, key + 1)
        if key.start is None:
            key = slice(0, key.stop)
        if key.stop is None:
            key = slice(key.start, bins)
        return key


    # Correct horizontal alignment by checking against valid values
    @staticmethod
    def ha(alignement):
        if alignement in ha:
            return ha.index(alignement) - 1
        if alignement in ha_short:
            return alignement
        return -1


    # Correct vertical alignment by checking against valid values
    @staticmethod
    def va(alignement):
        if alignement in va:
            return va.index(alignement) - 1
        if alignement in ha_short:
            return alignement
        return 1


    # Corrects the docstring by formatting and capitalizing if needed
    @staticmethod
    def doc(doc, capitalize = 1):
        doc = doc.strip()
        if len(doc) > 0 and doc[-1] != '.':
            doc += '.'
        doc = sub(r'\s+', ' ', doc)
        if capitalize:
            doc = doc[0].upper() + doc[1:]
        else:
            doc = doc[0].lower() + doc[1:]
        return doc


    # Correct the alignment of limits to ensure it is valid
    @staticmethod
    def limits_alignment(alignment):
        if alignment is None or alignment not in limit_alignments:
            return limit_alignments[0]
        return alignment


    # Correct the direction to ensure it is valid
    @staticmethod
    def limits_direction(direction):
        direction = directions[1] if direction is None or direction not in directions else bool(direction)
        return direction


    # Correct the scale to ensure it is valid
    @staticmethod
    def scale(scale):
        if scale is None or scale not in scales:
            return scales[0]
        return scale


    # # Correct the pixel for rulers
    # @staticmethod
    # def ruler_pixel(pixel):
    #     return correct_class.pixel(pixel, default_ruler_pixel)


    # Correct a single label, applying default pixel settings
    @staticmethod
    def label(label, default_pixel):
        if label is None or string_methods.only_spaces(label):
            return None
        if isinstance(label, str): 
            label = colorize(label.strip()).set_pixel(default_pixel)
        #and label._no_background():
        label._fix_background(default_pixel)
        return label


    # Correct a list of labels
    @staticmethod
    def labels(labels, default_pixel):
        return [correct_class.label(label, default_pixel) for label in labels]

    # Correct side input to a list of valid side values
    @staticmethod
    def axes(axis):
        if axis is None:
            side_list = r2
        elif object_methods.is_list_like(axis):
            side_list = axis
        else:
            side_list = [axis]
        return [correct_class.axis(a) for a in side_list]


    # Correct a single axis string or boolean
    @staticmethod
    def axis(axis):
        return correct_class.boolean_string(axis, axis_names)

    # Correct the side of an axis to ensure it is valid
    @staticmethod
    def side(axis, side):
        sides = ysides if axis else xsides
        return correct_class.boolean_string(side, sides)

    # # Correct axis input to a list of valid axis values
    # @staticmethod
    # def axis(axis = None):
    #     if axis is None:
    #         axis_list = r2
    #     elif object_methods.is_list_like(axis):
    #         axis_list = axis
    #     else:
    #         axis_list = [axis]
    #     return [correct_class.single_axis(a) for a in axis_list]


    # Correct side input to a list of valid side values
    @staticmethod
    def sides(axis, side):
        if side is None:
            side_list = r2
        elif object_methods.is_list_like(side):
            side_list = side
        else:
            side_list = [side]
        return [correct_class.side(axis, s) for s in side_list]


    @staticmethod
    def status(value, default):
        return value if value is not None else default

    # Correct the axis style to ensure it is valid
    @staticmethod
    def axis_style(style):
        return style if style in axis_styles else axis_styles[0]


    # # Correct axis pixel with default axis pixel
    # axis_pixel = staticmethod(lambda pixel = None: correct_class.pixel(pixel, default_axis_pixel))


    # Correct a boolean or string side to ensure it is valid
    @staticmethod
    def boolean_string(side, sides, sides_short = None):
        if side is None:
            side = sides[0]
        elif isinstance(side, str):
            side = side.strip()
        if side in sides:
            side = sides.index(side)
        if sides_short is not None and side in sides_short:
            side = sides_short.index(side)
        if not (isinstance(side, int) and side in range(2)):
            side = 0
        return side


    # Format x and y data lists properly
    @staticmethod
    def data(x = None, y = None):
        if x is None and y is None:
            x, y = [], []
        elif x is not None and y is None:
            y = x
            x = list(range(1, len(y) + 1))
        elif object_methods.is_numerical(x) and not object_methods.is_numerical(y):
            x = [x] * len(y)
        elif object_methods.is_numerical(y) and not object_methods.is_numerical(x):
            y = [y] * len(x)
        lx, ly = len(x), len(y)
        if lx != ly:
            l = min(lx, ly)
            x = x[:l]
            y = y[:l]
        return [list(x), list(y)]


    # Correct a single marker, wrapping it into a marker object if needed
    @staticmethod
    def marker(marker, default_marker):
        if marker is None:
            return default_marker
        if isinstance(marker, str):
            return marker_class(marker)._fix(default_marker)
        if isinstance(marker, list):
            return marker_class(*marker)._fix(default_marker)
        return marker

    # Correct a list of markers, repeating them to match the specified length
    @staticmethod
    def markers(marker, default_marker, length):
        if not isinstance(marker, list):
            marker = [marker]
        marker = [correct_class.marker(m, default_marker) for m in marker]
        return list_methods.repeat(marker, length)

    # Correct the limits by combining the current and new limits
    @staticmethod
    def limits(limits, new_limits):
        new_limits = limits if new_limits is None else new_limits
        limits = list_methods.replace_none(limits, new_limits)
        [a, b] = limits
        limits = [a - 1, b + 1] if a == b and a is not None else limits
        #minimum = min(limits[0], new_limits[0]) if new_limits[0] is not None else limits[0]
        #maximum = max(limits[1], new_limits[1]) if new_limits[1] is not None else limits[1]
        return limits

    # Correct the line style to ensure it is valid
    @staticmethod
    def line_style(style):
        return style if style in line_styles else line_styles[0]

    @staticmethod
    def label(label, default_pixel):
        if label is None or string_methods.only_spaces(label):
            return None
        if isinstance(label, str): 
            label = colorize_class(label.strip()).set_pixel(default_pixel)
        #and label._no_background():
        label._fix_background(default_pixel)
        return label


    @staticmethod
    def signal_label(label): 
        return "xxxxxx" if label is None else label.strip() 

    # @staticmethod
    # def signal_label(label, length):
    #     return f"signal[{length}]" if label is None else label

    # Create signal label, defaulting to 'signal(length)' if label is None 
    @staticmethod
    def legend_label(label, length): 
        return f'signal[{length}]' if len(label) == 0 else label


    @staticmethod
    def bool(element = None):
        return element if isinstance(element, bool) or element in r2 else False