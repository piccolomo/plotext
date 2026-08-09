# The text pieces a docstring is built from: a plain piece, the alias line, and a label with its value, as in "type: a numeric value".

from plotext._methods.string import add_prefix, connect_strings
from plotext._constants.text import space


# One piece of text of a docstring, held as a colorize object, or nothing at all.
class text_class:
    # Start with the given text, or with nothing.
    def __init__(self, text = None):
        self._set(text)

    # Replace the text.
    def _set(self, text = None):
        self._text = text
        return self

    # Paint the text with the given pixel.
    def _set_pixel(self, pixel):
        self._text.fill(pixel)
        return self

    # The pixel painting the text.
    def _get_pixel(self):
        return self._text.pixel()

    # True when there is no text at all.
    def _empty(self):
        return self._text is None

    # The text as a string, with its colors or without them.
    def _get(self, colorless = 0):
        return None if self._empty() else self._text.string(colorless)

    # The text as it appears in the docstring, after the given prefix.
    def _get_docstring(self, prefix = None):
        return add_prefix(self._get(), prefix)

    # A copy of this piece.
    def _copy(self):
        out = text_class()
        out._text = self._text
        return out

    # Representation
    def __repr__(self):
        return f"PrettyText({self._get()})"


# The alias piece, printing as "The mean() method is an alias." for the alias mean.
class alias_class(text_class):
    # Start with the given alias name, or with nothing.
    def __init__(self, alias = None):
        text_class.__init__(self, alias)

    # The alias line, or nothing when no alias was given.
    def _get_docstring(self, prefix = None):
        doc = None if self._empty() else "The " + self._get() + '() method is an alias.'
        return add_prefix(doc, prefix)

    # Representation
    def __repr__(self):
        return f"PrettyAlias({self._get()})"


# A label and its value, printed together as "type: a numeric value".
class labeled_text_class:
    # Start with the given label and value, each optional.
    def __init__(self, label = None, text = None):
        self._label = text_class(label)
        self._value = text_class(text)
        self._set_separator()

    # Replace the label, the word before the separator.
    def _set_label(self, label = None):
        self._label._set(label)
        return self

    # Replace the value, the text after the separator.
    def _set_value(self, value = None):
        self._value._set(value)
        return self

    # The label as a string, with its colors or without them.
    def _get_label(self, colorless = 0):
        return self._label._get(colorless)

    # The value as a string, with its colors or without them.
    def _get_value(self, colorless = 0):
        return self._value._get(colorless)

    # Set what sits between the label and the value, a space when not given.
    def _set_separator(self, separator = None):
        self._separator = space if separator is None else separator

    # The label and value together, after the given prefix; nothing at all when the value is missing.
    def _get_docstring(self, prefix = None):
        docs = [] if self._value._empty() else [self._label._get_docstring(), self._value._get_docstring()]
        doc = connect_strings(docs, self._separator)
        return add_prefix(doc, prefix)

    # A copy of this piece.
    def _copy(self):
        out = labeled_text_class()
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
