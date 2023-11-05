import sys, shutil, os, re, math, inspect
from plotext._dict import *

###############################################
#########    Number Manipulation     ##########
###############################################

def round(n, d = 0): # the standard round(0.5) = 0 instead of 1; this version rounds 0.5 to 1
    n *= 10 ** d
    f = math.floor(n)
    r = f if n - f < 0.5 else math.ceil(n)
    return r * 10 ** (-d)

def mean(x, y, p = 1): # mean of x and y with optional power p; if p tends to 0 the minimum is returned; if p tends to infinity the max is returned; p = 1 is the standard mean
    return ((x ** p + y ** p) / 2) ** (1 / p)

def replace(data, data2, element = None): # replace element in data with correspondent in data2 when element is found
    res = []
    for i in range(len(data)):
        el = data[i] if data[i] != element else data2[i]
        res.append(el)
    return res

def try_float(data): # it turn a string into float if it can
    try:
        return float(data)
    except:
        return data

def quantile(data, q): # calculate the quantile of a given array
    data = sorted(data)
    index = q * (len(data) - 1)
    if index.is_integer():
        return data[int(index)]
    else:
        return (data[int(index)] + data[int(index) + 1]) / 2

###############################################
###########    List Creation     ##############
###############################################

def linspace(lower, upper, length = 10): # it returns a lists of numbers from lower to upper with given length
    slope = (upper - lower) / (length - 1) if length > 1 else 0
    return [lower + x * slope for x in range(length)]

def sin(periods = 2, length = 200, amplitude = 1, phase = 0, decay = 0): # sinusoidal data with given parameters
    f = 2 * math.pi * periods / (length - 1)
    phase =  math.pi * phase
    d = decay / length
    return [amplitude * math.sin(f * el + phase) * math.exp(- d * el) for el in range(length)]

def square(periods = 2, length = 200, amplitude = 1):
    T = length / periods
    step = lambda t: amplitude if t % T <= T / 2 else - amplitude
    return [step(i) for i in range(length)]

def to_list(data, length): # eg: to_list(1, 3) = [1, 1 ,1]; to_list([1,2,3], 6) = [1, 2, 3, 1, 2, 3]
    data = data if isinstance(data, list) else [data] * length
    data = data * math.ceil(length / len(data)) if len(data) > 0 else []
    return data[ : length]

def difference(data1, data2) : # elements in data1 not in date2
    return [el for el in data1 if el not in data2]

###############################################
#########    List Transformation     ##########
###############################################

def log(data): # it apply log function to the data
    return [math.log10(el) for el in data] if isinstance(data, list) else math.log10(data)

def power10(data): # it apply log function to the data
    return [10 ** el for el in data]

def floor(data): # it floors a list of data
    return list(map(math.floor, data))

def repeat(data, length): # repeat the same data till length is reached
    l = len(data) if type(data) == list else 1
    data = join([data] * math.ceil(length / l))
    return data[ : length]

###############################################
##########    List Manipulation     ###########
###############################################

def no_duplicates(data): # removes duplicates from a list
    return list(set(list(data)))
    #return list(dict.fromkeys(data)) # it takes double time

def join(data): # flatten lists at first level
    #return [el for row in data for el in row]
    return [el for row in data for el in (join(row) if type (row) == list else [row])]

def cumsum(data): # it returns the cumulative sums of a list; eg: cumsum([0,1,2,3,4]) = [0,1,3,6,10]
    s = [0]
    for i in range(len(data)):
        s.append(s[-1] + data[i])
    return s[1:]

###############################################
#########    Matrix Manipulation     ##########
###############################################

def matrix_size(matrix):  # cols, height
    return [len(matrix[0]), len(matrix)] if matrix != [] else [0, 0]

def transpose(data, length = 1): # it needs no explanation
    return [[]] * length if data == [] else list(map(list, zip(*data)))

def vstack(matrix, extra): # vertical stack of two matrices
    return extra + matrix # + extra

def hstack(matrix, extra): # horizontal stack of two matrices
    lm, le = len(matrix), len(extra)
    l = max(lm, le)
    return [matrix[i] + extra[i] for i in range(l)]

def turn_gray(matrix): # it takes a standard matrix and turns it into an grayscale one
    M, m = max(join(matrix), default = 0), min(join(matrix), default = 0)
    to_gray = lambda el: tuple([int(255 * (el - m) / (M - m))] * 3) if M != m else (127, 127, 127)
    return [[to_gray(el) for el in l] for l in matrix]

def brush(*lists): # remove duplicates from lists x, y, z ...
    l = min(map(len, lists))
    lists = [el[:l] for el in lists]
    z = list(zip(*lists))
    z = no_duplicates(z)
    #z = sorted(z)#, key = lambda x: x[0])
    lists = transpose(z, len(lists))
    return lists

###############################################
#########   String Manipulation     ###########
###############################################

nl = "\n"

def only_spaces(string): # it returns True if string is made of only empty spaces or is None or ''
    return (type(string) == str) and (string == len(string) * space) #and len(string) != 0

def format_time(time): # it properly formats the computational time
    t = time if time is not None else 0
    unit = 's' if t >= 1 else 'ms' if t >= 10 ** -3 else 'µs'
    p = 0 if unit == 's' else 3 if unit == 'ms' else 6
    t = round(10 ** p * t, 1)
    l = len(str(int(t)))
    t = str(t)
    #t = ' ' * (3 - l) + t
    return t[ : l + 2] + ' ' + unit

positive_color = 'green+'
negative_color = 'red'
title_color = 'cyan+'

def format_strings(string1, string2, color = positive_color): # returns string1 in bold and with color + string2 with a pre-formatted style
    return colorize(string1, color, "bold") + " " + colorize(string2, style = info_style)

def correct_coord(string, label, coord): # In the attempt to insert a label in string at given coordinate, the coordinate is adjusted so not to hit the borders of the string
    l = len(label)
    b, e = max(coord - l + 1, 0), min(coord + l, len(string) - 1)
    data = [i for i in range(b, e) if string[i] is space]
    b, e = min(data, default = coord - l + 1), max(data, default = coord + l)
    b, e = e - l + 1, b + l
    return (b + e - l) // 2

def no_char_duplicates(string, char): # it remove char duplicates from string
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string)
    return string

def read_lines(text, delimiter = None, columns = None): # from a long text to well formatted data
    delimiter = " " if delimiter is None else delimiter
    data = []
    columns = len(no_char_duplicates(text[0], delimiter).split(delimiter)) if columns is None else columns
    for i in range(len(text)):
        row = text[i]
        row = no_char_duplicates(row, delimiter)
        row = row.split(delimiter)
        row = [el.replace('\n', '') for el in row]
        cols = len(row)
        row = [row[col].replace('\n', '') if col in range(cols) else '' for col in range(columns)]
        row = [try_float(el) for el in row]
        data.append(row)
    return data

def pad_string(num, length): # pad a number with spaces before to reach length
    num = str(num)
    l = len(num)
    return num + ' ' * (length - l)

def max_length(strings):
    strings = map(str, strings)
    return max(map(len, strings), default = 0)

###############################################
##########   File Manipulation     ############
###############################################

def correct_path(path):
    folder, base = os.path.dirname(path), os.path.basename(path)
    folder = os.path.expanduser("~") if folder in ['', '~'] else folder
    path = os.path.join(folder, base)
    return path

def is_file(path, log = True): # returns True if path exists
    res = os.path.isfile(path)
    print(format_strings("not a file:", path, negative_color)) if not res and log else None
    return res

def script_folder(): # the folder of the script executed
    return parent_folder(inspect.getfile(sys._getframe(1)))

def parent_folder(path, level = 1): # it return the parent folder of the path or file given; if level is higher then 1 the process is iterated
    if level <= 0:
        return path
    elif level == 1:
        return os.path.abspath(os.path.join(path, os.pardir))
    else:
        return parent_folder(parent_folder(path, level - 1))

def join_paths(*args): # it join a list of string in a proper file path; if the first argument is ~ it is turnded into the used home folder path
    args = list(args)
    args[0] = _correct_path(args[0]) if args[0] == "~" else args[0]
    return os.path.abspath(os.path.join(*args))

def delete_file(path, log = True): # remove the file if it exists
    path = correct_path(path)
    if is_file(path):
        os.remove(path)
        print(format_strings("file removed:", path, negative_color)) if log else None

def read_data(path, delimiter = None, columns = None, first_row = None, log = True): # it turns a text file into data lists
    path = correct_path(path)
    first_row = 0 if first_row is None else int(first_row)
    file = open(path, "r")
    text = file.readlines()[first_row:]
    file.close()
    print(format_strings("data read from", path)) if log else None
    return read_lines(text, delimiter, columns)

def write_data(data, path, delimiter = None, columns = None, log = True): # it turns a matrix into a text file
    delimiter = " " if delimiter is None else delimiter
    cols = len(data[0])
    cols = range(1, cols + 1) if columns is None else columns
    text = ""
    for row in data:
        row = [row[i - 1] for i in cols]
        row = list(map(str, row))
        text += delimiter.join(row) + '\n'
    save_text(text, path, log = log)

def save_text(text, path, append = False, log = True): # it saves some text to the path selected
    path = correct_path(path)
    mode = "a" if append else "w+"
    with open(path , mode, encoding='utf-8') as file:
        file.write(text)
    print(format_strings("text saved in", path)) if log else None

def download(url, path, log = True): # it download the url (image, video, gif etc) to path
    from urllib.request import urlretrieve
    path = correct_path(path)
    urlretrieve(url, path)
    print(format_strings('url saved in', path)) if log else None

###############################################
#########    Platform Utilities    ############
###############################################

def is_ipython(): # true if running in ipython shenn
    try:
        __IPYTHON__
        return True
    except NameError:
        return False

def platform(): # the platform (unix or windows) you are using plotext in
   platform = sys.platform
   if platform in {'win32', 'cygwin'}:
       return 'windows'
   else:
       return 'unix'

platform = platform()

# to enable ascii escape color sequences
if platform == "windows":
    import subprocess
    subprocess.call('', shell = True)

def terminal_size(): # it returns the terminal size as [width, height]
    try:
        size = shutil.get_terminal_size()
        return list(size)
    except OSError:
        return [None, None]

terminal_width = lambda: terminal_size()[0]
tw = terminal_width

terminal_height = lambda: terminal_size()[1]
th = terminal_height

def clear_terminal(lines = None): # it cleat the entire terminal, or the specified number of lines
    if lines is None:
        write('\033c')
    else:
        for r in range(lines):
            write("\033[A") # moves the curson up
            write("\033[2K") # clear the entire line

def write(string): # the print function used by plotext
    sys.stdout.write(string)

class memorize: # it memorise the arguments of a function, when used as its decorator, to reduce computational time
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

##############################################
#########    Marker Utilities      ###########
##############################################

space = ' ' # the default null character that appears as background to all plots
plot_marker = "hd" if platform == 'unix' else 'dot'

hd_markers = {hd_codes[el] : el for el in hd_codes}
fhd_markers = {fhd_codes[el] : el for el in fhd_codes}
braille_markers = {braille_codes[el] : el for el in braille_codes}
simple_bar_marker = '▇'

@memorize
def get_hd_marker(code):
   return hd_codes[code] if len(code) == 4 else fhd_codes[code] if len(code) == 6 else braille_codes[code]

def marker_factor(marker, hd, fhd, braille): # useful to improve the resolution of the canvas for higher resolution markers
   return hd if marker == 'hd' else fhd if marker == 'fhd' else braille if marker == 'braille' else 1

##############################################
###########    Color Utilities    ############
##############################################

# A user could specify three types of colors
  # an integer for 256 color codes
  # a tuple    for RGB color codes
  # a string   for 16 color codes or styles

# Along side the user needs to specify whatever it is for background / fullground / style
# which plotext calls 'character' = 0 / 1 / 2


#colors_no_plus = [el for el in colors if '+' not in el and el + '+' not in colors and el is not no_color] # basically just [black, white]

def get_color_code(color): # the color number code from color string
    color = color.strip()
    return color_codes[color]

def get_color_name(code): # the color string from color number code
    codes = list(color_codes.values())
    return colors[codes.index(code)] if code in codes else no_color

def is_string_color(color):
    return isinstance(color, str) and color.strip() in colors

def is_integer_color(color):
    return isinstance(color, int) and 0 <= color <= 255

def is_rgb_color(color):
    is_rgb = isinstance(color, list) or isinstance(color, tuple)
    is_rgb = is_rgb and len(color) == 3
    is_rgb = is_rgb and all([is_integer_color(el) for el in color])
    return is_rgb

def is_color(color):
    return is_string_color(color) or is_integer_color(color) or is_rgb_color(color)

def colorize(string, color = None, style = None, background = None, show = False): # it paints a text with given fullground and background color
    string = apply_ansi(string, background, 0)
    string = apply_ansi(string, color, 1)
    string = apply_ansi(string, style, 2)
    if show:
        print(string)
    return string

def uncolorize(string): # remove color codes from colored string
    colored = lambda: ansi_begin in string
    while colored():
        b = string.index(ansi_begin)
        e = string[b : ].index('m') + b + 1
        string = string.replace(string[b : e], '')
    return string

def apply_ansi(string, color, character):
    begin, end = ansi(color, character)
    return begin + string + end

#ansi_begin = '\033['
ansi_begin = '\x1b['
ansi_end = ansi_begin + '0m'

@memorize
def colors_to_ansi(fullground, style, background):
    color = [background, fullground, style]
    return ''.join([ansi(color[i], i)[0] for i in range(3)])

@memorize
def ansi(color, character):
    if color == no_color:
        return ['', '']
    col, fg, tp = '', '', ''
    if character == 2 and is_style(color):
        col = get_style_codes(color)
        col = ';'.join([str(el) for el in col])
    elif character != 2:
        fg = '38;' if character == 1 else '48;'
        tp = '5;'
        if is_string_color(color):
            col = str(get_color_code(color))
        elif is_integer_color(color):
            col = str(color)
        elif is_rgb_color(color):
            col = ';'.join([str(el) for el in color])
            tp = '2;'
    is_color = col != ''
    begin = ansi_begin + fg + tp + col + 'm' if is_color else ''
    end = ansi_end if is_color else ''
    return [begin, end]

## This section is useful to produce html colored version of the plot and to translate all color types (types 0 and 1) in rgb (type 2 in plotext) and avoid confusion. the match is almost exact and it depends on the terminal i suppose

def to_rgb(color):
    if is_string_color(color): # from 0 to 1
        color = get_color_code(color)
        #color = type0_to_type1_codes[code]
    if is_integer_color(color): # from 0 or 1 to 2
        return type1_to_type2_codes[color]
    return color

##############################################
############     Style Codes    ##############
##############################################

no_style = 'default'

styles = list(style_codes.keys()) + [no_style]

info_style = 'dim'

def get_style_code(style): # from single style to style number code
    style = style.strip()
    return style_codes[style]

def get_style_codes(style): # from many styles (separated by space) to as many number codes
    style = style.strip().split()
    codes = [get_style_code(el) for el in style if el in styles]
    codes = no_duplicates(codes)
    return codes

def get_style_name(code): # from style number code to style name
    codes = list(style_codes.values())
    return styles[codes.index(code)] if code in codes else no_style

def clean_styles(style): # it returns a well written sequence of styles (separated by spaces) from a possible confused one
    codes = get_style_codes(style)
    return ' '.join([get_style_name(el) for el in codes])

def is_style(style):
    style = style.strip().split() if isinstance(style, str) else ['']
    return any([el in styles for el in style])

##############################################
###########     Plot Utilities    ############
##############################################

def set_data(x = None, y = None): # it return properly formatted x and y data lists
   if x is None and y is None :
       x, y = [], []
   elif x is not None and y is None:
       y = x
       x = list(range(1, len(y) + 1))
   lx, ly = len(x), len(y)
   if lx != ly:
       l = min(lx, ly)
       x = x[ : l]
       y = y[ : l]
   return [list(x), list(y)]

##############################################
#######     Figure Class Utilities    ########
##############################################

def set_sizes(sizes, size_max): # given certain widths (or heights) - some of them are None -  it sets them so to respect max value
    bins = len(sizes)
    for s in range(bins):
        size_set = sum([el for el in sizes[0 : s] + sizes[s + 1 : ] if el is not None])
        available = max(size_max - size_set, 0)
        to_set = len([el for el in sizes[s : ] if el is None])
        sizes[s] = available // to_set if sizes[s] is None else sizes[s]
    return sizes

def fit_sizes(sizes, size_max): # honestly forgot the point of this function: yeeeeei :-) but it is useful - probably assumes all sizes not None (due to set_sizes) and reduces those that exceed size_max from last one to first
    bins = len(sizes)
    s = bins - 1
    #while (sum(sizes) != size_max if not_less else sum(sizes) > size_max) and s >= 0:
    while sum(sizes) > size_max and s >= 0:
        other_sizes = sum([sizes[i] for i in range(bins) if i != s])
        sizes[s] = max(size_max - other_sizes, 0)
        s -= 1
    return sizes

##############################################
#######     Build Class Utilities    #########
##############################################

def get_first(data, test = True): # if test take the first element, otherwise the second
    return data[0] if test else data[1]

def apply_scale(data, test = False): # apply log scale if test
    return log(data) if test else data

def reverse_scale(data, test = False): # apply log scale if test
    return power10(data) if test else data

def replace_none(data, num_data): # replace None elements in data with correspondent in num_data
    return [data[i] if data[i] is not None else num_data[i] for i in range(len(data))]

numerical = lambda el:  not (el is None or math.isnan(el)) or isinstance(el, str) # in the case of string datetimes
all_numerical = lambda data: all([numerical(el) for el in data])

def get_lim(data): # it returns the data minimum and maximum limits
    data = [el for el in data if numerical(el)]
    m = min(data, default = 0)
    M = max(data, default = 0)
    m, M = (m, M) if m != M else (0.5 * m, 1.5 * m) if m == M != 0 else (-1, 1)
    return [m, M]

def get_matrix_data(data, lim, bins): # from data to relative canvas coordinates
    change = lambda el: 0.5 + (bins - 1) * (el - lim[0]) / (lim[1] - lim[0])
    # round is so that for example 9.9999 = 10, otherwise the floor function will give different results
    return [math.floor(round(change(el), 8)) if numerical(el) else el for el in data]

def get_lines(x, y, *other): # it returns the lines between all couples of data points like x[i], y[i] to x[i + 1], y[i + 1]; other are the lisXt of markers and colors that needs to be elongated
    # if len(x) * len(y) == 0:
    #     return [], [], *[[]] * len(other)
    o = transpose(other, len(other))
    xl, yl, ol = [[] for i in range(3)]
    for n in range(len(x) - 1):
        xn, yn = x[n : n + 2], y[n : n + 2]
        xn, yn = get_line(xn, yn)
        xl += xn[:-1]
        yl += yn[:-1]
        ol += [o[n]] * len(xn[:-1])
    xl = xl + [x[-1]] if x != [] else xl
    yl = yl + [y[-1]] if x != [] else yl
    ol = ol + [o[-1]] if x != [] else ol
    return [xl, yl] + transpose(ol, len(other))

def get_line(x, y): # it returns a line of points from x[0],y[0] to x[1],y[1] distanced between each other in x and y by at least 1.
    if not all_numerical(join([x, y])):
        return x, y
    x0, x1 = x
    y0, y1 = y
    dx, dy = int(x1) - int(x0), int(y1) - int(y0)
    ax, ay = abs(dx), abs(dy)
    a = int(max(ax, ay) + 1)
    x = [int(el) for el in linspace(x0, x1, a)]
    y = [int(el) for el in linspace(y0, y1, a)]
    return [x, y]

def get_fill_level(fill, lim, bins):
    if fill is False:
        return False
    elif isinstance(fill, str):
        return fill
    else:
        fill = min(max(fill, lim[0]), lim[1])
        fill = get_matrix_data([fill], lim, bins)[0]
        return fill

def find_filling_values(x, y, y0):
    xn, yn, yf = [[]] * 3
    l = len(x);
    while len(x) > 0:
        i = len(xn)
        xn.append(x[i])
        yn.append(y[i])
        J = [j for j in range(l) if x[j] == x[i]]
        if J != []:
            Y = [y[j] for j in J]
            j = Y.index(min(Y))
            J.pop(j)
            [x.pop(j) for j in J]
            [y.pop(j) for j in J]
            yf.append(y[j])
    return xn, yn, yf

def get_fill_boundaries(x, y):
    xm = []
    l = len(x)
    for i in range(l):
        xi, yi = x[i], y[i]
        I = [j for j in range(l) if x[j] == xi and y[j] < yi]
        Y = [y[j] for j in I]
        m = min(Y, default = yi)
        xm.append([x[i], m])
    x, m = transpose(xm)
    return m

def fill_data(x, y, y0, *other): # it fills x, y with y data points reaching y0; and c are the list of markers and colors that needs to be elongated
    #y0 = get_fill_boundaries(x, y)
    y0 = get_fill_boundaries(x, y) if isinstance(y0, str) else [y0] * len(x)
    o = transpose(other, len(other))
    xf, yf, of = [[] for i in range(3)]
    xy = []
    for i in range(len(x)):
        xi, yi, y0i = x[i], y[i], y0[i]
        if [xi, yi] not in xy:
            xy.append([xi, yi])
            yn = range(y0i, yi + 1) if y0i < yi else range(yi, y0i) if y0i > yi else [y0i]
            yn = list(yn)
            xn = [xi] * len(yn)
            xf += xn
            yf += yn
            of += [o[i]] * len(xn)
    return [xf, yf] + transpose(of, len(other))

def remove_outsiders(x, y, width, height, *other):
    I = [i for i in range(len(x)) if x[i] in range(width) and y[i] in range(height)]
    o = transpose(other, len(other))
    return transpose([(x[i], y[i], *o[i]) for i in I], 2 + len(other))

def get_labels(ticks): # it returns the approximated string version of the data ticks
    d = distinguishing_digit(ticks)
    formatting_string = "{:." + str(d + 1) + "f}"
    labels = [formatting_string.format(el) for el in ticks]
    pos = [el.index('.') + d + 2 for el in labels]
    labels = [labels[i][: pos[i]] for i in range(len(labels))]
    all_integers = all(map(lambda el: el == int(el), ticks))
    labels = [add_extra_zeros(el, d) if len(labels) > 1 else el for el in labels] if not all_integers else [str(int(el)) for el in ticks]
    #sign = any([el < 0 for el in ticks])
    #labels = ['+' + labels[i] if ticks[i] > 0 and sign else labels[i] for i in range(len(labels))]
    return labels

def distinguishing_digit(data): # it return the minimum amount of decimal digits necessary to distinguish all elements of a list
    #data = [el for el in data if 'e' not in str(el)]
    d = [_distinguishing_digit(data[i], data[i + 1]) for i in range(len(data) - 1)]
    return max(d, default = 1)

def _distinguishing_digit(a, b): # it return the minimum amount of decimal digits necessary to distinguish a from b (when both are rounded to those digits).
    d = abs(a - b)
    d = 0 if d == 0 else - math.log10(2 * d)
    #d = round(d, 10)
    d = 0 if d < 0 else math.ceil(d)
    d = d + 1 if round(a, d) == round(b, d) else d
    return d

def add_extra_zeros(label, d): # it adds 0s at the end of a label if necessary
    zeros = len(label) - 1 - label.index('.' if 'e' not in label else 'e')
    if zeros < d:
        label += '0' * (d - zeros)
    return label

def add_extra_spaces(labels, side): # it adds empty spaces before or after the labels if necessary
    length = 0 if labels == [] else max_length(labels)
    if side == "left":
        labels = [space * (length - len(el)) + el for el in labels]
    if side == "right":
        labels = [el + space * (length - len(el)) for el in labels]
    return labels

def hd_group(x, y, xf, yf): # it returns the real coordinates of the HD markers and the matrix that defines the marker
    l, xfm, yfm = len(x), max(xf), max(yf)
    xm = [el // xfm if numerical(el) else el for el in x]
    ym = [el // yfm if numerical(el) else el for el in y]
    m = {}
    for i in range(l):
        xyi = xm[i], ym[i]
        xfi, yfi = xf[i], yf[i]
        mi = [[0 for x in range(xfi)] for y in range(yfi)]
        m[xyi] = mi
    for i in range(l):
        xyi = xm[i], ym[i]
        if all_numerical(xyi):
            xk, yk = x[i] % xfi, y[i] % yfi
            xk, yk = math.floor(xk), math.floor(yk)
            m[xyi][yk][xk] = 1
    x, y = transpose(m.keys(), 2)
    m = [tuple(join(el[::-1])) for el in m.values()]
    return x, y, m

###############################################
#############   Bar Functions    ##############
###############################################

def bars(x, y, width, minimum): # given the bars center coordinates and height, it returns the full bar coordinates
   # if x == []:
   #     return [], []
   bins = len(x)
   #bin_size_half = (max(x) - min(x)) / (bins - 1) * width / 2
   bin_size_half = width / 2
   # adjust the bar width according to the number of bins
   if bins > 1:
       bin_size_half *= (max(x) - min(x)) / (bins - 1)
   xbar, ybar = [], []
   for i in range(bins):
       xbar.append([x[i] - bin_size_half, x[i] + bin_size_half])
       ybar.append([minimum, y[i]])
   return xbar, ybar

def set_multiple_bar_data(*args):
    l = len(args)
    Y = [] if l == 0 else args[0] if l == 1 else args[1]
    Y = [Y] if not isinstance(Y, list) or len(Y) == 0 else Y
    m = len(Y[0])
    x = [] if l == 0 else list(range(1, m + 1)) if l == 1 else args[0]
    return x, Y

def hist_data(data, bins = 10, norm = False): # it returns data in histogram form if norm is False. Otherwise, it returns data in density form where all bins sum to 1.
    #data = [round(el, 15) for el in data]
    # if data == []:
    #     return [], []
    bins = 0 if len(data) == 0 else bins
    m, M = min(data, default = 0), max(data, default = 0)
    data = [(el - m) / (M - m) * bins if el != M else bins - 1 for el in data]
    data = [int(el) for el in data]
    histx = linspace(m, M, bins)
    histy = [0] * bins
    for el in data:
        histy[el] += 1
    if norm:
        histy = [el / len(data) for el in histy]
    return histx, histy

def single_bar(x, y, ylabel, marker, colors):
    l = len(y)
    lc = len(colors)
    xs = colorize(str(x), 'gray+', 'bold')
    bar = [marker * el for el in y]
    bar = [apply_ansi(bar[i], colors[i % lc], 1) for i in range(l)]
    ylabel = colorize(f'{ylabel:.2f}', 'gray+', 'bold')
    bar = xs + space + ''.join(bar) + space + ylabel
    return bar

def bar_data(*args, width = None, mode = 'stacked'):
    x, Y = set_multiple_bar_data(*args)
    x = list(map(str, x))
    x = add_extra_spaces(x, 'right')
    lx = len(x[0])
    y = [sum(el) for el in transpose(Y)] if mode == 'stacked' else Y
    ly = max_length([round(el, 2) for el in join(y)])

    width_term = terminal_width()
    width = width_term if width is None else min(width, width_term)
    width = max(width, lx + ly + 2 + 1)

    my = max(join(y))
    my = 1 if my == 0 else my
    dx = my / (width - lx - ly - 2)
    Yi = [[round(el / dx, 0) for el in y] for y in Y]
    Yi = transpose(Yi)

    return x, y, Yi, width

def correct_marker(marker = None):
    return simple_bar_marker if marker is None else marker[0]

def get_title(title, width):
    out = ''
    if title is not None:
        l = len(uncolorize(title))
        w1 = (width - 2 - l) // 2; w2 = width - l - 2 - w1
        l1 = '─' * w1 + space
        l2 = space + '─' * w2
        out = colorize(l1 + title + l2, 'gray+', 'bold') + '\n'
    return out

def get_simple_labels(marker, labels, colors, width):
    out = '\n'
    if labels != None:
        l = len(labels)
        lc = len(colors)
        out =  space.join([colorize(marker * 3, colors[i % lc]) + space + colorize(labels[i], 'gray+', 'bold') for i in range(l)])
        out = '\n' + get_title(out, width)
    return out

###############################################
#############   Box Functions    ##############
###############################################

def box(x, y, width, minimum): # given the bars center coordinates and height, it returns the full bar coordinates
    # if x == []:
    #     return [], []
    bins = len(x)
    #bin_size_half = (max(x) - min(x)) / (bins - 1) * width / 2
    bin_size_half = width / 2
    # adjust the bar width according to the number of bins
    if bins > 1:
        bin_size_half *= (max(x) - min(x)) / (bins - 1)
    c, q1, q2, q3, h, l = [], [], [], [], [], []
    xbar, ybar, mybar = [], [], []

    for i in range(bins):
        c.append(x[i])
        xbar.append([x[i] - bin_size_half, x[i] + bin_size_half])
        q1.append(quantile(y[i], 0.25))
        q2.append(quantile(y[i], 0.50))
        q3.append(quantile(y[i], 0.75))
        h.append(max(y[i]))
        l.append(min(y[i]))

    return q1, q2, q3, h, l, c, xbar

##############################################
##########    Image Utilities    #############
##############################################

def update_size(size_old, size_new): # it resize an image to the desired size, maintaining or not its size ratio and adding or not a pixel averaging factor with resample = True
    size_old = [size_old[0], size_old[1] / 2]
    ratio_old = size_old[1] / size_old[0]
    size_new = replace(size_new, size_old)
    ratio_new = size_new[1] / size_new[0]
    #ratio_new = size_new[1] / size_new[0]
    size_new = [1 if el == 0 else el for el in size_new]
    return [int(size_new[0]), int(size_new[1])]

def image_to_matrix(image): # from image to a matrix of pixels
    pixels = list(image.getdata())
    width, height = image.size
    return [pixels[i * width:(i + 1) * width] for i in range(height)]
