from ._link import *
from ._pixel import *
from ._matrix import *
from ._system import write


class colorize():
	def __init__(self, string = None, foreground = None, background = None, style = None, pointer = None):
		if pointer is None:
			px = pixel(foreground, background, style)
			self._pointer = colorize_new(wstring(str(string)), px._pointer)
		else:
			self._pointer = pointer

	def set_pixel(self, pixel = None):
		pixel = pixel() if pixel is None else pixel
		colorize_set_pixel(self._pointer, pixel._pointer)
		return self

	def set_string(self, string):
		new = colorize(string).set_pixel(self.get_pixel())
		return self.assign(new)

	def get_length(self):
		return colorize_get_length(self._pointer)

	def get_pixel(self):
		return pixel(pointer = colorize_get_pixel(self._pointer))

	def get_matrix(self):
		return matrix(pointer = colorize_get_matrix(self._pointer))

	def get_string(self, colorless = False):
		p = colorize_get_wstring(self._pointer, colorless)
		string = wstring.from_buffer(p).value
		wstring_delete(p)
		return string

	def print(self, colorless = False, end = '\n', flush = True):
		colorize_show(self._pointer, colorless)
		write(end, flush);
		return self

	def copy(self):
		return colorize(pointer = colorize_copy(self._pointer))

	def _part(self, start, stop):
		return colorize(pointer = colorize_part(self._pointer, start, stop))

	def hstack(self, string, adapt = True):
		string  = colorize(string) if isinstance(string, str) else string
		return self.get_matrix().hstack(string.get_matrix(), adapt)

	def vstack(self, string, adapt = True):
		string  = colorize(string) if isinstance(string, str) else string
		return self.get_matrix().vstack(string.get_matrix(), adapt)

	def assign(self, string):
		string  = colorize(string) if isinstance(string, str) else string
		colorize_copy_from(self._pointer, string._pointer)
		return self

	def __repr__(self):
		return self.get_string()

	def __add__(self, string):
		return self.hstack(string, 1)

	def __truediv__(self, string):
		return self.vstack(string, 1)

	def __len__(self):
		return self.get_length()

	def __getitem__(self, key):
		key = correct_slice(key, self.get_length())
		return self._part(key.start, key.stop)

	def __eq__(self, string):
		string  = colorize(string) if isinstance(string, str) else string
		return colorize_equals(self._pointer, string._pointer)

	def __copy__(self):
		return self.copy()

	def __str__(self):
		return self.get_string()



ansi_begin = '\x1b['

def uncolorize(string): # remove color codes from colored string
    colored = lambda: ansi_begin in string
    while colored():
        b = string.index(ansi_begin)
        e = string[b : ].index('m') + b + 1
        string = string.replace(string[b : e], '')
    return string