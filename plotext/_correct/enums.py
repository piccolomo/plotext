# Validation utilities for the names listed in _constants/enums.py: effect, candlestick style and line style.

from plotext._constants.enums import effect_names, candlestick_styles, line_styles


# Validate an effect name against the allowed ones, anything unknown giving the first.
def effect_name(name):
    return name if name in effect_names else effect_names[0]


# Validate a candlestick style against the allowed ones, anything unknown giving the first, 'candle'.
def style(name):
    return name if name in candlestick_styles else candlestick_styles[0]


# Validate a line style and return its position in the allowed ones, an already valid position passing through, anything unknown giving 0, the default style.
def line_style(style):
    return line_styles.index(style) if style in line_styles else style if style in range(len(line_styles)) else 0
