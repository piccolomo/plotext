import os
import sys
import math
from datetime import datetime as dt
import docstrings as _docstrings
 
##############################################
############    Set Functions    #############
##############################################
def set_first_to_both(x = None, y = None):# by setting one parameter to a value, both are set
    if x != None and y == None:
        y = x
    return [x, y]

def set_list_to_both(x = None, y = None): # by setting a parameter to a list, both are set
    if type(x) == list:
        x, y = x[0], x[1]
    return [x, y]

def set_if_none(x = None, x_none = None): # set a parameter when none is provided. 
    if x == None:
        x = x_none
    return x

def set_list_if_none(data, data_none):
    for i in range(len(data)):
        data[i] = set_if_none(data[i], data_none[i])
    return data

##############################################
#########    Utility Functions    ############
##############################################
def sort_data(data1, data2): # sort data2 from data1 and remove duplicates of data1 and 2 based on data1
    res = zip(*sorted(zip(data1, data2)))
    data1, data2 = list(map(list, res))
    d1 = []; d2 = []
    for i in range(len(data1)):
        if data1[i] not in d1:
            d1.append(data1[i])
            d2.append(data2[i])
    return [d1, d2]

def get_data(*args):
    if len(args) == 0:
        x, y = [], []
    elif len(args) == 1:
        y = args[0]
        x = list(range(len(y)))
    else:
        x = args[0]
        y = args[1]
    x, y = list(x), list(y)
    length = min(len(x), len(y))
    if len(x) != len(y):
        x = x[ : length]
        y = y[ : length]
    return x, y

def transpose(lists):
    lists = list(zip(*lists))
    return list(map(list, lists))

def get_lim_data(data):
    m = min([min(el, default = 0) for el in data], default = 0)
    M = max([max(el, default = 0) for el in data], default = 0)
    if m == M:
        m = m - 1
        M = M + 1
    lim_data = [m, M]
    lim_data.sort()
    return lim_data

def linspace(lower, upper, length):
    if length == 1:
        return [0.5 * (lower + upper)]
    return [lower + x * (upper - lower) / (length - 1) for x in range(length - 1)] + [upper]

def arange(start, stop, step = 1):
    res = []
    i = start
    while i < stop:
        res.append(i)
        i = i + step
    return res

def get_ticks(lim, frequency):
    ticks = linspace(min(lim), max(lim), frequency)
    ticks = [int(el) if el == int(el) else el for el in ticks]
    return ticks

def get_log_ticks(lim, frequency):
    ticks = list(linspace(lim[0], lim[1], frequency))
    labels = [10 ** el for el in ticks]
    labels = get_labels(labels)
    return ticks, labels

def get_labels(ticks):
    l = len(ticks)
    if len(ticks) == 1:
        c = len(str(ticks[0]))
    else:
        c = max([distinguish(ticks[i], ticks[i + 1]) for i in range(l - 1)])
    ticks = [round_to_character(el, c) for el in ticks]
    #ticks = [int(el) if int(el) == el else el for el in ticks]

    #ticks_sn = [scientific_notation(*scientific_base(el)) for el in ticks]
    ticks = [str(el) for el in ticks]
    #ticks = [ticks[i] if len(ticks[i]) <= c else ticks_sn[i] for i in range(l)]
    return ticks

int_len = lambda x: len(str(int(x)))
def distinguish(a, b):
    dif = abs(a - b)
    ca, cb, cd = map(int_len, [a, b, dif])
    dec = 0 if dif == 0 or int(dif) > 0 else -math.floor(math.log10(dif)) + cd + 1
    res =  max(ca, cb, dec)
    res = res + 1 if a < 0 or b < 0 else res
    return res

def round_to_character(n, c):
    int_len = len(str(int(n)))
    d = c - int_len - 1
    if d < 0:
        d = 0
    return round(n, d)

def scientific_base(num):
    base = abs(num)
    exp = 0 if num == 0 else int(math.log10(base))
    base = num / (10 ** exp)
    base = int(base) if int(base) == base else base
    return [base, exp]

def scientific_notation(base, exp):
    return str(base) + 'E' + str(exp) 

def get_matrix_data(data, plot_lim, bins):
    bins = 1 if bins == 0 else bins
    dz = (plot_lim[1] - plot_lim[0]) / bins
    data = [int((el - plot_lim[0]) / dz) if el != plot_lim[1] else bins - 1 for el in data]
    return data

def get_matrix_data_hd(data, plot_lim, bins):
    return [el / 2 for el in get_matrix_data(data, plot_lim, 2 * bins)]

def update_matrix(matrix, x, y, marker, color):
    if matrix == []:
        return []
    if marker == "small":
        return update_matrix_small(matrix, x, y, color)
    cols, rows = len(matrix[0]), len(matrix)
    for i in range(len(x)):
        c, r = x[i], y[i]
        if 0 <= r < rows and 0 <= c < cols:
            c, r = int(c), int(r)
            matrix[rows - 1 - r][c][:2] = [marker, color]
    return matrix

def update_matrix_small(matrix, x, y, color):
    cols, rows = len(matrix[0]), len(matrix)
    for i in range(len(x)):
        c, r = x[i], y[i]
        new = small_marker(c, r)
        c, r = int(c), int(r)
        if 0 <= r < rows and 0 <= c < cols:
            old = matrix[rows - 1 - r][c][0]
            old = " " if old not in blocks.keys() else old
            old = blocks[old]
            new = sum_small(old, new)
            new = matrix_to_block(new)
            matrix[rows - 1 - r][c][:2] = [new, color]
    return matrix
            
def small_marker(c, r):
    c = (2 * c) % 2
    r = (2 * r) % 2
    c, r = int(c), int(r)
    new = [[(c == 0) * (r == 1), (c == 1) * (r == 1)]]
    new += [[(c == 0) * (r == 0), (c == 1) * (r == 0)]]
    return new

def sum_small(block1, block2):
    new = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            new[i][j] = block1[i][j] + block2[i][j]
            new[i][j] = int(bool(new[i][j]))
    return new

blocks = {" ": [[0, 0], [0, 0]],
          "▘": [[1, 0], [0, 0]],
          "▖": [[0, 0], [1, 0]],
          "▗": [[0, 0], [0, 1]],
          "▝": [[0, 1], [0, 0]],
          "▌": [[1, 0], [1, 0]],
          "▐": [[0, 1], [0, 1]],
          "▄": [[0, 0], [1, 1]],
          "▀": [[1, 1], [0, 0]],
          "▚": [[1, 0], [0, 1]],
          "▞": [[0, 1], [1, 0]],
          "▛": [[1, 1], [1, 0]],
          "▙": [[1, 0], [1, 1]],
          "▟": [[0, 1], [1, 1]],
          "▜": [[1, 1], [0, 1]],
          "█": [[1, 1], [1, 1]]}

def matrix_to_block(matrix):
    for k in blocks.keys():
        if matrix == blocks[k]:
            return k

def get_line(x, y): 
    x_line = []
    y_line = []
    for n in range(len(x) - 1):
        Dy, Dx = y[n + 1] - y[n], x[n + 1] - x[n]
        Ay, Ax = abs(Dy), abs(Dx)
        Sy, Sx = 0 if Dy == 0 else int(abs(Dy) / Dy), 0 if Dx == 0 else int(abs(Dx) / Dx)
        if Ax >= Ay and Ax != 0:
            x_line_n = [x[n] + i * Sx for i in range(Ax)]
            y_line_n = [y[n] + i * Dy / Ax for i in range(Ax)]
        elif Ay > Ax and Ay != 0:
            y_line_n = [y[n] + i *  Sy     for i in range(Ay)]
            x_line_n = [x[n] + i * Dx / Ay for i in range(Ay)]
        elif Ax == 0:
            y_line_n = arange(y[n], y[n + 1] + 1)
            x_line_n = [x[n]] * len(y_line_n)
        elif Ay == 0:
            x_line_n = arange(x[n], x[n + 1] + 1)
            y_line_n = [y[n]] * len(x_line_n)
        x_line.extend(x_line_n)
        y_line.extend(y_line_n)
    x_line += [x[-1]]
    y_line += [y[-1]]
    return x_line, y_line

def fill_data(x, y, y0):
    y_new = y
    x_new = x
    for i in range(len(y)):
        yi = int(y[i])
        y_temp = range(min(y0, yi), max(y0, yi))
        y_new += y_temp
        x_new += [x[i]] * len(y_temp)
    return [x, y]

def frame_matrix(matrix, symbol = None):
    l, w = len(matrix), len(matrix[0])
    frame = [symbol] * 6 if symbol!= None else ["┌", "─", "┐", "│", "┘", "└"] 
    side = [[frame[3]] *  l]
    matrix = transpose(side + transpose(matrix) + side)
    up = [[frame[0]] + [frame[1]] * w + [frame[2]]]
    down = [[frame[5]] + [frame[1]] * w + [frame[4]]]
    matrix = up + matrix + down
    return matrix

def insert(sub_matrix, matrix):
    if matrix == []:
        return []
    l, w = len(sub_matrix), len(sub_matrix[0])
    L, W = len(matrix), len(matrix[0])
    if L >= l and W >= w:
        for i in range(l):
            for j in range(w):
                matrix[i][j] = sub_matrix[i][j]
    return matrix

def join(matrix1, matrix2, separator = None, orientation = "vertical"):
    if orientation == "horizontal":
        matrix1 = transpose(matrix1)
        matrix2 = transpose(matrix2)
        return transpose(join(matrix1, matrix2, separator, "vertical"))
    if matrix1 == [] or matrix2 == []:
        return matrix1 + matrix2
    w = min(len(matrix1[0]), len(matrix2[0]))
    separator = [] if separator == None else [[separator] * w]
    matrix1 = [el[:w] for el in matrix1]
    matrix2 = [el[:w] for el in matrix2]
    return matrix1 + separator + matrix2

def log(data):
    return [math.log10(el) for el in data]

##############################################
#########    Bar/Hist Functions    ###########
##############################################
def bar_xdata(x):
    x_type = [type(el) == str for el in x]
    if any(x_type):
        x_labels = list(map(str, x))
        x = list(range(len(x)))
    else:
        x_labels = get_labels(x)
    return x, x_labels

def bars(x, y, width = 4 / 5):
    x, y = x[:], y[:]
    bins = len(x)
    bin_size_half = width / 2
    # adjust the bar width according to the number of bins
    if bins > 1:
        bin_size_half *= (max(x) - min(x)) / (bins - 1)
    #bin_size_half = (max(x) - min(x)) / (bins) * width / 2
    #x[0] += bin_size_half
    #x[bins - 1] -= bin_size_half
    xbar = []
    ybar = []
    for i in range(bins):
        xbar.append([x[i] - bin_size_half, x[i] - bin_size_half,
                     x[i] + bin_size_half, x[i] + bin_size_half,
                     x[i] - bin_size_half])
        ybar.append([0, y[i], y[i], 0, 0])
    return xbar, ybar

def hist_data(data, bins = 10):
    data = [round(el, 15) for el in data]
    m, M = min(data), max(data)
    data = [(el - m) / (M - m) * bins if el != M else bins - 1 for el in data]
    data = [int(el) for el in data]
    histx = linspace(m, M, bins)
    histy = [0] * bins
    for el in data:
        histy[el] += 1
    return histx, histy


##############################################
#########   Date/Time Functions    ###########
##############################################
today = dt.today()

def time(day = None, month = None, year = None, hour = 0, minute = 0, second = 0):
    year = today.year if year == None else year
    month = today.month if month == None else month
    day = today.day if day == None else day
    return dt(year = year, month = month, day = day, hour = hour, minute = minute, second = second).timestamp()

def string_to_date(string):
    string = string.split(" ")
    if len(string) == 1:
        date = string[0] if '/' in string[0] else today.strftime("%d/%m/%Y")
        time = string[0] if ':' in string[0] else '0:0:0'
        string = [date, time]
    date = string[0]
    time = string[1]
    if date.count('/') == 1:
        date += '/' + str(today.year)
    if time.count(':') == 1:
        time += ':00' 
    time = dt.strptime(date + ' ' + time, '%d/%m/%Y %H:%M:%S')
    day, month, year, hour, minute, second = time.day, time.month, time.year, time.hour, time.minute, time.second
    return [day, month, year, hour, minute, second]

def string_to_time(string):
    return time(*string_to_date(string))


##############################################
#####    Plotting Utility Functions    #######
##############################################
def get_canvas(matrix):
    canvas = ''
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            marker = matrix[r][c][0]
            fullground = matrix[r][c][1]
            background = matrix[r][c][2]
            marker = add_color(marker, fullground, background)
            canvas += marker
        canvas += '\n'
    return canvas + '\n'
  

_terminal_printed_lines_cnt = 0

def write(string):
    global _terminal_printed_lines_cnt
    sys.stdout.write(string)
    _terminal_printed_lines_cnt += string.count('\n')


##############################################
######    Platform/Shell Functions    ########
##############################################
def platform():
    if sys.platform.startswith("win"):
        return "windows"
    else:
        return "linux"

def shell():
    if 'idlelib.run' in sys.modules:
        return "idle"
    elif "spyder" in sys.modules:
        return "spyder"
    else:
        return "regular"


##############################################
###########    Other Functions    ############
##############################################
def check_path(path):
    home = os.path.expanduser("~") 
    if path == None:
        path = os.path.join(home, "plot.txt")
    basedir = os.path.dirname(path)
    if os.path.exists(basedir):
        return path
    else:
        print("warning: parent directory doesn't exists.")
        path = os.path.join(home, os.path.basename(path))
    return path
    
def terminal_size():
    return list(os.get_terminal_size())

def docstrings():
    fun = dir(_docstrings)
    name = [el for el in fun if el[0] != '_']
    fun = [getattr(_docstrings, el) for el in name]
    name = [el.replace('_doc', '') for el in name]
    name = [add_color(el, 'indigo') for el in name]
    name = [add_color(el, 'bold') for el in name]
    for i  in range(len(fun)):
        print()
        print()
        print(name[i])
        print(fun[i])

def version():
    init_path = "__init__.py"
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, init_path), 'r') as fp:
        lines = fp.read()
    for line in lines.splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            version = line.split(delim)[1]
            print("plotext version:", version)
            return version
    else:
        print("Unable to find version string.")

def sleep_1us():
    time = 1 / 10 ** 6
    [i for i in range(int(time * 2.58 * 10 ** 7))]

def sleep(time = 0.01):
    ms = int(time * 10 ** 6)
    for m in range(ms):
        sleep_1us()
    #[i for i in range(int(time * 15269989))]

def sin(length = 1000, peaks = 2, decay = 0, phase = 0):
    f = 2 * math.pi / length * peaks
    ph =  math.pi * phase
    d = 1 / length * decay
    return [math.sin(f * el + ph) * math.exp(- d * el) for el in range(length)]

##############################################
########    Color/Marker Functions    ########
##############################################
fullground_color = {'none': 0, 'black': 30, 'iron': 90, 'gray': 2, 'cloud': 37, 'white': 97, 'red': 31, 'tomato': 91, 'basil': 32, 'green': 92, 'yellow': 93, 'gold': 33, 'blue': 34, 'indigo': 94, 'teal': 36, 'artic': 96, 'lilac': 95, 'violet': 35, 'italic': 3, 'bold': 1, 'flash': 5}
background_color = {'none': 28, 'black': 40, 'iron': 100, 'cloud': 47, 'white': 107, 'red': 41, 'tomato': 101, 'basil': 42, 'green': 102, 'yellow': 103, 'gold': 43, 'blue': 44, 'indigo': 104, 'teal': 46, 'artic': 106, 'lilac': 105, 'violet': 45}
color_sequence = ["blue", "tomato", "gold", "iron", "basil", "none", "gray", "cloud", "lilac", "black", "artic", "red", "green", "yellow", "indigo", "teal", "violet", "white", "flash"]

def apply_color(text, code):
    if code == 0 or code == 28:
        return text
    return '\033[' + str(code) + 'm' + text + '\033[0m'

def add_color(text = "", color = "none", background = "none"):
    color = fullground_color[color]
    background = background_color[background]
    if color != "none":
        text = apply_color(text, color)
    if background != "none":
        text = apply_color(text, background)
    return text

def remove_color(string):
    for c in list(fullground_color.values()) + list(background_color.values()):
        string = string.replace('\x1b[' + str(c) + 'm', '')
    return string

def colors():
    key = list(fullground_color.keys())
    title = "Fullground\tBackground"
    lines = '─' * 26
    #title = _add_color(title, "none", "black")
    title = add_color(title, "bold")
    #title = _apply_color(title, 4)
    out = '\n' + title + '\n' + lines
    for i in range(len(key)):
        full_color = ""
        if key[i] in fullground_color.keys():
            back = "none" if key[i] not in ["black"] else "cloud"
            full_color = add_color(key[i]+ "\t\t" , key[i], back)
        back_color = add_color("not available", "italic")
        if key[i] in background_color.keys():
            full = "black" if key[i] not in ["none", "black", "iron"] else "white"
            back_color = add_color(key[i], full, key[i])
        out += "\n" * 1 + full_color + back_color 
    out += "\n\n" + "Fullground colors can be set to the 'color' attribute or given as input to plt.ticks_color()."
    out += "\n" + "Background colors can be given as input to plt.canvas_color() and plt.axes_color()."
    print(out)

marker = {'small':  '▘',
          'big':    '█',
          'dot':    '•',
          'heart':  '♥',
          'smile':  '☺',
          'dollar': '$',
          'euro':   '€'}
marker_sequence = ["small", "dot", "x", "o", "heart", "dollar", "smile", "euro", "big", "@", "^", "é", "a", "b", "c", "d", "e", "f"]
    
def markers(): 
    print()
    title = "Code\tMarker"
    lines = '─' * 14
    title = add_color(title, "bold")
    print(title + '\n' + lines)
    for el in marker:
        print(el + '\t' + marker[el])
    print("\nThese codes can be set to the 'marker' attribute.")
