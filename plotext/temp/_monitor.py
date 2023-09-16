# from plotext._default import default_monitor
# from plotext._axes import * 
# from plotext._canvas import canvas_class
# from plotext._matrix import matrix_class
# from plotext._build import build_class
# import plotext._utility as ut
# from copy import deepcopy
# import math

# # This file defines the monitor class, i.e. the plot, where actual data is plotted; the plot is build separately in the build class for clarity; here only the main tools and drawing methods are written

# class monitor_class(build_class):
    
#     def __init__(self, date):
#         self.axes_init(date)
#         self.canvas = canvas_class()
#         self.signals = signals_class()
#         self.color_init()
#         self.data_init()
#         #self.matrix = matrix_class()

#     def copy(self): # to deep copy 
#         return deepcopy(self)

#     def set_size(self, size): # called externally by the figure containing it, to pass the size
#         self.size = size

# ##############################################
# #########    Internal Variables    ###########
# ##############################################

#     def axes_init(self, date):
#         self.xaxes = [xaxis_class(date), xaxis_class(date)]
#         self.yaxes = [yaxis_class(date), yaxis_class(date)]

#     def color_init(self):
#         self.set_theme('default')

#     def data_init(self):
#         self.fast_plot = False
#         self.lines_init()
#         self.text_init()
#         self.draw_init()

#     def lines_init(self):
#         self.vcoord = [[], []] # those are user defined extra grid lines, vertical or horizontal, for each axis
#         self.hcoord = [[], []]
#         self.vcolors = [[], []] # their color
#         self.hcolors = [[], []]

#     def text_init(self):
#         self.text = []
#         self.tx = []
#         self.ty = []
#         self.txside = []
#         self.tyside = []
#         self.torien = []
#         self.talign = []
#         self.tfull = []
#         self.tback = []
#         self.tstyle = []

#     def draw_init(self):  # Variables Set with Draw internal Arguments
#         self.xside = [] # which side the x axis should go, for each plot (lower or upper)
#         self.yside = [] # which side the y axis should go, for each plot (left or right)

#         self.x = [] # list of x coordinates 
#         self.y = [] # list of y coordinates
#         self.signals = 0 # number of signals to plot

#         self.lines = [] # whatever to draw lines between points

#         self.marker = [] # list of markers used for each plot
#         self.color = [] # list of marker colors used for each plot
#         self.past_colors = []
#         self.style = []

#         self.fillx = [] # fill data vertically (till x axis)
#         self.filly = [] # fill data horizontally (till y axis)

#         self.label = [] # subplot list of labels

# ##############################################
# #######    External Set Functions    #########
# ##############################################

#     def set_ylabel(self, label = None, yside = None):
#         pos = self.yside_to_pos(yside)
#         self.ylabel[pos] = self.set_label(label)
        
#     def set_xlim(self, left = None, right = None, xside = None):
#         left = None if left is None else float(left)
#         right = None if right is None else float(right)
#         xlim = [left, right]
#         xlim = xlim if None in xlim else [min(xlim), max(xlim)]
#         pos = self.xside_to_pos(xside)
#         self.xlim[pos] = xlim

#     def set_ylim(self, lower = None, upper = None, yside = None):
#         lower = None if lower is None else float(lower)
#         upper = None if upper is None else float(upper)
#         ylim = [lower, upper]
#         ylim = ylim if None in ylim else [min(ylim), max(ylim)]
#         pos = self.yside_to_pos(yside)
#         self.ylim[pos] = ylim

#     def set_xscale(self, scale = None, xside = None):
#         default_case = (scale is None or scale not in self.default.xscale)
#         scale = self.default.xscale[0] if default_case else scale
#         pos = self.xside_to_pos(xside)
#         self.xscale[pos] = scale

#     def set_yscale(self, scale = None, yside = None):
#         default_case = (scale is None or scale not in self.default.yscale)
#         scale = self.default.yscale[0] if default_case else scale
#         pos = self.yside_to_pos(yside)
#         self.yscale[pos] = scale

#     def set_xticks(self, ticks = None, labels = None, xside = None):
#         pos = self.xside_to_pos(xside)
#         ticks = self.default.xticks[pos] if ticks is None else list(ticks)
#         labels = ut.get_labels(ticks) if labels is None else list(map(str, labels))
#         ticks, labels = ut.brush(ticks, labels)
#         self.xticks[pos] = ticks
#         self.xlabels[pos] = labels
#         self.xfrequency[pos] = self.xfrequency[pos] if ticks is None else len(ticks)

#     def set_yticks(self, ticks = None, labels = None, yside = None):
#         pos = self.yside_to_pos(yside)
#         ticks = self.default.yticks[pos] if ticks is None else list(ticks)
#         labels = ut.get_labels(ticks) if labels is None else list(map(str, labels))
#         ticks, labels = ut.brush(ticks, labels)
#         self.yticks[pos] = ticks
#         self.ylabels[pos] = labels
#         self.yfrequency[pos] = self.yfrequency[pos] if ticks is None else len(ticks)

#     def set_xfrequency(self, frequency = None, xside = None):
#         pos = self.xside_to_pos(xside)
#         frequency = self.default.xfrequency[pos] if frequency is None else int(frequency)
#         self.xfrequency[pos] = frequency
        
#     def set_yfrequency(self, frequency = None, yside = None):
#         pos = self.yside_to_pos(yside)
#         frequency = self.default.yfrequency[pos] if frequency is None else int(frequency)
#         self.yfrequency[pos] = frequency

#     def set_xreverse(self, reverse = None, xside = None):
#         pos = self.xside_to_pos(xside)
#         direction = self.default.xdirection[pos] if reverse is None else 2 * int(not reverse) - 1
#         self.xdirection[pos] = direction

#     def set_yreverse(self, reverse = None, yside = None):
#         pos = self.yside_to_pos(yside)
#         direction = self.default.ydirection[pos] if reverse is None else 2 * int(not reverse) - 1
#         self.ydirection[pos] = direction
        
#     def set_xaxes(self, lower = None, upper = None):
#         self.xaxes[0] = self.default.xaxes[0] if lower is None else bool(lower)
#         self.xaxes[1] = self.default.xaxes[1] if upper is None else bool(upper)
        
#     def set_yaxes(self, left = None, right = None):
#         self.yaxes[0] = self.default.yaxes[0] if left is None else bool(left)
#         self.yaxes[1] = self.default.yaxes[1] if right is None else bool(right)

#     def set_frame(self, frame = None):
#         self.set_xaxes(frame, frame)
#         self.set_yaxes(frame, frame)

#     def set_grid(self, horizontal = None, vertical = None):
#         horizontal = self.default.grid[0] if horizontal is None else bool(horizontal)
#         vertical = self.default.grid[1] if vertical is None else bool(vertical)
#         self.grid = [horizontal, vertical]

#     def set_color(self, color = None):
#         color = color if ut.is_color(color) else None
#         return self.default.canvas_color if color is None else color

        
#     def set_axes_color(self, color = None):
#         self.axes_color = self.set_color(color)
        
#     def set_ticks_color(self, color = None):
#         self.ticks_color = self.set_color(color)

#     def set_ticks_style(self, style = None):
#         style = style if ut.is_style(style) else None
#         style = self.default.ticks_style if style is None else ut.clean_styles(style)
#         self.ticks_style = style

#     def set_theme(self, theme = None):
#         theme = 'default' if theme is None or theme not in ut.themes else theme
#         self._set_theme(*ut.themes[theme])

#     def clear_color(self):
#         self.set_theme('clear')

# ##############################################
# #######    Set Functions Utilities    ########
# ##############################################

#     def set_label(self, label = None): 
#         label = None if label is None else str(label).strip()
#         spaces = ut.only_spaces(label)
#         label = None if spaces else label 
#         return label

#     def correct_xside(self, xside = None): # from axis side to position
#         xaxis = default_monitor.xside
#         xside = xaxis[xside - 1] if isinstance(xside, int) and 1 <= xside <= 2 else xaxis[0] if xside is None or xside.strip() not in xaxis else xside.strip()
#         return xside

#     def correct_yside(self, yside = None):
#         yaxis = default_monitor.yside
#         yside = yaxis[yside - 1] if isinstance(yside, int) and 1 <= yside <= 2 else yaxis[0] if yside is None or yside.strip() not in yaxis else yside.strip()
#         return yside

#     def xside_to_pos(self, xside = None): # from axis side to position
#         xside = self.correct_xside(xside)
#         pos = default_monitor.xside.index(xside)
#         return pos

#     def yside_to_pos(self, yside = None):
#         yside = self.correct_yside(yside)
#         pos = default_monitor.yside.index(yside)
#         return pos
    
#     def get_xaxis(self, xside = None):
#         xpos = self.xside_to_pos(xside)
#         return self.xaxes[xpos]
    
#     def get_yaxis(self, yside = None):
#         ypos = self.yside_to_pos(yside)
#         return self.yaxes[ypos]

#     def _set_theme(self, canvas_color, axes_color, ticks_color, ticks_style, color_sequence):
#         self.canvas_color = canvas_color
#         self.axes_color = axes_color
#         self.ticks_color = ticks_color
#         self.ticks_style = ticks_style
#         self.color_sequence = color_sequence
        
# ##############################################
# ##########    Draw() Function    #############
# ##############################################

#     def draw(self, *args, **kwargs): # from draw() comes directly the functions scatter() and plot()
#         x, y = ut.set_data(*args)
#         xside = kwargs.get("xside")
#         yside = kwargs.get("yside")
#         xside = self.correct_xside(xside)
#         yside = self.correct_yside(yside)
        
#         self.add_data(*args, xside = xside, yside = yside)
#         self.add_lines(kwargs.get("lines"))
#         self.add_marker(kwargs.get("marker"))
#         self.add_color(kwargs.get("color"))
#         self.add_styles(kwargs.get("style"))
#         self.add_fillx(kwargs.get("fillx"))
#         self.add_filly(kwargs.get("filly"))
#         self.add_label(kwargs.get("label"))
        
# ##############################################
# #######    Draw() Called Functions    ########
# ##############################################

#     def add_data(self, *args, xside = None, yside = None):
        
#         self.get_xaxis(xside).add_data(x)
#         self.get_yaxis(yside).add_data(y)
#         self.signals += 1

#     def add_lines(self, lines):
#         lines = default_monitor.lines if lines is None else bool(lines) 
#         self.lines.append(lines)
        
#     def add_marker(self, marker = None):
#         single_marker = isinstance(marker, str) or marker is None
#         marker = self.check_marker(marker) if single_marker else list(map(self.check_marker, marker))
#         length = len(self.x[-1])
#         marker = ut.to_list(marker, length)
#         self.canvas.add_marker(marker)

#     def add_color(self, color = None):
#         list_color = isinstance(color, list) 
#         color = list(map(self.check_color, color)) if list_color else self.check_color(color)
#         length = len(self.x[-1])
#         self.past_colors = self.past_colors + [color] if color not in self.past_colors else self.past_colors
#         color = ut.to_list(color, length)
#         self.canvas.add_color(color)

#     def add_styles(self, style = None):
#         single_style = isinstance(style, str) or style is None
#         style = self.check_style(style) if single_style else list(map(self.check_style, style))
#         length = len(self.x[-1])
#         style = ut.to_list(style, length)
#         self.style.append(style)

#     def add_fillx(self, fillx = None):
#         fillx = self.check_fill(fillx)
#         self.fillx.append(fillx)

#     def add_filly(self, filly = None):
#         filly = self.check_fill(filly)
#         self.filly.append(filly)

#     def add_label(self, label = None):
#         spaces = ut.only_spaces(label)
#         label = default_monitor.label if label is None or spaces else str(label).strip() # strip to remove spaces before and after
#         self.label.append(label)#
#         #figure.subplot.label_show.append(default.label_show)
    
# ##############################################
# ######    Draw() Functions Utilities   #######
# ##############################################





#     def check_style(self, style = None):
#         style = None if style is None else str(style)
#         style = style if ut.is_style(style) else ut.no_color
#         return style


# ##############################################
# ######    Other Plotting Functions    ########
# ##############################################

#     # this is the general drawing function for the bar, box, candlestick and error plots
#     def draw_sixtuples(self, sixtuples, marker = None, positive_color = None, negative_color = None, fill = None, width = None, orientation = None, offset = None, reset_ticks = None, xside = None, yside = None, label = None):
        
#         bar_marker = default_monitor.bar_marker if marker is None else marker
#         positive_color = self.check_color(positive_color)
#         negative_color = self.check_color(negative_color)
#         fill = default_monitor.bar_fill if fill is None else fill
#         width = default_monitor.bar_width if width is None else width
#         width = 1 if width > 1 else 0 if width < 0 else width
#         orientation = self.check_orientation(orientation, 1)
#         offset = 0 if offset is None else offset
#         reset_ticks = True if reset_ticks is None else reset_ticks

#         l = len(sixtuples)
#         vertical = orientation[0] == 'v'
        
#         x = [el[0] for el in sixtuples]
#         y = [el[1:] for el in sixtuples]

#         x = bar_data_class(x, self.get_xconverter(xside))
#         x.add(offset)

#         self.set_xticks(x.numbers, x.labels, xside) if reset_ticks and orientation[0] == 'v' else self.set_yticks(x.numbers, x.labels, yside) if reset_ticks else None

#         bar_size = width * (max(x) - min(x)) / (l - 1)
        
#         vline_marker = '│' if vertical else '─'
#         hline_marker = '─' if vertical else '│'
        
#         #first_bar_index = min([i for i in range(l) if y[i][0] != y[i][1]], default = 0) # finds the position of the first non zero bar
        
#         for i in range(l):
#             left, center, right = x[i] - bar_size / 2, x[i], x[i] + bar_size / 2
#             line_low, line_center, line_high = y[i][0], y[i][2], y[i][4]
#             bar_low, bar_high = y[i][1], y[i][3]

#             plot_color = positive_color if bar_high >= bar_low else negative_color
#             plot_label = label if i == 0 else None

#             # draw line along bar
#             plot_lines = line_low is not None and line_high is not None
#             xi, yi = [center, center], [line_low, line_high]
#             xi, yi = (xi, yi) if vertical else (yi, xi) 
#             self.draw(xi, yi,
#                       xside = xside,
#                       yside = yside,
#                       color = plot_color,
#                       marker = vline_marker,
#                       lines = True) if plot_lines else None
            
#             # draw bar
#             plot_lines = line_center is not None
#             xi, yi = [left, right], [bar_low, bar_high]
#             xi, yi = (xi, yi) if vertical else (yi, xi) 
#             self.draw_rectangle(xi, yi,
#                                 xside = xside, 
#                                 yside = yside,
#                                 lines = True,
#                                 marker = bar_marker,
#                                 color = plot_color,
#                                 fill = fill,
#                                 label = plot_label)

#             # draw line across bar
#             xi, yi = [left, right], [line_center, line_center]
#             xi, yi = (xi, yi) if vertical else (yi, xi) 
#             self.draw(xi, yi,
#                       xside = xside,
#                       yside = yside,
#                       color = plot_color,
#                       marker = hline_marker,
#                       lines = True) if plot_lines else None

            
            

#            # no_bar = (yi[1] == yi[0] and orientation[0] == 'v') or (xi[1] == xi[0] and orientation[0] == 'h')
            
#     def draw_bar(self, *args, marker = None, color = None, fill = None, width = None, orientation = None, minimum = None, offset = None, reset_ticks = None, xside = None, yside = None, label = None):
#         x, y = ut.set_data(*args)
#         minimum = 0 if minimum is None else minimum 
#         sixtuples = [[x[i], None, minimum, None, y[i], None] for i in range(len(y))]
#         self.draw_sixtuples(sixtuples, marker = marker, positive_color = color, fill = fill, width = width, orientation = orientation, offset = offset, reset_ticks = reset_ticks, xside = xside, yside = yside, label = label)

#     def draw_multiple_bar(self, *args, marker = None, color = None, fill = None, width = None, orientation = None, minimum = None, offset = None, reset_ticks = None, xside = None, yside = None, labels = None):
#         x, Y = ut.set_multiple_bar_data(*args)
#         ly = len(Y)
#         width = default_monitor.bar_width if width is None else width
#         marker = [marker] * ly if marker is None or type(marker) != list else marker
#         color = [color] * ly if color is None else color
#         labels = [labels] * ly if labels is None else labels
#         width = width / ly if ly != 0 else 0
#         offset = ut.linspace(-1 / 2 + 1 / (2 * ly), 1 / 2 - 1 / (2 * ly), ly) if ly != 0 else []
#         for i in range(ly):
#             self.draw_bar(x, Y[i],
#                           marker = marker[i],
#                           color = color[i],
#                           fill = fill,
#                           width = width,
#                           orientation = orientation,
#                           minimum = minimum,
#                           offset = offset[i],
#                           xside = xside,
#                           yside = yside,
#                           label = labels[i],
#                           reset_ticks = reset_ticks)

#     def draw_stacked_bar(self, *args, marker = None, color = None, fill = None, width = None, orientation = None, minimum = None, offset = None, reset_ticks = None, xside = None, yside = None, labels = None):
#         x, Y = ut.set_multiple_bar_data(*args)
#         ly = len(Y)
#         marker = [marker] * ly if marker is None or type(marker) != list else marker
#         color = [color] * ly if color is None else color
#         labels = [label] * ly if labels is None else labels
#         Y = ut.transpose([ut.cumsum(el) for el in ut.transpose(Y)])
#         for i in range(ly - 1, -1, -1):
#             self.draw_bar(x, Y[i],
#                           xside = xside, 
#                           yside = yside,
#                           marker = marker[i],
#                           color = color[i],
#                           fill = fill,
#                           width = width,
#                           orientation = orientation,
#                           label = labels[i],
#                           minimum = minimum,
#                           reset_ticks = reset_ticks)

#     def draw_hist(self, data, bins = None, marker = None, color = None, fill = None, norm = None, width = None, orientation = None, minimum = None, xside = None, yside = None, label = None):
#         bins = default_monitor.hist_bins if bins is None else bins
#         norm = False if norm is None else norm
#         x, y = ut.hist_data(data, bins, norm)
#         self.draw_bar(x, y,
#                       xside = xside, 
#                       yside = yside,
#                       marker = marker,
#                       color = color,
#                       fill = fill,
#                       width = width,
#                       orientation = orientation,
#                       label = label,
#                       minimum = None,
#                       reset_ticks = False)

#     def draw_candlestick(self, dates, data, positive_color = None, negative_color = None, orientation = None, xside = None, yside = None, label = None):
#         l = len(dates); r = range(l)
#         positive_color = 'green' if positive_color is None else positive_color
#         negative_color = 'red' if negative_color is None else negative_color
#         sixtuples = [[dates[i], data["Low"][i], data["Open"][i], None, data["Close"][i], data["High"][i]] for i in r]
#         self.draw_sixtuples(sixtuples, marker = 'sd', positive_color = positive_color, negative_color = negative_color, fill = True, width = 0, orientation = orientation, offset = 0, reset_ticks = False, xside = xside, yside = yside, label = label)
#         #self.set_xticks(dates, x.labels, xside) if reset_ticks and orientation[0] == 'v' else self.set_yticks(x.numbers, x.labels, yside) if reset_ticks else None
        
#         # markers = ['sd', '│', '─'] #if markers is None else markers
#         # colors = colors if isinstance(colors, list) and len(colors, 2) else ['green', 'red']
#         # x = []; y = []; color = []
#         # Open = data["Open"]; Close = data["Close"]; High = data["High"]; Low = data["Low"]
#         # for i in range(ln):
#         #     d = dates[i]
#         #     o, c, h, l = Open[i], Close[i], High[i], Low[i]
#         #     color = colors[0] if c > o else colors[1]
#         #     m, M = min(o, c), max(o, c)
#         #     lab = label if i == 0 else None
#         #     if orientation in ['v', 'vertical']:
#         #         self.draw([d, d], [M, h], xside = xside, yside = yside, color = color, marker = markers[1], lines = True)
#         #         self.draw([d, d], [l, m], xside = xside, yside = yside, color = color, marker = markers[1], lines = True)
#         #         self.draw([d, d], [m, M], xside = xside, yside = yside, color = color, marker = markers[0], lines = True, label = lab)
#         #     elif orientation in ['h', 'horizontal']:
#         #         self.draw([M, h], [d, d], xside = xside, yside = yside, color = color, marker = markers[2], lines = True)
#         #         self.draw([l, m], [d, d], xside = xside, yside = yside, color = color, marker = markers[2], lines = True)
#         #         self.draw([m, M], [d, d], xside = xside, yside = yside, color = color, marker = markers[0], lines = True, label = lab)

#     # about marker??
#     def draw_box(self, *args, xside = None, yside = None, orientation = None, color = None, label = None, fill = None, width = None, minimum = None, offset = None, reset_ticks = None, quintuples = None):
#         quintuples = False if quintuples is None else quintuples
#         get_quintuples = lambda data: [ut.quantile(data, q) for q in [0, 0.25, 0.5, 0.75, 1]]
#         x, Y = ut.set_data(*args); l = len(x)
#         Y = Y if quintuples else list(map(get_quintuples, Y))
#         minimum = 0 if minimum is None else minimum 
#         sixtuples = [[x[i]] + Y[i] for i in range(l)]
#         self.draw_sixtuples(sixtuples, positive_color = color, fill = fill, width = width, orientation = orientation, offset = offset, reset_ticks = reset_ticks, xside = xside, yside = yside, label = label)


        
#         # x, y = ut.set_data(*args)
#         # fill = default_monitor.bar_fill if fill is None else fill
#         # width = default_monitor.bar_width if width is None else width
#         # width = 1 if width > 1 else 0 if width < 0 else width
#         # orientation = self.check_orientation(orientation, 1)
#         # minimum = 0 if minimum is None else minimum
#         # offset = 0 if offset is None else offset
#         # reset_ticks = True if reset_ticks is None else reset_ticks
#         # colors = ['green', 'red'] if colors is None else colors
#         # 

#         # x_string = any([type(el) == str for el in x]) # if x are strings
#         # l = len(x)
#         # xticks = range(1, l + 1) if x_string else x
#         # xlabels = x if x_string else map(str, x)
#         # x = xticks if x_string else x
#         # x = [el + offset for el in x]
#         # (self.set_xticks(xticks, xlabels, xside) if orientation[0] == 'v' else self.set_yticks(xticks, xlabels, yside)) if reset_ticks else None
#         # if quintuples:
#         #     # todo: check y is aligned.
#         #     _, _, _, _, _, c, xbar = ut.box(x, y, width, minimum)
#         #     q1, q2, q3, max_, min_ = [], [], [], [], []
#         #     for d in y:
#         #         max_.append(d[0])
#         #         q3.append(d[1])
#         #         q2.append(d[2])
#         #         q1.append(d[3])
#         #         min_.append(d[4])
#         # else:
#         #     q1, q2, q3, max_, min_, c, xbar = ut.box(x, y, width, minimum)
#         # markers = ['sd', '│', '─'] #if markers is None else markers
        
#         # for i in range(l):
#         #     lab = label if i == 0 else None
#         #     color = colors[0]
#         #     mcolor = colors[1]
#         #     d, l, h, m, E, M = c[i], min_[i], max_[i], q1[i], q2[i], q3[i]
#         #     Ew = (M - m) / 30
#         #     if orientation in ['v', 'vertical']:
#         #         self.draw([d, d], [M, h], xside = xside, yside = yside, color = color, marker = markers[1], lines = True)
#         #         self.draw([d, d], [l, m], xside = xside, yside = yside, color = color, marker = markers[1], lines = True)
#         #         self.draw_rectangle(xbar[i], [m, M], xside = xside, yside = yside,
#         #             lines = True, color = color, fill = fill, marker = markers[0], label = lab)
#         #         self.draw_rectangle(xbar[i], [E, E], xside = xside, yside = yside,
#         #             lines = True, color = mcolor, fill = fill, marker = markers[2])
#         #         #self.draw([d, d], [m, M], xside = xside, yside = yside, color = color, marker = markers[0], lines = True, label = lab)
#         #         #self.draw(xbar[i], [E, E], xside = xside, yside = yside, color = mcolor, marker = markers[0], lines = False)
#         #     elif orientation in ['h', 'horizontal']:
#         #         self.draw([M, h], [d, d], xside = xside, yside = yside, color = color, marker = markers[2], lines = True)
#         #         self.draw([l, m], [d, d], xside = xside, yside = yside, color = color, marker = markers[2], lines = True)
#         #         self.draw_rectangle([m, M], xbar[i], xside = xside, yside = yside,
#         #             lines = True, color = color, fill = fill, marker = markers[0], label = lab)
#         #         self.draw_rectangle([E, E], xbar[i], xside = xside, yside = yside,
#         #             lines = True, color = mcolor, fill = fill, marker = markers[1])
#         #         #self.draw([m, M], [d, d], xside = xside, yside = yside, color = color, marker = markers[0], lines = True, label = lab)
#         #         #self.draw([E, E], [d, d], xside = xside, yside = yside, color = 'red', marker = markers[0], lines = True)
        
# ##############################################
# ###########    Plotting Tools    #############
# ##############################################
        
#     def draw_error(self, *args, xerr = None, yerr = None, color = None, xside = None, yside = None, label = None):
#         x, y = ut.set_data(*args)
#         l = len(x)
#         xerr = [0] * l if xerr is None else xerr
#         yerr = [0] * l if yerr is None else yerr
#         for i in range(l):
#             col = self.color[-1][-1] if i > 0 else color
#             self.draw([x[i], x[i]], [y[i] - yerr[i] / 2, y[i] + yerr[i] / 2], xside = xside, yside = yside, marker = "│", color = col, lines = True)
#             col = self.color[-1][-1] if i == 0 else col
#             self.draw([x[i] - xerr[i] / 2, x[i] + xerr[i] / 2], [y[i], y[i]], xside = xside, yside = yside, marker = "─", color = col, lines = True)
#             self.draw([x[i]], [y[i]], xside = xside, yside = yside, marker = "┼", color = col, lines = True)

#     def draw_event_plot(self, data, marker = None, color = None, orientation = None, side = None):
#         x, y = data, [1.1] * len(data)
#         orientation = self.check_orientation(orientation, 1)
#         if orientation in ['v', 'vertical']:
#             self.draw(x, y, xside = side, marker = marker, color = color, fillx = True)
#             self.set_ylim(0, 1)
#             self.set_yfrequency(0)
#         else:
#             self.draw(y, x, yside = side, marker = marker, color = color, filly = True)
#             self.set_xlim(0, 1)
#             self.set_xfrequency(0)

#     def draw_vertical_line(self, coordinate, color = None, xside = None):
#         pos = self.xside_to_pos(xside)
#         self.vcoord[pos].append(coordinate)
#         color = self.ticks_color if color is None else color
#         self.vcolors[pos].append(self.check_color(color))

#     def draw_horizontal_line(self, coordinate, color = None, yside = None):
#         pos = self.xside_to_pos(yside)
#         self.hcoord[pos].append(coordinate)
#         color = self.ticks_color if color is None else color
#         self.hcolors[pos].append(self.check_color(color))

#     def draw_text(self, text, x, y, xside = None, yside = None, color = None, background = None, style = None, orientation = None, alignment = None):
#         orientation = self.check_orientation(orientation)
#         text = text if orientation is default_monitor.orientation[0] else text[::-1]
#         self.text.append(str(text))
#         self.tx.append(x)
#         self.ty.append(y) 
#         self.txside.append(self.correct_xside(xside))
#         self.tyside.append(self.correct_yside(yside))
#         color = self.next_color() if color is None or not ut.is_color(color) else color
#         background = self.canvas_color if background is None or not ut.is_color(background) else background
#         self.tfull.append(color)
#         self.tback.append(background)
#         self.tstyle.append(self.check_style(style))
#         alignment = self.check_alignment(alignment)
#         self.torien.append(orientation)
#         self.talign.append(alignment)

#     def draw_rectangle(self, x = None, y = None, marker = None, color = None, lines = None, fill = None, reset_lim = False, xside = None, yside = None, label = None):
#         x = [0, 1] if x is None or len(x) < 2 else x  
#         y = [0, 1] if y is None or len(y) < 2 else y  
#         xpos = self.xside_to_pos(xside)
#         ypos = self.yside_to_pos(yside)
#         lines = True if lines is None else lines
#         fill = False if fill is None else fill
#         xm = min(x); xM = max(x);
#         ym = min(y); yM = max(y);
#         dx = abs(xM - xm); dy = abs(yM - ym);
#         if reset_lim:
#             self.xlim[xpos] = [xm - 0.5 * dx, xM + 0.5 * dx]
#             self.ylim[xpos] = [ym - 0.5 * dy, yM + 0.5 * dy]
#         x, y = [xm, xm, xM, xM, xm], [ym, yM, yM, ym, ym]
#         self.draw(x, y,
#                   xside = xside, 
#                   yside = yside,
#                   lines = True if fill else lines,
#                   marker = marker,
#                   color = color,
#                   fillx = "internal" if fill else False,
#                   filly = False,
#                   label = label)

#     def draw_polygon(self, x = None, y = None,  radius = None, sides = None, marker = None, color = None, lines = None, fill = None, reset_lim = False, xside = None, yside = None, label = None):
#         x = 0 if x is None else x
#         y = 0 if y is None else y
#         radius = 1 if radius is None else abs(int(radius))
#         sides = 3 if sides is None else max(3, int(abs(sides)))
#         xpos = self.xside_to_pos(xside)
#         ypos = self.yside_to_pos(yside)
#         lines = True if lines is None else lines
#         fill = False if fill is None else fill
        
#         alpha = 2 * math.pi / sides
#         init = alpha / 2 + math.pi / 2 if sides % 2 == 0 else alpha / 4 * ((-1) ** (sides // 2))# * math.pi #- ((-1) ** (sides)) * alpha / 4
#         #init = 0 * init
#         get_point = lambda i: [x + math.cos(alpha * i + init) * radius, y + math.sin(alpha * i + init) * radius]
#         # the rounding is needed so that results like 9.9999 are rounded to 10 and display as same coordinate in the plot, otherwise the floor function will turn 9.999 into 9
#         points = [get_point(i) for i in range(sides + 1)]
#         if reset_lim:
#             self.xlim[xpos] = [x - 1.5 * radius, x + 1.5 * radius]
#             self.ylim[xpos] = [y - 1.5 * radius, y + 1.5 * radius]
#         self.draw(*ut.transpose(points),
#                   xside = xside, 
#                   yside = yside,
#                   lines = True if fill else lines,
#                   marker = marker,
#                   color = color,
#                   fillx = "internal" if fill else False,
#                   filly = False,
#                   label = label)
        
#     def draw_confusion_matrix(self, actual, predicted, color = None, style = None, labels = None):
#         color = default_monitor.cmatrix_color if color is None else self.check_color(color)
#         style = default_monitor.cmatrix_style if style is None else self.check_style(style)
        
#         L = len(actual)
#         n_labels = sorted(ut.no_duplicates(actual))
#         labels = n_labels if labels is None else list(labels)
#         l = len(n_labels)

#         get_sum = lambda a, p: sum([actual[i] == a and predicted[i] == p for i in range(L)])
#         cmatrix = [[get_sum(n_labels[r], n_labels[c]) for c in range(l)] for r in range(l)]
#         cm = ut.join(cmatrix); m, M, t = min(cm), max(cm), sum(cm)

#         lm = 253; lM = 80
#         to_255 = lambda l: round(lm + (lM - lm) * (l - m) / (M - m)) # l=m -> lm; l=M->lM
#         to_color = lambda l: tuple([to_255(l)] * 3)
#         to_text = lambda n: str(round(n, 2)) + ' - ' + str(round(100 * n / t, 2)) + '%'
#         for r in range(l):
#             for c in range(l):
#                 count = cmatrix[r][c]
#                 col = to_color(count)
#                 self.draw_rectangle([c - 0.5, c + 0.5], [r - 0.5, r + 0.5], color = col, fill = True)
#                 self.draw_text(to_text(count), c, r, color = color, background = col, style = style)

#         self.set_yreverse(True)
#         self.set_xticks(n_labels, labels)
#         self.set_yticks(n_labels, labels)
#         self.set_ticks_color(color); self.set_ticks_style(style);
#         self.set_axes_color('default'); self.set_canvas_color('default'); 
#         self.set_title('Confusion Matrix')
#         self.set_xlabel('Predicted')
#         self.set_ylabel('Actual')

#     def draw_indicator(self, value, label = None, color = None, style = None):
#         color = default_monitor.cmatrix_color if color is None else self.check_color(color)
#         style = default_monitor.cmatrix_style if style is None else self.check_style(style)

#         self.set_title(label)
#         self.set_ticks_color(color);
#         self.set_ticks_style(style);
#         self.set_axes_color('default')
#         self.set_canvas_color('default')
#         self.set_xfrequency(0)
#         self.set_yfrequency(0)

#         self.draw_text(str(value), 0, 0, color = color, style = style, alignment = 'center')

# ##############################################
# ##############    2D Plots    ################
# ############################################## 
    
#     def draw_matrix(self, matrix, marker = None, style = None, fast = False):
#         matrix = [l.copy() for l in matrix]
#         marker = [marker] if type(marker) != list else marker
#         marker = [self.check_marker("sd") if el in ut.join([None, ut.hd_symbols]) else self.check_marker(el) for el in marker]
#         style = ut.no_color if style is None else self.check_style(style)
#         cols, rows = ut.matrix_size(matrix)
#         rows = 0 if cols == 0 else rows
#         matrix = matrix if rows * cols != 0 and ut.is_rgb_color(matrix[0][0]) else ut.turn_gray(matrix)
#         marker = ut.repeat(marker, cols)
#         if not fast:
#             for r in range(rows):
#                 xyc = [(c, r, matrix[rows - 1 - r][c]) for c in range(cols)]
#                 x, y, color = ut.transpose(xyc, 3)
#                 self.draw(x, y, marker = marker, color = color, style = style)
#             self.set_canvas_color("black")
#             self.set_xlabel('column') 
#             self.set_ylabel('row')
#             xf, yf = min(self.xfrequency[0], cols), min(self.yfrequency[0], rows)
#             xt = ut.linspace(0, cols - 1, xf)
#             xl = ut.get_labels([el + 1 for el in xt])
#             yt = ut.linspace(0, rows - 1, yf)
#             yl = ut.get_labels([rows - el for el in yt])
#             self.set_xticks(xt, xl)
#             self.set_yticks(yt, yl)
#         else: # if fast
#             for r in range(rows):
#                 for c in range(cols):
#                     ansi = ut.colors_to_ansi(matrix[r][c], style, "black")
#                     matrix[r][c] = ansi + marker[c] + ut.ansi_end
#             self.matrix.canvas = '\n'.join([''.join(row) for row in matrix])
#             self.fast_plot = True

#     def draw_image(self, path, marker = None, style = None, fast = False, grayscale = False):
#         from PIL import Image        
#         path = ut.correct_path(path)
#         if not ut.is_file(path):
#             return
#         image = Image.open(path)
#         self._draw_image(image, marker = marker, style = style, grayscale = grayscale, fast = fast)
        
# ##############################################
# #######    Plotting Tools Utilities    #######
# ##############################################

#     def check_orientation(self, orientation = None, default_index = 0):
#         default = default_monitor.orientation
#         default_first_letter = [el[0] for el in default]
#         orientation = default[default_first_letter.index(orientation)] if orientation in default_first_letter else orientation
#         orientation = default[default_index] if orientation not in default else orientation
#         return orientation

#     def check_alignment(self, alignment = None):
#         default = default_monitor.alignment[0:-1]
#         default_first_letter = [el[0] for el in default]
#         alignment = default[default_first_letter.index(alignment)] if alignment in default_first_letter else alignment
#         alignment = default[1] if alignment not in default else alignment
#         return alignment

#     def _draw_image(self, image, marker = None, style = None, fast = False, grayscale = False):
#         from PIL import ImageOps
#         image = ImageOps.grayscale(image) if grayscale else image
#         image = image.convert('RGB')
#         size = ut.update_size(image.size, self.size)
#         image = image.resize(size, resample = True)
#         matrix = ut.image_to_matrix(image)
#         self.set_xfrequency(0); self.set_yfrequency(0);
#         self.draw_matrix(matrix, marker = marker, style = style, fast = fast)
#         self.set_xlabel(); self.set_ylabel()
