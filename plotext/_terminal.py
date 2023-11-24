from plotext._default import default_terminal
from plotext._system import write
import shutil

class terminal_class():
    def __init__(self):
        self.set_prompt_height()
        self.update_size()

    def set_prompt_height(self, height = None):
        self.prompt_height = default_terminal.prompt_height if height is None else int(height)

    def update_size(self):
        try:
            self.width, self.height = shutil.get_terminal_size()
        except OSError:
            self.width, self.height = default_size.size
        self.height -= self.prompt_height
        self.size = [self.width, self.height]

    def get_size(self):
        self.update_size()
        return self.size

    def clear(self, lines = None): # it cleat the entire terminal, or the specified number of lines
        if lines is None:
            write('\033c')
        else:
            for r in range(lines):
                write("\033[A") # moves the curson up
                write("\033[2K") # clear the entire line

terminal = terminal_class()
