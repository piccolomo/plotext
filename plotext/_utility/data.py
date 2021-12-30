from math import log10, ceil, floor, pi, exp, log10
from time import sleep as sleeping
from time import time as timing
from math import sin as _sin
from math import isnan

##############################################
############    Set Functions    #############
##############################################

def set_data(x = None, y = None): # it return properly formatted x and y data lists
    if x is None and y is None :
        x, y = [], []
    elif x is not None and y is None:
        y = x
        x = range(1, len(y) + 1)
    x, y = list(x), list(y)
    lx, ly = len(x), len(y)
    if lx != ly:
        l = min(lx, ly)
        x = x[ : l]
        y = y[ : l]
    return [x, y]
    
##############################################
#########    List Manipulation     ###########
##############################################

def remove_non_numerical(x, y):
    l = len(x)
    numerical = lambda el: isinstance(el, int) or (isinstance(el, float) and el != None and not isnan(el))
    xn = [x[i] for i in range(l) if numerical(x[i]) and numerical(y[i])]
    yn = [y[i] for i in range(l) if numerical(x[i]) and numerical(y[i])]
    return xn, yn

def brush(x, y): # remove duplicates from x and y and sort both according to x only
    l = min(len(x), len(y))
    x, y = x[:l], y[:l]
    xy = [(x[i], y[i]) for i in range(l)]
    xy = no_duplicates(xy)
    #xy = sorted(xy)
    x, y = ([], []) if xy == [] else zip(*xy)
    return [x, y]

def first(data1, data2): # it finds first element of data1 which is not in data2, if data1 = data2, data1[0] is returned
    res = [el for el in data1 if el not in data2]
    res = data1 if res == [] else res
    return res[0]
   
def transpose(lists): # it needs no explanation
    #return [[lists[r][c] for r in range(len(lists))] for c in range(len(lists[0]))]
    return list(map(list, zip(*lists)))
    
def join(data): # flatten lists at all levels
    return [el for row in data for el in (join(row) if type (row) == list else [row]) ]
    #return [el for row in lists for el in row]

def repeat(data, length): # repeat the same data till length is reached
    l = len(data) if type(data) == 1 else 1
    data = join([data] * ceil(length / l))
    return data[ : length]

def no_duplicates(data): # removes duplicates from a list
    return list(dict.fromkeys(data))
    # new = []
    # for el in data:
    #     if el not in new:
    #         new.append(el)
    # return new

def replace(data, data2, element = None): # replace element in data with correspondent in data2 when element is found
    res = []
    for i in range(len(data)):
        el = data[i] if data[i] != element else data2[i]
        res.append(el)
    return res

def get_lim(data): # it returns the data minimum and maximum limits
    m = min(data, default = None)
    M = max(data, default = None)
    m, M = (m - 1, M + 1) if m == M and m is not None else (m, M)
    lim = [m, M]
    return lim

def linspace(lower, upper, length): # it returns a lists of numbers from lower to upper with given length
    length = int(length)
    return [lower] if length == 1 else [lower + x * (upper - lower) / (length - 1) for x in range(length)]

def remove_outsiders(x, y, width, height): # it removes elements from x and y that are beyond 0 and width for x and 0 and height for y
    xn, yn = [], []
    for i in range(len(x)):
        if 0 <= x[i] <= width  and 0 <= y[i] <= height:
            xn.append(x[i])
            yn.append(y[i])
    return xn, yn
    
def correct_data(data, factor): # it is useful when using higher resolution markers where factor is 2 or 3
    return [int(el) / factor for el in data]

def pad_list(data, side, element, length):
    element = [element] * int(length)
    if side == 'left':
        data = element + data
    else:
        data = data + element
    return data

def mean(x, y, p = 1): # mean of x and y with optional power p; if p tends to 0 the minumum is returned; if p tends to infinity the max is returned; p=1 is the normal mean
    return ((x ** p + y ** p) / 2) ** (1 / p)

def distinguish(a, b): # it return the minimum amount of decimal digits necessary to distinguish a from b (when both are rounded to those digits).
    d = abs(a - b)
    d = 0 if d == 0 else -log10(2 * d)
    #d = round(d, 10)
    d = 0 if d < 0 else ceil(d)
    d = d + 1 if round(a, d) == round(b, d) else d
    return d
    
def distinguish_list(data): # it return the minimum amount of decimal digits necessary to distinguish all elements of a list
    d = [distinguish(data[i], data[i + 1]) for i in range(len(data) - 1)]
    return max(d, default = 1)

def sin(amplitude = 1, periods = 2, length = 200, phase = 0, decay = 0): # sinusoidal data with given parameters
    f = 2 * pi * periods / (length - 1) 
    phase =  pi * phase
    d = decay / length
    return [amplitude * _sin(f * el + phase) * exp(- d * el) for el in range(length)]

def log(data): # it apply log function to the data
    return [log10(el) for el in data]

##############################################
##########    Matrix Functions    ############
##############################################
    
def pad_matrix(matrix, extra, side): # it adds an extra matrix to a matrix depending on  their mutual size and chosen side (lower and upper or left and right)
    rows, erows = len(matrix), len(extra)
    #erows, ecols = len(extra), len(extra[0])
    if side == "lower":# and ecols == cols:
        return matrix + extra
    elif side == "upper":# and ecols == cols:
        return extra + matrix
    elif side == "left":# and erows == rows:
        #return transpose(pad_matrix(transpose(matrix), transpose(extra), "upper"))
        return [(extra[r] if r < erows else []) + (matrix[r] if r < rows else []) for r in range(max(rows, erows))]
    elif side == 'right':# and erows == rows:
        return [(matrix[r] if r < rows else []) + (extra[r] if r < erows else []) for r in range(max(rows, erows))]
    else:
        return matrix

def insert(matrix, data, r, c): # insert a list in a matrix at given coordinates starting from upper left corner
    #rows = len(matrix)
    if matrix == []:
        return matrix
    matrix = [el.copy() for el in matrix]
    cols = len(matrix[0])
    l = min(len(data), cols - c)
    if r < len(matrix):
        matrix[r][c : c + l] = data[ : l]
    return matrix

def round(n, d = 0): # the standard round(0.5) = 0 instead of 1; this version rounds 0.5 to 1   
    n *= 10 ** d
    f = floor(n)
    r = f if n - f < 0.5 else ceil(n)
    return r * 10 ** (-d)

def cumsum(data): # it returns the cumulative sums of a list; eg: cumsum([0,1,2,3,4]) = [0,1,3,6,10]
    s = [0]
    for i in range(len(data)):
        s.append(s[-1] + data[i])
    return s[1:]

def sleep(time): #  it adds a sleeping time and returns the actual time slept in a lazy cosy way
    t = timing()
    sleeping(time)
    return timing() - t
