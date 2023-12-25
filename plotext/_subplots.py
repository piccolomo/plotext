from plotext._default import default_subplot
from plotext._log import log


class subplots_class():
    def __init__(self):
        self.take_maximum_size()
        self.size_direction()
        self.subplots()

    def subplots(self, rows = None, cols = None):
        self._set_subplots(rows, cols)
        self._create_subplots()
        self.clear_sizes()
        return self

    def take_minimum_size(self):
        self._max_or_min = lambda data: min(remove_none(data), default = None)
        return self

    def take_maximum_size(self):
        self._max_or_min = lambda data: max(remove_none(data), default = None)
        return self

    def size_direction(self, direction = None):
        self._size_direction = default_subplot.size_direction if direction is None else 1 if int(direction) > 0 else -1
        return self

    def subplot(self, row = None, col = None):
        row = 1 if row is None else row
        col = 1 if col is None else col
        valid = self._has_subplots and row in self._Rows and col in self._Cols
        plot = self._get_subplot(row, col) if valid else self._get_master()
        log.warning('Subplot not present, main figure returned') if not valid else None
        self._set_active(plot)
        return plot
    
    def extend(self, function, *args, **kwargs):
        [getattr(self._get_subplot(*pos), function)(*args, **kwargs) for pos in self._Slots] if self._has_subplots else None
        
    def _set_subplots(self, rows = None, cols = None):
        rows = 1 if rows is None else min(rows, self._height // 3)
        cols = 1 if cols is None else min(cols, self._width // 3)
        (rows, cols) = (0, 0) if rows * cols == 1 else (rows, cols)
        self._rows = rows;  self._cols = cols
        self._slots = [self._cols, self._rows]
        self._Rows = list(range(1, self._rows + 1))
        self._Cols = list(range(1, self._cols + 1))
        self._Slots = [(row, col) for row in self._Rows for col in self._Cols]
        self._has_subplots = rows * cols != 0

    def _create_subplots(self):
        self._subplots = None
        self._subplots = None if not self._has_subplots else [[self._create_subplot(row, col) for col in self._Cols] for row in self._Rows]

    def clear_sizes(self):
        self.extend('_set_size', None, None)
        self._initialize_sizes()
        self.extend('clear_sizes')

    def _initialize_sizes(self):
        widths = set_none_sizes(self._get_widths(), self._width)
        heights = set_none_sizes(self._get_heights(), self._height)
        [self._set_subplot_size(row, col, widths[col - 1], heights[row - 1]) for col in self._Cols for row in self._Rows]

    def _harmonize_sizes(self):
        widths = fit_sizes(self._get_widths(), self._width, self._size_direction)
        heights = fit_sizes(self._get_heights(), self._height, self._size_direction)
        [self._set_subplot_size(row, col, widths[col - 1], heights[row - 1]) for col in self._Cols for row in self._Rows]

    def _get_cumulative_widths(self):
        return  [0] + cumulative_sum(self._get_widths())

    def _get_widths(self):
        return [self._get_column_width(col) for col in self._Cols]

    def _get_column_width(self, col):
        return self._max_or_min([self._get_subplot(row, col)._width for row in self._Rows]) if col in self._Cols else None

    def _get_cumulative_heights(self):
        return  [0] + cumulative_sum(self._get_heights())
    
    def _get_heights(self):
        return [self._get_row_height(row) for row in self._Rows]

    def _get_row_height(self, row):
        return self._max_or_min([self._get_subplot(row, col)._height for col in self._Cols]) if row in self._Rows else None

    def _set_subplot_size(self, row, col, width = None, height = None):
        self._get_subplot(row, col)._set_size(width, height)

    def _get_subplot(self, row, col):
        return self._subplots[row - 1][col - 1]

##############################################
#########    Function Utilities    ###########
##############################################
        
def set_none_sizes(sizes, size_max): # given certain widths (or heights) - some of them are None -  it sets them so to respect max value
    bins = len(sizes)
    for s in range(bins):
        size_set = sum([el for el in sizes[0 : s] + sizes[s + 1 : ] if el is not None])
        available = max(size_max - size_set, 0)
        to_set = len([el for el in sizes[s : ] if el is None])
        sizes[s] = available // to_set if sizes[s] is None else sizes[s]
    return sizes
    
def fit_sizes(sizes, size_max, direction = 1):
    sizes = sizes[::direction]
    l = len(sizes)
    for i in range(l):
        m = size_max - sum(sizes[:i])
        sizes[i] = min(sizes[i], m) if i != l - 1 else m
    return sizes[::direction]
    
remove_none = lambda data: [el for el in data if el is not None]

def cumulative_sum(numbers):
    s = 0
    res = []
    for num in numbers:
        s += num
        res.append(s)
    return res
