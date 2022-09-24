from plotext._utility.marker import space_marker, marker_codes, hd_marker_codes, plot_marker, marker_factor
from plotext._utility.color import no_color_name, color_sequence, color_code, to_gray_rgb
from plotext._utility.string import only_spaces
from plotext._matrices import subplot_matrices
from plotext._default import subplot_default
from plotext._datetime import datetime_class
from plotext._utility.data import mean
from plotext._utility.image import *
from plotext._utility.data import *
from plotext._utility.plot import *
from plotext._utility.bar import *
from math import floor

datetime = datetime_class() # usefull for datetime plot

##############################################
#########    Subplot Container    ############
##############################################
class subplot_class():
    def __init__(self, row, col):
        self.default = subplot_default()
        self.matrices = subplot_matrices()

        self.row, self.col = row, col # the subplot row and col coordinate in figure
        self.width, self.height = [None, None]
        self.set_size(self.width, self.height) # width x height of this subplot
        self.rowspan, self.colspan = [1, 1]

        self.data_init()
        self.settings_init()

    def set_size(self, width = None, height = None):
        self.width = width if width is None else int(width)
        self.height = height if height is None else int(height)
        self.size = [self.width, self.height]

    def data_init(self): 
        # Variables Set with Draw internal Arguments
        self.xside = [] # which side the x axis should go, for each plot (lower or upper)
        self.yside = [] # which side the y axis should go, for each plot (left or right)

        self.x = [] # list of x coordinates 
        self.y = [] # list of y coordinates
        self.signals = 0 # number of signals to plot

        self.lines = [] # whatever to draw lines between points

        self.marker = [] # list of markers used for each plot
        self.color = [] # list of marker colors used for each plot

        self.fillx = [] # fill data vertically (till x axis)
        self.filly = [] # fill data horizontally (till y axis)

        self.label = [] # subplot list of labels
        
        # bar settings
        self.bars = {} # bar x label: bar coord; uesefull to keep track of all bar plots in case multiple are plotted
        self.bar_labelled = False # if the bar labels are string or numbers
        self.bar_ylim = [None, None] # lim values of bar height
        self.bar_xlim = [None, None] # lim values of bar labels


    def settings_init(self): # plot settings initialization
        # Variables Set with Outside Functions
        self.row
        self.title = None

        self.xlabel = [None, None]
        self.ylabel = [None, None]

        self.xaxes = self.default.xaxes # whatever to show the lower and upper x axis
        self.yaxes = self.default.yaxes # whatever to show the left and right y axis

        self.grid = self.default.grid # whatever to show the horizontal and vertical grid lines

        self.color_sequence = color_sequence # needed as it can be modified
        self.canvas_color = self.default.canvas_color
        self.ticks_color = self.default.ticks_color
        self.axes_color = self.default.axes_color
        
        self.xlim = [[None, None], [None, None]] # the x axis plot limits for lower and upper xside
        self.ylim = [[None, None], [None, None]] # the y axis plot limits for left and right yside
        
        self.xscale = [self.default.xscale[0]] * 2 # the scale on x axis
        self.yscale = [self.default.xscale[0]] * 2

        self.xfrequency = self.default.xfrequency # lower and upper xaxes ticks frequency
        self.yfrequency = self.default.yfrequency # left and right yaxes ticks frequency

        self.xticks = [[], []] # xticks coordinates for both axes
        self.xlabels = [[], []] # xlabels for both axes

        self.yticks = [[], []]
        self.ylabels = [[], []]

        self.vlines = [[], []] # those are user defined extra grid lines, vertical or horizontal
        self.hlines = [[], []]
        
        self.vcolors = [[], []] # their color
        self.hcolors = [[], []]

##############################################
#########    Utility Functions    ############
##############################################

    def xside_to_pos(self, xside = None): # from axis side to position
        xaxis = self.default.xside
        xside = xaxis[0] if xside is None or xside not in xaxis else xside
        pos = self.default.xside.index(xside)
        return pos

    def yside_to_pos(self, yside = None):
        yaxis = self.default.yside
        yside = yaxis[0] if yside is None or yside not in yaxis else yside
        pos = self.default.yside.index(yside)
        return pos

##############################################
#########    Basic Draw Function    ##########
##############################################

    def draw(self, *args, **kwargs):
        self.add_xside(kwargs.get("xside"))
        self.add_yside(kwargs.get("yside"))

        self.add_data(*args)

        self.add_lines(kwargs.get("lines"))

        self.add_markers(kwargs.get("marker"))
        self.add_colors(kwargs.get("color"))

        self.add_fillx(kwargs.get("fillx"))
        self.add_filly(kwargs.get("filly"))

        self.add_label(kwargs.get("label"))

##############################################
###########    Draw Functions    #############
##############################################

    def add_xside(self, xside = None):
        xside = self.default.xside[0] if xside is None or xside not in self.default.xside else xside
        self.xside.append(xside)

    def add_yside(self, yside = None):
        yside = self.default.yside[0] if yside is None or yside not in self.default.yside else yside
        self.yside.append(yside)

    def add_data(self, *args):
        x, y = set_data(*args)
        x, y = remove_non_numerical(x, y)
        self.x.append(x)
        self.y.append(y)
        self.signals += 1

    def add_lines(self, lines):
        lines = self.default.lines if lines is None else bool(lines) 
        self.lines.append(lines)

    def add_markers(self, marker = None):
        l = len(self.x[-1])
        marker = list(marker) if type(marker) == range else marker
        marker = repeat([self.check_marker(el) for el in marker], l) if type(marker) == list else self.check_marker(marker)
        self.marker.append(marker)

    def check_marker(self, marker = None):
        marker = None if marker is None else str(marker)
        marker = marker if marker in marker_codes or marker in hd_marker_codes else marker
        marker = plot_marker if marker is None else marker
        spaces = only_spaces(marker)
        marker = space_marker if spaces else marker
        marker = marker if marker in hd_marker_codes or marker in marker_codes else marker[0]
        return marker

    def add_colors(self, color = None):
        l = len(self.x[-1])
        color = list(color) if type(color) == range else color
        past_colors = no_duplicates(join(self.color))
        color = repeat([self.check_color(el, past_colors) for el in color], l) if type(color) == list else self.check_color(color, past_colors)
        self.color.append(color)

    def check_color(self, color = None, past_colors = []): # past colors are not calcuated here to reduce time for list based colors
        code = color_code(color, 1)
        nocolor = code[0] == 3
        color = None if color is None or nocolor else color
        color = first(self.color_sequence, past_colors) if color is None else color
        return color
        
    def add_fillx(self, fillx = None):
        fillx = self.default.fillx if fillx is None else bool(fillx) 
        self.fillx.append(fillx)

    def add_filly(self, filly = None):
        filly = self.default.filly if filly is None else bool(filly) 
        self.filly.append(filly)

    def add_label(self, label = None):
        spaces = only_spaces(label)
        label = self.default.label if label is None or spaces else str(label).strip() # strip to remove spaces before and after
        self.label.append(label)
        #figure.subplot.label_show.append(default.label_show)

##############################################
##########    Build Functions    #############
##############################################

    def correct_frequency(self):
        self.xfrequency = [self.xfrequency[i] if self.default.xside[i] in self.xside or self.vlines[i] != [] else 0 for i in range(2)]
        self.yfrequency = [self.yfrequency[i] if self.default.yside[i] in self.yside or self.hlines[i] != [] else 0 for i in range(2)]

    def adjust_height(self):
        self.xaxes[0] = False if self.height <= 1 else self.xaxes[0]
        self.xaxes[1] = False if self.height <= 2 else self.xaxes[1]
        self.xfrequency[0] = 0 if self.height <= 3 else self.xfrequency[0]
        self.xfrequency[1] = 0 if self.height <= 4 else self.xfrequency[1]
        self.title = None if self.height <= 5 else self.title
        self.xlabel[1] = None if self.height <= 5 else self.xlabel[1]
        self.xlabel[0] = None if self.height <= 6 else self.xlabel[0]
        self.ylabel = [None, None] if self.height <= 6 else self.ylabel

    def set_scale(self):
        xscale = [self.xscale[0] if self.xside[s] == self.default.xside[0] else self.xscale[1] for s in range(self.signals)]
        yscale = [self.yscale[0] if self.yside[s] == self.default.yside[0] else self.yscale[1] for s in range(self.signals)]
        self.x = [self.x[s] if xscale[s] == self.default.xscale[0] else log(self.x[s]) for s in range(self.signals)]
        self.y = [self.y[s] if yscale[s] == self.default.yscale[0] else log(self.y[s]) for s in range(self.signals)]
        self.xticks = [log(self.xticks[i]) if self.xscale[i] == self.default.xscale[1] and self.xticks[i] != [] else self.xticks[i] for i in range(2)]
        self.yticks = [log(self.yticks[i]) if self.yscale[i] == self.default.yscale[1] and self.yticks[i] != [] else self.yticks[i] for i in range(2)]
        self.xlim = [log(self.xlim[i]) if self.xscale[i] == self.default.xscale[1] and None not in self.xlim[i] else self.xlim[i] for i in range(2)]
        self.ylim = [log(self.ylim[i]) if self.yscale[i] == self.default.yscale[1] and None not in self.ylim[i] else self.ylim[i] for i in range(2)]

    def get_lim(self, data, axis, default_axis, lim_set):
        data = [[data[i] for i in range(len(data)) if axis[i] == s] for s in default_axis]
        data = [join(el) for el in data]
        lim = [get_lim(el) for el in data]
        return [replace(lim_set[s], lim[s]) for s in range(2)]

    def get_xlim(self):
        x = self.x + self.vlines # to include the vertical lines in the limits
        xside = self.xside + self.default.xside
        self.xlim = self.get_lim(x, xside, self.default.xside, self.xlim)

    def get_ylim(self):
        y = self.y + self.hlines # to include the vertical lines in the limits
        yside = self.yside + self.default.yside
        self.ylim = self.get_lim(y, yside, self.default.yside, self.ylim)

    def get_height_canvas(self):
        self.title_width = any([el is not None for el in [self.title, self.xlabel[1]]])
        self.labels_width = any([el is not None for el in [self.xlabel[0], self.ylabel[0], self.ylabel[1]]])
        self.height_canvas = self.height - sum(self.xaxes) - sum(map(bool, self.xfrequency)) - self.labels_width - self.title_width

    def get_yticks(self):
        self.yfrequency = [min(el, self.height_canvas) for el in self.yfrequency]
        self.yticks = [get_ticks(self.ylim[i], self.yfrequency[i]) if self.yticks[i] == [] else self.yticks[i] for i in range(2)]
        self.ylabels = [get_labels(self.yticks[i], self.yscale[i])  if self.ylabels[i] == [] else self.ylabels[i] for i in range(2)]
        self.ylabels = [pad_labels(self.ylabels[i], self.default.yside[i]) for i in range(2)]
        self.ylabels_width = [0 if l == [] else len(l[0]) for l in self.ylabels]

    def get_width_canvas(self):
        self.width_canvas = self.width - sum(self.ylabels_width) - int(self.yaxes[0]) - int(self.yaxes[1])

    def adjust_width(self):
        for i in range(1,-1,-1):
            if self.width_canvas <= 0:
                self.yfrequency[i] = 0
                self.yticks[i] = []
                self.ylabels[i] = []
                self.get_yticks()
                self.get_width_canvas()
        for i in range(1,-1,-1):
            if self.width_canvas <= 0:
                self.yaxes[i] = 0
                self.get_width_canvas()
            
    def get_xticks(self):
        self.xfrequency = [min(el, self.width_canvas) for el in self.xfrequency]
        self.xticks = [get_ticks(self.xlim[i], self.xfrequency[i]) if self.xticks[i] == [] else self.xticks[i] for i in range(2)]
        self.xlabels = [get_labels(self.xticks[i], self.xscale[i]) if self.xlabels[i] == [] else self.xlabels[i] for i in range(2)]
        # self.xlabels = [_utility.get_labels(el) for el in self.xticks]
        self.xlabels_height = [0 if l == [] else 1 for l in self.xlabels]

    def get_relative_ticks(self):
        self.cticks = self._get_relative_ticks(self.xticks, self.xlim, self.width_canvas)
        self.rticks = self._get_relative_ticks(self.yticks, self.ylim, self.height_canvas)

        self.vticks = self._get_relative_ticks(self.vlines, self.xlim, self.width_canvas) #relative ticks for user defined lines
        self.hticks = self._get_relative_ticks(self.hlines, self.ylim, self.height_canvas)

    def _get_relative_ticks(self, ticks, lim, bins):
        ticks = [get_matrix_data(ticks[s], lim[s], bins) for s in range(2)]
        return [list(map(floor, el)) for el in ticks] # here i use floor instead of int because otherwise int(-0.8) = 0 would appear in the plot, which shouldn't: floor(-0.8) = -1 won't appear; for positive numbers int and floor are the same function

    def create_matrices(self):
        self.matrices.create(self.width_canvas, self.height_canvas, space_marker, no_color_name, self.canvas_color)

    def add_grid(self):
        [self.matrices.update_same_elements(*get_line([c, c], [0, self.height_canvas - 1]), "│", self.ticks_color) for c in join(self.cticks) if self.grid[0]]
        [self.matrices.update_same_elements(*get_line([0, self.width_canvas - 1], [r, r]), "─", self.ticks_color) for r in join(self.rticks) if self.grid[1]]
        
    def add_extra_lines(self):
        for s in range(2):
            for i in range(len(self.vticks[s])):
                c = self.vticks[s][i]
                x, y = get_line([c, c], [0, self.height_canvas - 1])
                self.matrices.update_same_elements(x, y, "│", self.vcolors[s][i])
            for i in range(len(self.hticks[s])):
                r = self.hticks[s][i]
                x, y = get_line([0, self.width_canvas - 1], [r, r])
                self.matrices.update_same_elements(x, y, "─", self.hcolors[s][i])

    def update_matrix(self):
        xlim = [self.xlim[0] if self.xside[s] == self.default.xside[0] else self.xlim[1] for s in range(self.signals)]
        ylim = [self.ylim[0] if self.yside[s] == self.default.yside[0] else self.ylim[1] for s in range(self.signals)]

        xfactor = [marker_factor(self.marker[s], 2, 2) for s in range(self.signals)]
        yfactor = [marker_factor(self.marker[s], 2, 3) for s in range(self.signals)]
        
        x = [get_matrix_data(self.x[s], xlim[s], self.width_canvas * xfactor[s]) for s in range(self.signals)]
        y = [get_matrix_data(self.y[s], ylim[s], self.height_canvas * yfactor[s]) for s in range(self.signals)]

        m = [self.marker[s] if type(self.marker[s]) == list else [self.marker[s]] * len(self.x[s]) for s in range(self.signals)]
        c = [self.color[s] if type(self.color[s]) == list else [self.color[s]] * len(self.x[s]) for s in range(self.signals)]
        
        xymc = [get_lines(x[s], y[s], m[s], c[s]) if self.lines[s] else [x[s], y[s], m[s], c[s]] for s in range(self.signals)]
        empty = [[]] * self.signals
        x, y, m, c =  (empty, empty, empty, empty) if xymc == [] else transpose(xymc)

        y0 = [get_matrix_data([0], ylim[s], self.height_canvas * yfactor[s])[0] for s in range(self.signals)]
        y0 = [max(0, el) for el in y0]
        x0 = [get_matrix_data([0], xlim[s], self.width_canvas * xfactor[s])[0] for s in range(self.signals)]
        x0 = [max(0, el) for el in x0]
        xymc = [fill_data(x[s], y[s], y0[s], m[s], c[s]) if self.fillx[s] else [x[s], y[s], m[s], c[s]] for s in range(self.signals)]
        yxmc = [fill_data(y[s], x[s], x0[s], m[s], c[s]) if self.filly[s] else [y[s], x[s], m[s], c[s]] for s in range(self.signals)]
        x1, y1, m1, c1 =  (empty, empty, empty, empty) if xymc == [] else transpose(xymc)
        y2, x2, m2, c2 =  (empty, empty, empty, empty) if yxmc == [] else transpose(yxmc)
        sub_join = lambda data1, data2: [data1[i] + data2[i] for i in range(len(data1))]
        x, y, m, c = sub_join(x1, x2), sub_join(y1, y2), sub_join(m1, m2), sub_join(c1, c2)
        
        xy = [remove_outsiders(x[s], y[s], self.width_canvas * xfactor[s], self.height_canvas * yfactor[s]) for s in range(self.signals)]
        x, y = (empty, empty) if xy == [] else transpose(xy)
        
        x = [correct_data(x[s], xfactor[s]) for s in range(self.signals)]
        y = [correct_data(y[s], yfactor[s]) for s in range(self.signals)]

        xy = [brush(x[s], y[s]) for s in range(self.signals)]

        empty = [[]] * self.signals
        x, y = (empty, empty) if xy == [] else transpose(xy)

        [self.matrices.update_different_elements(x[s], y[s], m[s], c[s]) for s in range(self.signals) if m[s] != space_marker]

    def add_legend(self):
        sides = get_side_symbols(self.xside, self.yside)
        marker, color, label = get_legend(self.label, self.marker, self.color)
        m = 0 if marker == [] else len(marker[0])
        l = 0 if label == [] else len(label[0])

        if self.width_canvas < l + m or l == 0:
            return

        [self.matrices.insert(i, 0, marker[i], color[i]) for i in range(len(marker))]

        c = [[self.ticks_color] * len(label[i])  for i in range(len(label))]
        [self.matrices.insert(i, m, label[i], c[i]) for i in range(len(label))]

        c = [[self.ticks_color] * len(sides[i])  for i in range(len(label))]
        [self.matrices.insert(i, m + l - 1, sides[i], c[i]) for i in range(len(label))]

        mr = ' ' * (l + m)
        c = [self.ticks_color] * (l + m)
        self.matrices.insert(len(label), 0, mr, c)

    def add_yaxis(self):
        axis = ['│' * self.height_canvas for i in range(2)]
        primary_tick = ['┼' if self.grid[1] else ('┤' if i == 0 else '├') for i in range(2)]
        axis = [update_axis(axis[i], self.rticks[i], primary_tick[i]) for i in range(2)]
        secondary_tick = [('├'  if i == 0 else '┤') if self.grid[1] else None for i in range(2)]
        axis = [update_axis(axis[i], self.rticks[i - 1], secondary_tick[i]) for i in range(2)]
        hline_tick = [('├'  if i == 0 else '┤') for i in range(2)]
        axis = [update_axis(axis[i], join(self.hticks), hline_tick[i]) for i in range(2)]

        axis = [transpose([list(el)[::-1]]) for el in axis]
        [self.matrices.pad(self.default.yside[i], axis[i], self.ticks_color, self.axes_color) for i in range(2) if self.yaxes[i]]

        ticks = [get_yticks(self.height_canvas, self.ylabels[i], self.rticks[i]) for i in range(2)]
        [self.matrices.pad(self.default.yside[i], ticks[i], self.ticks_color, self.axes_color) for i in range(2) if self.yfrequency[i]]

    def add_xaxis(self):
        ticks = [get_xticks(self.width_canvas, self.xlabels[i], self.cticks[i]) for i in range(2)] # numerical ticks
        ticks, cticks = transpose(ticks)
        
        pad_stop = [len(self.xlabels[i]) > 0 for i in range(2)] # spaces before and after numerical ticks
        pad_length = [(self.ylabels_width[i] + self.yaxes[i]) for i in range(2)]
        ticks = [pad_list(ticks[i], "left", space_marker, pad_length[0] * pad_stop[i]) for i in range(2)]
        ticks = [pad_list(ticks[i], "right", space_marker, pad_length[1] * pad_stop[i]) for i in range(2)]
        
        axis = ['─' * self.width_canvas for i in range(2)]
        primary_tick = ['┼' if self.grid[0] else ('┬' if i == 0 else '┴') for i in range(2)]
        axis = [update_axis(axis[i], cticks[i], primary_tick[i]) for i in range(2)]
        secondary_tick = [('┴'  if i == 0 else '┬') if self.grid[0] else None for i in range(2)]
        axis = [update_axis(axis[i], cticks[i - 1], secondary_tick[i]) for i in range(2)]
        vline_tick = [('┴'  if i == 0 else '┬') for i in range(2)]
        axis = [update_axis(axis[i], join(self.vticks), vline_tick[i]) for i in range(2)]
        axis = [list(el) for el in axis]
        axis = [pad_list(axis[i], "left", '└' if i == 0 else '┌', self.yaxes[0]) for i in range(2)]
        axis = [pad_list(axis[i], "right", '┘' if i == 0 else '┐', self.yaxes[1]) for i in range(2)]
        axis = [pad_list(axis[i], "left", space_marker, self.ylabels_width[0]) for i in range(2)]
        axis = [pad_list(axis[i], "right", space_marker, self.ylabels_width[1]) for i in range(2)]
        axis = [[el] for el in axis]
        
        [self.matrices.pad(self.default.xside[i], axis[i], self.ticks_color, self.axes_color) for i in range(2) if self.xaxes[i]]
        [self.matrices.pad(self.default.xside[i], [ticks[i]], self.ticks_color, self.axes_color) for i in range(2) if ticks[i] != []]

    def add_labels(self):
        lower, upper = get_plot_labels(self.xlabel, self.ylabel, self.title, self.width, self.width_canvas, self.ylabels_width)
        if self.labels_width:
            self.matrices.pad(self.default.xside[0], [lower], self.ticks_color, self.axes_color)
        if self.title_width:
            self.matrices.pad(self.default.xside[1], [upper], self.ticks_color, self.axes_color)
        
##############################################
######    Other Plotting Functions    ########
##############################################

    def draw_date(self, t, y, **kwargs):
        t, y = set_data(t, y)
        x = list(map(datetime.string_to_timestamp, t))
        self.draw(x, y, **kwargs)
        pos = self.xside_to_pos(self.xside[-1])
        self.xticks[pos] = x
        self.xlabels[pos] = datetime._strings_to_xlabels(t)

    def get_bar_parameters(self, **kwargs):
        xside = kwargs.get("xside")
        yside = kwargs.get("yside")
        marker = kwargs.get("marker")
        color = kwargs.get("color")
        fill = kwargs.get("fill")
        width = kwargs.get("width")
        orientation = kwargs.get("orientation")
        label = kwargs.get("label")
        minimum = kwargs.get("minimum")
        offset = kwargs.get("offset")
        return xside, yside, marker, color, fill, width, orientation, label, minimum, offset
        
    def draw_single_bar(self, x, y, **kwargs):
        x, y = set_data(x, y)
        xside, yside, marker, color, fill, width, orientation, label, minimum, offset = self.get_bar_parameters(**kwargs)
        
        marker = self.default.bar_marker if marker is None else marker
        fill = self.default.bar_fill if fill is None else fill
        width = self.default.bar_width if width is None else width
        width = 1 if width > 1 else 0 if width < 0 else width
        orientation = self.default.bar_orientation[0] if orientation is None or orientation not in self.default.bar_orientation else orientation
        offset = 0 if offset is None else offset

        xpos = self.xside_to_pos(xside)
        ypos = self.xside_to_pos(yside)

        x, xlabels, labelled, self.bars = update_bars(x, self.bars, offset)
        xticks = x
        x = [el + offset for el in x]
        self.bar_labelled = any([labelled, self.bar_labelled])
        self.bar_ylim = update_bar_ylim(self.bar_ylim + y + [minimum])
        xbar, ybar = bars(x, y, width, self.bar_ylim[0])
    
        if orientation in ['vertical', 'v']:
             fillx, filly = fill, False
             if self.bar_labelled:
                 self.xticks[xpos] = self.xticks[xpos] + xticks
                 self.xlabels[xpos] = self.xlabels[xpos] + xlabels
             self.ylim[ypos] = self.bar_ylim
             self.bar_xlim = update_bar_xlim(self.bar_xlim + self.xlim[xpos] + xticks + join(xbar))
             self.xlim[xpos] = self.bar_xlim
            
        elif orientation in ['horizontal', 'h']:
            xbar, ybar = ybar, xbar
            fillx, filly = False, fill
            if self.bar_labelled:
                self.yticks[ypos] = self.yticks[ypos] + xticks
                self.ylabels[ypos] = self.ylabels[ypos] + xlabels
            self.xlim[xpos] = self.bar_ylim
            self.bar_xlim = update_bar_xlim(self.bar_xlim + self.ylim[ypos] + xticks + join(ybar))
            self.ylim[ypos] = self.bar_xlim

        firstbar = min([b for b in range(len(x)) if ybar[b][1] != 0], default = 0) # finds the position of the first non zero bar
            
        for b in range(len(x)):
            xb = xbar[b][1:3] if fill else xbar[b]
            yb = ybar[b][1:3] if fill else ybar[b]
            plot_label = label if b == firstbar else None
            plot_color = color if b == 0 else self.color[-1]
            nobar = (yb[1] == 0 and orientation[0] == 'v') or (xb[1] == 0 and orientation[0] == 'h')
            plot_marker = " " if nobar else marker
            self.draw(xb, yb,
                 xside = xside, 
                 yside = yside,
                 lines = True,
                 marker = plot_marker,
                 color = plot_color,
                 fillx = fillx,
                 filly = filly,
                 label = plot_label)

    def draw_multiple_bar(self, x, y, **kwargs):
        xside, yside, marker, color, fill, width, orientation, label, minimum, offset = self.get_bar_parameters(**kwargs)
        ly = len(y)

        width = self.default.bar_width if width is None else width
        marker = [marker] * ly if marker is None or type(marker) != list else marker
        color = [color] * ly if color is None else color
        label = [label] * ly if label is None else label
        width = width / ly if ly != 0 else 0
        offset = linspace(-1 / 2 + 1 / (2 * ly), 1 / 2 - 1 / (2 * ly), ly) if ly!= 0 else []
        
        for i in range(ly):
            self.draw_single_bar(x, y[i],
                xside = xside,
                yside = yside,
                marker = marker[i],
                color = color[i],
                fill = fill,
                width = width,
                orientation = orientation,
                label = label[i],
                minimum = minimum,
                offset = offset[i])

    def draw_stacked_bar(self, x, y, **kwargs):
        xside, yside, marker, color, fill, width, orientation, label, minimum, offset = self.get_bar_parameters(**kwargs)
        ly = len(y)
        marker = [marker] * ly if marker is None or type(marker) != list else marker
        color = [color] * ly if color is None else color
        label = [label] * ly if label is None else label

        y = transpose([cumsum(el) for el in transpose(y)])
        for i in range(ly - 1, -1, -1):
            self.draw_single_bar(x, y[i],
                xside = xside, 
                yside = yside,
                marker = marker[i],
                color = color[i],
                fill = fill,
                width = width,
                orientation = orientation,
                label = label[i],
                minimum = minimum)

    def draw_hist(self, data, **kwargs):
        bins = kwargs.get("bins")
        bins = self.default.hist_bins if bins is None else bins
        norm = kwargs.get("norm", False)
        x, y = hist_data(data, bins, norm)
        self.draw_single_bar(x, y, **kwargs)

    def draw_matrix(self, matrix, **kwargs):
        matrix = [l.copy() for l in matrix]
        xside = kwargs.get("xside")
        yside = kwargs.get("yside")
        xpos = self.xside_to_pos(xside)
        ypos = self.xside_to_pos(yside)
        marker = kwargs.get("marker")
        marker = [marker] if type(marker) != list else marker
        marker = ["sd" if el in [None, "hd", "fhd"] else self.check_marker(el) for el in marker]
        
        rgb_test = lambda data: (type(data) == tuple or type(data) == list) and len(data) == 3
        
        rows, cols = 0 if matrix == [] else len(matrix), 0 if matrix == [] else len(matrix[0])
        matrix = matrix if rows * cols != 0 and rgb_test(matrix[0][0]) else to_gray_rgb(matrix)

        for r in range(rows):
            xyc = [(c, r, matrix[rows - 1 - r][c]) for c in range(cols)]
            x, y, color = transpose(xyc)
            # here i did not call self.draw() because the function add_colors is quite slow
            self.add_xside(xside)
            self.add_yside(yside)
            self.add_data(x, y)
            self.add_lines(False)
            self.marker.append(repeat(marker, cols))
            self.color.append(color)
            self.add_fillx(False)
            self.add_filly(False)
            self.add_label(None)

        #self.canvas_color = no_color_name
        #self.axes_color = no_color_name
        #self.ticks_color = no_color_name
        xticks, yticks = list(range(cols)), list(range(rows))
        xlabels, ylabels = list(map(str, range(1, cols + 1))), list(map(str, range(rows, 0 ,-1)))
        
        self.xticks[xpos] = xticks
        self.xlabels[xpos] = xlabels
        self.yticks[ypos] = yticks
        self.ylabels[ypos] = ylabels
        self.xfrequency[xpos] = len(xticks)
        self.yfrequency[ypos] = len(yticks)
        
        self.xlabel[xpos] = "column"
        self.ylabel[ypos] = "row"

    def draw_image(self, path, size = [None, None], marker = None, grayscale = False, keep_ratio = False, resample = True):
        from PIL import Image, ImageOps

        image = Image.open(path)
        image = ImageOps.grayscale(image) if grayscale else image
        image = image.convert('RGB')
        image = resize_image(image, size, keep_ratio, resample)
        size = image.size
        matrix = image_to_matrix(image)
        self.draw_matrix(matrix, marker = marker)
        
        self.canvas_color = no_color_name
        self.xticks = [[], []]
        self.xlabels = [[], []]
        self.xfrequency = [0, 0]
        self.yticks = [[], []]
        self.ylabels = [[], []]
        self.yfrequency = [0, 0]

        self.xlabel = [None, None]
        self.ylabel = [None, None]

        return size

    def draw_vertical_line(self, coordinate, xside = None, color = None):
        coordinate = datetime.string_to_timestamp(coordinate) if type(coordinate) == str else coordinate
        pos = self.xside_to_pos(xside)
        self.vlines[pos].append(coordinate)
        color = self.ticks_color if color is None else color
        self.vcolors[pos].append(self.check_color(color))
        
    def draw_horizontal_line(self, coordinate, yside = None, color = None):
        coordinate = datetime.string_to_timestamp(coordinate) if type(coordinate) == str else coordinate
        pos = self.xside_to_pos(yside)
        self.hlines[pos].append(coordinate)
        color = self.ticks_color if color is None else color
        self.hcolors[pos].append(self.check_color(color))
