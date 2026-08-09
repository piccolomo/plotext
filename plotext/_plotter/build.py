# Build: renders the final plot matrix from signals, rulers, axes, labels, ticks, legend and corners

from plotext._primitives.matrix import matrix as matrix_class
from plotext._primitives.box import box_class
from plotext._plotter.frame.rulers import rulers_class
from plotext._signal.grid import grid as grid_class
from plotext._signal.points import points_class
from plotext._constants.numerical import binary
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

        # Upper Bar Height
        threshold = 0
        height = self._labels.upper_present()
        height *= self._parts.height() >= height + threshold
        threshold += height
        self._parts.upper_bar.set_height(height)

        # Lower Bar Height
        height = self._labels.lower_present()
        height *= self._parts.height() >= height + threshold
        threshold += height
        self._parts.lower_bar.set_height(height)

        # Lower Axis Height
        axis = self._axes.get(0, 0)
        height = axis.get_status()
        height *= self._parts.height() >= height + threshold
        threshold += height
        self._parts.lower_axis.set_height(height)

        # Upper Axis Height
        axis = self._axes.get(0, 1)
        height = axis.get_status()
        height *= self._parts.height() >= height + threshold
        threshold += height
        self._parts.upper_axis.set_height(height)

        # Lower Ticks Height
        ruler = irulers._get(0, 0)
        height = ruler._active_ticks()
        height *= self._parts.height() >= height + threshold
        threshold += height
        self._parts.lower_ticks.set_height(height)

        # Upper Ticks Height
        ruler = irulers._get(0, 1)
        height = ruler._active_ticks()
        height *= self._parts.height() >= threshold
        threshold += height
        self._parts.upper_ticks.set_height(height)

        # Left Axis Width
        threshold = 0
        axis = self._axes.get(1, 0)
        width = axis.get_status()
        width *= self._parts.width() >= width + threshold
        threshold += width
        self._parts.left_axis.set_width(width)

        # Right Axis Width
        axis = self._axes.get(1, 1)
        width = axis.get_status()
        width *= self._parts.width() >= width + threshold
        threshold += width
        self._parts.right_axis.set_width(width)

        # Left Ticks Width
        ruler = irulers._get(1, 0)
        width = ruler._get_ticks().get_labels_width()
        width *= self._parts.width() >= width + threshold
        threshold += width
        self._parts.left_ticks.set_width(width)

        # Right Ticks Width
        ruler = irulers._get(1, 1)
        width = ruler._get_ticks().get_labels_width()
        width *= self._parts.width() >= width + threshold
        threshold += width
        self._parts.right_ticks.set_width(width)

        # Canvas Size
        self._parts.update_canvas_size()
        width_canvas, height_canvas = self._parts.canvas.size()

        # Upper and Lower Widths

        #  Update Parts
        self._parts.update_widths()
        self._parts.update_positions()
        self._parts.update_corners()

        col_canvas, row_canvas = self._parts.canvas.position()

        self._stop_event("initialize build")

        # Build Matrix
        self._start_event("create matrix")
        matrix = matrix_class(self._parts.width(), self._parts.height(), self._canvas_pixel)
        grid = grid_class(width_canvas, height_canvas)
        self._stop_event("create matrix")

        # Rescale Rulers
        self._start_event("rescale rulers")
        irulers.update_grid_lines()
        irulers._rescale(width_canvas, height_canvas)
        grid_xpositions = irulers._get_grid_positions(0)
        grid_ypositions = irulers._get_grid_positions(1)
        self._stop_event("rescale rulers")

        # Render all registered lines (user-added + grid-derived), cells merge arms automatically; crossings produce ┼ via cell.merge()
        self._start_event("lines")
        irulers.draw_lines(matrix, self._parts.canvas)
        self._stop_event("lines")

        # add points to canvas
        if self._parts.canvas.has_size():

            self._start_event("signals")
            signals.draw(matrix, irulers, self._parts.canvas, self._canvas_pixel, grid)
            self._stop_event("signals")


        # Add upper bar labels and title
        if self._parts.upper_bar.has_size():
            self._start_event("upper bar")
            p = self._parts.upper_bar
            self._labels.draw_upper_bar(matrix, *p.position(), p.width())
            self._stop_event("upper bar")

        # Add lower bar labels
        if self._parts.lower_bar.has_size():
            self._start_event("lower bar")
            p = self._parts.lower_bar
            self._labels.draw_lower_bar(matrix, *p.position(), p.width())
            self._stop_event("lower bar")

        # Add upper ticks
        ticks = []
        if self._parts.upper_ticks.has_size():
            self._start_event("upper ticks")
            p = self._parts.upper_ticks
            ticks = irulers._get(0, 1).draw_ticks(matrix, *p.position(), p.width())
            self._stop_event("upper ticks")

        # Add upper axis
        if self._parts.upper_axis.has_size():
            self._start_event("upper axis")
            p = self._parts.upper_axis
            self._axes.get(0, 1).draw(matrix, *p.position(), p.width(), ticks, grid_xpositions,
                self._parts.left_ticks.width(), self._parts.right_ticks.width())
            self._stop_event("upper axis")

        # Add lower ticks
        ticks = []
        if self._parts.lower_ticks.has_size():
            self._start_event("lower ticks")
            p = self._parts.lower_ticks
            ticks = irulers._get(0, 0).draw_ticks(matrix, *p.position(), p.width())
            self._stop_event("lower ticks")

        # Add lower axis
        if self._parts.lower_axis.has_size():
            self._start_event("lower axis")
            p = self._parts.lower_axis
            self._axes.get(0, 0).draw(matrix, *p.position(), p.width(), ticks, grid_xpositions,
                self._parts.left_ticks.width(), self._parts.right_ticks.width())
            self._stop_event("lower axis")

        # Add Left Ticks
        ticks = []
        if self._parts.left_ticks.has_size():
            self._start_event("left ticks")
            p = self._parts.left_ticks
            ticks = irulers._get(1, 0).draw_ticks(matrix, *p.position(), *p.size(), 0)
            self._stop_event("left ticks")

        # Add Left Axis
        if self._parts.left_axis.has_size():
            self._start_event("left axis")
            p = self._parts.left_axis
            self._axes.get(1, 0).draw(matrix, *p.position(), p.height(), ticks, grid_ypositions)
            self._stop_event("left axis")

        # Add Right Ticks
        ticks = []
        if self._parts.right_ticks.has_size():
            self._start_event("right ticks")
            p = self._parts.right_ticks
            ticks = irulers._get(1, 1).draw_ticks(matrix, *p.position(), *p.size(), 1)
            self._stop_event("right ticks")

        # Add Right Axis
        if self._parts.right_axis.has_size():
            self._start_event("right axis")
            p = self._parts.right_axis
            self._axes.get(1, 1).draw(matrix, *p.position(), p.height(), ticks, grid_ypositions)
            self._stop_event("right axis")

        # Corners
        self._start_event("corners")
        corner_parts = [[self._parts.lower_left_corner, self._parts.lower_right_corner],
                        [self._parts.upper_left_corner, self._parts.upper_right_corner]]
        for h in binary:
            for v in binary:
                part = corner_parts[h][v]
                if part.has_size() and self._axes.get(0, h).get_status() and self._axes.get(1, v).get_status():
                    corner = corner_class(h, v)
                    axis = self._axes.get(0, corner._horizontal)
                    ticks_pixel = self._rulers._get(0, corner._horizontal)._get_pixel()
                    corner.draw(matrix, *part.position(), *part.size(), axis.pixel(), axis.get_style(), ticks_pixel)
        self._stop_event("corners")

        # Legend
        self._start_event("legend")
        self._legend.update(signals, irulers)
        if self._legend.is_active():
            self._legend.fix_background(self._canvas_pixel)
            self._legend.draw(matrix, irulers, self._parts.canvas, self._parts.legend)
        self._stop_event("legend")

        return matrix