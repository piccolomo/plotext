from plotext._default import default_xaxis, default_yaxis
import plotext._utility as ut

class axis_class():
    def __init__(self, date):
        self.default = default_xaxis
        self.date = date.copy()
        
        self.set_title()
        self.set_label()
        self.set_lim()
        self.set_scale()
        
        self.set_ticks()
        self.set_frequency()
        self.set_direction()
        
        self.set_grid()
        
        self.set_axis_color()
        self.set_ticks_color()
        self.set_ticks_style()
        self.set_show()

        self.data = []
        self.data_type = None
        self.lines = []

##############################################
#######    External Set Functions    #########
##############################################

def set_title(self, title = None):
        self.title = self.set_label(title)

    def set_label(self, label = None):
        self.label = self.set_label(label)

    def set_lim(self, left = None, right = None):
        left = None if left is None else float(left)
        right = None if right is None else float(right)
        xlim = [left, right]
        xlim = xlim if None in xlim else [min(xlim), max(xlim)]
        self.lim = xlim

    def set_scale(self, scale = None, xside = None):
        default_case = (scale is None or scale not in default_xaxis.scales)
        scale = self.default.scale if default_case else scale
        self.scale = scale

    def set_ticks(self, ticks = None, labels = None):
        ticks = [] if ticks is None else list(ticks)
        labels = ut.get_labels(ticks) if labels is None else list(map(str, labels))
        ticks, labels = ut.brush(ticks, labels)
        self.xticks = ticks
        self.xlabels = labels
        self.frequency = self.xfrequency if ticks is None else len(ticks)

    def set_frequency(self, frequency = None):
        self.frequency = self.default.frequency if frequency is None else int(frequency)

    def set_direction(self, reverse = None):
        self.direction = self.default.direction if reverse is None else 2 * int(not reverse) - 1

    def set_grid(self, grid = None):
        self.grid = self.default.grid if grid is None else bool(horizontal)

    def set_axis_color(self, color = None):
        color = color if ut.is_color(color) else None
        self.axis_color = self.default.axis_color if color is None else color
        
    def set_ticks_color(self, color = None):
        color = color if ut.is_color(color) else None
        self.ticks_color = self.default.ticks_color if color is None else color

    def set_ticks_style(self, style = None):
        style = style if ut.is_style(style) else None
        self.ticks_style = self.default.ticks_style if style is None else ut.clean_styles(style)

    def set_show(self, show = None):
        self.show = self.default.show if show is None else bool(show)

##############################################
#######    Set Functions Utilities    ########
##############################################

    def set_label(self, label = None): 
        label = None if label is None else str(label).strip()
        spaces = ut.only_spaces(label)
        label = None if spaces else label 
        return label

    def set_color(self, color = None):
        return
    
##############################################
#######    Draw() Called Functions    ########
##############################################
        
    def add_data(self, data):
        self.data.append(data)

    def add_lines(self, lines):
        lines = self.default.lines if lines is None else bool(lines)
        self.lines.append(lines)


        


class xaxis_class(axis_class):
    frequency = default_xaxis.frequency
    
class yaxis_class(axis_class):
    frequency = default_xaxis.frequency



    
        
    
