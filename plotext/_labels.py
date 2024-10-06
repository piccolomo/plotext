from ._correct import correct_axis, correct_label, correct_side


class labels:
	def __init__(self):
		self.clear()
		#self.set_ticks_pixel()

	def set_ticks_pixel(self, pixel = None):
		self.ticks_pixel = pixel

	def clear(self):
		#self.set_ticks_pixel()
		self.xlabel = [None, None]
		self.ylabel = [None, None]
		self.title = None

	def set_label(self, axis = 0, side = 0, label = None):
		axis = correct_axis(axis)
		side = correct_side(axis, side)
		label = correct_label(label, self.ticks_pixel)
		if axis:
			self.ylabel[side] = label
		else:
			self.xlabel[side] = label
		return self

	def set_title(self, label):
		label = correct_label(label, self.ticks_pixel)
		self.title = label
		return self

	def upper_labels_present(self):
		return self.title is not None or self.xlabel[1] is not None

	def lower_labels_present(self):
		return self.xlabel[0] is not None or self.ylabel[0] is not None or self.ylabel[1] is not None


