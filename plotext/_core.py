from ._terminal import terminal as _terminal
from ._figure import figure_class
from ._log import log as _log

terminal = _terminal
master = _master = terminal._master

##############################################
###########    Size Functions    #############
##############################################

def limit_size(width = None, height = None):
    return _master.limit_size(width, height)

def plot_size(width = None, height = None):
    return _master.plot_size(width, height)
plotsize = plot_size

def size_direction(direction = None):
    return _master.size_direction(direction)

def take_minimum_size():
    return _master.take_minimum_size()
take_min = take_minimum_size

def take_maximum_size():
    return _master.take_maximum_size()
take_max = take_maximum_size

def prompt_size(height = None):
    _terminal.set_prompt_height(height)
    return clear_sizes()

##############################################
#########    Subplots Functions    ###########
##############################################

def main():
    return _master

def active():
    return _master._get_active()

def subplots(rows = None, cols = None):
    return _master.subplots(rows, cols)

def subplot(row = None, col = None):
    return _master.subplot(row, col)

##############################################
#########    Settings Functions    ###########
##############################################

def ticks_color(color = None):
    return _master.ticks_color(color)

def axes_color(color = None):
    return _master.axes_color(color)

def canvas_color(color = None):
    return _master.canvas_color(color)

def title(label = None):
    return _master.title(label)

def xlabel(label = None, xside = None):
    return _master.xlabel(label, xside)

def ylabel(label = None, yside = None):
    return _master.ylabel(label, yside)


def xaxes(lower = None, upper = None):
    return _master.xaxes(lower, upper)

def yaxes(left = None, right = None):
    return _master.yaxes(left, right)

def frame(frame = None):
    return _master.frame(frame)

def marks_style(style = None):
    return _master.marks_style(style)

def xlim(left = None, right = None, xside = None):
    return _master.xlim(left, right, xside)

def ylim(lower = None, upper = None, yside = None):
    return _master.ylim(lower, upper, yside)

def xfrequency(frequency = None, xside = None):
    return _master.xfrequency(frequency, xside)

def yfrequency(frequency = None, yside = None):
    return _master.yfrequency(frequency, yside)

def xticks(ticks = None, labels = None, xside = None):
    return _master.xticks(ticks, labels, xside)

def yticks(ticks = None, labels = None, yside = None):
    return _master.yticks(ticks, labels, yside)

def xreverse(reverse = None, xside = None):
    return _master.xreverse(reverse, xside)

def yreverse(reverse = None, yside = None):
    return _master.yreverse(reverse, yside)

def xscale(scale = None, xside = None):
    return _master.xscale(scale, xside)

def yscale(scale = None, yside = None):
    return _master.yscale(scale, yside)

def xdates(xside):
    return _master.xdates(xside)

def ydates(yside):
    return _master.ydates(yside)

def horizontal_line(y, color = None, yside = None):
    return _master.horizontal_line(y, color, yside)
hline = horizontal_line

def vertical_line(y, color = None, xside = None):
    return _master.vertical_line(y, color, xside)
vline = vertical_line

##############################################
######    Main Plotting Functions    #########
##############################################

def scatter(*args, xside = None, yside = None):
    _master.scatter(*args, xside = xside, yside = yside)
    show() if _master._interactive else None

##############################################
##########    Build Functions    #############
##############################################

def interactive(interactive = None):
    return _master.interactive(interactive)

def build(colorless = True):
    return _master.build(colorless)
    
def show():
    _master.show()

##############################################
##########    Clear Functions    #############
##############################################

def clear_sizes():
    return _master.clear_sizes()

def clear_subplots():
    return _master.clear_subplots()

def clear_settings():
    return _master.clear_settings()
    
def clear_data():
    return _master.clear_data()
cld = clear_data

def clear_figure():
    return _master.clear_figure()
clf = clear_figure

def clear_terminal(lines = None):
    return _terminal.clear(lines)
clt = clear_terminal

##############################################
#########    Utility Functions    ############
##############################################

def log(show = True):
    _log.on() if show else _log.off()

def terminal_size():
    return _terminal.get_size()
ts = terminal_size

def terminal_width():
    return terminal_size()[0]
tw = terminal_width

def terminal_height():
    return terminal_size()[1]
th = terminal_height
