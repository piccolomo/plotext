# Border symbols for various styles

horizontal_line = {
    "default": '─',
    "double": '═',
    "dotted": '┈'}

vertical_line = {
    "default": '│',
    "double": '║',
    "dotted": '┊'}

lower_right_corner = {
    "default": '┘',
    "double": '╝',
    "rounded": '╯'}

lower_left_corner = {
    "default": '└',
    "double": '╚',
    "rounded": '╰'}

upper_right_corner = {
    "default": '┐',
    "double": '╗',
    "rounded": '╮'}

upper_left_corner = {
    "default": '┌',
    "double": '╔',
    "rounded": '╭'}

full_node = {
    "default": '┼',
    "double": '╬'}

right_node = {
    "default": '├',
    "double": '╠'}

left_node = {
    "default": '┤',
    "double": '╣'}

upper_node = {
    "default": '┴',
    "double": '╩'}

lower_node = {
    "default": '┬',
    "double": '╦'}


# Retrieve a symbol from the dictionary for the given style. Defaults to the 'default' style if not found.
def get_symbol(dictionary, style):
    return dictionary.get(style, dictionary['default'])
