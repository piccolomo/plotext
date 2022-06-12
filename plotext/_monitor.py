from plotext._default import default_monitor_class
from plotext._date import date_class
import plotext._utility as ut
import math
from copy import deepcopy

class monitor_class():
    def __init__(self):
        self.default = default_monitor_class() # default values
        self.date = date_class() # datetime class for date object manipulation
        self.labels_init() 
        self.axes_init()
        self.color_init()
        self.data_init()
        self.matrix_init()
        self.size = [None, None] # the figure size of which monitor comes from (it will be passed externally, from figure._set_size)

    def copy(self): # to copy 
        return deepcopy(self)

##############################################
#########    Internal Variables    ###########
##############################################

    def labels_init(self):
        self.title = None
        self.xlabel = [None, None]
        self.ylabel = [None, None]

    def axes_init(self):
        self.xscale = [self.default.xscale[0]] * 2 # the scale on x axis
        self.yscale = [self.default.xscale[0]] * 2

        self.xticks = self.default.xticks # xticks coordinates for both axes
        self.xlabels = self.default.xticks[:] # xlabels for both axes
        self.xfrequency = self.default.xfrequency # lower and upper xaxes ticks frequency
        
        self.yticks = self.default.yticks
        self.ylabels = self.default.yticks[:]
        self.yfrequency = self.default.yfrequency # left and right yaxes ticks frequency

        self.xaxes = self.default.xaxes # whatever to show the lower and upper x axis
        self.yaxes = self.default.yaxes # whatever to show the left and right y axis

        self.grid = self.default.grid # whatever to show the horizontal and vertical grid lines

    def color_init(self):
        self.set_theme('default')

    def data_init(self):
        self.xlim = [[None, None], [None, None]] # the x axis plot limits for lower and upper xside
        self.ylim = [[None, None], [None, None]] # the y axis plot limits for left and right yside

        self.fast_plot = False
        self.lines_init()
        self.text_init()
        self.draw_init()
        self.bar_init()

    def lines_init(self):
        self.vlines = [[], []] # those are user defined extra grid lines, vertical or horizontal, for each axis
        self.hlines = [[], []]
        
        self.vcolors = [[], []] # their color
        self.hcolors = [[], []]

    def text_init(self):
        self.text = []
        self.tx = []
        self.ty = []
        self.txside = []
        self.tyside = []
        self.talign = []
        self.tcolor = []
        self.tstyle = []

    def draw_init(self):  # Variables Set with Draw internal Arguments
        self.xside = [] # which side the x axis should go, for each plot (lower or upper)
        self.yside = [] # which side the y axis should go, for each plot (left or right)
        
        self.x = [] # list of x coordinates 
        self.y = [] # list of y coordinates
        self.x_date = [False, False] # True if x axis is for date time plots
        self.y_date = [False, False]
        self.signals = 0 # number of signals to plot

        self.lines = [] # whatever to draw lines between points

        self.marker = [] # list of markers used for each plot
        self.color = [] # list of marker colors used for each plot
        self.past_colors = []
        self.style = []

        self.fillx = [] # fill data vertically (till x axis)
        self.filly = [] # fill data horizontally (till y axis)

        self.label = [] # subplot list of labels

    def bar_init(self):
        self.bar_labels = [] # the list of bar labels
        self.bar_coords = [] # the list of bar coordinates
        self.bar_labelled = False # if the bar labels are string or numbers
        self.bar_ylim = [None, None] # lim values of bar height
        self.bar_xlim = [None, None] # lim values of bar labels
    
    def matrix_init(self):
        self.matrix = [[]]
        self.canvas = ''

##############################################
###########    Set Functions    ##############
##############################################

    def set_title(self, title = None):
        self.title = self.set_label(title)

    def set_xlabel(self, label = None, xside = None):
        pos = self.xside_to_pos(xside)
        self.xlabel[pos] = self.set_label(label)
        
    def set_ylabel(self, label = None, yside = None):
        pos = self.yside_to_pos(yside)
        self.ylabel[pos] = self.set_label(label)
        
    def set_xlim(self, lower = None, upper = None, xside = None):
        lower = None if lower is None else float(lower)
        upper = None if upper is None else float(upper)
        xlim = [lower, upper]
        xlim = xlim if xlim == [None] * 2 else [min(xlim), max(xlim)]
        pos = self.xside_to_pos(xside)
        self.xlim[pos] = xlim

    def set_ylim(self, left = None, right = None, yside = None):
        left = None if left is None else float(left)
        right = None if right is None else float(right)
        ylim = [left, right]
        ylim = ylim if ylim == [None] * 2 else [min(ylim), max(ylim)]
        pos = self.yside_to_pos(yside)
        self.ylim[pos] = ylim

    def set_xscale(self, scale = None, xside = None):
        default_case = (scale is None or scale not in self.default.xscale)
        scale = self.default.xscale[0] if default_case else scale
        pos = self.xside_to_pos(xside)
        self.xscale[pos] = scale

    def set_yscale(self, scale = None, yside = None):
        default_case = (scale is None or scale not in self.default.yscale)
        scale = self.default.yscale[0] if default_case else scale
        pos = self.yside_to_pos(yside)
        self.yscale[pos] = scale

    def set_xticks(self, ticks = None, labels = None, xside = None):
        pos = self.xside_to_pos(xside)
        ticks = self.default.xticks[pos] if ticks is None else list(ticks)
        string_ticks = any([isinstance(el, str) for el in ticks])
        labels = ticks if string_ticks and labels is None else labels
        ticks = self.date.strings_to_time(ticks) if string_ticks else ticks
        labels = ticks if labels is None else list(labels)
        labels = list(map(str, labels))
        ticks, labels = ut.brush(ticks, labels)
        self.xticks[pos] = ticks
        self.xlabels[pos] = labels
        self.xfrequency[pos] = self.xfrequency[pos] if ticks is None else len(ticks)

    def set_yticks(self, ticks = None, labels = None, yside = None):
        pos = self.yside_to_pos(yside)
        ticks = self.default.yticks[pos] if ticks is None else list(ticks)
        string_ticks = any([isinstance(el, str) for el in ticks])
        labels = ticks if string_ticks and labels is None else labels
        ticks = self.date.strings_to_time(ticks) if string_ticks else ticks
        labels = ticks if labels is None else list(labels)
        labels = list(map(str, labels))
        ticks, labels = ut.brush(ticks, labels)
        self.yticks[pos] = ticks
        self.ylabels[pos] = labels
        self.yfrequency[pos] = self.yfrequency[pos] if ticks is None else len(ticks)

    def set_xfrequency(self, frequency = None, xside = None):
        pos = self.xside_to_pos(xside)
        frequency = self.default.xfrequency[pos] if frequency is None else int(frequency)
        self.xfrequency[pos] = frequency
        
    def set_yfrequency(self, frequency = None, yside = None):
        pos = self.yside_to_pos(yside)
        frequency = self.default.yfrequency[pos] if frequency is None else int(frequency)
        self.yfrequency[pos] = frequency
        
    def set_xaxes(self, lower = None, upper = None):
        self.xaxes[0] = self.default.xaxes[0] if lower is None else bool(lower)
        self.xaxes[1] = self.default.xaxes[1] if upper is None else bool(upper)
        
    def set_yaxes(self, left = None, right = None):
        self.yaxes[0] = self.default.yaxes[0] if left is None else bool(left)
        self.yaxes[1] = self.default.yaxes[1] if right is None else bool(right)

    def set_frame(self, frame = None):
        self.set_xaxes(frame, frame)
        self.set_yaxes(frame, frame)

    def set_grid(self, horizontal = None, vertical = None):
        horizontal = self.default.grid[0] if horizontal is None else bool(horizontal)
        vertical = self.default.grid[1] if vertical is None else bool(vertical)
        self.grid = [horizontal, vertical]

    def set_color(self, color = None):
        color = color if ut.is_color(color) else None
        return self.default.canvas_color if color is None else color

    def set_canvas_color(self, color = None):
        self.canvas_color = self.set_color(color)
        
    def set_axes_color(self, color = None):
        self.axes_color = self.set_color(color)
        
    def set_ticks_color(self, color = None):
        self.ticks_color = self.set_color(color)

    def set_ticks_style(self, style = None):
        style = style if ut.is_style(style) else None
        style = self.default.ticks_style if style is None else ut.clean_styles(style)
        self.ticks_style = style

    def set_theme(self, theme = None):
        theme = 'default' if theme is None or theme not in ut.themes else theme
        self._set_theme(*ut.themes[theme])

    def clear_color(self):
        self.set_theme('clear')

##############################################
#######    Set Functions Utilities    ########
##############################################

    def set_label(self, label = None):
        label = None if label is None else str(label).strip()
        spaces = ut.only_spaces(label)
        label = None if spaces else label 
        return label

    def correct_xside(self, xside = None): # from axis side to position
        xaxis = self.default.xside
        xside = xaxis[xside - 1] if isinstance(xside, int) and 1 <= xside <= 2 else xaxis[0] if xside is None or xside.strip() not in xaxis else xside.strip()
        return xside

    def correct_yside(self, yside = None):
        yaxis = self.default.yside
        yside = yaxis[yside - 1] if isinstance(yside, int) and 1 <= yside <= 2 else yaxis[0] if yside is None or yside.strip() not in yaxis else yside.strip()
        return yside

    def xside_to_pos(self, xside = None): # from axis side to position
        xside = self.correct_xside(xside)
        pos = self.default.xside.index(xside)
        return pos

    def yside_to_pos(self, yside = None):
        yside = self.correct_yside(yside)
        pos = self.default.yside.index(yside)
        return pos

    def _set_theme(self, canvas_color, axes_color, ticks_color, ticks_style, color_sequence):
        self.canvas_color = canvas_color
        self.axes_color = axes_color
        self.ticks_color = ticks_color
        self.ticks_style = ticks_style
        self.color_sequence = color_sequence

##############################################
##########    Draw() Functions    ############
##############################################

    def add_xside(self, xside = None):
        xside = self.correct_xside(xside)
        self.xside.append(xside)

    def add_yside(self, yside = None):
        yside = self.correct_yside(yside)
        self.yside.append(yside)

    def add_data(self, *args):
        x, y = set_data(*args)
        x, x_date = self.to_time(x)
        y, y_date = self.to_time(y)
        self.x_date[self.xside_to_pos(self.xside[-1])] = x_date
        self.y_date[self.yside_to_pos(self.yside[-1])] = y_date
        x, y = remove_non_numerical(x, y)
        self.x.append(x)
        self.y.append(y)
        self.signals += 1

    def add_lines(self, lines):
        lines = self.default.lines if lines is None else bool(lines) 
        self.lines.append(lines)
        
    def add_markers(self, marker = None):
        single_marker = isinstance(marker, str) or marker is None
        marker = self.check_marker(marker) if single_marker else list(map(self.check_marker, marker))
        length = len(self.x[-1])
        marker = ut.to_list(marker, length)
        self.marker.append(marker)

    def add_colors(self, color = None):
        list_color = isinstance(color, list) 
        color = list(map(self.check_color, color)) if list_color else self.check_color(color)
        length = len(self.x[-1])
        self.past_colors = self.past_colors + [color] if color not in self.past_colors else self.past_colors
        color = ut.to_list(color, length)
        self.color.append(color)

    def add_styles(self, style = None):
        single_style = isinstance(style, str) or style is None
        style = self.check_style(style) if single_style else list(map(self.check_style, style))
        length = len(self.x[-1])
        style = ut.to_list(style, length)
        self.style.append(style)

    def add_fillx(self, fillx = None):
        fillx = self.default.fillx if fillx is None else bool(fillx) 
        self.fillx.append(fillx)

    def add_filly(self, filly = None):
        filly = self.default.filly if filly is None else bool(filly) 
        self.filly.append(filly)

    def add_label(self, label = None):
        spaces = ut.only_spaces(label)
        label = self.default.label if label is None or spaces else str(label).strip() # strip to remove spaces before and after
        self.label.append(label)
        #figure.subplot.label_show.append(default.label_show)

##############################################
######    Draw() Functions Utilities   #######
##############################################

    def to_time(self, x):
        x_string = any([isinstance(el, str) for el in x])
        x = self.date.strings_to_time(x) if x_string else x
        return x, x_string
    
    def check_marker(self, marker = None):
        marker = None if marker is None else str(marker)
        marker = ut.plot_marker if marker is None else marker
        marker = ut.marker_codes[marker] if marker in ut.marker_codes else marker
        marker = marker if marker in ut.hd_symbols else marker[0]
        return marker

    def check_color(self, color = None):
        color = color if ut.is_color(color) else None
        color = self.next_color() if color is None else color
        return color

    def next_color(self):
        color = ut.difference(self.color_sequence, self.past_colors)
        color = color[0] if len(color) > 0 else self.color_sequence[0]
        return color

    def check_style(self, style):
        style = None if style is None else str(style)
        style = style if ut.is_style(style) else ut.no_color
        return style

##############################################
######    Main Plotting Functions    #########
##############################################

    def draw(self, *args, **kwargs):
        self.add_xside(kwargs.get("xside"))
        self.add_yside(kwargs.get("yside"))
        self.add_data(*args)
        self.add_lines(kwargs.get("lines"))
        self.add_markers(kwargs.get("marker"))
        self.add_colors(kwargs.get("color"))
        self.add_styles(kwargs.get("style"))
        self.add_fillx(kwargs.get("fillx"))
        self.add_filly(kwargs.get("filly"))
        self.add_label(kwargs.get("label"))

    def draw_error(self, *args, xerr = None, yerr = None, xside = None, yside = None, marker = None, color = None, label = None):
        x, y = set_data(*args)
        x, y = remove_non_numerical(x, y)
        l = len(x)
        xerr = [0] * l if xerr is None else xerr
        yerr = [0] * l if yerr is None else yerr
        for i in range(l):
            col = self.color[-1][-1] if i > 0 else color
            mar = self.marker[-1][-1] if i > 0 else marker
            self.draw([x[i], x[i]], [y[i] - yerr[i] / 2, y[i] + yerr[i] / 2], xside = xside, yside = yside, marker = mar, color = col, lines = True)
            self.draw([x[i] - xerr[i] / 2, x[i] + xerr[i] / 2], [y[i], y[i]], xside = xside, yside = yside, marker = mar, color = col, lines = True)
        print('ssd',x, y)

    def draw_candlestick(self, dates, data, orientation = None, colors = None, label = None):
        orientation = 'v' if orientation is None else orientation
        markers = ['sd', '│', '─'] #if markers is None else markers
        colors = ['green', 'red'] if colors is None else colors
        x = []; y = []; color = []
        ln = len(dates)
        Open = data["Open"]; Close = data["Close"]; High = data["High"]; Low = data["Low"]
        for i in range(ln):
            d = dates[i]
            o, c, h, l = Open[i], Close[i], High[i], Low[i]
            color = colors[0] if c > o else colors[1]
            m, M = min(o, c), max(o, c)
            lab = label if i == 0 else None
            if orientation in ['v', 'vertical']:
                self.draw([d, d], [M, h], color = color, marker = markers[1], lines = True)
                self.draw([d, d], [l, m], color = color, marker = markers[1], lines = True)
                self.draw([d, d], [m, M], color = color, marker = markers[0], lines = True, label = lab)
                #self.draw([d, d], [M, M], color = color, marker = markers[0], lines = False)
                #self.draw([d, d], [m, m], color = color, marker = markers[0], lines = False)
            elif orientation in ['h', 'horizontal']:
                self.draw([M, h], [d, d], color = color, marker = markers[2], lines = True)
                self.draw([l, m], [d, d], color = color, marker = markers[2], lines = True)
                self.draw([m, M], [d, d], color = color, marker = markers[0], lines = True, label = lab)
                #self.draw([M, M], [d, d], color = color, marker = markers[0], lines = False)
                #self.draw([m, m], [d, d], color = color, marker = markers[0], lines = False)

    def draw_bar(self, *args, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None, offset = None):
        x, y = set_data(*args)
        x, y = remove_non_numerical(x, y)
        marker = self.default.bar_marker if marker is None else marker
        fill = self.default.bar_fill if fill is None else fill
        width = self.default.bar_width if width is None else width
        width = 1 if width > 1 else 0 if width < 0 else width
        orientation = self.default.bar_orientation[0] if orientation is None or orientation not in self.default.bar_orientation else orientation
        offset = 0 if offset is None else offset
        xpos = self.xside_to_pos(xside)
        ypos = self.yside_to_pos(yside)
        
        bar_labelled = any([type(el) == str for el in x])
        if not bar_labelled: # all x are numbers
            xlabels = get_labels(x)
        else:
            xlabels = list(map(str, x)) 
            xcoords = [] 
            for el in xlabels:
                if el in self.bar_labels:
                    pos = self.bar_labels.index(el)
                    xcoords.append(self.bar_coords[pos])
                else:
                    i = len(self.bar_labels) + 1
                    xcoords.append(i)
                    self.bar_labels.append(el)
                    self.bar_coords.append(i)
            x = xcoords
        xticks = x
        x = [el + offset for el in x]

        self.bar_labelled = any([bar_labelled, self.bar_labelled])
        self.bar_ylim = update_bar_ylim(self.bar_ylim + y + [minimum])
        xbar, ybar = bars(x, y, width, self.bar_ylim[0])
    
        if orientation in ['vertical', 'v']:
             fillx, filly = fill, False
             if self.bar_labelled:
                 self.xticks[xpos] = (self.xticks[xpos] if self.xticks[xpos] is not None else []) + xticks
                 self.xlabels[xpos] = (self.xlabels[xpos] if self.xlabels[xpos] is not None else []) + xlabels

             self.ylim[ypos] = self.bar_ylim
             self.bar_xlim = update_bar_xlim(self.bar_xlim + self.xlim[xpos] + xticks + ut.join(xbar))
             self.xlim[xpos] = self.bar_xlim
            
        elif orientation in ['horizontal', 'h']:
            xbar, ybar = ybar, xbar
            fillx, filly = False, fill
            if self.bar_labelled:
                self.yticks[ypos] = (self.yticks[ypos] if self.yticks[ypos] is not None else []) + xticks
                self.ylabels[ypos] = (self.ylabels[ypos] if self.ylabels[ypos] is not None else []) + xlabels
            self.xlim[xpos] = self.bar_ylim
            self.bar_xlim = update_bar_xlim(self.bar_xlim + self.ylim[ypos] + xticks + ut.join(ybar))
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

    def draw_multiple_bar(self, *args, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None):

        x, Y = set_bar_data(*args)
        ly = len(Y)
        width = self.default.bar_width if width is None else width
        marker = [marker] * ly if marker is None or type(marker) != list else marker
        color = [color] * ly if color is None else color
        label = [label] * ly if label is None else label
        width = width / ly if ly != 0 else 0
        offset = ut.linspace(-1 / 2 + 1 / (2 * ly), 1 / 2 - 1 / (2 * ly), ly) if ly != 0 else []
        
        for i in range(ly):
            self.draw_bar(x, Y[i],
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

    def draw_stacked_bar(self, *args, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None):
        x, Y = set_bar_data(*args)
        ly = len(Y)
        marker = [marker] * ly if marker is None or type(marker) != list else marker
        color = [color] * ly if color is None else color
        label = [label] * ly if label is None else label
        Y = ut.transpose([ut.cumsum(el) for el in ut.transpose(Y)])
        for i in range(ly - 1, -1, -1):
            self.draw_bar(x, Y[i],
                xside = xside, 
                yside = yside,
                marker = marker[i],
                color = color[i],
                fill = fill,
                width = width,
                orientation = orientation,
                label = label[i],
                minimum = minimum)

    def draw_hist(self, data, bins = None, norm = None, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None):
        bins = self.default.hist_bins if bins is None else bins
        norm = False if norm is None else norm
        x, y = hist_data(data, bins, norm)
        self.draw_bar(x, y,
                xside = xside, 
                yside = yside,
                marker = marker,
                color = color,
                fill = fill,
                width = width,
                orientation = orientation,
                label = label,
                minimum = None)

    def draw_matrix(self, matrix, marker = None, style = None, fast = False):
        matrix = [l.copy() for l in matrix]
        marker = [marker] if type(marker) != list else marker
        marker = [self.check_marker("sd") if el in ut.join([None, ut.hd_symbols]) else self.check_marker(el) for el in marker]
        style = ut.no_color if style is None else self.check_style(style)
        rows, cols = ut.matrix_size(matrix)
        rows = 0 if cols == 0 else rows
        matrix = matrix if rows * cols != 0 and ut.is_rgb_color(matrix[0][0]) else ut.turn_gray(matrix)
        marker = ut.repeat(marker, cols)
        if not fast:
            for r in range(rows):
                xyc = [(c, r, matrix[rows - 1 - r][c]) for c in range(cols)]
                x, y, color = ut.transpose(xyc, 3)
                self.draw(x, y, marker = marker, color = color, style = style)
            self.set_canvas_color("black")
            self.set_xlabel('column') 
            self.set_ylabel('row')
            xf, yf = min(self.xfrequency[0], cols), min(self.yfrequency[0], rows)
            xt = ut.linspace(0, cols - 1, xf)
            xl = get_labels([el + 1 for el in xt])
            yt = ut.linspace(0, rows - 1, yf)
            yl = get_labels([rows - el for el in yt])
            self.set_xticks(xt, xl)
            self.set_yticks(yt, yl)
        else:
            self.matrix = []
            for r in range(rows):
                matrix_r = []
                for c in range(cols):
                    colors = ["black", matrix[r][c], style]
                    ansi = ut.all_ansi(*colors)
                    m = ansi + marker[c] + ut.ansi_end
                    matrix_r.append([m] + colors)
                self.matrix.append(matrix_r)
            self.fast_plot = True

    def draw_image(self, path, marker = None, style = None, grayscale = False, fast = False):
        from PIL import Image, ImageOps
        path = ut.correct_path(path)
        if not ut.is_file(path):
            return
        image = Image.open(path)
        self._draw_image(image, marker = marker, style = style, grayscale = grayscale, fast = fast)

##############################################
###########    Plotting Tools    #############
##############################################

    def draw_event_plot(self, data, orientation = None, marker = None, color = None, side = None):
        x, y = data, [1.1] * len(data)
        orientation = 'v' if orientation is None else orientation
        if orientation in ['v', 'vertical']:
            self.draw(x, y, xside = side, marker = marker, color = color, fillx = True)
            self.set_ylim(0, 1)
            self.set_yfrequency(0)
        else:
            self.draw(y, x, yside = side, marker = marker, color = color, filly = True)
            self.set_xlim(0, 1)
            self.set_xfrequency(0)

    def draw_vertical_line(self, coordinate, color = None, xside = None):
        coordinate = self.string_to_coordinate(coordinate) if isinstance(coordinate, str) else coordinate
        pos = self.xside_to_pos(xside)
        self.vlines[pos].append(coordinate)
        color = self.ticks_color if color is None else color
        self.vcolors[pos].append(self.check_color(color))

    def draw_horizontal_line(self, coordinate, color = None, yside = None):
        coordinate = self.string_to_coordinate(coordinate) if isinstance(coordinate, str) else coordinate
        pos = self.xside_to_pos(yside)
        self.hlines[pos].append(coordinate)
        color = self.ticks_color if color is None else color
        self.hcolors[pos].append(self.check_color(color))

    def draw_text(self, text, x, y, xside = None, yside = None, color = None, style = None, alignment = None):
        self.text.append(str(text))
        x = self.string_to_coordinate(x) if isinstance(x, str) else x
        y = self.string_to_coordinate(y) if isinstance(y, str) else y
        self.tx.append(x)
        self.ty.append(y) 
        self.txside.append(self.correct_xside(xside))
        self.tyside.append(self.correct_yside(yside))
        self.tcolor.append(self.check_color(color))
        self.tstyle.append(self.check_style(style))
        alignment = self.default.talign[0] if alignment not in self.default.talign else alignment
        self.talign.append(alignment)

##############################################
#######    Plotting Tools Utilities    #######
############################################## 

    def string_to_coordinate(self, string):
        if string in self.bar_labels:
            pos = self.bar_labels.index(string)
            return self.bar_coords[pos]
        else:
            return self.date.string_to_time(string)

    def _draw_image(self, image, marker = None, style = None, grayscale = False, fast = False):
        image = ImageOps.grayscale(image) if grayscale else image
        image = image.convert('RGB')
        size = update_size(image.size, self.size)
        image = image.resize(size, resample = True)
        matrix = image_to_matrix(image)
        self.set_xfrequency(0); self.set_yfrequency(0);
        self.draw_matrix(matrix, marker = marker, style = style, fast = fast)
        self.set_xlabel(); self.set_ylabel()

##############################################
##########    Build Functions    #############
##############################################

    def build_plot(self, width, height):
        # Initial Tools
        signals = len(self.x)
        Signals = list(range(signals))
        texts = len(self.text)
        Texts = list(range(texts))
        r2 = [0, 1]

        # Color Simpler utilities
        sp = ut.space
        tc, ac, cc, ts, nc = self.ticks_color, self.axes_color, self.canvas_color, self.ticks_style, ut.no_color
        grid_colors = [cc, tc, nc]
        grid_ansi = ut.all_ansi(*grid_colors)
        canvas_colors = [cc, nc, nc]
        canvas_ansi = ut.all_ansi(*canvas_colors)
        #axes_no_colors = [ac, nc, nc]
        axes_colors = [ac, tc, ts]
        axes_ansi = ut.all_ansi(*axes_colors)

        # Apply Axes Scale (linear or log)
        xscale = [self.xscale[0] if self.xside[s] == self.default.xside[0] else self.xscale[1] for s in Signals]
        yscale = [self.yscale[0] if self.yside[s] == self.default.yside[0] else self.yscale[1] for s in Signals]
        self.x = [self.x[s] if xscale[s] is self.default.xscale[0] else ut.log(self.x[s]) for s in Signals]
        self.y = [self.y[s] if yscale[s] is self.default.yscale[0] else ut.log(self.y[s]) for s in Signals]
        self.xticks = [self.xticks[i] if self.xscale[i] is self.default.xscale[0] or self.xticks[i] is None else ut.log(self.xticks[i]) for i in r2]
        self.yticks = [self.yticks[i] if self.yscale[i] is self.default.yscale[0] or self.yticks[i] is None else ut.log(self.yticks[i]) for i in r2]
        self.hlines = [self.hlines[i] if self.yscale[i] is self.default.yscale[0] or self.hlines[i] is None else ut.log(self.hlines[i]) for i in r2]
        self.vlines = [self.vlines[i] if self.xscale[i] is self.default.xscale[0] or self.vlines[i] is None else ut.log(self.vlines[i]) for i in r2]

        # Apply Axes Scale (linear or log) to text
        txscale = [self.xscale[0] if self.txside[s] == self.default.xside[0] else self.xscale[1] for s in Texts]
        tyscale = [self.yscale[0] if self.yside[s] == self.default.yside[0] else self.yscale[1] for s in Texts]
        self.tx = [self.tx[s] if xscale[s] is self.default.xscale[0] else ut.log(self.tx[s]) for s in Texts]
        self.ty = [self.ty[s] if yscale[s] is self.default.yscale[0] else ut.log(self.ty[s]) for s in Texts]

        # Get X Limits
        x = [ut.join([self.x[s] for s in Signals if self.xside[s] is side]) for side in self.default.xside]
        x = [x[i] + self.vlines[i] for i in r2]
        xlim = list(map(get_lim, x))
        self.xlim = [[self.xlim[s][i] if self.xlim[s][i] is not None else xlim[s][i] for i in r2] for s in r2]
        xlim = [self.xlim[0] if self.xside[s] == self.default.xside[0] else self.xlim[1] for s in Signals]
        
        # Get Y Limits
        y = [ut.join([self.y[s] for s in Signals if self.yside[s] is side]) for side in self.default.yside]
        y = [y[i] + self.hlines[i] for i in r2]
        ylim = list(map(get_lim, y))
        self.ylim = [[self.ylim[s][i] if self.ylim[s][i] is not None else ylim[s][i] for i in r2] for s in r2]
        ylim = [self.ylim[0] if self.yside[s] == self.default.yside[0] else self.ylim[1] for s in Signals]

        # Adjust Height
        self.xaxes[0] = False if height <= 1 else self.xaxes[0]
        self.xaxes[1] = False if height <= 2 else self.xaxes[1]
        self.xfrequency[0] = 0 if height <= 3 else self.xfrequency[0]
        self.xfrequency[1] = 0 if height <= 4 else self.xfrequency[1]
        self.title = None if height <= 5 else self.title
        self.xlabel[1] = None if height <= 5 else self.xlabel[1]
        self.xlabel[0] = None if height <= 6 else self.xlabel[0]
        self.ylabel = [None, None] if height <= 6 else self.ylabel

        # Adjust X Ticks Frequency
        self.xfrequency = [self.xfrequency[i] if self.default.xside[i] in self.xside else 0 for i in r2]
        self.yfrequency = [self.yfrequency[i] if self.default.yside[i] in self.yside else 0 for i in r2]

        # Get Height Canvas
        height_xticks = [int(bool(el)) for el in self.xfrequency]
        height_lowbar = any([el is not None for el in self.ylabel + [self.xlabel[0]]])
        height_highbar = any([el is not None for el in [self.title, self.xlabel[1]]])
        height_canvas = height - sum(self.xaxes) - sum(height_xticks) - height_lowbar - height_highbar
        Height_canvas = range(height_canvas)

        # Adjust X Ticks Frequency
        self.yfrequency = [min(el, height_canvas) for el in self.yfrequency]

        # Adjust Width
        self.yaxes[0] = False if width <= 1 else self.yaxes[0]
        self.yaxes[1] = False if width <= 2 else self.yaxes[1]

        # Get Width Canvas
        width_canvas = width - sum(self.yaxes)

        # Get and Adjust Y Axis Numerical Ticks
        large, k = True, 0
        while large and k <= 2:
            yticks = [self.yticks[i] if isinstance(self.yticks[i], list) else ut.linspace(*self.ylim[i], self.yfrequency[i]) if None not in self.ylim[i] else [] for i in r2]
            yticks_scaled = [yticks[i] if self.yscale[i] == self.default.yscale[0] else ut.power10(yticks[i]) for i in r2]
            ylabels = [self.ylabels[i] if isinstance(self.yticks[i], list) else self.date.times_to_string(yticks_scaled[i]) if self.y_date[i] else get_labels(yticks_scaled[i]) for i in r2]
            ylabels = [add_extra_spaces(ylabels[i], self.default.yside[i]) for i in r2]
            width_ylabels = [0 if el == [] else len(el[0]) for el in ylabels]
            if width_canvas - sum(width_ylabels) >= 1:
                large = False
            else:
                if k <= 1:
                    self.yfrequency[k] = 0
                k += 1
        width_canvas -= sum(width_ylabels)
        Width_canvas = range(width_canvas)

        # Relative Y Ticks 
        rticks = [get_matrix_data(yticks[i], self.ylim[i], height_canvas) if None not in self.ylim[i] else [] for i in r2]
        rticks = [ut.floor(el) for el in rticks]

        # Get X Axis Numerical Ticks 
        self.xfrequency = [min(el, width_canvas) for el in self.xfrequency]
        xticks = [self.xticks[i] if isinstance(self.xticks[i], list) else ut.linspace(*self.xlim[i], self.xfrequency[i]) if None not in self.xlim[i] else [] for i in r2]
        xticks_scaled = [xticks[i] if self.xscale[i] == self.default.xscale[0] else ut.power10(xticks[i]) for i in r2]
        xlabels = [self.xlabels[i] if isinstance(self.xticks[i], list) else self.date.times_to_string(xticks_scaled[i]) if self.x_date[i] else get_labels(xticks_scaled[i]) for i in r2]
        xticks, xlabels = ut.transpose([ut.brush(xticks[i], xlabels[i]) for i in r2], 2)

        # Relative X Ticks 
        cticks = [get_matrix_data(xticks[i], self.xlim[i], width_canvas) if None not in self.xlim[i] else [] for i in r2]
        cticks = [ut.floor(el) for el in cticks]

        # Create Matrix of Markers with Grid Lines
        row0 = ['┼' if self.grid[1] and col in ut.join(cticks) else '─' for col in Width_canvas]
        row = ['│' if self.grid[1] and col in ut.join(cticks) else ut.space for col in Width_canvas]
        row0 = [grid_ansi + el  for el in row0]
        row = [grid_ansi + el for el in row]
        row0 = [[el] + grid_colors for el in row0]; row = [[el] + canvas_colors for el in row]
        self.matrix = [row0[:] if self.grid[0] and r in ut.join(rticks) else row[:] for r in Height_canvas][::-1]

        # Get Optional Grid Lines Numerical Ticks
        vticks = [get_matrix_data(self.vlines[i], self.xlim[i], width_canvas) if None not in self.xlim[i] else [] for i in r2]
        vticks = [ut.floor(el) for el in vticks]
        hticks = [get_matrix_data(self.hlines[i], self.ylim[i], height_canvas) if None not in self.ylim[i] else [] for i in r2]
        hticks = [ut.floor(el) for el in hticks]

        is_inside_canvas = lambda row, col: 0 <= row < height_canvas and 0 <= col < width_canvas
        # Add Optional Grid Lines to Matrix
        for r in r2:
            # Add Vertical Lines
            for i in range(len(vticks[r])):
                col = vticks[r][i]
                vlines_colors = [cc, self.vcolors[r][i], ts]
                vansi = ut.all_ansi(*vlines_colors)
                for row in Height_canvas:
                    if is_inside_canvas(row, col):
                        self.matrix[row][col] = [vansi + '│'] + vlines_colors if ut.uncolorize(self.matrix[row][col][0]) not in ['─', '┼'] else ['┼'] + vlines_colors
            # Add Horizontal Lines
            for i in range(len(hticks[r])):
                row = height_canvas - 1 - hticks[r][i]
                hlines_colors = [cc, self.hcolors[r][i], ts]
                hansi = ut.all_ansi(*hlines_colors)
                for col in Width_canvas:
                    if is_inside_canvas(row, col):
                        self.matrix[row][col] = [hansi + '─'] + hlines_colors if ut.uncolorize(self.matrix[row][col][0]) not in ['│', '┼'] else ['┼'] + vlines_colors

        # Add Optional Text to Data
        dx = [(self.xlim[i][1] - self.xlim[i][0]) / width_canvas if None not in self.xlim[i] and width_canvas != 0 else 0 for i in r2]
        for s in Texts:
            m = list(self.text[s])
            c = self.tcolor[s]
            l = len(m)
            xpos = self.xside_to_pos(self.txside[s])
            ypos = self.yside_to_pos(self.tyside[s])
            i0 = 0 if self.talign[s] == 'left' else l // 2 if self.talign[s] == 'center' else l - 1
            x = [self.tx[s] + dx[xpos] * (i - i0) for i in range(l)]
            y = [self.ty[s] for i in range(l)]
            c = [self.tcolor[s]] * l
            s = [self.tstyle[s]] * l
            self.marker.append(m)
            self.x.append(x)
            self.y.append(y)
            self.color.append(c)
            self.style.append(s)
            xlim.append(self.xlim[xpos])
            ylim.append(self.ylim[ypos])
            self.lines.append(False)
            self.fillx.append(False)
            self.filly.append(False)
            self.label.append(None)
        signals = len(self.x)
        Signals = list(range(signals))

        # Expand Canvas to accommodate HD markers
        xf = [max([ut.marker_factor(el, 2, 2, 2) for el in self.marker[s]], default = 1) for s in Signals]
        yf = [max([ut.marker_factor(el, 2, 3, 4) for el in self.marker[s]], default = 1) for s in Signals]
        width_expanded = [width_canvas * el for el in xf]
        height_expanded = [height_canvas * el for el in yf]
        
        #Get Relative Data to Be Plotted on Matrix
        x = [get_matrix_data(self.x[s], xlim[s], width_expanded[s])  for s in Signals]
        y = [get_matrix_data(self.y[s], ylim[s], height_expanded[s]) for s in Signals]
        m, c, st = self.marker, self.color, self.style

        # Add Lines between Data Points
        x, y, m, c, st = ut.transpose([get_lines(x[s], y[s], m[s], c[s], st[s]) if self.lines[s] else (x[s], y[s], m[s], c[s], st[s]) for s in Signals], 5)
        #x, y, m, c, st = ut.transpose([ut.brush(x[s], y[s], m[s], c[s], st[s]) for s in Signals], 5)
        
        # Fillx
        zeroy = [min(max(0, ylim[s][0]), ylim[s][1]) if None not in ylim[s] else 0 for s in Signals]
        y0 = [get_matrix_data([zeroy[s]], ylim[s], height_expanded[s])[0] if None not in ylim[s] else 0 for s in Signals]
        x, y, m, c, st = ut.transpose([fill_data(x[s], y[s], y0[s], m[s], c[s], st[s]) if self.fillx[s] else (x[s], y[s], m[s], c[s], st[s]) for s in Signals], 5)

        # Filly
        zerox = [[min(max(0, xlim[s][0]), xlim[s][1])] if None not in ylim[s] else 0 for s in Signals]
        x0 = [get_matrix_data(zerox[s], xlim[s], width_expanded[s])[0] if None not in ylim[s] else 0 for s in Signals]
        y, x, m, c, st = ut.transpose([fill_data(y[s], x[s], x0[s], m[s], c[s], st[s]) if self.filly[s] else (y[s], x[s], m[s], c[s], st[s]) for s in Signals], 5)

        # Reduce Canvas size if expanded
        #x = [reduce_canvas(x[s], xf) for s in Signals]
        #y = [reduce_canvas(y[s], yf) for s in Signals]
        x, y, m, c, st = ut.transpose([ut.brush(x[s], y[s], m[s], c[s], st[s]) for s in Signals], 5)

        # Get Actual HD Markers
        for s in Signals:
            xf = [ut.marker_factor(el, 2, 2, 2) for el in m[s]]
            yf = [ut.marker_factor(el, 2, 3, 4) for el in m[s]]
            if max(xf, default = 1) * max(yf, default = 1) != 1:
                 x[s], y[s], mxy = hd_group(x[s], y[s], xf, yf)
                 m[s] = [ut.get_hd_marker(mxy[i]) if m[s][i] in ut.hd_symbols else m[s][i] for i in range(len(x[s]))]
        #         x[s], y[s], m[s], c[s], st[s] = ut.brush(x[s], y[s], m[s], c[s], st[s])
        #print(x[0], y[0], xf[0], yf[0], m[0])

        # Add Data to Canvas
        #x, y, m, c, st = ut.transpose([ut.brush(x[s], y[s], m[s], c[s], st[s]) for s in Signals], 5)
        for s in Signals:
            for i in range(len(x[s])):
                row, col = height_canvas - 1 - y[s][i], x[s][i]
                if self.matrix == [] or not is_inside_canvas(row, col):
                    continue
                self.matrix[row][col] = [m[s][i], cc, c[s][i], st[s][i]]

        # Add Colors to Data
        for s in Signals:
            for i in range(len(x[s])):
                row, col = height_canvas - 1 - y[s][i], x[s][i]
                if self.matrix == [] or not is_inside_canvas(row, col):
                    continue
                if col == 0 or self.matrix[row][col][1:] != self.matrix[row][col - 1][1:]:
                    ansi = ut.all_ansi(*self.matrix[row][col][1:])
                    self.matrix[row][col][0] = ansi + self.matrix[row][col][0]
                if col != width_canvas - 1 and self.matrix[row][col][1:] != self.matrix[row][col + 1][1:]:
                    self.matrix[row][col][0] = self.matrix[row][col][0] + ut.ansi_end + ut.ansi(cc, 0)[0]
                if col == width_canvas - 1:
                    self.matrix[row][col][0] = self.matrix[row][col][0] + ut.ansi_end

        # utility function used to add legend, axis, ticks
        def insert(m, color, st, row, col):
            length = len(m)
            color = color if isinstance(color, list) else [color] * length
            st = st if isinstance(st, list) else [st] * length
            if row < height_canvas and col + length < width_canvas:
                for i in range(length):
                    colors = [cc, color[i], st[i]]
                    self.matrix[row][col + i] = [m[i]] + colors
                    ansi = ut.all_ansi(*colors)
                    self.matrix[row][col + i][0] = ansi + self.matrix[row][col + i][0]
                colors = self.matrix[row][col + length][1:]
                ansi = ut.all_ansi(*colors)
                self.matrix[row][col + length][1:] = colors
                self.matrix[row][col + length][0] = ansi + self.matrix[row][col + length][0]

        # Add Legend
        Labelled = [s for s in Signals if self.label[s] is not None]
        # Add Legend Side Symbols
        sides = [side_symbols[(self.xside[s], self.yside[s])] for s in Labelled]
        show_sides = not ut.no_duplicates(sides) == ['L']
        sides = [sp + el + sp if show_sides else sp for el in sides]
        [insert(sides[s], tc, ts, s, 0) for s in range(len(sides))] if show_sides else None
        col = len(sides[0]) if len(sides) > 0 else 0
        # Add Legend Markers
        marker = [''.join(ut.no_duplicates(self.marker[s])) for s in Labelled]
        marker = ['🬗' if marker[s] == 'fhd' else '▞' if marker[s] == 'hd' else ''.join(marker[s][:3]) for s in range(len(marker))]
        marker = [(marker[s][ : 3] * 3)[ : 3] for s in range(len(marker))]
        color = [(c[s][ : 3] * 3)[ : 3] for s in Labelled]
        style = [(st[s][ : 3] * 3)[ : 3] for s in Labelled]
        [insert(marker[s], color[s], style[s], s, col) for s in range(len(marker))]
        col += len(marker[0]) if len(marker) > 0 else 0
        # Add Legend Labels
        label = [self.label[s] for s in Labelled]
        length = max(map(len, label), default = 0)
        label = [sp + el + sp * (length - len(el)) for el in label]
        [insert(label[s], tc, ts, s, col) for s in range(len(label))]
        # Add Legend Frame
        # [insert(ut.space, tc, ts, s, col) for s in Labelled]
        # [insert(ut.space * (col + 1), tc, ts, len(label), 0) for s in Labelled]

        
        # Basic Y Axes
        yaxis = ['│' * height_canvas * self.yaxes[i] for i in r2]

        # Add Tick Sign in the side of Y Numbers
        primary_tick = ['┼' if self.grid[0] else ('┤' if i == 0 else '├') for i in r2]
        primary_tick = [[primary_tick[i]] * len(rticks[i]) for i in r2]
        yaxis = [ut.insert_strings(yaxis[i], primary_tick[i] , rticks[i])[0] for i in r2]

        # Add Tick Sign in the side of Canvas
        secondary_tick = [('├' if i == 0 else '┤') if self.grid[0] else '' for i in r2] 
        secondary_tick = [[secondary_tick[i]] * len(rticks[i - 1]) for i in r2]
        yaxis = [ut.insert_strings(yaxis[i], secondary_tick[i] , rticks[i - 1])[0] for i in r2]

        # Add Tick Sign in the side of Canvas due to horizontal lines
        hhticks = [el for el in ut.join(hticks)]
        tertiary_tick = [('├' if i == 0 else '┤') if hhticks != [] else '' for i in r2]
        tertiary_tick = [['┼' if hhticks[j] in rticks[i] else tertiary_tick[i] for j in range(len(hhticks))] for i in r2]
        yaxis = [ut.insert_strings(yaxis[i], tertiary_tick[i], hhticks)[0] for i in r2]

        # Add Colors to Y Axes
        yaxis = [[axes_ansi + el + ut.ansi_end if el != ''  else '' for el in axis] for axis in yaxis]
        yaxis = [[[[el] + axes_colors] for el in axis][::-1] for axis in yaxis]

        # Add Y Axes to Matrix
        for i in r2:
            self.matrix = ut.pad(self.matrix, yaxis[i], self.default.yside[i])

            
        # Add Y Numerical Ticks
        yticks = [[ylabels[i][rticks[i].index(h)] if h in rticks[i] else ut.space * width_ylabels[i] for h in Height_canvas][::-1] for i in r2]
        
        # Add Colors to Y Ticks
        yticks = [[[axes_ansi + tick[0] if i == 0 else (tick[i] + ut.ansi_end) if i == len(tick) - 1 else tick[i] for i in range(len(tick))] for tick in ytick] for ytick in yticks]
        yticks = [[[[el] + axes_colors for el in tick] for tick in ytick] for ytick in yticks]
        for i in r2:
            self.matrix = ut.pad(self.matrix, yticks[i], self.default.yside[i])

        
        # Build X Ticks
        xticks = [ut.space * width_canvas  for i in r2]
        xticks, cticks = ut.transpose([ut.insert_strings(xticks[i], xlabels[i], cticks[i], 1) for i in r2], 2)

        # Add Side Spaces to X Ticks due to Y Labels
        xticks = [ut.space * width_ylabels[0] + ut.space * bool(self.yaxes[0]) + xticks[i] + ut.space * bool(self.yaxes[1]) + ut.space * width_ylabels[1] for i in r2]
        #xf = [int(bool(el)) for el in self.xfrequency]
        xticks = [xticks[i] * height_xticks[i] for i in r2]

        # Build X Axis
        xaxis = ['─' * width_canvas for i in r2]

        # Add Tick Sign in the side of X Numbers
        primary_tick = ['┼' if self.grid[1] else ('┬' if i == 0 else '┴') for i in r2] # tick on the side of x numbers
        primary_tick = [[primary_tick[i]] * len(cticks[i]) for i in r2]
        xaxis = [ut.insert_strings(xaxis[i], primary_tick[i] , cticks[i])[0] for i in r2]

        # Add Tick Sign in the side of Canvas
        secondary_tick = [('┴'  if i == 0 else '┬') if self.grid[1] else '' for i in r2]  # tick on the canvas side
        secondary_tick = [[secondary_tick[i]] * len(cticks[i - 1]) for i in r2]
        xaxis = [ut.insert_strings(xaxis[i], secondary_tick[i] , cticks[i - 1])[0] for i in r2]

        # Add Tick Sign in the side of Canvas due to vertical lines
        vvticks = ut.join(vticks)
        tertiary_tick = [('┴' if i == 0 else '┬') if vvticks != [] else '' for i in r2] # tick on the canvas side due to vertical lines
        tertiary_tick = [['┼' if vvticks[j] in cticks[i] else tertiary_tick[i] for j in range(len(vvticks))] for i in r2]
        xaxis = [ut.insert_strings(xaxis[i], tertiary_tick[i], vvticks)[0] for i in r2]

        # Add Side Spaces to X Axes due to Y Labels
        xaxis = [ut.space * width_ylabels[0] + ('└' if  i == 0 else '┌') * bool(self.yaxes[0]) + xaxis[i] + ('┘' if  i == 0 else '┐') * bool(self.yaxes[1]) + ut.space * width_ylabels[1] for i in r2]
        xa = [int(el) for el in self.xaxes]
        xaxis = [list(xaxis[i] * xa[i]) for i in r2]

        # Add Colors to X Axes and X Ticks
        xaxis = [[axes_ansi + axis[0] if i == 0 else axis[i] for i in range(len(axis))] for axis in xaxis]
        xticks = [[axes_ansi + ticks[0] if i == 0 else ticks[i] for i in range(len(ticks))] for ticks in xticks]
        xaxis = [[[[el] + axes_colors for el in axe]] if len(axe) != 0 else [] for axe in xaxis]
        xticks = [[[[el] + axes_colors for el in tick]] if len(tick) != 0 else [] for tick in xticks]

        # Add X Axes and X Ticks to Matrix
        for i in r2:
            self.matrix = ut.pad(self.matrix, xaxis[i], self.default.xside[i]) 
            self.matrix = ut.pad(self.matrix, xticks[i], self.default.xside[i])

        # Add Lower Label Bar
        low_bar = ut.space * width * height_lowbar
        ylabel = ['' if self.ylabel[i] is None else self.ylabel[i]  for i in r2]
        xlabel = '' if self.xlabel[0] is None else self.xlabel[0] 
        label = [ylabel[0], xlabel, ylabel[1]]
        center = width_ylabels[0] + int(self.yaxes[0]) + width_canvas // 2
        pos = [0, center, width - 1]
        low_bar = ut.insert_strings(low_bar, label, pos, 1)[0]
        low_bar = [axes_ansi + low_bar[0] if i == 0 else low_bar[i] for i in range(len(low_bar))]
        low_bar = [[[el] + axes_colors for el in low_bar]] if len(low_bar) != 0 else []
        self.matrix = ut.pad(self.matrix, low_bar, self.default.xside[0])

        # Add High Label Bar
        no_xlabel = self.xlabel[1] is None #or cticks[1] == []
        high_bar = sp * width * height_highbar
        title = '' if self.title is None else self.title
        xlabel = '' if no_xlabel else self.xlabel[1]
        label = [title] + ([xlabel] if not no_xlabel else [])
        pos = [0, center] if not no_xlabel else [center]
        high_bar = ut.insert_strings(high_bar, label, pos, 1)[0]
        high_bar = [axes_ansi + high_bar[0] if i == 0 else high_bar[i] for i in range(len(high_bar))]
        high_bar = [[[el] + axes_colors for el in high_bar]] if len(high_bar) != 0 else []
        self.matrix = ut.pad(self.matrix, high_bar, self.default.xside[1])

        if width > 0:
            for row in range(height):
                self.matrix[row][0][0] = ut.ansi_end + self.matrix[row][0][0]
                self.matrix[row][-1][0] = self.matrix[row][-1][0] + ut.ansi_end


    def to_canvas(self):
        matrix = [[col[0] for col in row] for row in self.matrix]
        canvas = [''.join(row) for row in matrix]
        self.canvas = '\n'.join(canvas) + '\n'

    def to_html(self):
        rows, cols = ut.matrix_size(self.matrix)
        code = lambda color: "rgb" + str(color).replace(" ", "")
        #html = "<body>\n<p style=\"font-family:courier; font-size:11pt;\">\n\n"
        html = "<body> \n <code style = style=\"font-family:courier; \"font-size : 10pt;\"> \n\n"
        for r in range(rows):
            for c in range(cols):
                marker, background, color, style = self.matrix[r][c]
                marker = ut.uncolorize(marker)
                marker = "&nbsp;" if marker == ut.space else marker
                marker = '<b>' + marker + '</b>' if style == 'bold' else marker
                marker = '<i>' + marker + '</i>' if style == 'italic' else marker
                color = 'white' if color == 'default' else color
                background = 'black' if background == 'default' else background
                color = ut.to_rgb(color)
                background = ut.to_rgb(background)
                html += "<span style = \"color:" + code(color) + "; background-color: " + code(background) + "\">" + marker + "</span>"
            html += " <br>\n\n"
        html += "<code> \n </body>"
        return html

##############################################
#########    Utility Functions    ############
##############################################

def set_data(x = None, y = None): # it return properly formatted x and y data lists
   if x is None and y is None :
       x, y = [], []
   elif x is not None and y is None:
       y = x
       x = list(range(1, len(y) + 1))
   lx, ly = len(x), len(y)
   if lx != ly:
       l = min(lx, ly)
       x = x[ : l]
       y = y[ : l]
   return [x, y]

non_numerical = lambda el:  el == None or (not isinstance(el, str) and math.isnan(el))

def remove_non_numerical(x, y): # it remove None and nan values but keeps strings for possible date or bar plots
   l = len(x)
   p = [i for i in range(l) if not (non_numerical(x[i]) or non_numerical(y[i]))]
   xn = [ut.try_float(x[i]) for i in p]
   yn = [ut.try_float(y[i]) for i in p]
   return xn, yn

def set_bar_data(*args):
    if len(args) == 1:
        Y = args[0]
        x = list(range(1, len(Y[0]) + 1))
    else:
        x, Y = args
    return x, Y

def get_lim(data): # it returns the data minimum and maximum limits
    m = min(data, default = None)
    M = max(data, default = None)
    m, M = (m, M) if m is None or m != M else (0.5 * m, 1.5 * m) if m == M != 0 else (-1, 1) 
    return [m, M]

def get_matrix_data(data, lim, bins): # from data to relative canvas coordinates
    change = lambda el: 0.5 + (bins - 1) * (el - lim[0]) / (lim[1] - lim[0])
    return [math.floor(change(el)) for el in data]

def get_lines(x, y, *other): # it returns the lines between all couples of data points like x[i], y[i] to x[i + 1], y[i + 1]; other are the list of markers and colors that needs to be elongated
    o = ut.transpose(other, len(other))
    xl, yl, ol = [[] for i in range(3)] 
    for n in range(len(x) - 1):
        xn, yn = x[n : n + 2], y[n : n + 2]
        xn, yn = get_line(xn, yn)
        xl += xn[:-1]
        yl += yn[:-1]
        ol += [o[n]] * len(xn[:-1])
    xl = xl + [x[-1]] if x != [] else xl
    yl = yl + [y[-1]] if x != [] else yl
    ol = ol + [o[-1]] if x != [] else ol
    return xl, yl, *ut.transpose(ol, len(other))

def get_line(x, y): # it returns a line of points from x[0],y[0] to x[1],y[1] distanced between each other in x and y by at least 1.
    x0, x1 = x
    y0, y1 = y
    dx, dy = int(x1) - int(x0), int(y1) - int(y0)
    ax, ay = abs(dx), abs(dy)
    a = int(max(ax, ay) + 1)
    x = [int(el) for el in ut.linspace(x0, x1, a)]
    y = [int(el) for el in ut.linspace(y0, y1, a)]
    return [x, y]

def fill_data(x, y, y0, *other): # it fills x, y with y data points reaching y0;  and c are the list of markers and colors that needs to be elongated
    o = ut.transpose(other, len(other))
    xy = []
    xf, yf, of = [[] for i in range(3)] 
    for i in range(len(x)):
        xi, yi = x[i], y[i]
        if [xi, yi] not in xy:
            xy.append([xi, yi])
            yn = range(y0, yi + 1) if y0 < yi else range(yi, y0) if y0 > yi else [yi]
            yn = list(yn)
            xn = [xi] * len(yn)
            xf += xn
            yf += yn
            of += [o[i]] * len(xn)
    return [xf, yf, *ut.transpose(of, len(other))]

def reduce_canvas(x, xf):
    return [int(el // xf) for el in x]

side_symbols = {("lower", "left"): 'L', ("lower", "right"): '⅃', ("upper", "left"): 'Γ', ("upper", "right"): '⅂'} # symbols used in the legend to indentify the axes used for plot

def get_labels(ticks): # it returns the approximated string version of the data ticks
    d = distinguishing_digit(ticks)
    formatting_string = "{:." + str(d + 1) + "f}"
    labels = [formatting_string.format(el) for el in ticks]
    #labels = [str(ut.round(el, d + 1)) for el in ticks]
    pos = [el.index('.') + d + 2 for el in labels]
    labels = [labels[i][: pos[i]] for i in range(len(labels))]
    labels = [add_extra_zeros(el, d + 1) if len(labels) > 1 else el for el in labels]
    #sign = any([el < 0 for el in ticks])
    #labels = ['+' + labels[i] if ticks[i] > 0 and sign else labels[i] for i in range(len(labels))]
    return labels

def distinguishing_digit(data): # it return the minimum amount of decimal digits necessary to distinguish all elements of a list
    #data = [el for el in data if 'e' not in str(el)]
    d = [_distinguishing_digit(data[i], data[i + 1]) for i in range(len(data) - 1)]
    return max(d, default = 1)

def _distinguishing_digit(a, b): # it return the minimum amount of decimal digits necessary to distinguish a from b (when both are rounded to those digits).
    d = abs(a - b)
    d = 0 if d == 0 else - math.log10(2 * d)
    #d = round(d, 10)
    d = 0 if d < 0 else math.ceil(d)
    d = d + 1 if ut.round(a, d) == ut.round(b, d) else d
    return d
    
def add_extra_zeros(label, d): # it adds 0s at the end of a label if necessary
    zeros = len(label) - 1 - label.index('.' if 'e' not in label else 'e')
    if zeros < d:
        label += '0' * (d - zeros)
    return label

def add_extra_spaces(labels, side): # it adds empty spaces before or after the labels if necessary
    length = 0 if labels == [] else max(list(map(len, labels)))
    if side == "left":
        labels = [ut.space * (length - len(el)) + el for el in labels]
    if side == "right":
        labels = [el + ut.space * (length - len(el)) for el in labels]
    return labels

def add_ticks(axis, coords, tick): # adds ticks to an axis at each coordinate
    for i in range(len(coords)):
        axis = ut.insert_string(axis, tick, coords[i], 'left') if tick is not None else axis
    return axis

def hd_group(x, y, xf, yf): # it returns the real coordinates of the HD markers and the matrix that defines the marker
    l, xfm, yfm = len(x), max(xf), max(yf)
    xm = [el // xfm for el in x]
    ym = [el // yfm for el in y]
    m = {}
    for i in range(l):
        xyi = xm[i], ym[i]
        xfi, yfi = xf[i], yf[i]
        mi = [[0 for x in range(xfi)] for y in range(yfi)]
        m[xyi] = mi
    for i in range(l):
        xyi = xm[i], ym[i]
        xk, yk = x[i] % xfi, y[i] % yfi
        xk, yk = math.floor(xk), math.floor(yk)
        m[xyi][yk][xk] = 1
    x, y = ut.transpose(m.keys(), 2)
    m = [tuple(ut.join(el[::-1])) for el in m.values()]
    return x, y, m

###############################################
#############   Bar Functions    ##############
###############################################

def update_bar_xlim(y): # it updates the bar limits along their base dimension  (x if orientation is vertical otherwise y)
   y = [el for el in y if el is not None]
   bar_lim = get_lim(y)
   return bar_lim

def update_bar_ylim(y): # it updates the bar limits along their heights (y if orientation is vertical otherwise x)
   bar_lim = update_bar_xlim(y)
   if None not in bar_lim:
       delta = (bar_lim[1] - bar_lim[0]) / 20
       delta = bar_lim[0] / 20 if delta == 0 else delta
       bar_lim[0] = bar_lim[0] - delta if bar_lim[0] - delta > 0 else bar_lim[0]
   return bar_lim

def bars(x, y, width, minimum): # given the bars center coordinates and height, it returns the full bar coordinates
   if x == []:
       return [], []
   bins = len(x)
   #bin_size_half = (max(x) - min(x)) / (bins - 1) * width / 2
   bin_size_half = width / 2
   # adjust the bar width according to the number of bins
   if bins > 1:
       bin_size_half *= (max(x) - min(x)) / (bins - 1)
   xbar, ybar = [], []
   for i in range(bins):
       xbar.append([x[i] - bin_size_half, x[i] - bin_size_half,
                    x[i] + bin_size_half, x[i] + bin_size_half,
                    x[i] - bin_size_half])
       ybar.append([minimum, y[i], y[i], minimum, minimum])
   return xbar, ybar

def hist_data(data, bins = 10, norm = False): # it returns data in histogram form if norm is False. Otherwise, it returns data in density form where all bins sum to 1.
    #data = [round(el, 15) for el in data]
    if data == []:
        return [], []
    m, M = min(data), max(data)
    data = [(el - m) / (M - m) * bins if el != M else bins - 1 for el in data]
    data = [int(el) for el in data]
    histx = ut.linspace(m, M, bins)
    histy = [0] * bins
    for el in data:
        histy[el] += 1
    if norm:
        histy = [el / len(data) for el in histy]
    return histx, histy

###############################################
############   Image Functions    #############
###############################################

def update_size(size_old, size_new): # it resize an image to the desired size, mantaining or not its size ratio and adding or not a pixel averaging factor with resample = True
    size_old = [size_old[0], size_old[1] / 2]
    ratio_old = size_old[1] / size_old[0]
    size_new = ut.replace(size_new, size_old)
    ratio_new = size_new[1] / size_new[0]
    #ratio_new = size_new[1] / size_new[0]
    size_new = [1 if el == 0 else el for el in size_new]
    return [int(size_new[0]), int(size_new[1])]

def image_to_matrix(image): # from image to a matrix of pixels
    pixels = list(image.getdata())
    width, height = image.size
    return [pixels[i * width:(i + 1) * width] for i in range(height)]
