from ._pixels import default_pixels
from ._function import Function
from ._text import Text
from ._utility import *
from .._utility import hash


class docs:
	def __init__(self, colorless = False, separator = None):
		self._functions = []
		self._colorless = colorless
		self._pixels = default_pixels
		self.set_separator(separator)

	def set_separator(self, separator = None):
		separator = space if separator is None else separator
		self._separator = separator
		return self

	def set_default_pixel(self, component, pixel = None):
		pixel = pixel() if pixel is None else pixel
		self._pixels[component] = pixel
		return self

	def add_function(self, function):
		self._functions.append(Function(function))
		return self

	def add_doc(self, doc = None):
		doc = self._colorize(doc, "doc")
		doc.set_string(correct_doc(doc.get_string(1), 1))
		self._last().set_doc(doc)
		return self

	def add_alias(self, alias = None):
		alias = self._colorize(alias, "alias")
		self._last().set_alias(alias)
		return self

	def _set_parameters_intro(self):
		fun = self._last(); pixel = fun.doc.get_pixel()
		fun.parameters_intro.set(colorize('This is its parameter:').set_pixel(pixel)) if fun.get_parameters() == 1 else None
		fun.parameters_intro.set(colorize('These are its parameters:').set_pixel(pixel)) if fun.get_parameters() == 2 else None
		return self

	def add_parameter(self, name = None, doc = None):
		name = self._colorize(name, "parameter.name")
		doc = self._colorize(doc, "parameter.doc")
		doc.set_string(correct_doc(doc.get_string(1), 0))
		par = self._last().add_parameter(name, doc)
		par.set_separator(self._separator)
		par.set_type_label(self._colorize("type", "parameter.type.label"))
		par.set_default_label(self._colorize("default", "parameter.default.label"))
		self._set_parameters_intro()
		return self

	def add_parameter_spec(self, type = None, default = None):
		type = self._colorize(type, "parameter.type")
		default = self._colorize(default, "parameter.default")
		self._last().last().set_spec(type, default)

	def add_past_parameter(self, name, function):
		parameter = self._get_function(function).get_parameter(name)
		self._last().parameters.append(parameter.copy())
		self._set_parameters_intro()
		return self

	def add_output(self, doc = None, type = None):
		name = self._colorize("Returns", "output.name")
		doc = self._colorize(doc, "output.doc")
		doc.set_string(correct_doc(doc.get_string(1), 0))
		type = self._colorize(type, "output.type")
		out = self._last().set_output(name, doc, type)
		out.set_type_label(self._colorize("type", "output.type.label"))
		out.set_separator(self._separator)
		return self

	def add_past_output(self, function):
		output = self._get_function(function).output
		self._last().output = output.copy()
		return self


	def update(self):
		[el.update(self._colorless) for el in self._functions]
		[set_attribute(self, el.get_name(), el.show) for el in self._functions]
		return self

	def _get_string(self):
		return (new_lines(3)).join([el.get_title(self._get_default_pixel("title")) + new_line + el.get_docstring() for el in self._functions])

	def show(self):
		print(self._get_string())
		return self

	
	def _colorize(self, text, component):
		return None if text is None else text if is_colorized(text) else colorize(text).set_pixel(self._get_default_pixel(component))

	def _get_default_pixel(self, component):
		return self._pixels[component]

	def _get_function(self, name):
		names = [el.get_name() for el in self._functions]
		index = names.index(name) if name in names else None
		return self._functions[index] if name in names else None

	def _last(self):
		return self._functions[-1]

	def _get_length(self):
		return len(self._functions)

	def __repr__(self):
		return "PrettyDoc(" + str(self._get_length()) + " functions)"

	def __add__(self, doc):
		self._functions = self._functions + doc._functions

	def _hash(self):
		return hash(self._get_string())