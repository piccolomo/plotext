from plotext._default import correct_xside, correct_yside, default_settings
from plotext._colorize import colorize


class settings_class():
    def __init__(self):
        self.bar_upper = bar_upper_class()
        self.bar_lower = bar_lower_class()
        self.set_ticks_color()
        self.set_axes_color()

        
    def set_ticks_color(self, color = None):
        self.ticks_color = color if color is not None else default_settings.ticks_color
        
    def set_axes_color(self, color = None):
        self.axes_color = color if color is not None else default_settings.axes_color

        
    def ylabel(self, label, yside):
        label = self.correct_label(label)
        yside = correct_yside(yside)
        self.bar_lower.set_left(label) if yside == 'left' else self.bar_lower.set_right(label)

    def xlabel(self, label, xside):
        label = self.correct_label(label)
        xside = correct_xside(xside)
        self.bar_lower.set_center(label) if xside == 'lower' else self.bar_upper.set_label(label)

    def title(self, label):
        label = self.correct_label(label)
        self.bar_upper.set_title(label)
        
    def correct_label(self, label):
        return colorize(label, self.ticks_color, self.axes_color).part(0, 1) if isinstance(label, str) else label

    
    def update(self):
        self.bar_upper.update()

    def clear(self):
        self.__init__()
            

class bar_lower_class():
    def __init__(self):
        self.set_left()
        self.set_center()
        self.set_right()
        
    def set_left(self, label = None):
        self.left = label

    def set_center(self, label = None):
        self.center = label

    def set_right(self, label = None):
        self.right = label

        
class bar_upper_class(bar_lower_class):
    def __init__(self):
        super().__init__()
        self.set_label()
        self.set_title()

    def set_title(self, label = None):
        self.title = label

    def set_label(self, label = None):
        self.label = label

    def update(self):
        label_on = self.label is not None
        self.set_center(self.label)
        self.set_left(self.title) if label_on else self.set_center(self.title) 

