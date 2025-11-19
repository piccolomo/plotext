from plotext.prettydoc import *  # Import all PrettyDoc utilities
# from plotext._doc import type  # Alternative import (commented out)

# Create PrettyDoc instance with separator
pd = docs(1, ': ')

# Short references to PrettyDoc methods
add = pd.add_function
alias = pd.add_alias
doc = pd.add_doc
par = pd.add_parameter
spec = pd.add_parameter_spec
past = pd.add_past_parameter
out = pd.add_output
past_out = pd.add_past_output

# Types used for PrettyDoc
class type:
    float = 'float'
    floats = 'a list of float numbers'
    int = 'int'
    bool = 'bool'
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
    axis = "'x' (0) or 'y' (1); list of both axes also allowed"
    side = "0/1 ('lower'/'upper' for x, 'left'/'right' for y); list allowed"
    xside = "'lower' or 'upper' (0 or 1); list allowed"
    yside = "'left' or 'right' (0 or 1); list allowed"
    label = 'a string or colorize object'
    docs = 'plotext.prettydoc.docs'
    function = 'a python function'

# Messages for PrettyDoc guidance
class message:
    colors = "Use plotext.colors() for available color codes."
    styles = "Use plotext.styles() for available style codes."
    components = "Use plotext.prettydoc.components() to see available components."

# Add docs class
add(docs)
doc("Initializes a PrettyDoc object to manage visually enhanced docstrings.")
par("colorless", "Excludes color formatting if True."); spec(type.bool, False)
par("separator", "Defines separator between fields."); spec(type.string, repr(" "))
out("The PrettyDoc object itself", type.docs)

# Set default pixel
add(docs.set_default_pixel)
doc("Configures default color/style for a PrettyDoc component.")
par("component", "Component to modify; see " + message.components); spec(type.string)
out("Updated PrettyDoc object", type.docs)

# List components
add(components)
doc("Lists available docstring components for customization.")

# Add function registration
add(docs.add_function)
doc("Registers a function for PrettyDoc customization until update() is called.")
par("function", "Function to document or list of functions"); spec(type.function)
par("name", "Optional function name; defaults to __qualname__")
past_out("docs.set_default_pixel")

# Add main doc
add(docs.add_doc)
doc("Adds main documentation for the most recently added function.")
par("doc", "Description of function purpose"); spec(type.label)
past_out("docs.set_default_pixel")

# Add alias
add(docs.add_alias)
doc("Assigns an alias to the most recently added function.")
par("alias", "Alias name"); spec(type.label)
past_out("docs.set_default_pixel")

# Add parameters
add(docs.add_parameter)
doc("Adds a parameter description.")
par("name", "Parameter name"); spec(type.label)
par("doc", "Parameter description"); spec(type.label)
past_out("docs.set_default_pixel")

# Parameter type and default
add(docs.add_parameter_spec)
doc("Specifies type and default for last parameter.")
par("type", "Parameter type"); spec(type.label)
par("default", "Default value"); spec(type.label, None)
past_out("docs.set_default_pixel")

# Copy past parameter
add(docs.add_past_parameter)
doc("Copies parameter from previously documented function.")
par("name", "Parameter name"); spec(type.label)
par("function", "Function containing the parameter"); spec(type.string)
past_out("docs.set_default_pixel")

# Add output
add(docs.add_output)
doc("Documents output for most recently added function.")
par("type", "Output type"); spec(type.label)
par("doc", "Output description"); spec(type.label)
past_out("docs.set_default_pixel")

# Copy past output
add(docs.add_past_output)
doc("Copies output from previously documented function.")
past("function", "docs.add_past_parameter")
past_out("docs.set_default_pixel")

# Update PrettyDoc
add(docs.update)
doc("Finalizes and applies customized docstrings.")
past_out("docs.set_default_pixel")

# Show PrettyDoc
add(docs.show)
doc("Renders all registered docstrings with color/style.")
past_out("docs.set_default_pixel")

# Add test method
add(test, name='test')
doc("Executes unit tests for PrettyDoc module.")

# Apply all updates
pd.update()