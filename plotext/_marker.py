from plotext._cimport import *
from plotext._constants import hd_markers


class marker_class:
    # Initialize marker with style, colors, and optional pointer
    def __init__(self, marker = 'hd', foreground = 'default', background = 'default', style = 'default', pointer = None):
        if pointer is not None:
            self._pointer = pointer
        else:
            pixel = pixel_class(foreground, background, style)
            p = pixel._pointer
            marker = default_marker if marker is None else marker
            marker = hd_markers.index(marker) + 1 if marker in hd_markers else str(marker)[0]
            if isinstance(marker, str):
                self._pointer = clink.marker_new_normal(wchar(marker), p)
            else:
                self._pointer = clink.marker_new_hd(marker, p)

    # Delete underlying marker pointer
    def __del__(self):
        clink.marker_delete(self._pointer)

    # Get marker model character
    def get_model(self):
        p = clink.marker_get_model(self._pointer)
        c = wchar.from_buffer(p).value
        return c

    # Get associated pixel object
    def get_pixel(self):
        return pixel_class(pointer = clink.marker_get_pixel(self._pointer))

    # Get string representation of the marker
    def get_string(self):
        p = clink.marker_get_wstring(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Return a copy of this marker
    def copy(self):
        return marker_class(pointer = clink.marker_copy(self._pointer))

    def __copy__(self):
        return self.copy()

    def __repr__(self):
        return self.get_string()
