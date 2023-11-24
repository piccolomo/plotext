from plotext._default import default_settings, correct_xside, correct_yside, xside_to_index, yside_to_index
from plotext._colorize import colorize


class settings_class():
    def __init__(self):
        self.bar_upper = bar_upper_class()
        self.bar_lower = bar_lower_class()
        self.set_ticks_color()
        self.set_axes_color()
        self.init_xaxes()
        self.init_yaxes()
        self.init_xfrequency()
        self.init_yfrequency()
        self.init_lim()
        self.init_ticks()

        
    def set_ticks_color(self, color = None):
        self.ticks_color = color if color is not None else default_settings.ticks_color
        
    def set_axes_color(self, color = None):
        self.axes_color = color if color is not None else default_settings.axes_color

        
    def set_ylabel(self, label, yside):
        label = self.correct_label(label)
        yside = correct_yside(yside)
        self.bar_lower.set_left(label) if yside == 'left' else self.bar_lower.set_right(label)

    def set_xlabel(self, label, xside):
        label = self.correct_label(label)
        xside = correct_xside(xside)
        self.bar_lower.set_center(label) if xside == 'lower' else self.bar_upper.set_label(label)

    def set_title(self, label):
        label = self.correct_label(label)
        self.bar_upper.set_title(label)
        
    def init_xaxes(self):
        self.xaxes = default_settings.xaxes

    def init_yaxes(self):
        self.yaxes = default_settings.yaxes
    
    def set_xaxes(self, lower, upper):
        self.xaxes[0] = self.xaxes[0] if lower is None else bool(lower)
        self.xaxes[1] = self.xaxes[1] if upper is None else bool(upper)
        
    def set_yaxes(self, left, rigth):
        self.yaxes[0] = self.yaxes[0] if left is None else bool(left)
        self.yaxes[1] = self.yaxes[1] if rigth is None else bool(rigth)

    def set_frame(self, frame):
        self.set_xaxes(frame, frame)
        self.set_yaxes(frame, frame)

        
    def init_xfrequency(self):
        self.xfrequency = [default_settings.xfrequency] * 2
        
    def init_yfrequency(self):
        self.yfrequency = [default_settings.yfrequency] * 2

    def set_xfrequency(self, frequency, xside):
        index = xside_to_index(xside)
        self.xfrequency[index] = self.xfrequency[index] if frequency is None else int(frequency)
        
    def set_yfrequency(self, frequency, yside):
        index = yside_to_index(yside)
        self.yfrequency[index] = self.yfrequency[index] if frequency is None else int(frequency)

    def init_lim(self):
        self.xlim = [[None, None], [None, None]]
        self.ylim = [[None, None], [None, None]]

    def set_xlim(self, left, right , xside):
        index = xside_to_index(xside)
        self.xlim[index] = [left, right]

    def set_ylim(self, lower, upper, yside):
        index = yside_to_index(yside)
        self.ylim[index] = [lower, upper]

    def init_ticks(self):
        self.xticks = [None, None]
        self.yticks = [None, None]
        self.xlabels = [None, None]
        self.ylabels = [None, None]

    def set_xticks(self, ticks, labels, xside):
        index = xside_to_index(xside)
        self.xticks[index] = ticks
        self.xlabels[index] = labels
        xfrequency = None if ticks is None else len(ticks)
        self.set_xfrequency(xfrequency, xside)

    def set_yticks(self, ticks, labels, yside):
        index = yside_to_index(yside)
        self.yticks[index] = ticks
        self.ylabels[index] = labels
        yfrequency = None if ticks is None else len(ticks)
        self.set_yfrequency(yfrequency, yside)

        
    def correct_label(self, label):
        return colorize(label, self.ticks_color, self.axes_color).part(0, 1) if isinstance(label, str) else label
    
    def update(self):
        self.bar_upper.update()

    def clear(self):
        self.__init__()
            

class bar_lower_class():
    def __init__(self):
        self.set_left()
        self.set_center()
        self.set_right()
        
    def set_left(self, label = None):
        self.left = label

    def set_center(self, label = None):
        self.center = label

    def set_right(self, label = None):
        self.right = label

        
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

