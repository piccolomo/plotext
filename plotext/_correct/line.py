# Line style validation utilities

from plotext._settings.constants.enums import line_styles


# Validate line style, falling back to the first available style
def line_style(style):
    return style if style in line_styles else line_styles[0]
