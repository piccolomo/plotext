#from plotext._utility import bar_marker
from plotext._utility import no_color, plot_marker

class default_figure_class():
    
    def __init__(self):
        self.set_limitsize()
        self.set_size_term()
        self.set_size_term_inf()
        self.interactive = False

    def set_limitsize(self, limit_width = None, limit_height = None):
        self.limit_width = True if limit_width is None else bool(limit_width)
        self.limit_height = True if limit_height is None else bool(limit_height)
        self.limit_size = [self.limit_width, self.limit_height]

    def set_size_term(self, width = None, height = None):
        self.width_term = 211 * 2 // 3 if width is None else int(width)
        self.height_term = 53 * 2 // 3 if height is None else int(height)
        self.size_term = [self.width_term, self.height_term]

    def set_size_term_inf(self, width = None, height = None):
        m = 5
        self.width_term_inf = m * self.width_term if width is None else int(width)
        self.height_term_inf = m * self.height_term if height is None else int(height)
        self.size_term_inf = [self.width_term, self.height_term]

        
class default_monitor_class():
    
    def __init__(self):
        self.marker = plot_marker
        self.color_init()
        self.axes_init()
        self.canvas_init()
        self.text_init()
        self.draw_init()
        self.bar_init()
        self.confusion_matrix_init()

    def color_init(self): # Default Values for Color Set with Outside Functions
        self.canvas_color = "white"
        self.axes_color = "white"
        self.ticks_color = "black"
        self.ticks_style = no_color

    def axes_init(self):  # Default Values for Variables Set with Outside Functions
        self.xaxes = [True, True]
        self.yaxes = [True, True]
        self.xfrequency = [5, 5] # lower and upper xaxes ticks frequency
        self.yfrequency = [7, 7] # left and right yaxes ticks frequency
        self.xdirection = [1, 1] # direction of x axes
        self.ydirection = [1, 1]
        self.xticks = [None, None] # xticks coordinates for both axes
        self.yticks = [None, None]

    def canvas_init(self):
        self.xscale = ["linear", "log"] # the two possibilities, the first is default
        self.yscale = ["linear", "log"]
        self.grid = [False, False]
    
    def text_init(self):
        self.alignment = ['left', 'center', 'right', 'top', 'bottom', 'dynamic']
        self.orientation = ['horizontal', 'vertical'] # the two possible orientations, the first is the default: v = vertical, h = horizontal
        
    def draw_init(self): # Default Values for Variables Set with Draw internal Arguments
        self.xside = ["lower", "upper"] # the two possibilities, the first is default
        self.yside = ["left", "right"] # the two possibilities, the first is default
        self.lines = False
        self.fill = False
        self.fill_internal = "internal"
        #self.filly = False
        self.label = None

    def bar_init(self):
        self.bar_marker = "sd"
        self.bar_fill = True # bar plot filled or not
        self.bar_width = 4 / 5 # bar width
        self.hist_bins = 10

    def confusion_matrix_init(self):
        self.cmatrix_color = 'orange+'
        self.cmatrix_style = 'bold'
