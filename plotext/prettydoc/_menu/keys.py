# Keys: reading one keystroke at a time, and putting the terminal in the state where each key arrives instantly, on its own page.

import sys, os
from plotext._settings.system import platform
from plotext._methods.string import write

enter_separate_page = '\x1b[?1049h\x1b[?25l'
exit_separate_page  = '\x1b[?1049l\x1b[?25h'


# Reading one key: read_key() gives its name, one of up, down, left, right, pgup, pgdn, enter, esc and q, or nothing for any other key; read_key_or_resize() waits for one, and gives nothing as soon as the terminal changes size, so that the menu is drawn again at the new size. The two are written twice, once for windows and once for the other systems, which read the keyboard differently.
if platform == "windows":
    import msvcrt, time
    arrow_keys = {b'H': 'up', b'P': 'down', b'K': 'left', b'M': 'right', b'I': 'pgup', b'Q': 'pgdn'}
    def read_key():
        character = msvcrt.getch()
        if character in (b'\xe0', b'\x00'): return arrow_keys.get(msvcrt.getch())
        if character == b'\r':              return 'enter'
        if character == b'\x1b':            return 'esc'
        if character.lower() == b'q':       return 'q'
        return None
    def read_key_or_resize(terminal_size):
        while not msvcrt.kbhit():
            if os.get_terminal_size() != terminal_size:
                return None
            time.sleep(0.05)
        return read_key()
else:
    import termios, tty, select
    arrow_keys = {b'[A': 'up', b'[B': 'down', b'[D': 'left', b'[C': 'right', b'[5': 'pgup', b'[6': 'pgdn'}
    def read_key():
        character = os.read(0, 1)
        if character == b'\x1b':
            if not select.select([0], [], [], 0.05)[0]: return 'esc'   # bare Esc, no follow-up within 50 ms
            escape_sequence = os.read(0, 2)
            if escape_sequence in (b'[5', b'[6'): os.read(0, 1)                    # consume the trailing ~ of PageUp/PageDn
            return arrow_keys.get(escape_sequence)
        if character in (b'\r', b'\n'): return 'enter'
        if character.lower() == b'q':   return 'q'
        return None
    def read_key_or_resize(terminal_size):
        while not select.select([0], [], [], 0.25)[0]:
            if os.get_terminal_size() != terminal_size:
                return None
        return read_key()


# Ask the terminal to deliver every key as it is typed, without showing it on screen; what it gives back is how the terminal behaved before, so that disable_instant_keys() can put it back.
def enable_instant_keys():
    if platform == "windows": return None
    state = termios.tcgetattr(sys.stdin.fileno())
    tty.setcbreak(sys.stdin.fileno())
    return state


# Put the terminal back the way it was, keys waiting for the Enter key again.
def disable_instant_keys(previous_terminal_state):
    if previous_terminal_state is not None:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, previous_terminal_state)


# Move onto a blank page of its own, leaving the past rows of the terminal untouched, and hide the cursor while the menu is drawn.
def enter_independent_terminal():
    write(enter_separate_page, flush = True)


# Leave that page; the terminal comes back exactly as it was.
def exit_independent_terminal():
    write(exit_separate_page, flush = True)
