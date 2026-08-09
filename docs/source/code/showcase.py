# The animation of the front page: a column of three moving plots on the left, a picture and the scrolling logo on the right.

import math
from PIL import Image
import plotext as plt

fig = plt.figure

frames = 32                                            # how many frames the animation takes to come back to its start
turns = 1                                              # how many times the plots go round while the word crosses once

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken"]

samples, bins = 7 * 10 ** 2, 10                        # how many values each histogram counts, and in how many bars

paper = (255, 255, 255)                                # the color of everything the scrolling word has not reached yet

# the logo, downloaded beside this script the first time and reused afterwards; it is already drawn on white paper, so its own colors are used as they are
address = "https://raw.githubusercontent.com/piccolomo/plotext/master/docs/source/images/logo6.png"
picture = "logo6.png"
plt.file.download(address, picture) if not plt.file.exists(picture) else None
logo = Image.open(picture).convert("RGB")


# The picture is read and resampled once, before the loop: doing it on every frame costs ten times the whole rest of the plot
w, h = plt.terminal.size(update = True)
fig.plot_size(w, h - 1)
fig.subplots(1, 2)
fig.subplot(1, 2).subplots(2, 1)
puppy = fig.subplot(1, 2).subplot(1, 1).image(plt.sample("puppy"))

frame = 0
while True:

    phase = frame % frames / frames                    # where the word is in its crossing, from 0 to 1
    spin = turns * phase % 1                           # where the plots are in their own turn, twice as fast as the word

    w, h = plt.terminal.size(update = True)            # take a fresh terminal size
    if frame: plt.terminal.clean(h)                    # clean the previous frame, hint included

    fig.clear()
    fig.plot_size(w, h - 1)                            # adapt to the terminal, one row spared for the hint
    fig.subplots(1, 2)

    left, right = fig.subplot(1, 1), fig.subplot(1, 2)
    left.subplots(3, 1)
    right.subplots(2, 1)

    # two waves sliding at slightly different speeds, so they drift in and out of step
    sub = left.subplot(1, 1)
    sub.theme("simple")
    sub.draw(sub.signal(plt.sin(periods = 2, phase = 2   * spin),       marker = "fhd").lines().label("sin"))
    sub.draw(sub.signal(plt.sin(periods = 2, phase = 4   * spin + 0.5), marker = "fhd").lines().label("shifted"))
    sub.title(plt.effect("signals", "shimmer", step = frame, period = frames // turns))

    # the two bar groups rising and falling, each pizza a fifth of a turn behind the one before
    sub = left.subplot(2, 1)
    sub.theme("dusk")
    lower = [14 + 6 * math.sin(2 * math.pi * (spin + index / 5)) for index in range(5)]
    upper = [16 + 6 * math.sin(2 * math.pi * (spin + index / 5 + 0.5)) for index in range(5)]
    sub.draw(sub.bar(pizzas, [lower, upper], stacked = True))
    sub.title(plt.effect("stacked bars", "pulse", step = frame, period = frames // turns))

    # three distributions drifting apart and back together
    sub = left.subplot(3, 1)
    sub.theme("matrix")
    drift = 1.5 * math.sin(2 * math.pi * spin)
    sub.draw(sub.hist(plt.noise(length = 10 * samples, offset = 0,             seed = 0), bins = bins))
    sub.draw(sub.hist(plt.noise(length =  6 * samples, offset = 3 + drift,     seed = 1), bins = bins))
    sub.draw(sub.hist(plt.noise(length =  4 * samples, offset = 6 + 2 * drift, seed = 2), bins = bins))
    sub.ruler("y").frequency(0)
    sub.title(plt.effect("histograms", "gradient", step = frame, period = frames // turns))

    # the bundled picture, prepared before the loop
    sub = right.subplot(1, 1)
    sub.axes(False)
    sub.ruler("both").frequency(0)
    sub.draw(puppy)
    sub.title(plt.effect("a very good boy", "rainbow", step = frame, period = frames // turns))

    # the logo scrolling right to left, drawn as a heatmap of its own colors
    sub = right.subplot(2, 1)
    sub.axes(False)
    sub.ruler("both").frequency(0)
    cols, rows = w // 2 + 4, (h - 1) // 2 + 4          # a few cells more than the panel has characters, so none is left blank
    word_cols = round(rows * logo.size[0] / logo.size[1] * 2)
    letters = logo.resize((word_cols, rows)).load()
    shift = round(phase * (word_cols + cols))          # the word travels its own width plus the panel, so the loop closes
    place = lambda col: (col - cols + shift) % (word_cols + cols)
    marquee = [[letters[place(col), row] if place(col) < word_cols else paper for col in range(cols)] for row in range(rows)]
    sub.draw(sub.heatmap(marquee))
    sub.title(plt.effect("heatmaps", "pulse", step = frame, period = frames // turns))

    plt.sleep(0.001)                                   # pause between frames
    fig.show(flush = True)

    if plt.terminal.is_pressed('q'): break             # exit on key press
    print("press q to exit")

    frame += 1
