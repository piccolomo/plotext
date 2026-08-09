# Layout: the sizes and the pieces the menu is drawn with, the column widths, the cells, the frame lines and the headers.

from plotext._primitives.colorize import colorize
from plotext.prettydoc._defaults.pixels import default_pixels
from plotext.prettydoc._menu.text import get_visible_length, add_background, end_of_colors


# ANSI control sequences used throughout the file.
cursor_to_top_left      = '\x1b[H'
erase_to_end_of_line    = '\x1b[K'
erase_below_cursor      = '\x1b[J'
enter_separate_page     = '\x1b[?1049h\x1b[?25l'
exit_separate_page      = '\x1b[?1049l\x1b[?25h'
new_line                = '\n'

# Reverse video painted on the picked entry of the active column: text and background colors swap, following the terminal theme.
active_background       = '\x1b[7m'

# Rows taken by everything around the column content (blank top row, top frame, header row, header divider, bottom frame, blank row, footer hint); one more row is taken when a title is shown above the frame.
reserved_rows = 7


# Wrap text in a chosen foreground (and optional style).
def color(text, foreground, style = None):
    return str(colorize(text, pixel = (foreground, None, style)))


# Wrap text in gray plus dim style, painting the table frame very lightly.
def dim(text):
    return str(colorize(text, pixel = ('gray+', None, 'dim')))


# Widths of the three columns: the first two fit their widest entry, shrinking on a narrow terminal, the docstring column takes the remaining terminal width.
def get_column_widths(sections, terminal_width, hide_sections = False):
    if hide_sections:
        method_width = max((len(text) for _, items in sections for text, _ in items), default = 8) + 2
        method_width = min(method_width, max(8, terminal_width - 4 - 24))
        docstring_width = max(24, terminal_width - method_width - 4)
        return [method_width, docstring_width]
    section_width = max(len(title) for title, _ in sections) + 2
    method_width = max((len(text) for _, items in sections for text, _ in items), default = 8) + 2
    available_width = terminal_width - 5 - 24
    section_width = min(section_width, max(10, available_width - method_width))
    method_width = min(method_width, max(8, available_width - section_width))
    docstring_width = max(24, terminal_width - section_width - method_width - 5)
    return [section_width, method_width, docstring_width]


# One column cell: a leading space, the text padded to fill the column width; plain text longer than the column is cut, colored text arrives already fitted.
def get_cell(text, width):
    visible_length = get_visible_length(text)
    text = text[:width - 1] if visible_length == len(text) else text
    return ' ' + text + ' ' * max(0, width - 1 - min(visible_length, width - 1))


# The picked entry cell: bold reversed text, with no color of its own, when its column is the active one, yellow otherwise; either way keeping the given style.
def get_picked_cell(cell, is_active, style = None):
    if is_active:
        bold_style = 'bold' + (' ' + style if style else '')
        return add_background(str(colorize(cell, pixel = (None, None, bold_style))), active_background)
    return color(cell, 'yellow', style)


# The right border of a column at the given row, filled where the rows on display sit within the whole content, so that it doubles as a scroll indicator; painted like the rest of the frame.
def get_column_border(row, rows, total, scroll):
    if total <= rows:
        return dim('│')
    filled_height = max(1, rows * rows // total)
    filled_start = (rows - filled_height) * scroll // max(1, total - rows)
    return dim('█') if filled_start <= row < filled_start + filled_height else dim('│')


# One horizontal frame line, built from its left, middle and right glyphs, painted like the rest of the frame.
def get_frame_line(column_widths, edges):
    left, middle, right = edges
    return dim(left + middle.join('─' * column_width for column_width in column_widths) + right)


# The header cells naming the columns, in the header colors; the sections header goes when its column is hidden.
def get_header_cells(column_widths):
    headers = ['Sections', 'Methods', 'Docstring'][-len(column_widths):]
    return [str(colorize(get_cell(headers[column], column_widths[column])).fill(default_pixels['header'])) for column in range(len(column_widths))]


# One empty row between the given cells, so that the section and method lists breathe.
def add_empty_rows(cells, width):
    spaced_cells = []
    for cell in cells:
        spaced_cells.append(cell)
        spaced_cells.append(' ' * width)
    return spaced_cells[:-1]


# The cells of the sections column: each section title in blue, never bold; the picked one takes the picked entry colors.
def get_section_cells(sections, selected_section, width, is_active):
    cells = []
    for index, (section_title, _) in enumerate(sections):
        cell = get_cell(section_title, width)
        cell = get_picked_cell(cell, is_active) if index == selected_section else color(cell, 'blue+')
        cells.append(cell)
    return add_empty_rows(cells, width)


# The cells of the methods column: plain method names, never bold; the picked one takes the picked entry colors; attribute entries (objects reached by name without parentheses, like figure) render in italic dim to stand apart from methods.
def get_method_cells(items, selected_method, width, is_active):
    cells = []
    for index, (text, function) in enumerate(items):
        cell = get_cell(text, width)
        is_attribute = function._get_kind() == 'attribute'
        if index == selected_method:
            cell = get_picked_cell(cell, is_active, 'italic' if is_attribute else None)
        elif is_attribute:
            cell = str(colorize(cell).fill(default_pixels['attribute']))
        cells.append(cell)
    return add_empty_rows(cells, width)


# Bottom line with the reachable keys, all colored gray.
def get_footer_hint():
    return color(' arrows to navigate, enter to view, left and right to change column, q to quit', 'gray+')


# Title line shown above the frame, colored, aligned to its left edge.
def get_title_line(title):
    return ' ' + str(colorize(title).fill(default_pixels['title']))


# Assemble the full menu string: cursor reset, blank top row, optional title, top frame, header row and its divider, one row per visible line with the scroll indicators at the column borders, bottom frame, blank, footer hint, clear-to-end; the frame is painted very lightly, the active column marked by its bold pick.
def get_menu(header_cells, column_cells, scrolls, rows, column_widths, title = None):
    string_parts = [cursor_to_top_left, erase_to_end_of_line + new_line]
    if title is not None:
        string_parts.append(get_title_line(title) + erase_to_end_of_line + new_line)
    string_parts.append(get_frame_line(column_widths, '┌┬┐') + erase_to_end_of_line + new_line)
    string_parts.append(dim('│') + dim('│').join(header_cells) + dim('│') + erase_to_end_of_line + new_line)
    string_parts.append(get_frame_line(column_widths, '├┼┤') + erase_to_end_of_line + new_line)
    for row in range(rows):
        row_string = dim('│')
        for column in range(len(column_widths)):
            index = row + scrolls[column]
            cells = column_cells[column]
            row_string += cells[index] if index < len(cells) else ' ' * column_widths[column]
            row_string += get_column_border(row, rows, len(cells), scrolls[column])
        string_parts.append(row_string + erase_to_end_of_line + new_line)
    string_parts.append(get_frame_line(column_widths, '└┴┘') + erase_to_end_of_line + new_line)
    string_parts.append(erase_to_end_of_line + new_line)
    string_parts.append(get_footer_hint() + erase_to_end_of_line)
    string_parts.append(erase_below_cursor)
    return ''.join(string_parts)
