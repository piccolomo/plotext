# Prettydoc section: the docs manager and its members

from plotext._doc.tools import *
from plotext import prettydoc


section('prettydoc')


add(prettydoc.docs)
doc("Initializes a docs manager, which builds visually styled docstrings: its methods register the objects to document, together with each piece of their docstring (the description, the parameters, the output and so on), and its update() method creates the documentation container, a final and distinct object.")
source("plotext.prettydoc")
par("colorless", "Whether to write each __doc__ as plain text, without color codes; the interactive menu and the doc() methods always print colored. The interactive menu is opened by calling the documentation container, returned by update(), as a method", explanation("bool"), False)
par("separator", "String placed between a field label and its content in every rendered docstring line, as in 'Source: plotext' or 'type: an integer'", explanation("string"), repr(': '))
out("The initialized docs manager", explanation("docs"))

add(prettydoc.docs.pixel)
doc("Configures the default color and style of the selected docstring component.\n"
    "The component named attribute is special: it colors the menu entries documenting attributes, the objects reached by name without parentheses, like plotext.figure, telling them visually apart from methods.")
source("plotext.prettydoc.docs()")
par("component", "Component to modify; call plotext.prettydoc.components() to see the available component names", explanation("string"))
par("pixel", "Pixel carrying the desired color and style", explanation("pixel_par"), None)
out("The docs manager itself", explanation("docs"))

add(prettydoc.components)
doc("Prints the list of available docstring components with a short description of each. A component is one piece of the rendered docstring, like the title, the description, a parameter name or its type, each with its own color and style, configurable with the pixel() method of the docs manager.")
source("plotext.prettydoc")

add(prettydoc.docs.section)
doc("Sets the current section name: every entry added afterwards with function() belongs to it, grouped together in the interactive menu, until section() is called again. Call it with no argument, or with None, to leave the following entries without a section. The interactive menu is opened by calling the documentation container, returned by update(), as a method.")
source("plotext.prettydoc.docs()")
par("section", "The section name; if None, the following entries belong to no section", explanation("string"), None)
past_out("plotext.prettydoc.docs().pixel")

add(prettydoc.docs.title)
doc("Sets the title shown above the interactive menu. The interactive menu is opened by calling the documentation container, returned by update(), as a method.")
source("plotext.prettydoc.docs()")
par("title", "Title text, or None to remove it", explanation("string"), None)
past_out("plotext.prettydoc.docs().pixel")

add(prettydoc.docs.function)
doc("Registers a function to be documented. All subsequent manager calls apply to the most recently added function until another is registered. Each function is stored under a unique key, based on its name (the name parameter, or the function's __name__ attribute when no name is given); if a source path is set with the source() method, the key becomes the source path joined with the name: for example, in plotext.figure.bar, plotext.figure is the source path and bar the name.")
source("plotext.prettydoc.docs()")
par("function", "The function to document; a list of functions all receive the same docstring, useful for aliases", explanation("function"))
par("name", "Name of the entry; if None, the function's own __name__ attribute is used", explanation("string"), None)
past_out("plotext.prettydoc.docs().pixel")

add(prettydoc.docs.description)
doc("Adds the main body of documentation for the most recently added function, and the alternative name it also answers to.\n"
    "Each of the two is added only when given, so a function with no alias is documented with the description alone, and an alias can be added on its own.")
source("plotext.prettydoc.docs()")
par("doc", "Description of what the function does", explanation("label"), None)
par("alias", "Alternative name of the function", explanation("label"), None)
past_out("plotext.prettydoc.docs().pixel")

add(prettydoc.docs.parameter)
doc("Adds a parameter to the most recently added function, with the type and default value shown under its description.\n"
    "The type accepts any string, including one registered in a plotext.prettydoc registry: for example, parameter('degrees', 'the angle', registry('celsius'), 25) renders the type as 'a temperature in Celsius degrees' and the default as 25, once 'celsius' has been registered there.")
source("plotext.prettydoc.docs()")
par("name", "Parameter name", explanation("label"))
par("doc", "Parameter description", explanation("label"), None)
par("type", "Parameter type", explanation("label"), None)
par("default", "Parameter default value", explanation("label"), None)
past_out("plotext.prettydoc.docs().pixel")

add(prettydoc.docs.source)
doc("A method is called from an object: in plotext.figure.bar(), the method bar() is called from plotext.figure. Prettydoc cannot retrieve this calling object's name (or sequence of objects) on its own: with this method, the user can declare the source path for the most recently added function. The source path is rendered in the Source field of the docstring.\n"
    "The source may also be a list of source paths, for methods reachable from several places: for example, both plotext.figure and plotext.figure.subplot() are valid source paths for the bar() method. All paths appear in the Source field, while only the first enters the function unique key, described in the function() method.")
source("plotext.prettydoc.docs()")
par("value", "The source path, or a list of source paths; if None, no Source field is rendered", "a string, or a list of strings", None)
past_out("plotext.prettydoc.docs().pixel")

add(prettydoc.docs.output)
doc("Documents the output of the most recently added function.")
source("plotext.prettydoc.docs()")
par("doc", "Description of the output", explanation("label"))
par("type", "Output type", explanation("label"), None)
past_out("plotext.prettydoc.docs().pixel")

add(prettydoc.docs.past_parameter)
doc("Copies a parameter from a previously documented function onto the current one. The type and default value replace the copied ones when given, and keep them otherwise; an empty string removes the field.")
source("plotext.prettydoc.docs()")
par("name", "Name of the parameter to copy", explanation("string"))
par("function", "Unique key of the function that already defines this parameter", explanation("function_key"))
past_par("type", "plotext.prettydoc.docs().parameter")
past_par("default", "plotext.prettydoc.docs().parameter")
past_out("plotext.prettydoc.docs().pixel")

add(prettydoc.docs.past_output)
doc("Copies the output specification from a previously documented function.")
source("plotext.prettydoc.docs()")
par("function", "Unique key of the function whose output should be reused", explanation("function_key"))
past_out("plotext.prettydoc.docs().pixel")

add(prettydoc.docs.update)
doc("Creates the documentation container: a distinct object with one method per documented entry, carrying the same name and printing its docstring. Called as a method, the documentation container opens the interactive menu: three scrollable columns, holding the sections, the methods of the picked section, and the docstring of the picked method.\n"
    "It also writes each registered docstring into the __doc__ of its documented method or attribute, and attaches to each a doc() method that prints the docstring in color.")
source("plotext.prettydoc.docs()")
out("The documentation of every registered entry", explanation("documentation"))

add(prettydoc.docs.string)
doc("Returns every registered docstring joined in a single string, in registration order, ready to be printed or saved.")
source("plotext.prettydoc.docs()")
out("All the docstrings, joined", explanation("string"))


add(prettydoc.registry)
doc("Initializes a registry: a store of the strings shared by several docstrings (type explanations, recurring messages, long sentences), each kept under a short name, so that a text needed in many docstrings is written once and reused. Strings go in with the add() method, and come back by calling the registry with their name; a name never added raises an error, while the get() method returns a chosen default instead. The registry stands on its own, with no tie to a docs manager: the same one can feed several, and a manager needs none.")
source("plotext.prettydoc")
out("The initialized registry", explanation("registry"))

add(prettydoc.registry.add)
doc("Stores a string under a short name; an existing name is overwritten.")
source("plotext.prettydoc.registry()")
par("name", "Name to store the string under", explanation("string"))
par("doc", "The string to store", explanation("string"))
out("The registry itself", explanation("registry"))

add(prettydoc.registry.get)
doc("Returns the string stored under the given name, the given default standing in when the name was never used.")
source("plotext.prettydoc.registry()")
par("name", "Name of the stored string", explanation("string"))
par("default", "Value returned when the name was never used", explanation("string"), None)
out("The stored string, or the default", explanation("string"))

add(prettydoc.test)
doc("Runs the prettydoc unit test suite and prints a summary of the results.")
source("plotext.prettydoc")
