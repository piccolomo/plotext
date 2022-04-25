import math

###############################################
#########    Number Manipulation     ##########
###############################################

def round(n, d = 0): # the standard round(0.5) = 0 instead of 1; this version rounds 0.5 to 1   
    n *= 10 ** d
    f = math.floor(n)
    r = f if n - f < 0.5 else math.ceil(n)
    return r * 10 ** (-d)

def mean(x, y, p = 1): # mean of x and y with optional power p; if p tends to 0 the minumum is returned; if p tends to infinity the max is returned; p = 1 is the standard mean
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

###############################################
##########    Numbers to List     #############
###############################################

def linspace(lower, upper, length = 10): # it returns a lists of numbers from lower to upper with given length
    length = int(length)
    return [lower] if length == 1 else [lower + x * (upper - lower) / (length - 1) for x in range(length)]

###############################################
##############    List Math     ###############
###############################################
    
def log(data): # it apply log function to the data
    return [math.log10(el) for el in data] if isinstance(data, list) else math.log10(data)
 
def power10(data): # it apply log function to the data
    return [10 ** el for el in data]

def sin(periods = 2, length = 200, amplitude = 1, phase = 0, decay = 0): # sinusoidal data with given parameters
    f = 2 * math.pi * periods / (length - 1) 
    phase =  math.pi * phase
    d = decay / length
    return [amplitude * math.sin(f * el + phase) * math.exp(- d * el) for el in range(length)]

def floor(data): # it floors a list of data
    return list(map(math.floor, data))

###############################################
##########    List Manipulation     ###########
###############################################

def brush(*lists): # remove duplicates from lists x, y, z ... and sort all according to x only
    l = min(map(len, lists))
    lists = [el[:l] for el in lists]
    z = list(zip(*lists))
    z = no_duplicates(z)
    z = sorted(z, key = lambda x: x[0])
    lists = transpose(z, len(lists))
    return lists

def join(data): # flatten lists at first level
    #return [el for row in data for el in row]
    return [el for row in data for el in (join(row) if type (row) == list else [row])]
 
def no_duplicates(data): # removes duplicates from a list
    return list(set(list(data)))
    #return list(dict.fromkeys(data)) # it takes double time

def transpose(matrix, length = 1): # it needs no explanation
    return [[]] * length if matrix == [] else list(map(list, zip(*matrix)))

def repeat(data, length): # repeat the same data till length is reached
    l = len(data) if type(data) == list else 1
    data = join([data] * math.ceil(length / l))
    return data[ : length]

def to_list(data, length): # eg: to_list(1, 3) = [1, 1 ,1]; to_list([1,2,3], 6) = [1, 2, 3, 1, 2, 3]
    data = data if isinstance(data, list) else [data] * length
    data = data * math.ceil(length / len(data)) if len(data) > 0 else []
    return data[ : length]

def difference(data1, data2) : # elements in data1 not in date2 
    return [el for el in data1 if el not in data2]

def cumsum(data): # it returns the cumulative sums of a list; eg: cumsum([0,1,2,3,4]) = [0,1,3,6,10]
    s = [0]
    for i in range(len(data)):
        s.append(s[-1] + data[i])
    return s[1:]

###############################################
#########    Matrix Manipulation     ##########
###############################################

def matrix_size(matrix):
    return [len(matrix), len(matrix[0])] if matrix != [] else [0, 0]

def join_matrices(matrices): # from a matrix of matrices to a single matrix
    if matrices == []:
        return matrices
    rows, cols = len(matrices), len(matrices[0])
    matrix = []
    for r in range(rows):
        matrix_r = []
        for c in range(cols):
            matrix_r = pad(matrix_r, matrices[r][c], "right")
        matrix = pad(matrix, matrix_r, "lower")
    return matrix

def pad(matrix, extra, side): # it adds an extra matrix to matrix depending on side (left, right, upper, lower)
    if side == "lower":
        return vstack(matrix, extra)
    elif side == "upper":
        return vstack(extra, matrix)
    elif side == "right":
        return hstack(matrix, extra)
    else:
        return hstack(extra, matrix)

def vstack(matrix, extra): # vertical stack of two matrices
    if extra == [] or extra == [[]]:
        return matrix
    else:
        return matrix + extra

def hstack(matrix, extra): # horizontal stack of two matrices
    lm, le = len(matrix), len(extra)
    l = max(lm, le)
    matrix += [[]] * (l - lm)
    extra += [[]] * (l - le)
    return [matrix[i] + extra[i] for i in range(l)]
 
###############################################
########    Memorization Decorator     ########
###############################################

class memorize: # it memorise the arguments of a function, when used as its decorator, to reduce computational time
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
