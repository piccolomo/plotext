from plotext._subplot import subplot_class
from plotext._matrix import matrix_class
from plotext._settings import settings_class
from plotext._signal import signals_class
from plotext._build import build_class
from plotext._date import date_class
from plotext._placement import placement
from plotext._converter import string_converter_class, get_type


class figure_class(subplot_class, settings_class, matrix_class, signals_class, build_class):
    def __init__(self, parent = None, row = None, col = None):
        super(figure_class, self).__init__(parent, row, col)
        settings_class.__init__(self)
        matrix_class.__init__(self, 0, 0, background = 'white')
        signals_class.__init__(self)
        self._create_date_converters()
        self._create_string_converters()

    def _create_date_converters(self):
        self._xdate = [date_class(), date_class()]
        self._ydate = [date_class(), date_class()]

    def _create_string_converters(self):
        self._xstring = [string_converter_class(), string_converter_class()]
        self._ystring = [string_converter_class(), string_converter_class()]

    def _get_xdate_converter(self, xside):
        xside = placement.xside_to_index(xside)
        return self._xdate[xside]
    
    def _get_ydate_converter(self, yside):
        yside = placement.yside_to_index(yside)
        return self._ydate[yside]

    def _get_xstring_converter(self, xside):
        xside = placement.xside_to_index(xside)
        return self._xstring[xside]
    
    def _get_ystring_converter(self, yside):
        yside = placement.yside_to_index(yside)
        return self._ystring[yside]

    def _create_subplot(self, row = None, col = None):
        plot = figure_class(self, row, col)
        plot._copy_settings_from(self)
        plot._signals = self._signals.copy()
        return plot

#  Clear Functions

    def clear_data(self):
        [self._get_xdate_converter(xside).clear() for xside in [1, 2]]
        [self._get_ydate_converter(yside).clear() for yside in [1, 2]]
        [self._get_xstring_converter(xside).clear() for xside in [1, 2]]
        [self._get_ystring_converter(yside).clear() for yside in [1, 2]]
        self._clear_signals()

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

##############################################
###########    Draw Functions    #############
##############################################

    def _draw(self, *args, xside = None, yside = None):
        x, y = normalize_data(*args)
        xstring = get_type(x) == 'string'
        ystring = get_type(y) == 'string'
        xconverter = self._get_xstring_converter(xside)
        yconverter = self._get_ystring_converter(yside)
        x = xconverter.convert(x) if xstring  else x
        y = yconverter.convert(y) if ystring  else y
        self.xticks(*xconverter.get_ticks()) if xstring else None
        self.yticks(*yconverter.get_ticks()) if ystring else None
        super(figure_class, self)._draw(x, y, xside, yside)


# Signal Utilities

def normalize_data(x = None, y = None): # it return properly formatted x and y data lists
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
