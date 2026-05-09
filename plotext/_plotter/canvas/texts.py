# Texts container: holds user-registered text drawables and renders them onto the canvas region.


class texts_class:
    def __init__(self):
        self._texts = []

    def clear(self):
        self._texts = []
        return self

    def add(self, text):
        self._texts.append(text)
        return self

    def __iter__(self):
        return iter(self._texts)

    def __len__(self):
        return len(self._texts)

    # Render every text onto the canvas region of matrix; per-text x/y rulers looked up via irulers using the text's xside/yside.
    def draw(self, matrix, irulers, canvas_part):
        for t in self:
            xruler = irulers._get(0, t._get_xside())
            yruler = irulers._get(1, t._get_yside())
            t.draw(matrix, xruler, yruler, canvas_part)
        return self
