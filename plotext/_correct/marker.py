# Marker normalization utilities: single marker and repeated marker lists

from plotext._primitives.marker import marker as marker_class
from plotext._methods.object import is_list_like
from plotext._methods.sequence import repeat


# Correct a single marker
def marker(marker, default_marker):
    marker = default_marker if marker is None else marker_class(marker) if isinstance(marker, str) else marker
    return marker._fix(default_marker.get_pixel())                                    # _fix expects a pixel_class, not a marker_class


# Correct a list of markers and repeat to match length
def markers(marker_value, default_marker, length):
    if not is_list_like(marker_value):
        marker_value = [marker_value]
    marker_value = [marker(m, default_marker) for m in marker_value]
    return repeat(marker_value, length)
