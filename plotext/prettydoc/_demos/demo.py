# Demo: reference table of PrettyDoc components and what each one styles

from plotext._correct import label as correct_label
from plotext._constants.text import space, new_line
from plotext._primitives.colorize import colorize


# Map from component name to its human-readable description
components_doc = {
    "title":                  "The function name, shown above each printed docstring",
    "header":                 "The three column names of the interactive menu",
    "alias":                  "The function alias",
    "attribute":              "The menu entries documenting attributes, reached by name without parentheses, like plotext.figure",
    "doc":                    "The main body of the function documentation",
    "parameters.label":       "The header introducing the parameters section",
    "parameter.name":         "The name of the parameter",
    "parameter.type":         "The type of the parameter",
    "parameter.type.label":   "The \"type\" header introducing the parameter's type",
    "parameter.default":      "The default value of the parameter",
    "parameter.default.label": "The \"default\" header introducing the parameter's default value",
    "parameter.doc":          "The main description of the parameter",
    "output.name":            "The \"Returns\" header introducing the function output",
    "output.type":            "The type of the output",
    "output.type.label":      "The \"type\" header introducing the output type",
    "output.doc":             "The main description of the function output",
}


# Print the styled reference table of PrettyDoc components
def components():
    colorize("PrettyDoc Components", pixel = (None, None, 'bold')).print()
    out = [
        colorize(el + space, pixel = ('cyan+', None, 'default')) +
        colorize(correct_label.doc(components_doc[el], 0), pixel = (None, None, 'italic'))
        for el in components_doc]
    out = [el.string() for el in out]
    out = new_line.join(out)
    print(out)
