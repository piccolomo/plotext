# Border characters grouped by type and style

# Horizontal and vertical edges
horizontal_line = {"default": '─', "double": '═', "dotted": '┈'}
vertical_line   = {"default": '│', "double": '║', "dotted": '┊'}

# Corner characters (top/bottom, left/right)
lower_right_corner = {"default": '┘', "double": '╝', "rounded": '╯'}
lower_left_corner  = {"default": '└', "double": '╚', "rounded": '╰'}
upper_right_corner = {"default": '┐', "double": '╗', "rounded": '╮'}
upper_left_corner  = {"default": '┌', "double": '╔', "rounded": '╭'}

# Junction characters (connections between edges)
full_junction   = {"default": '┼', "double": '╬'}
right_junction  = {"default": '├', "double": '╠'}
left_junction   = {"default": '┤', "double": '╣'}
upper_junction  = {"default": '┴', "double": '╩'}
lower_junction  = {"default": '┬', "double": '╦'}