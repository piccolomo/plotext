# thisd file just holds the drawing methods of the plot class

from plotext._correct import correct_class as correct
from plotext._signal import signal_class
from plotext._marker import marker
from plotext._methods.list import math, transpose, insert_after_each, insert_before_each


class draw_class:

    def draw_signal(self, signal):
        self._signals.draw(signal)
        colors = signal.get_foreground_unique_integer_colors()
        self._cycler.remove_colors(colors)
        if self._has_subplots():
            [self._get_subplot(*pos).draw(signal) for pos in self._get_slots_range()]
        return self 

    def draw(self, *args, marker = None, fillx = None, filly = None, xside = None, yside = None, label = None, lines = False):
        x, y = correct.data(*args) 
        x = self._get_date(0, xside).convert(x, "timestamp") if self._get_date(0, xside)._active else x
        y = self._get_date(1, yside).convert(y, "timestamp") if self._get_date(1, yside)._active else y
        label = correct.signal_label(label) 
        signal = self.signal(x, y, marker = marker, xside = xside, yside = yside, label = label, lines = lines)
        [signal.set_fill_point(i, point.get_x(), 0, point.get_marker()) for i, point in enumerate(signal)] if fillx else None
        [signal.set_fill_point(i, 0, point.get_y(), point.get_marker()) for i, point in enumerate(signal)] if filly else None
        self.draw_signal(signal)
        return signal

    def candlestick(self, data, colors = None, orientation = None, xside = None, yside = None, label = None):
        # Default setup
        orientation = correct.orientation(orientation); is_vertical = orientation in ['v', 'vertical']
        colors = ["green", "red"] if colors is None else colors
        line = '│' if is_vertical else '─'; core = "█"

        data = {"date": [], "open": [], "close": [], "high": [], "low": []} if not data else data
        date, open, close, high, low = [list(data[el]) for el in ["date", "open", "close", "high", "low"]]
        converter = self._get_date(0, xside) if is_vertical else self._get_date(1, yside)
        date = converter.convert(date, "timestamp")

        m = [min(open[i], close[i]) for i in range(len(date))]
        M = [max(open[i], close[i]) for i in range(len(date))]
        core_marker = [marker(core, colors[0] if open[i] < close[i] else colors[1]) for i in range(len(date))]
        line_marker = [marker(line, colors[0] if open[i] < close[i] else colors[1]) for i in range(len(date))]

        x, y = (date, high) if is_vertical else (high, date)
        lines = self.signal(x, y, marker = line_marker, xside = xside, yside = yside, label = label)

        x, y = (date, low) if is_vertical else (low, date)
        lines.set_fill(self.signal(x, y, marker = line_marker))
        
        x, y = (date, M) if is_vertical else (M, date)
        core = self.signal(x, y, marker = core_marker, xside = xside, yside = yside)

        x, y = (date, m) if is_vertical else (m, date)
        core.set_fill(self.signal(x, y, marker = core_marker))

        signal = lines.append(core).set_marker(marker("┿", colors[0]))

        self.draw_signal(signal)
        return signal

    def polygon(self, x = 0, y = 0, radius = 1, sides = 3, up = False, marker = None, lines = True, fill = False, xside = None, yside = None, label = None):
        alpha = 2 * math.pi / sides
        init = alpha / 2 + math.pi / 2 if sides % 2 == 0 else alpha / 4 * ((-1) ** (sides // 2))# * math.pi #- ((-1) ** (sides)) * alpha / 4
        extra = ((alpha / 2) * up if sides % 2 == 0 else alpha / 2 * (1 + up)) #if up else (0 if sides % 2 == 0 else alpha / 2)
        get_point = lambda i: [x + math.cos(alpha * i + init + extra) * radius, y + math.sin(alpha * i + init + extra) * radius]
        # the rounding is needed so that results like 9.9999 are rounded to 10 and display as same coordinate in the plot, otherwise the floor function will turn 9.999 into 9
        points = [get_point(i) for i in range(sides + lines)] 
        #points = points[6:8]
        #print(points)
        xl, yl = transpose(points)
        signal = self.signal(xl, yl, marker = marker, xside = xside, yside = yside, lines = lines)
        #print(signal.get_length()) 
        #[signal.set_fill_point(i, signal.get_point(i).get_x(), 0*y, signal.get_marker()) for i in range(5)] if fill else None
        [signal.set_fill_point(i, x, y, signal.get_marker()) for i in range(sides + lines)] if fill else None

        #signal.log(1)
        #[signal.set_fill_point(i, x, y, signal.get_marker()) for i in signal.get_range()] if fill else None
        self.draw_signal(signal)
        return signal
        
