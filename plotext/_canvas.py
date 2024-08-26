from ._link import *
from ._pixel import white_pixel
from ._points import *

class canvas:
	def __init__(self, width, height, pixel = white_pixel):
		self._pointer = canvas_new(width, height, pixel._pointer)

	def __del__(self):
		canvas_delete(self._pointer)

	def set_xlim(self, left, right):
		canvas_set_xlim(self._pointer, left, right)
		return self

	def set_ylim(self, lower, upper):
		canvas_set_ylim(self._pointer, lower, upper)
		return self

	def set_fillx_level(self, level):
		canvas_set_fillx_level(self._pointer, level)
		return self

	def set_filly_level(self, level):
		canvas_set_filly_level(self._pointer, level)
		return self

	def draw(self, points):
		canvas_draw(self._pointer, points._pointer)
		return self

	# def draw(self, x, y, marker):
	# 	points = points_class(len(x))
	# 	[points.add(xi, yi, mi) for (xi, yi, mi) in zip(x, y, marker)]
	# 	return self._draw(points)

	def show(self):
		canvas_show(self._pointer)
		return self