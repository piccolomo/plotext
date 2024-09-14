from ._text import Text, LabelledText
from ._methods import *


class Parameter:
	def __init__(self, name = None, doc = None):
		self.name = LabelledText().set_label(name).set_value(doc)
		self.type = LabelledText()
		self.default = LabelledText()

	def set_separator(self, separator = None):
		self.name.set_separator(separator)
		self.type.set_separator(separator)
		self.default.set_separator(separator)
		return self

	def set_spec(self, type = None, default = None):
		self.type.set_value(type)
		self.default.set_value(default)
		return self

	def set_type_label(self, label = None):
		self.type.label.set(label)
		return self

	def set_default_label(self, label = None):
		self.default.label.set(label)
		return self

	def get_name(self):
		return self.name.label.get_string(1)

	def get_specs_docstring(self, prefix = None):
		docs = [self.type.get_docstring(), self.default.get_docstring(comma)]
		doc = connect_doctrings(docs)
		return add_prefix(doc, prefix)

	def get_docstring(self, prefix = None):
		docs = [self.name.get_docstring(), self.get_specs_docstring(new_line)]
		doc = connect_doctrings(docs)
		return add_prefix(doc, prefix)

	def copy(self):
		out = Parameter()
		out.name = self.name.copy()
		out.type = self.type.copy()
		out.default = self.default.copy()
		return out