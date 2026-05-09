# Parts container: owns the named regions (bars, corners, axes, ticks, canvas, legend) that make up a plot layout

from plotext._plotter.utils.part import part_class as part


# Layout container for all named plot regions, with sizing, positioning and corner updates
class parts_class:
    # Initialize all parts with default size
    def __init__(self):
        # Upper parts
        self.upper_bar = part('upper bar')

        self.upper_left_corner = part('upper left corner')
        self.upper_ticks = part('upper ticks')
        self.upper_axis = part('upper axis')
        self.upper_right_corner = part('upper right corner')

        # Left parts
        self.left_ticks = part('left ticks')
        self.left_axis = part('left axis')

        # Central parts
        self.canvas = part('canvas')
        self.legend = part('legend')

        # Right parts
        self.right_axis = part('right axis')
        self.right_ticks = part('right ticks')

        # Lower parts
        self.lower_left_corner = part('lower left corner')
        self.lower_axis = part('lower axis')
        self.lower_ticks = part('lower ticks')
        self.lower_right_corner = part('lower right corner')

        self.lower_bar = part('lower bar')

        self.set_size(0, 0)

    # Clear all parts and reset overall size
    def clear(self):
        for value in vars(self).values():
            if isinstance(value, part):
                value.clear()
        self.set_size(0, 0)
        return self

    # Set overall width and height
    def set_size(self, width, height):
        self._width = width
        self._height = height
        return self

    # Get overall size
    def get_size(self):
        return self._width, self._height

    # Get overall width
    def get_width(self):
        return self._width

    # Get overall height
    def get_height(self):
        return self._height

    # Get total height of upper section
    def get_upper_height(self):
        return self.upper_bar.get_height() + self.upper_axis.get_height() + self.upper_ticks.get_height()

    # Get total height of lower section
    def get_lower_height(self):
        return self.lower_bar.get_height() + self.lower_axis.get_height() + self.lower_ticks.get_height()

    # Get canvas height
    def get_canvas_height(self):
        return self._height - self.get_upper_height() - self.get_lower_height()

    # Get total width of left section
    def get_left_width(self):
        return self.left_ticks.get_width() + self.left_axis.get_width()

    # Get total width of right section
    def get_right_width(self):
        return self.right_ticks.get_width() + self.right_axis.get_width()

    # Get canvas width
    def get_canvas_width(self):
        return self._width - self.get_left_width() - self.get_right_width()

    # Update canvas size and adjust vertical parts
    def update_canvas_size(self):
        canvas_height = self.get_canvas_height()
        canvas_width = self.get_canvas_width()

        self.canvas.set_size(canvas_width, canvas_height)
        self.left_ticks.set_height(canvas_height)
        self.left_axis.set_height(canvas_height)
        self.right_axis.set_height(canvas_height)
        self.right_ticks.set_height(canvas_height)
        return self

    # Update widths of bars, ticks, and axes
    def update_widths(self):
        self.upper_bar.set_width(self._width)
        self.lower_bar.set_width(self._width)

        canvas_width = self.canvas.get_width()
        self.upper_ticks.set_width(canvas_width)
        self.upper_axis.set_width(canvas_width)
        self.lower_axis.set_width(canvas_width)
        self.lower_ticks.set_width(canvas_width)

        return self

    # Update positions of all parts
    def update_positions(self):
        self.upper_bar.set_position(0, 0)

        left_width = self.get_left_width()
        upper_height = self.get_upper_height()

        self.upper_ticks.set_position(left_width, self.upper_bar.get_row(1))
        self.upper_axis.set_position(left_width, self.upper_ticks.get_row(1))

        self.left_ticks.set_position(0, upper_height)
        self.left_axis.set_position(self.left_ticks.get_width(), upper_height)

        self.canvas.set_position(left_width, upper_height)

        self.right_axis.set_position(self.canvas.get_col(1), upper_height)
        self.right_ticks.set_position(self.right_axis.get_col(1), upper_height)

        self.lower_axis.set_position(left_width, self.canvas.get_row(1))
        self.lower_ticks.set_position(left_width, self.lower_axis.get_row(1))

        self.lower_bar.set_position(0, self.lower_ticks.get_row(1))
        return self

    # Update sizes and positions of the four corner parts
    def update_corners(self):
        self.upper_left_corner.set_width(self.get_left_width())
        self.lower_left_corner.set_width(self.get_left_width())

        self.upper_right_corner.set_width(self.get_right_width())
        self.lower_right_corner.set_width(self.get_right_width())

        self.upper_left_corner.set_height(self.upper_axis._height + self.upper_ticks._height)
        self.upper_right_corner.set_height(self.upper_axis._height + self.upper_ticks._height)

        self.lower_left_corner.set_height(self.lower_axis._height + self.lower_ticks._height)
        self.lower_right_corner.set_height(self.lower_axis._height + self.lower_ticks._height)

        self.upper_left_corner.set_position(0, self.upper_bar.get_height())
        self.upper_right_corner.set_position(self.canvas.get_col(1), self.upper_bar.get_height())

        self.lower_left_corner.set_position(0, self.lower_axis._row)
        self.lower_right_corner.set_position(self.canvas.get_col(1), self.lower_axis._row)

        return self

    # Run basic tests for size consistency
    def test(self):
        width_test = (self.left_ticks.get_width() + self.left_axis.get_width() + self.canvas.get_width() + self.right_axis.get_width() + self.right_ticks.get_width()) == self._width

        height_test = (self.upper_bar.get_height() + self.upper_ticks.get_height() + self.upper_axis.get_height() + self.canvas.get_height() + self.lower_axis.get_height() +
                       self.lower_bar.get_height() + self.lower_ticks.get_height() == self._height)
        height_test2 = self.left_ticks.get_height() == self.right_ticks.get_height() == self.canvas.get_height()

        corner_width_test = (self.upper_left_corner.get_width() + self.canvas.get_width() + self.upper_right_corner.get_width()) == self._width
        corner_width_test2 = (self.upper_left_corner.get_width() == self.lower_left_corner.get_width()) and (self.upper_right_corner.get_width() == self.lower_right_corner.get_width())

        corner_height_test = self.upper_left_corner.get_height() == self.upper_right_corner.get_height() and self.lower_left_corner.get_height() == self.lower_right_corner.get_height()

        print("Width Test:", width_test)
        print("Height Test:", height_test and height_test2)

        print("Corner Test:", corner_width_test and corner_width_test2 and corner_height_test)

        return self

    # Return a log string summarizing all parts
    def get_log(self):
        out = f'Plotext Parts: total size {(self._width, self._height)}'
        for value in vars(self).values():
            if isinstance(value, part):
                out += f'\n {value.get_log()}'
        return out

    # Print log
    def log(self):
        print(self.get_log())
        return self

    # String representation in one line
    def __repr__(self):
        return self.get_log()
