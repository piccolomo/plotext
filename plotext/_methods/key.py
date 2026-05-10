# Non-blocking key polling: returns True if the user has pressed `key` since the last call. Auto-sets cbreak on first call so keystrokes are delivered immediately, restores cooked mode on exit. Returns False when stdin is not a TTY.

import sys, atexit


if sys.platform == 'win32':
    import msvcrt
    def is_pressed(key = 'q'):
        if not sys.stdin.isatty() or not msvcrt.kbhit(): return False
        try: ch = msvcrt.getch().decode(errors = 'ignore')
        except Exception: return False
        return ch.lower() == key.lower()

else:
    import select, termios, tty
    _setup_done = False
    # Set the terminal into cbreak mode once and register a restore-on-exit hook.
    def _setup():
        global _setup_done
        if _setup_done or not sys.stdin.isatty(): return
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        tty.setcbreak(fd)
        atexit.register(lambda: termios.tcsetattr(fd, termios.TCSADRAIN, old))
        _setup_done = True

    def is_pressed(key = 'q'):
        if not sys.stdin.isatty(): return False
        _setup()
        if not select.select([sys.stdin], [], [], 0)[0]: return False
        return sys.stdin.read(1).lower() == key.lower()
