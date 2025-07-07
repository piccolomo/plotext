from plotext.prettydoc import * 
from plotext.prettydoc._docs import docs_class as docs  # Import all core functions and classes

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


class type:  # Class defining different data types for documentation
    bool = 'bool'  # Boolean type
    docs = 'plotext.prettydoc.docs'  # PrettyDoc class
    string = 'string'  # String type
    function = 'function'  # Function type
    colorize_plus = "plotext.colorize or string"  # Colorize plus type

    float = 'float'  # Float type
    floats = 'floats'  # Floats type
    int = 'int'  # Integer type

    pixel = "plotext.pixel"  # Pixel type in plotext
    colorize = "plotext.colorize"  # Colorize type
    matrix = "plotext.matrix"  # Matrix type
    matrix_plus = "plotext.matrix or plotext.colorize or a string"  # Matrix or colorize or string type
    color = "string color code, integer (lower than 256), a tuple of 3 integers (each lower than 256)"  # Color type
    alignment = "string or integer"  # Alignment type

class message:  # Class for message components in PrettyDoc
    components = "Access the plotext.prettydoc.components() method for the available components."  # Message for accessing PrettyDoc components

# Adding function documentation to PrettyDoc instance
add(docs, 'docs')  
doc("An object of this class is used to add beautiful docstrings to your functions.")
par("colorless", "Determines whether the function docstrings should be colorless. Regardless of this parameter, the colored version is registered as an attribute (named after the function) of the class object")  
spec(type.bool, False)  # Specifying the type for 'colorless' parameter
par("separator", "specifies the separator between fields like parameter name and its description, etc.")  
spec(type.string, repr(" "))  # Specifying the type for 'separator' parameter
out("itself", type.docs)  # Adding output documentation

# Adding documentation for set_default_pixel method
add(docs.set_default_pixel, 'docs.set_default_pixel')  
doc("It allows to change the default coloring of a specific prettydoc docstring component.")
par("component", "Specifies which component to change the coloring of; " + message.components)  
spec(type.string)  # Specifying type for 'component'
out("itself, updated", type.docs)  # Adding output documentation

# Adding documentation for components method
add(components, 'components')  
doc("It displays the available docstring components, which can be modified using the plotext.prettydoc.docs().set_default_pixel() method.")

# Adding documentation for add_function method
add(docs.add_function, 'docs.add_function')  
doc("It adds a function to the docs() object. Once the function all subsequent methods will refer to the last function added. Finally use the docs.update() method to process and register the docstrings.")
par("function", "The function to which the pretty docstring will be added.")
par("name", "The name of the function. If None, it defaults to the function’s __qualname__ attribute.")  
spec("a function", "None")  # Specifying type for 'function'
past_out("docs.set_default_pixel")  # Adding output from past method

# Adding documentation for add_doc method
add(docs.add_doc, 'docs.add_doc')  
doc("It adds the documentation body to the last function.")
par("doc", "the documentation describing the function")  
spec(type.colorize_plus)  # Specifying type for 'doc'
past_out("docs.set_default_pixel")  # Adding output from past method

# Adding documentation for add_alias method
add(docs.add_alias, 'docs.add_alias')  
doc("It adds an alias to the last function.")
par("alias", "the name of the alias")  
spec(type.colorize_plus)  # Specifying type for 'alias'
past_out("docs.set_default_pixel")  # Adding output from past method

# Adding documentation for add_parameter method
add(docs.add_parameter, 'docs.add_parameter')  
doc("It adds a parameter to the last function.")
par("name", "the name of the parameter")  
spec(type.colorize_plus)  # Specifying type for 'name'
par("doc", "its main description")  
spec(type.colorize_plus)  # Specifying type for 'doc'
past_out("docs.set_default_pixel")  # Adding output from past method

# Adding documentation for add_parameter_spec method
add(docs.add_parameter_spec, 'docs.add_parameter_spec')  
doc("It adds the type and default specification to the last parameter added.")
par("type", "its type")  
spec(type.colorize_plus)  # Specifying type for 'type'
par("default", "its default value")  
spec(type.colorize_plus)  # Specifying type for 'default'
past_out("docs.set_default_pixel")  # Adding output from past method

# Adding documentation for add_past_parameter method
add(docs.add_past_parameter, 'docs.add_past_parameter')  
doc("It adds a parameter from a previously added function to the current one.")
par("name", "the name of the parameter")  
spec(type.colorize_plus)  # Specifying type for 'name'
par("function", "the past function name")  
spec(type.colorize_plus)  # Specifying type for 'function'
past_out("docs.set_default_pixel")  # Adding output from past method

# Adding documentation for add_output method
add(docs.add_output, 'docs.add_output')  
doc("It adds the output documentation to the last function.")
par("type", "the output type")  
spec(type.colorize_plus)  # Specifying type for 'type'
par("doc", "the output main description")  
spec(type.colorize_plus)  # Specifying type for 'doc'
past_out("docs.set_default_pixel")  # Adding output from past method

# Adding documentation for add_past_output method
add(docs.add_past_output, 'docs.add_past_output')  
doc("It adds the output details from a previously added function to the current one.")
past("function", "docs.add_past_parameter")  # Using past function for 'function'
past_out("docs.set_default_pixel")  # Adding output from past method

# Adding documentation for update method
add(docs.update, 'docs.update')  
doc("It processes and updates the function docstrings.")
past_out("docs.set_default_pixel")  # Adding output from past method

# Adding documentation for show method
add(docs.show, 'docs.show')  
doc("It displays all the docstrings with color formatting.")
past_out("docs.set_default_pixel")  # Adding output from past method

# Adding documentation for test method
add(test, 'test')  
doc("It performs unit tests for the prettydoc module.")

pd.update()  # Update the PrettyDoc instance with all added documentation