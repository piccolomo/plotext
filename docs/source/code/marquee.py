# The plotext logo scrolling right to left across the terminal. The whole word is drawn once, as a strip of colored characters, and each frame is a slice of that strip: only the slicing happens in the loop, so the scroll is as smooth as the terminal allows.

import time
from PIL import Image
import plotext as plt

fig = plt.figure
paper = (255, 255, 255)                                # the color of everything the word has not reached yet
seconds = 1.5                                          # how long the word takes to cross the screen

# the logo is already drawn on white paper, so its own colors are used as they are
logo = Image.open("docs/source/images/logo6.png").convert("RGB")

w, h = plt.terminal.size(update = True)
rows = h - 1                                           # one row spared for the hint
word_cols = round(rows * logo.size[0] / logo.size[1] * 2)
letters = logo.resize((word_cols, rows)).load()

# the strip: a screen of paper, then the word, then a screen of paper again, so that the word enters and leaves
strip_cols = word_cols + 2 * w
colors = [[letters[col - w, row] if w <= col < w + word_cols else paper for col in range(strip_cols)] for row in range(rows)]

plt.terminal.limit(False, False)
fig.clear()
fig.plot_size(strip_cols, rows)
fig.axes(False)
fig.ruler("both").frequency(0)
fig.draw(fig.heatmap(colors))
strip = fig.build()                                    # the whole word, drawn once

frame, started = 0, time.time()
while True:

    if frame: plt.terminal.clean(h)                    # clean the previous frame, hint included

    travel = strip_cols - w
    shift = round((time.time() - started) / seconds * travel) % travel   # where the word has got to by now, read from the clock, so the crossing lasts the same time on any terminal
    strip[:, shift : shift + w].print()                # the piece of the strip on show now

    if plt.terminal.is_pressed('q'): break             # exit on key press
    print("press q to exit")

    frame += 1
