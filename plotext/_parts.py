from plotext._part import part_class as part


class parts_class:
    def __init__(self):
        # Upper parts
        self.upper_bar = part('upper bar')
        self.upper_ticks = part('upper ticks')
        self.upper_axis = part('upper axis')

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
        self.lower_axis = part('lower axis')
        self.lower_ticks = part('lower ticks')
        self.lower_bar = part('lower bar')

        self.set_size(0, 0)

    # Reset all parts and overall size
    def clear(self):
        for part_obj in [self.upper_bar, self.upper_ticks, self.upper_axis,
                         self.left_ticks, self.left_axis,
                         self.canvas, self.legend,
                         self.right_axis, self.right_ticks,
                         self.lower_axis, self.lower_ticks,
                         self.lower_bar]:
            part_obj.clear()
        self.set_size(0, 0)
        return self

    # Set overall width and height
    def set_size(self, width, height):
        self.width = width
        self.height = height
        return self

    # Get overall size
    def get_size(self):
        return self.width, self.height

    # Get total height of upper section
    def get_upper_height(self):
        return self.upper_bar.height + self.upper_axis.height + self.upper_ticks.height

    # Get total height of lower section
    def get_lower_height(self):
        return self.lower_bar.height + self.lower_axis.height + self.lower_ticks.height

    # Get canvas height
    def get_canvas_height(self):
        return self.height - self.get_upper_height() - self.get_lower_height()

    # Get total width of left section
    def get_left_width(self):
        return self.left_ticks.width + self.left_axis.width

    # Get total width of right section
    def get_right_width(self):
        return self.right_ticks.width + self.right_axis.width

    # Get canvas width
    def get_canvas_width(self):
        return self.width - self.get_left_width() - self.get_right_width()

    # Update canvas size and related vertical heights
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
        self.upper_bar.set_width(self.width)
        self.lower_bar.set_width(self.width)

        xwidth = self.canvas.width + self.left_axis.width + self.right_axis.width
        self.upper_ticks.set_width(self.canvas.width)
        self.upper_axis.set_width(xwidth)
        self.lower_axis.set_width(xwidth)
        self.lower_ticks.set_width(self.canvas.width)
        return self

    # Update positions of all parts
    def update_positions(self):
        self.upper_bar.set_position(0, 0)

        left_width = self.get_left_width()
        upper_height = self.get_upper_height()

        self.upper_ticks.set_position(left_width, self.upper_bar.get_row(1))
        self.upper_axis.set_position(self.left_ticks.width, self.upper_ticks.get_row(1))

        self.left_ticks.set_position(0, upper_height)
        self.left_axis.set_position(self.left_ticks.width, upper_height)

        self.canvas.set_position(left_width, upper_height)

        self.right_axis.set_position(self.canvas.get_col(1), upper_height)
        self.right_ticks.set_position(self.right_axis.get_col(1), upper_height)

        self.lower_axis.set_position(self.left_ticks.width, self.canvas.get_row(1))
        self.lower_ticks.set_position(left_width, self.lower_axis.get_row(1))

        self.lower_bar.set_position(0, self.lower_ticks.get_row(1))
        return self

    # Run basic tests for consistency
    def test_parts(self):
        width_test = (self.left_ticks.width + self.canvas.width + self.right_ticks.width) == self.width
        height_test = (self.upper_bar.height + self.upper_ticks.height + self.canvas.height +
                       self.lower_bar.height + self.lower_ticks.height)
        height_test2 = self.left_ticks.height == self.right_ticks.height == self.canvas.height
        print("Width Test:", width_test)
        print("Height Test:", height_test)
        print("Height Test 2:", height_test2)
        return self

    # Return a log string for all parts
    def get_log(self):
        out = f'Plot size: {(self.width, self.height)}'
        for value in vars(self).values():
            if isinstance(value, part):
                out += '\n' + value.get_log()
        return out

    # Print log
    def log(self):
        print(self.get_log())
        return self

    def __repr__(self):
        return self.get_log()