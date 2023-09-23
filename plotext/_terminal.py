from plotext._default import default_terminal
import shutil

class terminal_class():
    def __init__(self):
        self.default = default_terminal
        self.update_size()

    def update_size(self): # it returns the terminal size as [width, height]
        try:
            self.width, self.height = shutil.get_terminal_size()
            self.height -= 2
        except OSError:
            self.width, self.height = self.default.size
        self.size = [self.width, self.height]

terminal = terminal_class()
