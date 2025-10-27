from plotext._methods.list import transpose  # For matrix operations
from plotext._constants import r2, inf  # Axis side constants
from plotext._signal import signal_class#, get_scatter_points
#from plotext._derived import default_marker


class signals_class:
    def __init__(self):
        self.clear()
        #self.set_default_marker()

    # Clear all stored signals
    def clear(self):
        self.signal = []

    # Add a new signal
    def add(self, signal):
        self.signal.append(signal)
        return self

    # def set_default_marker(self):
    #     self.default_marker = default_marker
    #     return self

    # def update_default_marker(self, marker):
    #     self.default_marker._fix(marker)
    # return self

    # Get number of signals stored
    def get_length(self):
        return len(self.signal)

    # Get range of indices for signals
    def get_range(self):
        return range(self.get_length())

    # Retrieve signal by index
    def get(self, index):
        return self.signal[index]

    # Get total points across all signals
    def get_total_points(self):
        return sum(el.get_length() for el in self)

    # Get combined x-axis limits from all signals
    def get_xlimits(self, ymin = -inf, ymax = inf):
        limits = [signal.get_xlimits(ymin, ymax) for signal in self.signal] 
        limits = transpose(limits, 2)
        return [min(limits[0], default = None), max(limits[1], default = None)]

    # Get combined y-axis limits from all signals
    def get_ylimits(self, xmin = -inf, xmax = inf):
        limits = [signal.get_ylimits(xmin, xmax) for signal in self.signal]
        limits = transpose(limits, 2)
        return [min(limits[0], default = None), max(limits[1], default = None)]

    # Get limits for specified axis and side
    def get_limits(self, axis = 0, side = 0, min = -inf, max = inf):
        selection = self.select(yside = side) if axis else self.select(xside = side)
        return selection.get_ylimits(min, max) if axis else selection.get_xlimits(min, max)

    def select_in_matrix(self, width, height):
        [signal.select_in_matrix(width, height) for signal in self.signal]
        return self


    # Fix background for all signals
    def fix_background(self, pixel):
        for signal in self.signal:
            signal.fix_background(pixel)
        return self

    #def get_

    def draw(self, signal):
        #signal = get_scatter_points(*args, marker = marker, xside = xside, yside = yside, label = label) 

        # if filly is not None and filly != False:
        #     level = 0 if isinstance(filly, bool) else filly 
        #     filly = [level] * length
        #     fillm = m if fillm is None else fillm
        #     fillm = correct.markers(fillm, default_marker, length)
        #     signal.set_fill(x, filly, fillm)
            
        self.add(signal)
        return self 

    # def plot(self, *args, marker = None, fillx = None, filly = None, xside = None, yside = None, label = None):
    #     x, y = correct.data(*args)
    #     length = len(x)
    #     label = self.correct_label(label)
    #     m = correct.markers(marker, default_marker, length)
    #     signal = signal_class(x, y, m, xside, yside, label, self.default_marker) 
    #     xf = [x[0]] + x[:-1]
    #     yf = [y[0]] + y[:-1]
    #     mf = [m[0]] + m[:-1]
    #     #signal.set_fill(xf, yf, mf)
    #     self.add(signal)
    #     return self




    # Select signals matching xside and yside criteria
    def select(self, xside = None, yside = None):
        xside = r2 if xside is None else [xside]
        yside = r2 if yside is None else [yside]
        filtered = [s for s in self.signal if s.get_xside() in xside and s.get_yside() in yside]
        new_signals = signals_class()
        new_signals.signal = filtered
        return new_signals

    # Deep copy of signals_class instance
    def copy(self):
        out = signals_class()
        out.signal = [signal.copy() for signal in self.signal]
        return out

    # Clone signals from another signals_class instance
    def clone(self, signals):
        self.signal = [el.copy() for el in signals.signal]
        return self

    # Generate a summary log of signals
    def get_log(self, fill = False):
        log = f"{self.get_length()} Signals \n"
        for i in self.get_range():
            log += ' ' + self.get(i).get_log(fill) + '\n'
        return log

    # String representation returns the log summary
    def __repr__(self):
        return self.get_log()

    # Print the log summary
    def log(self, fill = False):
        print(self.get_log(fill))

    # Iterator over stored signals
    def __iter__(self):
        return iter(self.signal)
