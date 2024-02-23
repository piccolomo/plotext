from plotext._colorize import colorize
from plotext._matrix import matrix_class
from functools import lru_cache as memorize
from plotext._converter import get_data_type
from plotext._hd_marker import hd_marker_codes, sum_tuples
from plotext._default import default_settings


class build_class():
    
    def show(self):
        self._build()
        self._print()

    def build(self, colorless = False):
        self._build()
        return self._get_string(colorless)

    def _build(self):
        self.extend('_build') if self._has_subplots else None
        self._clear_memorized_methods()
        self._update_matrix_size()
        self._build_plot() if not self._has_subplots else None
        self._join_matrices() if self._has_subplots else None

    def _build_plot(self):
        r2 = [1, 2]
        
        [self._build_bar(xside) for xside in r2]
        [self._build_ticks(axis, side) for axis in r2 for side in r2]
        [self._build_axis(axis, side) for axis in r2 for side in r2]
        [self._build_corner(xside, yside) for xside in r2 for yside in r2]
        self._add_signals()


##############################################
#########    Building Utilities    ###########
##############################################

    def _build_bar(self, xside):
        self._insert_matrix(*self._get_bar_position(xside), self._get_bar(xside))

    def _build_ticks(self, axis, side):
        self._insert_matrix(*self._get_ticks_position(axis, side), self._get_ticks(axis, side)[0])

    def _build_axis(self, axis, side):
        self._insert_matrix(*self._get_axis_position(axis, side), self._get_axis(axis, side))

    def _build_corner(self, xside, yside):
        self._insert_matrix(*self._get_corner_position(xside, yside), self._get_corner(xside, yside))

        
    def _get_bar(self, xside):
        return self._get_set_bar(xside, *self._get_bar_size(xside))

    def _get_ticks(self, axis, side):
        width, height = self._get_ticks_size(axis, side)
        ticks, labels = self._get_relative_ticks(axis, side)
        just_do_it = width != 0 and height != 0
        matrix = matrix_class(width, height, background = self._axes_color)
        Rt = range(len(ticks)) if just_do_it else range(0)
        indexes = [i for i in Rt if matrix._insert_dynamic(ticks[i], 0, labels[i])] if axis == 1 and just_do_it else None
        ticks = [ticks[i] for i in indexes] if just_do_it and axis == 1 else ticks
        labels = [labels[i] for i in indexes] if just_do_it and axis ==1 else labels
        [matrix._insert_aligned(width - 1, ticks[i], labels[i], ha = 1, check_spaces = 1) for i in Rt] if just_do_it and axis == 2 else None
        return matrix, ticks, labels
    
    def _get_axis(self, axis, side):
        coord, ticks = transpose(self._get_axis_marks(axis, side), 2)
        coord = [(c, 0) if axis == 1 else (0, c) for c in coord]
        size = self._get_axis_size(axis, side)
        t = self._tick.horizontal if axis == 1 else self._tick.vertical
        matrix = matrix_class(*size, t, self._ticks_color, self._axes_color)
        Rt = range(len(ticks))
        [matrix._insert_matrix(*coord[i], ticks[i]) for i in Rt] if 0 not in size else None
        return matrix

    def _get_corner(self, xside, yside):
        width, height = self._get_corner_size(xside, yside)
        matrix = matrix_class(width, height, background = self._axes_color)
        symbol =  self._tick.upper_left if (xside, yside) == (1, 2) else self._tick.lower_left if (xside, yside) == (2, 2) else self._tick.upper_right if (xside, yside) == (1, 1) else self._tick.lower_right
        position = (0, 0) if (xside, yside) == (1, 2) else (0, height - 1) if (xside, yside) == (2, 2) else (width - 1, 0) if (xside, yside) == (1, 1) else (width - 1, height - 1)
        add_tick = self._get_xaxis_height(xside) * self._get_yaxis_width(yside) #and width_canvas >= 0
        symbol = colorize(symbol, self._ticks_color, self._axes_color)
        matrix._insert_matrix(*position, symbol) if add_tick else None
        return matrix

    #def _get_grid(self, ) # transform into signals
    
    def _add_signals(self):
        xoffset, yoffset = self._get_canvas_position(2, 1)
        width, height = self._get_canvas_width(), self._get_canvas_height()
        for signal in self._signals:
            m = signal.marker
            l = len(m)
            xres, yres = m[0].resolution(False) if l > 0 else (1, 1)
            hd =  xres * yres != 1 and l > 0
            xside, yside = signal.xside, signal.yside
            lines = signal.lines
            fillx = signal.fillx
            filly = signal.filly
            xlim = self._get_real_lim(1, xside)
            ylim = self._get_real_lim(2, yside)
            x = digitize(signal.x, xlim, xres * width, self._get_set_scale(1, xside))
            y = digitize(signal.y, ylim, yres * height, self._get_set_scale(2, yside))
            x, y, m = transpose(get_lines(x, y, m)) if lines else (x, y, m)
            x, y, m = fill(x, y, m, filly) if filly else (x, y, m)
            y, x, m = fill(y, x, m, fillx) if fillx else (y, x, m)
            x, y, m = brush(x, y, m)
            x = change_direction(x, self._get_set_direction(1, xside), xres * width)
            y = change_direction(y, -self._get_set_direction(2, yside), yres * height)
            x = divide(x, xres); y = divide(y, yres)
            #x, y, m = transpose(sorted(transpose([x, y, m])))
            x, y, m = get_hd_markers(x, y, m) if hd else (floor(x), floor(y), m)
            #m = [el.colorize() for el in m]
            x = add(x, xoffset); y = add(y, yoffset)
            #m = self._colorize(m)
            #m = [el._select(0, 0, 1, 1) for el in self._colorize(m)]
            [self._insert_aligned(x[i], y[i], m[i], 0, 0) for i in range(len(x))] #if not lines else self._insert_lines(x, y, m)

    def _get_bar_size(self, xside):
        return self._width, self._get_bar_height(xside)

    def _get_axis_size(self, axis, side):
        return self._get_xaxis_size(side) if axis == 1 else self._get_yaxis_size(side)

    def _get_xaxis_size(self, xside):
        return (self._get_canvas_width(), self._get_xaxis_height(xside))

    def _get_yaxis_size(self, yside):
        return (self._get_yaxis_width(yside), self._get_canvas_height())

    def _get_ticks_size(self, axis, side):
        return self._get_xticks_size(side) if axis == 1 else self._get_yticks_size(side)

    def _get_xticks_size(self, xside):
         return (self._get_canvas_width(), self._get_xticks_height(xside))

    def _get_yticks_size(self, yside):
         return (self._get_yticks_width(yside), self._get_canvas_height())

    @memorize
    def _get_canvas_length(self, axis):
         return self._get_canvas_width() if axis == 1 else self._get_canvas_height()


    @memorize
    def _get_bar_height(self, xside):
        height = int(self._get_bar_status(xside))
        height = 0 if xside == 1 and self._height < 1 else height
        height = 0 if xside == 2 and self._height < 2 else height
        return height

    @memorize
    def _get_xaxis_height(self, xside):
        height = int(self._xaxes[xside - 1])
        height = 0 if xside == 1 and self._height < 3 else height
        height = 0 if xside == 2 and self._height < 4 else height
        return height

    @memorize
    def _get_yaxis_width(self, yside):
        width = int(self._yaxes[yside - 1])
        width = 0 if yside == 1 and self._width < 1 else width
        width = 0 if yside == 2 and self._width < 2 else width
        return width

    @memorize
    def _get_xticks_height(self, xside):
        height = int(self._get_ticks_data(1, xside)[0] is not None)
        height = 0 if xside == 1 and self._height < 5 else height
        height = 0 if xside == 2 and self._height < 6 else height
        return height
    
    @memorize
    def _get_yticks_width(self, yside):
        _, labels = self._get_relative_ticks(2, yside)
        width = max([label._get_width() for label in labels], default = 0)
        width_occupied = sum([self._get_yaxis_width(yside) for yside in [1, 2]]) + (0 if yside == 1 else  self._get_yticks_width(1))
        width = 0 if self._width - width_occupied - width < 0 else width
        return width

    @memorize
    def _get_canvas_height(self):
        bars_height = sum([self._get_bar_height(xside) for xside in [1, 2]])
        xticks_height = sum([self._get_xticks_height(xside) for xside in [1, 2]])
        xaxis_height = sum([self._get_xaxis_height(xside) for xside in [1, 2]])
        return max(0, self._height - (bars_height + xticks_height + xaxis_height))

    @memorize
    def _get_canvas_width(self):
        corner_width = sum([self._get_corner_size(2, yside)[0] for yside in [1, 2]])
        return max(0, self._width - corner_width)

    @memorize
    def _get_corner_size(self, xside, yside):
        width = self._get_yticks_width(yside) + self._get_yaxis_width(yside)
        height = self._get_xticks_height(xside) + self._get_xaxis_height(xside)
        return width, height


    
    def _get_bar_position(self, xside):
        row = 0 if xside == 2 else self._get_canvas_position(1, 1)[1] + self._get_xticks_height(1) + self._get_xaxis_height(1)
        return (0, row)

    def _get_axis_position(self, axis, side):
        return self._get_xaxis_position(side) if axis == 1 else self._get_yaxis_position(side)

    def _get_ticks_position(self, axis, side):
        return self._get_xticks_position(side) if axis == 1 else self._get_yticks_position(side)

    @memorize
    def _get_canvas_position(self, xside, yside):
        col = self._get_yticks_width(1) + self._get_yaxis_width(1) if yside == 1 else self._get_canvas_position(1, 1)[0] + self._get_canvas_width()
        row = self._get_bar_height(2) + self._get_xticks_height(2) + self._get_xaxis_height(2) if xside == 2 else self._get_canvas_position(2, 1)[1] + self._get_canvas_height()
        return col, row

    def _get_xaxis_position(self, xside):
        col = self._get_xticks_position(1)[0]
        row = self._get_xticks_position(2)[1] + self._get_xticks_height(2) if xside == 2 else self._get_canvas_position(1, 1)[1]
        return (col, row)

    @memorize
    def _get_yaxis_position(self, yside):
        col = self._get_yticks_width(1) if yside == 1 else self._get_canvas_position(1, 2)[0]
        row = self._get_yticks_position(yside)[1]
        return (col, row)

    @memorize
    def _get_xticks_position(self, xside):
        col = self._get_yticks_width(1) + self._get_yaxis_width(1)
        row = self._get_bar_height(2) if xside == 2 else self._get_canvas_position(1, 1)[1] + self._get_xaxis_height(1)
        return (col, row)

    @memorize
    def _get_yticks_position(self, yside):
        col = 0 if yside == 1 else self._get_canvas_position(1, 2)[0] + self._get_yaxis_width(2)
        row = self._get_canvas_position(2, 2)[1]
        return (col, row)

    def _get_corner_position(self, xside, yside):
        col = 0 if yside == 1 else self._get_yaxis_position(2)[0]
        row = self._get_canvas_position(1, 1)[1] if xside == 1 else self._get_xticks_position(2)[1]
        return (col, row)


    @memorize
    def _compute_ticks(self, axis, side):
        lim, frequency = self._get_real_lim(axis, side), self._get_set_frequency(axis, side)
        just_do_it = None not in lim
        ticks = linspace(*lim, frequency) if just_do_it else []
        return ticks

    @memorize
    def _get_ticks_data(self, axis, side):
        ticks, labels = self._get_set_ticks(axis, side), self._get_set_labels(axis, side)
        converter = self._string_converter(axis, side)
        ticks = converter.convert(ticks) if len(ticks) > 0 and get_data_type(ticks) == 'string' else ticks
        ticks = self._compute_ticks(axis, side) if len(ticks) == 0 else ticks
        labels_needed = lambda: len(ticks) > 0 and len(labels) == 0
        converter = self._date(axis, side)
        is_datetime = labels_needed() and get_data_type(ticks) == 'datetime'
        labels = converter.datetimes_to_strings(ticks) if is_datetime else labels
        labels = get_labels(ticks) if labels_needed()  else labels
        labels = self.color_labels(labels)
        return ticks, labels
    

    @memorize
    def _get_relative_ticks(self, axis, side):
        length = self._get_canvas_length(axis)
        ticks, labels = self._get_ticks_data(axis, side)
        lim = self._get_real_lim(axis, side)
        ticks = digitize(ticks, lim, length, self._get_set_scale(axis, side)) if ticks is not None and None not in lim and length > 0 else []
        ticks = ticks if self._get_set_direction(axis, side) == (1 if axis == 1 else -1) else [length - 1 - el for el in ticks]
        return ticks, labels

    @memorize
    def _get_relative_lines(self, axis, side):
        length = self._get_canvas_length(axis)
        lim = self._get_real_lim(axis, side)
        ticks = digitize(self._get_set_lines(axis, side), lim, length, self._get_set_scale(axis, side)) if None not in lim and length > 0 else []
        ticks = ticks if self._get_set_direction(axis, side) == 1 else [length - 1 - el for el in ticks]
        return ticks

    def _get_axis_numerical_marks(self, axis, side):
        ticks, _ = self._get_relative_ticks(axis, side); lt = len(ticks)
        number_tick = (self._tick.lower if side == 1 else self._tick.upper) if axis == 1 else (self._tick.left if side == 1 else self._tick.right)
        tc, ac = self._ticks_color, self._axes_color
        number_tick = (self._tick.lower if side == 1 else self._tick.upper) if axis == 1 else (self._tick.left if side == 1 else self._tick.right)
        ticks = [(ticks[i], colorize(number_tick, self._ticks_color, self._axes_color)) for i in range(lt)]
        return ticks

    def _get_axis_lines_marks(self, axis, side):
        lines1 = self._get_relative_lines(axis, 1); l1 = len(lines1)
        lines2 = self._get_relative_lines(axis, 2); l2 = len(lines2)
        colors1 = self._get_set_lines_colors(axis, 1)
        colors2 = self._get_set_lines_colors(axis, 2)
        lines_tick = (self._tick.upper if side == 1 else self._tick.lower) if axis == 1 else (self._tick.right if side == 1 else self._tick.left)
        lines1 = [(lines1[i], colorize(lines_tick, colors1[i], self._axes_color)) for i in range(l1)]
        lines2 = [(lines2[i], colorize(lines_tick, colors2[i], self._axes_color)) for i in range(l2)]
        lines = lines1 + lines2
        return lines
        
    def _get_axis_marks(self, axis, side):
        numerical = self._get_axis_numerical_marks(axis, side)
        lines = self._get_axis_lines_marks(axis, side)
        
        lines0 = transpose(lines)[0] if len(lines) > 0 else [];
        numerical0 = transpose(numerical)[0] if len(numerical) > 0 else []
        
        pure_numerical = [el for el in numerical if el[0] not in lines0]
        pure_lines = [el for el in lines if el[0] not in numerical0]
        common = [(el[0], self._tick.cross, el[2], el[3]) for el in lines if el[0] in numerical0]
        return pure_numerical + pure_lines + common


    @memorize
    def _get_real_lim(self, axis, side):
        lim = replace_none(self._get_set_lim(axis, side), self._get_signals_lim(axis, side))
        lim = [(1 - default_settings.lim_delta) * lim[0], (1 + default_settings.lim_delta) * lim[1]] if None not in lim and lim[0] == lim[1] else lim
        return lim

    color_labels = lambda self, labels: [colorize(label, self._ticks_color, self._axes_color) for label in labels]
    
    def _update_matrix_size(self):
        self._resize(*self._size, self._canvas_color)

    def _clear_memorized_methods(self):
         self._get_canvas_length.cache_clear()
         self._get_bar_height.cache_clear()
         self._get_xaxis_height.cache_clear()
         self._get_yaxis_width.cache_clear()        
         self._get_xticks_height.cache_clear()
         self._get_yticks_width.cache_clear()
         self._get_canvas_height.cache_clear()
         self._get_canvas_width.cache_clear()
         self._get_corner_size.cache_clear()
         self._get_canvas_position.cache_clear()
         self._get_yaxis_position.cache_clear()
         self._get_xticks_position.cache_clear()
         self._get_yticks_position.cache_clear()
         self._compute_ticks.cache_clear()
         self._get_ticks_data.cache_clear()
         self._get_relative_ticks.cache_clear()
         self._get_relative_lines.cache_clear()
         self._get_real_lim.cache_clear()

    def _join_matrices(self):
        cumulative_width = self._get_cumulative_widths()
        cumulative_height = self._get_cumulative_heights()
        [self._insert_matrix(cumulative_width[col - 1], cumulative_height[row - 1], self._get_subplot(row, col)) for col in self._Cols for row in self._Rows]

    def _colorize(self, strings):
        return  [el if isinstance(el, colorize) else colorize(el, self._ticks_color, self._axes_color) for el in strings]

##############################################
#########    Function Utilities    ###########
##############################################

import itertools
import math

replace_none = lambda data, new: [data[i] if data[i] is not None else new[i]for i in range(len(data))] 

def set_element(data, index, value):
    data[index] = value

def linspace(lower, upper, length = 10, scale = 'linear'): # it returns a lists of numbers from lower to upper with given length
    upper, lower = log10([upper, lower]) if scale == 'log' else (upper, lower)
    slope = (upper - lower) / (length - 1) if length > 1 else 0
    data = [lower + x * slope for x in range(length)]
    data = power10(data) if scale == 'log' else data
    return data

def digitize(data, lim, bins, scale = 'linear'):
    data = log10(data) if scale == 'log' else data
    lim = log10(lim) if scale == 'log' else lim
    data = rescale(data, lim, bins)
    return floor(data)

def rescale(data, lim, bins):
    change = lambda el: 0.5 + (bins - 1) * (el - lim[0]) / (lim[1] - lim[0])
    data = [change(el) for el in data]
    return data

def floor(data):
    return list(map(math.floor, data))

def log10(data): # it apply log function to the data
    return [math.log10(el) for el in data]

def power10(data): # it apply log function to the data
    return [10 ** el for el in data]

def get_labels(ticks): # it returns the approximated string version of the data ticks
    d = get_distinguishing_digit(ticks)
    formatting_string ="{:." + str(d + 1) + "f}"
    labels = [formatting_string.format(el) for el in ticks]
    return labels

def get_distinguishing_digit(data): # it return the minimum amount of decimal digits necessary to distinguish all elements of a list
    d = [_get_distinguishing_digit(data[i], data[i + 1]) for i in range(len(data) - 1)]
    return max(d, default = 1)

def _get_distinguishing_digit(a, b): # it return the minimum amount of decimal digits necessary to distinguish a from b
    d = abs(a - b)
    d = 0 if d == 0 else - math.log10(2 * d)
    d = 0 if d < 0 else math.ceil(d)
    return d

def transpose(data, length = 1): # it needs no explanation
    return [[]] * length if data == [] else list(map(list, zip(*data)))

def change_direction(data, direction, length):
    return data if direction == 1 else [length - 1 - el for el in data]

def add(data, offset):
    return [el + offset for el in data]

def get_line(x1, y1, x2, y2, m):
    delta_x = x2 - x1
    delta_y = y2 - y1
    range_y = range(min(y1, y2), max(y1, y2))
    range_x = range(min(x1, x2), max(x1, x2))
    if delta_x == 0:
        return [(x1, y, m) for y in range_y]
    elif delta_y == 0:
        return [(x, y1, m) for x in range_x]
    else:
        s = delta_x / delta_y; si = s ** (-1)
        points_y = [(round(x1 + s * (y - y1)), y, m) for y in range_y]
        points_x = [(x, round(y1 + si * (x - x1)), m) for x in range_x]
        return list(set(points_y + points_x))
    
def get_lines(x, y, m):
    L = range(len(x) - 1)
    return join([get_line(x[i], y[i], x[i + 1], y[i + 1], m[i]) for i in L]) + [(x[-1], y[-1], m[-1])]

def join(data): # flatten lists at first level
    #return [el for row in data for el in row]
    return [el for row in data for el in (join(row) if type (row) == list else [row])]

def divide(data, factor):
    return [el / factor for el in data]

from collections import defaultdict

def get_hd_markers(x, y, m):
    L = range(len(x))
    marker = m[0].get_string(True)
    marker = hd_marker_codes[marker]
    xf = floor(x); yf = floor(y)
    xy = []; mn = []; t = []
    for i in L:
        xyi = xf[i], yf[i]
        ti = marker.get_tuple(x[i], y[i])
        if xyi not in xy:
            xy.append(xyi)
            mn.append(m[i].copy())
            t.append(ti)
        else:
            index = xy.index(xyi)
            t[index] = sum_tuples(t[index], ti)
    s = [marker.get_marker(el) for el in t]
    m = [mn[i]._reset_string(s[i]) for i in range(len(s))]
    x, y = transpose(xy, 2)
    return x, y, m

def fill(x, y, m, method = None):
    xn, yn, mn = [], [], []
    l = len(x); L = range(l)
    ymin = [min([y[j] for j in L if x[i] == x[j]]) for i in L] if method == 'internal' else [0] * l 
    for i in L:
        for y_new in range(ymin[i], y[i] + 1):
            xn.append(x[i])
            yn.append(y_new)
            mn.append(m[i])
    return xn, yn, mn

def brush(*lists):
    return transpose(no_duplicates(transpose(lists, len(lists))))

def no_duplicates(data): # removes duplicates from a list
    data.sort(key = lambda el: el[:2])
    return list(k for k, _ in itertools.groupby(data))
    #return list(set(list(data)))
    


# def get_frame(width, height):
#     Width = range(width); Height = range(height)
#     matrix = [[self._tick.h] * width if row in [0, height - 1] else [self._tick.v if col in [0, width - 1] else space for col in Width] for row in Height]
#     if width * height != 0:
#         matrix[0][0] = tick.lower_right
#         matrix[0][-1] = tick.lower_left
#         matrix[-1][0] = tick.upper_right
#         matrix[-1][-1] = tick.upper_left
#     return nl.join([''.join(row) for row in matrix])
