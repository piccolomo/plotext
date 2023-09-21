class ticks_class():
    def __init__(self):
        self.set_scale()
        
        self.set_ticks()
        self.set_direction()
        
        self.set_grid()
        
        self.set_ticks_color()
        self.set_ticks_style()

# External Set Functions

    def set_lim(self, minimum = None, maximum = None):
        minimum = None if minimum is None else float(minimum)
        maximum = None if maximum is None else float(maximum)
        xlim = [minimum, maximum]
        xlim = xlim if None in xlim else [min(xlim), max(xlim)]
        self.lim = xlim

    def set_scale(self, scale = None):
        default_case = (scale is None or scale not in default_axis.scales)
        scale = default_axis.scale if default_case else scale
        self.scale = scale

    def set_ticks(self, ticks = None, labels = None):
        ticks = [] if ticks is None else list(ticks)
        labels = get_labels(ticks) if labels is None else list(map(str, labels))
        ticks, labels = brush(ticks, labels)
        self.ticks = ticks
        self.labels = labels
        self.labels_width = 0 if len(labels) == 0 else len(labels[0])
        self.set_frequency(len(ticks))

    def set_frequency(self, frequency = None):
        self.frequency = self.default_frequency if frequency is None else int(frequency)
        self.show_ticks = self.frequency != 0

    def set_direction(self, reverse = None):
        self.direction = default_axis.direction if reverse is None else 2 * int(not reverse) - 1

    def set_grid(self, grid = None):
        self.grid = default_axis.grid if grid is None else bool(horizontal)

    def set_ticks_color(self, color = None):
        color = color if is_color(color) else None
        self.ticks_color = default_axis.ticks_color if color is None else color

    def set_ticks_style(self, style = None):
        style = style if is_style(style) else None
        self.ticks_style = default_axis.ticks_style if style is None else clean_styles(style)

#class xticks_class():

from math import log10, ceil

def get_labels(ticks): # it returns the approximated string version of the data ticks
    d = get_distinguishing_digit(ticks)
    formatting_string = "{:." + str(d + 1) + "f}"
    labels = [formatting_string.format(el) for el in ticks]
    pos = [el.index('.') + d + 2 for el in labels]
    labels = [labels[i][: pos[i]] for i in range(len(labels))]
    all_integers = all(map(lambda el: el == int(el), ticks))
    labels = [str(int(el)) for el in ticks] if all_integers else labels
    add_zeros = not all_integers and len(labels) > 1
    labels = [add_extra_zeros(el, d) for el in labels] if add_zeros else labels
    return labels

def get_distinguishing_digit(data): # it return the minimum amount of decimal digits necessary to distinguish all elements of a list
    d = [_get_distinguishing_digit(data[i], data[i + 1]) for i in range(len(data) - 1)]
    return max(d, default = 1)

def _get_distinguishing_digit(a, b): # it return the minimum amount of decimal digits necessary to distinguish a from b
    d = abs(a - b)
    d = 0 if d == 0 else - log10(2 * d)
    d = 0 if d < 0 else ceil(d)
    #d = d + 1 if round(a, d) == round(b, d) else d
    return d

def add_extra_zeros(label, ndigits): # it adds 0s at the end of a label if necessary
    zeros = len(label) - 1 - label.index('.' if 'e' not in label else 'e')
    return (label + '0' * (ndigits - zeros)) if zeros < ndigits else label

def brush(*lists): # remove duplicates from lists x, y, z ...
    l = min(map(len, lists)) 
    lists = [el[:l] for el in lists] 
    z = transpose(lists, len(lists))
    z = no_duplicates(z)
    #z = sorted(z) #, key = lambda x: x[0])
    lists = transpose(z, len(lists))
    return lists

def transpose(data, length = 1): # it needs no explanation
    return list(map(list, zip(*data))) if len(data) != 0 else [[]] * length

def no_duplicates(data): # removes duplicates from a list
    new = []
    [new.append(item) for item in data if item not in new]
    return new


# def add_extra_spaces(labels, side): # it adds empty spaces before or after the labels if necessary
#     length = 0 if labels == [] else max_length(labels)
#     if side == "left":
#         labels = [space * (length - len(el)) + el for el in labels]
#     if side == "right":
#         labels = [el + space * (length - len(el)) for el in labels]
#     return labels
