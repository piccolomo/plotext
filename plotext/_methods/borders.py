# Functions to retrieve and resolve border characters based on style, axis, and orientation

from plotext._settings.constants import borders


# Alias for the full (cross) junction symbol dictionary
full_node = borders.full_junction


# Retrieve character for a given style with fallback to 'default'
def get_symbol(dictionary, style):
    return dictionary.get(style, dictionary["default"])


# Get edge (line) character based on axis (0=horizontal, 1=vertical)
def get_line_symbol(axis, style):
    return get_symbol(borders.vertical_line if axis else borders.horizontal_line, style)


# Get x-axis corner character based on orientation
def get_xaxis_corner(horizontal, vertical, style):
    if vertical:
        return get_symbol(
            borders.upper_left_corner if not horizontal else borders.upper_right_corner, style)
    return get_symbol(
        borders.lower_left_corner if not horizontal else borders.lower_right_corner, style)


# Get junction (tick) character based on axis and side
def get_tick_symbol(axis, side, style):
    if axis == 1:  # vertical axis
        return get_symbol(borders.left_junction if side == 0 else borders.right_junction, style)
    return get_symbol(borders.lower_junction if side == 0 else borders.upper_junction, style)


# Get corner symbol based on orientation
def get_corner_symbol(horizontal, vertical, style):
    if vertical and horizontal:
        return get_symbol(borders.upper_right_corner, style)
    if vertical and not horizontal:
        return get_symbol(borders.upper_left_corner, style)
    if not vertical and horizontal:
        return get_symbol(borders.lower_right_corner, style)
    return get_symbol(borders.lower_left_corner, style)
