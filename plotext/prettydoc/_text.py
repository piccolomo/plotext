from ._utility import *


class Text:
	def __init__(self, text = None):
		self.set(text)

	def set(self, text = None):
		self.text = text
		return self

	def set_string(self, string):
		self.text.set_string(string)
		return self

	def set_pixel(self, pixel):
		self.text.set_pixel(pixel)
		return self

	def get_pixel(self):
		return self.text.get_pixel()

	def empty(self):
		return self.text is None

	def get(self):
		return self.text

	def get_string(self, colorless = 0):
		return None if self.empty() else self.get().get_string(colorless)

	def get_docstring(self, prefix = None):
		return add_prefix(self.get_string(), prefix)

	def copy(self):
		out = Text()
		out.set(self.get())
		return out


class LabelledText:
	def __init__(self, label = None, text = None):
		self.label = Text(label)
		self.value = Text(text)
		self.set_separator()

	def set_label(self, label = None):
		self.label.set(label)
		return self

	def set_value(self, value = None):
		self.value.set(value)
		return self

	def set_separator(self, separator = None):
		separator = space if separator is None else separator
		self.separator = separator

	def get_docstring(self, prefix = None):
		docs = [] if self.value.empty() else [self.label.get_docstring(), self.value.get_docstring()] 
		doc = connect_doctrings(docs, self.separator)
		return add_prefix(doc, prefix)

	def copy(self):
		out = LabelledText()
		out.label = self.label.copy()
		out.value = self.value.copy()
		out.set_separator(self.separator)	
		return out


class Alias(Text):
	def __init__(self, alias = None):
		Text.__init__(self, alias)

	def get_docstring(self, prefix = None):
		doc = None if self.empty() else "The " + self.get_string()  + '() method is an alias.'
		return add_prefix(doc, prefix)