# Marker primitive: wraps a C++ marker pointer; handles normal/typed markers and exposes model, pixel and string

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring, wchar
from plotext._primitives.pixel import pixel as pixel_class
from plotext._settings import defaults
from plotext._constants import enums
from plotext._correct import pixel as correct_pixel


# Marker: one glyph (or higher-resolution marker type) with its pixel styling, backed by the C kernel
class marker:
    # Dispatch on symbol type: a matrix / colorize becomes a multi-cell matrix_marker (ha, va apply); anything else falls through to standard single-cell marker construction.
    def __new__(cls, symbol=None, pixel=None, ha=-1, va=-1, _pointer=None):
        if _pointer is None:
            from plotext._primitives.matrix import matrix as matrix_class
            from plotext._primitives.colorize import colorize as colorize_class
            if isinstance(symbol, (matrix_class, colorize_class)):
                from plotext._primitives.matrix_marker import matrix_marker as matrix_marker_class
                return matrix_marker_class(symbol, ha = ha, va = va)
        return super().__new__(cls)

    # Initialize marker from a normal character, a named character symbol, or a higher-resolution code (hd / fhd / braille).
    # Named-symbol → glyph resolution is performed on the C side via get_symbol().
    def __init__(self, symbol=None, pixel=None, ha=-1, va=-1, _pointer=None):
        self._pointer = None
        if _pointer is not None: self._pointer = _pointer; return
        m  = defaults.marker if symbol is None else symbol
        px = correct_pixel.pixel(pixel, pixel_class())
        hd_factories = {'hd': clink.marker_new_hd, 'fhd': clink.marker_new_fhd, 'braille': clink.marker_new_braille}
        if isinstance(m, str) and len(m) > 1 and m not in hd_factories and m not in enums.symbol_codes:
            raise ValueError(f"Unknown marker {m!r}. Use a single character, hd/fhd/braille, or one of: {', '.join(enums.symbol_codes)}.")
        self._pointer = hd_factories[m](px._pointer)                          if m in hd_factories       else \
                        clink.marker_new_code(m.encode('utf-8'), px._pointer) if m in enums.symbol_codes else \
                        clink.marker_new_normal(wchar(str(m)[0]), px._pointer)

    # Release the C marker pointer on deletion
    def __del__(self):
        if self._pointer is not None:
            clink.marker_delete(self._pointer)
            self._pointer = None

    # Fix the marker background against another pixel
    def _set_pixel(self, pixel):
        clink.marker_set_pixel(self._pointer, pixel._pointer)
        return self

    def _fix(self, pixel):
        clink.marker_fix(self._pointer, pixel._pointer)
        return self

    # Get the character used as the model of the marker
    def _get_model(self):
        return clink.marker_get_model(self._pointer)[0]

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
