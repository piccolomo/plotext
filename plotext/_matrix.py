from ._link import *
from ._pixel import *


class matrix_class:
	def __init__(self, width = 0, height = 0, pixel = white_pixel, pointer = None):
		self._pointer = matrix_new(width, height, pixel._pointer) if pointer is None else pointer

	def __del__(self):
		matrix_delete(self._pointer)

	def get_width(self):
		return matrix_get_width(self._pointer)

	def get_height(self):
		return matrix_get_height(self._pointer)

	def vstack(self, matrix, adapt = False):
		return matrix_class(pointer = matrix_vstack(self._pointer, matrix._pointer, adapt))

	def hstack(self, matrix, adapt = False):
		return matrix_class(pointer = matrix_hstack(self._pointer, matrix._pointer, adapt))

	def part(self, col_start, col_stop, row_start, row_stop):
		return matrix_class(pointer = matrix_part(self._pointer, col_start, col_stop, row_start, row_stop))

	def get_vslice(self, start, stop):
		return self.part(0, self.get_width(), start, stop)

	def get_hslice(self, start, end):
		return self.part(start, end, 0, self.get_height())

	def get_row(self, row):
		return self.get_vslice(row, row + 1)

	def __getitem__(self, key):
		print(key)
		if isinstance(key, int):
			return self.get_row(key)
		elif isinstance(key, slice):
			return self.get_vslice(key.start, key.stop)
		else:
			return self.part(key[1].start, key[1].stop, key[0].start, key[0].stop)

	def get_string(self, colorless = False):
		p = matrix_get_wstring(self._pointer, colorless)
		string = wstring.from_buffer(p).value#.decode()
		wstring_delete(p)
		return string#

	def show(self):
		matrix_show(self._pointer)
		return self

	def __repr__(self):
		return self.get_string()


class colorize(matrix_class):
	def __init__(self, string, fullground = None, background = None, style = None):
		string = wstring(string)
		pixel = pixel_class().set_fullground(fullground).set_background(background).set_style(style)
		self._pointer = colorize_new(string, pixel._pointer)

	def __add__(self, matrix):
		return self.hstack(matrix, 1)

	def __truediv__(self, matrix):
		return self.vstack(matrix, 1)