from plotext._default import default_signal
from plotext._placement import placement

class signal_class():
    def __init__(self, x, y, xside = None, yside = None):
        self.x, self.y = x, y
        self.xside = placement.correct_xside(xside)
        self.yside = placement.correct_yside(yside)
        self.length = len(x)

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


    def _get_xmin(self, xside = None):
        xside = placement.correct_xside(xside)
        return min([s.get_xmin() for s in self._signals if s.xside == xside], default = None)
    
    def _get_xmax(self, xside = None):
        xside = placement.correct_xside(xside)
        return max([s.get_xmax() for s in self._signals if s.xside == xside], default = None)

    def _get_xlim_signals(self, xside = None):
        return (self._get_xmin(xside), self._get_xmax(xside))
    
    def _get_ymin(self, yside = None):
        yside = placement.correct_yside(yside)
        return min([s.get_ymin() for s in self._signals if s.yside == yside], default = None)
    
    def _get_ymax(self, yside = None):
        yside = placement.correct_yside(yside)
        return max([s.get_ymax() for s in self._signals if s.yside == yside], default = None)

    def _get_ylim_signals(self, yside = None):
        return (self._get_ymin(yside), self._get_ymax(yside))

# Draw Functions
  
    def _draw(self, x, y, xside = None, yside = None):
        self.extend('_draw', x, y, xside = None, yside = None)
        signal = signal_class(x, y, xside, yside)
        self._signals.append(signal)

    def scatter(self, *args, xside = None, yside = None):
        self._draw(*args, xside = xside, yside = yside)



