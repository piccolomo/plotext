from plotext._default import default_signal
from plotext._default import correct_xside, correct_yside


class signal_class():
    def __init__(self):
        self.set()

    def set(self, *args, xside = None, yside = None):
        self.x, self.y = set_data(*args)
        self.length = len(self.x)
        self.xside = correct_xside(xside)
        self.yside = correct_yside(yside)

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
        self.clear_data()

    def clear_data(self):
        self._signals = []
    
    def _draw(self, *args, **kwargs):
        self._add_signal(*args, **kwargs)

    def _get_xmin(self, xside = None):
        xside = correct_xside(xside)
        return min([s.get_xmin() for s in self._signals if s.xside == xside], default = None)
    
    def _get_xmax(self, xside = None):
        xside = correct_xside(xside)
        return max([s.get_xmax() for s in self._signals if s.xside == xside], default = None)

    def _get_xlim_signals(self, xside = None):
        return (self._get_xmin(xside), self._get_xmax(xside))
    
    def _get_ymin(self, yside = None):
        yside = correct_yside(yside)
        return min([s.get_ymin() for s in self._signals if s.yside == yside], default = None)
    
    def _get_ymax(self, yside = None):
        yside = correct_yside(yside)
        return max([s.get_ymax() for s in self._signals if s.yside == yside], default = None)

    def _get_ylim_signals(self, yside = None):
        return (self._get_ymin(yside), self._get_ymax(yside))

##############################################
###########    Draw Functions    #############
##############################################

    def _draw(self, *args, **kwargs):
        self.extend('_draw', *args, **kwargs)
        signal = signal_class()
        signal.set(*args, **kwargs)
        self._signals.append(signal)

    def scatter(self, *args, xside = None, yside = None):
        self._draw(*args, xside = xside, yside = yside)


# Signal Utilities

def set_data(x = None, y = None): # it return properly formatted x and y data lists
   if x is None and y is None:
       x, y = [], []
   elif x is not None and y is None:
       y = x
       x = list(range(len(y)))
   lx, ly = len(x), len(y)
   if lx != ly:
       l = min(lx, ly)
       x = x[ : l]
       y = y[ : l]
   return [list(x), list(y)]
