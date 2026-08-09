# Step-driven text effects: a single dispatcher that returns a styled 1-row matrix.

from math import exp, sin, pi
from colorsys import hsv_to_rgb
from plotext._primitives.matrix import matrix
from plotext._primitives.pixel  import pixel
from plotext._correct.enums import effect_name


# Apply effect `name` to `text` at animation `step`; returns a styled 1-row matrix. The effect repeats every `period` step units; None picks each effect's own default.
def effect(text, name = "shimmer", step = 0.0, period = None):
    name = effect_name(name)
    if name == "shimmer":  return get_shimmer_effect(text, step, period = period)
    if name == "pulse":    return get_pulse_effect(text, step, period = period)
    if name == "rainbow":  return get_rainbow_effect(text, step, period = period)
    if name == "gradient": return get_gradient_effect(text, step, period = period)


# Gaussian bright spot sweeping across the text at position `step` (in chars); repeats every `period` chars (None uses the text length).
def get_shimmer_effect(text, step, color = (60, 60, 90), highlight = (255, 255, 255), width = 2.0, wrap = True, period = None):
    length = len(text)
    period = length if period is None else period
    colors = []
    for i in range(length):
        scale = get_shimmer_scale(i - step, period, width, wrap)
        colors.append(rgb_mix(color, highlight, scale))
    return get_single_row_matrix(text, colors)


# Whole-string brightness oscillates between `color` and `highlight` with sine period `period` (None uses 10).
def get_pulse_effect(text, step, color = (120, 120, 200), highlight = (255, 255, 255), period = None):
    period = 10.0 if period is None else period
    scale  = get_pulse_scale(step, period)
    rgb    = rgb_mix(color, highlight, scale)
    colors = [rgb] * len(text)
    return get_single_row_matrix(text, colors)


# Hue cycles across chars; advancing `step` scrolls the pattern; repeats every `period` units (None uses 10).
def get_rainbow_effect(text, step, period = None, saturation = 1.0, brightness = 1.0):
    period = 10.0 if period is None else period
    colors = []
    for i in range(len(text)):
        hue     = get_rainbow_hue(i + step, period)
        r, g, b = hsv_to_rgb(hue, saturation, brightness)
        colors.append((int(r * 255), int(g * 255), int(b * 255)))
    return get_single_row_matrix(text, colors)


# Gradient wave: sinusoidal blend between `start` and `end` along the text; advancing `step` scrolls the wave.
def get_gradient_effect(text, step = 0.0, period = None, start = (255, 100, 50), end = (50, 150, 255)):
    period = max(2, len(text)) if period is None else period
    colors = []
    for i in range(len(text)):
        scale = get_gradient_scale(i + step, period)
        colors.append(rgb_mix(start, end, scale))
    return get_single_row_matrix(text, colors)


# Gaussian intensity at signed offset `index` for the shimmer effect; wraps around every `period` units when `wrap = True`.
def get_shimmer_scale(index, period, std, wrap = True):
    dist = ((index + period / 2) % period) - period / 2 if wrap else index      # nearest periodic distance when wrap
    return exp(-(dist / std) ** 2)


# Sine-wave intensity at time `step` for the pulse effect; full cycle every `period` units.
def get_pulse_scale(step, period):
    return (1 + sin(2 * pi * step / period)) / 2


# Hue at signed offset `index` for the rainbow effect; cycles every `period` units, returns a float in [0, 1).
def get_rainbow_hue(index, period):
    return (index % period) / period


# Sine-wave intensity at signed offset `index` for the gradient effect; full cycle every `period` units.
def get_gradient_scale(index, period):
    return (sin(2 * pi * index / period) + 1) / 2


# Mix two RGB colors: scale = 0 returns rgb1, scale = 1 returns rgb2, 0.5 the midpoint.
def rgb_mix(rgb1, rgb2, scale):
    return tuple(int(a + (b - a) * scale) for a, b in zip(rgb1, rgb2))


# Build a 1-row matrix where char i gets foreground colors[i].
def get_single_row_matrix(text, colors):
    m = matrix(len(text), 1)
    for i, (ch, rgb) in enumerate(zip(text, colors)):
        m._set_pixelled_character(i, 0, ch, pixel(foreground = rgb))
    return m
