from plotext._methods.list import transpose
from plotext._constants import r2, inf


class signals_class:
    def __init__(self):
        self.clear()

    def clear(self):
        self.signal = []

    def add(self, signal):
        self.signal.append(signal)
        return self

    def get_length(self):
        return len(self.signal)

    def get_range(self):
        return range(self.get_length())

    def get(self, index):
        return self.signal[index]

    def get_total_points(self):
        return sum(el.get_length() for el in self.signal)

    def get_xlimits(self, ymin = -inf, ymax = inf):
        limits = [s.get_xlimits(ymin, ymax) for s in self.signal]
        lo, hi = transpose(limits, 2)
        return [min(lo, default = None), max(hi, default = None)]

    def get_ylimits(self, xmin = -inf, xmax = inf):
        limits = [s.get_ylimits(xmin, xmax) for s in self.signal]
        lo, hi = transpose(limits, 2)
        return [min(lo, default = None), max(hi, default = None)]

    def get_limits(self, axis = 0, side = 0, min = -inf, max = inf):
        selection = self.select(yside = side) if axis else self.select(xside = side)
        return selection.get_ylimits(min, max) if axis else selection.get_xlimits(min, max)

    def select_in_matrix(self, width, height):
        for s in self.signal:
            s.select_in_matrix(width, height)
        return self

    def fix_background(self, pixel):
        for s in self.signal:
            s.fix_background(pixel)
        return self

    def draw(self, signal):
        self.add(signal)
        return self

    def select(self, xside = None, yside = None):
        xside = r2 if xside is None else [xside]
        yside = r2 if yside is None else [yside]
        filtered = [s for s in self.signal if s.get_xside() in xside and s.get_yside() in yside]
        out = signals_class()
        out.signal = filtered
        return out

    def copy(self):
        out = signals_class()
        out.signal = [s.copy() for s in self.signal]
        return out

    def clone(self, signals):
        self.signal = [s.copy() for s in signals.signal]
        return self

    def get_log(self, fill = False):
        out = f"{self.get_length()} Signals\n"
        for i in self.get_range():
            out += ' ' + self.get(i).get_log(fill) + '\n'
        return out

    def __repr__(self):
        return self.get_log()

    def log(self, fill = False):
        print(self.get_log(fill))
        return self

    def __iter__(self):
        return iter(self.signal)
