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
from plotext._default import color_sequence, default_marker_code
from plotext._matrix import join_matrices
from plotext._timer import timer_class

from plotext._draw import draw_class
from plotext._cycler import color_cycler

from plotext._marker import marker as marker_class


class plot_class(draw_class, plot_build_class, subplot_class):

    def __init__(self, parent):
        self._parts = parts_class()     
        self._labels = labels_class()   
        self._rulers = rulers_class()   
        self._axes = axes_class()       
        self._signals = signals_class()   
        self._legend = legend_class()  
        self._timer = timer_class() 
        self._cycler = color_cycler(color_sequence)   
        
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
        self._set_size(*self.get_terminal()._size) if self._is_master() else None
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
        [self._get_ruler(a, s).set_frequency() for a in r2 for s in r2]
        if self._has_subplots():
            [self._get_subplot(*pos).clear_settings() for pos in self._get_slots_range()]
        return self

    def clear_pixels(self):
        self._labels.set_pixel()
        [self._get_ruler(a, s).set_pixel() for a in r2 for s in r2]
        self._axes.set_pixel()
        self._legend.set_pixel()
        self.canvas_pixel()
        self._cycler.reset()
        #self._signals.set_default_marker().update_default_marker(self._canvas_pixel)
        if self._has_subplots():
            [self._get_subplot(*pos).clear_size() for pos in self._get_slots_range()]
        return self

    def clear(self):
        self.clear_size()
        self.clear_data()
        self.clear_settings()
        self.clear_pixels()
        return self

    clf = clear;

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

    def next_marker(self):
        return marker_class(default_marker_code, self._cycler.next_color())#._fix(self._canvas_pixel)


    def signal(self, *args, marker = None, xside = None, yside = None, plot = None, label = None):
        x, y = correct.data(*args) 
        signal = signal_class(len(x))
        m = correct.markers(marker, self.next_marker(), len(x)) 
        signal.set_points(x, y, m) 
        label = '' if label is None else label
        signal.set_details(xside, yside, label)
        signal._plot = correct.bool(plot) 
        return signal


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



    def _get_ruler(self, axis = 0, side = 0):
        return self._rulers.get(axis, side) 

    def _set_lim(self, left = None, right = None, axis = 0, side = 0):
        self._get_ruler(axis, side).set_limits(left, right)
        if self._has_subplots():
            [self._get_subplot(*pos).xlim(left, right) for pos in self._get_slots_range()]
        return self

    def xlim(self, left = None, right = None, side = 0):
        return self._set_lim(left, right, 0, side)

    def ylim(self, lower = None, upper = None, side = 0):
        return self._set_lim(lower, upper, 1, side)

    def ruler(self, axis = None, side = None, frequency = None, scale = None, alignment = None, direction = None, pixel = None):
        self._get_ruler(axis, side).set(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel)
        if self._has_subplots():
            [self._get_subplot(*pos)._set_ruler(frequency = frequency, axis = axis, side = side, alignment = alignment, direction = direction, scale = scale, pixel = pixel) for pos in self._get_slots_range()]
        return self

    def xruler(self, frequency = None, scale = None, alignment = None, direction = None, pixel = None, side = None):
        return self.ruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, axis = 0, side = side)

    def yruler(self, frequency = None, scale = None, alignment = None, direction = None, pixel = None, side = None):
        return self.ruler(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel, axis = 1, side = side)


    def convert(self, time, output = "timestamp", axis = None, side = None):
        return self._get_date(axis, side).convert(time, output)

    def date(self, form = None, active = True, axis = None, side = None):
        self._get_date(axis, side).set_form(form)._set_active(active)
        return self 

    def _get_date(self, axis = None, side = None):
        return self._get_ruler(axis, side).date



    def _set_ticks(self, ticks = None, labels = None, axis = 0, side = 0):
        self._get_ruler(axis, side).set_ticks(positions = ticks, labels = labels)
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
