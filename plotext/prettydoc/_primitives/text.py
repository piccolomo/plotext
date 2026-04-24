# Text primitives: text_class, alias_class and labelled_text_class used to build docstring components

from plotext._methods.string import add_prefix, connect_strings
from plotext._settings.constants.text import space


# Wrapper around a colorize (or None) value used as a docstring text fragment
class text_class:
    # Initialize with an optional text value
    def __init__(self, text = None):
        self._set(text)

    # Set the text value
    def _set(self, text = None):
        self._text = text
        return self

    # Set the string content of the text object
    def _set_string(self, string):
        self._text.set_string(string)
        return self

    # Set the pixel used for the text
    def _set_pixel(self, pixel):
        self._text.set_pixel(pixel)
        return self

    # Get the pixel from the text
    def _get_pixel(self):
        return self._text.get_pixel()

    # Check whether the text is empty
    def _empty(self):
        return self._text is None

    # Get the string representation (colorless or not)
    def _get(self, colorless = 0):
        return None if self._empty() else self._text.get_string(colorless)

    # Get formatted docstring with optional prefix
    def _get_docstring(self, prefix = None):
        return add_prefix(self._get(), prefix)

    # Return a copy of the object
    def _copy(self):
        out = text_class()
        out._text = self._text
        return out

    # Representation
    def __repr__(self):
        return f"PrettyText: {self._get()}"


# Text variant that renders as "The foo() method is an alias."
class alias_class(text_class):
    # Initialize with an optional alias name
    def __init__(self, alias = None):
        text_class.__init__(self, alias)

    # Return a docstring indicating alias nature
    def _get_docstring(self, prefix = None):
        doc = None if self._empty() else "The " + self._get() + '() method is an alias.'
        return add_prefix(doc, prefix)

    # Representation
    def __repr__(self):
        return f"PrettyAlias: {self._get()}"


# Pair of label + value text fragments, joined by a separator
class labelled_text_class:
    # Initialize with optional label and text
    def __init__(self, label = None, text = None):
        self._label = text_class(label)
        self._value = text_class(text)
        self._set_separator()

    # Set the label part
    def _set_label(self, label = None):
        self._label._set(label)
        return self

    # Set the value part
    def _set_value(self, value = None):
        self._value._set(value)
        return self

    # Get the label part as string
    def _get_label(self, colorless = 0):
        return self._label._get(colorless)

    # Get the value part as string
    def _get_value(self, colorless = 0):
        return self._value._get(colorless)

    # Set the separator between label and value
    def _set_separator(self, separator = None):
        self._separator = space if separator is None else separator

    # Get formatted docstring combining label and value
    def _get_docstring(self, prefix = None):
        docs = [] if self._value._empty() else [self._label._get_docstring(), self._value._get_docstring()]
        doc = connect_strings(docs, self._separator)
        return add_prefix(doc, prefix)

    # Return a copy of the object
    def _copy(self):
        out = labelled_text_class()
        out._label = self._label._copy()
        out._value = self._value._copy()
        out._set_separator(self._separator)
        return out

    # Representation
    def __repr__(self):
        out = f"PrettyLabelledText"
        out += f"\n label: {self._get_label()}"
        out += f"\n value: {self._get_value()}"
        return out
