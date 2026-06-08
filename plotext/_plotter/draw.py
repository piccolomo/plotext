# Draw mixin: high-level drawing primitives on top of plot_class. Methods are grouped:
#   1. Registration       — draw
#   2. Annotation         — text
#   3. Geometric shapes   — line, rectangle, polygon                   (built directly from signal)
#   4. Bar family         — bar, multiple_bar, stacked_bar, hist, box   (bar uses rectangle; the other four use bar / rectangle / segment)
#   5. Specialized        — candlestick, error, event              (compose line + rectangle / segment)

import math

from plotext._correct import matrix as correct_matrix
from plotext._correct import data as correct_data
from plotext._correct import axis as correct_axis
from plotext._correct import bool as correct_bool
from plotext._correct import placement as correct_placement
from plotext._correct import pixel as correct_pixel
from plotext._correct import line as correct_line
from plotext._correct import label as correct_label
from plotext._correct import marker as correct_marker
from plotext._correct import bar    as correct_bar
from plotext._correct import candlestick as correct_candlestick
from plotext._correct import heatmap as correct_heatmap
from plotext._primitives.marker import marker as marker_class
from plotext._primitives.matrix_marker import matrix_marker
from plotext._primitives.matrix import matrix as matrix_class
from plotext._primitives.colorize import colorize as colorize_class
from plotext._primitives.box import box_class, line
from plotext._primitives.pixel import pixel as pixel_class
from plotext._plotter.utils.interactive import refresh, silent
from plotext._settings import defaults
from plotext._methods import sequence
from plotext._methods.bar import bar_edges, box_data, hist_data, is_vertical
from plotext._methods.ruler import get_labels
from plotext._methods.object import is_rgb


class draw_class:

    # ---- 1. Registration ----------------------------------------------------

    # Register a pre-built drawable (always a signal now: plotted data, lines, annotations) on the plot and propagate to subplots
    @refresh
    def draw(self, drawable):
        self._signals._add(drawable)
        self._cycler.remove_pixels(drawable._get_unique_pixels())
        self._for_each_subplot("draw", drawable)
        return self

    # ---- 2. Annotation ------------------------------------------------------

    # Build a text annotation at (x, y): one-point signal whose marker is a MatrixMarker carrying the label matrix. orientation=0 horizontal (W×1 label, alignment maps to ha — accepts left/center/right), orientation=1 vertical (label transposed to 1×W, alignment maps to va — accepts top/center/bottom). Caller passes the result to draw() to register it.
    def text(self, x, y, label, alignment = None, orientation = None, xside = None, yside = None):
        label = correct_label.label(label, self._canvas_pixel)
        orientation = correct_placement.orientation(orientation)
        alignment = correct_placement.alignment(alignment, orientation = orientation)
        ha, va = (-1, alignment) if orientation == 1 else (alignment, -1)
        return self.signal([x], [y], marker = matrix_marker(label.transpose() if orientation == 1 else label, ha = ha, va = va), xside = xside, yside = yside)

    # ---- 3. Geometric shapes ------------------------------------------------

    # Build a straight line segment between two endpoints (x = (x1, x2), y = (y1, y2)). Free 2-point line for arbitrary diagonals or axis-aligned segments.
    def segment(self, x = (0, 1), y = (0, 1), marker = None, xside = None, yside = None):
        return self.signal(list(x)[:2], list(y)[:2], marker = marker, xside = xside, yside = yside).lines(True)

    # Add a line at coord. orientation 0 = horizontal (on y-ruler), 1 = vertical (on x-ruler). Registered on the ruler; rendered at build time.
    @refresh
    def line(self, coord, orientation = 0, relative = False, pixel = None, style = None, label = None, xside = None, yside = None):
        orientation = correct_placement.orientation(orientation)
        relative    = correct_bool.boolean(relative, False)
        pixel       = correct_pixel.pixel(pixel, defaults.pixels["line"])
        style       = correct_line.line_style(style)
        label       = correct_label.label(label, pixel)

        if orientation == 1:
            xside = correct_axis.side(0, xside)
            ruler = self._rulers.get(axis = 0, side = xside)
        else:
            yside = correct_axis.side(1, yside)
            ruler = self._rulers.get(axis = 1, side = yside)

        ruler.add_line(coord, relative, pixel, style, label)
        self._for_each_subplot("line", coord, orientation, relative, pixel, style, label, xside, yside)
        return self

    # Build a rectangle signal spanning given x/y ranges; lines = outline, fill = body. Optional `label` centered inside the rectangle.
    def rectangle(self, x = (0, 1), y = (0, 1), marker = None, lines = True, fill = True, label = None, xside = None, yside = None):
        x0, x1 = min(x), max(x)
        y0, y1 = min(y), max(y)
        if fill:
            upper = self.signal([x0, x1], [y1, y1], marker = marker, xside = xside, yside = yside).fill_method("full")
            if lines: upper.line_method("full")
            lower = self.signal([x0, x1], [y0, y0], marker = marker)
            upper.fill(lower)
            upper.lines(lines)
            sig = upper
        else:
            xs = [x0, x1, x1, x0, x0]
            ys = [y0, y0, y1, y1, y0]
            sig = self.signal(xs, ys, marker = marker, xside = xside, yside = yside)
            if lines: sig.line_method("full")
            sig.lines(lines)
        if label is not None:
            rect_pixel = sig._get_marker().get_pixel()
            if fill:
                label_pixel = rect_pixel.copy()._swap()                                # bg = rect.fg
                label_pixel._copy_fullground(self._canvas_pixel.copy()._swap())        # fg = canvas.bg
            else:
                label_pixel = pixel_class()._copy_fullground(rect_pixel)               # fg = rect.fg
            label_mat = correct_label.label(label, label_pixel)
            join = sig.get_length()
            sig._append(self.signal([(x0 + x1) / 2], [(y0 + y1) / 2], marker = matrix_marker(label_mat, ha = 0, va = 0), xside = xside, yside = yside))
            sig._set_connected(join, False)
        return sig

    # Build a regular polygon signal centred at (x, y) with given radius and sides.
    def polygon(self, x = 0, y = 0, radius = 1, sides = 3, up = False, marker = None, lines = True, fill = False, xside = None, yside = None):
        sides = 3 if sides is None else max(3, sides)
        alpha = 2 * math.pi / sides
        init = alpha / 2 + math.pi / 2 if sides % 2 == 0 else alpha / 4 * ((-1) ** (sides // 2))
        extra = (alpha / 2) * up if sides % 2 == 0 else alpha / 2 * (1 + up)
        get_point = lambda i: [x + math.cos(alpha * i + init + extra) * radius,
                               y + math.sin(alpha * i + init + extra) * radius]
        points = [get_point(i) for i in range(sides + 1)]   # +1 closes the path
        xl, yl = sequence.transpose(points)
        signal = self.signal(xl, yl, marker = marker, xside = xside, yside = yside)
        if lines: signal.line_method("full")
        if fill:
            signal.fill_method("full")
            for i, p in enumerate(signal):
                signal._set_fill_point(i, x, y, p.get_marker())
        signal.lines(lines)
        return signal

    # ---- 4. Bar family ------------------------------------------------------

    # Build a bar plot signal; args: bar(y_max), bar(x, y_max), or bar(x, y_min, y_max). When labelled=True each bar carries its height value (y_max) as the rectangle's centered label.
    @silent
    def bar(self, *args, marker = None, width = None, orientation = None, lines = True, fill = True, labelled = False, xside = None, yside = None, _reset_ticks = True, _offset = 0):
        x, y_min, y_max = correct_bar.bar_data(*args)
        width = correct_bar.width(width)

        # String x → integer positions; remember original strings as labels
        string_x = any(isinstance(el, str) for el in x)
        if string_x:
            positions = list(range(1, len(x) + 1))
            labels = list(map(str, x))
            x = positions

        # Apply x offset
        x = [el + _offset for el in x]

        # Numeric x: bar centres (post-offset) become tick positions, their string version the labels
        if not string_x:
            positions = list(x)
            labels = get_labels(x)

        # Bar geometry
        xe, ye = bar_edges(x, y_min, y_max, width)

        vertical = is_vertical(correct_matrix.orientation(orientation))

        # Pick the marker once so every bar shares the same colour from the cycler; normalize so string codes ('hd', 'full', a single char) become proper marker instances.
        bar_marker = correct_marker.marker(marker, self._next_marker())

        # Start empty and append one rectangle per bar; disconnect at joins keeps outlines isolated
        sig = self.signal([], [], marker = bar_marker, xside = xside, yside = yside)
        for i in range(len(x)):
            rx, ry = (xe[i], ye[i]) if vertical else (ye[i], xe[i])
            rect = self.rectangle(rx, ry, marker = bar_marker,
                                  lines = lines, fill = fill,
                                  label = str(y_max[i]) if labelled else None,
                                  xside = xside, yside = yside)
            join = sig.get_length()
            sig._append(rect)
            # Break the line from the previous bar's last point to this bar's first (harmless when join=0)
            sig._set_connected(join, False)

        # Auto-set ticks at bar centres (string version of value as label)
        if _reset_ticks:
            if vertical:
                self.ticks(positions, labels = labels, axis = "x", side = xside)
            else:
                self.ticks(positions, labels = labels, axis = "y", side = yside)

        return sig

    # Build a grouped bar plot from (x, Y) where Y is a list of height-sequences; sub-bars are merged into one signal via _append, per-rectangle markers preserve cycler colours.
    @silent
    def multiple_bar(self, *args, marker = None, width = None, orientation = None, lines = True, fill = True, labelled = False, xside = None, yside = None, _reset_ticks = True, _offset = None):
        x, Y = correct_bar.multiple_bar_data(*args)
        n = len(Y)
        width = correct_bar.width(width)
        sub_width = width / n if n else 0
        offsets = [(-1/2 + 1/(2 * n)) + i / n for i in range(n)]
        markers = marker if isinstance(marker, list) else [marker] * n

        # _offset = where the category label sits relative to the integer position. Default lines it up with the first sub-bar in horizontal orientation (avoids row-rounding collisions); stays centered (0) in vertical, where sub-cell rendering handles the gap cleanly.
        vertical = is_vertical(correct_matrix.orientation(orientation))
        if _offset is None: _offset = 0 if vertical or not n else offsets[0]

        # Start empty and append one sub-bar per Y row (mirrors bar()'s own start-empty-then-append pattern).
        main = self.signal([], [], xside = xside, yside = yside)
        for i in range(n):
            # _reset_ticks=False on sub-bars: each bar() shifts x by its offset, ticks would land off-centre — we re-set them ourselves below at group centres.
            sub = self.bar(x, Y[i], marker = markers[i], width = sub_width, orientation = orientation, _offset = offsets[i], lines = lines, fill = fill, labelled = labelled, xside = xside, yside = yside, _reset_ticks = False)
            # Mark this bar's colour as used so the next sub-bar's _next_marker() picks a different one (draw() normally does this — we trigger it inline).
            self._cycler.remove_pixels(sub._get_unique_pixels())
            main._append(sub)

        if _reset_ticks and n:
            string_x = any(isinstance(el, str) for el in x)
            positions = [p + _offset for p in (range(1, len(x) + 1) if string_x else x)]
            labels = list(map(str, x)) if string_x else get_labels(x)
            axis = "x" if vertical else "y"
            self.ticks(positions, labels = labels, axis = axis, side = xside if axis == "x" else yside)

        return main

    # Build a stacked bar plot from (x, Y) where Y is a list of height-sequences; each group's bar starts at the previous group's cumulative top via the 3-arg bar(x, y_min, y_max) form.
    @silent
    def stacked_bar(self, *args, marker = None, width = None, orientation = None, lines = True, fill = True, labelled = False, xside = None, yside = None, _reset_ticks = True):
        x, Y = correct_bar.multiple_bar_data(*args)
        n = len(Y)
        width = correct_bar.width(width)
        markers = marker if isinstance(marker, list) else [marker] * n

        # Cumulative running sum per x slot; each group becomes a 3-arg bar from previous_cum to new_cum.
        cum = [0] * len(x)
        main = self.signal([], [], xside = xside, yside = yside)
        for i in range(n):
            y_min = list(cum)
            cum = [cum[k] + Y[i][k] for k in range(len(x))]
            sub = self.bar(x, y_min, list(cum), marker = markers[i], width = width, orientation = orientation, lines = lines, fill = fill, labelled = labelled, xside = xside, yside = yside, _reset_ticks = _reset_ticks if i == 0 else False)
            self._cycler.remove_pixels(sub._get_unique_pixels())
            main._append(sub)
        return main

    # Build a histogram from a flat data sequence: bin via hist_data() then forward to bar() with _reset_ticks=False so the frequency-based ticks survive.
    def hist(self, data, bins = 10, marker = None, width = None, orientation = None, norm = False, lines = True, fill = True, xside = None, yside = None):
        x, y = hist_data(data, bins, norm)
        return self.bar(x, y, marker = marker, width = width, orientation = orientation, lines = lines, fill = fill, xside = xside, yside = yside, _reset_ticks = False)

    # Build a box-and-whisker plot per category from raw values: a Q1..Q3 rectangle, a median segment across it, and whiskers from box edges to min/max.
    @silent
    def box(self, *args, marker = None, width = None, orientation = None, lines = True, fill = True, xside = None, yside = None):
        x, y = correct_data.data(*args)
        width = correct_bar.width(width)
        lows, q1s, q2s, q3s, highs = box_data(y)

        positions      = list(range(1, len(x) + 1)) if any(isinstance(el, str) for el in x) else list(x)
        vertical       = is_vertical(correct_matrix.orientation(orientation))
        swap           = lambda a, b: (a, b) if vertical else (b, a)
        box_marker     = correct_marker.marker(marker, self._next_marker())
        whisker_marker = line(orientation = int(vertical), pixel = box_marker.get_pixel())
        median_pixel   = box_marker.get_pixel()
        median_pixel._copy_background(self._canvas_pixel)
        median_pixel._swap()                                                # fg = canvas bg, bg = box fg
        median_marker  = line(orientation = 1 - int(vertical), pixel = median_pixel)   # thin perpendicular line glyph; the swapped pixel paints fg = canvas bg, bg = box fg

        xe, _ = bar_edges(positions, lows, highs, width)
        sig = self.signal([], [], xside = xside, yside = yside)
        sig._set_marker(box_marker)
        for i, c in enumerate(positions):
            # Order matters: whiskers first, then the box (so its outline overwrites the whisker tips at the edge cells), then the median (so it overwrites the box body where it crosses).
            subs = (
                self.segment  (*swap((c, c), (q3s[i], highs[i])), marker = whisker_marker, xside = xside, yside = yside),
                self.segment  (*swap((c, c), (lows[i], q1s[i])), marker = whisker_marker, xside = xside, yside = yside),
                self.rectangle(*swap(xe[i], (q1s[i], q3s[i])), marker = box_marker, lines = lines, fill = fill, xside = xside, yside = yside),
                self.segment  (*swap(xe[i], (q2s[i], q2s[i])), marker = median_marker, xside = xside, yside = yside),
            )
            for sub in subs:
                join = sig.get_length()
                sig._append(sub)
                sig._set_connected(join, False)

        labels = list(map(str, x)) if any(isinstance(el, str) for el in x) else get_labels(x)
        self.ticks(positions, labels = labels, axis = "x" if vertical else "y", side = (xside if vertical else yside) or 0)
        return sig

    # ---- 5. Specialized -----------------------------------------------------

    # Build an OHLC candlestick signal from a dict with date/open/close/high/low keys. style='candle' (default) draws a filled body between open and close; style='ohlc' replaces the body with two short ticks (open extending towards the previous bar, close extending towards the next) — flatter, preferred when bars are dense. tick controls the OHLC tick half-width (autosized to 40% of the median date spacing when None); ignored for candles.
    def candlestick(self, data, style = None, tick = None, orientation = None, xside = None, yside = None):
        vertical = is_vertical(correct_matrix.orientation(orientation))
        style    = correct_candlestick.style(style)

        up_pixel   = pixel_class(foreground = defaults.candlestick_up_color)
        down_pixel = pixel_class(foreground = defaults.candlestick_down_color)
        body_ch = '█'

        data = {"date": [], "open": [], "close": [], "high": [], "low": []} if not data else data
        date = list(data["date"])
        op   = list(data["open"])
        cl   = list(data["close"])
        high = list(data["high"])
        low  = list(data["low"])
        n    = len(date)

        # OHLC mode: tick = number of dash cells flanking the wick (default 2). Ticks are stamped as matrix markers whose first / last cell carries the explicit corner glyph (├ / ┤ for vertical, ┴ / ┬ for horizontal), so the wick column doesn't get the perpendicular arm and crossings stay one-sided.
        if style == 'ohlc':
            tick = 2 if tick is None else int(tick)
            if vertical:
                close_glyphs, open_glyphs = '├' + '─' * tick, '─' * tick + '┤'
                close_ha, close_va, open_ha, open_va = -1, 0, 1, 0
            else:
                close_glyphs, open_glyphs = '│\n' * tick + '┴', '┬' + '\n│' * tick
                close_ha, close_va, open_ha, open_va = 0, 1, 0, -1

        sig = self.signal([], [], xside = xside, yside = yside)
        sig._set_marker(box_class(up = True, down = True, left = True, right = True, pixel = up_pixel))
        for i in range(n):
            pix         = up_pixel if op[i] < cl[i] else down_pixel
            wick_marker = box_class(up = vertical, down = vertical, left = not vertical, right = not vertical, pixel = pix)
            wick = (self.segment((date[i], date[i]), (low[i], high[i]), marker = wick_marker, xside = xside, yside = yside) if vertical
                    else self.segment((low[i], high[i]), (date[i], date[i]), marker = wick_marker, xside = xside, yside = yside))

            if style == 'candle':
                body_lo, body_hi = min(op[i], cl[i]), max(op[i], cl[i])
                rx, ry = ((date[i], date[i]), (body_lo, body_hi)) if vertical else ((body_lo, body_hi), (date[i], date[i]))
                parts = (wick, self.rectangle(rx, ry, marker = marker_class(body_ch, pix), xside = xside, yside = yside))
            else:  # ohlc
                cm   = matrix_marker(colorize_class(close_glyphs).set_pixel(pix), ha = close_ha, va = close_va)
                om   = matrix_marker(colorize_class(open_glyphs ).set_pixel(pix), ha = open_ha,  va = open_va)
                if vertical:
                    c_tk = self.signal([date[i]], [cl[i]], marker = cm, xside = xside, yside = yside)
                    o_tk = self.signal([date[i]], [op[i]], marker = om, xside = xside, yside = yside)
                else:
                    c_tk = self.signal([cl[i]], [date[i]], marker = cm, xside = xside, yside = yside)
                    o_tk = self.signal([op[i]], [date[i]], marker = om, xside = xside, yside = yside)
                parts = (wick, o_tk, c_tk)

            for sub in parts:
                join = sig.get_length()
                sig._append(sub)
                sig._set_connected(join, False)

        return sig

    # Build an error-bar plot from (y) | (x, y) | (x, y, yerr) | (x, y, yerr, xerr); strokes are BoxMarkers so v/h overlaps merge to ┼.
    def error(self, *args, pixel = None, style = None, xside = None, yside = None, label = None):
        x, y, xerr, yerr = correct_data.error_data(*args)

        # Single colour for every part of every error bar; pixel overrides cycler when given.
        px       = correct_pixel.pixel(pixel, self._cycler.next_pixel())
        style    = correct_line.line_style(style)
        v_marker = box_class(up = True, down = True, pixel = px, style = style)
        h_marker = box_class(left = True, right = True, pixel = px, style = style)
        c_marker = box_class(up = True, down = True, left = True, right = True, pixel = px, style = style)

        sig = self.signal([], [], xside = xside, yside = yside)
        sig._set_marker(c_marker)
        sig._set_label(label) if label is not None else None
        for i in range(len(x)):
            v = self.segment((x[i], x[i]), (y[i] - yerr[i] / 2, y[i] + yerr[i] / 2), marker = v_marker, xside = xside, yside = yside)
            h = self.segment((x[i] - xerr[i] / 2, x[i] + xerr[i] / 2), (y[i], y[i]), marker = h_marker, xside = xside, yside = yside)
            c = self.signal([x[i]], [y[i]], marker = c_marker, xside = xside, yside = yside)
            for sub in (v, h, c):
                join = sig.get_length()
                sig._append(sub)
                sig._set_connected(join, False)
        return sig

    # Build an event plot via ruler-registered lines so each stem spans the full canvas and merges with the axes (┼ / ┴ / ┬ on the axis cells); the perpendicular axis is squashed to [0, 1] with no ticks. Returns the figure (no signal involved).
    @refresh
    def event(self, data, orientation = None, pixel = None, style = None, side = None, label = None):
        vertical = is_vertical(correct_matrix.orientation(orientation))
        line_orientation = 1 if vertical else 0
        pixel = correct_pixel.pixel(pixel, self._cycler.next_pixel())
        for i, d in enumerate(data):
            kwargs = {"xside": side} if vertical else {"yside": side}
            self.line(d, orientation = line_orientation, relative = True, pixel = pixel, style = style, label = label if i == 0 else None, **kwargs)
        data_axis = "x" if vertical else "y"
        cross_axis = "y" if vertical else "x"
        if data:
            self.lim(min(data), max(data), axis = data_axis)
        self.lim(0, 1, axis = cross_axis); self.frequency(0, axis = cross_axis)
        return self


    # ---- 6. Structured 2D data ---------------------------------------------

    # Heatmap signal: per-cell symbol coloured by colormap (numeric input) or RGB triple. fill=True densifies each row into a band filled to the previous row. Row 0 maps to the top. HD symbols rejected — cell resolution is one full char.
    def heatmap(self, data, map = 'gray', fill = False, symbol = None, xside = None, yside = None):
        rows, cols, m = correct_data.matrix(data)
        rgb = m if not m or is_rgb(m[0][0]) else correct_heatmap.colormap(m, map)
        signal = self.signal([], [], xside = xside, yside = yside)
        base_marker = marker_class(correct_heatmap.symbol(symbol))  # single template; per-cell markers are cheap clones with the cell pixel attached
        get_marker = lambda r, c:base_marker.copy()._set_pixel(pixel_class(rgb[r][c]))
        Cols = list(range(cols))
        prev_row_signal = None
        for r in range(rows):
            row = rows - 1 - r
            column_markers = [get_marker(r, c) for c in range(cols)]
            row_signal = self.signal(Cols, [row] * cols, marker = column_markers, xside = xside, yside = yside)
            row_signal.line_method("full").fill_method("full").lines(True) if fill else None
            row_signal.fill(prev_row_signal) if r != 0 and fill else None
            join = signal.get_length()
            signal._append(row_signal)
            signal._set_connected(join, False)                                          # break the line between consecutive rows so densification doesn't draw a diagonal across the canvas
            prev_row_signal = row_signal
        return signal


    # Image signal: opens via Pillow, optional gray, resamples to plot/terminal size, returns a heatmap with each pixel as one canvas char. Caller handles plot_size, frame, tick frequency.
    def image(self, path, gray = False, symbol = None):
        from plotext._settings import system
        from plotext._methods.file import correct as _correct_path
        img = system.Image.open(_correct_path(path))
        if gray: img = system.ImageOps.grayscale(img)
        img = img.convert('RGB')
        width, height = self.get_size()
        if width is None or height is None:
            from plotext._kernel.api import terminal
            width, height = terminal.get_size()
        img = img.resize((width, height))
        pixels = list(img.getdata())
        matrix = [list(pixels[r * width : (r + 1) * width]) for r in range(height)]
        return self.heatmap(matrix, fill = False, symbol = symbol)


    # Confusion matrix: builds a composite signal of gradient-filled rectangle cells from tabulated (actual, predicted) counts. Caller is responsible for ticks, axis labels, and title.
    def confusion_matrix(self, actual, predicted, labels = None, norm = False, map = 'gray'):
        labels, counts = sequence._crosstab(actual, predicted, labels)
        n = len(labels)
        rgb = correct_heatmap.colormap(counts, map)
        row_sums = [sum(row) or 1 for row in counts] if norm else None
        signal = self.signal([], [])
        for r in range(n):
            for c in range(n):
                y = n - 1 - r
                cell_marker = marker_class('█', pixel = pixel_class(foreground = rgb[r][c]))
                label = f"{counts[r][c] / row_sums[r] * 100:.0f} %" if norm else str(counts[r][c])
                cell_rect = self.rectangle(x = (c - 0.5, c + 0.5), y = (y - 0.5, y + 0.5), marker = cell_marker, lines = True, fill = True, label = label)
                join = signal.get_length()
                signal._append(cell_rect)
                signal._set_connected(join, False)
        return signal
