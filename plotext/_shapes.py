from plotext._signal import signal_class

def get_rectangle(self, x, y = None, marker = None, lines = None, fill = None, xside = None, yside = None, label = None):
    x = [0, 1] if x is None or len(x) < 2 else x  
    y = [0, 1] if y is None or len(y) < 2 else y  
    xpos = self.xside_to_pos(xside)
    ypos = self.yside_to_pos(yside)
    lines = True if lines is None else lines
    fill = False if fill is None else fill
    xm = min(x); xM = max(x);
    ym = min(y); yM = max(y);
    dx = abs(xM - xm); dy = abs(yM - ym);
    if reset_lim:
        self.xlim[xpos] = [xm - 0.5 * dx, xM + 0.5 * dx]
        self.ylim[xpos] = [ym - 0.5 * dy, yM + 0.5 * dy]
    x, y = [xm, xm, xM, xM, xm], [ym, yM, yM, ym, ym]
    self.draw(x, y,
              xside = xside, 
              yside = yside,
              lines = True if fill else lines,
              marker = marker,
              color = color,
              fillx = "internal" if fill else False,
              filly = False,
              label = label)
