# Enum-style constants: named sets of allowed values for axes, alignment, scales, styles, colors and markers

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
axis_styles = ['default', 'double', 'dotted', 'rounded']
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

# Markers
hd_markers_codes = ['none', 'hd', 'fhd', 'braille']

# Character symbol codes — list of names that mirror the keys of
# symbol_codes in plotext/_kernel/cpp/utility/5_maps.cpp. Used by
# plotext.markers() to enumerate available named character symbols.
# The name-to-glyph resolution itself is handled on the C side.
symbol_codes = [
    'block', 'dot', 'dollar', 'euro', 'bitcoin', 'at',
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

# Subplot harmonization policy: when nested subplots disagree, take the
# smallest (everyone fits) or the largest (one grows to accommodate).
size_policies = ['minimum', 'maximum']

# Text effects (used by plotext.effect)
effect_names = ['shimmer', 'pulse', 'rainbow', 'gradient']
