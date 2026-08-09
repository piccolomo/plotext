# Enum-style constants: named sets of allowed values for axes, alignment, scales, styles, colors and markers

from plotext._settings.system import platform

# Axes and layout
axis_names = ['x', 'y']

xsides = ['lower', 'upper']
ysides = ['left', 'right']

orientations = ['vertical', 'horizontal']
orientations_short = ['v', 'h']

# Alignment
horizontal_alignments       = ['left', 'center', 'right']
horizontal_alignments_short = ['l',    'c',      'r']
vertical_alignments         = ['top',  'center', 'bottom']
vertical_alignments_short   = ['t',    'c',      'b']
alignments_int              = [-1, 0, 1]

# Scales and limits
scales = ['linear', 'log']
limit_alignments = ['center', 'edge']

# Styles
line_styles = ['default', 'double', 'heavy', 'dotted', 'rounded']                              # index = C kernel line_normal/double/heavy/dotted/rounded

style_codes = [
    'bold', 'dim', 'italic', 'underline',
    'double-underline', 'strike', 'inverted', 'flash']

# Colors
color_codes = [
    'black', 'white', 'gray', 'gray+',
    'red', 'red+', 'green', 'green+',
    'orange', 'orange+', 'blue', 'blue+',
    'magenta', 'magenta+', 'cyan', 'cyan+']

# Colormaps: lookup tables of (r, g, b) stops used by heatmap()
viridis = [(68, 1, 84), (72, 24, 106), (71, 45, 123), (65, 68, 135),
           (57, 86, 140), (49, 104, 142), (42, 120, 142), (36, 136, 142),
           (31, 152, 139), (34, 168, 132), (53, 183, 121), (84, 197, 104),
           (122, 209, 81), (165, 219, 54), (212, 225, 25), (253, 231, 37)]

# Markers: the higher resolution codes, fhd missing on windows, its characters not fitting in a windows one, so there the word is drawn as text like any unknown marker
hd_markers_codes = ['hd', 'fhd', 'braille'] if platform == 'unix' else ['hd', 'braille']

# The named character codes, as heart or star, the same names held on the C side, which turns each into its glyph; markers() prints them all.
symbol_codes = [
    'full', 'brick', 'dot', 'dollar', 'euro', 'bitcoin', 'at',
    'heart', 'smile', 'shamrock', 'atom',
    'snowflake', 'sun', 'cloud', 'umbrella', 'zigzag',
    'star', 'emptystar', 'flower',
    'queen', 'king', 'cross', 'yinyang', 'om',
    'square', 'emptysquare', 'circle', 'emptycircle', 'diamond', 'emptydiamond',
    'up', 'down', 'left', 'right',
    'arrowup', 'arrowdown', 'arrowleft', 'arrowright',
    'infinity', 'check', 'xmark',
    'eighth', 'beamed', 'flat', 'sharp',
]

# Line rendering
line_methods = ['simple', 'full']

# Targets for signal.density(): apply the chosen line method to the connecting lines, to the stem fills, or to both at once.
line_method_scopes = ['line', 'fill', 'both']

# When subplots ask for different sizes, take the smallest, so every one fits, or the largest, so one grows.
size_policies = ['minimum', 'maximum']
size_policies_short = ['min', 'max']

# Text effects (used by plotext.effect)
effect_names = ['shimmer', 'pulse', 'rainbow', 'gradient']

# Candlestick body styles (consumed by fig.candlestick): candle = filled body, ohlc = open/close ticks
candlestick_styles = ['candle', 'ohlc']
