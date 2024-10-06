from ._correct import correct_axis, correct_side, correct_labels
from ._utility import linspace, rescale, replace_none
from ._default import xfrequency, yfrequency
import math


class single_tick:
	def __init__(self, position, label):
		self.set(position, label)

	def set_position(self,position):
		self.position = position
		return self

	def set(self, position, label):
		self.position = position
		self.label = label
		return self

	def get(self):
		return self.position, self.label

	def get_position(self):
		return self.position

	def get_label(self):
		return self.label

	def whitin_limits(self, limits):
		return self.position >= limits[0] and self.position <= limits[1]

	def __repr__(self):
		return str(self.get())


class multiple_ticks:
	def __init__(self):
		self.set_pixel() 
		self.set()

	def set_pixel(self, pixel = None):
		self.pixel = pixel

	def set_positions(self, positions):
		[t.set_position(p) for t, p in zip(self._ticks, positions)]
		return self

	def set(self, positions = [], labels = None):
		labels = get_labels(positions) if labels is None else labels
		labels = correct_labels(labels, self.pixel)
		self._ticks = [single_tick(t, l) for (t, l) in zip(positions, labels)]
		return self

	def get_positions(self, limits = None):
		return [el.get_position() for el in self._ticks]

	def get_labels(self):
		return [el.get_label() for el in self._ticks]

	def get_tuples(self):
		return [el.get() for el in self._ticks]

	def get_labels_width(self):
		return max([len(label) for label in self.get_labels()], default = 0)

	def select(self, limits):
		new = ticks()
		new._ticks = [el for el in self._ticks if el.whitin_limits(limits)] 
		return new 

	def active(self):
		return len(self._ticks) > 0

	def get_length(self):
		return len(self._ticks)

	def copy(self):
		new = ticks()
		new.ticks_pixel = self.ticks_pixel
		new._ticks = self._ticks
		return new

	def get_log(self):
		return 'ticks: ' + str(self._ticks)

	def __repr__(self):
		return self.get_log()


class auto_ticks:
	def __init__(self):
		self.set_limits()
		self.set_signal_limits()
		self.set_default_frequency()
		self.set_frequency()
	
	def set_limits(self, limits = None):
		self.limits = [None, None] if limits is None else limits

	def set_signal_limits(self, limits = None):
		self.signal_limits = [None, None] if limits is None else limits
		return self

	def set_default_frequency(self, frequency = None):
		self.default_frequency = frequency
		return self

	def set_frequency(self, frequency = None):
		self.frequency = self.default_frequency if frequency is None else frequency
		return self

	def get_real_limits(self):
		return replace_none(self.limits, self.signal_limits)

	def get_ticks(self):
		limits = self.get_real_limits()
		return linspace(*limits, self.frequency) if None not in limits else []

	def get_status(self):
		return None not in self.get_real_limits()

	def get_log(self):
		return 'frequency: ' + str(self.frequency) + ', real limits: ' + str(self.get_real_limits())

	def __repr__(self):
		return 'Auto Ticks: ' + self.get_log()


class ruler(multiple_ticks, auto_ticks):
	def __init__(self):
		multiple_ticks.__init__(self)
		auto_ticks.__init__(self)

	def within_limits(self):
		return self.select(self.get_real_limits())	

	def filter(self):
		self._ticks = self.within_limits()._ticks
		return self

	def update(self):
		self.set(auto_ticks.get_ticks(self)) if not multiple_ticks.active(self) else None
		return self

	def rescale(self, bins):
		positions = [rescale(el, *self.get_real_limits(), bins) for el in self.get_positions()]
		return self.copy().set_positions(positions)

	def get_relative_ticks(self, bins):
		return self.within_limits().rescale(bins)

	def active(self):
		return multiple_ticks.active(self) or auto_ticks.active(self)

	def copy(self):
		new = ruler()
		new.pixel = self.pixel
		new._ticks = self._ticks
		new.set_limits(self.limits)
		new.set_signal_limits(self.signal_limits)
		new.set_default_frequency(self.default_frequency)
		new.set_frequency(self.frequency)
		return new

	def __repr__(self):
		return 'Ruler: ' + auto_ticks.get_log(self) + ' ' + multiple_ticks.get_log(self) 


class ticks:
	def __init__(self):
		self._xruler = [ruler(), ruler()]
		self._yruler = [ruler(), ruler()]

		for el in self._xruler:
			el.set_default_frequency(xfrequency)
			el.set_frequency()

		for el in self._yruler:
			el.set_default_frequency(yfrequency)
			el.set_frequency()

	def set_ticks_pixel(self, pixel = None):
		[el.set_pixel(pixel) for el in self._xruler]
		[el.set_pixel(pixel) for el in self._yruler]
		return self

	def set_ticks(self, ticks = [], labels = None, axis = 0, side = 0):
		axis = correct_axis(axis)
		side = correct_xside(side)
		return self.get_ruler(axis, side).set(ticks, labels)

	def set_limits(self, lower, upper, axis = 0, side = 0):
		axis = correct_axis(axis)
		side = correct_xside(side)
		return self.get_ruler(axis, side).set_limits([lower, upper])

	def set_frequency(self, frequency, axis = 0, side = 0):
		axis = correct_axis(axis)
		side = correct_xside(side)
		return self.get_ruler(axis, side).set_frequency(frequency)

	def get_ruler(self, axis = 0, side = 0):
		container = self._yruler if axis else self._xruler
		return container[side]


def get_labels(ticks): # it returns the approximated string version of the data ticks
    d = distinguishing_digit(ticks)
    formatting_string = "{:." + str(d) + "f}"
    labels = [formatting_string.format(el) for el in ticks]
    return labels

def distinguishing_digit(data): # it return the minimum amount of decimal digits necessary to distinguish all elements of a list
    d = [_distinguishing_digit(data[i], data[i + 1]) for i in range(len(data) - 1)]
    return max(d, default = 1)

def _distinguishing_digit(a, b): # it return the minimum amount of decimal digits necessary to distinguish a from b (when both are rounded to those digits).
    d = abs(a - b)
    d = 0 if d == 0 else - math.log10(2 * d)
    d = 0 if d < 0 else math.ceil(d)
    d = d + 1 if round(a, d) == round(b, d) else d
    return d