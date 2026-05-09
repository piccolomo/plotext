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

# Markers
hd_markers_codes = ['none', 'hd', 'fhd', 'braille']

# Character marker codes — list of names that mirror the keys of
# marker_codes in plotext/_kernel/cpp/utility/5_maps.cpp. Used by
# plotext.markers() to enumerate available named character markers.
# The name-to-glyph resolution itself is handled on the C side.
marker_codes = [
    'sd', 'dot', 'dollar', 'euro', 'bitcoin', 'at', 'heart', 'smile',
    'gclef', 'note', 'shamrock', 'atom', 'snowflake', 'star', 'flower',
    'lightning', 'queen', 'king', 'cross', 'yinyang', 'om', 'osiris',
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
    'eight', 'nine',
]

# Line rendering
line_methods = ['simple', 'full']

# Subplot harmonization policy: when nested subplots disagree, take the
# smallest (everyone fits) or the largest (one grows to accommodate).
size_policies = ['minimum', 'maximum']
