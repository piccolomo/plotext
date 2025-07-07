from plotext._symbols import *


class line_class:
    def __init__(self, position, orientation, style, pixel):
        self.set_position(position)
        self.set_orientation(orientation)
        self.set_style(style)
        self.set_pixel(pixel)


    # Set the position of the line
    def set_position(self, position):
        self.position = position
        return self

    # Set the orientation (horizontal: True, vertical: False)
    def set_orientation(self, orientation):
        self.orientation = orientation
        return self

    # Set the style (e.g., 'default', 'double')
    def set_style(self, style):
        self.style = style
        return self

    # Set the pixel (rendering style)
    def set_pixel(self, pixel = None):
        self.pixel = pixel


    # Get the position of the line
    def get_position(self):
        return self.position

    # Get the orientation of the line
    def get_orientation(self):
        return self.orientation

    # Get the style of the line
    def get_style(self):
        return self.style

    # Get the pixel of the line
    def get_pixel(self):
        return self.pixel


    # Generate the string representation of the line with crossings
    def get_string(self, width, crossings = []):
        line = horizontal_line if self.orientation else vertical_line
        line = get_symbol(line, self.style)
        crossing = get_symbol(full_node, self.style)
        line = [crossing if i in crossings else line for i in range(width)]

        begin = right_node if self.orientation else lower_node
        end = left_node if self.orientation else upper_node

        begin = get_symbol(begin, self.style)
        end = get_symbol(end, self.style)

        return line


    # Create a copy of the line
    def copy(self):
        return line_class(self.get_position(), self.get_orientation(), self.get_style(), self.get_pixel())


    def __repr__(self):
        return f"Line position {round(self.position, 2)}, style {self.style}"
