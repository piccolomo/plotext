from plotext._cimport import matrix_class, dots_class

from plotext._rulers import rulers_class


class plot_build_class:

    # Build and return the full plot matrix
    def get_plot_matrix(self):
        
        #Fix Signal Background
        signals = self.signals.copy().fix_background(self._canvas_pixel)

        # Clone Rulers 
        irulers = rulers_class()
        irulers.clone(self.rulers) 
        irulers.get(1, 0).invert_direction()
        irulers.get(1, 1).invert_direction()

        # Update Rulers 
        irulers.update_ticks_limits(self.signals) 
        irulers.update_lines_limits() 
        irulers.update_ticks() 
     
        # Upper Bar Height
        threshold = 0
        height = self.labels.upper_present()
        height *= self.parts.height >= height + threshold; 
        threshold += height
        self.parts.upper_bar.set_height(height)

        # Lower Bar Height
        height = self.labels.lower_present()
        height *= self.parts.height >= height + threshold; 
        threshold += height
        self.parts.lower_bar.set_height(height)

        # Lower Axis Height
        axis = self.axes.get(0, 0)
        height = axis.status; 
        height *= self.parts.height >= height + threshold; 
        threshold += height
        self.parts.lower_axis.set_height(height)

        # Upper Axis Height
        axis = self.axes.get(0, 1)
        height = axis.status; 
        height *= self.parts.height >= height + threshold; 
        threshold += height
        self.parts.upper_axis.set_height(height)

        # Lower Ticks Height
        ruler = irulers.get(0, 0)
        #ruler.update_real_limits(self.get_signal_limits(0, 0))
        height = ruler.is_active(); 
        height *= self.parts.height >= height + threshold; 
        threshold += height
        self.parts.lower_ticks.set_height(height)

        # Upper Ticks Height 
        ruler = irulers.get(0, 1) 
        height = ruler.is_active(); 
        height *= self.parts.height >= threshold; 
        threshold += height
        self.parts.upper_ticks.set_height(height)

        # Left Axis Width 
        threshold = 0 
        axis = self.axes.get(1, 0)
        width = axis.status; 
        width *= self.parts.width >= width + threshold; 
        threshold += width
        self.parts.left_axis.set_width(width)

        # Right Axis Width
        axis = self.axes.get(1, 1)
        width = axis.status; 
        width *= self.parts.width >= width + threshold; 
        threshold += width
        self.parts.right_axis.set_width(width)

        # Left Ticks Width
        ruler = irulers.get(1, 0)
        width = ruler.ticks.get_labels_width(); 
        width *= self.parts.width >= width + threshold; 
        threshold += width
        self.parts.left_ticks.set_width(width)

        # Right Ticks Width
        ruler = irulers.get(1, 1)
        width = ruler.ticks.get_labels_width(); 
        width *= self.parts.width >= width + threshold; 
        threshold += width
        self.parts.right_ticks.set_width(width)

        # Canvas Size 
        self.parts.update_canvas_size()
        width_canvas, height_canvas = self.parts.canvas.get_size()
        
        # Upper and Lower Widths
        self.parts.update_widths()

        # Part Positions
        self.parts.update_positions()
        col_canvas, row_canvas = self.parts.canvas.get_position()

        # Build Matrix
        matrix = matrix_class(self.parts.width, self.parts.height, self._canvas_pixel) 

        # add points to canvas
        if self.parts.canvas.has_size():
            
            for signal in signals: 
                dots = dots_class(self.signals.get_total_points())
                xside = signal.xside
                yside = signal.yside

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

                # signal.log()

                signal.rescale_x(xlim, width_canvas, xdelta) 
                signal.rescale_y(ylim, height_canvas, ydelta) 

                col_offset, row_offset = self.parts.canvas.col, self.parts.canvas.row
                signal.add_offset(col_offset, row_offset)

                signal.fill()

                [dots.add(point) for point in signal if 0 <= point.get_col() - col_offset < width_canvas and 0 <= point.get_row() - row_offset < height_canvas]

                matrix.insert_dots(dots)

      
        # Add upper bar labels and title  
        if self.parts.upper_bar.has_size(): 
            part = matrix_class(self.parts.width, 1) 
            part._insert_colorized_aligned(self.parts.width // 2, 0, self.labels.x[1], 0) if self.labels.x[1] is not None else None
            title_centered = part._insert_colorized_aligned(self.parts.width // 2, 0, self.labels.title, 0) if self.labels.title is not None else False
            None if title_centered else part._insert_colorized_aligned(0, 0, self.labels.title, -1) if self.labels.title is not None else None
            matrix._insert_matrix(*self.parts.upper_bar.get_position(), part)

        # Add lower bar labels
        if self.parts.lower_bar.has_size():
            part = matrix_class(self.parts.width, 1) 
            part._insert_colorized_aligned(0, 0, self.labels.y[0], -1) if self.labels.y[0] is not None else None
            part._insert_colorized_aligned(self.parts.width // 2, 0, self.labels.x[0], 0) if self.labels.x[0] is not None else None
            part._insert_colorized_aligned(self.parts.width - 1, 0, self.labels.y[1], 1) if self.labels.y[1] is not None else None
            matrix._insert_matrix(*self.parts.lower_bar.get_position(), part)

        # Add upper ticks
        ticks = []
        if self.parts.upper_ticks.has_size():
            ruler = irulers.get(0, 1)
            ruler.rescale(width_canvas) 
            part = matrix_class(self.parts.width, 1, ruler.pixel) 
            col = self.parts.upper_ticks.col
            ticks = [part._insert_colorized_dynamically(c + col, 0, label) for c, label in ruler.get()]
            matrix._insert_matrix(0, self.parts.upper_ticks.row, part)

        # Add upper axis
        if self.parts.upper_axis.has_size():
            axis = self.axes.get(0, 1)
            width = self.parts.upper_axis.width
            string = axis.get_string(width)
            col, row = self.parts.upper_axis.get_position()
            [matrix._set_pixelled_character(col + c, row, char, axis.pixel) for c, char in enumerate(string)]
            [matrix._set_character(c, row, axis.tick) for c in ticks if c != -1] if width > 2 else None

            left_axis = matrix_class(self.parts.left_ticks.width, 1, axis.pixel); matrix._insert_matrix(0, row, left_axis)
            right_axis = matrix_class(self.parts.right_ticks.width, 1, axis.pixel); matrix._insert_matrix(self.parts.right_ticks.col, row, right_axis)

        # Add lower ticks
        ticks = []
        if self.parts.lower_ticks.has_size():
            ruler = irulers.get(0, 0)
            ruler.rescale(width_canvas) 
            part = matrix_class(self.parts.width, 1, ruler.pixel) 
            col = self.parts.lower_ticks.col
            ticks = [part._insert_colorized_dynamically(c + col, 0, label) for c, label in ruler.get()]
            matrix._insert_matrix(0, self.parts.lower_ticks.row, part)

        # Add lower axis
        if self.parts.lower_axis.has_size():
            axis = self.axes.get(0, 0)
            width = self.parts.lower_axis.width
            string = axis.get_string(width)
            col, row = self.parts.lower_axis.get_position()
            [matrix._set_pixelled_character(col + c, row, char, axis.pixel) for c, char in enumerate(string)]
            [matrix._set_character(c, row, axis.tick) for c in ticks if c != -1] if width > 2 else None

            left_axis = matrix_class(self.parts.left_ticks.width, 1, axis.pixel); matrix._insert_matrix(0, row, left_axis)
            right_axis = matrix_class(self.parts.right_ticks.width, 1, axis.pixel); matrix._insert_matrix(self.parts.right_ticks.col, row, right_axis)

        # Add left ticks
        ticks = [] 
        if self.parts.left_ticks.has_size(): 
            offset = row_canvas 
            ruler = irulers.get(1, 0) 
            ruler.rescale(height_canvas)
            part = matrix_class(*self.parts.left_ticks.get_size(), ruler.pixel) 
            [ticks.append(row + offset) if part._insert_colorized_aligned(0, row, label, -1) else None for row, label in ruler.get()] 
            matrix._insert_matrix(*self.parts.left_ticks.get_position(), part)

        # Add left axis
        if self.parts.left_axis.has_size():
            axis = self.axes.get(1, 0)
            height = self.parts.left_axis.height
            string = axis.get_string(height)
            col, row = self.parts.left_axis.get_position() 
            [matrix._set_pixelled_character(col, row + r, char, axis.pixel) for r, char in enumerate(string)]
            [matrix._set_character(col, r, axis.tick) for r in ticks] #if self.left_axis.height > 2 else None

        # Add right ticks
        ticks = [] 
        if self.parts.right_ticks.has_size(): 
            offset = row_canvas 
            ruler = irulers.get(1, 1) 
            ruler.rescale(height_canvas)
            part = matrix_class(*self.parts.right_ticks.get_size(), ruler.pixel) 
            [ticks.append(row + offset) if part._insert_colorized_aligned(0, row, label, -1) else None for row, label in ruler.get()] 
            matrix._insert_matrix(*self.parts.right_ticks.get_position(), part)

        # Add right axis
        if self.parts.right_axis.has_size():
            axis = self.axes.get(1, 0)
            height = self.parts.right_axis.height
            string = axis.get_string(height)
            col, row = self.parts.right_axis.get_position() 
            [matrix._set_pixelled_character(col, row + r, char, axis.pixel) for r, char in enumerate(string)]
            [matrix._set_character(col, r, axis.tick) for r in ticks] #if self.right_axis.height > 2 else None


        # Update and insert legend if active
        #self._legend.clear_signals()
        #self._legend.update(self.signals)
        self._legend.fix_background(self._canvas_pixel)

        if self._legend.active: 
            xscaler = irulers.get(0, self._legend.xside)
            yscaler = irulers.get(1, self._legend.yside)

            xdirection = xscaler.get_direction()
            ydirection = yscaler.get_direction()

            col = self._legend.get_absolute_position(0, xscaler, width_canvas) + col_canvas
            row = self._legend.get_absolute_position(1, yscaler, height_canvas) + row_canvas

            ha, va = self._legend.get_alignments(); va *= -1
            m = self._legend.get()

            matrix._insert_matrix_aligned(col, row, m, ha, va)

            self.parts.legend.set_position(col, row)
            self.parts.legend.set_size(*self._legend.get_size())

        return matrix