from re import sub

from plotext._methods.object import *
from plotext._methods.list import repeat, replace_none, is_list_like
from plotext._methods.string import only_spaces
from plotext._constants import *
from plotext._colorize import colorize as colorize_class
from plotext._pixel import pixel as pixel_class
from plotext._marker import marker as marker_class


class correct_class:

    # Correct pixel object using defaults
    @staticmethod
    def pixel(pixel, default_pixel):
        if pixel is None:
            return default_pixel
        if isinstance(pixel, str):
            return pixel_class(pixel)
        if isinstance(pixel, list):
            return pixel_class(*pixel)
        return pixel

    # Convert string or colorize object to matrix
    @staticmethod
    def matrix(obj):
        if isinstance(obj, colorize_class):
            return obj.get_matrix()
        if isinstance(obj, str):
            return colorize_class(obj).get_matrix()
        return obj

    # Adjust slice boundaries
    @staticmethod
    def slice(key, bins):
        if isinstance(key, int):
            key = slice(key, key + 1)
        if key.start is None:
            key = slice(0, key.stop)
        if key.stop is None:
            key = slice(key.start, bins)
        return key

    # Correct orientation
    @staticmethod
    def orientation(orientation):
        return orientation if orientation in orientations + orientations_short else orientations[0]

    # Horizontal alignment correction
    @staticmethod
    def ha(alignement):
        if alignement in ha:
            return ha.index(alignement) - 1
        if alignement in ha_short:
            return alignement
        return -1

    # Vertical alignment correction
    @staticmethod
    def va(alignement):
        if alignement in va:
            return va.index(alignement) - 1
        if alignement in ha_short:
            return alignement
        return 1

    # Clean and capitalize doc string
    @staticmethod
    def doc(doc, capitalize=1):
        doc = doc.strip()
        if doc and doc[-1] != '.':
            doc += '.'
        doc = sub(r'\s+', ' ', doc)
        return doc[0].upper() + doc[1:] if capitalize else doc[0].lower() + doc[1:]

    # Validate limits alignment
    @staticmethod
    def limits_alignment(alignment):
        return alignment if alignment in limit_alignments else limit_alignments[0]

    # Validate direction
    @staticmethod
    def limits_direction(direction):
        return bool(direction) if direction in directions else directions[1]

    # Validate scale
    @staticmethod
    def scale(scale):
        return scale if scale in scales else scales[0]

    # Correct single label
    @staticmethod
    def label(label, default_pixel):
        if label is None or only_spaces(label):
            return None
        if isinstance(label, str):
            label = colorize_class(label.strip()).set_pixel(default_pixel)
        label._fix_background(default_pixel)
        return label

    # Correct list of labels
    @staticmethod
    def labels(labels, default_pixel):
        return [correct_class.label(label, default_pixel) for label in labels]

    # Correct side(s) input
    @staticmethod
    def axes(axis):
        if axis is None:
            side_list = r2
        elif is_list_like(axis):
            side_list = axis
        else:
            side_list = [axis]
        return [correct_class.axis(a) for a in side_list]

    # Correct single axis
    @staticmethod
    def axis(axis):
        return correct_class.boolean_string(axis, axis_names)

    # Correct axis side
    @staticmethod
    def side(axis, side):
        sides = ysides if axis else xsides
        return correct_class.boolean_string(side, sides)

    # Correct sides list
    @staticmethod
    def sides(axis, side):
        if side is None:
            side_list = [0]
        elif is_list_like(side):
            side_list = side
        else:
            side_list = [side]
        return [correct_class.side(axis, s) for s in side_list]

    # Validate status
    @staticmethod
    def status(value, default):
        return value if value is not None else default

    # Validate axis style
    @staticmethod
    def axis_style(style):
        return style if style in axis_styles else axis_styles[0]

    # Correct boolean/string side
    @staticmethod
    def boolean_string(side, sides, sides_short=None):
        if side is None:
            side = sides[0]
        elif isinstance(side, str):
            side = side.strip()
        if side in sides:
            side = sides.index(side)
        if sides_short and side in sides_short:
            side = sides_short.index(side)
        if not (isinstance(side, int) and side in range(2)):
            side = 0
        return side

    # Format x and y data lists
    @staticmethod
    def data(x=None, y=None):
        if x is None and y is None:
            x, y = [], []
        elif x is not None and y is None:
            y, x = x, list(range(1, len(x) + 1))
        elif is_numerical(x) and not is_numerical(y):
            x = [x] * len(y)
        elif is_numerical(y) and not is_numerical(x):
            y = [y] * len(x)
        l = min(len(x), len(y))
        return [list(x[:l]), list(y[:l])]

    # Correct single marker
    @staticmethod
    def marker(marker, default_marker):
        marker = default_marker if marker is None else marker_class(marker) if isinstance(marker, str) else marker
        return marker._fix(default_marker)

    # Correct list of markers
    @staticmethod
    def markers(marker, default_marker, length):
        if not is_list_like(marker):
            marker = [marker]
        marker = [correct_class.marker(m, default_marker) for m in marker]
        return repeat(marker, length)

    # Correct limits
    @staticmethod
    def limits(limits, new_limits):
        new_limits = limits if new_limits is None else new_limits
        limits = replace_none(limits, new_limits)
        a, b = limits
        return [a - 1, b + 1] if a == b and a is not None else limits

    # Correct line style
    @staticmethod
    def line_style(style):
        return style if style in line_styles else line_styles[0]

    # Signal label default
    @staticmethod
    def signal_label(label):
        return "xxxxxx" if label is None else label.strip()

    # Legend label default
    @staticmethod
    def legend_label(label, length):
        return f'signal[{length}]' if len(label) == 0 else label

    # Validate boolean
    @staticmethod
    def bool(element=None):
        return element if isinstance(element, bool) or element in r2 else False

    # Validate line method
    @staticmethod
    def line_method(method=None):
        return method if method not in line_methods or method not in r2 else 0
