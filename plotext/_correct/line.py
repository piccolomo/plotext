# Line style validation utilities

from plotext._constants.enums import line_styles


# Validate line style and return its index (matches C kernel line_normal/double/heavy/dotted/rounded constants), falling back to 0 ("default") for unknown values
def line_style(style):
    return line_styles.index(style) if style in line_styles else 0
