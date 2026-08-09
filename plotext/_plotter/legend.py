# Legend component for plotext: manages markers, labels, pixel, position and frame

from plotext._primitives.matrix import matrix as matrix_class
from plotext._primitives.marker import marker
from plotext._signal.point import point_class
from plotext._plotter.frame.axes import axes_class
from plotext._plotter.frame.corner import corner_class
from plotext._correct import pixel as correct_pixel
from plotext._correct import matrix as correct_matrix
from plotext._correct import axis as correct_axis
from plotext._correct import label as correct_label
from plotext._methods.ruler import rescale
from plotext._settings import defaults
from plotext._constants.numerical import binary


# Legend container: holds markers, labels, pixel, position and frame axes
class legend_class:

    # Initialize legend with axes, settings, signals and pixel
    def __init__(self):
        self._axes = axes_class()
        self.clear_settings()
        self.clear_signals()
        self.set_pixel()

    # Reset legend to initial state
    def clear_settings(self):
        self._axes.clear_settings()
        self.set_status()
        self.frame()
        self.set_position()
        self.set_ha()
        self.set_va()
        self.set_xside()
        self.set_yside()
        return self

    # Clear markers and labels
    def clear_signals(self):
        self._markers = []
        self._labels = []
        return self

    # Reset pixel to legend default, on the box and its frame axes
    def clear_pixel(self):
        self.set_pixel()
        return self

    # Set several legend options at once, each value passed as it is, since the single setters validate it.
    def set(self, status = None, x = None, y = None, relative = None, ha = None, va = None, pixel = None, style = None, xside = None, yside = None):
        if status is not None:
            self.set_status(status)
        if style is not None:
            self.frame(True, style)
        if x is not None or y is not None or relative is not None:
            self.set_position(x, y, relative)
        if ha is not None:
            self.set_ha(ha)
        if va is not None:
            self.set_va(va)
        if pixel is not None:
            self.set_pixel(pixel)
        if xside is not None:
            self.set_xside(xside)
        if yside is not None:
            self.set_yside(yside)
        return self

    # Activate or deactivate the legend; the default leaves it undecided, to be settled by the labels at drawing time
    def set_status(self, status = None):
        self._status = defaults.legend["status"] if status is None else bool(status)
        return self

    # The legend is drawn when it holds at least one label and was not switched off, so it appears on its own as soon as something is labeled
    def is_active(self):
        return len(self._labels) > 0 and self._status is not False

    # Enable the legend
    def enable(self):
        return self.set_status(True)

    # Disable the legend
    def disable(self):
        return self.set_status(False)

    # Set pixel, default if none provided
    def set_pixel(self, pixel = None, default_pixel = None):
        pixel = correct_pixel.pixel(pixel, defaults.pixels["legend"])
        self._pixel = pixel
        self._axes.set(pixel = pixel, axis = binary, side = binary)
        return self

    # Set legend position (x, y) and relative flag
    def set_position(self, x = None, y = None, relative = None):
        self._x = defaults.legend["x position"] if x is None else x
        self._y = defaults.legend["y position"] if y is None else y
        self._relative = defaults.legend["relative"] if relative is None else relative
        return self

    # Set horizontal alignment
    def set_ha(self, ha = -1):
        self._ha = correct_matrix.ha(ha)
        return self

    # Set vertical alignment: like ha, the name states the box edge the anchor touches, top (the default) hanging the box downwards
    def set_va(self, va = -1):
        self._va = correct_matrix.va(va)
        return self

    # Set x axis side
    def set_xside(self, side = 0):
        self._xside = correct_axis.side(0, side)
        return self

    # Set y axis side
    def set_yside(self, side = 0):
        self._yside = correct_axis.side(1, side)
        return self

    # Get x side
    def get_xside(self):
        return self._xside

    # Get y side
    def get_yside(self):
        return self._yside

    # Get current position as tuple (x, y)
    def position(self):
        return self._x, self._y

    # Get alignments
    def get_alignments(self):
        return self._ha, self._va

    # Get current status
    def get_status(self):
        return self._status

    # Compute absolute position along the axis: relative reads the value in ruler units and maps it like a tick position, otherwise it is already in canvas character units
    def get_absolute_position(self, axis, ruler, bins):
        position = self._x if axis == 0 else self._y
        if self._relative:
            limits = ruler._get_limits(direction = True)
            delta = ruler._get_delta()
            position = int(rescale(position, *limits, bins, delta))
        return position

    # Set frame style for legend axes
    def frame(self, frame = True, style = None, pixel = None):
        return self._axes.frame(frame, style, pixel)

    # Number of labels
    def length(self):
        return len(self._markers)

    # Index range
    def get_range(self):
        return range(self.length())

    # Compute width
    def width(self):
        frame = 4 * self._axes.get(1, 0).get_status()
        return max((el.width() for el in self._labels), default = 0) + 2 + frame

    # Compute height
    def height(self):
        frame = 4 * self._axes.get(0, 0).get_status()
        return 2 * self.length() - 1 + frame

    # Get (width, height) size
    def size(self):
        return self.width(), self.height()

    # Add marker-label pair
    def add(self, marker, label):
        label = correct_label.label(label, self._pixel)
        self._markers.append(marker)
        self._labels.append(label)
        return self

    # Update with signals (and optional rulers). Only what carries a label enters the legend, signals and ruler lines alike; the unlabeled ones stay out.
    def update(self, signals, rulers = None):
        self.clear_signals()
        for signal in signals:
            label = signal._get_label()
            if label is not None:
                self.add(signal._get_marker(), label)
        if rulers is not None:
            for ruler in rulers:
                for line_sig in ruler._lines:
                    if line_sig.get_label() is not None:
                        self.add(line_sig, line_sig.get_label())
        return self

    # Fix background on pixel, labels and markers
    def fix_background(self, pixel):
        self._pixel._fix_background(pixel)
        [label._fix_background(pixel) for label in self._labels]
        [marker._fix(pixel) for marker in self._markers]
        return self

    # Construct the legend matrix
    def get(self):
        width, height = self.size()
        log = matrix_class(width, height, self._pixel)
        frame = self._axes.get(0, 0).get_status()

        if frame:
            log._insert_matrix(0,         0,          self._axes.get(0, 1).get(width))           # top
            log._insert_matrix(0,         height - 1, self._axes.get(0, 0).get(width))           # bottom
            log._insert_matrix(0,         frame,      self._axes.get(1, 0).get(height - 2))      # left
            log._insert_matrix(width - 1, frame,      self._axes.get(1, 1).get(height - 2))      # right
            # Corners, stamp the four box-marker corner glyphs (┌ ┐ └ ┘) so the frame closes properly
            for v in binary:
                for h in binary:
                    axis = self._axes.get(0, v)
                    col = (width - 1) if h else 0
                    row = 0 if v else (height - 1)
                    corner_class(v, h).draw(log, col, row, 1, 1, axis.pixel(), axis.get_style(), axis.pixel())

        col, row = 2 * frame, 2 * frame
        pixel = self._axes.get().pixel()

        for r in self.get_range():
            m = self._markers[r]
            log._set_pixelled_character(col, row + 2 * r, m._get_model(), m.pixel())
            l = self._labels[r]
            log._insert_point(point_class(col + 2, row + 2 * r, marker(l, ha = -1)))

        return log

    # Clone from another legend
    def clone(self, legend):
        self._markers = legend._markers.copy()
        self._labels = legend._labels.copy()
        self._xside = legend._xside
        self._yside = legend._yside
        self._status = legend._status
        self._pixel.clone(legend._pixel)
        self._axes.clone(legend._axes)
        self._x, self._y = legend.position()
        self._ha, self._va = legend.get_alignments()
        return self

    # Render the legend onto matrix at its computed canvas-relative position; legend_part is updated with the final position/size.
    def draw(self, matrix, irulers, canvas_part, legend_part):
        canvas_col, canvas_row = canvas_part.position()
        canvas_width, canvas_height = canvas_part.size()
        xruler = irulers._get(0, self.get_xside())
        yruler = irulers._get(1, self.get_yside())
        col = self.get_absolute_position(0, xruler, canvas_width) + canvas_col
        row = self.get_absolute_position(1, yruler, canvas_height) + canvas_row
        ha, va = self.get_alignments()
        matrix._insert_matrix_aligned(col, row, self.get(), ha, va)
        legend_part.set_position(col, row)
        legend_part.set_size(*self.size())
        return self

    # String representation
    def __repr__(self):
        out = "Plotext Legend"
        out += f"\n status: {'active' if self._status else 'inactive'}"
        out += f"\n size: {self.length()}"
        out += f"\n xside: {self._xside}, yside: {self._yside}"
        out += f"\n pos: ({self._x}, {self._y}), relative: {self._relative}"
        out += f"\n align: ha={self._ha}, va={self._va}"
        out += f"\n pixel: {self._pixel}"
        for i in self.get_range():
            out += f"\n  marker: {self._markers[i]}, label: {self._labels[i]}"
        return out