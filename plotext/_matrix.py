from ._link import *
from ._pixel import *
from ._system import write
from ._alignment import correct_ha, correct_va

class matrix:
	def __init__(self, width = 0, height = 0, pixel = pixel(background = "white"), pointer = None):
		self._pointer = matrix_new(width, height, pixel._pointer) if pointer is None else pointer

	def __del__(self):
		matrix_delete(self._pointer)

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

	def _insert_colorize(self, col, row, object, ha = -1, check_space = False):
		#object = self._correct_colorize(object)
		return matrix_insert_colorize(self._pointer, col, row, object._pointer, ha, check_space)

	def _insert_colorize_dynamically(self, col, row, object):
		#object = self._correct_colorize(object)
		return matrix_insert_colorize_dynamically(self._pointer, col, row, object._pointer)

	def _correct_matrix(self, object):
		from ._colorize import colorize
		return object.get_matrix() if isinstance(object, colorize) else colorize(object).get_matrix() if isinstance(object, str) else object

	# def _correct_colorize(self, object):
	# 	from ._colorize import colorize
	# 	return colorize(object) if isinstance(object, str) else object

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


