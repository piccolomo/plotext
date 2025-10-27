from plotext.prettydoc import * 
#from plotext._doc import type

# Create an instance of the docs class with specific separator
pd = docs(1, ': ')  
# pd = docs()  # Alternative initialization (without separator)

# Shortened references to common methods in pd (PrettyDoc)
add = pd.add_function  # Method to add a function to the doc
alias = pd.add_alias  # Method to add an alias to the function
doc = pd.add_doc  # Method to add documentation to the function
par = pd.add_parameter  # Method to add a parameter to the function
spec = pd.add_parameter_spec  # Method to add parameter type and default spec
past = pd.add_past_parameter  # Method to add a past parameter to the function
out = pd.add_output  # Method to add output documentation
past_out = pd.add_past_output  # Method to add past output to the function


class type:
    float = 'float'; 
    floats = 'a list of float numbers'; 
    int = 'int'; 
    bool = 'bool'; 
    string = 'a string'
    tuple = 'a tuple'

    pixel = "plotext.pixel"
    colorize = "plotext.colorize"
    matrix = "plotext.matrix"

    color = "a string color code, an integer (lower than 256) or a tuple of 3 integers (each lower than 256)"
    style = 'a style code string'

    alignment = "a string or an integer"

    data = "one or two lists of numbers"
    marker = "a character, a marker code, a plotext.marker() object, or a list thereof"
    axis = "'x' (0 in short) or 'y' (1 in short); a list of both axes can also be provided"
    side = "0 (or 'lower' for x axis and 'left' for y axis) or 1 (or 'upper' for x axis and 'right' for y axis); a list of both sides can also be provided"
    xside = "'lower' or 'upper' (0 or 1 in short); a list of both sides can also be provided"
    yside = "'left' or 'right' (0 or 1 in short); a list of both sides can also be provided"

    label = 'a string or colorize object'
    docs = 'plotext.prettydoc.docs'  # PrettyDoc class
    function = 'a python function'  # Function type


class message:  # Class for message components in PrettyDoc
    colors = "access the plotext.colors() method for the available color codes."
    styles = "access the plotext.styles() method for the available style codes."
    components = "Access the plotext.prettydoc.components() method for the available components."  # Message for accessing PrettyDoc components


add(docs)
doc("Initializes a PrettyDoc object to create and manage visually enhanced docstrings for functions and classes.")
par("colorless", "Specifies whether the function docstrings should exclude color formatting. The colored version is always stored as an attribute (named after the function) of this class object."); spec(type.bool, False)
par("separator", "Defines the separator used between fields, such as parameter names and their descriptions."); spec(type.string, repr(" "))
out("The PrettyDoc object itself", type.docs)

add(docs.set_default_pixel)
doc("Configures the default color and style settings for a specific PrettyDoc docstring component.")
par("component", "Identifies the docstring component to modify; available components can be retrieved via " + message.components)
spec(type.string)
out("The updated PrettyDoc object", type.docs)

add(components)
doc("Lists the available docstring components that can be customized using the plotext.prettydoc.docs().set_default_pixel() method.")

add(docs.add_function)
doc("Registers a function with the PrettyDoc object for docstring customization. All subsequent method calls will apply to the most recently added function until docs.update() is called to finalize and register the docstrings.") 
par("function", "The function to which the customized docstring will be applied or or list of functions, that should share the same docstring")
par("name", "The name for the function. If not provided, defaults to the function’s __qualname__ attribute."); spec(type.function)
past_out("docs.set_default_pixel")

add(docs.add_doc)
doc("Appends a main documentation description to the most recently added function.")
par("doc", "The descriptive text for the function’s purpose and behavior."); spec(type.label)
past_out("docs.set_default_pixel")

add(docs.add_alias)
doc("Assigns an alias name to the most recently added function.")
par("alias", "The alias name to associate with the function."); spec(type.label)
past_out("docs.set_default_pixel")

add(docs.add_parameter)
doc("Adds a parameter description to the most recently added function.")
par("name", "The name of the parameter to document."); spec(type.label)
par("doc", "The detailed description of the parameter’s purpose."); spec(type.label)
past_out("docs.set_default_pixel")

add(docs.add_parameter_spec)
doc("Specifies the type and default value for the most recently added parameter.")
par("type", "The data type of the parameter."); spec(type.label)
par("default", "The default value of the parameter, if applicable."); spec(type.label, None)
past_out("docs.set_default_pixel")

add(docs.add_past_parameter)
doc("Copies a parameter’s details from a previously documented function to the current function.")
par("name", "The name of the parameter to copy."); spec(type.label)
par("function", "The name of the previously documented function containing the parameter."); spec(type.string)
past_out("docs.set_default_pixel")

add(docs.add_output)
doc("Documents the output details for the most recently added function.")
par("type", "The data type of the function’s output."); spec(type.label)
par("doc", "A description of the function’s output."); spec(type.label)
past_out("docs.set_default_pixel")

add(docs.add_past_output)
doc("Copies output details from a previously documented function to the current function.")
past("function", "docs.add_past_parameter")
past_out("docs.set_default_pixel")

add(docs.update)
doc("Finalizes and applies the customized docstrings to all registered functions.")
past_out("docs.set_default_pixel")

add(docs.show)
doc("Renders all registered docstrings with their color and style formatting.")
past_out("docs.set_default_pixel")

add(test, name = 'test')
doc("Executes unit tests to validate the functionality of the PrettyDoc module.")

pd.update()