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


	def get_position(self, xside = 0, yside = 0):
		col = self.col + (self.width if xside else 0)
		row = self.row + (self.height if yside else 0)
		return col, row

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def get_size(self):
		return self.width, self.height

	def get_col(self):
		return self.col

	def get_row(self):
		return self.row

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

	# def add_part(self, name):
	# 	self.part[name] = part()
	# 	return self.part[name]

	# def get_part(self, name):
	# 	return self.part[name]


	# def set_part_position(self, name, col, row):
	# 	return self.get_part(name).set_position(col, row)

	# def set_part_size(self, name, width, height):
	# 	return self.get_part(name).set_size(width, height)

	# def set_part_width(self, name, width):
	# 	return self.get_part(name).set_width(width)

	# def set_part_height(self, name, height):
	# 	return self.get_part(name).set_height(height)


	# def get_part_position(self, name, xside = 0, yside = 0):
	# 	return self.get_part(name).get_position(xside, yside)

	# def get_part_width(self, name):
	# 	return self.get_part(name).get_width()

	# def get_part_height(self, name):
	# 	return self.get_part(name).get_height()


	# def part_has_size(self, name):
	# 	return self.get_part(name).has_size()

	# def part_has_width(self, name):
	# 	return self.get_part(name).has_width()

	# def part_has_height(self, name):
	# 	return self.get_part(name).has_height()

	# def log_parts(self):
	# 	[print(k + ':', self.part[k]) for k in self.part.keys()]
	# 	return self
