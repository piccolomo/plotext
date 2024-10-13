from ._utility import *
from ._colorize import colorize
from ._pixel import pixel as pixel_class
from ._marker import marker as marker_class
from ._constants import *


def correct_axis_style(style):
	return style if style in axis_styles else axis_styles[0]

def correct_single_marker(marker):
	return marker if isinstance(marker, marker_class) else marker_class(marker)

def correct_marker(marker, length):
	marker = marker if isinstance(marker, list) else [marker]
	marker = [correct_single_marker(el) for el in marker]
	return repeat(marker, length)

def correct_pixel(pixel, default):
	default_pixel = lambda: pixel_class(*default)
	pixel = default_pixel() if pixel is None else pixel_class(pixel) if isinstance(pixel, str) else pixel
	pixel._copy_background(default_pixel()) if pixel is not None and pixel._no_background() else None
	return pixel

def correct_label(label, default_pixel):
	label = None if label is None or only_spaces(label) else colorize(str(label).strip()).set_pixel(default_pixel) if isinstance(label, str) else label
	label._copy_background(default_pixel) if label is not None and label._no_background() else None
	return label

def correct_labels(labels, default_pixel):
	return [correct_label(label, default_pixel) for label in labels]

def correct_boolean_string(side, sides):
	side = sides[0] if side is None else side.strip() if isinstance(side, str) else side
	side = sides.index(side) if side in sides else side
	side = side if isinstance(side, int) and side in range(2) else 0
	return side

correct_axis = lambda axis = None: correct_boolean_string(axis, axes)

def correct_side(axis, side):
	sides = ysides if axis else xsides
	return correct_boolean_string(side, sides)


def correct_limit_alignment(alignment):
	return limit_alignments[0] if alignment is None or alignment not in limit_alignments else alignment

def get_limit_delta(alignment):
	return limit_delta[limit_alignments.index(alignment)]


def correct_direction(direction):
	return directions[1] if direction is None or direction not in directions else direction


def correct_scale(scale):
	return scales[0] if scale is None or scale not in scales else scale


