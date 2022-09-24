# /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys as _sys
import os as _os
from ticks import _round_data

##############################################
######    Hidden Utility Functions     #######
##############################################
def print(string):
    _sys.stdout.write(string)

def set_vars(var, pad = None):
    if len(var) == 1:
        var = var[0]
        if type(var) != list:
            if var == None:
                var = pad
            var = [var, pad]
    elif len(var) == 2:
        var = list(var)
    return var
    
def set_lim(data_lim, plot_lim = [None, None], bins = 2):
    plot_min, plot_max = plot_lim
    data_min, data_max = data_lim

    if data_min == data_max:
        if data_min == 0:
            data_min, data_max = [-1, 1]
        else:
            data_min, data_max = [0.5 *  data_min, 1.5 *  data_max]
    if bins == 1:
        bins = 2    
    dz = (data_max - data_min) / (bins - 1)
    if plot_min == None:
        plot_min = data_min - dz / 2
    if plot_max == None:
        plot_max = data_max + dz / 2
    plot_lim = plot_min, plot_max
    return plot_lim

def get_ticks(ticks_number, ticks_length, plot_lims, dz):
    m, M = plot_lims
    m = m + dz / 2 
    M = M - dz / 2
    if ticks_number == 0 or ticks_length == 0:
        values = []
    if ticks_number == 1:
        values = [0.5 * (m + M)]
    else:
        step = (M - m) / (ticks_number - 1)
        values = arange(m, M + step, step)
    labels, ab = _round_data(values, ticks_length)
    return values, labels, ab

def arange(start, stop, step = 1):
    res = []
    i = start
    while i < stop:
        res.append(i)
        i = i+step
        #i=_round(i,14)
    return res

# it returns all the lines connecting the data points 
def get_line(x, y, dx): 
    x_line = []
    y_line = []
    for n in range(len(x) - 1):
        slope = 1. * (y[n + 1] - y[n]) / (x[n + 1] - x[n])
        dy = slope * dx
        x_line_n = arange(x[n], x[n + 1], dx)
        if dy == 0:
            y_line_n = [y[n]] * len(x_line_n)
        else:
            #y_line_n = _range(y[n], y[n + 1], dy)
            y_line_n = [(x_line_n[i] - x[n]) * slope + y[n] for i in range(len(x_line_n))]
        x_line.extend(x_line_n)
        y_line.extend(y_line_n)
    return x_line, y_line

def discretization(data, plot_lim, bins):
    dz = (plot_lim[1] - plot_lim[0]) / bins
    data = [int((el - plot_lim[0]) / dz) for el in data]
    return data

def update_grid(grid, x, y, marker):
    rows, cols = len(grid), len(grid[0])
    for i in range(len(x)):
        c, r = x[i], y[i]
        if 0 <= c < cols and 0 <= r < rows:
            grid[r][c] = marker
    return grid

fg_colors = ['norm', 'black', 'gray', 'red', 'green', 'yellow', 'orange', 'blue', 'violet', 'cyan', 'bold']
fg_color_codes = [0, 30, 2, 91, 92, 93, 33, 94, 95, 96, 1]
bg_colors = ['norm', 'black', 'gray', 'red', 'green', 'yellow', 'orange', 'blue', 'violet', 'cyan', 'white']
bg_color_codes = [28, 40, 100, 41, 42, 103, 43, 44, 45, 106, 47]
    
# it applies the proper color codes to a string
def add_color(text = "", color = "norm"):
    background = "norm"
    if type(color) == list:
        color, background = color
    if color == "norm" and background == "norm": 
        return text
    code = '\033['
    if type(color) == str:
        for c in range(len(fg_colors)):
            if color == fg_colors[c]:
                code += str(fg_color_codes[c])
    code += 'm'
    code += '\033['
    if type(background) == str:
        for c in range(len(bg_colors)):
            if background == bg_colors[c]:
                code += str(bg_color_codes[c])
    code += 'm'
    return code + text + '\033[0m'

def remove_color(string):
    for color_code in fg_color_codes + bg_color_codes:
        string = string.replace('\x1b[' + str(color_code) + 'm', '')
    return string

def sign(num,): # Similar to to str(numpy.sign)
    if num < 0:
        return "- "
    elif num >= 0:
        return "+ "

def str_num(num, d):
    i = int(num)
    f = abs(round(num - i, d))
    i, f = str(i), str(f)[2:]
    #f += "0" * (d - len(f))
    s = sign(num)
    if i=='0' and f=='0':
        num=""
    else:
        num = s+ i + "." + f
    return num

def get_equation(label = "x", a = 1, b = 0, d = 5):
    a, b = round(float(a), d), round(float(b), d)
    if [a, b] == [1, 0]:
        return ""
    a, b = str_num(a, d), str_num(b, d)
    eq = label + " = " + a + " × " + label + "_tick " + b
    return eq

def get_centered_label(label, length, color):
    label = label[:length]
    label_c = [add_color(add_color(el, color), "bold") for el in label]
    space1 = int((length - len(label)) / 2)
    space2 = length - len(label) - space1
    space = [add_color(" ", color)]
    label = space * space1 + label_c + space * space2
    return label

def get_opposite_labels(labels, length, color):
    if labels == ["", ""]:
        return ""
    labels[0] = labels[0] + "  "
    labels[1] = "  " + labels[1]
    space = length - sum(map(len, labels))
    labels = labels[0] + " " * space + labels[1] 
    labels = add_color(labels, color)
    return labels + '\n'

def check_path(path):
    basedir = _os.path.dirname(path)
    if _os.path.exists(basedir):
        return path
    else:
        print("warning: parent directory doesn't exists.")
        home = _os.path.expanduser("~") 
        path = _os.path.join(home, _os.path.basename(path))
    return path
