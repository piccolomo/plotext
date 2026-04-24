# Signals container: holds a list of signal objects, with aggregated limits and selection

from plotext._methods import sequence
from plotext._settings.constants.numerical import binary, infinity


# Container for multiple signal objects with aggregated limits and side-based selection
class signals_class:
    # Initialize signals container
    def __init__(self):
        self._clear()

    # Clear all signals
    def _clear(self):
        self._signal = []

    # Add a signal (as a copy)
    def _add(self, signal):
        self._signal.append(signal.copy())
        return self

    # Get number of signals
    def _get_length(self):
        return len(self._signal)

    # Get range for iteration
    def _get_range(self):
        return range(self._get_length())

    # Get signal by index
    def get(self, index):
        return self._signal[index]

    # Get total points across all signals
    def _get_total_points(self):
        return sum(el._get_length() for el in self._signal)

    # Get X limits across all signals
    def _get_xlimits(self, ymin = -infinity, ymax = infinity):
        limits = [s._get_xlimits(ymin, ymax) for s in self._signal]
        lo, hi = sequence.transpose(limits, 2)
        return [min(lo, default = None), max(hi, default = None)]

    # Get Y limits across all signals
    def _get_ylimits(self, xmin = -infinity, xmax = infinity):
        limits = [s._get_ylimits(xmin, xmax) for s in self._signal]
        lo, hi = sequence.transpose(limits, 2)
        return [min(lo, default = None), max(hi, default = None)]

    # Get axis/side limits
    def _get_limits(self, axis = 0, side = 0, min = -infinity, max = infinity):
        selection = self._select(yside = side) if axis else self._select(xside = side)
        return selection._get_ylimits(min, max) if axis else selection._get_xlimits(min, max)

    # Fix background for all signals
    def _fix_background(self, pixel):
        for s in self._signal:
            s._fix_background(pixel)
        return self

    # Select signals by X/Y side
    def _select(self, xside = None, yside = None):
        xside = binary if xside is None else [xside]
        yside = binary if yside is None else [yside]
        filtered = [s for s in self._signal if s._get_xside() in xside and s._get_yside() in yside]
        out = signals_class()
        out._signal = filtered
        return out

    # Copy signals container
    def _copy(self):
        out = signals_class()
        out._signal = [s.copy() for s in self._signal]
        return out

    # Clone signals from another container
    def _clone(self, signals):
        self._signal = [s.copy() for s in signals._signal]
        return self

    # Get log string for all signals
    def _get_log(self, fill = False):
        out = ""
        for i in self._get_range():
            out += str(i + 1) + "th " + self.get(i)._get_log(fill) + ('\n' * 2 if i != self._get_length() - 1 else '')
        return out

    # Print log
    def log(self, fill = False):
        print(self._get_log(fill))
        return self

    # Iterator over signals
    def __iter__(self):
        return iter(self._signal)

    # Represent signals container
    def __repr__(self):
        return f"Plotext Signals: {self._get_length()}"
