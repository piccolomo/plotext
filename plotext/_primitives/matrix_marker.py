# MatrixMarker primitive: multi-cell marker carrying its own matrix + per-axis alignment (ha, va).
# Position comes from the Point that stamps it; xside/yside live on the Signal that owns the Point.

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring


class matrix_marker:
    # Build from a matrix (or colorize) + horizontal/vertical alignment (-1 left/top, 0 center, 1 right/bottom, 2 dynamic), or wrap an existing C pointer
    def __init__(self, matrix=None, ha=-1, va=-1, _pointer=None):
        if _pointer is not None:
            self._pointer = _pointer; return
        from plotext._primitives.colorize import colorize as colorize_class
        if isinstance(matrix, colorize_class): matrix = matrix.get_matrix()
        self._pointer = clink.marker_new_matrix(matrix._pointer, int(ha), int(va))

    def __del__(self):
        if self._pointer is not None:
            clink.marker_delete(self._pointer)
            self._pointer = None

    # Apply per-cell pixel correction (fills in unset fg/bg on each cell from the given pixel). Matches marker_class._fix so matrix_marker is interchangeable in correct_marker.marker().
    def _fix(self, pixel):
        clink.marker_fix(self._pointer, pixel._pointer)
        return self

    # Top-left cell pixel (representative; multi-cell markers don't have one owned pixel)
    def get_pixel(self):
        from plotext._primitives.pixel import pixel as pixel_class
        return pixel_class(_pointer=clink.marker_get_pixel(self._pointer))

    def copy(self):
        return self.__class__(_pointer=clink.marker_copy(self._pointer))

    def __copy__(self):
        return self.copy()

    def _get_string(self):
        p = clink.marker_get_wstring(self._pointer); s = wstring.from_buffer(p).value; clink.wstring_delete(p); return s

    def __repr__(self):
        return self._get_string()
