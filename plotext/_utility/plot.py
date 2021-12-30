from plotext._utility.data import linspace, repeat, pad_matrix, transpose, distinguish_list, replace, round
from plotext._utility.marker import sum_markers, refine_marker, space_marker, side_symbols
from plotext._utility.string import insert_label, only_spaces, pad_label, pad_labels
from plotext._utility.color import sum_colors, no_color_name
import shutil
import sys

def write(string): # the print function used by plotext
    sys.stdout.write(string)
        
def terminal_size(): # it returns the terminal size as [width, height]
    try:
        size = shutil.get_terminal_size()
        return list(size)
    except OSError:
        return [None, None]

##############################################
#######   Data Functions for Plot     ########
##############################################

def size_span(size, span): # it divides the plot size in the span dimension
    subsize = None if size is None else size / span
    sizes = [None] * span if size is None else [size - subsize * (span - 1)] + [subsize] * (span - 1)
    return sizes

def get_matrix_data(data, lim, bins): # it returns the actual data to be plotted in the plot canvas matrix  
    dz = (lim[1] - lim[0]) / (bins - 1) if (bins != 1) and (None not in lim) else 1
    data = [round((el - lim[0]) / dz + 0.5, 1) for el in data] if lim[0] != None else [None] * len(data)
    return data
    
def sum_elements(past, present): # sums markers or colors
    return sum_markers(past, present) if type(present) == str else sum_colors(past, present)
    
def join_matrices(matrices): # it joins a matrix of matrices in a single matrices with an empty separator
    if matrices == []:
        return matrices
    rows, cols = len(matrices), len(matrices[0])
    matrix = []
    for c in range(cols):
        matrix_c = []
        for r in range(rows):
            matrix_c = pad_matrix(matrix_c, matrices[r][c], "lower")
        matrix = pad_matrix(matrix, matrix_c, "right")
    return matrix     

def get_line(x, y): # it returns a line of points from x[0],y[0] to x[1],y[1] distanced between each other in x and y by at least 1.
    x0, x1 = x
    y0, y1 = y
    dx, dy = int(x1) - int(x0), int(y1) - int(y0)
    ax, ay = abs(dx), abs(dy)
    a = int(max(ax, ay) + 1)
    x = linspace(x0, x1, a)
    y = linspace(y0, y1, a)
    return [x, y]

def get_lines(x, y, m, c): # it returns the lines between all couples of data points like x[i], y[i] to x[i + 1], y[i + 1]; m and c are the list of markers and colors that needs to be elongated
    xl, yl, ml, cl = [], [], [], []
    for n in range(len(x) - 1):
        xn, yn = x[n : n + 2], y[n : n + 2]
        xn, yn = get_line(xn, yn)
        xl += xn[:-1]
        yl += yn[:-1]
        ml += [m[n]] * len(xn)
        cl += [c[n]] * len(xn)
    xl, yl, ml, cl = [xl + [x[-1]], yl + [y[-1]], ml + [m[-1]], cl + [c[-1]]] if x != [] else [xl, yl, ml, cl]
    return xl, yl, ml, cl   

def fill_data(x, y, y0, m, c): # it fills x, y with y data points reaching y0;  and c are the list of markers and colors that needs to be elongated
    y0 = int(y0)
    xy = []
    xf, yf, mf, cf = [], [], [], []
    for i in range(len(x)):
        xi, yi = int(x[i]), int(y[i])
        if [xi, yi] not in xy:
            xy.append([xi, yi])
            yn = list(range(min(y0, yi), max(y0, yi) + 1))
            xn = [xi] * len(yn)
            xf += xn
            yf += yn
            mf += [m[i]] * len(xn)
            cf += [c[i]] * len(xn)
    return [xf, yf, mf, cf]   
        
##############################################
#######   Plot Building Functions     ########
##############################################

def modify_widths(matrix, colspan, rowspan, maximum):# it returns the rightly formatted widths (or heights) for the subplots matrix
    if matrix == []:
        return []
    rows, cols = len(matrix), len(matrix[0])
    matrix = span_zeros(matrix, colspan, rowspan)
    effective = span_sizes(matrix, colspan, rowspan)
    
    Max = lambda data: max([el for el in data if el is not None], default = None)
    max_col = lambda col: Max([effective[row][col] for row in range(rows)])
    sizes = [max_col(col) for col in range(cols)]
    size_required = sum([el for el in sizes if el is not None])
    available = maximum - size_required
    for c in range(cols):
        notset = len([el for el in sizes if el is None])
        if sizes[c] is None:
            sizes[c] = int(available / notset)
            available -= sizes[c]
        successive = maximum - sum(sizes[:c])
        if sizes[c] > successive:
            sizes[c] = successive
    effective = [[sizes[col] for col in range(cols)] for row in range(rows)]
    sum_effective = lambda row, col: sum([effective[row][c] for c in range(col, col + colspan[row][col])])
    matrix = [[matrix[r][c] if matrix[r][c] == 0 else sum_effective(r, c) for c in range(cols)] for r in range(rows)]
    return matrix

def span_zeros(matrix, colspan, rowspan): # span plot zero dimensions to the plots which are hidden by the span parameters
    rows, cols = len(matrix), len(matrix[0])
    new = [el.copy() for el in matrix]
    for row in range(rows):
        for col in range(cols):
            for r in range(row, row + rowspan[row][col]):
                for c in range(col, col + colspan[row][col]):
                    if c != col:
                        new[r][c] = 0
    return new

def span_sizes(matrix, colspan, rowspan): # it divides the size according to the span
    rows, cols = len(matrix), len(matrix[0])
    new = [el.copy() for el in matrix]
    for row in range(rows):
        for col in range(cols):
            cspan = colspan[row][col]
            rspan = rowspan[row][col]
            m = matrix[row][col]
            size = int(m / cspan) if m is not None else None
            size = [m - size * (cspan - 1)] + [size] * (cspan - 1) if m is not None else [None] * cspan
            size = [size] * rspan
            for r in range(rspan):
                for c in range(cspan):
                    if rspan * cspan > 1:
                        new[row + r][col + c] = size[r][c]
    return new

def get_ticks(lim, frequency): # it returns the data ticks with given limits and frequency
    ticks = [] if None in lim else linspace(lim[0], lim[1], frequency)
    return ticks

def get_labels(ticks, scale): # it returns the approximated string version of the data ticks
    ticks = ticks if scale == "linear" else [10 ** el for el in ticks]
    d = distinguish_list(ticks)
    labels = [str(round(el, d + 1)) for el in ticks]
    labels = [el[: el.index('.') + d + 2] for el in labels]
    labels = [pad_label(el, d + 1) if len(labels) > 1 else el for el in labels]
    sign = any([el < 0 for el in ticks])
    #labels = ['+' + labels[i] if ticks[i] > 0 and sign else labels[i] for i in range(len(labels))]
    return labels

##############################################
#########    Ticks and Legend     ############
##############################################

def get_side_symbols(xside, yside):
    sides = transpose([xside, yside])
    sides = list(map(tuple, sides))
    symbols = []
    if len(set(sides)) > 1:
        symbols = [space_marker + side_symbols[el] + space_marker for el in sides]
    else:
        symbols = [''] * len(xside)
    return symbols

def get_legend(label, marker, color):
    signals = len(marker)
    marker = [repeat(marker[i], 3) for i in range(signals) if label[i] is not None]
    marker = [[refine_marker(m, 0, 0) for m in el] for el in marker]
    color = [repeat(color[i], 3) for i in range(signals) if label[i] is not None] 
    label = [list(label[i])  for i in range(signals) if label[i] is not None]
    l = max(map(len, label), default = 0)
    color = [[no_color_name] +  el for el in color]
    marker = [[space_marker] +  el for el in marker]
    label = [[space_marker] +  el + [space_marker] * (l - len(el) + 1) for el in label]
    return marker, color, label

def update_axis(axis, coords, tick): # adds ticks to an axis at each coordinate
    for i in range(len(coords)):
        if tick is not None:
            axis = insert_label(axis, tick, coords[i], 'left')[0]
    return axis

def get_yticks(length, labels, coords): # it returns the list of numerical y ticks only at the given coordinates
    l = 0 if labels == [] else len(labels[0])
    ticks = [[space_marker] * l] * length
    for i in range(len(coords)):
        c = coords[i]
        if 0 <= c < length:
            ticks[c] = list(labels[i])
    return ticks[::-1]
    
def get_xticks(length, labels, coords):
    ticks = space_marker * length * int(bool(len(labels)))
    ticks_coords = []
    for i in range(len(coords)):
        c = coords[i]
        ticks_temp, b, e = insert_label(ticks, labels[i], c, 'center')
        previous = ticks[max(b - 2, 0): min(e, length) ]
        if 0 <= c < length and only_spaces(previous) and b not in ticks_coords:
            ticks = ticks_temp
            ticks_coords.append(c)
    ticks = list(ticks)
    return ticks, ticks_coords

def get_plot_labels(xlabel, ylabel, title, width, width_canvas, ylabels_width):
    no_string = lambda string: '' if string is None else string
    xlabel = list(map(no_string, xlabel))
    ylabel = list(map(no_string, ylabel))
    title = no_string(title)

    xlabel[0] = '[x] ' * (xlabel[0] != '') + xlabel[0]
    xlabel[0] = xlabel[0][:width]
    xlabel1 = '[x] ' * (xlabel[1] != '') + xlabel[1] # alternative version when no title
    xlabel[1] = xlabel[1] + ' [upper x]' * (xlabel[1] != '')
    ylabel[0] = '[y] ' * (ylabel[0] != '') + ylabel[0]
    ylabel[1] = ylabel[1] + ' [y]' * (ylabel[1] != '') 

    lower = space_marker * width
    coord = ylabels_width[0] + width_canvas // 2
    lower_new, b, e = insert_label(lower, xlabel[0], coord, 'center')
    lower = lower_new if only_spaces(lower[b:e]) and len(xlabel[0]) <= width else lower
    lower_new, b, e = insert_label(lower, ylabel[0], 0, 'left')
    lower = lower_new if only_spaces(lower[b:e + 1]) and len(ylabel[0]) <= width else lower
    lower_new, b, e = insert_label(lower, ylabel[1], width, 'right')
    lower = lower_new if only_spaces(lower[b - 1:e]) and len(ylabel[1]) <= width else lower
    lower = list(lower)
    
    title = space_marker + title[:width-2] + space_marker if title != '' else title
    upper = space_marker * width
    coord = ylabels_width[0] + width_canvas // 2
    upper_new, bt, et = insert_label(upper, title, coord, 'center')
    title_true = only_spaces(upper[bt : et]) and 0 < len(title) <= width 
    upper = upper_new if title_true else upper
    coord = width if title_true  else coord
    xlabel[1] = xlabel[1] if title_true else xlabel1
    upper_new, b, e = insert_label(upper, xlabel[1], coord, 'center')
    upper = upper_new if only_spaces(upper[b - 1 : e]) and len(xlabel[1]) <= width else upper
    upper = [upper[i] if i in range(bt, et) and title_true else upper[i] for i in range(width)]
    # bold_escape = begin_escape(color_code("bold", 1))
    # end = end_escape(color_code("bold", 1))
    # if len(upper) > 0:
    #     upper[bt] = bold_escape + upper[bt]
    #     upper[et] = upper[et] + end
    return lower, upper

