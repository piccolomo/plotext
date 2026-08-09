# The named color themes: each holds the pixels of the canvas, axes, ruler, label and legend, plus the sequence given to the signals; theme(name) writes them as they are, so the colorless one really removes every color, and the default one, taking the package defaults, restores the look out of the box.

from plotext._primitives.pixel import pixel
from plotext._correct.pixel import pixel_par as correct_pixel
from plotext._settings import defaults


# The 16 colors given to the signals in turn, the same as defaults.pixel_sequence
_default_palette = [12, 10, 9, 14, 13, 11, 0, 15, 8, 7, 1, 2, 3, 4, 5, 6]


# The colors of a theme first, then the remaining default ones, each color appearing once.
def _seq(*prefix):
    rest = [c for c in _default_palette if c not in prefix]
    return [pixel(foreground = c) for c in list(prefix) + rest]


# Build a theme from its canvas background, the one text pixel shared by axes, ruler, label, legend and grid, and its color sequence; anything missing stays without color.
def _make(canvas = None, text = None, sequence = None, grid = None):
    text = text if text is not None else pixel()
    return {
        "canvas":   canvas   if canvas   is not None else pixel(),
        "axes":     text,
        "ruler":    text,
        "label":    text,
        "legend":   text,
        "grid":     grid     if grid     is not None else text,
        "sequence": sequence if sequence is not None else [pixel() for _ in range(16)],
    }


# Promote a user sequence: color codes become pixels, pixel objects pass through; the standard palette follows, skipping the codes already given
def _sequence(entries):
    entries = list(entries)
    rest = [c for c in _default_palette if c not in entries]
    return [entry if isinstance(entry, pixel) else pixel(foreground = entry) for entry in entries] + [pixel(foreground = c) for c in rest]


# Register a custom theme under the given name, overwriting any existing entry: canvas takes the canvas background color, text one pixel (in any accepted form) shared by axes, rulers, labels and legend, sequence the signal colors (color codes or pixels, completed with the standard palette), and grid the grid lines pixel, the text one when not given
def add_theme(name, canvas = None, text = None, sequence = None, grid = None):
    canvas = pixel(background = canvas) if canvas is not None else None
    text = correct_pixel(text) if text is not None else None
    grid = correct_pixel(grid) if grid is not None else None
    sequence = _sequence(sequence) if sequence is not None else None
    themes[name] = _make(canvas, text, sequence, grid)


# Windows-style accent sequence (RGB, ported from old plotext)
_windows_seq = [pixel(foreground = c) for c in [(0, 64, 239), (242, 80, 34), (127, 186, 0), (255, 185, 0)]] + _seq()


themes = {
    "default":   {"canvas": defaults.pixels["canvas"], "axes": defaults.pixels["axis"], "ruler": defaults.pixels["ruler"],
                  "label": defaults.pixels["label"], "legend": defaults.pixels["legend"], "grid": defaults.pixels["grid"],
                  "sequence": defaults.pixel_sequence},
    "simple":    _make(sequence = _seq(*_default_palette)),                                                                          # no colors on the frame, signals on the default sequence
    "colorless": _make(),
    "dusk":      _make(pixel(background = 66),         pixel(foreground = 216,          background = 4, style = "bold"),             _seq(111, 174, 186)),
    "sand":      _make(pixel(background = 180),        pixel(foreground = 184,          background = 24, style = "bold"),            _seq(39, 202, 228)),
    "wine":      _make(pixel(background = 95),         pixel(foreground = 190,          background = 52, style = "bold"),            _seq(27, 34, 52)),
    "garden":    _make(pixel(background = 95),         pixel(foreground = 221,          background = 22, style = "bold"),            _seq(142, 124, 57)),
    "dark":      _make(pixel(background = "black"),    pixel(foreground = "orange",     background = "black"),                       _seq("blue", 22, 54)),
    "dreamland": _make(pixel(background = 180),        pixel(foreground = 221,          background = 2, style = "bold"),             _seq(6, 125, 190)),
    "retro":     _make(pixel(background = 250),        pixel(foreground = 186,          background = 234),                           _seq(21, 41, 196)),
    "windows":   _make(pixel(background = "gray+"),    pixel(foreground = "black",      background = "gray+"),                       _windows_seq),
    "matrix":    _make(pixel(background = (13, 2, 8)), pixel(foreground = (0, 255, 65), background = (13, 2, 8), style = "bold"),    [pixel(foreground = c) for c in [(0, 255, 65), (0, 143, 17), (0, 59, 0)]] + _seq()),
}
