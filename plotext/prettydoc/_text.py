# Internal imports
from plotext._methods.string import *
from plotext._constants import space


# Class for managing text and its properties
class text_class:
    def __init__(self, text = None):
        self.set(text)

    # Set the text value
    def set(self, text = None):
        self.text = text
        return self

    # Set the string content of the text object
    def set_string(self, string):
        self.text.set_string(string)
        return self

    # Set the pixel used for the text
    def set_pixel(self, pixel):
        self.text.set_pixel(pixel)
        return self

    # Get the pixel from the text
    def get_pixel(self):
        return self.text.get_pixel()

    # Check whether the text is empty
    def empty(self):
        return self.text is None

    # Get the underlying text object
    def get(self):
        return self.text

    # Get the string representation (colorless or not)
    def get_string(self, colorless = 0):
        return None if self.empty() else self.get().get_string(colorless)

    # Get formatted docstring with optional prefix
    def get_docstring(self, prefix = None):
        return add_prefix(self.get_string(), prefix)

    # Return a copy of the object
    def copy(self):
        out = text_class()
        out.set(self.get())
        return out

    def __repr__(self):
        return "PrettyText: " + self.get_string()


# Class for managing labeled text (label + value)
class labelled_text_class:
    def __init__(self, label = None, text = None):
        self.label = text_class(label)
        self.value = text_class(text)
        self.set_separator()

    # Set the label part
    def set_label(self, label = None):
        self.label.set(label)
        return self

    # Set the value part
    def set_value(self, value = None):
        self.value.set(value)
        return self

    # Set the separator between label and value
    def set_separator(self, separator = None):
        self.separator = space if separator is None else separator

    # Get formatted docstring combining label and value
    def get_docstring(self, prefix = None):
        docs = [] if self.value.empty() else [self.label.get_docstring(), self.value.get_docstring()]
        doc = connect_strings(docs, self.separator)
        return add_prefix(doc, prefix)

    # Return a copy of the object
    def copy(self):
        out = labelled_text_class()
        out.label = self.label.copy()
        out.value = self.value.copy()
        out.set_separator(self.separator)
        return out


# Class for managing aliases of text
class alias_class(text_class):
    def __init__(self, alias = None):
        text_class.__init__(self, alias)

    # Return a docstring indicating alias nature
    def get_docstring(self, prefix = None):
        doc = None if self.empty() else "The " + self.get_string() + '() method is an alias.'
        return add_prefix(doc, prefix)
