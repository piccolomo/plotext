# Environments
- [Matplotlib](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#matplotlib)
- [Rich](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#rich)
- [Tkinter](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#tkinter)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Matplotlib
To automatically transform a `matplotlib` plot into a `plotext` one use the function `from_matplotlib()`. Here is an example:

```python
import matplotlib.pyplot as plt
import plotext as plx

y = plx.sin(); ym = [-el for el in y]
x = range(len(y))

plt.clf()
plt.subplot(211)
plt.plot(x, y, color = 'red')
plt.title('Some Smart Title')
plt.xlabel('here is a label')


plt.subplot(212)
plt.plot(x, ym, color = 'green')
plt.ylabel('the y axis')

plt.show(block = 0)

fig = plt.gcf()

plx.from_matplotlib(fig)
plx.show()
```

![matplotlib](https://raw.githubusercontent.com/piccolomo/plotext/master/data/matplotlib.png)

These feature is under development: please report any bug, with some possible idea on how to fix it.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Environments](https://github.com/piccolomo/plotext/blob/master/readme/environments.md)


## Rich
The integration with the package `rich` has been discussed in [issue 26](https://github.com/piccolomo/plotext/issues/26) and [issue 27](https://github.com/piccolomo/plotext/issues/27). Thanks to the kind help of its creator, `@willmcgugan`, as well as the user `@whisller`, it seems that the following code could be a good working template:

```python
from rich.layout import Layout
from rich.live import Live
from rich.ansi import AnsiDecoder
from rich.console import Group
from rich.jupyter import JupyterMixin
from rich.panel import Panel
from rich.text import Text

from time import sleep
import plotext as plt

def make_plot(width, height, phase = 0, title = ""):
    plt.clf()
    l, frames = 1000, 30
    x = range(1, l + 1)
    y = plt.sin(periods = 2, length = l, phase = 2 * phase  / frames)
    plt.scatter(x, y, marker = "fhd")
    plt.plotsize(width, height)
    plt.xaxes(1, 0)
    plt.yaxes(1, 0)
    plt.title(title)
    plt.theme('dark')
    plt.ylim(-1, 1)
    #plt.cls()
    return plt.build()

class plotextMixin(JupyterMixin):
    def __init__(self, phase = 0, title = ""):
        self.decoder = AnsiDecoder()
        self.phase = phase
        self.title = title
        
    def __rich_console__(self, console, options):
        self.width = options.max_width or console.width
        self.height = options.height or console.height
        canvas = make_plot(self.width, self.height, self.phase, self.title)
        self.rich_canvas = Group(*self.decoder.decode(canvas))
        yield self.rich_canvas

def make_layout():
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=1),
        Layout(name="main", ratio=1),
    )
    layout["main"].split_column(
        Layout(name="static", ratio = 1),
        Layout(name="dynamic"),
    )
    return layout

layout = make_layout()

header = layout['header']
title = plt.colorize("Pl✺ text ", "cyan+", "bold") + "integration with " + plt.colorize("rich_", style = "dim")
header.update(Text(title, justify = "left"))

static = layout["static"]
phase = 0
mixin_static = Panel(plotextMixin(title = "Static Plot"))
static.update(mixin_static)

dynamic = layout["dynamic"]

with Live(layout, refresh_per_second=0.0001) as live:
    while True:
        phase += 1
        mixin_dynamic = Panel(plotextMixin(phase, "Dynamic Plot")) 
        dynamic.update(mixin_dynamic)
        #sleep(0.001)
        live.refresh()
```
[Main Guide](https://github.com/piccolomo/plotext#guide), [Environments](https://github.com/piccolomo/plotext/blob/master/readme/environments.md)

## Tkinter
The integration with the package `tkinter` has been discussed in [Issue 33](https://github.com/piccolomo/plotext/issues/33). Thanks to the great inputs from user `@gregwa1953`, here is an initial take on it, where a test image is downloaded in the home folder, visualized and finally removed:

```python
import tkinter as tk
import plotext as plt
from plotext._utility.color import to_rgb, uncolorize
import tkinter.font as tkfont

image_path = 'cat.jpg'
#font_name = "UbuntuMono"
#font_name = "MonoSpace"

font_name = "SourceCodePro"
font_size = 13
font_size_plot = 25

font = font_name + " " + str(font_size)
stick_horizontal = tk.W + tk.E
stick_all = tk.E + tk.W + tk.N + tk.S
padx, pady = 2, 2
frame_color = "gray85"
nocommand = lambda: int

def frame(parent, row = 0, col = 0, stick = stick_horizontal):
     frame = tk.Frame(parent, background = frame_color, relief = 'groove', bd = 0)
     frame.config(highlightthickness = 0, highlightbackground = frame_color)
     frame.grid(row = row, column = col, sticky = stick, padx = padx, pady = pady)
     return frame

def button(parent, label = "button", row = 0, col = 0, command = nocommand):
     button = tk.Button(parent, text = label, font = font, command = command, relief = "raised", state = "normal", background = frame_color)
     button.grid(row = row, column = col, padx = padx, pady = pady)
     return button

def text(parent, width, height, font = None):
    text = tk.Text(parent, font = font, width = width, height = height, wrap = tk.NONE)
    text.grid(row = 0, column = 0, stick = stick_all)
    return text

def scale(parent, row = 0 , col = 0):
     scale = tk.Scale(parent, from_= 2, to = 30, orient = tk.HORIZONTAL, font = font, length = 300)
     scale.set(font_size)
     scale.grid(row = row, column = col, padx = padx, pady = pady)
     return scale

def from_rgb(rgb): # translates an rgb tuple of int to a tkinter friendly color code
    return "#%02x%02x%02x" % rgb
    #r, g, b = rgb
    #return f'#{r:02x}{g:02x}{b:02x}'

class window():
     def __init__(self):
          self.root = tk.Tk()
          self.root.resizable(True, True)
          self.root.title("Plotext in Tkinter")
          self.root.option_add('*Font', font)
          self.root.geometry('%dx%d+0+0' % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
          #self.root.geometry('%dx%d+0+0' % (300, 300))
          self.root.columnconfigure(0, weight = 1)
          self.root.rowconfigure(1, weight = 1)
          
          self.upper_frame = frame(self.root, row = 0)
          self.lower_frame = frame(self.root, row = 1, stick = stick_all)

          self.plot_button = button(self.upper_frame, label = "Plot ", command = self.plot_command, col = 0)
          self.scale = scale(self.upper_frame, col = 1)
          self.save_button = button(self.upper_frame, label = "Save", command = self.save_command, col = 2)
          self.close_button = button(self.upper_frame, label = "Close", command = self.close_command, col = 3)
          
          self.clear_command()
          self.root.mainloop()

     def clear_command(self):
          for widgets in self.lower_frame.winfo_children():
               widgets.destroy()

     def save_command(self):
          plt.savefig("plot.html")

     def close_command(self):
          self.root.destroy()
          
     def plot_command(self):
          self.plot_button.config(state = "disabled", relief = "sunken")
          self.scale.config(state = "disabled")
          self.clear_command()
          self.get_plot_size()
          
          self.plotext_command()
          self.add_plot()
          self.add_colors()
          
          self.plot_button.config(state = "normal", relief = "raised")
          self.scale.config(state = "normal")
          
     def get_plot_size(self):
          self.root.update()
          size = self.lower_frame.winfo_width(), self.lower_frame.winfo_height()

          font_size = self.scale.get()
          self.font_plot = tkfont.Font(family = font_name, size = font_size)
          font_size = self.font_plot.measure('m'), self.font_plot.metrics('linespace')# in pixels

          size = [size[i] / font_size[i] for i in range(2)]
          size = list(map(int, size))
          self.cols, self.rows = self.size = size
          
     def plotext_command(self):
          plt.clf()
          plt.limitsize(False, False)
          plt.plotsize(*self.size)
          plt.image_plot(image_path, fast = True)
          plt.build()
          #plt.show()
          
     def add_plot(self):
          # Add Colorless Plot 
          self.cols, self.rows = plt.figure._size
          self.plot_text = text(self.lower_frame, self.cols, self.rows, font = self.font_plot)         
          self.canvas = plt.figure.monitor.canvas
          self.canvas = uncolorize(self.canvas)
          self.plot_text.insert("end", self.canvas)
          self.plot_text.update()
          
     def add_colors(self): # Add Colors to Plot
          self.color = plt.figure.monitor.matrix
          tag = lambda r, c: str(r) + "*" + str(c)
          coord = lambda r, c: str(r + 1) + "." + str(c)
          for r in range(self.rows):
               for c in range(self.cols):
                    fg = from_rgb(to_rgb(self.color[r][c][2]))
                    bg = from_rgb(to_rgb(self.color[r][c][1]))
                    self.plot_text.tag_add(tag(r, c), coord(r, c))
                    self.plot_text.tag_config(tag(r, c), foreground = fg, background = bg)
               self.plot_text.update()
          self.plot_text.update()

if __name__ == '__main__':        
     plt.download(plt.test_image_url, image_path)
     gui = window()
     plt.delete_file(image_path)
```
which outputs:

![tkinter](https://raw.githubusercontent.com/piccolomo/plotext/master/data/tkinter.png)
- Using the `scale` slider one can change the font size; lower font size makes the final plot bigger, which requires more computational time,
- the `Save` button saves the plots as an `html` file in the user home folder.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Environments](https://github.com/piccolomo/plotext/blob/master/readme/environments.md)