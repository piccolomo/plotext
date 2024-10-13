from ._link import *
from ._pixel import empty_pixel
from ._matrix import matrix
#from ._signal import *

class canvas_class:
	def __init__(self, width, height, pixel = empty_pixel):
		self._pointer = canvas_new(width, height, pixel._pointer)

	def __del__(self):
		canvas_delete(self._pointer)

	def set_lim(self, axis, side, left, right):
		canvas_set_lim(self._pointer, axis, side, left, right)
		return self

	def get_lim(self, axis = 0, side = 0):
		return canvas_get_lim_lower(self._pointer, axis, side), canvas_get_lim_upper(self._pointer, axis, side)

	def set_fill_level(self, axis, side, level):
		canvas_set_fill_level(self._pointer, axis, side, level)
		return self
	
	def set_delta(self, axis, side, delta):
		canvas_set_delta(self._pointer, axis, side, delta)
		return self


	def draw(self, signal):
		canvas_draw(self._pointer, signal._pointer, signal.xside, signal.yside)
		return self
        
	def get_matrix(self):
		pointer = canvas_get_matrix(self._pointer)
		return matrix(pointer = pointer)

	def show(self):
		canvas_show(self._pointer)
		return self
