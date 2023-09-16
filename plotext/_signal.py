from plotext._default import default_signal
from plotext._global import platform
from plotext._marker import check_marker
from plotext._color import check_color
from plotext._style import check_style
from math import ceil


class signal_class():
    def __init__(self):
        self.x = []
        self.y = []
        self.marker = []
        self.color = []
        self.style = []
        self.fillx = default_signal.fill
        self.filly = default_signal.fill
        self.xside = default_signal.xside 
        self.yside = default_signal.yside
        self.label = None
        self.lines = default_signal.lines

        
class signals_class():
    def __init__(self):
        self.signal = []
        self.length = 0
        self.color_sequence = default_signal.color_sequence
        self.past_colors = [] 

    def add(self, *args, marker = None, color = None, style = None, fillx = None, filly = None, xside = None, yside = None, label = None, lines = None):
        x, y = set_data(*args)
        length = len(x)
        
        signal = signal_class()
        signal.x = x
        signal.y = y
        signal.marker = self.check_marker(marker, length)
        signal.color = self.check_color(color, length)
        signal.style = self.check_style(style, length)
        signal.fillx = self.check_fill(fillx)
        signal.filly = self.check_fill(filly)
        signal.xside = self.correct_xside(xside)
        signal.yside = self.correct_yside(yside)
        signal.label = self.check_label(label)
        signal.lines = self.check_lines(lines)
        
        self.signal.append(signal)
        self.length += 1
   
    def check_marker(self, marker = None, length = None):
        marker = list(map(check_marker, marker)) if isinstance(marker, list) else check_marker(marker)
        return to_list(marker, length)

    def check_color(self, color = None, length = None):
        if isinstance(color, list):
            color = list(map(check_color, color))
        else:
            color = self.next_color() if color is None else check_color(color)
            self.past_colors.append(color) if color not in self.past_colors else None
        return to_list(color, length)
        
    def check_style(self, style = None, length = None):
        style = list(map(check_style, style)) if isinstance(style, list) else check_style(style)
        return to_list(style, length)

    def check_fill(self, fill = None):
        return default_signal.fill if fill not in default_signal.fills else fill

    def check_label(self, label = None):
        return None if label is None or only_spaces(label) else str(label).strip() # strip to remove spaces before and after
    
    def check_lines(self, lines = None):
        lines = default_monitor.lines if lines is None else bool(lines)

    def next_color(self):
        color = difference(self.color_sequence, self.past_colors)
        return color[0] if len(color) > 0 else self.color_sequence[0]

    def correct_xside(self, xside = None):
        xsides = default_signal.xsides
        return xsides[xside - 1] if isinstance(xside, int) and 1 <= xside <= 2 else xsides[0] if xside is None or xside.strip() not in xsides else xside.strip()

    def correct_yside(self, yside = None):
        ysides = default_signal.ysides
        return ysides[yside - 1] if isinstance(yside, int) and 1 <= yside <= 2 else ysides[0] if yside is None or yside.strip() not in ysides else yside.strip()
    
##############################################
#############     Utilities    ###############
##############################################       

def set_data(x = None, y = None): # it return properly formatted x and y data lists
   if x is None and y is None:
       x, y = [], []
   elif x is not None and y is None:
       y = x
       x = list(range(len(y)))
   lx, ly = len(x), len(y)
   if lx != ly:
       l = min(lx, ly)
       x = x[ : l]
       y = y[ : l]
   return [list(x), list(y)]

def to_list(data, length): # eg: to_list(1, 3) = [1, 1 ,1]; to_list([1,2,3], 6) = [1, 2, 3, 1, 2, 3]
    data = data if isinstance(data, list) else [data] * length
    data = data * ceil(length / len(data)) if len(data) > 0 else []
    return data[ : length]

def difference(data1, data2) : # elements in data1 not in date2
    return [el for el in data1 if el not in data2]

