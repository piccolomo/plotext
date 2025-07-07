from plotext._matrix import matrix_class
from plotext._axes import axes_class
from plotext._default import default_legend_pixel
from plotext._methods import *


class legend_class:
    def __init__(self):
        self.clear()

    # Reset legend to initial state
    def clear(self):
        self.clear_signals()
        self.axes = axes_class()
        self.set_active(False)
        self.set_pixel()
        self.frame()
        self.set_position()
        self.set_alignment()
        self.set_axes()
        return self

    # Clear markers and labels
    def clear_signals(self):
        self.markers = []
        self.labels = []
        return self

    # Activate or deactivate the legend
    def set_active(self, active = True):
        self.active = active
        return self

    def enable(self):
        return self.set_active(True)

    def disable(self):
        return self.set_active(False)

    # Set pixel style for the legend
    def set_pixel(self, pixel = default_legend_pixel):
        self.pixel = pixel
        return self

    # Set legend position (x, y) and whether position is relative
    def set_position(self, x = 0, y = 0, relative = False):
        self.x = x
        self.y = y
        self.relative = relative
        return self

    # Set horizontal and vertical alignment
    def set_alignment(self, ha = -1, va = 1):
        self.ha = ha  # horizontal alignment
        self.va = va  # vertical alignment
        return self

    # Set axes sides for x and y
    def set_axes(self, xside = 0, yside = 0):
        self.xside = xside
        self.yside = yside
        return self

    # Get current position as tuple (x, y)
    def get_position(self):
        return self.x, self.y

    # Get current horizontal and vertical alignment
    def get_alignments(self):
        return self.ha, self.va

    # Compute absolute position along an axis using scaler and bin count
    def get_absolute_position(self, axis, scaler, bins):
        col = self.x if axis == 0 else self.y
        side = self.xside if axis == 0 else self.yside

        if self.relative:
            direction = scaler.get_direction()
            lim = scaler.get_limits(scaled=True, direction=direction)
            delta = scaler.get_delta()
            col = bins - 1 if col is None else col
            col = int(list_methods.rescale(col, *lim, bins, delta))
        return col

    # Set frame style for legend axes
    def frame(self, frame=True, style=None, pixel=None):
        return self.axes.frame(frame, style, pixel)

    # Number of markers/labels in the legend
    def get_length(self):
        return len(self.markers)

    # Range of indices for markers/labels
    def get_range(self):
        return range(self.get_length())

    # Compute width of legend (max label length + padding + frame size)
    def get_width(self):
        frame = 4 * self.axes.get(1, 0).status
        return max((len(el) for el in self.labels), default=0) + 2 + frame

    # Compute height of legend (rows plus frame size)
    def get_height(self):
        frame = 4 * self.axes.get(0, 0).status
        return 2 * self.get_length() - 1 + frame

    # Get width and height as tuple
    def get_size(self):
        return self.get_width(), self.get_height()

    # Add a marker-label pair to legend
    def add(self, marker, label):
        self.markers.append(marker)
        self.labels.append(label)
        return self

    # # Update legend with markers and labels from signals
    # def update(self, signals):
    #     for signal in signals:
    #         marker = signal.get(0).get_marker()
    #         label = signal.label
    #         self.add(marker, label)

    def fix_background(self, pixel):
        self.pixel._fix_background(pixel)
        [label._fix_background(pixel) for label in self.labels]
        return self

    # Construct and return the legend as a matrix_class object
    def get(self):
        width, height = self.get_size()
        log = matrix_class(width, height, self.pixel)
        frame = self.axes.get(0, 0).status

        if frame:
            # Draw top axis
            axis = self.axes.get(0, 1)
            col, row = 0, 0
            string = axis.get_string(width)
            for c, char in enumerate(string):
                log._set_pixelled_character(col + c, row, char, axis.pixel)

            # Draw left axis
            axis = self.axes.get(1, 0)
            col, row = 0, frame
            string = axis.get_string(height - 2)
            for r, char in enumerate(string):
                log._set_pixelled_character(col, row + r, char, axis.pixel)

            # Draw right axis
            axis = self.axes.get(1, 0)
            col, row = width - 1, frame
            string = axis.get_string(height - 2)
            for r, char in enumerate(string):
                log._set_pixelled_character(col, row + r, char, axis.pixel)

            # Draw bottom axis
            axis = self.axes.get(0, 0)
            col, row = 0, height - 1
            string = axis.get_string(width)
            for c, char in enumerate(string):
                log._set_pixelled_character(col + c, row, char, axis.pixel)

        col, row = 2 * frame, 2 * frame
        pixel = self.axes.get().pixel

        # Draw markers and labels inside the frame
        for r in self.get_range():
            m = self.markers[r]
            log._set_pixelled_character(col, row + 2 * r, m.get_model(), m.get_pixel())
            l = self.labels[r]
            #l._fix(self.pixel)
            log._insert_colorized_aligned(col + 2, row + 2 * r, l)

        return log

    # Copy properties and data from another legend instance
    def clone(self, legend):
        self.markers = legend.markers.copy()
        self.labels = legend.labels.copy()
        self.xside = legend.xside
        self.yside = legend.yside
        self.active = legend.active
        self.pixel.clone(legend.pixel)
        self.axes.clone(legend.axes)
        self.x, self.y = legend.get_position()
        self.ha, self.va = legend.get_alignments()
        self.xside, self.yside = legend.xside, legend.yside
        return

    def __repr__(self):
        state = "active" if self.active else "inactive"
        pos = f"({self.x}, {self.y})"
        align = f"ha = {self.ha}, va = {self.va}"
        axes = f"xside = {self.xside}, yside = {self.yside}"
        count = self.get_length()
        out = f"Legend {state}, length {count}, pos = {pos}, {align}, {axes}, {self.pixel}"
        for i in self.get_range():
            out += f"\n {self.markers[i]} {self.labels[i]}"
        return out
