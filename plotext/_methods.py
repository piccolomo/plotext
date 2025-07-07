from plotext._constants import space, new_line, empty, ansi_begin, limit_delta, limit_alignments
from plotext._clink import clink
import math, inspect, hashlib, pickle, sys
from copy import copy


class object_methods:
    # Return the SHA-256 hash of an object
    @staticmethod
    def hash(obj):
        return hashlib.sha256(pickle.dumps(obj)).hexdigest()

    # Hash list of floats after rounding to specified decimals
    @staticmethod
    def hash_floats(data, decimals = 5):
        return object_methods.hash([round(el, decimals) for el in data])

    # Check if object is numerical type
    @staticmethod
    def is_numerical(x):
        return isinstance(x, (int, float, bool))

    # Check if object is list-like
    @staticmethod
    def is_list_like(obj):
        return hasattr(obj, '__len__') and hasattr(obj, '__getitem__')

    # Set nested attribute on an object, creating intermediate attributes if missing
    @staticmethod
    def set_attribute(obj, attribute, value):
        value_copy = copy(value)
        if inspect.ismethod(value):
            def value_copy():
                getattr(value.__self__, value.__name__)()
        attributes = attribute.split('.')
        for atr in attributes[:-1]:
            if not hasattr(obj, atr):
                setattr(obj, atr, type('', (), {})())
            obj = getattr(obj, atr)
        setattr(obj, attributes[-1], value_copy)
        return obj


class string_methods:
    # Write a string to stdout and optionally flush output
    @staticmethod
    def write(string, flush = True):
        sys.stdout.write(string)
        if flush:
            sys.stdout.flush()

    # Lambda for creating multiple new lines (default 2)
    new_lines = staticmethod(lambda n = 2: new_line * n)

    # Add prefix to string if prefix and doc exist
    @staticmethod
    def add_prefix(doc, prefix):
        return None if doc is None else doc if prefix is None else prefix + doc

    # Pad string with spaces up to specified length
    @staticmethod
    def pad(string, length = None):
        string = str(string)
        l = len(string)
        length = l if length is None else int(length)
        return string + ' ' * (length - l)

    # Check if string contains only spaces
    @staticmethod
    def only_spaces(string):
        return string == len(string) * space

    # Join list of docstrings with delimiter, ignoring None
    @staticmethod
    def connect_strings(docs, delimiter = empty):
        docs = [el for el in docs if el is not None]
        return delimiter.join(docs) if docs else None

    # Remove ANSI color codes from a string or colorize object
    @staticmethod
    def uncolorize(string):
        from plotext._colorize import colorize_class
        if isinstance(string, colorize_class):
            return string.get_string(1)
        colored = lambda string: ansi_begin in string
        while colored(string):
            b = string.index(ansi_begin)
            e = string[b:].index('m') + b + 1
            string = string.replace(string[b:e], '')
        return string


class list_methods: 
    # Rescale a list within boundaries
    rescale = clink.rescale

    # Remove None values from list
    remove_none = staticmethod(lambda data: [el for el in data if el is not None])

    # Get maximum or minimum from list (ignores None)
    @staticmethod
    def get_extreme(data, maximum = True):
        method = max if maximum else min
        return method(list_methods.remove_none(data), default = None)

    # Repeat elements of a list up to given length, preserving copies
    @staticmethod
    def repeat(data, length):
        original = data.copy()
        make_copy = lambda: [copy(el) for el in original]
        l = (length + 1) // len(data)
        [data.extend(make_copy()) for _ in range(l)]
        return data[:length]

    # Transpose a 2D list (matrix)
    @staticmethod
    def transpose(data, length = 1):
        return [[]] * length if data == [] else list(map(list, zip(*data)))

    # Replace None elements in list with values from alternative list
    @staticmethod
    def replace_none(data, alternative):
        return [a if d is None and a is not None else d for (d, a) in zip(data, alternative)]

    # Compute cumulative sum of a list of numbers
    @staticmethod
    def cumulative_sum(numbers):
        s = 0
        res = []
        for num in numbers:
            s += num
            res.append(s)
        return res

    # Remove duplicates from list
    @staticmethod
    def unique(data):
        return list(set(list(data)))

    # Generate sinusoidal data with parameters
    @staticmethod
    def sin(periods = 2, length = 200, amplitude = 1, phase = 0, decay = 0):
        f = 2 * math.pi * periods / (length - 1)
        phase = math.pi * phase
        d = decay / length
        return [amplitude * math.sin(f * el + phase) * math.exp(-d * el) for el in range(length)]

    # Generate list of evenly spaced values from lower to upper
    @staticmethod
    def linspace(lower, upper, length = 10):
        slope = (upper - lower) / (length - 1) if length > 1 else 0
        return [lower + x * slope for x in range(length)]

    # Apply log base 10 to data list
    @staticmethod
    def log(data):
        return [math.log10(el) for el in data]

    # Apply inverse of log (power 10) to data list
    @staticmethod
    def power10(data):
        return [10 ** el for el in data]





class subplot_methods:
    # Set None values in sizes so total sums to size_max
    @staticmethod
    def set_none_sizes(sizes, size_max):
        bins = len(sizes)
        for s in range(bins):
            size_set = sum([el for el in sizes[0:s] + sizes[s + 1:] if el is not None])
            available = max(size_max - size_set, 0)
            to_set = len([el for el in sizes[s:] if el is None])
            sizes[s] = available // to_set if sizes[s] is None else sizes[s]
        return sizes

    # Fit sizes so they do not exceed size_max, respecting direction
    @staticmethod
    def fit_sizes(sizes, size_max, direction = 1):
        sizes = sizes[::direction]
        l = len(sizes)
        for i in range(l):
            m = size_max - sum(sizes[:i])
            sizes[i] = min(sizes[i], m) if i != l - 1 else m
        return sizes[::direction]



class ruler_methods:
    # Apply scaling to data; supports "log" scale
    @staticmethod
    def apply_scale(data, scale):
        return list_methods.log(data) if scale == "log" else data

    # Reverse scaling of data; supports "log" scale
    @staticmethod
    def reverse_scale(data, scale):
        return list_methods.power10(data) if scale == "log" else data

    # Generate string labels for ticks with appropriate decimal precision
    @staticmethod
    def get_labels(ticks):
        d = ruler_methods.distinguishing_digit(ticks)
        fmt = f"{{:.{d}f}}"
        return [fmt.format(el) for el in ticks]

    # Determine minimum decimal digits needed to distinguish all values
    @staticmethod
    def distinguishing_digit(data):
        d = [ruler_methods._distinguishing_digit(data[i], data[i + 1]) for i in range(len(data) - 1)]
        return max(d, default = 1)

    # Compute digits needed to distinguish two float values
    @staticmethod
    def _distinguishing_digit(a, b):
        d = abs(a - b)
        d = 0 if d == 0 else -math.log10(2 * d)
        d = 0 if d < 0 else math.ceil(d)
        return d + 1 if round(a, d) == round(b, d) else d

    # Get the delta adjustment for a given alignment
    def get_limit_delta(alignment):
        return limit_delta[limit_alignments.index(alignment)]



class log_methods:
    # Format limit values as string for logging
    @staticmethod
    def limits(limits):
        limits = ['None' if limit is None else str(round(limit, 2)) for limit in limits]
        return '[' + ', '.join(limits) + ']'

    # Format axis and side for logging purposes
    @staticmethod
    def axis(axis, side):
        return 'axis ' + str(axis) + ' side ' + str(side)
