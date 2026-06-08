# Parameter primitive: a function parameter or output with name, type and default fields

from plotext.prettydoc._primitives.text import text_class, labelled_text_class
from plotext._constants.text import new_line, comma
from plotext._methods.string import add_prefix, connect_strings


# One documented parameter: name + description, with optional type and default
class parameter_class:
    # Initialize name, type, and default attributes with labelled text
    def __init__(self, name = None, doc = None):
        self._name = labelled_text_class()._set_label(name)._set_value(doc)
        self._type = labelled_text_class()
        self._default = labelled_text_class()

    # Set the separator symbol for all fields
    def _set_separator(self, separator = None):
        self._name._set_separator(separator)
        self._type._set_separator(separator)
        self._default._set_separator(separator)
        return self

    # Set type and default values
    def _set_spec(self, type = None, default = None):
        self._type._set_value(type)
        self._default._set_value(default)
        return self

    # Set custom label for the type field
    def _set_type_label(self, label = None):
        self._type._label._set(label)
        return self

    # Set custom label for the default field
    def _set_default_label(self, label = None):
        self._default._label._set(label)
        return self

    # Return the name label string
    def _get_name(self, colorless = 0):
        return self._name._get_label(colorless)

    # Return the type value string
    def _get_type(self, colorless = 0):
        return self._type._get_value(colorless)

    # Return the default value string
    def _get_default(self, colorless = 0):
        return self._default._get_value(colorless)

    # Get combined docstring for type and default, with optional prefix
    def _get_specs_docstring(self, prefix = None):
        docs = [self._type._get_docstring(), self._default._get_docstring(comma)]
        doc = connect_strings(docs)
        return add_prefix(doc, prefix)

    # Get full docstring including name and specs, with optional prefix
    def _get_docstring(self, prefix = None):
        docs = [self._name._get_docstring(), self._get_specs_docstring(new_line + ' ')]
        doc = connect_strings(docs)
        return add_prefix(doc, prefix)

    # Return a deep copy of the parameter
    def _copy(self):
        out = parameter_class()
        out._name = self._name._copy()
        out._type = self._type._copy()
        out._default = self._default._copy()
        return out

    # Representation
    def __repr__(self):
        out = f"PrettyParameter"
        out += f"\n name: {self._get_name()}"
        out += f"\n type: {self._get_type()}"
        out += f"\n default: {self._get_default()}"
        return out
