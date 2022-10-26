import plotext._utility as ut
import math

# this file builds a class inherited by the monitor_class() in _monitor.py just because its only method - build_plot() - is very long and it is the core of plot building and it is written separately for clarity

class build_class():
    
    def build_plot(self): # it builds the plot given the external settings and internal settings collected in draw()

        # Initial Tools
        r2 = [0, 1]
        signals = len(self.x); Signals = list(range(signals))
        texts = len(self.text); Texts = list(range(texts))
        width, height = self.size
        ticks_colors = self.ticks_color, self.ticks_style

        # Find if Axes are used
        xside = [(self.default.xside[i] in self.xside + self.txside) or self.vcoord[i] != [] for i in r2]
        yside = [(self.default.yside[i] in self.yside + self.tyside) or self.hcoord[i] != [] for i in r2]

        # Remove Useless X and Y Ticks and Labels if axes are not used 
        self.xticks = [self.xticks[i] if xside[i] else None for i in r2]
        self.xlabels = [self.xlabels[i] if xside[i] else None for i in r2]

        self.yticks = [self.yticks[i] if yside[i] else None for i in r2]
        self.ylabels = [self.ylabels[i] if yside[i] else None for i in r2]

        # Remove Useless h and v user defined Lines if axes are not used
        self.hcoord = [self.hcoord[i] if yside[i] else [] for i in r2]
        self.vcoord = [self.vcoord[i] if xside[i] else [] for i in r2]
        self.hcolors = [self.hcolors[i] if yside[i] else [] for i in r2]
        self.vcolors = [self.vcolors[i] if xside[i] else [] for i in r2]

        # Apply Scale (linear or log) to the data
        xscale = [ut.get_first(self.xscale, self.xside[s] is self.default.xside[0]) for s in Signals] # the x scale for each signal 
        yscale = [ut.get_first(self.yscale, self.yside[s] is self.default.yside[0]) for s in Signals] # the y scale for each signal 
        self.x = [ut.apply_scale(self.x[s], xscale[s] is self.default.xscale[1]) for s in Signals] # apply optional log scale
        self.y = [ut.apply_scale(self.y[s], yscale[s] is self.default.yscale[1]) for s in Signals]

        # Apply Scale (linear or log) to the Axes Ticks
        self.xticks = [ut.apply_scale(self.xticks[i], self.xscale[i] is self.default.xscale[1]) if self.xticks[i] is not None else None for i in r2] # apply optional log scale
        self.yticks = [ut.apply_scale(self.yticks[i], self.yscale[i] is self.default.yscale[1]) if self.yticks[i] is not None else None  for i in r2] # apply optional log scale
        
        # Apply Scale (linear or log) to the user defined Lines
        self.hcoord = [ut.apply_scale(self.hcoord[i], self.yscale[i] is self.default.yscale[1]) for i in r2] # apply optional log scale
        self.vcoord = [ut.apply_scale(self.vcoord[i], self.xscale[i] is self.default.xscale[1]) for i in r2] # apply optional log scale

        # Apply Scale (linear or log) to the user defined Text
        txscale = [ut.get_first(self.xscale, self.txside[s] is self.default.xside[0]) for s in Texts] # the x scale for each text
        tyscale = [ut.get_first(self.yscale, self.tyside[s] is self.default.yside[0]) for s in Texts] # the y scale for each text 
        self.tx = [ut.apply_scale([self.tx[s]], txscale[s] is self.default.xscale[1])[0] for s in Texts] #if width_canvas * height_canvas > 0 else [] # apply optional log scale
        self.ty = [ut.apply_scale([self.ty[s]], tyscale[s] is self.default.yscale[1])[0] for s in Texts] #if width_canvas * height_canvas > 0 else [] # apply optional log scale
        tx = [[self.tx[s] for s in Texts if self.txside[s] is self.default.xside[i]] for i in r2] # text x coord for each axis
        ty = [[self.ty[s] for s in Texts if self.tyside[s] is self.default.yside[i]] for i in r2] # text x coofor each axis

        # Get X Axes Limits
        x = [ut.join([self.x[s] for s in Signals if self.xside[s] is side]) for side in self.default.xside] # total x data for each axis
        x = [x[i] + self.vcoord[i] + tx[i] for i in r2] # add v lines and text coords to calculate xlim
        xlim = [ut.get_lim(el) if len(el) > 0 else [None, None] for el in x]
        self.xlim = [ut.replace_none(self.xlim[i], xlim[i]) for i in r2]
        self.xlim = [self.xlim[i][:: self.xdirection[i]] for i in r2] # optionally reverse axes
        xlim = [self.xlim[0] if self.xside[s] == self.default.xside[0] else self.xlim[1] for s in Signals] # xlim for each signal

        # Get Y Axes Limits
        y = [ut.join([self.y[s] for s in Signals if self.yside[s] is side]) for side in self.default.yside]
        y = [y[i] + self.hcoord[i] + ty[i] for i in r2] # add h lines and text coords to calculate ylim
        ylim = list(map(ut.get_lim, y))
        self.ylim = [ut.replace_none(self.ylim[i], ylim[i]) for i in r2]
        self.ylim = [self.ylim[i][:: self.ydirection[i]] for i in r2] # optionally reverse axes
        ylim = [self.ylim[0] if self.yside[s] == self.default.yside[0] else self.ylim[1] for s in Signals] # ylim for each signal

        # Get Y Ticks and Labels
        yticks_to_set = [self.yticks[i] is None and yside[i] and len(y[i]) > 0 for i in r2]
        yticks = [ut.linspace(*self.ylim[i], self.yfrequency[i]) if yticks_to_set[i] else self.yticks[i] for i in r2] # the actual Y ticks
        yticks_rescaled = [ut.reverse_scale(yticks[i], self.yscale[i] is self.default.yscale[1]) for i in r2]
        
        ylabels = [self.date.times_to_string(yticks_rescaled[i]) if self.y_date[i] else ut.get_labels(yticks_rescaled[i]) if yticks_to_set[i] else self.ylabels[i] for i in r2]
        ylabels = [ut.add_extra_spaces(ylabels[i], self.default.yside[i]) if ylabels[i] is not None else None for i in r2]
        width_ylabels = [ut.max_length(el) if el is not None else 0 for el in ylabels]

        # Get X Ticks and Labels
        xticks_to_set = [self.xticks[i] is None and xside[i] and len(x[i]) > 0 for i in r2]
        xticks = [ut.linspace(*self.xlim[i], self.xfrequency[i]) if xticks_to_set[i] else self.xticks[i] for i in r2] # the actual X ticks
        xticks_rescaled = [ut.reverse_scale(xticks[i], self.xscale[i] is self.default.xscale[1]) for i in r2]
        xlabels = [self.date.times_to_string(xticks_rescaled[i]) if self.x_date[i] else ut.get_labels(xticks_rescaled[i]) if xticks_to_set[i] else self.xlabels[i] for i in r2]
        xlabels = [ut.add_extra_spaces(xlabels[i], self.default.xside[i]) if xticks_to_set[i] else self.xlabels[i] for i in r2]
        height_xlabels = [len(el) > 0 if el is not None else 0 for el in xlabels]

        # Canvas Dimensions (the area of data points)
        width_canvas = width - sum(self.yaxes) - sum(width_ylabels)
        height_highbar = any([el is not None for el in [self.title, self.xlabel[1]]])
        height_lowbar = any([el is not None for el in self.ylabel + [self.xlabel[0]]])
        height_canvas = height - sum(self.xaxes) - sum(height_xlabels) - height_highbar - height_lowbar
        
        # Canvas Offset
        col_start = width_ylabels[0] + self.yaxes[0]
        col_end = col_start + width_canvas
        row_start = height_lowbar + height_xlabels[0] + self.xaxes[0]
        row_end = row_start + height_canvas

        # Get Absolute X and Y Ticks
        cticks = [ut.get_matrix_data(xticks[i], self.xlim[i], width_canvas) if xticks[i] != None else [] for i in r2]
        rticks = [ut.get_matrix_data(yticks[i], self.ylim[i], height_canvas) if yticks[i] != None else [] for i in r2]

        # Get Absolute Coordinates for user defined Lines 
        hticks = [ut.get_matrix_data(self.hcoord[i], self.ylim[i], height_canvas) if None not in self.ylim[i] else [] for i in r2]
        vticks = [ut.get_matrix_data(self.vcoord[i], self.xlim[i], width_canvas) if None not in self.xlim[i] else [] for i in r2]

        # Get Absolute Coordinates for user defined Text
        txlim = [ut.get_first(self.xlim, self.txside[s] == self.default.xside[0]) for s in Texts] # xlim for each text
        tylim = [ut.get_first(self.ylim, self.tyside[s] == self.default.yside[0]) for s in Texts] # xlim for each text
        tcticks = [ut.get_matrix_data([self.tx[s]], txlim[s], width_canvas)[0] if width_canvas > 0 else 0 for s in Texts] #if width_canvas > 0 else [] # 
        trticks = [ut.get_matrix_data([self.ty[s]], tylim[s], height_canvas)[0] if height_canvas > 0 else 0  for s in Texts] #if height_canvas > 0 else [] #

        # Get effective number of User Lines
        hlines = [len(el) for el in hticks]; Hlines = [list(range(el)) for el in hlines] # number of user defined horizontal lines for each y axis (as list)
        vlines = [len(el) for el in vticks]; Vlines = [list(range(el)) for el in vlines] # number of user defined vertical lines for each x axis (as list)

        # Create Matrix of Markers
        self.matrix.set_size(width, height)
        self.matrix.set_axes_color(self.axes_color)
        self.matrix.set_canvas_area(col_start, col_end, row_start, row_end)
        self.matrix.set_canvas_color(self.canvas_color)
        self.matrix.set_matrices()

        # Add Title
        col_center = col_start + width_canvas // 2 # centered on the canvas not the entire plot
        col_title = col_center if self.xlabel[1] is None else 0
        row_title = row_end + self.xaxes[1] + height_xlabels[1]
        alignment_title = "center" if self.xlabel[1] is None else "left"
        self.matrix.add_horizontal_string(col_title, row_title, self.title, *ticks_colors, alignment = alignment_title, check_space = True) if self.title and height > 0 else None

        # Add Upper X Label
        self.matrix.add_horizontal_string(col_center, row_title, self.xlabel[1], *ticks_colors, alignment = "center", check_space = True) if self.xlabel[1] and height > 0 else None

        # Add Lower X Ticks
        row_xticks = min(row_start - self.xaxes[0] - 1, height - 1)
        cticks_inserted = [height > 0 and self.matrix.add_horizontal_string(col_start + cticks[0][i], row_xticks, xlabels[0][i], *ticks_colors, alignment = "dynamic", check_space = True) for i in range(len(cticks[0]))]
        cticks[0] = [cticks[0][i] for i in range(len(cticks[0])) if cticks_inserted[i]] # it updates the x ticks coordinates whatever x labels were inserted 

        # Add Upper X Ticks: the reason to do it here prematurely, is that the cticks[1] need to be re-evaluated for next step 
        row_xticks = row_end + self.xaxes[1]
        cticks_inserted = [height > 0 and self.matrix.add_horizontal_string(col_start + cticks[1][i], row_xticks, xlabels[1][i], *ticks_colors, alignment = "dynamic", check_space = True) for i in range(len(cticks[1]))]
        cticks[1] = [cticks[1][i] for i in range(len(cticks[1])) if cticks_inserted[i]] # it updates the x ticks coordinates whatever x labels were inserted 

        # Add Upper X Axes (from previous step)
        tick = lambda i: '┼' if (self.grid[1] and i in cticks[1]) else '┬' if (self.grid[1] and i in cticks[0] or i in ut.join(vticks)) else '┴' if i in cticks[1] else '─'
        xaxis = [tick(i) for i in range(width_canvas)]
        self.matrix.add_horizontal_string(col_start, row_end, xaxis, self.ticks_color) if self.xaxes[0] and height_canvas >= -1 else None   

        # Add Left Y Ticks
        [self.matrix.add_horizontal_string(0, rticks[0][i] + row_start, ylabels[0][i], *ticks_colors) for i in range(len(rticks[0]))] if width >= width_ylabels[0] else None
        
        # Add Left Y Axis
        tick = lambda i: '┼' if (self.grid[0] and i in rticks[0]) else '├' if (self.grid[0] and i in rticks[1] or i in ut.join(hticks)) else '┤' if i in rticks[0] else '│'
        yaxis = [tick(i) for i in range(height_canvas)]
        col_yaxis = width_ylabels[0]
        self.matrix.add_vertical_string(col_yaxis, row_start, yaxis, self.ticks_color) if self.yaxes[0] and width >= sum(width_ylabels) + 1 else None

        # Add Right Y Axis
        tick = lambda i: '┼' if (self.grid[0] and i in rticks[1]) else '┤' if (self.grid[0] and i in rticks[0] or i in ut.join(hticks)) else '├' if i in rticks[1] else '│'
        yaxis = [tick(i) for i in range(height_canvas)]
        self.matrix.add_vertical_string(col_end, row_start, yaxis, self.ticks_color) if self.yaxes[1] and width >= sum(width_ylabels) + self.yaxes[0] + 1 else None

        # Add Right Y Ticks
        [self.matrix.add_horizontal_string(col_end + 1, rticks[1][i] + row_start, ylabels[1][i], *ticks_colors) for i in range(len(rticks[1]))] if width >= sum(width_ylabels) + 1 else None

        # Add Frame 4 Corners if necessary
        canvas_test = height_canvas >= 0 and width_canvas >= 0
        self.matrix.insert_element(col_start - 1, row_start - 1, '└', self.ticks_color) if self.xaxes[0] and self.yaxes[0] and canvas_test else None
        self.matrix.insert_element(col_end, row_start - 1, '┘', self.ticks_color) if self.xaxes[0] and self.yaxes[1] and canvas_test else None
        self.matrix.insert_element(col_start - 1, row_end, '┌', self.ticks_color) if self.xaxes[1] and self.yaxes[0] and canvas_test else None
        self.matrix.insert_element(col_end, row_end, '┐', self.ticks_color) if self.xaxes[1] and self.yaxes[1] and canvas_test else None

        # Add Lower X Axes (from previous step)
        tick = lambda i: '┼' if (self.grid[1] and i in cticks[0]) else '┴' if (self.grid[1] and i in cticks[1] or i in ut.join(vticks)) else '┬' if i in cticks[0] else '─'
        xaxis = [tick(i) for i in range(width_canvas)]
        self.matrix.add_horizontal_string(col_start, row_start - 1, xaxis, self.ticks_color) if self.xaxes[0] and height_canvas >= -1 else None

        # Add Left Y Label
        self.matrix.add_horizontal_string(0, 0, self.ylabel[0], *ticks_colors, check_space = True) if self.ylabel[0] and height > 0 else None
        
        # Add Right Y Label 
        self.matrix.add_horizontal_string(width - 1, 0, self.ylabel[1], *ticks_colors, check_space = True, alignment = "right") if self.ylabel[1] and height > 0 else None

        # Add Lower X Label 
        self.matrix.add_horizontal_string(col_center, 0, self.xlabel[0], *ticks_colors, alignment = "center", check_space = True) if self.xlabel[0] and height > 0 else None

        # Add Grid Lines
        hline = '─' * width_canvas
        [self.matrix.add_horizontal_string(0 + col_start, row + row_start, hline, self.ticks_color) for row in ut.join(rticks) if self.grid[0]]
        vline = '│' * height_canvas
        [self.matrix.add_vertical_string(col + col_start, 0 + row_start, vline, self.ticks_color)  for col in ut.join(cticks) if self.grid[1]]
        [self.matrix.insert_element(col + col_start, row + row_start, '┼') for row in ut.join(rticks) for col in ut.join(cticks) if all(self.grid)] # deals with the crossing between grids
        
        # Add user defined Lines
        [[self.matrix.add_horizontal_string(col_start, hticks[i][l] + row_start, hline, self.hcolors[i][l]) for l in Hlines[i]] for i in r2]
        [[self.matrix.add_vertical_string(vticks[i][l] + col_start, 0 + row_start, vline, self.vcolors[i][l]) for l in Vlines[i]] for i in r2]
        [[[self.matrix.insert_element(col + col_start, hticks[i][l] + row_start, '┼', self.hcolors[i][l]) for l in Hlines[i]] for i in r2] for col in ut.join(cticks) if self.grid[1]] # deals with the crossing between h lines and v grids
        [[[self.matrix.insert_element(vticks[i][l] + col_start, row + row_start, '┼', self.vcolors[i][l]) for l in Vlines[i]] for i in r2] for row in ut.join(rticks) if self.grid[0]] # deals with the crossing between v lines and h grids
        [[[[self.matrix.insert_element(col_start + vticks[iv][lv], hticks[i][l] + row_start, '┼', self.hcolors[i][l]) for l in Hlines[i]] for i in r2] for lv in Vlines[iv]] for iv in r2] # deals with the crossing between h and v lines

        # Expand Canvas to accommodate HD markers
        xf = [max([ut.marker_factor(el, 2, 2, 2) for el in self.marker[s]], default = 1) for s in Signals]
        yf = [max([ut.marker_factor(el, 2, 3, 4) for el in self.marker[s]], default = 1) for s in Signals]
        width_expanded = [width_canvas * el for el in xf]
        height_expanded = [height_canvas * el for el in yf]

        # Get Relative Data to Be Plotted on Matrix
        test_canvas = [width_expanded[s] * width_expanded[s] for s in Signals]
        x = [ut.get_matrix_data(self.x[s], xlim[s], width_expanded[s]) if test_canvas[s] else [] for s in Signals]
        y = [ut.get_matrix_data(self.y[s], ylim[s], height_expanded[s]) if test_canvas[s] else []  for s in Signals]
        m, c, st = self.marker, self.color, self.style


        # Add Lines between Data Points
        x, y, m, c, st = ut.transpose([ut.get_lines(x[s], y[s], m[s], c[s], st[s]) if self.lines[s] else (x[s], y[s], m[s], c[s], st[s]) for s in Signals], 5)

        # Fillx
        #x, y, m, c, st = ut.transpose([ut.brush(x[s], y[s], m[s], c[s], st[s]) for s in Signals], 5)
        level = [ut.get_fill_level(self.fillx[s], ylim[s], height_expanded[s]) for s in Signals]
        x, y, m, c, st = ut.transpose([ut.fill_data(x[s], y[s], level[s], m[s], c[s], st[s]) if self.fillx[s] is not False else (x[s], y[s], m[s], c[s], st[s]) for s in Signals], 5)
        
        # Filly
        #x, y, m, c, st = ut.transpose([ut.brush(x[s], y[s], m[s], c[s], st[s]) for s in Signals], 5)
        level = [ut.get_fill_level(self.filly[s], xlim[s], width_expanded[s]) for s in Signals]
        y, x, m, c, st = ut.transpose([ut.fill_data(y[s], x[s], level[s], m[s], c[s], st[s]) if self.filly[s] is not False else (y[s], x[s], m[s], c[s], st[s]) for s in Signals], 5)

        # Get Actual HD Markers
        x, y, m, c, st = ut.transpose([ut.brush(x[s], y[s], m[s], c[s], st[s]) for s in Signals], 5)
        xf = [[ut.marker_factor(el, 2, 2, 2) for el in m[s]] for s in Signals]
        yf = [[ut.marker_factor(el, 2, 3, 4) for el in m[s]] for s in Signals]
        test = [max(xf[s], default = 1) * max(yf[s], default = 1) != 1 for s in Signals]
        x, y, mxy = ut.transpose([ut.hd_group(x[s], y[s], xf[s], yf[s]) if test[s] else (x[s], y[s], []) for s in Signals], 3)
        m = [[ut.get_hd_marker(mxy[s][i]) if m[s][i] in ut.hd_symbols else m[s][i] for i in range(len(x[s]))] for s in Signals]

        # Add Data to Canvas
        x, y, m, c, st = ut.transpose([ut.remove_outsiders(x[s], y[s], width_canvas, height_canvas, m[s], c[s], st[s]) for s in Signals], 5)

        x, y, m, c, st = ut.transpose([ut.brush(x[s], y[s], m[s], c[s], st[s]) for s in Signals], 5)
        [[self.matrix.insert_element(x[s][i] + col_start, y[s][i] + row_start, m[s][i], c[s][i], st[s][i]) for i in range(len(x[s]))] for s in Signals]

        # Legend Utilities
        labelled = lambda s: self.label[s] is not None
        labels = [ut.space + self.label[s] + ut.space for s in Signals if labelled(s)]; l = len(labels); L = ut.max_length(labels)
        labels = [el + ut.space * (L - len(el)) for el in labels]

        # Add Legend Side Symbols
        side = [ut.space + ut.side_symbols[(self.xside[s], self.yside[s])] for s in Signals if labelled(s)]
        side_test = not (ut.no_duplicates(side) == [' L']) and not l == 1; S = 2 if side_test else 0;
        legend_test = width_canvas >= S + 3 + L and height_canvas >= len(labels)
        [self.matrix.add_horizontal_string(col_start, row_end - 1 - s, side[s], self.ticks_color, self.ticks_style) for s in range(l)] if legend_test and side_test else None

        # Add Legend Markers
        take_3 = lambda data: (data[ : 3] * 3)[ : 3]
        marker = [take_3(self.marker[s]) for s in Signals if labelled(s)]
        replace_hd_marker = lambda marker: ut.hd_symbols[marker] if marker in ut.hd_symbols else marker
        marker = [[ut.space] + list(map(replace_hd_marker, el)) for el in marker]
        color =  [[ut.no_color] + take_3(c[s]) for s in Signals if labelled(s)]
        style =  [[ut.no_color] + take_3(st[s]) for s in Signals if labelled(s)]
        [[self.matrix.insert_element(col_start + S + i, row_end - 1 - s, marker[s][i], color[s][i], style[s][i]) for i in range(3)] for s in range(l)] if legend_test else None
        [self.matrix.add_horizontal_string(col_start + S + 3, row_end - 1 - s, labels[s], self.ticks_color, self.ticks_style) for s in range(l)] if legend_test else None

        # Add Text to Canvas
        [self.matrix.add_multiple_horizontal_strings(col_start + tcticks[s], row_start + trticks[s], self.text[s], self.tfull[s], self.tstyle[s], self.tback[s], self.talign[s], False, True) for s in Texts if self.torien[s] is self.default.orientation[0]] 
        [self.matrix.add_multiple_vertical_strings(col_start + tcticks[s], row_start + trticks[s], self.text[s], self.tfull[s], self.tstyle[s], self.tback[s], self.talign[s], True) for s in Texts if self.torien[s] is self.default.orientation[1]]




