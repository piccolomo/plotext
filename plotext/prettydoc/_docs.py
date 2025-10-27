from plotext.prettydoc._pixels import default_pixels
from plotext._constants import space, new_line
from plotext.prettydoc._function import function_class

from plotext._methods.object import * 
from plotext._colorize import colorize
from plotext._correct import correct_class as correct


class docs:
    def __init__(self, colorless=False, separator=None):
        self._functions = []
        self._colorless = colorless
        self._pixels = default_pixels
        self.set_separator(separator)

    # Set separator string used in documentation
    def set_separator(self, separator=None):
        self._separator = space if separator is None else separator
        return self

    # Set default pixel for a component
    def set_default_pixel(self, component, pixel=None):
        pixel = pixel() if pixel is None else pixel
        self._pixels[component] = pixel
        return self

    # Add a function wrapper to docs
    def add_function(self, *function, name = None):
        self._functions.append(function_class(*function, name = name))
        return self

    # Add documentation text for last function
    def add_doc(self, doc=None):
        doc = self._colorize(doc, "doc")
        doc.set_string(correct.doc(doc.get_string(1), 1))
        self._last().set_doc(doc)
        return self

    # Add alias text for last function
    def add_alias(self, alias=None):
        alias = self._colorize(alias, "alias")
        self._last().set_alias(alias)
        return self

    # Set introductory text for parameters based on their count
    def _set_parameters_intro(self):
        fun = self._last()
        pixel = fun.doc.get_pixel()
        if fun.get_parameters() == 1:
            fun.parameters_intro.set(colorize('This is its parameter:').set_pixel(pixel))
        elif fun.get_parameters() == 2:
            fun.parameters_intro.set(colorize('These are its parameters:').set_pixel(pixel))
        return self

    # Add a parameter with name and doc
    def add_parameter(self, name=None, doc=None):
        name = self._colorize(name, "parameter.name")
        doc = self._colorize(doc, "parameter.doc")
        doc.set_string(correct.doc(doc.get_string(1), 0))
        par = self._last().add_parameter(name, doc)
        par.set_separator(self._separator)
        par.set_type_label(self._colorize("type", "parameter.type.label"))
        par.set_default_label(self._colorize("default", "parameter.default.label"))
        self._set_parameters_intro()
        return self

    # Add type and default specification to the last parameter
    def add_parameter_spec(self, type = None, default = None):
        type = self._colorize(type, "parameter.type") 
        default = self._colorize(repr(default), "parameter.default")
        self._last().last().set_spec(type, default)

    # Add a previously defined parameter from another function
    def add_past_parameter(self, name, function):
        parameter = self._get_function(function).get_parameter(name)
        self._last().parameters.append(parameter.copy())
        self._set_parameters_intro()
        return self

    # Add output specification for the last function
    def add_output(self, doc = None, type = None):
        name = self._colorize("Returns", "output.name")
        doc = self._colorize(doc, "output.doc")
        doc.set_string(correct.doc(doc.get_string(1), 0))
        type = self._colorize(type, "output.type")
        out = self._last().set_output(name, doc, type)
        out.set_type_label(self._colorize("type", "output.type.label"))
        out.set_separator(self._separator)
        return self

    # def add_output_type(self, type = None):


    # Add previously defined output from another function
    def add_past_output(self, function):
        output = self._get_function(function).output
        self._last().output = output.copy()
        return self

    # Update all functions' docstrings and add show methods as attributes
    def update(self):
        [el.update(self._colorless) for el in self._functions]
        [set_attribute(self, el.get_name(), el.show) for el in self._functions]
        return self

    # Get full combined string of all functions with titles and docs
    def _get_string(self):
        return (string_methods.new_lines(3)).join(
            [el.get_title(self._get_default_pixel("title")) + new_line + el.get_docstring() for el in self._functions])

    # Print all functions' docs
    def show(self):
        print(self._get_string())
        return self

    # Colorize text if not already colorized or None
    def _colorize(self, text, component):
        if text is None:
            return None
        if isinstance(text, colorize):
            return text
        return colorize(text).set_pixel(self._get_default_pixel(component))

    # Retrieve default pixel for a component
    def _get_default_pixel(self, component):
        return self._pixels[component]

    # Retrieve function by name (lowercase qualified name)
    def _get_function(self, name): 
        names = [el.get_name() for el in self._functions]
        index = names.index(name) if name in names else None
        return self._functions[index] if name in names else None

    # Return last function added
    def _last(self):
        return self._functions[-1]

    # Number of functions in docs
    def _get_length(self):
        return len(self._functions)

    def __repr__(self):
        return "PrettyDoc(" + str(self._get_length()) + " functions)"

    # Concatenate another docs_class's functions to self
    def __add__(self, doc):
        self._functions = self._functions + doc._functions

    # Hash of combined doc string
    def _hash(self):
        return hash(self._get_string())