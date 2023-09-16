from plotext._signal import signals_class
from plotext._axes import axis_class
from plotext._canvas import canvas_class
from plotext._matrix import matrix_class
from copy import deepcopy

class monitor_class():
    def __init__(self):
        self.signals = signals_class()
        self.set_axes()
        self.canvas = canvas_class()
        self.matrix = matrix_class()

    def set_axes(self):
        self.xaxes = [axis_class('x', 'lower'), axis_class('x', 'upper')]
        self.yaxes = [axis_class('y', 'left') , axis_class('y', 'right')]
    
    def copy(self): # to deep copy 
        return deepcopy(self)

    def set_size(self, width = None, height = None):
        self.width = None if width is None else int(width) 
        self.height = None if height is None else int(height)
        self.size = [self.width, self.height]

##############################################
##########    Draw() Function    #############
##############################################

    def draw(self, *args, **kwargs): # from draw() comes directly the functions scatter() and plot()
        self.signals.add(*args, **kwargs)
