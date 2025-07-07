from plotext._methods import *  # For matrix operations
from plotext._constants import r2  # Axis side constants


class signals_class:
    def __init__(self):
        self.clear()

    # Clear all stored signals
    def clear(self):
        self.signal = []

    # Add a new signal
    def add(self, signal):
        self.signal.append(signal)
        return self

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
    def get_xlimits(self):
        limits = [signal.get_xlimits() for signal in self.signal]
        limits = list_methods.transpose(limits, 2)
        return [min(limits[0], default=None), max(limits[1], default=None)]

    # Get combined y-axis limits from all signals
    def get_ylimits(self):
        limits = [signal.get_ylimits() for signal in self.signal]
        limits = list_methods.transpose(limits, 2)
        return [min(limits[0], default=None), max(limits[1], default=None)]

    # Get limits for specified axis and side
    def get_limits(self, axis=0, side=0):
        selection = self.select(yside=side) if axis else self.select(xside=side)
        return selection.get_ylimits() if axis else selection.get_xlimits()

    # Fix background for all signals
    def fix_background(self, pixel):
        for signal in self.signal:
            signal.fix_background(pixel)
        return self

    # Select signals matching xside and yside criteria
    def select(self, xside=None, yside=None):
        xside = r2 if xside is None else [xside]
        yside = r2 if yside is None else [yside]
        filtered = [s for s in self.signal if s.xside in xside and s.yside in yside]
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
    def get_log(self):
        log = f"{self.get_length()} Signals \n"
        for i in self.get_range():
            log += ' ' + self.get(i).get_log() + '\n'
        return log

    # String representation returns the log summary
    def __repr__(self):
        return self.get_log()

    # Print the log summary
    def log(self):
        print(self.get_log())

    # Iterator over stored signals
    def __iter__(self):
        return iter(self.signal)
