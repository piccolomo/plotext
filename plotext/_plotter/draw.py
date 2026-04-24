# Draw mixin: high-level drawing primitives (signal, candlestick, polygon) on top of plot_class

import math

from plotext._correct import matrix as correct_matrix
from plotext._primitives.marker import marker
from plotext._methods import sequence


# Drawing mixin providing signal, candlestick and polygon methods
class draw_class:

    # Draw a pre-built signal on the plot and propagate to subplots
    def draw(self, signal):
        self._signals._add(signal)
        self._cycler.remove_colors(signal._get_foreground_unique_integer_colors())

        self._for_each_subplot("draw", signal)
        return self

    # Build (but do not draw) an OHLC candlestick signal from a dict with keys
    # 'date', 'open', 'close', 'high', 'low'. Pass the returned signal to draw().
    def candlestick(self, data, colors = None, orientation = None, xside = None, yside = None):
        # Orientation: vertical = dates on x and prices on y (the usual case);
        # horizontal = dates on y and prices on x.
        orientation = correct_matrix.orientation(orientation)
        is_vertical = orientation in ['v', 'vertical']

        # Up / down candle colors (up = close > open).
        # Dojis (open == close) use the down color.
        colors = ["green", "red"] if colors is None else colors
        up_color, down_color = colors[0], colors[1]

        # Characters for the thin wick and the filled body.
        wick = '│' if is_vertical else '─'
        body = '█'

        # Unpack the OHLC dict (empty fallback so an empty chart still renders).
        data = {"date": [], "open": [], "close": [], "high": [], "low": []} if not data else data
        date = list(data["date"])
        op   = list(data["open"])          # 'open' would shadow the builtin
        cl   = list(data["close"])
        high = list(data["high"])
        low  = list(data["low"])
        n    = len(date)

        # Body limits per candle: bottom = min(open, close), top = max(open, close).
        body_bot = [min(op[i], cl[i]) for i in range(n)]
        body_top = [max(op[i], cl[i]) for i in range(n)]

        # Per-candle color and the two sets of markers (wick line / body block).
        candle_color = [up_color if op[i] < cl[i] else down_color for i in range(n)]
        wick_marker  = [marker(wick, candle_color[i]) for i in range(n)]
        body_marker  = [marker(body, candle_color[i]) for i in range(n)]

        # Helper: build a signal where (top_values) are the main points and
        # (bot_values) are attached as fill points. Orientation swaps x/y.
        def make(top_values, bot_values, mk):
            if is_vertical:
                x_top, y_top = date, top_values
                x_bot, y_bot = date, bot_values
            else:
                x_top, y_top = top_values, date
                x_bot, y_bot = bot_values, date
            s = self.signal(x_top, y_top, marker = mk, xside = xside, yside = yside)
            s.fill(self.signal(x_bot, y_bot, marker = mk))
            return s

        wick_signal = make(high,     low,      wick_marker)     # thin high-to-low line
        body_signal = make(body_top, body_bot, body_marker)     # filled body rectangle

        # Merge the body points into the wick signal so label / legend / cycler
        # treat the pair as a single entity. "┿" is the representative legend marker.
        wick_signal._append(body_signal)
        wick_signal._set_marker(marker("┿", up_color))

        return wick_signal

    # Draw a regular polygon centered at (x, y) with the given radius and number of sides
    def polygon(self, x = 0, y = 0, radius = 1, sides = 3, up = False, marker = None, lines = True, fill = False, xside = None, yside = None, label = None):
        sides = 3 if sides is None else max(3, sides)
        alpha = 2 * math.pi / sides
        init = alpha / 2 + math.pi / 2 if sides % 2 == 0 else alpha / 4 * ((-1) ** (sides // 2))
        extra = ((alpha / 2) * up if sides % 2 == 0 else alpha / 2 * (1 + up))
        get_point = lambda i: [x + math.cos(alpha * i + init + extra) * radius, y + math.sin(alpha * i + init + extra) * radius]
        points = [get_point(i) for i in range(sides + lines)]
        xl, yl = sequence.transpose(points)
        signal = self.signal(xl, yl, marker = marker, xside = xside, yside = yside).lines(lines)
        [signal._set_fill_point(i, x, 0 * y, signal.get_marker()) for i in range(sides + lines)] if fill else None
        self._draw_signal(signal)
        return signal