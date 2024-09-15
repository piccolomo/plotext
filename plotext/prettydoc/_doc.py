from ._core import *

pd = docs(1, ': ')
#pd = docs()
add = pd.add_function
alias = pd.add_alias
doc = pd.add_doc
par = pd.add_parameter
spec = pd.add_parameter_spec
past = pd.add_past_parameter
out = pd.add_output
past_out = pd.add_past_output


class type:
	bool = 'bool'; 
	docs = 'plotext.prettydoc.docs'
	string = 'string'
	function = 'function'
	colorize_plus = "plotext.colorize or string"

	float = 'float'; 
	floats = 'floats'; 
	int = 'int'; 
	
	pixel = "plotext.pixel"
	colorize = "plotext.colorize"
	matrix = "plotext.matrix"
	matrix_plus = "plotext.matrix or plotext.colorize or a string"
	color = "string color code, integer (lower than 256), a tuple of 3 integers (each lower than 256)"
	alignment = "string or integer"

class message:
	components = "Access the plotext.prettydoc.components() method for the available components."

add(docs)
doc("An object of this class is used to add beautiful docstrings to your functions.")
par("colorless", "Determines whether the function docstrings should be colorless. Regardless of this parameter, the colored version is registered as an attribute (named after the function) of the class object"); 
spec(type.bool, False)
par("separator", "specifies the separator between fields like parameter name and its description, etc."); spec(type.string, repr(" "))
out("itself", type.docs)

add(docs.set_default_pixel)
doc("It allows to change the default coloring of a specific prettydoc docstring component. ")
par("component", "Specifies which component to change the coloring of; " + message.components)
spec(type.string)
out("itself, updated", type.docs)

add(components)
doc("It displays the available docstring components, which can be modified using the plotext.prettydoc.docs().set_default_pixel() method.")

add(docs.add_function)
doc("It adds a function to the docs() object. Once the function all subsequent methods will refer to the last function added. Finally use the docs.update() method to process and register the docstrings.")
par("function", "The function to which the pretty docstring will be added.")
spec("a function")
past_out("docs.set_default_pixel")

add(docs.add_doc)
doc("It adds the documentation body to the last function.")
par("doc", "the documentation describing the function"); spec(type.colorize_plus)
past_out("docs.set_default_pixel")

add(docs.add_alias)
doc("It adds an alias to the last function.")
par("alias", "the name of the alias"); spec(type.colorize_plus)
past_out("docs.set_default_pixel")

add(docs.add_parameter)
doc("It adds a parameter to the last function.")
par("name", "the name of the parameter"); spec(type.colorize_plus)
par("doc", "its main description"); spec(type.colorize_plus)
past_out("docs.set_default_pixel")

add(docs.add_parameter_spec)
doc("It adds the type and default specification to the last parameter added.")
par("type", "its type"); spec(type.colorize_plus)
par("default", "its default value"); spec(type.colorize_plus)
past_out("docs.set_default_pixel")

add(docs.add_past_parameter)
doc("It adds a parameter from a previously added function to the current one. ")
par("name", "the name of the parameter"); spec(type.colorize_plus)
par("function", "the  past function name"); spec(type.colorize_plus)
past_out("docs.set_default_pixel")

add(docs.add_output)
doc("It adds the output documentation to the last function.")
par("type", "the output type"); spec(type.colorize_plus)
par("doc", "the output main description"); spec(type.colorize_plus)
past_out("docs.set_default_pixel")

add(docs.add_past_output)
doc("It adds the output details from a previously added function to the current one.")
past("function", "docs.add_past_parameter");
past_out("docs.set_default_pixel")

add(docs.update)
doc("It process and update the function docstrings.")
past_out("docs.set_default_pixel")

add(docs.show)
doc("It displays all the docstrings with color formatting.")
past_out("docs.set_default_pixel")

add(test)
doc("It performs unit tests for the prettydoc module.")

pd.update()