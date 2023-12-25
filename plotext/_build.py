from plotext._colorize import colorize
from plotext._marker import tick, nl, space
from plotext._matrix import matrix_class
from functools import lru_cache as memorize


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

        # 300u
        [self._build_bar(xside) for xside in r2] # 900u
        
        [self._build_xticks(xside) for xside in r2] # 1.42
        [self._build_xaxis(xside) for xside in r2] # 1.78
        
        [self._build_yticks(yside) for yside in r2] # 2.4
        [self._build_yaxis(yside) for yside in r2] # 2.9
        
        [self._build_corner(xside, yside) for xside in r2 for yside in r2] # 3.12
        #6.44


##############################################
#########    Building Utilities    ###########
##############################################

    def _build_bar(self, xside):
        matrix = self._get_bar(xside)
        self._insert_matrix(*self._get_bar_position(xside), matrix)

    def _build_xticks(self, xside):
        matrix, _, _  = self._get_xticks(xside)
        self._insert_matrix(*self._get_xticks_position(xside), matrix)

    def _build_xaxis(self, xside):
        matrix = self._get_xaxis(xside)
        self._insert_matrix(*self._get_xaxis_position(xside), matrix)

    def _build_yticks(self, yside):
        matrix = self._get_yticks(yside)
        self._insert_matrix(*self._get_yticks_position(yside), matrix)

    def _build_yaxis(self, yside):
        matrix = self._get_yaxis(yside)
        self._insert_matrix(*self._get_yaxis_position(yside), matrix)

    def _build_corner(self, xside, yside):
        matrix = self._get_corner(xside, yside)
        self._insert_matrix(*self._get_corner_position(xside, yside), matrix)

        
    def _get_bar(self, xside):
        return self._get_bar_set(xside, self._width, self._get_bar_height(xside))

    def _get_xaxis(self, xside):
        width = self._get_width_canvas()
        height = self._get_xaxis_height(xside)
        _, ticks, labels = self._get_xticks(xside)
        just_do_it = ticks is not None
        matrix = matrix_class(width, height, tick.h, self._ticks_color, self._axes_color)
        Rt = range(len(ticks)) if just_do_it else range(0)
        side_tick = tick.lower if xside == 1 else tick.upper
        [matrix._insert_marker(ticks[i], 0, side_tick, self._ticks_color, self._axes_color) for i in Rt] if just_do_it else None
        return matrix
    
    @memorize
    def _get_xticks(self, xside):
        width = self._get_width_canvas()
        height = self._get_xticks_height(xside)
        ticks, labels = self._get_relative_xticks(xside)
        just_do_it = ticks is not None and height > 0
        matrix = matrix_class(width, height, background = self._axes_color)
        Rt = range(len(ticks)) if just_do_it else range(0)
        indexes = [i for i in Rt if matrix._insert_dynamic(ticks[i], 0, labels[i])] if just_do_it else None
        ticks = [ticks[i] for i in indexes] if just_do_it else None
        labels = [labels[i] for i in indexes] if just_do_it else None
        return matrix, ticks, labels

    def _get_yticks(self, yside):
        width = self._get_yticks_width(yside)
        height = self._get_height_canvas()
        ticks, labels = self._get_relative_yticks(yside)
        just_do_it = ticks is not None #and width > 0
        matrix = matrix_class(width, height, background = self._axes_color)
        Rt = range(len(ticks)) if just_do_it else range(0)
        [matrix._insert_aligned(width - 1, ticks[i], labels[i], ha = 1, check_spaces = 1) for i in Rt] if just_do_it else None
        return matrix

    def _get_yaxis(self, yside):
        ticks, labels = self._get_relative_yticks(yside)
        height = self._get_height_canvas()
        width = self._get_yaxis_width(yside)
        just_do_it = ticks is not None and width > 0
        matrix = matrix_class(width, height, tick.v, self._ticks_color, self._axes_color)
        Rt = range(len(ticks)) if just_do_it else range(0)
        side_tick = tick.l if yside == 1 else tick.r
        ticks, _ = self._get_relative_yticks(yside)
        [matrix._insert_marker(0, ticks[i], side_tick, self._ticks_color, self._axes_color) for i in Rt] if just_do_it else None
        return matrix

    def _get_corner(self, xside, yside):
        width, height = self._get_corner_size(xside, yside)
        matrix = matrix_class(width, height, background = self._axes_color)
        symbol =  tick.ul if (xside, yside) == (1, 2) else tick.ll if (xside, yside) == (2, 2) else tick.ur if (xside, yside) == (1, 1) else tick.lr
        position = (0, 0) if (xside, yside) == (1, 2) else (0, height - 1) if (xside, yside) == (2, 2) else (width - 1, 0) if (xside, yside) == (1, 1) else (width - 1, height - 1)
        add_tick = self._get_xaxis_height(xside) * self._get_yaxis_width(yside) #and width_canvas >= 0
        matrix._insert_marker(*position, symbol, self._ticks_color, self._axes_color) if add_tick  else None
        return matrix

    
    @memorize
    def _get_bar_height(self, xside):
        height = self._get_bar_status(xside)
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
    def _get_xticks_height(self, xside):
        height = int(self._get_xticks_data(xside)[0] is not None)
        height = 0 if xside == 1 and self._height < 5 else height
        height = 0 if xside == 2 and self._height < 6 else height
        return height
    

    @memorize
    def _get_yaxis_width(self, yside):
        width = int(self._yaxes[yside - 1])
        width = 0 if yside == 1 and self._width < 1 else width
        width = 0 if yside == 2 and self._width < 2 else width
        return width

    @memorize
    def _get_yticks_width(self, yside):
        _, labels = self._get_relative_yticks(yside)
        width = max([label._get_width() for label in labels]) if labels is not None else 0
        width_occupied = sum([self._get_yaxis_width(yside) for yside in [1, 2]]) + (0 if yside == 1 else  self._get_yticks_width(1))
        width = 0 if self._width - width_occupied - width < 0 else width
        return width

    
    @memorize
    def _get_corner_size(self, xside, yside):
        width = self._get_yticks_width(yside) + self._get_yaxis_width(yside)
        height = self._get_xticks_height(xside) + self._get_xaxis_height(xside)
        return width, height


    @memorize
    def _get_height_canvas(self):
        bars_height = sum([self._get_bar_height(xside) for xside in [1, 2]])
        xticks_height = sum([self._get_xticks_height(xside) for xside in [1, 2]])
        xaxis_height = sum([self._get_xaxis_height(xside) for xside in [1, 2]])
        return max(0, self._height - (bars_height + xticks_height + xaxis_height))

    @memorize
    def _get_width_canvas(self):
        corner_width = sum([self._get_corner_size(2, yside)[0] for yside in [1, 2]])
        return max(0, self._width - corner_width)


    @memorize
    def _get_canvas_position(self, xside, yside):
        col = self._get_yticks_width(1) + self._get_yaxis_width(1) if yside == 1 else self._get_canvas_position(1, 1)[0] + self._get_width_canvas()
        row = self._get_bar_height(2) + self._get_xticks_height(2) + self._get_xaxis_height(2) if xside == 2 else self._get_canvas_position(2, 1)[1] + self._get_height_canvas()
        return col, row

    def _get_bar_position(self, xside):
        row = 0 if xside == 2 else self._get_canvas_position(1, 1)[1] + self._get_xticks_height(1) + self._get_xaxis_height(1)
        return (0, row)

    @memorize
    def _get_xticks_position(self, xside):
        col = self._get_yticks_width(1) + self._get_yaxis_width(1)
        row = self._get_bar_height(2) if xside == 2 else self._get_canvas_position(1, 1)[1] + self._get_xaxis_height(1)
        return (col, row)

    @memorize
    def _get_xaxis_position(self, xside):
        col = self._get_xticks_position(1)[0]
        row = self._get_xticks_position(2)[1] + self._get_xticks_height(2) if xside == 2 else self._get_canvas_position(1, 1)[1]
        return (col, row)

    @memorize
    def _get_yticks_position(self, yside):
        col = 0 if yside == 1 else self._get_canvas_position(1, 2)[0] + self._get_yaxis_width(2)
        row = self._get_canvas_position(2, 2)[1]
        return (col, row)

    @memorize
    def _get_yaxis_position(self, yside):
        col = self._get_yticks_width(1) if yside == 1 else self._get_canvas_position(1, 2)[0]
        row = self._get_yticks_position(yside)[1]
        return (col, row)

    def _get_corner_position(self, xside, yside):
        col = 0 if yside == 1 else self._get_yaxis_position(2)[0]
        row = self._get_canvas_position(1, 1)[1] if xside == 1 else self._get_xticks_position(2)[1]
        return (col, row)

    
    @memorize
    def _get_xticks_data(self, xside):
        frequency = self._get_xfrequency(xside)
        ticks = self._get_xticks_set(xside)
        lim = self._get_xlim(xside)
        just_do_it = ticks is None and None not in lim
        ticks = linspace(*lim, frequency) if just_do_it else ticks
        labels = self._get_xlabels(xside)
        just_do_it = ticks is not None and labels is None
        labels = get_labels(ticks) if just_do_it else labels
        labels = self.color_labels(labels) if just_do_it else labels
        return ticks, labels

    @memorize
    def _get_yticks_data(self, yside):
        frequency = self._get_yfrequency(yside)
        ticks = self._get_yticks_set(yside)
        lim = self._get_ylim(yside)
        just_do_it = ticks is None and None not in lim
        ticks = linspace(*lim, frequency, self._get_yscale(yside)) if just_do_it else ticks
        labels = self._get_ylabels(yside)
        just_do_it = ticks is not None and labels is None
        labels = get_labels(ticks) if just_do_it else labels
        labels = self.color_labels(labels) if just_do_it else labels
        return ticks, labels

    def _get_relative_xticks(self, xside):
        width = self._get_width_canvas()
        ticks, labels = self._get_xticks_data(xside)
        lim = self._get_xlim(xside)
        ticks = digitize(ticks, lim, width, self._get_xscale(xside)) if ticks is not None and None not in lim and width > 0 else None
        ticks = None if ticks is None else ticks if self._get_xdirection(xside) == 1 else [width - 1 - el for el in ticks]
        return ticks, labels

    @memorize
    def _get_relative_yticks(self, yside):
        height = self._get_height_canvas()
        ticks, labels = self._get_yticks_data(yside)
        lim = self._get_ylim(yside)
        ticks = digitize(ticks, lim, height, self._get_yscale(yside)) if ticks is not None and None not in lim and height > 0 else None
        ticks = None if ticks is None else (ticks if self._get_ydirection(yside) == -1 else [height - 1 - el for el in ticks])
        return ticks, labels

    @memorize
    def _get_xlim(self, xside):
        return replace_none(self._get_xlim_set(xside), self._get_xlim_signals(xside))

    @memorize
    def _get_ylim(self, yside):
        return replace_none(self._get_ylim_set(yside), self._get_ylim_signals(yside))

    color_labels = lambda self, labels: [colorize(label, self._ticks_color, self._axes_color) for label in labels]
    
    def _update_matrix_size(self):
        self._resize(*self._size, self._canvas_color)

    def _clear_memorized_methods(self):
        self._get_xticks.cache_clear()
       
        self._get_bar_height.cache_clear()
        self._get_xaxis_height.cache_clear()
        self._get_xticks_height.cache_clear()
        self._get_yticks_width.cache_clear()
        self._get_yaxis_width.cache_clear()        
        self._get_corner_size.cache_clear()
        
        self._get_height_canvas.cache_clear()
        self._get_width_canvas.cache_clear()
        
        self._get_canvas_position.cache_clear()
        self._get_xticks_position.cache_clear()
        self._get_xaxis_position.cache_clear()
        
        self._get_yticks_position.cache_clear()
        self._get_yaxis_position.cache_clear()
        
        self._get_xticks_data.cache_clear()
        self._get_yticks_data.cache_clear()
        self._get_relative_yticks.cache_clear()
        self._get_xlim.cache_clear()
        self._get_ylim.cache_clear()

    def _join_matrices(self):
        cumulative_width = self._get_cumulative_widths()
        cumulative_height = self._get_cumulative_heights()
        [self._insert_matrix(cumulative_width[col - 1], cumulative_height[row - 1], self._get_subplot(row, col)) for col in self._Cols for row in self._Rows]
        
 
##############################################
#########    Function Utilities    ###########
##############################################

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
    change = lambda el: 0.5 + (bins - 1) * (el - lim[0]) / (lim[1] - lim[0])
    data = [change(el) for el in data]
    data = list(map(math.floor, data)) #if round else data
    return data

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

# def get_frame(width, height):
#     Width = range(width); Height = range(height)
#     matrix = [[tick.h] * width if row in [0, height - 1] else [tick.v if col in [0, width - 1] else space for col in Width] for row in Height]
#     if width * height != 0:
#         matrix[0][0] = tick.lower_right
#         matrix[0][-1] = tick.lower_left
#         matrix[-1][0] = tick.upper_right
#         matrix[-1][-1] = tick.upper_left
#     return nl.join([''.join(row) for row in matrix])
