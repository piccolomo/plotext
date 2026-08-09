import tkinter as tk
import tkinter.font as tkfont

import plotext as plt

font_name, font_size = "DejaVu Sans Mono", 14

plt.terminal.limit(False, False)   # the window decides the plot size, not the terminal


# The plot drawn at the given size in characters, as a matrix of colored characters
def get_plot(width, height):
    fig = plt.figure
    fig.clear()
    fig.plot_size(width, height)
    fig.theme("dark")
    fig.draw(fig.signal(plt.sin(periods = 2)).lines().label("sin"))
    fig.draw(fig.signal(plt.sin(periods = 2, phase = 0.5)).lines().label("shifted"))
    fig.title("Plotext in Tkinter")
    fig.label("time", "x")
    return fig.build()


# An (r, g, b) triple written the way tkinter reads a color, and None when the character carries none
def get_color(rgb):
    return None if rgb is None else "#%02x%02x%02x" % rgb


# Writes the matrix into the text box: each stretch of characters sharing one coloring is inserted under a tag of its own, so the number of tags is the number of colorings, not the number of characters
def write_plot(text_box, matrix):
    text_box.delete("1.0", tk.END)
    characters = matrix.string(colorless = True).split("\n")
    for row in range(matrix.height()):
        start = 0
        for column in range(1, matrix.width() + 1):
            here = get_colors(matrix, row, column) if column < matrix.width() else None
            if here == get_colors(matrix, row, start):
                continue
            write_stretch(text_box, characters[row][start:column], get_colors(matrix, row, start))
            start = column
        text_box.insert(tk.END, "\n")


# The foreground and background of one character, as a pair of tkinter colors
def get_colors(matrix, row, column):
    pixel = matrix.get(row, column)
    return get_color(pixel.foreground()), get_color(pixel.background())


# Adds one stretch of text under the tag named after its two colors, creating the tag the first time it is met
def write_stretch(text_box, text, colors):
    foreground, background = colors
    tag = f"{foreground}/{background}"
    text_box.tag_config(tag, foreground = foreground or "white", background = background or "black")
    text_box.insert(tk.END, text, tag)


# The window: a text box holding the plot, redrawn at the size the window currently allows
def show_window():
    root = tk.Tk()
    root.title("Plotext in Tkinter")
    root.geometry("1000x560")

    font = tkfont.Font(family = font_name, size = font_size)
    # every padding set to zero, so that neighbouring block characters touch and the plot lines look continuous
    text_box = tk.Text(root, font = font, background = "black", wrap = tk.NONE,
                       borderwidth = 0, padx = 0, pady = 0, spacing1 = 0, spacing2 = 0, spacing3 = 0)
    text_box.pack(fill = tk.BOTH, expand = True)

    def redraw(event = None):
        root.update_idletasks()
        width = text_box.winfo_width() // font.measure("m")
        height = text_box.winfo_height() // font.metrics("linespace")
        write_plot(text_box, get_plot(width, height))

    root.bind("<Configure>", redraw)
    redraw()
    root.mainloop()


show_window()
