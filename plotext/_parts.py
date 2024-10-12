class part:
	def __init__(self, name):
		self.name = name
		self.set_position()
		self.set_size()


	def set_position(self, col = None, row = None):
		self.col = None if col is None else int(col)
		self.row = None if row is None else int(row)
		return self

	def set_width(self, width):
		self.width = None if width is None else int(width)
		return self

	def set_height(self, height):
		self.height = None if height is None else int(height)
		return self

	def set_size(self, width = None, height = None):
		self.set_width(width)
		self.set_height(height)
		return self


	def has_size(self):
		return self.has_height() and self.has_width()

	def has_height(self):
		return self.height != 0

	def has_width(self):
		return self.width != 0

	def get_col(self, side = 0):
		return self.col + (self.width if side else 0)

	def get_row(self, side = 0):
		return self.row + (self.height if side else 0)
	
	def get_position(self, xside = 0, yside = 0):
		return self.get_col(xside), self.get_row(yside)

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def get_size(self):
		return self.width, self.height

	def __str__(self):
		return self.name + ': position: ' + str((self.col, self.row)) + ', size: ' + str((self.width, self.height))

	def __repr__(self):
		return str(self)


class parts:
	def __init__(self):
		self.upper_bar = part('upper bar')
		
		self.upper_ticks = part('upper ticks')
		self.upper_axis = part('upper axis')

		self.left_ticks = part('left ticks')
		self.left_axis = part('left axis')

		self.canvas = part('canvas')

		self.right_axis = part('right axis')
		self.right_ticks = part('right ticks')
		
		self.lower_axis = part('lower axis')
		self.lower_ticks = part('lower ticks')
	
		self.lower_bar = part('lower bar')

		self.set_size(0, 0)

	def set_size(self, width, height):
		self.width = max(0, width)
		self.height = max(0, height)

	def get_upper_height(self):
		return self.upper_bar.height + self.upper_axis.height + self.upper_ticks.height

	def get_lower_height(self):
		return self.lower_bar.height + self.lower_axis.height + self.lower_ticks.height

	def get_canvas_height(self):
		return self.height - self.get_upper_height() - self.get_lower_height()

	def get_left_width(self):
		return self.left_ticks.width + self.left_axis.width

	def get_right_width(self):
		return self.right_ticks.width + self.right_axis.width

	def get_canvas_width(self):
		return self.width - self.get_left_width() - self.get_right_width()

	def update_canvas_size(self):
		canvas_height = self.get_canvas_height()
		canvas_width = self.get_canvas_width()

		self.canvas.set_size(canvas_width, canvas_height)
		self.left_ticks.set_height(canvas_height)
		self.left_axis.set_height(canvas_height)
		self.right_axis.set_height(canvas_height)
		self.right_ticks.set_height(canvas_width)

	def update_widths(self):
		self.upper_bar.set_width(self.width)
		self.lower_bar.set_width(self.width)

		xwidth = self.canvas.width + self.left_axis.width + self.right_axis.width
		#xwidth = 0 if xwidth <=2 else xwidth
		self.upper_ticks.set_width(xwidth)
		self.upper_axis.set_width(xwidth)
		self.lower_axis.set_width(xwidth)
		self.lower_ticks.set_width(xwidth)


	def update_positions(self):
		self.upper_bar.set_position(0, 0)

		left_width = self.get_left_width()
		upper_height = self.get_upper_height()
	
		self.upper_ticks.set_position(left_width, self.upper_bar.get_row(1))
		self.upper_axis.set_position(self.left_ticks.width, self.upper_ticks.get_row(1))

		self.left_ticks.set_position(0, upper_height)
		self.left_axis.set_position(self.left_ticks.width, upper_height)

		self.canvas.set_position(left_width, upper_height)

		self.right_axis.set_position(self.canvas.get_col(1), upper_height)
		self.right_ticks.set_position(self.right_axis.get_col(1), upper_height)

		self.lower_axis.set_position(self.left_ticks.width, self.canvas.get_row(1))
		self.lower_ticks.set_position(left_width, self.lower_axis.get_row(1))

		self.lower_bar.set_position(0, self.lower_ticks.get_row(1))




	def get_parts(self):
		return [value for value in vars(self).values() if isinstance(value, part)]

	def log_parts(self):
		[print(el) for el in self.get_parts()]
		return self

	def test_parts(self):
		width_test = self.left_ticks.width + self.canvas.width + self.right_ticks.width == self.width
		height_test = self.upper_bar.height + self.upper_ticks.height + self.canvas.height + self.lower_bar.height + self.lower_ticks.height
		height_test2 = self.left_ticks.height == self.right_ticks.height == self.canvas.height
		print("Width Test", width_test)
		print("Height Test", height_test)
		print("Height Test 2", height_test2)
		return self