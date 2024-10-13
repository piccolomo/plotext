from ._parts import parts
from ._signal import signals
from ._labels import labels
from ._ticks import rulers
from ._matrix import matrix as matrix_class
from ._default import *
from ._correct import correct_pixel, correct_axis_style
from ._pixel import pixel
from ._canvas import canvas_class
from ._axis import axes


class plot(parts, signals, labels, rulers, axes):
	def __init__(self):
		parts.__init__(self)
		signals.__init__(self)
		labels.__init__(self)
		rulers.__init__(self)
		axes.__init__(self)
		
		self.set_ticks_pixel()
		self.set_axes()
		self.set_canvas_pixel()

	def set_ticks_pixel(self, pixel = None):
		pixel = correct_pixel(pixel, default_ticks_pixel)
		labels.set_ticks_pixel(self, pixel)
		rulers.set_ticks_pixel(self, pixel)
		return self

	def set_axes(self, status = True, style = None, pixel = None):
		style = correct_axis_style(style)
		pixel = correct_pixel(pixel, default_axes_pixel)
		axes.set_axes(self, status, style, pixel)
		return self
		
	def set_canvas_pixel(self, pixel = None):
		self.canvas_pixel = correct_pixel(pixel, default_canvas_pixel)
		return self
		
	def build(self):
		# Tools
		r2 = [0, 1]

		# Upper Bar Height
		threshold = 0
		height = self.upper_labels_present(); height *= self.height >= height + threshold; threshold += height
		self.upper_bar.set_height(height)

		# Lower Bar Height
		height = self.lower_labels_present(); height *= self.height >= height + threshold; threshold += height
		self.lower_bar.set_height(height)

		# Lower Axis Height
		axis = self.get_axis(0, 0)
		height = axis.status; height *= self.height >= height + threshold; threshold += height
		self.lower_axis.set_height(height)

		# Upper Axis Height
		axis = self.get_axis(0, 1)
		height = axis.status; height *= self.height >= height + threshold; threshold += height
		self.upper_axis.set_height(height)

		# Lower Ticks Height
		ruler = self.get_ruler(0, 0)
		ruler.update_real_limits(*self.get_signal_limits(0, 0))
		ruler.update()
		height = ruler.is_active(); height *= self.height >= height + threshold; threshold += height
		self.lower_ticks.set_height(height)

		# Upper Ticks Height
		ruler = self.get_ruler(0, 1)
		ruler.update_real_limits(*self.get_signal_limits(0, 1))
		ruler.update()
		height = ruler.is_active(); height *= self.height >= threshold; threshold += height
		self.upper_ticks.set_height(height)


		# Left Axis Width
		threshold = 0
		axis = self.get_axis(1, 0)
		width = axis.status; width *= self.width >= width + threshold; threshold += width
		self.left_axis.set_width(width)

		# Right Axis Width
		axis = self.get_axis(1, 1)
		width = axis.status; width *= self.width >= width + threshold; threshold += width
		self.right_axis.set_width(width)

		# Left Ticks Width
		ruler = self.get_ruler(1, 0)
		ruler.update_real_limits(*self.get_signal_limits(1, 0))
		ruler.update()
		width = ruler.get_labels_width(); width *= self.width >= width + threshold; threshold += width
		self.left_ticks.set_width(width)

		# Right Ticks Width
		ruler = self.get_ruler(1, 1)
		ruler.update_real_limits(*self.get_signal_limits(1, 1))
		ruler.update()
		width = ruler.get_labels_width(); width *= self.width >= width + threshold; threshold += width
		self.right_ticks.set_width(width)

		# Canvas Size 
		self.update_canvas_size()

		# Upper and Lower Widths
		self.update_widths()

		# Part Positions
		self.update_positions()

		matrix = matrix_class(self.width, self.height)

		if self.upper_bar.has_size():
			matrix._insert_aligned(self.width // 2, 0, self.xlabel[1], 0) if self.xlabel[1] is not None else None
			title_centered = matrix._insert_aligned(self.width // 2, 0, self.title, 0) if self.title is not None else False
			None if title_centered else matrix._insert_aligned(0, 0, self.title, -1) if self.title is not None else None

		if self.lower_bar.has_size():
			row = self.lower_bar.row
			matrix._insert_aligned(0, row, self.ylabel[0], -1) if self.ylabel[0] is not None else None
			matrix._insert_aligned(self.width // 2, row, self.xlabel[0], 0) if self.xlabel[0] is not None else None
			matrix._insert_aligned(self.width - 1, row, self.ylabel[1], 1) if self.ylabel[1] is not None else None

		ticks = []
		if self.upper_ticks.has_size():
			col, row = self.upper_ticks.get_position()
			ruler = self.get_ruler(0, 1)
			ruler.rescale(self.canvas.width)
			ticks = [matrix._insert_dynamically(col + c, row, label) for c, label in ruler.get_rescaled_tuples()]

		if self.upper_axis.has_size():
			axis = self.get_axis(0, 1)
			string = axis.get_string(self.upper_axis.width)
			col, row = self.upper_axis.get_position()
			[matrix._set_pixelled_char(col + c, row, char, axis.pixel) for c, char in enumerate(string)]
			[matrix._set_char(c, row, axis.tick) for c in ticks if c != -1] if self.upper_axis.width > 2 else None

		ticks = []
		if self.lower_ticks.has_size():
			col, row = self.lower_ticks.get_position()
			ruler = self.get_ruler(0, 0)
			ruler.rescale(self.canvas.width)
			ticks = [matrix._insert_dynamically(col + c, row, label) for c, label in ruler.get_rescaled_tuples()]

		if self.lower_axis.has_size():
			axis = self.get_axis(0, 0)
			string = axis.get_string(self.lower_axis.width, self.upper_axis.has_size())
			col, row = self.lower_axis.get_position()
			[matrix._set_pixelled_char(col + c, row, char, axis.pixel) for c, char in enumerate(string)]
			[matrix._set_char(c, row, axis.tick) for c in ticks if c != -1] if self.lower_axis.width > 2 else None
	
		ticks = []
		if self.left_ticks.has_size():
			offset = self.canvas.row
			ruler = self.get_ruler(1, 0)
			ruler.rescale(self.canvas.height)
			[ticks.append(row + offset) if matrix._insert_aligned(0, row + offset, label, -1) else None for row, label in ruler.get_rescaled_tuples()]

		if self.left_axis.has_size():
			axis = self.get_axis(1, 0)
			string = axis.get_string(self.left_axis.height)
			col, row = self.left_axis.get_position()
			[matrix._set_pixelled_char(col, row + r, char, axis.pixel) for r, char in enumerate(string)]
			[matrix._set_char(col, r, axis.tick) for r in ticks] #if self.left_axis.height > 2 else None

		ticks = []
		if self.right_ticks.has_size():
			col = self.right_ticks.col
			offset = self.right_ticks.row
			ruler = self.get_ruler(1, 1)
			ruler.rescale(self.canvas.height)
			[ticks.append(row + offset) if matrix._insert_aligned(col, row + offset, label, -1) else None for row, label in ruler.get_rescaled_tuples()]

		if self.right_axis.has_size():
			axis = self.get_axis(1, 1)
			string = axis.get_string(self.right_axis.height)
			col, row = self.right_axis.get_position()
			[matrix._set_pixelled_char(col, row + r, char, axis.pixel) for r, char in enumerate(string)]
			[matrix._set_char(col, r, axis.tick) for r in ticks] #if self.right_axis.height > 2 else None

		if self.canvas.has_size():
			canvas = canvas_class(*self.canvas.get_size(), self.canvas_pixel)
			for axis in r2:
				for side in r2:
					ruler = self.get_ruler(axis, side)
					limits = ruler.get_real_limits()
					delta = ruler.get_limits_delta()
					canvas.set_lim(axis, side, *limits) if None not in limits else None
					canvas.set_delta(axis, side, delta)
			[canvas.draw(self.get_signal(i)) for i in self.get_Length()]
			matrix._insert_canvas(*self.canvas.get_position(), canvas)

		return matrix
