from plotext._constants import r2
from plotext._ruler import *
from plotext._methods.log import *


class rulers_class:

    def __init__(self):
        self.x = [xruler_class(), xruler_class()]
        self.y = [yruler_class(), yruler_class()]
        
    # Clear all rulers and return self for chaining
    def clear(self):
        self.get(0, 0).clear()
        self.get(0, 1).clear()
        self.get(1, 0).clear()
        self.get(1, 1).clear()
        return self

    # def set(self, frequency = None, scale = None, alignment = None, direction = None, pixel = None, axis = 0, side = 0):
    #     axes = correct.axes(axis)
    #     sides = correct.sides(axis, side)
    #     [self.get(axis, side).set(frequency = frequency, alignment = alignment, direction = direction, scale = scale, pixel = pixel) for axis in axes for side in sides]
    #     return self

   #  def set_ticks(self, ticks = None, labels = None, axis = 0, side = 0):
   #      axis = correct.axis(axis)
   #      sides = correct.sides(axis, side)
   #      [self.get(axis, side).set_ticks(positions = ticks, labels = labels) for side in sides]
   #      return self

   # # Set default frequencies for x and y rulers
   #  def set_xfrequency(self, frequency = None):
   #      [el.set_frequency(frequency) for el in self.x]
   #      return self

   #  # Set default frequencies for x and y rulers
   #  def set_yfrequency(self, frequency = None):
   #      [el.set_frequency(frequency) for el in self.y]
   #      return self

   #  # Set default frequencies for x and y rulers
   #  def set_pixel(self, pixel = None):
   #      [el.set_pixel(pixel) for el in self.x]
   #      [el.set_pixel(pixel) for el in self.y]
   #      return self

    # Return ruler at specified axis and side (axis=0 for x, 1 for y)
    def get(self, axis = 0, side = 0):
        axis = correct.axis(axis)
        side = correct.side(axis, side)
        container = self.y if axis else self.x
        return container[side] 

    # Add a line to the specified ruler with given properties
    def add_line(self, position, style = None, pixel = None, orientation = None, side = None):
        sides = correct.single_side(axis, side)
        self.get(orientation, side).lines.add(position, orientation, style, pixel)
        return self

    # Clone rulers from another rulers_class instance
    def clone(self, rulers):
        [self.get(axis, side).clone(rulers.get(axis, side)) for axis in r2 for side in r2]
        return self

    # Update ticks limits for all rulers based on signals limits
    def update_ticks_limits(self, signals):
        for axis in r2: 
            for side in r2:
                lim = self.get(int(not axis), side).get_limits()
                lim = signals.get_limits(axis, side, *lim)
                #print(axis, side, not axis, lim0, lim)
                self.get(axis, side).update_ticks_limits(lim)
        return self

    # Update lines limits for all rulers
    def update_lines_limits(self):
        [self.get(axis, side).update_lines_limits() for axis in r2 for side in r2]
        return self

    # Update ticks for all rulers
    def update_ticks(self):
        [self.get(axis, side).update_ticks() for axis in r2 for side in r2]
        return self

    # Generate a log string for all rulers
    def get_log(self):
        log = ''
        for axis in r2:
            for side in r2:
                log += log_axis(axis, side) + ' ' + self.get(axis, side).get_log() + '\n'
        return log

    # Print the log of all rulers
    def log(self):
        print(self.get_log())

    def __repr__(self):
        return self.get_log()