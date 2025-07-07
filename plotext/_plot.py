from plotext._build import plot_build_class
from plotext._parts import parts_class
from plotext._subplot import subplot_class
from plotext._labels import labels_class
from plotext._rulers import rulers_class
from plotext._axes import axes_class
from plotext._signal import signal_class
from plotext._signals import signals_class
from plotext._legend import legend_class

from plotext._correct import correct_class as correct
from plotext._default import default_canvas_pixel, default_lines_pixel, default_legend_pixel
from plotext._constants import r2
from plotext._matrix import join_matrices
from time import time


class plot_class(plot_build_class, subplot_class):

    def __init__(self):
        self.parts = parts_class()
        self.labels = labels_class()
        self.rulers = rulers_class()
        self.axes = axes_class()
        self.signals = signals_class()
        self._legend = legend_class()
        
        subplot_class.__init__(self)
        plot_build_class.__init__(self)

        self.canvas_pixel()


    # Subplot handling methods

    def subplots(self, rows = None, cols = None):
        subplot_class.subplots(self, rows, cols)
        if self.has_subplots():
            [self.get_subplot(*pos).clone(self) for pos in self.get_slots_range()]
        return self

    def clear(self):
        self.parts.clear()
        self.labels.clear()
        self.rulers.clear()
        self.axes.clear()
        self.signals.clear()
        self._legend.clear()
        subplot_class.clear(self)
        return self

    def clone(self, plot):
        self.labels.clone(plot.labels)
        self.rulers.clone(plot.rulers)
        self.axes.clone(plot.axes)
        self.signals.clone(plot.signals)
        self.legend.clone(plot.legend)
        return self


    # Size and label setters

    def set_size(self, width = None, height = None):
        subplot_class.set_size(self, width, height)
        self.parts.set_size(*self.get_size())
        return self



     # Ruler and axis setters




    # Additional setters

    def title(self, title = None):
        title = correct.label(title)
        self.labels.set_title(title)
        if self.has_subplots():
            [self.get_subplot(*pos).title(title) for pos in self.get_slots_range()]
        return self

    def _set_label(self, label = None, axis = 0, side = 0):
        sides = correct.sides(axis, side)
        label = correct.label(label)
        if label is not None: 
            [self.labels.set_label(axis, side, label) for side in sides] 
        if self.has_subplots():
            [self.get_subplot(*pos).xlabel(label, side) for pos in self.get_slots_range()]
        return self


    def xlabel(self, label = None, side = 0):
        return self._set_label(label = label, axis = 0, side = side)

    def ylabel(self, label = None, side = 0):
        return self._set_label(label = label, axis = 1, side = side)


    def _set_lim(self, left = None, right = None, axis = 0, side = 0):
        self.rulers.get(axis, side).set_limits(left, right)
        if self.has_subplots():
            [self.get_subplot(*pos).xlim(left, right) for pos in self.get_slots_range()]
        return self

    def xlim(self, left = None, right = None, side = 0):
        return self._set_lim(left, right, 0, side)

    def ylim(self, lower = None, upper = None, side = 0):
        return self._set_lim(lower, upper, 1, side)

    def _set_ruler(self, frequency = None, scale = None, alignment = None, direction = None, pixel = None, axis = 0, side = 0):
        sides = correct.sides(axis, side)
        alignment = correct.limits_alignment(alignment)
        direction = correct.limits_direction(direction)
        scale = correct.scale(scale)
        pixel = correct.ruler_pixel(pixel)
        [self.rulers.get(axis, side).set(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel) for side in sides]
        if self.has_subplots():
            [self.get_subplot(*pos).set_ruler(requency = frequency, axis = axis, side = side, alignment = alignment, direction = direction, scale = scale, pixel = pixel) for pos in self.get_slots_range()]
        return self

    def xruler(self, frequency = None, scale = None, alignment = None, direction = None, pixel = None, side = 0):
        return self._set_ruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, axis = 0, side = side)

    def yruler(self, frequency = None, scale = None, alignment = None, direction = None, pixel = None, side = 0):
        return self._set_ruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, axis = 1, side = side)


    def _set_ticks(self, ticks = None, labels = None, axis = 0, side = 0):
        self.rulers.get(axis, side).set_ticks(positions = ticks, labels = labels)
        if self.has_subplots():
            [self.get_subplot(*pos).xticks(ticks = ticks, labels = labels, side = side) for pos in self.get_slots_range()]
        return self

    def xticks(self, ticks = None, labels = None, side = 0):
        return self._set_ticks(ticks = ticks, labels = labels, axis = 0, side = side)

    def yticks(self, ticks = None, labels = None, side = 0):
        return self._set_ticks(ticks = ticks, labels = labels, axis = 1, side = side)



    def _set_axis(self, status = None, style = None, pixel = None, axis = 0, side = 0):
        sides = correct.sides(axis, side)
        style = correct.axis_style(style)
        pixel = correct.axis_pixel(pixel)
        [self.axes.get(axis, side).set(status, style, pixel) for side in sides]
        if self.has_subplots():
            [self.get_subplot(*pos).xaxis(side = side, status = status, style = style, pixel = pixel) for pos in self.get_slots_range()]
        return self

    def xaxis(self, status = None, style = None, pixel = None, side = 0):
        return self._set_axis(status = status, style = style, pixel = pixel, axis = 0, side = side)

    def yaxis(self, status = None, style = None, pixel = None, side = 0):
        return self._set_axis(status = status, style = style, pixel = pixel, axis = 1, side = side)

    def frame(self, frame = True, style = None, pixel = None):
        self.xaxis(frame, style = style, pixel = pixel, side = r2)
        self.yaxis(frame, style = style, pixel = pixel, side = r2)
        return self



    def canvas_pixel(self, pixel = None):
        self._canvas_pixel = correct.pixel(pixel, default_canvas_pixel)
        if self.has_subplots():
            [self.get_subplot(*pos).canvas_pixel(pixel) for pos in self.get_slots_range()]
        return self


    # Add a line to the specified ruler with given properties
    def _add_line(self, position, style = None, pixel = None, axis = 0, side = 0):
        #orientation = correct.orientation(orientation)
        sides = correct.sides(axis, side)
        style = correct.line_style(style)
        pixel = correct.pixel(pixel, default_lines_pixel)
        [self.rulers.add_line(position, style, pixel, axis, side) for side in sides]
        if self.has_subplots():
            [self.get_subplot(*pos)._add_line(axis = axis, position = position, side = side, status = status, style = style, pixel = pixel) for pos in self.get_slots_range()]
        return self

    def xline(self, position, style = None, pixel = None, side = 0):
        return self._add_line(position = position, style = style, axis = 0, side = side)


    def legend(self, x = 0, y = 0, relative = False, active = True, ha = -1, va = 1, pixel = None, xside = 0, yside = 0):
        ha = correct.ha(ha)
        va = correct.va(va)
        xside = correct.side(0, xside)
        yside = correct.side(1, yside)
        pixel = correct.pixel(pixel, default_legend_pixel)
        self._legend.set_position(x, y, relative).set_active(active).set_alignment(ha, va).set_pixel(pixel).set_axes(xside, yside)
        if self.has_subplots():
            [self.get_subplot(*pos).legend(x = x, y = y, relative = relative, active = active, ha = ha, va = va, pixel = pixel, xside = xside, yside = yside) for pos in self.get_slots_range()]
        return self

    def draw(self, x = None, y = None, m = None, xside = None, yside = None, label = None, yfill = None, mfill = None):
        x, y = correct.data(x, y)
        length = len(x)
        m = correct.markers(m, length)
        xside = correct.side(0, xside)
        yside = correct.side(1, yside)
        label = correct.signal_label(label, length)
        signal = signal_class(x, y, m, xside, yside, label)
        if yfill is not None:
            x, yfill = correct.data(x, yfill)
            mfill = m if mfill is None else mfill
            mfill = correct.markers(mfill, length)
            signal.set_fill(x, yfill, mfill)
        self.signals.add(signal)
        marker = signal.get(0).get_marker()
        label = correct.label(signal.label, self._legend.pixel)
        self._legend.add(marker, label)
        if self.has_subplots():
            [self.get_subplot(*pos).draw(x = x, y = y, m = m, xside = xside, yside = yside, label = label, yfill = yfill, mfill = mfill) for pos in self.get_slots_range()]
        return self 


    # Build and show methods

    def show(self):
        t = time()
        out = self.build()
        out.print()
        self._time = time() - t

    def build(self):
        if self.no_subplots():
            out = self.get_plot_matrix()
        else:
            matrices = [[self.get_subplot(row, col).get_plot_matrix() for col in self.get_cols_range()] for row in self.get_rows_range()]
            out = join_matrices(matrices)
        return out
