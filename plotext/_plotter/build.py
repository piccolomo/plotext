# Build: renders the final plot matrix from signals, rulers, axes, labels, ticks, legend and corners

from plotext._primitives.matrix import matrix as matrix_class
from plotext._plotter.frame.ruler.rulers import rulers_class
from plotext._signal.map import points_map
from plotext._signal.points import points_class
from plotext._settings.constants.numerical import binary
from plotext._plotter.frame.corner import corner_class


# Build mixin providing the master matrix assembly routine for plot_class
class plot_build_class:

    # Build and return the full plot matrix
    def _get_plot_matrix(self):
        self._start_event("initialize build")

        #Fix Signal Background
        signals = self._signals._copy()

        # Clone Rulers
        irulers = self._rulers.copy()
        irulers._fix_pixels(self._canvas_pixel)
        irulers._get(1, 0)._invert_direction()
        irulers._get(1, 1)._invert_direction()

        # Update Rulers
        irulers._update_ticks_limits()
        irulers._update_signals_limits(self._signals)
        irulers._update_lines_limits()
        irulers._update_ticks()
        irulers._update_lines()

        # Upper Bar Height
        threshold = 0
        height = self._labels.upper_present()
        height *= self._parts.get_height() >= height + threshold
        threshold += height
        self._parts.upper_bar.set_height(height)

        # Lower Bar Height
        height = self._labels.lower_present()
        height *= self._parts.get_height() >= height + threshold
        threshold += height
        self._parts.lower_bar.set_height(height)

        # Lower Axis Height
        axis = self._axes.get(0, 0)
        height = axis.get_status()
        height *= self._parts.get_height() >= height + threshold
        threshold += height
        self._parts.lower_axis.set_height(height)

        # Upper Axis Height
        axis = self._axes.get(0, 1)
        height = axis.get_status()
        height *= self._parts.get_height() >= height + threshold
        threshold += height
        self._parts.upper_axis.set_height(height)

        # Lower Ticks Height
        ruler = irulers._get(0, 0)
        height = ruler._active_ticks()
        height *= self._parts.get_height() >= height + threshold
        threshold += height
        self._parts.lower_ticks.set_height(height)

        # Upper Ticks Height
        ruler = irulers._get(0, 1)
        height = ruler._active_ticks()
        height *= self._parts.get_height() >= threshold
        threshold += height
        self._parts.upper_ticks.set_height(height)

        # Left Axis Width
        threshold = 0
        axis = self._axes.get(1, 0)
        width = axis.get_status()
        width *= self._parts.get_width() >= width + threshold
        threshold += width
        self._parts.left_axis.set_width(width)

        # Right Axis Width
        axis = self._axes.get(1, 1)
        width = axis.get_status()
        width *= self._parts.get_width() >= width + threshold
        threshold += width
        self._parts.right_axis.set_width(width)

        # Left Ticks Width
        ruler = irulers._get(1, 0)
        width = ruler._get_ticks().get_labels_width()
        width *= self._parts.get_width() >= width + threshold
        threshold += width
        self._parts.left_ticks.set_width(width)

        # Right Ticks Width
        ruler = irulers._get(1, 1)
        width = ruler._get_ticks().get_labels_width()
        width *= self._parts.get_width() >= width + threshold
        threshold += width
        self._parts.right_ticks.set_width(width)

        # Canvas Size
        self._parts.update_canvas_size()
        width_canvas, height_canvas = self._parts.canvas.get_size()

        # Upper and Lower Widths

        #  Update Parts
        self._parts.update_widths()
        self._parts.update_positions()
        self._parts.update_corners()

        col_canvas, row_canvas = self._parts.canvas.get_position()

        self._stop_event("initialize build")

        # Build Matrix
        self._start_event("create matrix")
        matrix = matrix_class(self._parts.get_width(), self._parts.get_height(), self._canvas_pixel)
        map = points_map(width_canvas, height_canvas)
        self._stop_event("create matrix")

        # Rescale Rulers
        irulers._rescale(width_canvas, height_canvas)
        irulers._add_grid_lines()
        line_xpositions = irulers._get_line_positions(0)
        line_ypositions = irulers._get_line_positions(1)

        # Add Lines
        self._start_event("lines")
        for axis in binary:
            crossings = line_xpositions if axis else []
            for side in binary:
                ruler = irulers._get(axis, side)
                scale = ruler._get_scale()
                lines = ruler._get_lines()
                bins = width_canvas if axis else height_canvas
                for line in lines:
                    string = line.get_string(bins, not axis, crossings)
                    col, row = self._parts.canvas.get_position()
                    pos = line.get_position()
                    if axis == 0:
                        [matrix._set_pixelled_character(col + pos, row + r, char, line.get_pixel()) for r, char in enumerate(string)]
                    else:
                        [matrix._set_pixelled_character(col + c, row + pos, char, line.get_pixel()) for c, char in enumerate(string)]
        self._stop_event("lines")

        # add points to canvas
        if self._parts.canvas.has_size():

            col_offset, row_offset = self._parts.canvas.get_col(), self._parts.canvas.get_row()

            for signal in signals:

                self._start_event("rescaling signals")
                xside = signal._get_xside()
                yside = signal._get_yside()

                xruler = irulers._get(0, xside)
                yruler = irulers._get(1, yside)

                xlim = xruler._get_limits(direction = True)
                ylim = yruler._get_limits(direction = True)

                xdelta = xruler._get_delta()
                ydelta = yruler._get_delta()

                xscale = xruler._get_scale()
                yscale = yruler._get_scale()

                signal._log_x() if xscale == "log" else None
                signal._log_y() if yscale == "log" else None

                signal._rescale_x(xlim, width_canvas, xdelta)
                signal._rescale_y(ylim, height_canvas, ydelta)
                self._stop_event("rescaling signals")

                self._start_event("plot")
                signal._plot() if signal._get_lines() else None
                self._stop_event("plot")

                self._start_event("getting points")
                points = signal._get_points()
                points.select_in_matrix(width_canvas, height_canvas)
                points.squash(map)
                points.fix_background(self._canvas_pixel)
                points.add_offset(col_offset, row_offset)
                self._stop_event("getting points")

                self._start_event("insert points")
                matrix._insert_points(points)
                self._stop_event("insert points")


        # Add upper bar labels and title
        if self._parts.upper_bar.has_size():
            self._start_event("upper bar")
            part = matrix_class(self._parts.get_width(), 1, self._labels.get_pixel())
            part._insert_colorized_aligned(self._parts.get_width() // 2, 0, self._labels.get(0, 1), 0) if self._labels.get(0, 1) is not None else None
            title_centered = part._insert_colorized_aligned(self._parts.get_width() // 2, 0, self._labels.get_title(), 0) if self._labels.get_title() is not None else False
            None if title_centered else part._insert_colorized_aligned(0, 0, self._labels.get_title(), -1) if self._labels.get_title() is not None else None
            matrix._insert_matrix(*self._parts.upper_bar.get_position(), part)
            self._stop_event("upper bar")

        # Add lower bar labels
        if self._parts.lower_bar.has_size():
            self._start_event("lower bar")
            part = matrix_class(self._parts.get_width(), 1, self._labels.get_pixel())
            part._insert_colorized_aligned(0, 0, self._labels.get_y(0), -1) if self._labels.get(1, 0) is not None else None
            part._insert_colorized_aligned(self._parts.get_width() // 2, 0, self._labels.get(0, 0), 0) if self._labels.get_x(0) is not None else None
            part._insert_colorized_aligned(self._parts.get_width() - 1, 0, self._labels.get(1, 1), 1) if self._labels.get_y(1) is not None else None
            matrix._insert_matrix(*self._parts.lower_bar.get_position(), part)
            self._stop_event("lower bar")

        # Add upper ticks
        ticks = []
        if self._parts.upper_ticks.has_size():
            self._start_event("upper ticks")
            ruler = irulers._get(0, 1)
            part = self._parts.upper_ticks
            out = matrix_class(part.get_width(), 1, ruler._get_pixel())
            ticks = ruler._get_ticks_tuples()
            ticks_test = [out._insert_colorized_dynamically(c, 0, label) for c, label in ticks]
            ticks = [ticks[i][0] for i, tt in enumerate(ticks_test) if tt != -1]
            matrix._insert_matrix(*part.get_position(), out)
            self._stop_event("upper ticks")

        # Add upper axis
        if self._parts.upper_axis.has_size():
            self._start_event("upper axis")
            axis = self._axes.get(0, 1)
            width = self._parts.upper_axis.get_width()
            string = axis.get_string(width, ticks, line_xpositions)
            col, row = self._parts.upper_axis.get_position()
            [matrix._set_pixelled_character(col + c, row, char, axis.get_pixel()) for c, char in enumerate(string)]
            left_axis = matrix_class(self._parts.left_ticks.get_width(), 1, axis.get_pixel())
            matrix._insert_matrix(0, row, left_axis)
            right_axis = matrix_class(self._parts.right_ticks.get_width(), 1, axis.get_pixel())
            matrix._insert_matrix(self._parts.right_ticks.get_col(), row, right_axis)
            self._stop_event("upper axis")

        # Add lower ticks
        ticks = []
        if self._parts.lower_ticks.has_size():
            self._start_event("lower ticks")
            ruler = irulers._get(0, 0)
            part = self._parts.lower_ticks
            out = matrix_class(part.get_width(), 1, ruler._get_pixel())
            ticks = ruler._get_ticks_tuples()
            ticks_test = [out._insert_colorized_dynamically(c, 0, label) for c, label in ticks]
            ticks = [ticks[i][0] for i, tt in enumerate(ticks_test) if tt != -1]
            matrix._insert_matrix(*part.get_position(), out)
            self._stop_event("lower ticks")

        # Add lower axis
        if self._parts.lower_axis.has_size():
            self._start_event("lower axis")
            axis = self._axes.get(0, 0)
            width = self._parts.lower_axis.get_width()
            string = axis.get_string(width, ticks, line_xpositions)
            col, row = self._parts.lower_axis.get_position()
            [matrix._set_pixelled_character(col + c, row, char, axis.get_pixel()) for c, char in enumerate(string)]
            left_axis = matrix_class(self._parts.left_ticks.get_width(), 1, axis.get_pixel())
            matrix._insert_matrix(0, row, left_axis)
            right_axis = matrix_class(self._parts.right_ticks.get_width(), 1, axis.get_pixel())
            matrix._insert_matrix(self._parts.right_ticks.get_col(), row, right_axis)
            self._stop_event("lower axis")

        # Add Left Ticks
        ticks = []
        if self._parts.left_ticks.has_size():
            self._start_event("left ticks")
            offset = row_canvas
            ruler = irulers._get(1, 0)
            size = self._parts.left_ticks.get_size()
            part = matrix_class(*size, ruler._get_pixel())
            [ticks.append(row) if part._insert_colorized_aligned(size[0] - 1, row, label, 1) else None for row, label in ruler._get_ticks_tuples()]
            matrix._insert_matrix(*self._parts.left_ticks.get_position(), part)
            self._stop_event("left ticks")

        # Add Left Axis
        if self._parts.left_axis.has_size():
            self._start_event("left axis")
            axis = self._axes.get(1, 0)
            height = self._parts.left_axis.get_height()
            string = axis.get_string(height, ticks, line_ypositions)
            col, row = self._parts.left_axis.get_position()
            [matrix._set_pixelled_character(col, row + r, char, axis.get_pixel()) for r, char in enumerate(string)]
            self._stop_event("left axis")

        # Add Right Ticks
        ticks = []
        if self._parts.right_ticks.has_size():
            self._start_event("right ticks")
            offset = row_canvas
            ruler = irulers._get(1, 1)
            part = matrix_class(*self._parts.right_ticks.get_size(), ruler._get_pixel())
            [ticks.append(row) if part._insert_colorized_aligned(0, row, label, -1) else None for row, label in ruler._get_ticks_tuples()]
            matrix._insert_matrix(*self._parts.right_ticks.get_position(), part)
            self._stop_event("right ticks")

        # Add Right Axis
        if self._parts.right_axis.has_size():
            self._start_event("right axis")
            axis = self._axes.get(1, 1)
            height = self._parts.right_axis.get_height()
            string = axis.get_string(height, ticks, line_ypositions)
            col, row = self._parts.right_axis.get_position()
            [matrix._set_pixelled_character(col, row + r, char, axis.get_pixel()) for r, char in enumerate(string)]
            self._stop_event("right axis")


        # Legend
        self._start_event("legend")
        if self._legend.get_status():
            self._legend.update(signals)
            self._legend.fix_background(self._canvas_pixel)

            xruler = irulers._get(0, self._legend.get_xside())
            yruler = irulers._get(1, self._legend.get_yside())

            col = self._legend.get_absolute_position(0, xruler, width_canvas) + col_canvas
            row = self._legend.get_absolute_position(1, yruler, height_canvas) + row_canvas

            ha, va = self._legend.get_alignments()
            m = self._legend.get()
            matrix._insert_matrix_aligned(col, row, m, ha, va)

            self._parts.legend.set_position(col, row)
            self._parts.legend.set_size(*self._legend.get_size())
        self._stop_event("legend")

        # Corners
        self._start_event("corners")
        for h in binary:
            for v in binary:
                corner = corner_class(h, v)
                part = self._parts.lower_left_corner if corner.is_lower_left() else self._parts.upper_left_corner if corner.is_upper_left() else self._parts.lower_right_corner if corner.is_lower_right() else self._parts.upper_right_corner
                if part.has_size():
                    axis = self._axes.get(0, corner._horizontal)
                    axis_pixel = axis.get_pixel()
                    style = axis.get_style()
                    ticks_pixel = self._rulers._get(0, corner._horizontal)._get_pixel()
                    corner.set_pixels(axis_pixel, ticks_pixel).set_style(style)
                    size = part.get_size()
                    corner.set_size(*size)
                    matrix._insert_matrix(*part.get_position(), corner.get())
        self._stop_event("corners")

        return matrix