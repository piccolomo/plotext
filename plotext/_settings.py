from plotext._default import default_settings
from plotext._placement import placement
from plotext._colorize import colorize, matrix_class
from plotext._marker import tick_class


class settings_class():
    def __init__(self):
        self._bar_upper = bar_upper_class()
        self._bar_lower = bar_lower_class()
        self.clear_settings()

    def clear_settings(self):
        self._clear_bars()
        self.clear_color()
        self._init_axes()
        self._init_grid()
        self._set_frame_style()
        self._init_lim()
        self._init_frequency()
        self._init_ticks()
        self._init_direction()
        self._init_scale()
        self._init_lines()

    def _clear_bars(self):
        self._bar_upper.clear()
        self._bar_lower.clear()

    def clear_color(self):
        self.ticks_color()
        self.axes_color()
        self.canvas_color()
       
    def _init_axes(self):
        self._xaxes = [default_settings.frame] * 2
        self._yaxes = [default_settings.frame] * 2

    def _init_grid(self):
        self._grid = [default_settings.grid] * 2

    def _set_frame_style(self, style = None):
        self._tick = tick_class(style)
        
    def _init_lim(self):
        self._xlim = [[None, None], [None, None]]
        self._ylim = [[None, None], [None, None]]

    def _init_frequency(self):
        self._xfrequency = [default_settings.xfrequency] * 2 
        self._yfrequency = [default_settings.yfrequency] * 2 
    
    def _init_ticks(self):
        self._xticks = [[], []]
        self._yticks = [[], []]
        self._xlabels = [[], []]
        self._ylabels = [[], []]

    def _init_direction(self):
        self._xdirection = [default_settings.xdirection] * 2
        self._ydirection = [default_settings.xdirection] * 2

    def _init_scale(self):
        self._xscale = [default_settings.scale] * 2
        self._yscale = [default_settings.scale] * 2

    def _init_lines(self):
        self._hlines = [[], []]
        self._vlines = [[], []]
        self._hcolors = [[], []]
        self._vcolors = [[], []]
        
# User Functions

    def ticks_color(self, color = None):
        self.extend('ticks_color', color)
        self._ticks_color = color if color is not None else default_settings.ticks_color
        return self
        
    def axes_color(self, color = None):
        self.extend('axes_color', color)
        self._axes_color = color if color is not None else default_settings.axes_color
        return self
    
    def canvas_color(self, color = None):
        self.extend('canvas_color', color)
        self._canvas_color = color if color is not None else default_settings.canvas_color
        return self
        
    def title(self, label = None):
        self.extend('title', label)
        label = self._correct_label(label)
        self._bar_upper.set_title(label)
        return self
        
    def xlabel(self, label = None, xside = None):
        self.extend('xlabel', label, xside)
        label = self._correct_label(label)
        xside = placement.correct_xside(xside)
        self._bar_lower.set_center(label) if xside == 'lower' else self._bar_upper.set_label(label)
        return self
    
    def ylabel(self, label = None, yside = None):
        self.extend('ylabel', label, yside)
        label = self._correct_label(label)
        yside = placement.correct_yside(yside)
        self._bar_lower.set_left(label) if yside == 'left' else self._bar_lower.set_right(label)
        return self

    def xaxes(self, lower = None, upper = None):
        self.extend('xaxes', lower, upper)
        self._xaxes[0] = default_settings.frame if lower is None else bool(lower)
        self._xaxes[1] = default_settings.frame  if upper is None else bool(upper)
        return self

    def yaxes(self, left = None, right = None):
        self.extend('yaxes', left, right)
        self._yaxes[0] = default_settings.frame if left is None else bool(left)
        self._yaxes[1] = default_settings.frame if right is None else bool(right)
        return self

    def frame(self, frame = None, style = None):
        self.extend('frame', frame)
        self.xaxes(frame, frame)
        self.yaxes(frame, frame)
        self._set_frame_style(style)
        return self

    def xlim(self, left = None, right = None, xside = None):
        self.extend('xlim', left, right, xside)
        index = placement.xside_to_index(xside)
        self._xlim[index] = [left, right]
        return self

    def ylim(self, lower = None, upper = None, yside = None):
        self.extend('ylim', lower, upper, yside)
        index = placement.yside_to_index(yside)
        self._ylim[index] = [lower, upper]
        return self

    def xfrequency(self, frequency = None, xside = None):
        self.extend('xfrequency', frequency, xside)
        index = placement.xside_to_index(xside)
        self._xfrequency[index] = default_settings.xfrequency if frequency is None else int(frequency)
        return self
      
    def yfrequency(self, frequency = None, yside = None):
        self.extend('yfrequency', frequency, yside)
        index = placement.yside_to_index(yside)
        self._yfrequency[index] = default_settings.yfrequency if frequency is None else int(frequency)
        return self

    def xticks(self, ticks = None, labels = None, xside = None):
        self.extend('xticks', ticks, labels, xside)
        index = placement.xside_to_index(xside)
        self._xticks[index] = ticks if ticks is not None else []
        self._xlabels[index] = labels if labels is not None else []
        xfrequency = len(ticks)
        self.xfrequency(xfrequency, xside)
        return self

    def yticks(self, ticks = None, labels = None, yside = None):
        self.extend('yticks', ticks, labels, yside)
        index = placement.yside_to_index(yside)
        self._yticks[index] = ticks if ticks is not None else []
        self._ylabels[index] = labels if labels is not None else []
        yfrequency = len(ticks)
        self.yfrequency(yfrequency, yside)
        return self

    def xdirection(self, direction = None, xside = None):
        self.extend('xdirection', direction, xside)
        index = placement.xside_to_index(xside)
        direction = default_settings.xdirection if direction is None or direction not in [1, -1] else direction
        self._xdirection[index] = direction
        return self

    def ydirection(self, direction = None, yside = None):
        self.extend('ydirection', direction, yside)
        index = placement.yside_to_index(yside)
        direction = default_settings.ydirection if direction is None or direction not in [1, -1] else direction
        self._ydirection[index] = direction
        return self

    def xscale(self, scale = None, xside = None):
        self.extend('xscale', scale, xside)
        index = placement.xside_to_index(xside)
        default_case = scale is None or scale not in default_settings.scales
        scale = default_settings.scale if default_case else scale
        self._xscale[index] = scale
        return self


    def yscale(self, scale = None, yside = None):
        self.extend('yscale', scale, yside)
        index = placement.yside_to_index(yside)
        default_case = scale is None or scale not in default_settings.scales
        scale = default_settings.scale if default_case else scale
        self._yscale[index] = scale
        return self

# Get Functions

    def _get_set_bar(self, xside, width, height):
        return self._bar_lower.get(width, height, self._axes_color) if xside == 1 else self._bar_upper.get(width, height, self._axes_color)

    def _get_set_grid(self, axis):
        return self._grid[axis - 1]

    def _get_set_lim(self, axis, side):
        return self._get_set_xlim(side) if axis == 1 else self._get_set_ylim(side)

    def _get_set_frequency(self, axis, side):
        return self._get_xfrequency(side) if axis == 1 else self._get_yfrequency(side)

    def _get_set_ticks(self, axis, side):
        return self._get_xticks(side) if axis == 1 else self._get_yticks(side)

    def _get_set_labels(self, axis, side):
        return self._get_xlabels(side) if axis == 1 else self._get_ylabels(side)

    def _get_set_direction(self, axis, side):
        return self._get_xdirection(side) if axis == 1 else self._get_ydirection(side)
    
    def _get_set_scale(self, axis, side):
        return self._get_xscale(side) if axis == 1 else self._get_yscale(side)
  
    def _get_set_lines(self, axis, side):
        return self._get_hlines(side) if axis == 1 else self._get_vlines(side)
    
    def _get_set_lines_colors(self, axis, side):
        return self._get_hcolors(side) if axis == 1 else self._get_vcolors(side)
        
    
    def _get_set_xlim(self, xside):
        index = placement.xside_to_index(xside)
        return self._xlim[index]

    def _get_set_ylim(self, yside):
        index = placement.yside_to_index(yside)
        return self._ylim[index]

    def _get_xfrequency(self, xside):
        index = placement.xside_to_index(xside)
        return self._xfrequency[index]
    
    def _get_yfrequency(self, yside):
        index = placement.yside_to_index(yside)
        return self._yfrequency[index]

    def _get_xticks(self, xside):
        index = placement.xside_to_index(xside)
        return self._xticks[index]
    
    def _get_yticks(self, yside):
        index = placement.yside_to_index(yside)
        return self._yticks[index]

    def _get_xlabels(self, xside):
        index = placement.xside_to_index(xside)
        return self._xlabels[index]
    
    def _get_ylabels(self, yside):
        index = placement.yside_to_index(yside)
        return self._ylabels[index]

    def _get_xdirection(self, xside):
        index = placement.xside_to_index(xside)
        return self._xdirection[index]
    
    def _get_ydirection(self, yside):
        index = placement.yside_to_index(yside)
        return self._ydirection[index]

    def _get_xscale(self, xside):
        index = placement.xside_to_index(xside)
        return self._xscale[index]

    def _get_yscale(self, yside):
        index = placement.yside_to_index(yside)
        return self._yscale[index]

    def _get_bar_status(self, xside):
        return self._bar_lower.status() if xside == 1 else self._bar_upper.status() 

    def _get_hlines(self, yside):
        index = placement.yside_to_index(yside)
        return self._hlines[index]#, self._hcolors[index]

    def _get_vlines(self, xside):
        index = placement.xside_to_index(xside)
        return self._vlines[index]#, self._hcolors[index]
    
    def _get_hcolors(self, yside):
        index = placement.yside_to_index(yside)
        return self._hcolors[index]#, self._hcolors[index]

    def _get_vcolors(self, xside):
        index = placement.xside_to_index(xside)
        return self._vcolors[index]#, self._hcolors[index]

# Utility Functions

    def _correct_label(self, label):
        return None if label is None else colorize(label, self._ticks_color, self._axes_color)._part(0, 1) if isinstance(label, str) else label._part(0, 1)
    
    def _copy_settings_from(self, subplot):
        self.ticks_color(subplot._ticks_color)
        self.axes_color(subplot._axes_color)
        self.canvas_color(subplot._canvas_color)
        self.title(subplot._bar_upper.title)
        self.ylabel(subplot._bar_lower.left, 'left')
        self.ylabel(subplot._bar_lower.right, 'right')
        self.xlabel(subplot._bar_lower.center, 'lower')
        self.xlabel(subplot._bar_upper.label, 'upper')
        self.xaxes(*subplot._xaxes)
        self.yaxes(*subplot._yaxes)
        r2 = [1, 2]
        [self.xlim(*subplot._xlim[xside - 1], xside) for xside in r2]
        [self.ylim(*subplot._ylim[yside - 1], yside) for yside in r2]
        [self.xfrequency(subplot._xfrequency[xside - 1], xside) for xside in r2]
        [self.yfrequency(subplot._yfrequency[yside - 1], yside) for yside in r2]
        [self.xticks(subplot._xticks[xside - 1], subplot._xlabels[xside - 1], xside) for xside in r2]
        [self.yticks(subplot._yticks[yside - 1], subplot._ylabels[yside - 1], yside) for yside in r2]
        [self.xdirection(not(1 + subplot._xdirection[xside - 1]), xside) for xside in r2]
        [self.ydirection(not(1 + subplot._ydirection[yside - 1]), yside) for yside in r2]
        [self.xscale(subplot._xscale[xside - 1], xside) for xside in r2]
        [self.yscale(subplot._yscale[yside - 1], yside) for yside in r2]

        
class bar_lower_class():
    def __init__(self):
        self.set_left()
        self.set_center()
        self.set_right()

    def clear(self):
        self.__init__()
        
    def set_left(self, label = None):
        self.left = label

    def set_center(self, label = None):
        self.center = label

    def set_right(self, label = None):
        self.right = label

    def no_bar(self):
        return self.left is None and self.center is None and self.right is None

    def copy(self):
        new = self.__class__()
        new.set_left(self.left)
        new.set_center(self.center)
        new.set_right(self.right)
        return new

    def status(self):
        return self.left is not None or self.center is not None or self.right is not None


    def get(self, width, height, axes_color):
        left_test = self.left is not None
        center_test = self.center is not None
        right_test = self.right is not None

        bar = matrix_class(width, height, background = axes_color)

        if height > 0 and width > 0:
            bar._insert_aligned(0, 0, self.left, check_spaces = True) if left_test  else None
            bar._insert_aligned(width // 2, 0, self.center, 'center', check_spaces = True) if center_test else None
            bar._insert_aligned(width - 1, 0, self.right, 'right', check_spaces = True) if right_test else None
        return bar

    
class bar_upper_class(bar_lower_class):
    def __init__(self):
        super().__init__()
        self.set_label()
        self.set_title()

    def set_title(self, label = None):
        self.title = label

    def set_label(self, label = None):
        self.label = label

    def update(self):
        label_on = self.label is not None
        self.set_center(self.label)
        self.set_left(self.title) if label_on else self.set_center(self.title)

    def clear(self):
        self.set_title()
        self.set_label()
        self.update()

    def get(self, width, height, axes_color):
        #self.update()
        return bar_lower_class.get(self, width, height, axes_color)

    def status(self):
        self.update()
        return bar_lower_class.status(self)
