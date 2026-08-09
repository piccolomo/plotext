from rich.ansi import AnsiDecoder
from rich.console import Group
from rich.jupyter import JupyterMixin
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

import plotext as plt

plt.terminal.limit(False, False)   # the box decides the plot size, not the terminal


# The plot drawn at the given size, as a string of colored characters
def get_plot(width, height, phase = 0, title = ""):
    fig = plt.figure
    fig.clear()
    length, frames = 1000, 30
    y = plt.sin(periods = 2, length = length, phase = 2 * phase / frames)
    fig.draw(fig.signal(range(1, length + 1), y, marker = "fhd"))
    fig.plot_size(width, height)
    fig.theme("dark")
    fig.title(title)
    fig.ruler("y").lim(-1, 1)
    return fig.build().string()


# What rich asks for a plot each time it draws the panel holding it, at the size that panel currently has
class plotext_panel(JupyterMixin):
    def __init__(self, phase = 0, title = ""):
        self.decoder = AnsiDecoder()
        self.phase = phase
        self.title = title

    def __rich_console__(self, console, options):
        width = options.max_width or console.width
        height = options.height or console.height
        plot = get_plot(width, height, self.phase, self.title)
        yield Group(*self.decoder.decode(plot))


# A title row, a fixed plot and a plot redrawn at every frame
def get_layout():
    layout = Layout(name = "root")
    layout.split(Layout(name = "header", size = 1), Layout(name = "main", ratio = 1))
    layout["main"].split_column(Layout(name = "static", ratio = 1), Layout(name = "dynamic"))
    return layout


layout = get_layout()
title = plt.colorize("Plotext ", ("cyan+", None, "bold")) + "inside " + plt.colorize("rich", (None, None, "dim"))
layout["header"].update(Text.from_ansi(str(title)))
layout["static"].update(Panel(plotext_panel(title = "Static Plot")))

with Live(layout, refresh_per_second = 20) as live:
    for phase in range(120):
        layout["dynamic"].update(Panel(plotext_panel(phase, "Dynamic Plot")))
        live.refresh()
