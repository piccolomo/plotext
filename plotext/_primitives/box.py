# Box primitive: wraps a C++ BoxMarker pointer.
#   box_class — full-arm initialization (up/down/left/right + style + pixel). Plotter-internal use; covers ticks, corners, grid intersections.
#   line      — user-facing subclass with simple orientation init.

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring
from plotext._primitives.pixel import pixel as pixel_class


# Internal/plotter-facing class with full arm control.
class box_class:
    # 4 arm bools + style + pixel; or pass _pointer to wrap an existing C-side BoxMarker. style must be int (already corrected by caller).
    def __init__(self, up=False, down=False, left=False, right=False, pixel=pixel_class(), style=0, _pointer=None):
        self._pointer = _pointer if _pointer is not None else clink.marker_new_box(
            bool(up), bool(down), bool(left), bool(right),
            style,
            pixel._pointer)

    # Release the C marker pointer on deletion
    def __del__(self):
        if self._pointer is not None:
            clink.marker_delete(self._pointer)
            self._pointer = None

    # Orientation heuristic from the C kernel: 0 = horizontal, 1 = any vertical-arm
    def get_orientation(self):
        return int(clink.marker_get_orientation(self._pointer))

    # Style index (0..4 → default/double/heavy/dotted/rounded)
    def get_style(self):
        return int(clink.marker_get_style(self._pointer))

    # Pixel associated with the line
    def get_pixel(self):
        return pixel_class(_pointer=clink.marker_get_pixel(self._pointer))

    # Model glyph for the line kind (the legend-style preview char, e.g. ┼)
    def _get_model(self):
        return clink.marker_get_model(self._pointer)[0]

    # Rendered string (the actual glyph this line draws as a single cell)
    def _get_string(self):
        p = clink.marker_get_wstring(self._pointer); s = wstring.from_buffer(p).value; clink.wstring_delete(p); return s

    # Fix the line marker's background against another pixel
    def _fix(self, pixel):
        clink.marker_fix(self._pointer, pixel._pointer); return self

    # Deep copy
    def copy(self):
        return self.__class__(_pointer=clink.marker_copy(self._pointer))

    def __copy__(self):
        return self.copy()

    # String representation (the rendered glyph)
    def __repr__(self):
        return self._get_string()


# User-facing class — orientation-only init (0 = horizontal, 1 = vertical). Sugar over box_class. orientation must be int 0/1 (caller pre-corrects).
class line(box_class):
    def __init__(self, orientation=0, pixel=pixel_class(), style=0, _pointer=None):
        if _pointer is not None:
            super().__init__(_pointer=_pointer); return
        v = bool(orientation)
        super().__init__(up=v, down=v, left=not v, right=not v, pixel=pixel, style=style)
