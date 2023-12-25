from plotext._default import default_figure
from plotext._subplot import subplot_class
from plotext._matrix import matrix_class
from plotext._settings import settings_class
from plotext._signal import signals_class
from plotext._build import build_class
from copy import deepcopy, copy

class figure_class(subplot_class, settings_class, matrix_class, signals_class, build_class):
    def __init__(self, parent = None, row = None, col = None):
        super(figure_class, self).__init__(parent, row, col)
        settings_class.__init__(self)
        matrix_class.__init__(self, 0, 0, background = 'white')
        signals_class.__init__(self)

    def _create_subplot(self, row = None, col = None):
        plot = figure_class(self, row, col)
        plot._copy_settings_from(self)
        plot._signals = self._signals.copy()
        return plot

#  Clear Functions 
        
    def clear_subplots(self):
        self.subplots()

    def clear_figure(self):
        self.update_size()
        self.clear_subplots()
        self.clear_sizes()
        self.clear_settings()
        self.clear_data()
        return self
    clf = clear_figure


