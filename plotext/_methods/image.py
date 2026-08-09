# Direct heatmap / image painters: produce a fully-coloured plotext.matrix without going through the signal pipeline. Faster than fig.heatmap / fig.image, caller just print()s the returned matrix.

import time
from plotext._settings.system import Image, ImageOps, ImageSequence

from plotext._primitives.matrix import matrix as matrix_class
from plotext._primitives.pixel import pixel as pixel_class
from plotext._primitives.marker import marker as marker_class
from plotext._correct.data import matrix as correct_matrix
from plotext._correct.heatmap import colormap as correct_colormap, symbol as correct_symbol
from plotext._methods.file import correct as _correct_path
from plotext._methods.object import is_rgb
from plotext._methods.string import note


# A monospace terminal cell is roughly twice as tall as it is wide. When we preserve the aspect ratio of an image we need to compensate for that or square images come out visibly stretched vertically.
_char_ratio = 2.0                                                                   # height / width of a single terminal cell


# Paint a 2D matrix into a plotext.matrix; numeric input is colormapped, RGB input passes through.
def heatmap(data, map = 'gray', symbol = None):
    rows, cols, m = correct_matrix(data)
    if not m: return matrix_class(0, 0, pixel_class())
    rgb = m if is_rgb(m[0][0]) else correct_colormap(m, map)
    char = marker_class(correct_symbol(symbol))._get_model()
    out = matrix_class(cols, rows, pixel_class())
    for r in range(rows):
        for c in range(cols):
            out._set_pixelled_character(c, r, char, pixel_class(rgb[r][c]))         # matrix-grid coords (row 0 at top of print)
    return out


# Resolve target (width, height) for terminal rendering. None falls back to the terminal dim; user values are clamped against the terminal only when plt.terminal.limit is on for that axis. When src=(sw, sh) is provided and ratio=True, the result is further reduced so the source aspect is preserved (with _char_ratio compensation).
def _resolve_size(width, height, src = None, ratio = False):
    from plotext._kernel.api import terminal
    tw, th = terminal.size(update = True)
    lw, lh = terminal._limit
    width  = tw if width  is None else (min(width,  tw) if lw else width)
    height = th if height is None else (min(height, th) if lh else height)
    if ratio and src is not None:
        sw, sh = src
        scale = min(width / sw, (height * _char_ratio) / sh)
        width  = max(1, int(sw * scale))
        height = max(1, int(sh * scale / _char_ratio))
    return width, height


# Render an already-opened PIL.Image into a painted plotext.matrix at the resolved size; shared by image() and gif() (and video frames).
def _render_image(img, gray, ratio, width, height):
    if gray: img = ImageOps.grayscale(img)
    img = img.convert('RGB')
    width, height = _resolve_size(width, height, img.size, ratio)
    img = img.resize((width, height))
    pixels = list(img.getdata())
    return heatmap([list(pixels[r * width : (r + 1) * width]) for r in range(height)])


# Open an image file (local path, "~/…", or http/https URL, _correct_path downloads URLs once and caches the result) via Pillow and paint it into a plotext.matrix.
def image(path, gray = False, width = None, height = None, ratio = True):
    if Image is None:
        note("plotext.image", 'images need the image extra: pip install "plotext[image]"', "error")
        return
    return _render_image(Image.open(_correct_path(path)), gray, ratio, width, height)


# A colored "press q to exit" hint: q in bold red, on a discrete black label (fix_background fills the otherwise-unset cell backgrounds).
def _exit_hint():
    from plotext._primitives.colorize import colorize
    hint = colorize("press ", pixel = "white").hstack(colorize("q", pixel = ("red", None, "bold"))).hstack(colorize(" to exit", pixel = "white"))
    return hint._fix_background(pixel_class(background = "black"))


# Animate a GIF (local path, "~/…", or http/https URL, _correct_path downloads URLs once and caches the result): decode each frame on the fly, paint, print, sleep only the remainder of the GIF's per-frame duration. Press q to exit; seconds, when given, stops the stream after that many seconds. Terminal resizes apply automatically.
def gif(path, gray = False, width = None, height = None, ratio = True, loop = False, seconds = None, _hint = True):
    if Image is None:
        note("plotext.gif", 'gifs need the image extra: pip install "plotext[image]"', "error")
        return
    from plotext._kernel.api import terminal
    img = Image.open(_correct_path(path))
    hint = _exit_hint()
    quit_time = None if seconds is None else time.time() + seconds
    prev_height = 0
    while True:
        for frame in ImageSequence.Iterator(img):
            if terminal.is_pressed('q'): return
            if quit_time is not None and time.time() > quit_time: return
            start = time.perf_counter()
            matrix = _render_image(frame, gray, ratio, width, height)
            if _hint: matrix.insert(0, matrix.height() - 1, hint)   # overwrite the bottom-left with the exit hint (in place, no extra row)
            if prev_height: terminal.clean(prev_height)                  # up exactly the printed rows (frame need not fill the screen)
            matrix.print()
            prev_height = matrix.height()
            frame_time = img.info.get('duration', 100) / 1000
            paint_time = time.perf_counter() - start
            if paint_time < frame_time: time.sleep(frame_time - paint_time)
        if not loop: return
