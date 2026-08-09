# Rain on still water, drawn as a heatmap: each drop sends out a ring that widens and fades, and the rings cross each other.

import math
import plotext as plt

fig = plt.figure

frames = 16                                            # how many frames the animation takes to come back to its start
deep, pale = (12, 74, 78), (168, 232, 206)             # the colors of deep water and of a wave crest
drops = [(0.18, 0.30, 0), (0.62, 0.25, 4), (0.40, 0.72, 7), (0.83, 0.62, 11), (0.30, 0.55, 13)]   # where each drop lands, as a fraction of the plot, and on which frame
life = 9                                               # how many frames a ring lasts before it fades away


# The height of the water at one cell: every ring still alive adds its own wave, weaker as the ring widens and as it ages
def get_height(col, row, cols, rows, frame):
    height = 0
    for x, y, start in drops:
        age = (frame - start) % frames
        if age < life:
            distance = math.hypot(col - x * cols, 2 * (row - y * rows))
            front = 5 * age                            # how far the ring has travelled by now
            height += math.cos((distance - front) / 5) * math.exp(-((distance - front) / 14) ** 2) * (1 - age / life)
    return height


# That height written as a color, between deep water and a wave crest
def get_color(col, row, cols, rows, frame):
    level = min(1, max(0, 0.5 + get_height(col, row, cols, rows, frame) / 2))
    return tuple(round(low + (high - low) * level) for low, high in zip(deep, pale))


frame = 0
while True:

    w, h = plt.terminal.size(update = True)            # take a fresh terminal size
    if frame: plt.terminal.clean(h)                    # clean the previous frame, hint included

    fig.clear()
    fig.plot_size(w, h - 1)                            # adapt to the terminal, one row spared for the hint
    fig.axes(False)
    fig.ruler("both").frequency(0)

    cols, rows = w + 4, h + 4                          # a few cells more than the plot has characters, so none is left blank
    water = [[get_color(col, row, cols, rows, frame) for col in range(cols)] for row in range(rows)]
    fig.draw(fig.heatmap(water))
    fig.title(plt.effect("rain on still water", "shimmer", step = frame, period = frames))

    plt.sleep(0.001)                                   # pause between frames
    fig.show(flush = True)

    if plt.terminal.is_pressed('q'): break             # exit on key press
    print("press q to exit")

    frame += 1
