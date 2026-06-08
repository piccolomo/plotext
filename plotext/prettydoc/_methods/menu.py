# Interactive picker: arrows navigate, enter picks an item, q quits.
# Input shape used throughout this file:
#   sections = list of (title, items) tuples; one tuple = one column-group of the picker.
#       title   = the heading string shown on top of the column-group
#       items   = list of (text, function) pairs; text shows in the menu, function is what gets handed to print_function() on Enter

import sys, os
from plotext._settings.system import platform
from plotext._methods.string import write
from plotext._primitives.colorize import colorize


# ANSI control sequences used throughout the file.
cursor_to_top_left      = '\x1b[H'
clear_screen            = '\x1b[2J\x1b[H'
erase_to_end_of_line    = '\x1b[K'
erase_below_cursor      = '\x1b[J'
enter_separate_page     = '\x1b[?1049h\x1b[?25l'
exit_separate_page      = '\x1b[?1049l\x1b[?25h'
new_line                = '\n'

# Rows reserved for non-content (blank + top frame + bottom frame + blank + footer hint).
reserved_rows = 5


# Wrap text in dim style.
def dim(text):
    return str(colorize(text, style = 'dim'))


# Wrap text in a chosen foreground (and optional style).
def color(text, foreground, style = None):
    return str(colorize(text, foreground = foreground, style = style))


# Read one keystroke and return its name: 'up', 'down', 'left', 'right', 'pgup', 'pgdn', 'enter', 'esc', 'q', or None.
if platform == "windows":
    import msvcrt
    _arrow = {b'H': 'up', b'P': 'down', b'K': 'left', b'M': 'right', b'I': 'pgup', b'Q': 'pgdn'}
    def read_key():
        character = msvcrt.getch()
        if character in (b'\xe0', b'\x00'): return _arrow.get(msvcrt.getch())
        if character == b'\r':              return 'enter'
        if character == b'\x1b':            return 'esc'
        if character.lower() == b'q':       return 'q'
        return None
else:
    import termios, tty, select
    _arrow = {b'[A': 'up', b'[B': 'down', b'[D': 'left', b'[C': 'right', b'[5': 'pgup', b'[6': 'pgdn'}
    def read_key():
        character = os.read(0, 1)
        if character == b'\x1b':
            if not select.select([0], [], [], 0.05)[0]: return 'esc'   # bare Esc, no follow-up within 50 ms
            escape_sequence = os.read(0, 2)
            if escape_sequence in (b'[5', b'[6'): os.read(0, 1)                    # consume the trailing ~ of PageUp/PageDn
            return _arrow.get(escape_sequence)
        if character in (b'\r', b'\n'): return 'enter'
        if character.lower() == b'q':   return 'q'
        return None


# Make every keystroke arrive instantly with no echo on screen; returns the previous terminal state (a snapshot of how keys were being buffered and echoed) so disable_instant_keys() can restore it.
def enable_instant_keys():
    if platform == "windows": return None
    state = termios.tcgetattr(sys.stdin.fileno())
    tty.setcbreak(sys.stdin.fileno())
    return state


# Undo enable_instant_keys(); keystrokes go back to normal line-buffered mode.
def disable_instant_keys(previous_terminal_state):
    if previous_terminal_state is not None:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, previous_terminal_state)


# Swap to a separate blank page (independent from the shell's scroll history); hide the terminal cursor while we draw.
def enter_independent_terminal():
    write(enter_separate_page, flush = True)


# Discard the separate page; the shell's scroll history reappears unchanged.
def exit_independent_terminal():
    write(exit_separate_page, flush = True)


# One visual line in the menu. line_kind is 'header', 'item', 'blank', or 'divider'. column/row are set by assign_line_position().
class Line:
    def __init__(self, line_kind, text = '', function = None):
        self.line_kind, self.text, self.function = line_kind, text, function
        self.column, self.row = 0, 0


# Build the list of Lines for the whole menu. Each section becomes: header, blank, then one item line per pair; successive sections get a divider between them.
def make_lines(sections):
    lines = []
    for section_index, (title, items) in enumerate(sections):
        if section_index > 0:
            lines.append(Line('divider'))
        lines.append(Line('header', text = title))
        lines.append(Line('blank'))
        for text, function in items:
            lines.append(Line('item', text = text, function = function))
    return lines


# Lines the user is allowed to highlight (only items, never headers, blanks or dividers).
def get_items(lines):
    return [line for line in lines if line.line_kind == 'item']


# Assign each line a column and row by flowing them top-to-bottom; when a column fills up, the next line starts at the top of a new column.
def assign_line_position(lines, rows):
    for line_index, line in enumerate(lines):
        line.column, line.row = line_index // rows, line_index % rows


# How many columns the laid-out lines use.
def get_cols(lines):
    return max((line.column for line in lines), default = 0) + 1


# Width of each column: widest line's text in that column plus extra_padding for breathing room.
def get_column_widths(lines, extra_padding = 4):
    column_widths = [0] * get_cols(lines)
    for line in lines:
        column_widths[line.column] = max(column_widths[line.column], len(line.text))
    return [column_width + extra_padding for column_width in column_widths]


# Fast (column, row) -> Line lookup, so the renderer can find what to draw at each position.
def get_position_to_line_dict(lines):
    return {(line.column, line.row): line for line in lines}


# Pick the next Line to highlight after the user presses `pressed_key`: up/down step through items; pgup/pgdn jump by `rows`; left/right jump to the nearest item in the adjacent column.
def get_next_highlighted_line(selectable_lines, current_line, pressed_key, rows):
    current_index = selectable_lines.index(current_line)
    if pressed_key == 'up':   return selectable_lines[max(0, current_index - 1)]
    if pressed_key == 'down': return selectable_lines[min(len(selectable_lines) - 1, current_index + 1)]
    if pressed_key == 'pgup': return selectable_lines[max(0, current_index - rows)]
    if pressed_key == 'pgdn': return selectable_lines[min(len(selectable_lines) - 1, current_index + rows)]
    if pressed_key in ('left', 'right'):
        target_column = current_line.column + (-1 if pressed_key == 'left' else 1)
        if target_column >= 0:
            items_in_target_column = [line for line in selectable_lines if line.column == target_column]
            if items_in_target_column:
                return min(items_in_target_column, key = lambda line: abs(line.row - current_line.row))
    return current_line


# Top edge of the frame: ┌──┬──┐ with corner glyphs at the ends and ┬ between columns, all dim.
def get_upper_frame(column_widths):
    return dim('┌' + '┬'.join('─' * column_width for column_width in column_widths) + '┐')


# Bottom edge of the frame: └──┴──┘ with corner glyphs at the ends and ┴ between columns, all dim.
def get_lower_frame(column_widths):
    return dim('└' + '┴'.join('─' * column_width for column_width in column_widths) + '┘')


# Glyph at the right edge of column `col` on row `row`: ┼/├/┤ if a horizontal divider sits in column `col` or `col+1` at that row, otherwise │.
def get_column_right_separator(position_to_line_dict, col, row, cols):
    here_is_divider = (col, row) in position_to_line_dict and position_to_line_dict[(col, row)].line_kind == 'divider'
    if col == cols - 1: return '┤' if here_is_divider else '│'
    next_is_divider = (col + 1, row) in position_to_line_dict and position_to_line_dict[(col + 1, row)].line_kind == 'divider'
    return '┼' if here_is_divider and next_is_divider else '┤' if here_is_divider else '├' if next_is_divider else '│'


# Styled text for one Line at the given column_width: dim divider, bold-cyan header, bold-yellow highlighted item, plain item, or blank.
def get_line_string(line, column_width, is_highlighted):
    if line is None or line.line_kind == 'blank': return ' ' * column_width
    if line.line_kind == 'divider':               return dim('─' * column_width)
    text = (' ' + line.text).ljust(column_width)
    if line.line_kind == 'header':                return color(text, 'cyan+', 'bold')
    if is_highlighted:                            return color(text, 'yellow', 'bold')
    return text


# Left edge glyph for `row`: ├ if the first column has a divider on this row, otherwise │.
def get_left_edge(position_to_line_dict, row):
    first_column_has_divider = (0, row) in position_to_line_dict and position_to_line_dict[(0, row)].line_kind == 'divider'
    return dim('├' if first_column_has_divider else '│')


# Gray footer hint shown beneath the frame.
def get_footer_hint():
    return color(' press arrows to navigate, enter to view, q to quit', 'gray+')


# Assemble the full picker string: cursor reset, blank top row, frame edges, one string per row, bottom edge, blank, footer hint, clear-to-end.
def get_picker(position_to_line_dict, highlighted_line, terminal_height):
    lines = list(position_to_line_dict.values())
    column_widths = get_column_widths(lines)
    cols = get_cols(lines)
    string_parts = [cursor_to_top_left, erase_to_end_of_line + new_line, get_upper_frame(column_widths) + erase_to_end_of_line + new_line]
    visible_rows = max(0, terminal_height - reserved_rows)
    for row in range(visible_rows):
        row_string = get_left_edge(position_to_line_dict, row)
        for col in range(cols):
            line_at_this_position = position_to_line_dict.get((col, row))
            row_string += get_line_string(line_at_this_position, column_widths[col], line_at_this_position is highlighted_line)
            row_string += dim(get_column_right_separator(position_to_line_dict, col, row, cols))
        string_parts.append(row_string + erase_to_end_of_line + new_line)
    string_parts.append(get_lower_frame(column_widths) + erase_to_end_of_line + new_line)
    string_parts.append(erase_to_end_of_line + new_line)
    string_parts.append(get_footer_hint() + erase_to_end_of_line)
    string_parts.append(erase_below_cursor)
    return ''.join(string_parts)


# Print the picked function on a cleared screen, then wait for Enter (return to menu) or q (quit). Returns 'enter' or 'q'.
def display_picked_function(picked_function, print_function):
    write(clear_screen, flush = True)
    print_function(picked_function)
    print()
    print(color('press enter for main menu, q to quit', 'gray+'))
    while True:
        pressed_key = read_key()
        if pressed_key in ('enter', 'q'): return pressed_key


# Run the interactive picker. sections is a list of (title, [(text, function), ...]); print_function(function) is called when the user presses Enter on an item. Falls back to printing every item when interactive input isn't possible.
def run_picker(sections, print_function):
    lines = make_lines(sections)
    items = get_items(lines)
    if not sys.stdin.isatty() or not items:
        for item in items: print_function(item.function); print()
        return
    highlighted_line = items[0]
    previous_terminal_state = enable_instant_keys()
    enter_independent_terminal()
    try:
        while True:
            terminal_size = os.get_terminal_size()
            rows = max(1, terminal_size.lines - reserved_rows)
            assign_line_position(lines, rows)
            position_to_line_dict = get_position_to_line_dict(lines)
            write(get_picker(position_to_line_dict, highlighted_line, terminal_size.lines), flush = True)
            pressed_key = read_key()
            if pressed_key in ('q', 'esc'): break
            highlighted_line = get_next_highlighted_line(items, highlighted_line, pressed_key, rows)
            if pressed_key == 'enter' and display_picked_function(highlighted_line.function, print_function) == 'q': break
    finally:
        exit_independent_terminal()
        disable_instant_keys(previous_terminal_state)
