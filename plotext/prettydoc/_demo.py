from ._methods import *

components_doc = {
			"title": "The function name, which appears in doc().show()",
			"alias": "The function alias",
			"doc": "The main body of the function documentation",
			"parameters.label": "The header introducing the parameters section",
			"parameter.name": "The name of the parameter",
			"parameter.type": "The type of the parameter",
			"parameter.type.label": "The \"type\" header introducing the parameter's type",
			"parameter.default": "The default value of the parameter",
			"parameter.default.label": "The \"default\" header introdusing the parameter's default value",
			"parameter.doc": "The main description of the parameter",
			"output.name": "The \"Returns\" header introducing the function output",
			"output.type": "The type of the output",
			"output.type.label": "The \"type\" header introducing the output type",
			"output.doc": "The main description of the function output"}

def components():
	colorize("PrettyDoc Components", style = 'bold').print()
	out = [colorize(el, 'cyan+', style = 'default') + space + colorize(correct_doc(components_doc[el], 0), style = "italic") for el in components_doc]
	out = [el.get_string() for el in out]
	out = new_line.join(out)
	print(out)