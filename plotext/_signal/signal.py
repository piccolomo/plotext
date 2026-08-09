# Signal class: wraps C++ signal pointer; manages points, fill, axes, labels and plotting

from plotext._signal.point_filled import point
from plotext._primitives.marker import marker as marker_class
from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring

from plotext._constants.numerical import infinity, max_unique_pixels

from plotext._correct import bool as correct_bool
from plotext._correct import label as correct_label
from plotext._primitives.matrix import matrix as matrix_class
from plotext._signal.points import points_class


# Signal: ordered series of filled points with marker, label, line/fill methods and axis sides
class signal_class:
    # Initialize signal with length or existing pointer
    def __init__(self, length = None, _pointer = None):
        self._pointer = clink.signal_new(length) if _pointer is None else _pointer

    # Release the C pointer on deletion
    def __del__(self):
        if self._pointer is not None:
            clink.signal_delete(self._pointer)
            self._pointer = None

    # Clear all signal points
    def clear(self):
        clink.signal_clear(self._pointer)
        return self


    # === Public fluent methods (chainable) ===

    # Set the signal label shown on the legend
    def label(self, label = None):
        return self._set_label(label)

    # Connect every point uniformly (True = lines drawn between all points, False = scatter)
    def lines(self, active = True):
        a = bool(active)
        for i in range(self.length()):
            self._set_connected(i, a)
        return self

    # Connect a single point at index (effective range 1..N-1; out-of-range indices ignored)
    def line(self, index, active = True):
        if 0 <= index < self.length():
            self._set_connected(index, bool(active))
        return self

    # Fill a vertical stem from each point down to the x axis
    def fillx(self, active = True):
        if active:
            for i, p in enumerate(self):
                self._set_fill_point(i, p.x(), 0, p.marker())
        return self

    # Fill a horizontal stem from each point across to the y axis
    def filly(self, active = True):
        if active:
            for i, p in enumerate(self):
                self._set_fill_point(i, 0, p.y(), p.marker())
        return self


    # === Internal setters (used by plot_class.signal and by drawables) ===

    # Set the drawing method ('simple' or 'full'; 0 or 1) on connecting lines, on stem fills, or on both at once.
    def density(self, method = None, scope = None):
        method = correct_bool.line_method(method)
        scope = correct_bool.line_method_scope(scope)
        if scope in ('line', 'both'):
            clink.signal_set_line_method(self._pointer, method)
        if scope in ('fill', 'both'):
            clink.signal_set_fill_method(self._pointer, method)
        return self

    # Set the signal label, held as a one row matrix, so that a colorized label keeps its colors and its true width instead of counting its color codes as characters
    def _set_label(self, label):
        label = correct_label.label(label)
        clink.signal_set_label(self._pointer, None if label is None else label._pointer)
        return self

    # Set signal marker
    def _set_marker(self, m):
        clink.signal_set_marker(self._pointer, m._pointer)
        return self

    # Set point values
    def _set_point(self, index, x, y, m):
        clink.signal_set_point(self._pointer, index, x, y, m._pointer)
        return self

    # Append multiple points
    def _append_points(self, x, y, m):
        [self._append_point(x[i], y[i], m[i]) for i in range(len(x))]
        return self

    # Set fill point
    def _set_fill_point(self, index, x, y, m):
        clink.signal_set_fill_point(self._pointer, index, x, y, m._pointer)
        return self

    # Mark whether a line should be drawn from the previous point to the one at index (False starts a new segment)
    def _set_connected(self, index, connected = True):
        clink.signal_set_connected(self._pointer, index, bool(connected))
        return self

    # Read the connected flag at the given index
    def _is_connected(self, index):
        return clink.signal_is_connected(self._pointer, index)

    # Copy fill from another signal
    def fill(self, signal):
        for i in signal._get_range():
            point = signal.get(i)
            x, y, m = point.x(), point.y(), point.marker()
            self._set_fill_point(i, x, y, m)
        return self

    # Add a point
    def _append_point(self, x, y, m):
        clink.signal_append_point(self._pointer, x, y, m._pointer)
        return self

    # Fix background pixel
    def _fix_background(self, pixel):
        clink.signal_fix_background(self._pointer, pixel._pointer)
        return self

    # Add offset
    def _add_offset(self, dx, dy):
        clink.signal_add_offset(self._pointer, dx, dy)
        return self

    # Append another signal
    def _append(self, other):
        clink.signal_append(self._pointer, other._pointer)
        return self

    # Plot signal
    def _plot(self):
        clink.signal_plot(self._pointer)
        return self

    # Apply log scale to X
    def _log_x(self):
        clink.signal_log_x(self._pointer)
        return self

    # Apply log scale to Y
    def _log_y(self):
        clink.signal_log_y(self._pointer)
        return self

    # Rescale X axis
    def _rescale_x(self, limits, width, delta):
        clink.signal_rescale_x(self._pointer, limits[0], limits[1], width, delta)
        return self

    # Rescale Y axis
    def _rescale_y(self, limits, height, delta):
        clink.signal_rescale_y(self._pointer, limits[0], limits[1], height, delta)
        return self

    # Get X side
    def _get_xside(self):
        return clink.signal_get_xside(self._pointer)

    # Set X side
    def _set_xside(self, value):
        clink.signal_set_xside(self._pointer, value)
        return self

    # Get Y side
    def _get_yside(self):
        return clink.signal_get_yside(self._pointer)

    # Set Y side
    def _set_yside(self, value):
        clink.signal_set_yside(self._pointer, value)
        return self

    # Get the signal label as a matrix, None when the signal carries no label
    def _get_label(self):
        pointer = clink.signal_get_label(self._pointer)
        return None if pointer is None else matrix_class(0, 0, _pointer = pointer)

    # Get signal marker
    def _get_marker(self):
        return marker_class(_pointer = clink.signal_get_marker(self._pointer))

    # Get fill method
    def _get_fill_method(self):
        return clink.signal_get_fill_method(self._pointer)

    # Get line method
    def _get_line_method(self):
        return clink.signal_get_line_method(self._pointer)

    # Get point by index
    def get(self, index):
        return point(_pointer = clink.signal_get_point(self._pointer, index))

    # Get X values
    def _get_x(self):
        return [p._get_x() for p in self]

    # Get Y values
    def _get_y(self):
        return [p._get_y() for p in self]

    # Get number of points
    def length(self):
        return clink.signal_get_length(self._pointer)

    # Get range for iteration
    def _get_range(self):
        return range(self.length())

    # Get minimum X (optionally filtered by y-range)
    def _get_xmin(self, ymin = None, ymax = None):
        return clink.signal_get_xmin(self._pointer, -infinity if ymin is None else ymin, infinity if ymax is None else ymax)

    # Get maximum X (optionally filtered by y-range)
    def _get_xmax(self, ymin = None, ymax = None):
        return clink.signal_get_xmax(self._pointer, -infinity if ymin is None else ymin, infinity if ymax is None else ymax)

    # Get X limits (optionally filtered by y-range)
    def _get_xlimits(self, ymin = None, ymax = None):
        return self._get_xmin(ymin, ymax), self._get_xmax(ymin, ymax)

    # Get minimum Y (optionally filtered by x-range)
    def _get_ymin(self, xmin = None, xmax = None):
        return clink.signal_get_ymin(self._pointer, -infinity if xmin is None else xmin, infinity if xmax is None else xmax)

    # Get maximum Y (optionally filtered by x-range)
    def _get_ymax(self, xmin = None, xmax = None):
        return clink.signal_get_ymax(self._pointer, -infinity if xmin is None else xmin, infinity if xmax is None else xmax)

    # Get Y limits (optionally filtered by x-range)
    def _get_ylimits(self, xmin = None, xmax = None):
        return self._get_ymin(xmin, xmax), self._get_ymax(xmin, xmax)

    # Unique pixels across every point's main and (when present) fill markers, deduped via a Python set (pixels are hashable). Capped at max_unique_pixels (see _constants/numerical.py) so image-style signals return in O(cap) instead of O(N).
    def _get_unique_pixels(self):
        out, seen = [], set()
        for p in self:
            for px in p._get_pixels():
                if px not in seen:
                    seen.add(px)
                    out.append(px)
                    if len(out) >= max_unique_pixels:
                        return out
        return out

    # Get filled points object
    def _get_points(self):
        return points_class(_pointer = clink.signal_get_points(self._pointer))

    # Copy signal
    def copy(self):
        return signal_class(_pointer = clink.signal_copy(self._pointer))

    # Copy from another points object
    def clone(self, signal):
        clink.signal_assign(self._pointer, signal._pointer)
        return self

    # Get log string of signal
    def _get_log(self, full = False):
        p = clink.signal_get_wstring(self._pointer, full)
        out = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return out

    # Print signal summary followed by every point
    def log(self):
        print(self._get_log(full = True))
        return self

    # Turn the signal points into canvas positions: rescaled, drawn and made denser; the later steps, squashing, background and offset, happen once on all signals together, in signals_class.draw.
    def _prepare_points(self, xruler, yruler, canvas_width, canvas_height):
        xlim, ylim = xruler._get_limits(direction = True), yruler._get_limits(direction = True)
        xdelta, ydelta = xruler._get_delta(), yruler._get_delta()
        if xruler._get_scale() == "log": self._log_x()
        if yruler._get_scale() == "log": self._log_y()
        self._rescale_x(xlim, canvas_width, xdelta)
        self._rescale_y(ylim, canvas_height, ydelta)
        self._plot()
        points = self._get_points()
        points.select_in_matrix(canvas_width, canvas_height)
        return points

    # Represent signal as its one-line summary
    def __repr__(self):
        return self._get_log(full = False)

    # Iterator over points
    def __iter__(self):
        return (self.get(i) for i in self._get_range())
