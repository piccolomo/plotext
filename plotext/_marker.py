from plotext._clink import clink, wstring, wchar
from plotext._pixel import pixel as pixel_class
from plotext._constants import hd_markers_codes
from plotext._default import default_marker_code


class marker:
    # Initialize marker with style, colors, and optional pointer
    def __init__(self, marker = None, foreground = 'default', background = 'default', style = 'default', _pointer = None):
        if _pointer is not None:
            self._pointer = _pointer
        else:
            marker = default_marker_code if marker is None else marker
            marker = hd_markers_codes.index(marker) + 1 if marker in hd_markers_codes else str(marker)[0]

            px = pixel_class(foreground = foreground, background = background, style = style)
            p = px._pointer

            if isinstance(marker, str):
                self._pointer = clink.marker_new_normal(wchar(marker), p)
            else:  # if integer
                self._pointer = clink.marker_new_type(marker, p)

    # Delete underlying marker pointer
    def __del__(self):
        clink.marker_delete(self._pointer)

    # Fix marker by copying from another pixel's pointer
    def _fix(self, pixel):
        clink.marker_fix(self._pointer, pixel._pointer)
        return self

    # Get marker model character
    def get_model(self):
        p = clink.marker_get_model(self._pointer)
        c = wchar.from_buffer(p).value
        return c

    # Get associated pixel object
    def get_pixel(self):
        return pixel_class(_pointer = clink.marker_get_pixel(self._pointer))

    # Get string representation of the marker
    def get_string(self):
        p = clink.marker_get_wstring(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Return a copy of this marker
    def copy(self):
        return marker(_pointer = clink.marker_copy(self._pointer))

    def __copy__(self):
        return self.copy()

    def __repr__(self):
        return self.get_string()
