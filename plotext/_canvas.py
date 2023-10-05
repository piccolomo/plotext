from plotext._default import default_canvas_color
from plotext._color import is_color
from plotext._matrix import matrix_class

class canvas_class():
    def __init__(self):
        self.set_canvas_color()
        
    def set_canvas_color(self, color = None):
        color = color if is_color(color) else None
        self.color = default_canvas_color if color is None else color

    def set_size(self, width = None, height = None):
        self.width = int(width) if width is not None else width
        self.height = int(height) if height is not None else height

    def update_matrix(self):
        self.matrix = matrix_class(self.width, self.height)

    def clear(self):
        self.__init__()


def round8(data):
    return [round(el, 8) for el in data]

def digitize(data, lim, bins):
    change = lambda el: 0.5 + (bins - 1) * (el - lim[0]) / (lim[1] - lim[0])
    return [change(el) for el in round8(data)]

