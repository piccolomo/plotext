from ._link import *
from ._pixel import pixel as pixel_class
from ._system import write
from ._alignment import correct_ha, correct_va
from ._utility import hash


class matrix:
	def __init__(self, width = 0, height = 0, pixel = None, pointer = None):
		px = pixel_class(background = "white") if pixel is None else pixel
		self._pointer = matrix_new(width, height, px._pointer) if pointer is None else pointer

	def __del__(self):
		matrix_delete(self._pointer)

	def clear(self):
		matrix_clear(self._pointer)
		return self

	def get_width(self):
		return matrix_get_width(self._pointer)

	def get_height(self):
		return matrix_get_height(self._pointer)

	def get_string(self, colorless = False):
		p = matrix_get_wstring(self._pointer, colorless)
		string = wstring.from_buffer(p).value
		wstring_delete(p)
		return string

	def print(self, colorless = False, end = '\n', flush = True):
		matrix_show(self._pointer, colorless)
		write(end, flush)
		return self

	def copy(self):
		return matrix(pointer = matrix_copy(self._pointer))

	def vstack(self, object, adapt = True):
		object = self._correct_matrix(object)
		return self._vstack(object, adapt)

	def hstack(self, object, adapt = True):
		object = self._correct_matrix(object)
		return self._hstack(object, adapt)

	def insert(self, col, row, object, ha = -1, va = -1, adapt = True):
		ha = correct_ha(ha)
		va = correct_va(va)
		object = self._correct_matrix(object)
		matrix_insert(self._pointer, col, row, object._pointer, ha, va, adapt)
		return self

	def _insert_aligned(self, col, row, label, ha = -1, check_space = 1, change_color = True):
		#object = self._correct_colorize(string)
		return matrix_insert_aligned(self._pointer, col, row, label._pointer, ha, check_space, change_color)

	def _insert_dynamically(self, col, row, label):
		#object = self._correct_colorize(string)
		return matrix_insert_dynamically(self._pointer, col, row, label._pointer)

	def _insert_string(self, col, row, string):
		return matrix_insert_wstring(self._pointer, col, row, wstring(string))

	def _insert_canvas(self, col, row, canvas):
		matrix_insert_canvas(self._pointer, col, row, canvas._pointer)
		return self

	def _set_char(self, col, row, char):
		#object = self._correct_colorize(object)
		matrix_set_char(self._pointer, col, row, wchar(char))
		return self
	
	def _set_pixel(self, col, row, pixel):
		#object = self._correct_colorize(object)
		matrix_set_pixel(self._pointer, col, row, pixel._pointer)
		return self
	
	def _set_pixelled_char(self, col, row, char, pixel):
		self._set_char(col, row, char)
		self._set_pixel(col, row, pixel)
		return self

	def _correct_matrix(self, object):
		from ._colorize import colorize
		return object.get_matrix() if isinstance(object, colorize) else colorize(object).get_matrix() if isinstance(object, str) else object

	def _correct_colorize(self, object):
		from ._colorize import colorize
		return colorize(object) if isinstance(object, str) else object

	def _vstack(self, object, adapt = False):
		return matrix(pointer = matrix_vstack(self._pointer, object._pointer, adapt))

	def _hstack(self, object, adapt = False):
		return matrix(pointer = matrix_hstack(self._pointer, object._pointer, adapt))

	def _part(self, col_start, col_stop, row_start, row_stop):
		return matrix(pointer = matrix_part(self._pointer, col_start, col_stop, row_start, row_stop))

	def _is_empty(self, col_start, col_stop, row_start, row_stop):
		return matrix_is_empty(self._pointer, col_start, col_stop, row_start, row_stop)

	def _get_vslice(self, start, stop):
		return self.part(0, self.get_width(), start, stop)

	def _get_hslice(self, start, end):
		return self.part(start, end, 0, self.get_height())

	def _get_row(self, row):
		return self.get_vslice(row, row + 1)

	def __repr__(self):
		return self.get_string()

	def __add__(self, object):
		return self.hstack(object, 1)

	def __truediv__(self, object):
		return self.vstack(object, 1)

	def __copy__(self):
		return self.copy()

	def __str__(self):
		return self.get_string()

	def _hash(self):
		return hash(self.get_string())

	def __getitem__(self, key):
		width, height = self.get_width(), self.get_height()
		key = (key, slice(0, width)) if isinstance(key, int) or isinstance(key, slice) else key
		col_key = correct_slice(key[1], width)
		row_key = correct_slice(key[0], height)
		return self._part(col_key.start, col_key.stop, row_key.start, row_key.stop)

def correct_slice(key, bins):
	key = slice(key, key + 1) if isinstance(key, int) else key
	key = slice(0, key.stop) if key.start is None else key
	key = slice(key.start, bins - 1) if key.stop is None else key
	return key


