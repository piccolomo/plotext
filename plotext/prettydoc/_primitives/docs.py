# Docs primitive: the prettydoc docstring manager, plus docs_output (the finalized attribute-accessible container)

from plotext.prettydoc._defaults.pixels import default_pixels
from plotext.prettydoc._defaults.section import default_section
from plotext.prettydoc._primitives.function import function_class
from plotext.prettydoc._primitives.types import types_class
from plotext._constants.text import space, new_line
from plotext._methods import object as object_methods
from plotext._methods.string import new_lines
from plotext._primitives.colorize import colorize
from plotext._correct import label as correct_label


# Final container with one attribute per documented function (attribute-style access for end users)
class docs_output:

    # Return every (name, function) pair registered on this output
    def _get_functions(self):
        return list(self.__dict__.items())

    # Return the number of registered functions
    def _get_length(self):
        return len(self._get_functions())

    # Representation
    def __repr__(self):
        return f"PrettyDoc: {self._get_length()} functions"

    # Calling the container prints all docstrings
    def __call__(self):
        self._call()


# Builder that registers functions, parameters and outputs, and produces a docs_output
class docs:
    # Initialize a docs manager with colorless flag and optional separator
    def __init__(self, colorless = False, separator = None):
        self._functions = []
        self._colorless = colorless
        self._pixels = default_pixels
        self._default_section = default_section
        self.type = types_class()
        self._set_separator(separator)

    # Set the section label applied to subsequent add_function calls when section is not explicitly passed; pass None (the default) to reset.
    def set_section(self, section = None):
        self._default_section = section
        return self

    # Get the explanation for a data type
    def get(self, label, default = None):
        return getattr(self, label, default)

    # Set separator string used in documentation
    def _set_separator(self, separator = None):
        self._separator = ': ' if separator is None else separator
        return self

    # Set default pixel for a component
    def set_default_pixel(self, component, pixel = None):
        pixel = pixel() if pixel is None else pixel
        self._pixels[component] = pixel
        return self

    # Register a new data type in the shared type registry
    def register_type(self, type, doc):
        self.type.add(type, doc)
        return self

    # Add a function wrapper to docs
    def add_function(self, *function, name = None, section = None):
        section = section if section is not None else self._default_section
        self._functions.append(function_class(*function, name = name, section = section))
        return self

    # Add documentation text for last function
    def add_doc(self, doc = None):
        doc = self._colorize(doc, "doc")
        doc.set_string(correct_label.doc(doc.get_string(1), 1))
        self._last()._set_doc(doc)
        return self

    # Add alias text for last function
    def add_alias(self, alias = None):
        alias = self._colorize(alias, "alias")
        self._last()._set_alias(alias)
        return self

    # Set introductory text for parameters based on count
    def _set_parameters_intro(self):
        fun = self._last()
        pixel = fun._doc._get_pixel()
        count = fun._get_parameters()
        if count == 1:
            fun._parameters_intro._set(colorize('This is its parameter:').set_pixel(pixel))
        elif count == 2:
            fun._parameters_intro._set(colorize('These are its parameters:').set_pixel(pixel))
        return self

    # Add a parameter with name and doc
    def add_parameter(self, name = None, doc = None):
        name = self._colorize(name, "parameter.name")
        doc = self._colorize(doc, "parameter.doc")
        doc.set_string(correct_label.doc(doc.get_string(1), 0))
        par = self._last()._add_parameter(name, doc)
        par._set_separator(self._separator)
        par._set_type_label(self._colorize("type", "parameter.type.label"))
        par._set_default_label(self._colorize("default", "parameter.default.label"))
        self._set_parameters_intro()
        return self

    # Add type and default specification to last parameter
    def add_parameter_spec(self, type = None, default = None):
        type = self._colorize(type, "parameter.type", 1)
        default = self._colorize(default, "parameter.default", 1)
        self._last()._last()._set_spec(type, default)

    # Copy a parameter from another function
    def add_past_parameter(self, name, function):
        parameter = self._get_function(function)._get_parameter(name)
        self._last()._parameters.append(parameter._copy())
        self._set_parameters_intro()
        return self

    # Add output specification for last function
    def add_output(self, doc = None, type = None):
        name = self._colorize("Returns", "output.name")
        doc = self._colorize(doc, "output.doc")
        doc.set_string(correct_label.doc(doc.get_string(1), 0))
        type = self._colorize(type, "output.type")
        out = self._last()._set_output(name, doc, type)
        out._set_type_label(self._colorize("type", "output.type.label"))
        out._set_separator(self._separator)
        return self

    # Copy output from another function
    def add_past_output(self, function):
        output = self._get_function(function)._output
        self._last()._output = output._copy()
        return self

    # Update all functions' docstrings and produce a docs_output with attribute access per function
    def update(self):
        out = docs_output()
        [el._update(self._colorless) for el in self._functions]
        [object_methods.set_attribute(out, el._get_name(), el._show) for el in self._functions]
        object_methods.set_attribute(out, "_call", self.pick)
        return out

    # Get full combined string of all functions
    def get_string(self):
        return (new_lines(3)).join([el._get_titled_docstring(self._get_default_pixel("title")) for el in self._functions])

    # Print all functions' docs
    def show(self):
        print(self.get_string())
        return self

    # Open the interactive picker; functions group by their section. A single None-section is shown as "Pretty Docstrings"; with multiple sections, a None one is moved to the end and labelled "Unlabelled". On Enter the selected function prints title + docstring.
    def pick(self):
        from plotext.prettydoc._methods.menu import run_picker
        title_pixel = self._get_default_pixel("title")
        sections = self._get_section()
        if len(sections) == 1 and sections[0][0] is None:
            groups = [("Pretty Docstrings", sections[0][1])]
        else:
            labeled = [(sec, fns) for sec, fns in sections if sec is not None]
            unlabeled = [("Unlabelled", fns) for sec, fns in sections if sec is None]
            groups = labeled + unlabeled
        sections = [(title, [(fn._get_name(), fn) for fn in fns]) for title, fns in groups]
        run_picker(sections, print_function = lambda fn: print(fn._get_titled_docstring(title_pixel)))

    # Colorize text if not already colorized
    def _colorize(self, text, component, lower = 0):
        if text is None:
            return None
        text = colorize(text).set_pixel(self._get_default_pixel(component)) if not isinstance(text, colorize) else text
        text.set_string(text.get_string(1).lower()) if lower else None
        return text

    # Retrieve default pixel for a component
    def _get_default_pixel(self, component):
        return self._pixels[component]

    # Get a function wrapper by index
    def _get(self, index):
        return self._functions[index]

    # Retrieve function by name
    def _get_function(self, name):
        names = [el._get_name() for el in self._functions]
        index = names.index(name) if name in names else None
        return self._get(index) if name in names else None

    # Return last function added
    def _last(self):
        return self._functions[-1]

    # Return the unique section labels in first-seen order (functions registered without a section are skipped).
    def _get_unique_sections(self):
        seen = []
        for fn in self._functions:
            sec = fn._get_section()
            if sec is not None and sec not in seen:
                seen.append(sec)
        return seen

    # Return [(section, [functions])] in first-seen order; functions without a section land under None.
    def _get_section(self):
        groups = {}
        for fn in self._functions:
            groups.setdefault(fn._get_section(), []).append(fn)
        return list(groups.items())

    # Number of functions in docs
    def _get_length(self):
        return len(self._functions)

    # Concatenate another docs_class's functions
    def _add(self, doc):
        self._functions = self._functions + doc._functions

    # Hash of combined doc string
    def _hash(self):
        return object_methods.hash(self.get_string())

    # Representation
    def __repr__(self):
        return f"PrettyDoc Manager: {self._get_length()} functions"
