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

    # Clean the terminal: with no lines, everything is wiped, the past rows included; with -1, only what is on screen, with no flickering; with a number, the cursor moves up that many rows, so the next writing takes their place.
    def clean(self, lines = None):
        if lines is None:
            write('\033c')
        elif lines == -1:
            write('\033[H\033[2J')
        else:
            write("\033[A" * lines)
        return self

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
        height = max(0, height - self._prompt)             # the prompt cannot take away more rows than the terminal has, as when no terminal answers and the size comes back as zero
        self._size = self._width, self._height = [width, height]
        return self

    # Return current size, optionally updating first and optionally including the prompt height
    def size(self, update = False, plottable = True):
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
        out += '\n└─' + self._master._get_log()
        return out

    # Print the terminal log
    def log(self):
        print(self._get_log())
        return self

    # True when the given key was typed since the last call, answering right away without waiting; the first call asks the terminal to deliver each key as it is typed, and the answer is always False when the input is not a keyboard.
    def is_pressed(self, key = 'q'):
        return _is_pressed(key)

    # The terminal sits at the top of the plots hierarchy, above the master figure, and is its own parent at every level
    def parent(self, level = 1):
        return self

    # Short string representation
    def __repr__(self):
        width, height = self.size(update = False, plottable = True)
        return f'PlotextTerminal(width {width}, height {height}, prompt {self._prompt} lines, width limited {self._limit[0]}, height limited {self._limit[1]})'
