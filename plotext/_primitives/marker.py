# Marker primitive: wraps a C++ marker pointer; handles normal/typed markers and exposes model, pixel and string

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring, wchar
from plotext._primitives.pixel import pixel as pixel_class
from plotext._settings import defaults
from plotext._settings.constants import enums


# Marker: one glyph (or HD marker type) with its pixel styling, backed by the C kernel
class marker:
    # Initialize marker from a normal character, a named character code, or an HD marker code.
    # Named-code → glyph resolution is performed on the C side via get_marker().
    def __init__(self, marker=None, foreground='default', background='default', style='default', _pointer=None):
        if _pointer is not None:
            self._pointer = _pointer
            return
        m = defaults.marker if marker is None else marker
        px = pixel_class(foreground = foreground, background = background, style = style)
        if m in enums.hd_markers_codes:
            self._pointer = clink.marker_new_hd(enums.hd_markers_codes.index(m) + 1, px._pointer)
        elif m in enums.marker_codes:
            self._pointer = clink.marker_new_code(m.encode('utf-8'), px._pointer)
        else:
            self._pointer = clink.marker_new_normal(wchar(str(m)[0]), px._pointer)

    # Release the C marker pointer on deletion
    def __del__(self):
        if self._pointer is not None:
            clink.marker_delete(self._pointer)
            self._pointer = None

    # Fix the marker background against another pixel
    def _fix(self, pixel):
        clink.marker_fix(self._pointer, pixel._pointer)
        return self

    # Get the character used as the model of the marker
    def _get_model(self):
        return wchar.from_buffer(clink.marker_get_model(self._pointer)).value

    # Get the pixel associated with the marker
    def get_pixel(self):
        return pixel_class(_pointer=clink.marker_get_pixel(self._pointer))

    # Get the rendered marker string
    def _get_string(self):
        p = clink.marker_get_wstring(self._pointer)
        s = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return s

    # Create a copy of this marker
    def copy(self):
        return marker(_pointer=clink.marker_copy(self._pointer))

    # Copy protocol
    def __copy__(self):
        return self.copy()

    # String representation (the rendered marker)
    def __repr__(self):
        return self._get_string()
