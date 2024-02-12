from plotext._default import default_signal
from plotext._placement import placement
from plotext._marker import correct_markers

class signal_class():
    def __init__(self, x, y, marker, xside, yside, lines, fillx, filly):
        self.x, self.y = x, y
        self.length = len(x)
        marker = correct_markers(marker)
        self.marker = repeat(marker, self.length) if isinstance(marker, list) else marker
        self.xside = placement.correct_xside(xside)
        self.yside = placement.correct_yside(yside)
        self.lines = lines
        self.fillx = fillx
        self.filly = filly

    def get_xmin(self):
        return min(self.x, default = None)
    
    def get_xmax(self):
        return max(self.x, default = None)

    def get_xlim(self):
        return (self.get_xmin(), self.get_xmax())
    
    def get_ymin(self):
        return min(self.y, default = None)
    
    def get_ymax(self):
        return max(self.y, default = None)
        
    def get_ylim(self):
        return (self.get_ymin(), self.get_ymax())
    
    def __repr__(self):
        out = 'length ' + str(self.length)
        return out

    def print(self):
        print(self)


class signals_class():
    def __init__(self):
        self._clear_signals()

    def _clear_signals(self):
        self._signals = []


    def _get_signals_lim(self, axis, side):
        return self._get_signals_xlim(side) if axis == 1 else self._get_signals_ylim(side)


    def _get_signals_xlim(self, xside = None):
        return (self._get_signals_xmin(xside), self._get_signals_xmax(xside))

    def _get_signals_ylim(self, yside = None):
        return (self._get_signals_ymin(yside), self._get_signals_ymax(yside))


    def _get_signals_xmin(self, xside = None):
        xside = placement.correct_xside(xside)
        return min([s.get_xmin() for s in self._signals if s.xside == xside], default = None)
    
    def _get_signals_xmax(self, xside = None):
        xside = placement.correct_xside(xside)
        return max([s.get_xmax() for s in self._signals if s.xside == xside], default = None)

    def _get_signals_ymin(self, yside = None):
        yside = placement.correct_yside(yside)
        return min([s.get_ymin() for s in self._signals if s.yside == yside], default = None)
    
    def _get_signals_ymax(self, yside = None):
        yside = placement.correct_yside(yside)
        return max([s.get_ymax() for s in self._signals if s.yside == yside], default = None)

# Draw Functions
  
    def _draw(self, *args, **kwargs):
        self.extend('_draw', *args, **kwargs)
        signal = signal_class(*args, **kwargs)
        self._signals.append(signal)

    def scatter(self, *args, marker = None, xside = None, yside = None, fillx = False, filly = False):
        self._draw(*args, marker = marker, xside = xside, yside = yside, lines = False, fillx = fillx, filly = filly)
        
    def plot(self, *args, marker = None, xside = None, yside = None, fillx = False, filly = False):
        self._draw(*args, marker = marker, xside = xside, yside = yside, lines = True, fillx = fillx, filly = filly)
        

def repeat(data, length): # repeat the same data till length is reached
    l = int(length / len(data) + 1); L = range(l)
    for i in L:
        data += data
    return data[ : length]
