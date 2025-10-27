from plotext._matrix import matrix as matrix_class
from plotext._axes import axes_class
from plotext._methods import *
from plotext._derived import *
from plotext._correct import correct_class as correct


class legend_class:
    def __init__(self):
        self.axes = axes_class() 
        self.clear_settings() 
        self.clear_signals() 
        self.clear_signals() 
        self.set_pixel()  


    # Reset legend to initial state
    def clear_settings(self,):
        self.axes.clear_settings()
        self.set_active()
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

    def set(self, x = 0, y = 0, relative = False, status = None, ha = None, va = None, pixel = None, xside = None, yside = None):
        self.set_position(x, y, relative)
        self.set_active(status)
        self.set_alignment(ha, va)
        self.set_pixel(pixel)
        self.set_axes(xside, yside)
        return self

    # Activate or deactivate the legend
    def set_active(self, active = None):
        active = default_legend_status if active is None else active
        self.active = active
        return self

    def enable(self):
        return self.set_active(True)

    def disable(self):
        return self.set_active(False)

    # Set pixel, default if none provided
    def set_pixel(self, pixel = None, default_pixel = None):
        pixel = correct.pixel(pixel, default_legend_pixel)
        self.pixel = pixel
        self.axes.set_pixel(pixel) 
        return self

    # Set legend position (x, y) and whether position is relative
    def set_position(self, x = None, y = None, relative = None):
        self.x = default_legend_x_position if x is None else x
        self.y = default_legend_y_position if y is None else y
        self.relative = default_legend_relative if relative is None else relative
        return self

    # Set horizontal and vertical alignment
    def set_alignment(self, ha = -1, va = 1):
        ha = correct.ha(ha)
        va = correct.va(va)
        self.ha = ha  # horizontal alignment
        self.va = va  # vertical alignment
        return self

    # Set axes sides for x and y
    def set_axes(self, xside = 0, yside = 0):
        xside = correct.side(0, xside)
        yside = correct.side(1, yside)
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
    def get_absolute_position(self, axis, ruler, bins):
        col = self.x if axis == 0 else self.y
        #col = bins - 1 if col is None else col
        side = self.xside if axis == 0 else self.yside
        #direction = ruler.get_direction()

        if self.relative:
            lim = ruler.get_limits(scaled = True, direction = 1)
            delta = ruler.get_delta()
            col = int(list_methods.rescale(col, *lim, bins, delta))

        #col = bins - 1 - col if direction == -1 else col
        
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
        return max((len(el) for el in self.labels), default = 0) + 2 + frame

    # Compute height of legend (rows plus frame size)
    def get_height(self):
        frame = 4 * self.axes.get(0, 0).status
        return 2 * self.get_length() - 1 + frame

    # Get width and height as tuple
    def get_size(self):
        return self.get_width(), self.get_height()

    # Add a marker-label pair to legend
    def add(self, marker, label):
        #marker = correct.marker(marker, default_)
        label = correct.legend_label(label, self.get_length()) 
        label = correct.label(label, self.pixel)
        self.markers.append(marker) 
        self.labels.append(label) 
        return self

    # Update legend with markers and labels from signals
    def update(self, signals):
        self.clear_signals()
        for signal in signals:
            marker = signal.get_marker() 
            label = signal.get_label() 
            self.add(marker, label) 

    def fix_background(self, pixel):
        self.pixel._fix_background(pixel)
        [label._fix_background(pixel) for label in self.labels]
        [marker._fix(pixel) for marker in self.markers]
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
        out = f"Legend {state}, length {count}, pos = {pos}, {align}, {axes}, {self.pixel},  axis status {self.axes.get(0).status}, axes style {self.axes.get(0).style}"
        for i in self.get_range():
            out += f"\n {self.markers[i]} {self.labels[i]}"
        return out
