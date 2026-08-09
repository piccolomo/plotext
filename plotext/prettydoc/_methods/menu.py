# Interactive menu: three columns side by side, the sections, the methods of the picked section, and the docstring of the picked method; each column scrolls on its own.
# The sections given to it are a list of pairs: the section name, and its entries, each entry being its own pair of the text shown in the second column and the function whose docstring fills the third.

import os
import sys

from plotext._methods.string import write
from plotext.prettydoc._defaults.pixels import default_pixels
from plotext.prettydoc._menu.keys import read_key_or_resize, enable_instant_keys, disable_instant_keys, enter_independent_terminal, exit_independent_terminal
from plotext.prettydoc._menu.text import wrap_docstring
from plotext.prettydoc._menu.layout import get_column_widths, get_cell, get_section_cells, get_method_cells, get_header_cells, get_menu, reserved_rows


# What the menu remembers while it runs: the picked section and method, the column the keys act on, how far each column is scrolled, and the docstring on display.
class menu_state:
    def __init__(self, hide_sections):
        self.hide_sections = hide_sections                      # true when there are no sections, so their column is dropped
        self.section = 0                                        # the picked section, counted from the first
        self.method = 0                                         # the picked method inside that section
        self.column = 1 if hide_sections else 0                 # the column the keys act on: 0 sections, 1 methods, 2 docstring
        self.section_scroll = 0                                 # how many rows each column is scrolled down by
        self.method_scroll = 0
        self.docstring_scroll = 0
        self.docstring_cells = []                               # the docstring, already wrapped into rows
        self.docstring_choice = None                            # which docstring those rows belong to, so it is rebuilt only when the choice changes
        self.docstring_shown = False                            # true once Enter was pressed, since the third column starts empty


# Print every docstring one after the other, the answer when there is no keyboard to read.
def print_all_docstrings(sections, print_function):
    for _, items in sections:
        for _, function in items:
            print_function(function)
            print()


# Scroll a column just enough for its picked row to stay on display.
def follow_scroll(scroll, row, rows):
    return max(min(scroll, row), row - rows + 1)


# Move a value by one row or one page in the pressed direction, kept between zero and the given highest value.
def move(value, pressed_key, highest, page):
    step = {'up': -1, 'down': 1, 'pgup': -page, 'pgdn': page}[pressed_key]
    return max(0, min(highest, value + step))


# Wrap the docstring of the picked method into rows, but only when the choice or the column width changed since the last time.
def update_docstring(state, sections, docstring_width):
    choice = (state.section, state.method, docstring_width)
    if state.docstring_choice == choice:
        return
    state.docstring_choice = choice
    function = sections[state.section][1][state.method][1]
    docstring = function._get_titled_docstring(default_pixels['title'], section = True)
    state.docstring_cells = [get_cell(line, docstring_width) for line in wrap_docstring(str(docstring), docstring_width - 2)]
    state.docstring_scroll = 0


# Print the whole menu, its columns scrolled where the state says.
def draw_menu(state, sections, column_widths, rows, title):
    items = sections[state.section][1]
    column_cells = [get_method_cells(items, state.method, column_widths[-2], state.column == 1),
                    state.docstring_cells if state.docstring_shown else []]
    scrolls = [state.method_scroll, state.docstring_scroll]
    if not state.hide_sections:
        column_cells.insert(0, get_section_cells(sections, state.section, column_widths[0], state.column == 0))
        scrolls.insert(0, state.section_scroll)
    write(get_menu(get_header_cells(column_widths), column_cells, scrolls, rows, column_widths, title), flush = True)


# Change the state according to the pressed key; gives back False when the menu should close.
def apply_key(state, pressed_key, sections, rows):
    if pressed_key in ('q', 'esc'):
        return False
    if pressed_key in ('left', 'right'):
        first_column = 1 if state.hide_sections else 0
        state.column = max(first_column, min(2, state.column + (1 if pressed_key == 'right' else -1)))
    if pressed_key == 'enter':
        state.docstring_shown = state.docstring_shown or state.column > 0
        state.column = max(1, state.column)
    if pressed_key in ('up', 'down', 'pgup', 'pgdn'):
        page = max(1, rows // 2)
        if state.column == 0:
            state.section = move(state.section, pressed_key, len(sections) - 1, page)
            state.method, state.method_scroll, state.docstring_shown = 0, 0, False
        elif state.column == 1:
            items = sections[state.section][1]
            state.method = move(state.method, pressed_key, len(items) - 1, page)
        else:
            highest = max(0, len(state.docstring_cells) - rows)
            state.docstring_scroll = move(state.docstring_scroll, pressed_key, highest, rows)
    return True


# Run the interactive menu until q is pressed; with no keyboard to read, every docstring is printed instead, one after the other.
def run_menu(sections, print_function, title = None):
    functions = [function for _, items in sections for _, function in items]
    if not sys.stdin.isatty() or not functions:
        print_all_docstrings(sections, print_function)
        return

    state = menu_state(hide_sections = len(sections) == 1 and sections[0][0] is None)
    previous_terminal_state = enable_instant_keys()
    enter_independent_terminal()
    try:
        while True:
            terminal_size = os.get_terminal_size()
            rows = max(1, terminal_size.lines - reserved_rows - (title is not None))
            column_widths = get_column_widths(sections, terminal_size.columns, state.hide_sections)

            update_docstring(state, sections, column_widths[-1])
            state.section_scroll = follow_scroll(state.section_scroll, 2 * state.section, rows)
            state.method_scroll = follow_scroll(state.method_scroll, 2 * state.method, rows)
            state.docstring_scroll = min(state.docstring_scroll, max(0, len(state.docstring_cells) - rows))

            draw_menu(state, sections, column_widths, rows, title)

            pressed_key = read_key_or_resize(terminal_size)
            if not apply_key(state, pressed_key, sections, rows):
                break
    finally:
        exit_independent_terminal()
        disable_instant_keys(previous_terminal_state)
