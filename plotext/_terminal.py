from plotext._default import default_terminal
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

terminal = terminal_class()
