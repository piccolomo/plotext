from ._matrix import matrix
from ._symbols import *
from ._colorize import colorize


class xticks(matrix):
	def __init__(self, width, pixel = None):
		matrix.__init__(self, width, 1, pixel)

	def is_empty(self):
		return self._is_empty(0, self.get_width(), 0, 1)

	def insert(self, col, label):
		return self._insert_string_dynamically(col, 0, label)


class yticks(matrix):
	def __init__(self, width, height, pixel = None):
		matrix.__init__(self, width, height, pixel)


	def is_empty(self):
		return self._is_empty(0, self.get_width(), 0, 1)

	def insert(self, row, label):
		return self._insert_string(0, row, label)


#		self.left = left
	# def insert(self, row, label):
	# 	col = self.get_width() - 1 if self.left else 0
	# 	ha = 1 if self.left else -1
	# 	return self._insert_string_aligned(col, row, label, ha = ha, change_color = 0)