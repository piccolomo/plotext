# Source: one step along the dotted path of the documentation container, as the pixel in plotext.doc.pixel.copy(); reaching a name gives the next step, calling it prints the docstring ending there.

class source_class:

    # Start at the given step of the given container, the step being a dotted path, as "plotext.pixel".
    def __init__(self, container, path):
        self._container = container
        self._path = path

    # Reaching a name gives the next step, so that doc.pixel.copy reaches the copy() method of the pixel.
    def __getattr__(self, name):
        return self._container._resolve(self._path + '.' + name)

    # The names documented right after this step, offered when pressing the tab key.
    def __dir__(self):
        return self._container._next_names(self._path)

    def __repr__(self):
        return 'PrettyDocSource(' + self._path + ')'

    # Calling the step prints the docstring of the entry ending there.
    def __call__(self):
        self._container._printer(self._path)()
