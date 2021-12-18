[Plotext Guide](https://github.com/piccolomo/plotext#guide)

# Other Environments
- [Rich](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#rich)
- [Tkinter](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#tkinter)


## Rich

The integration with the package `rich` has been discussed in [Issue 26](https://github.com/piccolomo/plotext/issues/26). Thanks to the kind help of its creator, `willmcgugan`, as well as user `whisller`, it seems that the following code could be a good working template:

```python
from rich.layout import Layout
from rich.live import Live
from rich.ansi import AnsiDecoder
from rich.console import RenderGroup
from rich.jupyter import JupyterMixin
from rich.panel import Panel

from time import sleep
import plotext as plt

def make_plot(*size):
    plt.clf()
    plt.scatter(plt.sin(1000, 3))
    plt.plotsize(*size)
    plt.title("Plotext Integration in Rich - Test")
    return plt.build()

class plotextMixin(JupyterMixin):
    def __init__(self):
        self.decoder = AnsiDecoder()
        
    def __rich_console__(self, console, options):
        self.width = options.max_width or console.width
        self.height = options.height or console.height
        canvas = make_plot(self.width, self.height)
        self.rich_canvas = RenderGroup(*self.decoder.decode(canvas))
        yield self.rich_canvas

def make_layout():
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
    )
    layout["main"].split_row(
        Layout(name="plotext", size=120),
        Layout(name="main_right"),
    )
    return layout

layout = make_layout()
plotext_layout = layout["plotext"]
mix = plotextMixin()
mix = Panel(mix)
plotext_layout.update(mix)

with Live(layout, refresh_per_second=0.1) as live:
    while True:
        sleep(0.1)
```
which outputs:

![rich](https://raw.githubusercontent.com/piccolomo/plotext/master/images/rich.png)

[Other Environments](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#other-environments)


## Tkinter

The integration with the package `tkinter` has been discussed in [Issue 33](https://github.com/piccolomo/plotext/issues/33) and here is my initial take on it:
```python
import tkinter as tk 
import plotext as plt

font_name = "DejaVuSans"
font_name = "UbuntuMono"

button_font_size = 13
plot_font_size = 8
button_font = font_name + " " + str(button_font_size)
plot_font = font_name + " " + str(plot_font_size)
frame_color = "gray85"
left = tk.N + tk.S + tk.W
padx, pady = 2, 2

nocommand = lambda: int

def frame(parent, row = 0, col = 0):
     new = tk.Frame(parent, background = frame_color, relief = 'sunken', bd = 0)
     new.config(highlightthickness = 0, highlightbackground = frame_color)
     new.grid(row = row, column = col, sticky = left, padx = padx, pady = pady)
     return new
     
def button(parent, label = "button", row = 0, col = 0, command = nocommand):
    new = tk.Button(parent, text = label, font = button_font, command = command, relief = "raised", state = "normal", background = frame_color)
    new.grid(row = row, column = col, sticky = left, padx = padx, pady = pady)
    return new
    
def label(parent, label = "label", row = 0, col = 0):
    new = tk.Label(parent, text = label, font = plot_font, justify = tk.LEFT, background = frame_color)
    new.grid(row = row, column = col, sticky = left, padx = padx, pady = pady)
    return new

class window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Plotext in Tkinter")
        self.root_width, self.root_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry('%dx%d+0+0' % (self.root_width, self.root_height))
        self.upper_frame = frame(self.root, row = 0)
        self.lower_frame = frame(self.root, row = 1)
        self.plot_button = button(self.upper_frame, label = "Plot", command = self.plot_command, col = 0)
        self.clear_button = button(self.upper_frame, label = "Clear", command = self.clear_command, col = 1)
        self.canvas = ""
        self.plot_label = label(self.lower_frame, label = self.canvas)
        self.clear_command()
        self.root.mainloop()
        
    def clear_command(self):
        self.plot_button.config(state = "normal")
        self.clear_button.config(state = "disabled")
       
        self.canvas = ""
        self.plot_label.config(text = self.canvas)
       
    def plot_command(self):
        self.plot_button.config(state = "disabled")
        self.clear_button.config(state = "normal")
        self.plotext_command()        
        self.plot_label.config(text = self.canvas)
        
    def plotext_command(self):
        plt.plot(plt.sin(), marker = "dot")
        plt.plotsize(365, 90)
        plt.limitsize(False)
        plt.clc()
        self.canvas = plt.build()

if __name__ == '__main__':        
    gui = window()
```
which outputs:

![tkinter](https://raw.githubusercontent.com/piccolomo/plotext/master/images/tkinter.png)

**Note**: for now no color and no higher resolution markers are available.

[Other Environments](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#other-environments)

[Plotext Guide](https://github.com/piccolomo/plotext#guide)

