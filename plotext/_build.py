from plotext._matrix import matrix as matrix_class
from plotext._dots import dots_class
from plotext._rulers import rulers_class
from plotext._points_map import points_map
from plotext._points import points_class


class plot_build_class:

    # Build and return the full plot matrix
    def _get_plot_matrix(self):
        
        self._start_event("initialize build")

        #Fix Signal Background
        signals = self._signals.copy().fix_background(self._canvas_pixel)

        # Clone Rulers 
        irulers = rulers_class()
        irulers.clone(self._rulers) 
        irulers.get(1, 0).invert_direction()
        irulers.get(1, 1).invert_direction()

        # Update Rulers 
        irulers.update_ticks_limits(self._signals) 
        irulers.update_lines_limits() 
        irulers.update_ticks() 

        # Upper Bar Height
        threshold = 0
        height = self._labels.upper_present()
        height *= self._parts.height >= height + threshold; 
        threshold += height
        self._parts.upper_bar.set_height(height)

        # Lower Bar Height
        height = self._labels.lower_present()
        height *= self._parts.height >= height + threshold; 
        threshold += height
        self._parts.lower_bar.set_height(height)

        # Lower Axis Height
        axis = self._axes.get(0, 0)
        height = axis.status; 
        height *= self._parts.height >= height + threshold; 
        threshold += height
        self._parts.lower_axis.set_height(height)

        # Upper Axis Height
        axis = self._axes.get(0, 1)
        height = axis.status; 
        height *= self._parts.height >= height + threshold; 
        threshold += height
        self._parts.upper_axis.set_height(height)

        # Lower Ticks Height
        ruler = irulers.get(0, 0)
        #ruler.update_real_limits(self.get_signal_limits(0, 0))
        height = ruler.is_active(); 
        height *= self._parts.height >= height + threshold; 
        threshold += height
        self._parts.lower_ticks.set_height(height)

        # Upper Ticks Height 
        ruler = irulers.get(0, 1) 
        height = ruler.is_active(); 
        height *= self._parts.height >= threshold; 
        threshold += height
        self._parts.upper_ticks.set_height(height)

        # Left Axis Width 
        threshold = 0 
        axis = self._axes.get(1, 0)
        width = axis.status; 
        width *= self._parts.width >= width + threshold; 
        threshold += width
        self._parts.left_axis.set_width(width)

        # Right Axis Width
        axis = self._axes.get(1, 1)
        width = axis.status; 
        width *= self._parts.width >= width + threshold; 
        threshold += width
        self._parts.right_axis.set_width(width)

        # Left Ticks Width
        ruler = irulers.get(1, 0)
        width = ruler.ticks.get_labels_width(); 
        width *= self._parts.width >= width + threshold; 
        threshold += width
        self._parts.left_ticks.set_width(width)

        # Right Ticks Width
        ruler = irulers.get(1, 1)
        width = ruler.ticks.get_labels_width(); 
        width *= self._parts.width >= width + threshold; 
        threshold += width
        self._parts.right_ticks.set_width(width)

        # Canvas Size 
        self._parts.update_canvas_size()
        width_canvas, height_canvas = self._parts.canvas.get_size()
        
        # Upper and Lower Widths
        self._parts.update_widths()

        # Part Positions
        self._parts.update_positions()
        col_canvas, row_canvas = self._parts.canvas.get_position()

        self._stop_event("initialize build")

        
        # Build Matrix
        self._start_event("create matrix")
        matrix = matrix_class(self._parts.width, self._parts.height, self._canvas_pixel) 
        self._stop_event("create matrix")

        # add points to canvas
        if self._parts.canvas.has_size():
            self._start_event("rescaling signals")
            col_offset, row_offset = self._parts.canvas.col, self._parts.canvas.row

            for signal in signals: 
                xside = signal.get_xside()
                yside = signal.get_yside()

                xruler = irulers.get(0, xside) 
                yruler = irulers.get(1, yside) 

                xlim = xruler.limits.get(scaled = True, direction = True) 
                ylim = yruler.limits.get(scaled = True, direction = True) 

                xdelta = xruler.limits.get_delta()
                ydelta = yruler.limits.get_delta()

                xscale = xruler.limits.get_scale()
                yscale = yruler.limits.get_scale()

                signal.log_x() if xscale == "log" else None 
                signal.log_y() if yscale == "log" else None 

                signal.rescale_x(xlim, width_canvas, xdelta) 
                signal.rescale_y(ylim, height_canvas, ydelta) 

            self._stop_event("rescaling signals")

            self._start_event("plot")
            [signal.plot() for signal in signals if signal._plot] 
            self._stop_event("plot")

            self._start_event("squash")
            map = points_map(width_canvas, height_canvas)
            [signal.squash(map) for signal in signals] # if signals.get_total_points() > 1000 else None
            self._stop_event("squash")

            self._start_event("adding points to canvas")
            [signal.add_offset(col_offset, row_offset) for signal in signals] 
            [matrix._insert_signal(signal) for signal in signals] 
            self._stop_event("adding points to canvas")

              
        # Add upper bar labels and title  
        if self._parts.upper_bar.has_size(): 
            self._start_event("upper bar") 
            part = matrix_class(self._parts.width, 1, self._labels.pixel) 
            part._insert_colorized_aligned(self._parts.width // 2, 0, self._labels.x[1], 0) if self._labels.x[1] is not None else None
            title_centered = part._insert_colorized_aligned(self._parts.width // 2, 0, self._labels.title, 0) if self._labels.title is not None else False
            None if title_centered else part._insert_colorized_aligned(0, 0, self._labels.title, -1) if self._labels.title is not None else None
            matrix._insert_matrix(*self._parts.upper_bar.get_position(), part)
            self._stop_event("upper bar")


        # Add lower bar labels
        if self._parts.lower_bar.has_size():
            self._start_event("lower bar")
            part = matrix_class(self._parts.width, 1, self._labels.pixel) 
            part._insert_colorized_aligned(0, 0, self._labels.y[0], -1) if self._labels.y[0] is not None else None
            part._insert_colorized_aligned(self._parts.width // 2, 0, self._labels.x[0], 0) if self._labels.x[0] is not None else None
            part._insert_colorized_aligned(self._parts.width - 1, 0, self._labels.y[1], 1) if self._labels.y[1] is not None else None
            matrix._insert_matrix(*self._parts.lower_bar.get_position(), part)
            self._stop_event("lower bar")
        
        # Add upper ticks
        ticks = []
        if self._parts.upper_ticks.has_size():
            self._start_event("lower bar")
            ruler = irulers.get(0, 1)
            ruler.rescale(width_canvas) 
            part = matrix_class(self._parts.width, 1, ruler.pixel) 
            col = self._parts.upper_ticks.col
            ticks = [part._insert_colorized_dynamically(c + col, 0, label) for c, label in ruler.get()]
            matrix._insert_matrix(0, self._parts.upper_ticks.row, part)
            self._stop_event("lower bar")

        # Add upper axis
        if self._parts.upper_axis.has_size():
            self._start_event("upper axis")
            axis = self._axes.get(0, 1)
            width = self._parts.upper_axis.width
            string = axis.get_string(width)
            col, row = self._parts.upper_axis.get_position()
            [matrix._set_pixelled_character(col + c, row, char, axis.pixel) for c, char in enumerate(string)]
            [matrix._set_character(c, row, axis.tick) for c in ticks if c != -1] if width > 2 else None
            left_axis = matrix_class(self._parts.left_ticks.width, 1, axis.pixel); matrix._insert_matrix(0, row, left_axis)
            right_axis = matrix_class(self._parts.right_ticks.width, 1, axis.pixel); matrix._insert_matrix(self._parts.right_ticks.col, row, right_axis)
            self._stop_event("upper axis")

        # Add lower ticks
        ticks = []
        if self._parts.lower_ticks.has_size():
            self._start_event("lower ticks")
            ruler = irulers.get(0, 0)
            ruler.rescale(width_canvas) 
            part = matrix_class(self._parts.width, 1, ruler.pixel) 
            col = self._parts.lower_ticks.col
            ticks = [part._insert_colorized_dynamically(c + col, 0, label) for c, label in ruler.get()]
            matrix._insert_matrix(0, self._parts.lower_ticks.row, part)
            self._stop_event("lower ticks")

        # Add lower axis
        if self._parts.lower_axis.has_size():
            self._start_event("lower axis")
            axis = self._axes.get(0, 0)
            width = self._parts.lower_axis.width
            string = axis.get_string(width)
            col, row = self._parts.lower_axis.get_position()
            [matrix._set_pixelled_character(col + c, row, char, axis.pixel) for c, char in enumerate(string)]
            [matrix._set_character(c, row, axis.tick) for c in ticks if c != -1] if width > 2 else None
            left_axis = matrix_class(self._parts.left_ticks.width, 1, axis.pixel); matrix._insert_matrix(0, row, left_axis)
            right_axis = matrix_class(self._parts.right_ticks.width, 1, axis.pixel); matrix._insert_matrix(self._parts.right_ticks.col, row, right_axis)
            self._stop_event("lower axis")

        # Add left ticks
        ticks = [] 
        if self._parts.left_ticks.has_size(): 
            self._start_event("left ticks")
            offset = row_canvas 
            ruler = irulers.get(1, 0) 
            ruler.rescale(height_canvas)
            part = matrix_class(*self._parts.left_ticks.get_size(), ruler.pixel) 
            [ticks.append(row + offset) if part._insert_colorized_aligned(0, row, label, -1) else None for row, label in ruler.get()] 
            matrix._insert_matrix(*self._parts.left_ticks.get_position(), part)
            self._stop_event("left ticks")

        # Add left axis
        if self._parts.left_axis.has_size():
            self._start_event("left axis")
            axis = self._axes.get(1, 0)
            height = self._parts.left_axis.height
            string = axis.get_string(height)
            col, row = self._parts.left_axis.get_position() 
            [matrix._set_pixelled_character(col, row + r, char, axis.pixel) for r, char in enumerate(string)]
            [matrix._set_character(col, r, axis.tick) for r in ticks] #if self._left_axis.height > 2 else None
            self._stop_event("left axis")

        # Add right ticks
        ticks = [] 
        if self._parts.right_ticks.has_size(): 
            self._start_event("right ticks")
            offset = row_canvas 
            ruler = irulers.get(1, 1) 
            ruler.rescale(height_canvas)
            part = matrix_class(*self._parts.right_ticks.get_size(), ruler.pixel) 
            [ticks.append(row + offset) if part._insert_colorized_aligned(0, row, label, -1) else None for row, label in ruler.get()] 
            matrix._insert_matrix(*self._parts.right_ticks.get_position(), part)
            self._stop_event("right ticks")

        # Add right axis
        if self._parts.right_axis.has_size():
            self._start_event("right axis")
            axis = self._axes.get(1, 1)
            height = self._parts.right_axis.height
            string = axis.get_string(height)
            col, row = self._parts.right_axis.get_position() 
            [matrix._set_pixelled_character(col, row + r, char, axis.pixel) for r, char in enumerate(string)]
            [matrix._set_character(col, r, axis.tick) for r in ticks] #if self._right_axis.height > 2 else None
            self._stop_event("right axis")

        # Legend


        if self._legend.active: 
            self._start_event("legend") 

            self._legend.update(signals)

            self._legend.fix_background(self._canvas_pixel)

            xruler = irulers.get(0, self._legend.xside) 
            yruler = irulers.get(1, self._legend.yside) 

            col = self._legend.get_absolute_position(0, xruler, width_canvas) + col_canvas 
            row = self._legend.get_absolute_position(1, yruler, height_canvas) + row_canvas 

            ha, va = self._legend.get_alignments() 
            m = self._legend.get() 
            matrix._insert_matrix_aligned(col, row, m, ha, va) 

            self._parts.legend.set_position(col, row) 
            self._parts.legend.set_size(*self._legend.get_size()) 
            self._stop_event("legend")

        return matrix