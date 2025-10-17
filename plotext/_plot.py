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
from plotext._derived import default_canvas_pixel
from plotext._constants import r2
from plotext._matrix import join_matrices
from plotext._timer import timer_class


class plot_class(plot_build_class, subplot_class):

    def __init__(self, parent):
        self._parts = parts_class()
        self._labels = labels_class()
        self._rulers = rulers_class()
        self._axes = axes_class()
        self._signals = signals_class()
        self._legend = legend_class()
        self._timer = timer_class()
        
        subplot_class.__init__(self, parent)
        plot_build_class.__init__(self)

        self.clear()


    # Subplot handling methods

    def subplots(self, rows = None, cols = None):
        subplot_class._subplots(self, rows, cols)
        if self._has_subplots():
            [self._get_subplot(*pos)._clone(self) for pos in self._get_slots_range()]
        return self

    def clear_size(self):
        self._parts.clear()
        subplot_class._clear(self)
        if self._has_subplots():
            [self._get_subplot(*pos).clear_size() for pos in self._get_slots_range()]
        return self

    def clear_data(self):
        self._signals.clear()
        self._legend.clear_signals()
        if self._has_subplots():
            [self._get_subplot(*pos).clear_data() for pos in self._get_slots_range()]
        return self

    def clear_settings(self):
        self._rulers.clear()
        self._axes.clear_settings()
        self._labels.clear()
        self._legend.clear_settings()

        self._rulers.set_xfrequency()
        self._rulers.set_yfrequency()

        if self._has_subplots():
            [self._get_subplot(*pos).clear_settings() for pos in self._get_slots_range()]
        return self

    def clear_pixels(self):
        self._labels.set_pixel()
        self._rulers.set_pixel()
        self._axes.set_pixel()
        self._legend.set_pixel()
        self.canvas_pixel()
        self._signals.set_default_marker().update_default_marker(self._canvas_pixel)
        if self._has_subplots():
            [self._get_subplot(*pos).clear_size() for pos in self._get_slots_range()]
        return self

    def clear(self):
        self.clear_size()
        self.clear_data()
        self.clear_settings()
        self.clear_pixels()
        return self

    def _clone(self, plot):
        self._labels.clone(plot._labels)
        self._rulers.clone(plot._rulers)
        self._axes.clone(plot._axes)
        self._signals.clone(plot._signals)
        self._legend.clone(plot._legend)
        return self


    # Size and label setters

    def _set_size(self, width = None, height = None):
        subplot_class._set_size(self, width, height)
        self._parts.set_size(*self.get_size())
        return self


    # Additional setters

    def title(self, title = None):
        self._labels.set_title(title)
        if self._has_subplots():
            [self._get_subplot(*pos).title(title) for pos in self._get_slots_range()]
        return self

    def _set_label(self, label = None, axis = 0, side = 0):
        self._labels.set_label(axis, side, label) 
        if self._has_subplots():
            [self._get_subplot(*pos).xlabel(label, side) for pos in self._get_slots_range()]
        return self


    def xlabel(self, label = None, side = 0):
        return self._set_label(label = label, axis = 0, side = side)

    def ylabel(self, label = None, side = 0):
        return self._set_label(label = label, axis = 1, side = side)


    def _set_lim(self, left = None, right = None, axis = 0, side = 0):
        self.rulers.get(axis, side).set_limits(left, right)
        if self._has_subplots():
            [self._get_subplot(*pos).xlim(left, right) for pos in self._get_slots_range()]
        return self

    def xlim(self, left = None, right = None, side = 0):
        return self._set_lim(left, right, 0, side)

    def ylim(self, lower = None, upper = None, side = 0):
        return self._set_lim(lower, upper, 1, side)

    def ruler(self, frequency = None, scale = None, alignment = None, direction = None, pixel = None, axis = None, side = None):
        self._rulers.set(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, axis = axis, side = side)
        if self._has_subplots():
            [self._get_subplot(*pos)._set_ruler(frequency = frequency, axis = axis, side = side, alignment = alignment, direction = direction, scale = scale, pixel = pixel) for pos in self._get_slots_range()]
        return self

    def xruler(self, frequency = None, scale = None, alignment = None, direction = None, pixel = None, side = None):
        return self.ruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, axis = 0, side = side)

    def yruler(self, frequency = None, scale = None, alignment = None, direction = None, pixel = None, side = None):
        return self.ruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, axis = 1, side = side)

    def _set_ticks(self, ticks = None, labels = None, axis = 0, side = 0):
        self.rulers.set_ticks(axis = axis, side = side, positions = ticks, labels = labels)
        if self._has_subplots():
            [self._get_subplot(*pos)._set_ticks(ticks = ticks, labels = labels, axis = axis, side = side) for pos in self._get_slots_range()]
        return self

    def xticks(self, ticks = None, labels = None, side = 0):
        return self._set_ticks(ticks = ticks, labels = labels, axis = 0, side = side)

    def yticks(self, ticks = None, labels = None, side = 0):
        return self._set_ticks(ticks = ticks, labels = labels, axis = 1, side = side)

    def _set_axis(self, status = None, style = None, pixel = None, axis = 0, side = 0):
        self._axes.set(axis = axis, side = side, status = status, style = style, pixel = pixel)
        if self._has_subplots():
            [self._get_subplot(*pos)._set_axis(axis = axis, side = side, status = status, style = style, pixel = pixel) for pos in self._get_slots_range()]
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
        if self._has_subplots():
            [self._get_subplot(*pos).canvas_pixel(pixel) for pos in self._get_slots_range()]
        return self


    # Add a line to the specified ruler with given properties
    def _add_line(self, position, style = None, pixel = None, axis = 0, side = 0):
        self._rulers.add_line(position, style, pixel, axis, side)
        if self._has_subplots():
            [self._get_subplot(*pos)._add_line(axis = axis, position = position, side = side, status = status, style = style, pixel = pixel) for pos in self._get_slots_range()]
        return self

    def xline(self, position, style = None, pixel = None, side = 0):
        return self._add_line(position = position, style = style, axis = 0, side = side)


    def legend(self, x = 0, y = 0, relative = False, status = True, ha = None, va = None, pixel = None, xside = None, yside = None):
        self._legend.set(x, y, relative, status, ha, va, pixel, xside, yside)
        if self._has_subplots():
            [self._get_subplot(*pos).legend(x = x, y = y, relative = relative, status = status, ha = ha, va = va, pixel = pixel, xside = xside, yside = yside) for pos in self._get_slots_range()]
        return self

    def draw(self, signal):
        self._signals.draw(signal)
        if self._has_subplots():
            [self._get_subplot(*pos).draw(signal) for pos in self._get_slots_range()]
        return self 

    def scatter(self, *args, marker = None, fillx = None, filly = None, xside = None, yside = None, label = None):
        signal = signal_class(*args, marker = marker, xside = xside, yside = yside, label = label, plot = 0)
        [signal.set_fill_point(i, point.get_x(), 0, point.get_marker()) for i, point in enumerate(signal)] if fillx else None
        [signal.set_fill_point(i, 0, point.get_y(), point.get_marker()) for i, point in enumerate(signal)] if filly else None
        self.draw(signal)
        return self

    def plot(self, *args, marker = None, fillx = None, filly = None, xside = None, yside = None, label = None):
        signal = signal_class(*args, marker = marker, xside = xside, yside = yside, label = label, plot = 1)
        [signal.set_fill_point(i, point.get_x(), 0, point.get_marker()) for i, point in enumerate(signal)] if fillx else None
        [signal.set_fill_point(i, 0, point.get_y(), point.get_marker()) for i, point in enumerate(signal)] if filly else None
        self.draw(signal)
        return self


    # def plot(self, *args, marker = None, fillx = None, filly = None, xside = None, yside = None, label = None):
    #     self._signals.plot(*args, marker = marker, fillx = fillx, filly = filly, xside = xside, label = label)
    #     signal = self._signals.get(-1)
    #     label = signal.label
    #     marker = signal.get_marker() 
    #     self._legend.add(marker, label) 
    #     return self 


    # Build and show methods

    def _start_event(self, event):
        self._timer.start(event)
        return self

    def _stop_event(self, event):
        self._timer.stop(event)
        return self

    def time(self, full = True):
        self._timer.report(full)
        return self

    def show(self):
        out = self.build()
        self._start_event("print")
        out.print()
        self._stop_event("print")


    def build(self):
        self._timer.clear()
        if self._no_subplots():
            out = self._get_plot_matrix()
        else:
            self._start_event("create matrices")
            matrices = [[self._get_subplot(row, col)._get_plot_matrix() for col in self._get_cols_range()] for row in self._get_rows_range()]
            self._stop_event("create matrices")
            self._start_event("join matrices")
            out = join_matrices(matrices)
            self._stop_event("join matrices")
        return out
