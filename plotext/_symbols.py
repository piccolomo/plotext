# This module defines various border symbols for different styles and a function to retrieve the appropriate symbol.

# Horizontal line symbols for different styles
horizontal_line = {
    "default": '─',
    "double": '═',
    "dotted": '┈'}

# Vertical line symbols for different styles
vertical_line = {
    "default": '│',
    "double": '║',
    "dotted": '┊'}

# Lower right corner symbols for different styles
lower_right_corner = {
    "default": '┘',
    "double": '╝',
    "rounded": '╯'}

# Lower left corner symbols for different styles
lower_left_corner = {
    "default": '└',
    "double": '╚',
    "rounded": '╰'}

# Upper right corner symbols for different styles
upper_right_corner = {
    "default": '┐',
    "double": '╗',
    "rounded": '╮'}

# Upper left corner symbols for different styles
upper_left_corner = {
    "default": '┌',
    "double": '╔',
    "rounded": '╭'}

# Full node symbols for different styles
full_node = {
    "default": '┼',
    "double": '╬'}

# Right node symbols for different styles
right_node = {
    "default": '├',
    "double": '╠'}

# Left node symbols for different styles
left_node = {
    "default": '┤',
    "double": '╣'}

# Upper node symbols for different styles
upper_node = {
    "default": '┴',
    "double": '╩'}

# Lower node symbols for different styles
lower_node = {
    "default": '┬',
    "double": '╦'}

def get_symbol(dictionary, style):
    # Retrieve the symbol based on the style, defaulting to 'default' if the style is not found
    return dictionary.get(style, dictionary['default'])
