from plotext.prettydoc._text import text_class, alias_class
from plotext.prettydoc._parameter import parameter_class
from plotext._constants import space, empty
from plotext._methods import * 
from plotext._colorize import colorize_class


class function_class:
    def __init__(self, function, name = None):
        self.function = function
        self.name = self.function.__qualname__.lower() if name is None else name
        self.doc = text_class()
        self.alias = alias_class()
        self.parameters_intro = text_class()
        self.parameters = []
        self.output = parameter_class()

    # Return lowercase qualified function name
    def get_name(self):
        return self.name

    # Set function docstring text
    def set_doc(self, doc=None):
        self.doc.set(doc)
        return self

    # Set alias for the function
    def set_alias(self, alias=None):
        self.alias.set(alias)
        return self

    # Add a parameter to the function
    def add_parameter(self, name=None, doc=None):
        parameter = parameter_class(name, doc)
        self.parameters.append(parameter)
        return parameter

    # Set output parameter details
    def set_output(self, name=None, doc=None, type=None):
        self.output.name.set_label(name)
        self.output.name.set_value(doc)
        self.output.type.set_value(type)
        return self.output

    # Compose full docstring of the function
    def get_docstring(self, colorless=False):
        docs = [
            self.doc.get_docstring(),
            self.alias.get_docstring(space),
            self.parameters_intro.get_docstring(space),
        ]
        doc1 = string_methods.connect_strings(docs, empty)
        docs = [par.get_docstring(string_methods.new_lines(2)) for par in self.parameters]
        doc2 = string_methods.connect_strings(docs)
        doc3 = self.output.get_docstring(string_methods.new_lines(2))
        doc = string_methods.connect_strings([doc1, doc2, doc3])
        return string_methods.uncolorize(doc) if colorless else doc

    # Print the function docstring
    def show(self, colorless=False):
        print(self.get_docstring(colorless))

    # Update the function's __doc__ attribute
    def update(self, colorless=False):
        self.function.__doc__ = self.get_docstring(colorless)
        return self

    # Return number of parameters
    def get_parameters(self):
        return len(self.parameters)

    # Return last added parameter
    def last(self):
        return self.parameters[-1]

    # Get parameter by name
    def get_parameter(self, name):
        names = [el.get_name() for el in self.parameters] 
        index = names.index(name) if name in names else None 
        return self.parameters[index] if name in names else None 

    # Return colored function name string
    def get_title(self, pixel):
        return colorize_class(self.get_name()).set_pixel(pixel).get_string()

    def __repr__(self):
        return "PrettyFunctionDoc(" + self.get_name() + ")"
