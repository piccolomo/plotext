# Label normalization and formatting utilities

from re import sub

from plotext._primitives.colorize import colorize as colorize_class
from plotext._methods.string import only_spaces


# Normalize a single label
def label(label, default_pixel):
    if label is None or only_spaces(label):
        return None
    if isinstance(label, str):
        label = colorize_class(label).set_pixel(default_pixel)
    label._fix(default_pixel)
    return label


# Normalize list of labels
def labels(labels_value, default_pixel):
    return [label(l, default_pixel) for l in labels_value]


# Fallback label for legend entries: use the signal's own label if non-empty,
# otherwise synthesise "signal[N]" where N is the 0-based index in the plot's
# signal list.
def legend_label(label, length):
    return f'signal[{length}]' if len(label) == 0 else label


# Clean and format documentation string
def doc(doc, capitalize=1):
    doc = doc.strip()
    if doc and doc[-1] != '.':
        doc += '.'
    doc = sub(r'\s+', ' ', doc)
    return doc[0].upper() + doc[1:] if capitalize else doc[0].lower() + doc[1:]