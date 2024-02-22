from plotext._default import default_signal
from plotext._placement import placement
from plotext._marker import default_marker, harmonize_markers
from plotext._colorize import colorize


class signals_class():
    def __init__(self):
        self._clear_signals()

    def _clear_signals(self):
        self._signals = []
        self._past_colors = []

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
        marker = self._correct_markers(marker)
        self._draw(*args, marker = marker, xside = xside, yside = yside, lines = False, fillx = fillx, filly = filly)
        
    def plot(self, *args, marker = None, xside = None, yside = None, fillx = False, filly = False):
        marker = self._correct_markers(marker)
        self._draw(*args, marker = marker, xside = xside, yside = yside, lines = True, fillx = fillx, filly = filly)
        

    def _correct_markers(self, markers = None):
        markers = default_marker if markers is None else markers
        markers = [markers] if not isinstance(markers, list) else markers
        markers = list(map(self._correct_marker, markers))
        markers = harmonize_markers(markers)
        return markers
    
    def _correct_marker(self, single_marker):
        single_marker = colorize(single_marker, fullground = self._next_color(), background = self._canvas_color) if isinstance(single_marker, str) else single_marker
        #single_marker = single_marker._colorize() if isinstance(single_marker, marker) else single_marker
        return single_marker


    def _next_color(self):
        color = difference(self._color_sequence, self._past_colors)
        color = color[0] if len(color) > 0 else self.color_sequence[0]
        return color


class signal_class():
    def __init__(self, x, y, marker, xside, yside, lines, fillx, filly):
        self.x, self.y = x, y
        self.length = len(x)
        marker = repeat(marker, self.length)
        self.marker = marker#[m.copy() for m in marker]
        #if isinstance(marker, list) else marker
        self.xside = placement.correct_xside(xside)
        self.yside = placement.correct_yside(yside)
        self.lines = lines
        self.fillx = fillx
        self.filly = filly

                                               
   # marker = [marker] if isinstance(marker, (str, marker, colorize)) else marker
   # marker = list(map(correct_marker, marker))
   # hd_markers = 
   # marker = [hd_markers[0]] if len(hd_markers) > 0 else [el[0] for el in marker]
   #return marker


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



           

        
def repeat(data, length): # repeat the same data till length is reached
    l = int(length / len(data) + 1); L = range(l)
    for i in L:
        data += data
    return data[ : length]


def difference(data1, data2) : # elements in data1 not in date2
    return [el for el in data1 if el not in data2]
