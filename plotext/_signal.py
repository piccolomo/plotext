from plotext._default import default_signal
from plotext._default import correct_xside, correct_yside
from plotext._list import set_data


class signal_class():
    def __init__(self):
        self.set()

    def set(self, *args, xside = None, yside = None):
        self.x, self.y = set_data(*args)
        self.update_length()
        self.xside = correct_xside(xside)
        self.yside = correct_yside(yside)

    def update_length(self):
        self.length = len(self.x)

        
    def xmin(self):
        return min(self.x, default = None)
    
    def xmax(self):
        return max(self.x, default = None)

    def xlim(self):
        return (self.xmin(), self.xmax())
    
    def ymin(self):
        return min(self.y, default = None)
    
    def ymax(self):
        return max(self.y, default = None)
        
    def ylim(self):
        return (self.ymin(), self.ymax())

    
    def __repr__(self):
        out = 'length ' + str(self.length)
        return out

    def print(self):
        print(self)


class signals_class():
    def __init__(self):
        self.list = []
        self.update_length()

    def add(self, *args, **kwargs):
        signal = signal_class()
        signal.set(*args, **kwargs)
        self.list.append(signal)
        self.update_length()

    def update_length(self):
        self.length = len(self.list)


    def xmin(self, xside = None):
        xside = correct_xside(xside)
        return min([s.xmin() for s in self.list if s.xside == xside], default = None)
    
    def xmax(self, xside = None):
        xside = correct_xside(xside)
        return max([s.xmax() for s in self.list if s.xside == xside], default = None)

    def xlim(self, xside = None):
        return (self.xmin(xside), self.xmax(xside))
    
    def ymin(self, yside = None):
        yside = correct_yside(yside)
        return min([s.ymin() for s in self.list if s.yside == yside], default = None)
    
    def ymax(self, yside = None):
        yside = correct_yside(yside)
        return max([s.ymax() for s in self.list if s.yside == yside], default = None)

    def ylim(self, yside = None):
        return (self.ymin(yside), self.ymax(yside))

    
    def __repr__(self):
        out = '\n'.join([repr(el) for el in self.list])
        return out
