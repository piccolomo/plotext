from plotext._default import default_terminal
import shutil

class terminal_class():
    def __init__(self):
        self.set_prompt_size()
        self.update_size()

    def set_prompt_size(self, height = None):
        self.prompt_height = default_terminal.prompt_height if height is None else int(height)

    def update_size(self): # it returns the terminal size as [width, height]
        try:
            self.width, self.height = shutil.get_terminal_size()
        except OSError:
            self.width, self.height = default_size.size
        self.height -= self.prompt_height
        self.size = [self.width, self.height]

    # def update_max_size(self, width = None, height = None):
    #     m = 5
    #     self.infinite_width = m * self.width if width is None else int(width)
    #     self.infinite_height = m * self.height if height is None else int(height)
    #     self.infinite_size = [self.infinite_width, self.infinite_height]

terminal = terminal_class()
