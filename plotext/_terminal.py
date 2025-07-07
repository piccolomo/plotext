# Standard and internal imports
import shutil

from plotext._default import default_terminal_prompt_height
from plotext._methods import *
from plotext._plot import plot_class


class terminal_class:

    # Initialize terminal settings
    def __init__(self):
        self.set_prompt_height()
        self.update_size()
        self._create_master()

    # Clear entire terminal or specified number of lines
    def clear(self, lines = None):
        if lines is None:
            string_methods.write('\033c')
        else:
            for _ in range(lines):
                string_methods.write("\033[A")   # Move cursor up one line
                string_methods.write("\033[2K")  # Clear entire line
        return self

    # Get current terminal size (width, height)
    def get_size(self):
        try:
            size = shutil.get_terminal_size()
            return size.columns, size.lines
        except:
            # fallback defaults if terminal size cannot be determined
            return default_terminal_prompt_height, default_terminal_prompt_height

    # Set prompt height (default or custom)
    def set_prompt_height(self, height = None):
        self.prompt_height = default_terminal_prompt_height if height is None else int(height)
        return self

    # Update terminal width, height and size attributes
    def update_size(self):
        width, height = self.get_size()
        height -= self.prompt_height
        self._width = width
        self._height = max(0, height)
        self._size = [width, height]
        return self

    # Create a plot master object for the terminal
    def _create_master(self):
        self.master = plot_class()

    # String representation of the terminal object
    def __repr__(self):
        title = 'Terminal'
        size = f'height {self._height}, width {self._width}'
        return f'{title}({size})'
