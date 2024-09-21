from ._matrix import matrix
from ._symbols import *
from ._colorize import colorize


class xaxis(matrix):
	def __init__(self, width, upper = True, pixel = None, style = None):
		matrix.__init__(self, width, 1, pixel)

		line = get_symbol(horizontal_line, style)
		left_corner = get_symbol(upper_left_corner, style) if upper else get_symbol(lower_left_corner, style)
		right_corner = get_symbol(upper_right_corner, style) if upper else get_symbol(lower_right_corner, style)
		
		self._set_char(0, 0, left_corner) if width > 0 else None
		self._insert_string(1, 0, line * (width - 2)) if width > 2 else None
		self._set_char(width - 1, 0, right_corner) if width > 0 else None

		self.tick = get_symbol(lower_node, style) if upper else get_symbol(upper_node, style)
		self.tick_full = get_symbol(full_node, style)

	def insert(self, col, full = False):
		tick = self.tick_full if full else self.tick
		self._set_char(col, 0, tick)
		return self


class yaxis(matrix):
	def __init__(self, height, left = True, pixel = None, style = None):
		matrix.__init__(self, 1, height, pixel)

		line = get_symbol(vertical_line, style)

		[self._set_char(0, r, line) for r in range(height)]

		self.tick = get_symbol(right_node, style) if left else get_symbol(left_node, style)
		self.tick_full = get_symbol(full_node, style)

	def insert(self, row, full = False):
		tick = self.tick_full if full else self.tick
		self._set_char(0, row, tick)
		return self