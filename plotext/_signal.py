from ._link import *
from ._marker import marker as marker_class
from ._default import xsides, ysides

class signal:
	def __init__(self, x, y, marker, xside = None, yside = None, pointer = None):#, xside, yside, lines, fillx, filly):
		size = len(x)
		self._pointer = pointer if pointer is not None else points_new(size)
		marker = correct_marker(marker, size)
		[self.add(x[i], y[i], marker[i]) for i in range(size)]
		self._xside = correct_xside(xside)
		self._yside = correct_yside(yside)

	def get_xside(self):
		return self._xside

	def get_yside(self):
		return self._yside

	def __del__(self):
		points_delete(self._pointer)

	def add(self, x, y, marker):
		points_add(self._pointer, x, y, marker._pointer, marker.get_lines(), marker.get_fillx(), marker.get_filly())
		return self

	def at(self, index):
		return point(pointer = points_at(self._pointer, index))

	def _get_string(self, full = True):
		p = points_get_wstring(self._pointer, full)
		string = wstring.from_buffer(p).value
		wstring_delete(p)
		return string

	def log(self):
		print(self._get_string(1))

	def __repr__(self):
	 	return self._get_string(0)


class point:
	def __init__(self, pointer = None):
		self._pointer = pointer 
		
	def __del__(self):
		point_delete(self._pointer)

	def _get_string(self):
		p = point_get_wstring(self._pointer)
		string = wstring.from_buffer(p).value
		wstring_delete(p)
		return string

	def __repr__(self):
		return self._get_string()


def correct_single_marker(marker):
	return marker if isinstance(marker, marker_class) else marker_class(marker)

def correct_marker(marker, length):
	marker = marker if isinstance(marker, list) else [marker]
	marker = [correct_single_marker(el) for el in marker]
	make_copy = lambda: [el.copy() for el in marker]
	l = int(length / len(marker) + 1); L = range(l)
	[marker.extend(make_copy()) for i in L]
	return marker[ : length]

def correct_side(side, sides):
	side = sides[0] if side is None else side.strip() if isinstance(side, str) else side
	side = sides.index(side) if side in sides else side
	side = side if isinstance(side, int) and side in range(2) else 0
	return side

correct_xside = lambda side = None: correct_side(side, xsides)
correct_yside = lambda side = None: correct_side(side, ysides)



