from plotext._default import default_terminal
from plotext._master import master_class
from plotext._system import write
import shutil


class terminal_class():
    def __init__(self):
        self.set_prompt_height()
        self.update_size()
        self._create_master()
        self._parent = None
        
    def set_prompt_height(self, height = None):
        self.prompt_height = default_terminal.prompt_height if height is None else int(height)
        return self

    def update_size(self):
        try:
            width, height  = shutil.get_terminal_size()
        except: #OSError:
            width, height = default_terminal.size
        height -= self.prompt_height
        self._width = width
        self._height = max(0, height)
        self._size = [width, height]
        return self

    def get_size(self):
        #self.update_default_size()
        return self._size

    def clear(self, lines = None): # it cleat the entire terminal, or the specified number of lines
        write('\033c') if lines is None else None
        [write("\033[A\033[2K") for r in range(lines)] if lines is not None else None
        return self

    def _create_master(self):
        self._master = master_class(terminal = self)

    def __repr__(self):
        return 'terminal()'
    
    def _harmonize_sizes(self):
        pass

    def _set_size_direction(self, direction):
        pass

    def _get_parent(self, l):
        return self

terminal = terminal_class()


        
