from ._matrix import matrix
from ._ticks import get_ticks
from ._colorize import colorize


class xaxis(matrix):
	def __init__(self, width, upper = True, pixel = None, style = None):
		matrix.__init__(self, width, 1, pixel)
		ticks = get_ticks(style)
		left = ticks.upper_left if upper else ticks.lower_left
		left = colorize(left).set_pixel(pixel)
		right = ticks.upper_right if upper else ticks.lower_right
		right = colorize(right).set_pixel(pixel)
		line = ticks.horizontal * (width - 2)
		line = colorize(line).set_pixel(pixel)
		self._insert_colorize(0, 0, left)
		self._insert_colorize(1, 0, line)
		self._insert_colorize(width - 1, 0, right)


class yaxis(matrix):
	def __init__(self, height, pixel = None, style = None):
		matrix.__init__(self, 1, height, pixel)
		ticks = get_ticks(style)
		line = ticks.vertical
		line = colorize(line).set_pixel(pixel)
		[self._insert_colorize(0, r, line) for r in range(height)]

