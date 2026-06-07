# Named colour themes. Each entry is a dict of pre-built pixel objects (canvas + a shared "text" pixel used for frame / ruler / label / legend) plus a cycler sequence (list of pixel objects). Applied via fig.theme(name), which sets these pixels authoritatively (no merge with package defaults — so the `clear` theme can be genuinely colourless).

from plotext._primitives.pixel import pixel


# Base palette (16 default cycler colours) — same source as defaults.pixel_sequence
_default_palette = [12, 10, 9, 14, 13, 11, 0, 15, 8, 7, 1, 2, 3, 4, 5, 6]


# Theme-specific prefix + rest of default palette (de-duplicated). Each theme leads with its own colours then falls back to the standard cycle.
def _seq(*prefix):
    rest = [c for c in _default_palette if c not in prefix]
    return [pixel(foreground = c) for c in list(prefix) + rest]


# Uniform builder: canvas (its own background), text (foreground + background, shared across frame / ruler / label / legend so all chrome reads consistently against the canvas), and the cycler sequence. Missing fields fall back to a blank pixel (no colour) / 16 blank pixels.
def _make(canvas = None, text = None, sequence = None):
    return {
        "canvas":   canvas   if canvas   is not None else pixel(),
        "text":     text     if text     is not None else pixel(),
        "sequence": sequence if sequence is not None else [pixel() for _ in range(16)],
    }


# Windows-style accent sequence (RGB, ported from old plotext)
_windows_seq = [pixel(foreground = c) for c in [(0, 64, 239), (242, 80, 34), (127, 186, 0), (255, 185, 0)]] + _seq()


themes = {
    "default":   _make(pixel(background = "white"),    pixel(foreground = "black",      background = "white"),                       _seq(*_default_palette)),
    "simple":    _make(sequence = _seq(*_default_palette)),                                                                          # colourless chrome, default-coloured signals
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
