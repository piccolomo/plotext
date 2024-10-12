from ._symbols import *
from ._colorize import colorize
#from ._utility import set_data


class axis:
	def __init__(self, axis = 0, side = 0):
		self.set_axis(axis, side)
		self.set_status()
		self.set_style()
		self.set_pixel()
		self.update_tick()

	def set_axis(self, axis = 0, side = 0):
		self.axis = axis
		self.side = side
		return self

	def set_status(self, status = True):
		self.status = status
		return self

	def set_style(self, style = None):
		self.style = style
		return self
	
	def update_tick(self):
		if self.axis:
			self.tick = get_symbol(right_node, self.style) if self.side else get_symbol(left_node, self.style)
		else:
			self.tick = get_symbol(upper_node, self.style) if self.side else get_symbol(lower_node, self.style)
	
	def set_pixel(self, pixel = None):
		self.pixel = pixel

	def get_string(self, width, corners = True):
		if self.axis:
			line = get_symbol(vertical_line, self.style)
			axis = [line] * width
			return axis
		else:
			line = get_symbol(horizontal_line, self.style)
			left = get_symbol(upper_left_corner, self.style) if self.side else get_symbol(lower_left_corner, self.style)
			right = get_symbol(upper_right_corner, self.style) if self.side else get_symbol(lower_right_corner, self.style)
			axis = [left] + [line] * (width - 2) + [right] if corners else [line] * width
			return axis


class axes:
	def __init__(self):
		self._xaxis = [axis(0, 0), axis(0, 1)]
		self._yaxis = [axis(1, 0), axis(1, 1)]

	def set_axis(self, axis = 0, side = 0, status = True, style = None, pixel = None):
		axis = self.get_axis(axis, side)
		axis.set_status(status)
		axis.set_style(style)
		axis.set_pixel(pixel)
		axis.update_tick()
		return axis

	def set_axes(self, status = True, style = None, pixel = None):
		r2 = [0, 1]
		[self.set_axis(axis, side, status, style, pixel) for axis in r2 for side in r2]
		return self

	def get_axis(self, axis = 0, side = 0):
		container = self._yaxis if axis else self._xaxis
		return container[side]
	
	def get_string(self, axis = 0, side = 0):
		return self.get_axis(axis, side).get_string()