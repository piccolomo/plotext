from plotext._default import default_signal
import plotext._utility as ut

class signal_class():
    def __init__(self):
        pass
    
class signals_class():
    def __init__(self):
        pass

    def add(self, *args, **kwargs)
        x, y = ut.set_data(*args)
        xside = kwargs.get("xside")
        yside = kwargs.get("yside")
        xside = self.correct_xside(xside)
        yside = self.correct_yside(yside)
        
        self.add_data(*args, xside = xside, yside = yside)
        self.add_lines(kwargs.get("lines"))
        self.add_marker(kwargs.get("marker"))
        self.add_color(kwargs.get("color"))
        self.add_styles(kwargs.get("style"))
        self.add_fillx(kwargs.get("fillx"))
        self.add_filly(kwargs.get("filly"))
        self.add_label(kwargs.get("label"))
