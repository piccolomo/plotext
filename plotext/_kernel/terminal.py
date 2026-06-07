# Terminal: owns the master plot, tracks the terminal size and prompt height, and clears the screen

from plotext._settings import defaults
from plotext._methods.string import write
from plotext._methods.key import is_pressed as _is_pressed
from plotext._plotter.plot import plot_class
import shutil


# Terminal container: wraps a master plot_class and tracks terminal size and prompt height
class terminal:
    # Initialize settings and build the master plot
    def __init__(self):
        self.clear()
        self._create_master()

    # Clean the visible region of the terminal: None = hard reset (\033c, clears scrollback + modes), -1 = soft full-clear (\033[H\033[2J, just clear screen, no flicker, terminal state preserved), N>0 = cursor up so the next write overwrites the last N lines in place. _prompt is a hidden override of the reserved-prompt offset added to N (default uses self._prompt; playback passes 0 to move up exactly N lines when reprinting a frame that does not fill the screen).
    def clean(self, lines = None, _prompt = None):
        prompt = self._prompt if _prompt is None else _prompt
        if lines is None:
            write('\033c')
        elif lines == -1:
            write('\033[H\033[2J')
        else:
            write("\033[A" * (lines + prompt))
        return self

    clt = clean

    # Reset prompt, limit and size to defaults
    def clear(self):
        self.prompt()
        self.limit()
        self._update_size()
        return self

    # Set the prompt height (lines reserved below the plot)
    def prompt(self, height = None):
        self._prompt = defaults.terminal["prompt height"] if height is None else int(height)
        return self

    # Set whether width and height are limited to the terminal size
    def limit(self, width = None, height = None):
        width = defaults.terminal["limit width"] if width is None else bool(width)
        height = defaults.terminal["limit height"] if height is None else bool(height)
        self._limit = [width, height]
        return self

    # Query the total terminal size, falling back to defaults on failure
    def _get_total_size(self):
        try:
            size = shutil.get_terminal_size()
            width, height = size.columns, size.lines
        except:
            width, height = defaults.terminal["width"], defaults.terminal["height"]
        return width, height

    # Refresh cached size, subtracting the prompt height
    def _update_size(self):
        width, height = self._get_total_size()
        height -= self._prompt
        self._size = self._width, self._height = [width, height]
        return self

    # Return current size, optionally updating first and optionally including the prompt height
    def get_size(self, update = False, plottable = True):
        self._update_size() if update else None
        width, height = self._size
        if not plottable:
            height += self._prompt
        return width, height

    # Build the master plot and attach it
    def _create_master(self):
        self._master = plot_class(parent = self)
        self._master._set_size(*self._size)
        return self

    # Return the master plot
    def _get_master(self):
        return self._master

    # The terminal has no parent
    def _get_parent(self, level=None):
        return None

    # Identity check: this object is the terminal
    def _is_terminal(self):
        return True

    # Identity check: this object is a master
    def _is_master(self):
        return True

    # Identity check: this object is not a sub-master
    def _is_sub_master(self):
        return False

    # Build a multi-line log string including the master plot tree
    def _get_log(self):
        out = str(self)
        out += '\n└─' + self._master.get_log()
        return out

    # Print the terminal log
    def log(self):
        print(self._get_log())
        return self

    # Non-blocking poll: True if the user has pressed `key` since the last call. First call sets cbreak mode (restored at exit) so keystrokes are delivered immediately. Returns False when stdin is not a TTY.
    def is_pressed(self, key = 'q'):
        return _is_pressed(key)

    # Short string representation
    def __repr__(self):
        width, height = self.get_size(update = False, plottable = True)
        return f'Terminal(width: {width}, height: {height}, prompt: {self._prompt} lines, width limited: {self._limit[0]}, height limited: {self._limit[1]})'
