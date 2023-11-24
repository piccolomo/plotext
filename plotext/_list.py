from plotext._matrix import matrix_class
from math import floor

def is_constant(data):
    return all([el == data[0] for el in data])

def cumulative_sum(numbers):
    s = 0
    res = []
    for num in numbers:
        s += num
        res.append(s)
    return res


# Matrix Utilities
matrix_size = lambda matrix: [0, 0] if len(matrix) == 0 else [len(matrix[0]), len(matrix)] # width, height

def join_matrices(matrices):
    cols, rows = matrix_size(matrices); Rows = range(rows); Cols = range(cols)
    w = [matrices[0][col].cols() for col in Cols]
    h = [matrices[row][0].rows() for row in Rows]
    cw = [0] + cumulative_sum(w)
    ch = [0] + cumulative_sum(h)
    new = matrix_class(sum(w), sum(h))
    for row in Rows:
        for col in Cols:
            new.insert_m(cw[col], ch[row], matrices[row][col])
    return new 


# Figure Utilities
def fit_sizes(sizes, size_max, direction = 1):
    sizes = sizes[::direction]
    l = len(sizes)
    for i in range(l):
        m = size_max - sum(sizes[:i])
        sizes[i] = min(sizes[i], m) if i != l - 1 else m
    return sizes[::direction]

def get_sizes(size_max, bins):
    return fit_sizes([floor(size_max / max(1, bins))] * bins, size_max, -1)


# Signal Utilities
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
