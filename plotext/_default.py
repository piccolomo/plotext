from plotext._utility.marker import bar_marker

class figure_default(): # storing default values for figure class
    def __init__(self):
        self.terminal_size = [200, 50] # the terminal size if no size is detected
        self.terminal_infinite_size = [10 ** 10, 10 ** 10] # the maximum size allowed if force_size (basically infinity)
        self.limit_size = [True, True]
        self.cols_max = 10 # max number of subplots columns and rows
        self.rows_max = 10

class subplot_default(): # storing default values for subplot class
    def __init__(self):
        # Default Values for Variables Set with Draw internal Arguments
        
        self.xside = ["lower", "upper"] # the two possibilities, the first is default
        self.yside = ["left", "right"] # the two possibilities, the first is default

        self.lines = False

        self.fillx = False
        self.filly = False

        self.label = None 
        #self.label_show = True

        # Default Values for Variables Set with Outside Functions
        
        self.xaxes = [True, True]
        self.yaxes = [True, True]

        self.grid = [False, False]

        self.canvas_color = "bright-white"
        self.ticks_color = "black"
        self.axes_color = "bright-white"

        self.xscale = ["linear", "log"] # the two possibilities, the first is default
        self.yscale = ["linear", "log"]

        self.xfrequency = [5, 5] # lower and upper xaxes ticks frequency
        self.yfrequency = [7, 7] # left and right yaxes ticks frequency

        self.xticks = [[], []] # xticks coordinates for both axes
        self.yticks = [[], []]

        self.alignment = ["left", "center", "right"] # the three text alignments possibilities, the first is default

        # bar plot defaults
        self.bar_width = 4 / 5 # bar width
        self.bar_orientation = ['vertical', 'v', 'horizontal', 'h'] # the two possible orientations, the first is the default: v = vertical, h = horizontal
        self.bar_fill = True # bar plot filled or not
        self.bar_marker = bar_marker
        
        # hist plot defaults
        self.hist_bins = 10

