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

    def build_matrix(self):
        self.matrix = matrix_class(self.width, self.height)
