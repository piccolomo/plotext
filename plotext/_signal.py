from plotext._default import default_signal, default_color_sequence
from plotext._global import platform
from plotext._marker import check_marker
from plotext._color import check_color
from plotext._style import check_style
from plotext._axes import correct_xside, correct_yside
from math import ceil


class normal_signal_class():
    def __init__(self):
        self.set()

    def update_length(self):
        self.length = len(self.x)

    def set(self, *args, xside = None, yside = None, lines = None, fillx = None, filly = None, marker = None, color = None, style = None, label = None):
        self.x, self.y = set_data(*args)
        self.update_length()
        self.xside = correct_xside(xside)
        self.yside = correct_yside(yside)
        self.lines = self.check_lines(lines)
        self.fillx = self.check_fill(fillx)
        self.filly = self.check_fill(filly)
        self.marker = self.check_marker(marker)
        self.color = self.check_color(color)
        self.style = self.check_style(style)
        self.label = self.check_label(label)

    def check_lines(self, lines = None):
        lines = default_signal.lines if lines is None else bool(lines)

    def check_fill(self, fill = None):
        return default_signal.fill if fill not in default_signal.fills else fill
    
    def check_marker(self, marker = None):
        marker = list(map(check_marker, marker)) if isinstance(marker, list) else check_marker(marker)
        return to_list(marker, self.length)

    def check_color(self, color = None):
        color = list(map(check_color, color)) if isinstance(color, list) else check_color(color)
        return to_list(color, self.length)

    def check_style(self, style = None):
        style = list(map(check_style, style)) if isinstance(style, list) else check_style(style)
        return to_list(style, self.length)
    
    def check_label(self, label = None):
        return None if label is None or only_spaces(label) else str(label).strip()

    def __str__(self):
        out = 'length ' + str(self.length)
        return out

    def print(self):
        print(self)
        


class signals_class():
    def __init__(self):
        self.list = []
        self.update_length()
        self.color_sequence = default_color_sequence
        self.past_colors = []

    def update_length(self):
        self.length = len(self.list)

    def add_normal_signal(self, *args, **kwargs):
        color = kwargs.get("color")
        color = color if isinstance(color, list) else self.check_color()
        signal = normal_signal_class()
        signal.set(*args, **kwargs)
        self.list.append(signal)
        self.update_length()

    def check_color(self, color = None):
        color = self.next_color() if color is None else check_color(color)
        self.past_colors.append(color) if color not in self.past_colors else None
        return color
    
    def next_color(self):
        color = difference(self.color_sequence, self.past_colors)
        return color[0] if len(color) > 0 else self.color_sequence[0]

    def print(self):
        [print(el) for el in self.list]
    
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

def to_list(data, max_length): # eg: to_list(1, 3) = [1, 1 ,1]; to_list([1,2,3], 6) = [1, 2, 3, 1, 2, 3]
    data = data if isinstance(data, list) else [data] * max_length
    data = data * ceil(max_length / len(data)) if len(data) > 0 else []
    return data[ : max_length]

def only_spaces(string): # it returns True if string is made of only empty spaces or is None or ''
    return (type(string) == str) and (string == len(string) * space) #and len(string) != 0

def difference(data1, data2) : # elements in data1 not in date2
    return [el for el in data1 if el not in data2]

