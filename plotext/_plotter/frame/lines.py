# Lines: lightweight container of line_signal entries owned by a ruler.

class lines_class:
    def __init__(self):
        self._lines = []

    def clear(self):
        self._lines = []
        return self

    def add(self, line_signal):
        self._lines.append(line_signal)
        return self

    def copy(self):
        out = lines_class()
        out._lines = self._lines.copy()
        return out

    def rescale(self, ruler, bins):
        [l.rescale(ruler, bins) for l in self._lines]
        return self

    def __iter__(self):
        return iter(self._lines)

    def __len__(self):
        return len(self._lines)
