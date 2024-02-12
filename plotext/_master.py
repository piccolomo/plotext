from plotext._figure import figure_class
from plotext._default import default_master


class master_class(figure_class):
    def __init__(self, terminal = None):
        self.limit_size()
        self.interactive()
        figure_class.__init__(self, parent = terminal)
        self._set_active()

    def limit_size(self, width = None, height = None):
        self._limit_width = default_master.limit_width if width is None else bool(width)
        self._limit_height = default_master.limit_height if height is None else bool(height)
        self._limit = [self._limit_width, self._limit_height]
        return self

    def _set_size(self, width = None, height = None):
        self._width = self._parent._width if width is None else max(0, min(width, self._parent._width)) if self._limit_width else max(0, width)
        self._height = self._parent._height if height is None else max(0, min(height, self._parent._height)) if self._limit_width else max(0, height)
        self._size = self._width, self._height

    def _update_size(self):
        self._get_terminal().update_size()
        self._set_size()

    def clear_figure(self):
        self._update_size()
        super().clear_figure()
        

    def interactive(self, interactive = None):
        self._interactive = default_master.interactive if interactive is None else bool(interactive)
        return self

    def _set_active(self, subplot = None):
        self._active = subplot if subplot is not None else self

    def _get_active(self, subplot = None):
         return self._active

    def __repr__(self):
        return self._parent.__repr__() + '.main()'
