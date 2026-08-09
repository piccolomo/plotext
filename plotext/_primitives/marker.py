# Marker primitive: wraps a C++ marker pointer; handles normal/typed markers and exposes model, pixel and string

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring, wchar
from plotext._primitives.pixel import pixel as pixel_class
from plotext._correct.pixel import pixel_par as correct_pixel
from plotext._correct import matrix as correct_matrix
from plotext._settings import defaults
from plotext._constants import enums
from plotext._primitives.matrix import matrix as matrix_class
from plotext._primitives.colorize import colorize as colorize_class


# Marker: one glyph (or higher-resolution marker type) with its pixel styling, backed by the C kernel
class marker:
    # Build a marker from a single character, a named symbol like heart, a higher resolution code (hd, fhd, braille), or a matrix or colorize object covering several cells, aligned by ha and va.
    def __init__(self, symbol = None, pixel = None, ha = -1, va = -1, _pointer = None):
        self._pointer = None
        if _pointer is not None:
            self._pointer = _pointer
            return
        if isinstance(symbol, colorize_class):
            symbol = symbol.matrix()
        ha = ha if isinstance(ha, int) else correct_matrix.ha(ha)   # ints pass through untouched: 2 is the kernel dynamic alignment
        va = va if isinstance(va, int) else correct_matrix.va(va)
        m  = defaults.marker if symbol is None else symbol
        px = correct_pixel(pixel)
        if isinstance(m, matrix_class):
            self._pointer = clink.marker_new_matrix(m._pointer, ha, va)
        elif m == 'hd':
            self._pointer = clink.marker_new_hd(px._pointer)
        elif m == 'fhd' and 'fhd' in enums.hd_markers_codes:
            self._pointer = clink.marker_new_fhd(px._pointer)
        elif m == 'braille':
            self._pointer = clink.marker_new_braille(px._pointer)
        elif m in enums.symbol_codes:
            self._pointer = clink.marker_new_code(m.encode('utf-8'), px._pointer)
        elif isinstance(m, str) and len(m) == 1:
            self._pointer = clink.marker_new_normal(wchar(m), px._pointer)
        elif isinstance(m, str):
            m = colorize_class(m).matrix()
            self._pointer = clink.marker_new_matrix(m._pointer, ha, va)
        else:
            raise ValueError(f"Unknown marker {m!r}. Use a string, hd/fhd/braille, a plotext.matrix / plotext.colorize, or one of: {', '.join(enums.symbol_codes)}.")

    # Release the C marker pointer on deletion
    def __del__(self):
        if self._pointer is not None:
            clink.marker_delete(self._pointer)
            self._pointer = None

    # Apply a pixel to the marker, replacing its current color and style.
    def fill(self, pixel = None):
        pixel = correct_pixel(pixel)
        clink.marker_set_pixel(self._pointer, pixel._pointer)
        return self

    # Internal pixel setter kept for legacy call-sites; forwards to fill.
    def _set_pixel(self, pixel):
        return self.fill(pixel)

    def _fix(self, pixel):
        clink.marker_fix(self._pointer, pixel._pointer)
        return self

    # Get the character used as the model of the marker
    def _get_model(self):
        return clink.marker_get_model(self._pointer)[0]

    # Get the pixel associated with the marker
    def pixel(self):
        return pixel_class(_pointer = clink.marker_get_pixel(self._pointer))

    # Get the rendered marker string
    def _get_string(self):
        p = clink.marker_get_wstring(self._pointer)
        s = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return s

    # Create a copy of this marker
    def copy(self):
        return marker(_pointer = clink.marker_copy(self._pointer))

    # Copy protocol
    def __copy__(self):
        return self.copy()

    # String representation (the rendered marker)
    def __repr__(self):
        return self._get_string()
