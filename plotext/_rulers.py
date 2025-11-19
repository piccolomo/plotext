from plotext._constants import r2
from plotext._ruler import *
from plotext._methods.string import *


class rulers_class:

    def __init__(self):
        self.x = [xruler_class(), xruler_class()]
        self.y = [yruler_class(), yruler_class()]

    # --- Clear all rulers ---
    def clear(self):
        for axis in r2:
            for side in r2:
                self.get(axis, side).clear()
        return self

    # --- Access rulers ---
    def get(self, axis = 0, side = 0):
        axis = correct.axis(axis)
        side = correct.side(axis, side)
        container = self.y if axis else self.x
        return container[side]

    # --- Add line to a specific ruler ---
    def add_line(self, position, style = None, pixel = None, orientation = 0, side = 0):
        self.get(orientation, side).lines.add(position, orientation, style, pixel)
        return self

    # --- Clone rulers from another rulers_class instance ---
    def clone(self, rulers):
        for axis in r2:
            for side in r2:
                self.get(axis, side).clone(rulers.get(axis, side))
        return self

    # --- Update ticks limits based on signals limits ---
    def update_ticks_limits(self, signals):
        for axis in r2:
            for side in r2:
                lim = self.get(int(not axis), side).get_limits()
                lim = signals.get_limits(axis, side, *lim)
                self.get(axis, side).update_ticks_limits(lim)
        return self

    # --- Update lines limits ---
    def update_lines_limits(self):
        for axis in r2:
            for side in r2:
                self.get(axis, side).update_lines_limits()
        return self

    # --- Update ticks ---
    def update_ticks(self):
        for axis in r2:
            for side in r2:
                self.get(axis, side).update_ticks()
        return self

    # --- Logging ---
    def get_log(self):
        log = ''
        for axis in r2:
            for side in r2:
                log += log_axis(axis, side) + ' ' + self.get(axis, side).get_log() + '\n'
        return log

    def log(self):
        print(self.get_log())
        return self

    def __repr__(self):
        return self.get_log()
