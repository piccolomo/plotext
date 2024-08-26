from ._link import *
from ._pixel import *


class points_class:
	def __init__(self, size):
		self._pointer = points_new(size)

	def __del__(self):
		points_delete(self._pointer)

	def add(self, x, y, marker, pixel = pixel_class(), lines = 0, fillx = 0, filly = 0):
		marker = 1 if marker == "hd" else 2 if marker == "fhd" else 3 if marker == "braille" else marker
		points_add_normal(self._pointer, x, y, c.c_wchar(marker), pixel._pointer, lines, fillx, filly) if isinstance(marker, str) else points_add_hd(self._pointer, x, y, marker, pixel._pointer, lines, fillx, filly)
		return self

	def log(self, full = 0):
		points_log(self._pointer, full)
		return self