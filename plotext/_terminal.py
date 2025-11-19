import shutil
from plotext._default import default_terminal_prompt_height
from plotext._methods import *
from plotext._plot import plot_class


class terminal_class:

    def __init__(self):
        self.set_prompt_height()
        self.update_size()
        self._create_master()

    def clear(self, lines = None):
        if lines is None:
            string_methods.write('\033c')
        else:
            for _ in range(lines):
                string_methods.write("\033[A")
                string_methods.write("\033[2K")
        return self

    def get_size(self):
        try:
            size = shutil.get_terminal_size()
            return size.columns, size.lines
        except:
            return default_terminal_prompt_height, default_terminal_prompt_height

    def get_parent(self, level=None):
        return None

    def _is_terminal(self):
        return True

    def _is_master(self):
        return True

    def _is_sub_master(self):
        return False

    def set_prompt_height(self, height = None):
        self.prompt_height = default_terminal_prompt_height if height is None else int(height)
        return self

    def update_size(self):
        width, height = self.get_size()
        height -= self.prompt_height
        self._width = width
        self._height = max(0, height)
        self._size = [width, height]
        return self

    def _create_master(self):
        self._master = plot_class(parent = self)
        self._master._set_size(*self._size)

    def get_master(self):
        return self._master

    def get_log(self):
        out = str(self)
        out += '\n└─' + self._master.get_log()
        return out

    def log(self):
        print(self.get_log())
        return self

    def __repr__(self):
        size = f'height {self._height}, width {self._width}'
        return f'Terminal({size})'
