# Docs: the manager registering every function with its documentation, and building the container out of them.

from plotext.prettydoc._defaults.pixels import default_pixels

from plotext.prettydoc._primitives.function import function_class
from plotext.prettydoc._primitives.container import docs_output
from plotext._constants.text import space, new_line
from plotext._methods import object as object_methods
from plotext._methods.string import new_lines
from plotext._primitives.colorize import colorize
from plotext._correct import label as correct_label

# The section of an entry added before any section() call.
default_section = None


# The manager: every function is added to it with its documentation, and update() turns them all into the container.
class docs:
    # Start an empty manager; with colorless, the docstrings written into the functions carry no colors.
    def __init__(self, colorless = False, separator = None):
        self._functions = []
        self._colorless = colorless
        self._pixels = default_pixels
        self._default_section = default_section
        self._title = None
        self._set_separator(separator)

    # Set the title shown above the interactive menu; pass None (the default) to remove it.
    def title(self, title = None):
        self._title = title
        return self

    # Set the section every entry added afterwards belongs to; with no name, they belong to none.
    def section(self, section = None):
        self._default_section = section
        return self

    # Set what sits between each field label and its value, the colon of "type: a numeric value".
    def _set_separator(self, separator = None):
        self._separator = ': ' if separator is None else separator
        return self

    # Set the color and style of one docstring component, as the alias or the parameter name.
    def pixel(self, component, pixel = None):
        pixel = pixel() if pixel is None else pixel
        self._pixels[component] = pixel
        return self

    # Add a function to document; every call afterwards describes it, until the next one is added.
    def function(self, *function, name = None):
        self._functions.append(function_class(*function, name = name, section = self._default_section))
        return self

    # Add the description of the last function, and the alternative name it answers to, each only when given; the method cannot be called doc(), since update() attaches a doc() method to every documented object, this manager included.
    def description(self, doc = None, alias = None):
        doc = self._colorize(doc, "doc")
        alias = self._colorize(alias, "alias")
        if doc is not None:
            doc.write(correct_label.doc(doc.string(1), 1))
            self._last()._set_doc(doc)
        if alias is not None:
            self._last()._set_alias(alias)
        return self

    # Set the line introducing the parameters, in the singular or plural depending on how many there are.
    def _set_parameters_intro(self):
        fun = self._last()
        pixel = self._get_default_pixel("doc") if fun._doc._empty() else fun._doc._get_pixel()
        count = fun._get_parameters()
        if count == 1:
            fun._parameters_intro._set(colorize('This is its parameter:').fill(pixel))
        elif count == 2:
            fun._parameters_intro._set(colorize('These are its parameters:').fill(pixel))
        return self

    # Add a parameter to the last function, with its description, type and default, each only when given.
    def parameter(self, name = None, doc = None, type = None, default = None):
        name = self._colorize(name, "parameter.name")
        doc = self._colorize(doc, "parameter.doc")
        doc.write(correct_label.doc(doc.string(1), 0)) if doc is not None else None
        par = self._last()._add_parameter(name, doc)
        par._set_separator(self._separator)
        par._set_type_label(self._colorize("type", "parameter.type.label"))
        par._set_default_label(self._colorize("default", "parameter.default.label"))
        self._set_parameters_intro()
        self._set_spec(type, default)
        return self

    # Copy a parameter from another function, keeping its type and default unless new ones are given.
    def past_parameter(self, name, function, type = None, default = None):
        parameter = self._get_function(function)._get_parameter(name)
        self._last()._parameters.append(parameter._copy())
        self._set_parameters_intro()
        self._set_spec(type, default)
        return self

    # Set the type and default of the parameter added last; an empty string removes one of them.
    def _set_spec(self, type = None, default = None):
        type = type if type == '' else self._colorize(type, "parameter.type")
        default = default if default == '' else self._colorize(default, "parameter.default")
        self._last()._last()._set_spec(type, default)
        return self

    # Set the source path of the last function, what is written before its name to reach it; several paths are joined by commas.
    def source(self, value = None):
        value = ', '.join(value) if isinstance(value, (list, tuple)) else value
        label = self._colorize("Source", "output.name")
        value = self._colorize(value, "output.doc")
        src = self._last()._set_source(label, value)
        src._set_separator(self._separator)
        return self

    # Set what the last function gives back, with its description and type.
    def output(self, doc = None, type = None):
        name = self._colorize("Returns", "output.name")
        doc = self._colorize(doc, "output.doc")
        doc.write(correct_label.doc(doc.string(1), 0))
        type = self._colorize(type, "output.type")
        out = self._last()._set_output(name, doc, type)
        out._set_type_label(self._colorize("type", "output.type.label"))
        out._set_separator(self._separator)
        return self

    # Copy from another function what it gives back.
    def past_output(self, function):
        output = self._get_function(function)._output
        self._last()._output = output._copy()
        return self

    # Write every docstring into its function, attach a doc() method to each, and give back the container holding one printing method per entry.
    def update(self, _container = None):
        out = docs_output() if _container is None else _container
        for fn in self._functions:
            fn._update(self._colorless)
            out._function_dict[fn._get_registry_name()] = fn._show
            out._path_dict[fn._get_registry_name()] = fn._get_paths()
        out._call = self._pick
        return out

    # Every docstring joined in one text, in the order they were documented.
    def string(self):
        return (new_lines(3)).join([el._get_titled_docstring(self._get_default_pixel("title")) for el in self._functions])

    # Open the interactive menu: the sections, the methods of the picked section, and the docstring of the picked method. With no sections at all, the sections column is dropped; with multiple sections, a None one is moved to the end and labeled "Unlabeled".
    def _pick(self):
        from plotext.prettydoc._methods.menu import run_menu
        title_pixel = self._get_default_pixel("title")
        sections = self._get_section()
        if len(sections) == 1 and sections[0][0] is None:
            groups = [(None, sections[0][1])]
        else:
            labeled = [(sec, fns) for sec, fns in sections if sec is not None]
            unlabeled = [("Unlabeled", fns) for sec, fns in sections if sec is None]
            groups = labeled + unlabeled
        sections = [(title, [(fn._get_listed_name(), fn) for fn in fns]) for title, fns in groups]
        run_menu(sections, print_function = lambda fn: print(fn._get_titled_docstring(title_pixel, section = True)), title = self._title)

    # The text painted with the color of its component, unless it carries its own colors already.
    def _colorize(self, text, component, lower = 0):
        if text is None:
            return None
        text = colorize(text).fill(self._get_default_pixel(component)) if not isinstance(text, colorize) else text
        text.write(text.string(1).lower()) if lower else None
        return text

    # The color and style of one docstring component.
    def _get_default_pixel(self, component):
        return self._pixels[component]

    # The entry at the given position, counted in the order they were added.
    def _get(self, index):
        return self._functions[index]

    # The entry with the given name, the source path included when it has one, so that methods sharing a name are told apart.
    def _get_function(self, name):
        names = [el._get_registry_name() for el in self._functions]
        index = names.index(name) if name in names else None
        return self._get(index) if name in names else None

    # The entry added last, the one the following calls describe.
    def _last(self):
        return self._functions[-1]

    # The section names, in the order they first appear; entries without a section are skipped.
    def _get_unique_sections(self):
        seen = []
        for fn in self._functions:
            sec = fn._get_section()
            if sec is not None and sec not in seen:
                seen.append(sec)
        return seen

    # Every section with its entries, in the order they first appear; the entries without a section come under no name.
    def _get_section(self):
        groups = {}
        for fn in self._functions:
            groups.setdefault(fn._get_section(), []).append(fn)
        return list(groups.items())

    # How many entries the manager holds.
    def _get_length(self):
        return len(self._functions)

    # Take in the entries of another manager.
    def _add(self, doc):
        self._functions = self._functions + doc._functions

    # The hash of every docstring joined, used by the tests.
    def _hash(self):
        return object_methods.hash(self.string())

    # Representation
    def __repr__(self):
        return f"PrettyDocManager({self._get_length()} functions)"
