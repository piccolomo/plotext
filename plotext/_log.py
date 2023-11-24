from plotext._colorize import colorize

warning_color = 'orange+'

class log_class():
    def __init__(self):
        self.color_positive = 'green+'
        self.color_negative = 'red'
        self.color_title = 'cyan+'
        self.color_warning = 'orange'
        self.style_warning = 'dim'
        self.on()

    def on(self):
        self.show = True
        
    def off(self):
        self.show = False

    def warning(self, text):
        print(colorize('Warning', warning_color) + (' :' + text)) if self.show else None
        
log = log_class()
