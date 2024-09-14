from .._colorize import colorize, uncolorize, pixel
from re import sub
from copy import copy
import inspect


def correct_doc(doc, capitalize = 1):
	doc = doc.strip()
	doc = doc if len(doc) == 0 or doc[-1] == '.' else doc + '.'
	doc = sub(r'\s+', ' ', doc)
	doc = doc[0].upper() + doc[1:] if capitalize else doc[0].lower() + doc[1:]
	return doc

new_lines = lambda n = 2: new_line * n
new_line = '\n'; space = ' '; comma = ', '; colon = ': '; empty = ''; period = '.'
is_colorized = lambda el: isinstance(el, colorize)
#colorize = lambda string, color, style: _colorize(string, fullground = color, style = style)

def connect_doctrings(docs, delimiter = empty):
	docs = [el for el in docs if el is not None]
	return delimiter.join(docs) if len(docs) > 0 else None

def add_prefix(doc, prefix):
	return None if doc is None else doc if prefix is None else prefix + doc

def set_attribute(object, attribute, value):
	value_copy = copy(value)
	if inspect.ismethod(value):
		def value_copy():
			getattr(value.__self__, value.__name__)()
	attributes = attribute.split('.')
	for atr in attributes[:-1]:
		if not hasattr(object, atr):
			setattr(object, atr, type('', (), {})())
		object = getattr(object, atr)
	setattr(object, attributes[-1], value_copy)


# def get_function_parameters(method):
#    spec = args(method)
#    parameters =  ([spec.varargs] if spec.varargs is not None else []) + spec.args + spec.kwonlyargs
#    parameters = [el for el in parameters if el != 'self']
#    return parameters