# Pretty documentation manager: prettydoc.docs and its members, plus the top-level test runners

from plotext._doc.tools import *
from plotext import prettydoc, test


add(prettydoc.docs, name = "prettydoc.docs")
doc("Initializes a PrettyDoc object that manages visually styled docstrings.")
par("colorless", "If True, rendered docstrings will have no color formatting."); spec(type.bool, False)
par("separator", "Separator placed between a labelled field's label and value."); spec(type.string, repr(': '))
out("The PrettyDoc manager itself", type.docs)

add(prettydoc.docs.set_default_pixel, name = "prettydoc.docs.set_default_pixel")
doc("Configures the default color and style of one PrettyDoc component. "
    "Call plotext.prettydoc.components() to see the available component names.")
par("component", "Component to modify"); spec(type.string)
par("pixel", "Pixel carrying the desired color and style"); spec(type.pixel_par, None)
past_out("prettydoc.docs")

add(prettydoc.docs.register_type, name = "prettydoc.docs.register_type")
doc("Registers a new data type name and its human-readable explanation in the shared type registry.")
par("type", "Type name"); spec(type.string)
par("doc", "Explanation of the type"); spec(type.string)
past_out("prettydoc.docs")

add(prettydoc.components, name = "prettydoc.components")
doc("Prints the list of available PrettyDoc components with a short description of each.")

add(prettydoc.docs.add_function, name = "prettydoc.docs.add_function")
doc("Registers a function to be documented. All subsequent PrettyDoc calls apply to the most recently added function until another is registered.")
par("function", "The function (or list of aliased functions) to document"); spec(type.function)
par("name", "Optional explicit name; defaults to the function's __qualname__"); spec(type.string, None)
past_out("prettydoc.docs")

add(prettydoc.docs.add_doc, name = "prettydoc.docs.add_doc")
doc("Adds the main body of documentation for the most recently added function.")
par("doc", "Description of what the function does"); spec(type.label)
past_out("prettydoc.docs")

add(prettydoc.docs.add_alias, name = "prettydoc.docs.add_alias")
doc("Adds an alias name for the most recently added function.")
par("alias", "Alias name"); spec(type.label)
past_out("prettydoc.docs")

add(prettydoc.docs.add_parameter, name = "prettydoc.docs.add_parameter")
doc("Adds a parameter to the most recently added function.")
par("name", "Parameter name"); spec(type.label)
par("doc", "Parameter description"); spec(type.label)
past_out("prettydoc.docs")

add(prettydoc.docs.add_parameter_spec, name = "prettydoc.docs.add_parameter_spec")
doc("Sets the type and default value of the most recently added parameter.")
par("type", "Parameter type"); spec(type.label, None)
par("default", "Parameter default value"); spec(type.label, None)
past_out("prettydoc.docs")

add(prettydoc.docs.add_past_parameter, name = "prettydoc.docs.add_past_parameter")
doc("Copies a parameter from a previously documented function onto the current one.")
par("name", "Name of the parameter to copy"); spec(type.string)
par("function", "Name of the function that already defines this parameter"); spec(type.string)
past_out("prettydoc.docs")

add(prettydoc.docs.add_output, name = "prettydoc.docs.add_output")
doc("Documents the output of the most recently added function.")
par("doc", "Description of the output"); spec(type.label)
par("type", "Output type"); spec(type.label, None)
past_out("prettydoc.docs")

add(prettydoc.docs.add_past_output, name = "prettydoc.docs.add_past_output")
doc("Copies the output specification from a previously documented function.")
par("function", "Name of the function whose output should be reused"); spec(type.string)
past_out("prettydoc.docs")

add(prettydoc.docs.update, name = "prettydoc.docs.update")
doc("Finalizes the manager: applies every registered docstring to its function's __doc__ and returns a container that exposes every docstring by attribute name.")
out("A docs_output container with one callable attribute per registered function", type.docs)

add(prettydoc.docs.show, name = "prettydoc.docs.show")
doc("Prints every registered docstring, one after another.")
past_out("prettydoc.docs")


# Test runners

add(test, name = "test")
doc("Runs the plotext unit test suite and prints a summary of the results.")

add(prettydoc.test, name = "prettydoc.test")
doc("Runs only the prettydoc unit test suite and prints a summary of the results.")
