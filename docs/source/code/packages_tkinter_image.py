import tkinter as tk
import tkinter.font as tkfont

import plotext as plt

font_name = "DejaVu Sans Mono"

plt.terminal.limit(False, False)   # the window decides the plot size, not the terminal


# The bundled sample image drawn at the given size in characters: no frame and no numerical ticks, so that only the picture shows
def get_image(width, height):
    fig = plt.figure
    fig.clear()
    fig.plot_size(width, height)
    fig.axes(False)
    fig.ruler("both").frequency(0)
    fig.draw(fig.image(plt.sample("puppy")))
    return fig.build()


# An (r, g, b) triple written the way tkinter reads a color, and None when the character carries none
def get_color(rgb):
    return None if rgb is None else "#%02x%02x%02x" % rgb


# The foreground and the background of one character, as a pair of tkinter colors
def get_colors(matrix, row, column):
    pixel = matrix.get(row, column)
    return get_color(pixel.foreground()), get_color(pixel.background())


# Adds one stretch under the tag named after its two colors, creating the tag the first time it is met. A picture is made of full block characters, and a block glyph does not cover the gap tkinter leaves between two lines, so the stretch is written as blank characters carrying the color as their background, which does fill the whole cell.
def write_stretch(text_box, text, colors):
    foreground, background = colors
    tag = f"{foreground}/{background}"
    text_box.tag_config(tag, background = foreground or background or "black")
    text_box.insert(tk.END, " " * len(text), tag)


# Writes the matrix into the text box, one stretch of equal coloring at a time, as in the previous example
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


# The window: a row of controls above, the picture below
class window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Plotext in Tkinter")
        self.root.geometry("1000x620")

        controls = tk.Frame(self.root)
        controls.pack(fill = tk.X)
        tk.Button(controls, text = "Draw", command = self.draw).pack(side = tk.LEFT, padx = 4, pady = 4)
        tk.Button(controls, text = "Save", command = self.save).pack(side = tk.LEFT, padx = 4, pady = 4)
        tk.Button(controls, text = "Close", command = self.root.destroy).pack(side = tk.LEFT, padx = 4, pady = 4)

        # The font size chosen here decides how many characters fit, and so how detailed the picture is: the smaller the font, the finer the result and the longer it takes
        self.scale = tk.Scale(controls, from_ = 4, to = 20, orient = tk.HORIZONTAL, length = 260, label = "font size")
        self.scale.set(6)
        self.scale.pack(side = tk.LEFT, padx = 8)

        self.text_box = tk.Text(self.root, background = "black", wrap = tk.NONE,
                                borderwidth = 0, padx = 0, pady = 0, spacing1 = 0, spacing2 = 0, spacing3 = 0)
        self.text_box.pack(fill = tk.BOTH, expand = True)

        self.matrix = None
        self.draw()
        self.root.mainloop()

    # Draws the picture at the size the text box currently allows, in the chosen font size
    def draw(self):
        font = tkfont.Font(family = font_name, size = self.scale.get())
        self.text_box.config(font = font)
        self.root.update_idletasks()
        width = self.text_box.winfo_width() // font.measure("m")
        height = self.text_box.winfo_height() // font.metrics("linespace")
        self.matrix = get_image(width, height)
        write_plot(self.text_box, self.matrix)

    # Saves what is on display as a web page, colors included
    def save(self):
        self.matrix.save("plot.html", log = True)


window()
