from plotext._default import dp, correct_horizontal_alignment
from plotext._default import default_xfrequency, default_yfrequency


def linspace(lower, upper, length = 10): # it returns a lists of numbers from lower to upper with given length
    slope = (upper - lower) / (length - 1) if length > 1 else 0
    return [lower + x * slope for x in range(length)]

from math import log10, ceil, floor

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

space = ' '

# def correct_position(string, label, position): # In the attempt to insert a label in string at given coordinate, the coordinate is adjusted so not to hit the borders of the string
#     l = len(label)
#     b, e = max(position - l + 1, 0), min(position + l, len(string) - 1)
#     data = [i for i in range(b, e) if string[i] is space]
#     b, e = min(data, default = position - l + 1), max(data, default = position + l)
#     b, e = e - l + 1, b + l
#     return (b + e - l) // 2

def insert_label(string, label = '', position = 0, alignment = None):
    l = len(label)
    displacements = [0, - l // 2 + 1, - l + 1]
    alignment = correct_horizontal_alignment(alignment)
    displacement = displacements[dp.horizontal_alignments.index(alignment)]
    position = floor(position) + displacement
    #position = correct_position(string, label, position)
    ls = len(string)
    just_do_it = position in range(ls) and position + l - 1 in range(ls)
    string = string[:position] + label + string[position + l:] if just_do_it else string
    return string

def insert_labels(string, labels, positions):
    l = len(labels); r = range(l)
    for i in r:
        string = insert_label(string, labels[i], positions[i])
    return string

from plotext._default import default_placement as dp

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


# class ticks_class():
#     def __init__(self):
#         self.set_scale()
        
#         self.set_ticks()
#         self.set_direction()
        
#         self.set_grid()
        
#         self.set_ticks_color()
#         self.set_ticks_style()

# # External Set Functions



#class xticks_class():

# class axis_class():
#     def __init__(self):
#         self.set_show_axis()
#         self.set_axis_color()
#         self.set_size()
#         self.backup()

#         self.create_lim()
#         self.create_ticks()
#         self.set_scale()
#         self.set_grid()
#         self.set_ticks_color()
#         self.set_ticks_style()

#     def set_show_axis(self, show = None):
#         self.show_axis = default_axis.show_axis if show is None else bool(show)

#     def set_axis_color(self, color = None):
#         color = color if is_color(color) else None
#         self.axis_color = default_axis.axis_color if color is None else color

#     def set_size(self, width = None, height = None):
#         self.width = width
#         self.height = height
#         self.size = [self.width, self.height]

#     def set_width(self, width = None):
#         self.set_size(width, self.height)
        
#     def set_height(self, height = None):
#         self.set_size(self.width, height)
        
#     def update_size(self):
#         self.set_size(self.width, self.height)

#     def copy(self): # to deep copy
#         return deepcopy(self)

#     def backup(self):
#         self.show_axis_backup = self.show_axis

#     def restore(self):
#         self.show_axis = self.show_axis_backup

#     # Ticks Function

#     def set_show_ticks(self, show = None):
#         self.show_ticks = default_axis.show_ticks if show is None else bool(show)

#     def update_show_ticks(self):
#         self.show_ticks = not (None in self.lim or self.frequency == 0)

#     def set_scale(self, scale = None):
#         default_case = (scale is None or scale not in default_axis.scales)
#         scale = default_axis.scale if default_case else scale
#         self.scale = scale

#     def create_lim(self):
#         self.min = None; self.max = None
#         self.update_lim()
#         self.update_show_ticks()

#     def set_lim(self, minimum = None, maximum = None):
#         self.min = self.min if self.min is not None else minimum
#         self.max = self.max if self.max is not None else maximum
#         self.update_lim()
#         self.update_show_ticks()

#     def update_lim(self):
#         self.lim = (self.min, self.max)

#     def create_ticks(self):
#         ticks = linspace(*self.lim, self.frequency) if None not in self.lim else []
#         self.set_ticks(ticks)

#     def set_ticks(self, ticks = None, labels = None):
#         ticks = [] if ticks is None else list(ticks)
#         labels = get_labels(ticks) if labels is None else list(map(str, labels))
#         ticks, labels = brush(ticks, labels)
#         self.ticks = ticks
#         self.labels = labels
#         self.labels_width = 0 if len(labels) == 0 else len(labels[0])
#         self.set_frequency(len(ticks))

#     def set_default_frequency(self, frequency = None):
#         self.default_frequency = frequency
        
#     def set_frequency(self, frequency = None):
#         self.frequency = self.default_frequency if frequency is None else int(frequency)
#         self.update_show_ticks()

#     def set_direction(self, reverse = None):
#         self.direction = default_axis.direction if reverse is None else 2 * int(not reverse) - 1

#     def set_grid(self, grid = None):
#         self.grid = default_axis.grid if grid is None else bool(horizontal)

#     def set_ticks_color(self, color = None):
#         color = color if is_color(color) else None
#         self.ticks_color = default_axis.ticks_color if color is None else color

#     def set_ticks_style(self, style = None):
#         style = style if is_style(style) else None
#         self.ticks_style = default_axis.ticks_style if style is None else clean_styles(style)

    # def update_relative_ticks(self):
    #     self.rticks = digitize(self.ticks, self.lim, self.width_canvas)

    # def get_ticks_string(self):
    #     axis = space * self.width
    #     rticks = [el + self.width_left for el in self.rticks]
    #     axis = insert_labels(axis, self.labels, rticks)
    #     return axis
    # def clear(self):
    #     self.__init__(self.side)
