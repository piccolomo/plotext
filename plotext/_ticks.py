from ._correct import correct_axis, correct_side, correct_labels
from ._utility import linspace, rescale, replace_none
from ._default import xfrequency, yfrequency
import math


class tick:
	def __init__(self, position, label):
		self.set(position, label)

	def set(self, position, label):
		self.set_position(position)
		self.set_label(label)
		return self

	def set_position(self, position):
		self.position = position
		return self
	
	def set_label(self, label):
		self.label = label
		return self


	def get(self):
		return self.position, self.label

	def get_position(self):
		return self.position

	def get_label(self):
		return self.label
	

	def is_whitin_limits(self, limits):
		return self.position >= limits[0] and self.position <= limits[1]

	def copy(self):
		return tick(self.get_position(), self.get_label())

	def __repr__(self):
		return str(self.get())


class ticks:
	def __init__(self):
		self.set()

	def set(self, positions = [], labels = []):
		self._ticks = [tick(t, l) for (t, l) in zip(positions, labels)]
		return self
	
	def set_positions(self, positions):
		[t.set_position(p) for t, p in zip(self._ticks, positions)]
		return self
	
	def copy_from(self, ticks):
		self._ticks = ticks.copy()._ticks
		return self
	

	def get_positions(self, limits = None):
		return [el.get_position() for el in self._ticks]

	def get_labels(self):
		return [el.get_label() for el in self._ticks]

	def get_tuples(self):
		return [el.get() for el in self._ticks]
	

	def get_labels_width(self):
		return max([len(label) for label in self.get_labels()], default = 0)
	
	def is_active(self):
		return self.get_length() > 0

	def get_length(self):
		return len(self._ticks)


	def select(self, limits):
		new = ticks()
		new._ticks = [el.copy() for el in self._ticks if el.is_whitin_limits(limits)] 
		return new

	def copy(self):
		new = ticks()
		new._ticks = [el.copy() for el in self._ticks]
		return new


	def get_log(self):
		return 'ticks: ' + str(self._ticks)

	def __repr__(self):
		return self.get_log()



class user_ticks(ticks):
	def __init__(self):
		self.set_pixel() 
		ticks.__init__(self)
		self.set_default_frequency()
		self.set_user_limits()
		self.set_frequency()
	
	
	def set_pixel(self, pixel = None):
		self.pixel = pixel

	def set(self, positions = [], labels = None):
		labels = self.get_auto_labels(positions) if labels is None else labels
		ticks.set(self, positions, labels)
		return self
	
	def get_auto_labels(self, positions):
		labels = get_labels(positions)
		labels = correct_labels(labels, self.pixel)
		return labels
	

	def set_default_frequency(self, frequency = None):
		self.default_frequency = frequency
		return self

	def set_user_limits(self, lower = None, upper = None):
		self.user_limits = [lower, upper]

	def set_frequency(self, frequency = None):
		self.frequency = self.default_frequency if frequency is None else frequency
		return self
	

	def get_user_limits(self):
		return self.user_limits
	


	def get_log(self):
		return 'frequency: ' + str(self.frequency) + ', user limits: ' + str(self.get_user_limits())

	def __repr__(self):
		return 'Auto Ticks: ' + self.get_log()


class ruler(user_ticks):
	def __init__(self):
		user_ticks.__init__(self)
		self.ticks = ticks()
		self.rescaled_ticks = ticks()
		self.update_real_limits()


	def update_real_limits(self, signal_lower = None, signal_upper = None):
		self.real_limits = replace_none(self.user_limits, [signal_lower, signal_upper])
		return self

	def get_real_limits(self):
		return self.real_limits
	

	def get_auto_ticks(self):
		limits = self.get_real_limits()
		positions = linspace(*limits, self.frequency) if None not in limits else []
		return ticks().set(positions, self.get_auto_labels(positions))
	
	def get_ticks(self):
		limits = self.get_real_limits()
		selected = user_ticks.select(self, limits)
		return selected if selected.is_active() else self.get_auto_ticks()

	def is_active(self):
		return None not in self.get_real_limits() or user_ticks.is_active(self)


	def update(self):
		self.ticks.copy_from(self.get_ticks())
		return self
		
	def rescale(self, bins):
		limits = self.get_real_limits()
		positions = [rescale(el, *limits, bins) for el in self.ticks.get_positions(self)]
		labels = self.ticks.get_labels()
		self.rescaled_ticks.set(positions, labels)
		return self
	
	def get_rescaled_tuples(self):
		return self.rescaled_ticks.get_tuples()
	
	def get_labels_width(self):
		return self.ticks.get_labels_width()


	def __repr__(self):
		return 'Ruler: ' + user_ticks.get_log(self) + ', real limits ' + str(self.real_limits) + ', real ' + self.ticks.get_log() + ', rescaled ' + self.rescaled_ticks.get_log()


class rulers:
	def __init__(self):
		self._xruler = [ruler(), ruler()]
		self._yruler = [ruler(), ruler()]

		self.set_default_frequencies()

	def get_ruler(self, axis = 0, side = 0):
		container = self._yruler if axis else self._xruler
		return container[side]
	
	def set_default_frequencies(self):
		[el.set_default_frequency(xfrequency) for el in self._xruler]
		[el.set_frequency() for el in self._xruler]

		[el.set_default_frequency(yfrequency) for el in self._yruler]
		[el.set_frequency() for el in self._yruler]

	
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



# def set_signal_limits(self, limits = None):
# 	self.signal_limits = [None, None] if limits is None else limits
# 	return self





