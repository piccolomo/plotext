# Candlestick style validation

from plotext._constants.enums import candlestick_styles


# Validate candlestick style name against allowed names; falls back to default ('candle') if unknown.
def style(name):
    return name if name in candlestick_styles else candlestick_styles[0]
