# Marker normalization utilities: single marker and repeated marker lists

from plotext._primitives.marker import marker as marker_class
from plotext._primitives.matrix import matrix as matrix_class
from plotext._primitives.colorize import colorize as colorize_class
from plotext._methods.object import is_list_like
from plotext._methods.sequence import repeat


# Correct a single marker: strings, matrices and colorized objects are wrapped into a marker object
def marker(marker, default_marker):
    marker = default_marker if marker is None else marker_class(marker) if isinstance(marker, (str, matrix_class, colorize_class)) else marker
    return marker._fix(default_marker.pixel())                                    # _fix expects a pixel_class, not a marker_class


# Correct a list of markers and repeat to match length; a single matrix or colorized object counts as one marker, not a list
def markers(marker_value, default_marker, length):
    if not is_list_like(marker_value) or isinstance(marker_value, (matrix_class, colorize_class)):
        marker_value = [marker_value]
    marker_value = [marker(m, default_marker) for m in marker_value]
    return repeat(marker_value, length)
