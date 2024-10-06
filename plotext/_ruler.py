# from ._matrix import matrix
# from ._symbols import *
# from ._colorize import colorize
from ._correct import correct_axis, correct_side
from ._utility import linspace, rescale, replace_none
from ._default import xfrequency, yfrequency


class single_tick:
	def __init__(self, tick, label = None):
		self.set(tick, label)
		self.set_position()

	def set(self, tick, label = None):
		self.tick = tick
		self.label = str(tick) if label is None else label

	def set_position(self, position = None):
		self.position = position

	def get(self):
		return self.position, self.label

	def get_tick(self):
		return self.tick

	def get_label(self):
		return self.label

	def __repr__(self):
		return str(self.get())


class multiple_ticks:
	def __init__(self, frequency):
		self.set_default_frequency(frequency)
		self.set_frequency()
		self.set()
		self.set_limits()
		

	def set_frequency(self, frequency = None):
		self.frequency = self.default_frequency if frequency is None else frequency
		return self

	def set_default_frequency(self, frequency = None):
		self.default_frequency = frequency
		return self

	def get_auto_ticks(self, frequency):
		return linspace(*self.limits, self.frequency) if None not in self.limits else None 


	def set(self, ticks = [], labels = None):
		self.list = [single_tick(t) for t in ticks] if labels is None else [single_tick(t, l) for (t, l) in zip(ticks, labels)]


	def set_limits(self, left = None, right = None):
		self.limits = [left, right]

	def correct_limits(self, signal_limits):
		limits = replace_none(self.limits, signal_limits)
		self.set_limits(limits)


	def get_ticks(self):
		return [el.get_tick() for el in self.list]

	def get_labels(self):
		return [el.get_label() for el in self.list]

	def get_labels_width(self):
		return max([len(label) for label in self.get_labels()], default = 0)

	def get_positions(self):
		return [el.get_position() for el in self.list]

	def update_positions(self, bins):
		positions = rescale(self.get_ticks(), *self.get_limits(), bins)
		[t.set_position(p) for (t, p) in zip(self.list, positions)]
		return self

	def __repr__(self):
		return str(self.list)


class ticks:
	def __init__(self):
		self._xticks = [multiple_ticks(xfrequency), multiple_ticks(xfrequency)]
		self._yticks = [multiple_ticks(yfrequency), multiple_ticks(yfrequency)]

	def get_ruler(self, axis = 0, side = 0):
		# axis = correct_axis(axis)
		# side = correct_xside(side)
		container = self._yticks if axis else self._xticks
		return container[side]