# Function primitive: wraps one or more Python callables with a prettydoc docstring (doc, alias, parameters, output)

from plotext.prettydoc._primitives.text import text_class, alias_class
from plotext.prettydoc._primitives.parameter import parameter_class
from plotext._constants.text import space, empty, new_line
from plotext._methods.string import connect_strings, new_lines, uncolorize
from plotext._primitives.colorize import colorize


# One documented callable (or list of aliased callables) with its full docstring layout
class function_class:
    # Initialize wrapper around one or more functions
    def __init__(self, *function, name = None, section = None):
        self._function = list(function)
        self._set_name(function[0], name)
        self._section = section
        self._doc = text_class()
        self._alias = alias_class()
        self._parameters_intro = text_class()
        self._parameters = []
        self._output = parameter_class()

    # Derive the function name (from parameter or __qualname__)
    def _set_name(self, function, name):
        if name is not None:
            self._name = name
        elif hasattr(function, "__name__"):
            self._name = function.__qualname__.lower()
        else:
            self._name = name

    # Return lowercase qualified function name
    def _get_name(self):
        return self._name

    # Return the section label, or None if unset
    def _get_section(self):
        return self._section

    # Set function docstring text
    def _set_doc(self, doc = None):
        self._doc._set(doc)
        return self

    # Set alias for the function
    def _set_alias(self, alias = None):
        self._alias._set(alias)
        return self

    # Add a parameter to the function
    def _add_parameter(self, name = None, doc = None):
        parameter = parameter_class(name, doc)
        self._parameters.append(parameter)
        return parameter

    # Set output parameter details
    def _set_output(self, name = None, doc = None, type = None):
        self._output._name._set_label(name)
        self._output._name._set_value(doc)
        self._output._type._set_value(type)
        return self._output

    # Compose full docstring of the function
    def _get_docstring(self, colorless = False):
        docs = [self._doc._get_docstring(),
                self._alias._get_docstring(space),
                self._parameters_intro._get_docstring(space)]
        doc1 = connect_strings(docs, empty)
        docs = [par._get_docstring(new_lines(2)) for par in self._parameters]
        doc2 = connect_strings(docs)
        doc3 = self._output._get_docstring(new_lines(2))
        doc = connect_strings([doc1, doc2, doc3])
        return uncolorize(doc) if colorless else doc

    # Print the function docstring
    def _show(self, colorless = False):
        print(self._get_docstring(colorless))

    # Update the function's __doc__ (colorless) and attach a doc() method that prints the colored version; silently skip when the callable rejects attribute assignment (e.g. C functions).
    def _update(self, colorless = False):
        for function in self._function:
            function.__doc__ = self._get_docstring(colorless)
            try:
                function.doc = lambda: self._show(colorless = False)
            except (AttributeError, TypeError):
                pass
        return self

    # Return number of parameters
    def _get_parameters(self):
        return len(self._parameters)

    # Return last added parameter
    def _last(self):
        return self._parameters[-1]

    # Get parameter by name
    def _get_parameter(self, name):
        names = [el._get_name(colorless = 1) for el in self._parameters]
        index = names.index(name) if name in names else None
        return self._parameters[index] if name in names else None

    # Return colored function name string
    def _get_title(self, pixel):
        return colorize(self._get_name()).set_pixel(pixel).get_string()

    # Return title line followed by a blank line and then the full docstring
    def _get_titled_docstring(self, pixel):
        return self._get_title(pixel) + new_lines(2) + self._get_docstring()

    # Representation
    def __repr__(self):
        names = ', '.join([el._get_name() for el in self._parameters])
        return f"PrettyFunction called {self._name} with {len(self._parameters)} parameters ({names})"
