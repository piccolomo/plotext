# Label normalization and formatting utilities

from re import sub

from plotext._primitives.colorize import colorize as colorize_class
from plotext._primitives.matrix   import matrix   as matrix_class
from plotext._methods.string import only_spaces


# Normalize a single label (str / colorize / matrix / None) into a 1-row matrix ready to wrap in a marker. None passes through (means "no label"). Cells get `default_pixel`'s background where they don't already have one; with no pixel given the label keeps the colors it carries, to be painted later, when it is drawn.
def label(label, default_pixel = None):
    if label is None: return None
    if isinstance(label, matrix_class):
        label = label.copy()                                                         # don't mutate the caller's matrix
        label._fix(default_pixel) if default_pixel is not None else None
        return label
    if isinstance(label, str):
        if only_spaces(label): return None
        label = colorize_class(label)
        label.fill(default_pixel) if default_pixel is not None else None
    label._fix(default_pixel) if default_pixel is not None else None
    return label.matrix()


# Normalize list of labels
def labels(labels_value, default_pixel = None):
    return [label(l, default_pixel) for l in labels_value]



# Clean and format documentation string
def doc(doc, capitalize = 1):
    doc = doc.strip()
    if doc and doc[-1] != '.':
        doc += '.'
    doc = sub(r'[ \t]+', ' ', doc)
    doc = sub(r' ?\n ?', '\n', doc)
    return doc[0].upper() + doc[1:] if capitalize else doc[0].lower() + doc[1:]