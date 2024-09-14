from ._text import Text, Alias
from ._parameter import Parameter
from ._methods import *


class Function:
	def __init__(self, function):
		self.function = function
		self.doc = Text()
		self.alias = Alias()
		self.parameters_intro = Text()
		self.parameters = []
		self.output = Parameter()

	def get_name(self):
		return self.function.__qualname__.lower()

	def set_doc(self, doc = None):
		self.doc.set(doc)
		return self

	def set_alias(self, alias = None):
		self.alias.set(alias)
		return self

	def add_parameter(self, name = None, doc = None):
		parameter = Parameter(name, doc)
		self.parameters.append(parameter)
		return parameter

	def set_output(self, name = None, doc = None, type = None):
		self.output.name.set_label(name)
		self.output.name.set_value(doc)
		self.output.type.set_value(type)
		return self.output

	def get_docstring(self, colorless = False):
		docs = [self.doc.get_docstring(), self.alias.get_docstring(space), self.parameters_intro.get_docstring(space)]
		doc1 = connect_doctrings(docs, empty)
		docs = [par.get_docstring(new_lines(2)) for par in self.parameters]
		doc2 = connect_doctrings(docs)
		doc3 = self.output.get_docstring(new_lines(2))
		doc = connect_doctrings([doc1, doc2, doc3])
		return uncolorize(doc) if colorless else doc


	def show(self, colorless = False):
		print(self.get_docstring(colorless))

	def update(self, colorless = False):
		self.function.__doc__ = self.get_docstring(colorless)
		return self


	def get_parameters(self):
		return len(self.parameters)

	def last(self):
		return self.parameters[-1]

	def get_parameter(self, name):
		names = [el.get_name() for el in self.parameters]
		index = names.index(name) if name in names else None
		return self.parameters[index] if name in names else None

	def get_title(self, pixel):
		return colorize(self.get_name()).set_pixel(pixel).get_string()

	def __repr__(self):
		return "PrettyFunctionDoc(" + self.get_name() + ")"
