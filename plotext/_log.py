from plotext._color import colorize, no_color

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
        if not self.show:
            return 
        #message = colorize('Warning:', self.color_warning, "bold")
        #message += colorize(text, no_color, self.style_warning)
        print('Warning:', text) 
        
log = log_class()
        
