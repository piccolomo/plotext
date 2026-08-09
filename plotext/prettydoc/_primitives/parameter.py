# One documented parameter, or one output: its name and description, and the type and default printed under them.

from plotext.prettydoc._primitives.text import text_class, labeled_text_class
from plotext._constants.text import new_line
from plotext._methods.string import add_prefix, connect_strings


# One documented parameter: name + description, with optional type and default
class parameter_class:
    # Start with the given name and description, the type and default still empty.
    def __init__(self, name = None, doc = None):
        self._name = labeled_text_class()._set_label(name)._set_value(doc)
        self._type = labeled_text_class()
        self._default = labeled_text_class()

    # Set what sits between each field label and its value, as the colon of "type: a numeric value".
    def _set_separator(self, separator = None):
        for field in (self._name, self._type, self._default):
            field._set_separator(separator)
        return self

    # Set the type and the default of the parameter, each left as it is when not given, and removed when given as an empty string.
    def _set_spec(self, type = None, default = None):
        if type is not None:
            self._type._set_value(None if type == '' else type)
        if default is not None:
            self._default._set_value(None if default == '' else default)
        return self

    # Replace the word "type" printed before the type.
    def _set_type_label(self, label = None):
        self._type._label._set(label)
        return self

    # Replace the word "default" printed before the default value.
    def _set_default_label(self, label = None):
        self._default._label._set(label)
        return self

    # The parameter name as a string.
    def _get_name(self, colorless = 0):
        return self._name._get_label(colorless)

    # The type as a string.
    def _get_type(self, colorless = 0):
        return self._type._get_value(colorless)

    # The default value as a string.
    def _get_default(self, colorless = 0):
        return self._default._get_value(colorless)

    # The type and default lines, the default going on its own line under the type.
    def _get_specs_docstring(self, prefix = None):
        docs = [self._type._get_docstring(), self._default._get_docstring(new_line)]
        doc = connect_strings(docs)
        return add_prefix(doc, prefix)

    # The whole parameter as it appears in the docstring: its name and description, then its type and default.
    def _get_docstring(self, prefix = None):
        docs = [self._name._get_docstring(), self._get_specs_docstring(new_line)]
        doc = connect_strings(docs)
        return add_prefix(doc, prefix)

    # A copy of this parameter, sharing nothing with it.
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
