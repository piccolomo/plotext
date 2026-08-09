# Rebuilding the guide pictures

The pictures in `docs/source/images/` are captures of real plotext output. Three tools make them, all run from the repository root, with plotext importable and Pillow installed.

## render_ansi.py

Turns a file of colored terminal text into a png, painting the block characters as exact rectangles instead of letting a font draw them, so the plots come out sharp.

    python3 -c "import plotext as plt; plt.figure.draw(plt.figure.signal(plt.sin())); open('/tmp/plot.ansi', 'w').write(plt.figure.build().string())"
    python3 docs/render/render_ansi.py /tmp/plot.ansi docs/source/images/plot.png

The recipe for a still picture: write the plot to a file with `figure.build().string()`, then hand that file to this tool. Every still on the guide pages was made this way, at `plot_size(80, 22)` unless the page says otherwise.

Braille markers are not supported: they come out as dots rather than as the font would draw them.

## animate.py

Records one of the guide animations, by running its example itself with the terminal calls replaced, so that every frame is captured rather than printed. It takes the example, the picture to write, how many frames make one loop, and optionally the terminal size to record at.

    python3 docs/render/animate.py docs/source/code/heatmap_rain.py images/rain.webp 16 200 46

The animations are saved as **webp**, not gif: a gif is limited to 256 colors and has to throw the rest away, which shows badly on a plot, while a webp keeps them all and comes out several times smaller. The moonwalk went from 3.8 MB as a gif to 0.6 MB as a webp.

An animation must **close on itself**, or the loop jumps at the seam. That means every wave sliding a whole number of cycles over the loop, every title effect given `period = frames`, and anything born during the loop dying inside it.

## showcase_animation.py

Records the front page animation, `docs/source/images/showcase.webp`, from `docs/source/code/showcase.py`, at a terminal of 310 x 70 over 32 frames.

    python3 docs/render/showcase_animation.py

It differs from `animate.py` only in fixing that example's picture path, which the example writes relative to its own folder.

## moonwalk.webp

Recorded frame by frame from the sample video: the frames were decoded with `ffpyplayer`, each one drawn by `figure.image()` at a full terminal, then rendered through `render_ansi.py` and assembled. No script is kept for it, since it needs the video downloaded first.
