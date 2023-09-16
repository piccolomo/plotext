from plotext._default import default_canvas
import plotext._utility as ut

class canvas_class():
    def __init__(self):
        self.set_canvas_color()
        self.marker = []
        
    def set_canvas_color(self, color = None):
        color = color if ut.is_color(color) else None
        self.canvas_color = default_canvas.color if color is None else color

##############################################
#######    Draw() Called Functions    ########
##############################################

    def add_marker(self, marker):
        self.marker.append(marker)
        
    def add_color(self, color):
        self.color.append(color)

    def add_lines(self, lines):
        lines = self.default.lines if lines is None else bool(lines)
        self.lines.append(lines)


        
