# One documented entry: the function it describes, or several sharing one docstring, together with its description, alias, parameters, source and output.

from inspect import isroutine
from plotext.prettydoc._primitives.text import text_class, alias_class, labeled_text_class
from plotext.prettydoc._primitives.parameter import parameter_class
from plotext.prettydoc._defaults.pixels import default_pixels
from plotext._constants.text import space, empty, new_line
from plotext._methods.string import connect_strings, new_lines, uncolorize
from plotext._primitives.colorize import colorize

class function_class:
    # Start from one function, or several sharing the same docstring, with the given name and section.
    def __init__(self, *function, name = None, section = None):
        self._function = list(function)
        self._set_name(function[0], name)
        self._section = section
        self._doc = text_class()
        self._alias = alias_class()
        self._parameters_intro = text_class()
        self._parameters = []
        self._source = labeled_text_class()
        self._output = parameter_class()

    # Set the entry name, taken from the given one, or from the function own name when none is given.
    def _set_name(self, function, name = None):
        self._name = name if name is not None else function.__name__ if hasattr(function, "__name__") else None

    # The entry name alone, as "clear".
    def _get_name(self):
        return self._name

    # The name telling this entry from the others sharing it: the first source path joined with the name, as "plotext.figure.clear", or the name alone when no source was given.
    def _get_registry_name(self):
        source = self._source._get_value(colorless = 1)
        if source is None:
            return self._name
        first_source_path = source.split(',')[0].strip()
        return first_source_path + '.' + self._name

    # Every way of reaching this entry, one per source path, written without parentheses.
    def _get_paths(self):
        source = self._source._get_value(colorless = 1)
        source_paths = [] if source is None else [path.strip() for path in source.split(',')]
        paths = [path + '.' + self._name for path in source_paths] if source_paths else [self._name]
        paths = [path.replace('()', '') for path in paths]
        return paths

    # What the entry is called: a method when a plain function or a class was documented, an attribute when the documented object is reached by name alone, as plotext.figure is.
    def _get_kind(self):
        function = self._function[0]
        return 'method' if isinstance(function, type) or isroutine(function) else 'attribute'

    def _get_listed_name(self):
        alias = self._alias._get(colorless = 1)
        return self._name if alias is None else self._name + ' [' + alias + ']'

    # The section this entry belongs to, or nothing when it has none.
    def _get_section(self):
        return self._section

    # Set the main description, the text opening the docstring.
    def _set_doc(self, doc = None):
        self._doc._set(doc)
        return self

    # Set the alternative name the function also answers to.
    def _set_alias(self, alias = None):
        self._alias._set(alias)
        return self

    # Add one parameter, with its description, type and default.
    def _add_parameter(self, name = None, doc = None):
        parameter = parameter_class(name, doc)
        self._parameters.append(parameter)
        return parameter

    # Set the source path, what is written before the name to reach the method.
    def _set_source(self, label = None, value = None):
        self._source._set_label(label)
        self._source._set_value(value)
        return self._source

    # Set what the function gives back, with its description and type.
    def _set_output(self, name = None, doc = None, type = None):
        self._output._name._set_label(name)
        self._output._name._set_value(doc)
        self._output._type._set_value(type)
        return self._output

    # The whole docstring, its description, alias, parameters and output one after the other.
    def _get_docstring(self, colorless = False):
        docs = [self._doc._get_docstring(),
                self._alias._get_docstring(new_line),
                self._source._get_docstring(new_lines(2)),
                self._parameters_intro._get_docstring(new_lines(2))]
        doc1 = connect_strings(docs, empty)
        docs = [par._get_docstring(new_lines(2)) for par in self._parameters]
        doc2 = connect_strings(docs)
        doc3 = self._output._get_docstring(new_lines(2))
        doc = connect_strings([doc1, doc2, doc3])
        return uncolorize(doc) if colorless else doc

    # Print the docstring.
    def _show(self, colorless = False):
        print(self._get_docstring(colorless))

    # Write the docstring into the function itself and attach to it a doc() method printing the colored one; a function refusing both, as the Python built-in ones do, is skipped.
    def _update(self, colorless = False):
        for function in self._function:
            function.__doc__ = self._get_docstring(colorless)
            try:
                function.doc = lambda *instance: self._show(colorless = False)
            except (AttributeError, TypeError):
                pass
        return self

    # How many parameters the entry documents.
    def _get_parameters(self):
        return len(self._parameters)

    # The parameter added last, the one the following calls describe.
    def _last(self):
        return self._parameters[-1]

    # The parameter with the given name.
    def _get_parameter(self, name):
        names = [el._get_name(colorless = 1) for el in self._parameters]
        index = names.index(name) if name in names else None
        return self._parameters[index] if name in names else None

    # The colored title of the entry, its name followed by method or attribute; with section, the section name is printed above it.
    def _get_title(self, pixel, section = False):
        method_name = self._get_name()
        section_name = self._get_section()
        title = colorize(method_name).fill(pixel).string()
        if section and section_name is not None:
            return colorize(section_name).fill(default_pixels['section']).string() + ' section' + new_lines(2) + title + ' ' + self._get_kind()
        return title

    # The title, a blank line, then the whole docstring.
    def _get_titled_docstring(self, pixel, section = False):
        return self._get_title(pixel, section) + new_lines(2) + self._get_docstring()

    # Representation
    def __repr__(self):
        names = ', '.join([el._get_name() for el in self._parameters])
        return f"PrettyFunction({self._name}, {len(self._parameters)} parameters, {names})"
