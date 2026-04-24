# Signal class: wraps C++ signal pointer; manages points, fill, axes, labels and plotting

from plotext._signal.point_filled import point_filled_class
from plotext._primitives.marker import marker as marker_class
from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring

from plotext._settings.constants.numerical import infinity
from plotext._methods.sequence import unique

from plotext._correct import signal as correct
from plotext._correct import bool as correct_bool
from plotext._signal.points import points_class


# Signal: ordered series of filled points with marker, label, line/fill methods and axis sides
class signal_class:
    # Initialize signal with length or existing pointer
    def __init__(self, length = None, _pointer = None):
        self._pointer = clink.signal_new(length) if _pointer is None else _pointer
        self._set_lines()

    # Release the C pointer on deletion
    def __del__(self):
        if self._pointer is not None:
            clink.signal_delete(self._pointer)
            self._pointer = None

    # Clear all signal points
    def clear(self):
        clink.signal_clear(self._pointer)
        return self


    # =====================================================================
    # Public fluent methods: return self so they can be chained after
    # plt.signal(...) to configure the signal before plt.draw().
    # =====================================================================

    # Toggle line drawing between consecutive points
    def lines(self, value = True):
        return self._set_lines(correct_bool.boolean(value))

    # Set the signal label shown on the legend
    def label(self, label = None):
        return self._set_label(label)

    # Fill a vertical stem from each point down to the x axis
    def fillx(self, active = True):
        if active:
            for i, p in enumerate(self):
                self._set_fill_point(i, p.get_x(), 0, p.get_marker())
        return self

    # Fill a horizontal stem from each point across to the y axis
    def filly(self, active = True):
        if active:
            for i, p in enumerate(self):
                self._set_fill_point(i, 0, p.get_y(), p.get_marker())
        return self

    # Set the line drawing method ('simple' or 'full'; 0 or 1)
    def line_method(self, method = None):
        clink.signal_set_line_method(self._pointer, correct.line_method(method))
        return self

    # Set the fill drawing method ('simple' or 'full'; 0 or 1)
    def fill_method(self, method = None):
        clink.signal_set_fill_method(self._pointer, correct.line_method(method))
        return self


    # =====================================================================
    # Internal setters (used by plot_class.signal and by fluent methods above)
    # =====================================================================

    # Set whether lines are drawn
    def _set_lines(self, lines = False):
        self._lines = lines
        return self

    # Set signal label
    def _set_label(self, label):
        label = "" if label is None else str(label)
        clink.signal_set_label(self._pointer, wstring(label))
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

    # Copy fill from another signal
    def fill(self, signal):
        for i in signal._get_range():
            point = signal._get(i)
            x, y, m = point.get_x(), point.get_y(), point.get_marker()
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

    # Get lines flag
    def _get_lines(self):
        return self._lines

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

    # Get signal label
    def _get_label(self):
        p = clink.signal_get_label(self._pointer)
        out = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return out

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
    def _get(self, index):
        return point_filled_class(_pointer = clink.signal_get_point(self._pointer, index))

    # Get X values
    def _get_x(self):
        return [p._get_x() for p in self]

    # Get Y values
    def _get_y(self):
        return [p._get_y() for p in self]

    # Get number of points
    def get_length(self):
        return clink.signal_get_length(self._pointer)

    # Get range for iteration
    def _get_range(self):
        return range(self.get_length())

    # Get minimum X
    def _get_xmin(self, ymin = None, ymax = None):
        return clink.signal_get_xmin(self._pointer, -infinity if ymin is None else ymin, infinity if ymax is None else ymax)

    # Get maximum X
    def _get_xmax(self, ymin = None, ymax = None):
        return clink.signal_get_xmax(self._pointer, -infinity if ymin is None else ymin, infinity if ymax is None else ymax)

    # Get X limits
    def _get_xlimits(self, ymin = None, ymax = None):
        return self._get_xmin(ymin, ymax), self._get_xmax(ymin, ymax)

    # Get minimum Y
    def _get_ymin(self, xmin = None, xmax = None):
        return clink.signal_get_ymin(self._pointer, -infinity if xmin is None else xmin, infinity if xmax is None else xmax)

    # Get maximum Y
    def _get_ymax(self, xmin = None, xmax = None):
        return clink.signal_get_ymax(self._pointer, -infinity if xmin is None else xmin, infinity if xmax is None else xmax)

    # Get Y limits
    def _get_ylimits(self, xmin = None, xmax = None):
        return self._get_ymin(xmin, xmax), self._get_ymax(xmin, xmax)

    # Get unique integer foreground colors
    def _get_foreground_unique_integer_colors(self):
        return unique([p.get_foreground_integer_color() for p in self])

    # Get filled points object
    def _get_points(self):
        return points_class(_pointer = clink.signal_get_points(self._pointer))

    # Copy signal
    def copy(self):
        out = signal_class(_pointer = clink.signal_copy(self._pointer))
        out._lines = self._lines
        return out

    # Copy from another points object
    def clone(self, signal):
        clink.signal_assign(self._pointer, signal._pointer)
        return self

    # Get log string of signal
    def _get_log(self, fill = False):
        p = clink.signal_get_wstring(self._pointer, fill)
        out = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return out

    # Print log
    def log(self, fill = False):
        print(self._get_log(fill))
        return self

    # Represent signal
    def __repr__(self):
        return f"Plotext Signal: length {self.get_length()}, lines: {self._get_lines()}"

    # Iterator over points
    def __iter__(self):
        return (self._get(i) for i in self._get_range())
