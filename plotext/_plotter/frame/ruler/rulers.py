# Rulers container: manages 2x2 X/Y rulers, selection, clearing, cloning, updates

from plotext._settings.constants.numerical import binary
from plotext._plotter.frame.ruler.ruler import xruler_class, yruler_class
from plotext._correct import axis as correct_axis
from plotext._methods.sequence import unique


# Rulers container: four ruler slots (x lower/upper, y left/right)
class rulers_class:

    # Initialize 2x2 X and Y rulers
    def __init__(self):
        self._x = [xruler_class(), xruler_class()]
        self._y = [yruler_class(), yruler_class()]

    # Clear all rulers settings
    def clear_settings(self):
        [r._clear_settings() for r in self._get_all()]
        return self

    # Clear all rulers pixels
    def clear_pixels(self):
        [r._clear_pixels() for r in self._get_all()]
        return self

    # Clear all rulers styles
    def clear_styles(self):
        [r._clear_styles() for r in self._get_all()]
        return self

    # Access a specific ruler
    def _get(self, axis = 0, side = 0):
        container = self._y if axis else self._x
        return container[side]

    # Activate one specific ruler
    def get(self, axis = 0, side = 0):
        axis = correct_axis.axis(axis)
        side = correct_axis.side(axis, side)
        return self._get(axis, side)

    # Select multiple rulers
    def select(self, axis = 0, side = 0):
        axes = correct_axis.axes(axis)
        sides = correct_axis.sides(axes, side)
        return [self._get(a, s) for a in axes for s in sides]

    # Return all rulers
    def _get_all(self):
        self.select(binary, binary)
        return list(self.__iter__())

    # Set alignment for selected rulers
    def set_alignment(self, alignment = None, axis = 0, side = 0):
        [r.set_alignment(alignment = alignment) for r in self.select(axis, side)]
        return self

    # Set direction for selected rulers
    def set_direction(self, direction = None, axis = 0, side = 0):
        [r.set_direction(direction = direction) for r in self.select(axis, side)]
        return self

    # Set scale for selected rulers
    def set_scale(self, scale = None, axis = 0, side = 0):
        [r.set_scale(scale = scale) for r in self.select(axis, side)]
        return self

    # Set limits for selected rulers
    def set_limits(self, lower = None, upper = None, axis = 0, side = 0):
        [r.set_limits(lower, upper) for r in self.select(axis, side)]
        return self

    # Set frequency for selected rulers
    def set_frequency(self, frequency = None, axis = 0, side = 0):
        [r.set_frequency(frequency) for r in self.select(axis, side)]
        return self

    # Set ticks for selected rulers
    def set_ticks(self, positions = None, labels = None, axis = 0, side = 0):
        [r.set_ticks(positions, labels) for r in self.select(axis, side)]
        return self

    # Set grid for selected rulers
    def set_grid(self, active = None, style = None, pixel = None, axis = 0, side = 0):
        [r.set_grid(active, style, pixel) for r in self.select(axis, side)]
        return self

    # Set date mode for selected rulers
    def set_date(self, active = True, form = None, origin = None, axis = None, side = None):
        [r.set_date(active, form, origin) for r in self.select(axis, side)]
        return self

    # Convert a time value using the selected ruler's date
    def convert(self, time, output = "timestamp", axis = None, side = None):
        return self.get(axis, side)._date.convert(time, output)

    # Get all line positions for a given axis
    def _get_line_positions(self, axis = 0):
        data = self._y if axis else self._x
        return sorted(unique(data[0]._lines.get_positions() + data[1]._lines.get_positions()))

    # Clone rulers from another instance
    def _clone(self, rulers):
        [self._get(a, s)._clone(rulers._get(a, s)) for a in binary for s in binary]
        return self

    # Create a copy of this rulers instance
    def copy(self):
        out = rulers_class()
        out._clone(self)
        return out

    # Update ticks limits based on signal limits
    def _update_signals_limits(self, signals):
        for axis in binary:
            for side in binary:
                lim = self._get(int(not axis), side)._get_limits()
                lim = signals._get_limits(axis, side, *lim)
                self._get(axis, side)._update_limits(lim)
        return self

    # Update ticks limits
    def _update_ticks_limits(self):
        [self._get(a, s)._update_ticks_limits() for s in binary for a in binary]
        return self

    # Update lines limits
    def _update_lines_limits(self):
        [self._get(a, s)._update_lines_limits() for s in binary for a in binary]
        return self

    # Update ticks
    def _update_ticks(self):
        [self._get(a, s)._update_ticks() for s in binary for a in binary]
        return self

    # Update lines
    def _update_lines(self):
        [self._get(a, s)._update_lines() for s in binary for a in binary]
        return self

    # Rescale x-rulers to width and y-rulers to height
    def _rescale(self, width, height):
        [x._rescale(width) for x in self._x]
        [y._rescale(height) for y in self._y]

    # Add grid lines to all rulers
    def _add_grid_lines(self):
        [self._get(a, s)._add_grid_lines() for s in binary for a in binary]
        return self

    # Fix pixels for all rulers
    def _fix_pixels(self, pixel):
        [self._get(a, s)._fix_grid_pixel(pixel)._fix_pixel(pixel) for s in binary for a in binary]
        return self

    # Convert to list of all rulers
    def __list__(self):
        return list(iter(self))

    # Iterator over all x and y rulers
    def __iter__(self):
        return iter([r for r in self._x + self._y if r])

    # Total number of rulers
    def __len__(self):
        return len(self.__list__())

    # String representation
    def __repr__(self):
        l = len(self)
        out = f"{l} Plotext Rulers"
        names = ["left" if a and not s else "right" if a and s else "lower" if not a and not s else "upper"
                 for a in binary for s in binary if self._get(a, s)]
        if l > 0:
            out += ": " + ', '.join(names)
        return out