# Internal imports
from plotext.prettydoc._text import text_class, labelled_text_class
from plotext._constants import new_line, comma
from plotext._methods.string import * 



class parameter_class:

    # Initialize name, type, and default attributes with labelled text
    def __init__(self, name = None, doc = None):
        self.name = labelled_text_class().set_label(name).set_value(doc)
        self.type = labelled_text_class()
        self.default = labelled_text_class()


    # Set the separator symbol for all fields
    def set_separator(self, separator = None):
        self.name.set_separator(separator)
        self.type.set_separator(separator)
        self.default.set_separator(separator)
        return self


    # Set type and default values
    def set_spec(self, type = None, default = None):
        self.type.set_value(type)
        self.default.set_value(default)
        return self


    # Set custom label for the type field
    def set_type_label(self, label = None):
        self.type.label.set(label)
        return self

    # Set custom label for the default field
    def set_default_label(self, label = None):
        self.default.label.set(label)
        return self


    # Return the name label string
    def get_name(self):
        return self.name.label.get_string(1)


    # Get combined docstring for type and default, with optional prefix
    def get_specs_docstring(self, prefix = None):
        docs = [self.type.get_docstring(), self.default.get_docstring(comma)]
        doc = connect_strings(docs)
        return add_prefix(doc, prefix)


    # Get full docstring including name and specs, with optional prefix
    def get_docstring(self, prefix = None):
        docs = [self.name.get_docstring(), self.get_specs_docstring(new_line)]
        doc = connect_strings(docs)
        return add_prefix(doc, prefix)


    # Return a deep copy of the parameter
    def copy(self):
        out = parameter_class()
        out.name = self.name.copy()
        out.type = self.type.copy()
        out.default = self.default.copy()
        return out

