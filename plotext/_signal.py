from ._link import *
from ._marker import marker as marker_class
from ._correct import correct_marker, correct_side
from ._utility import linspace


class signals:
	def __init__(self):
		self._signal = []

	def get_length(self):
		return len(self._signal)
		
	def get_Length(self):
		return range(self.get_length())

	def add_signal(self, x, y, m, label = None, xside = 0, yside = 0):
		length = min(len(x), len(y))
		x = x[: length]
		y = y[: length]
		m = correct_marker(m, length)
		xside = correct_side(0, xside)
		yside = correct_side(1, yside)
		self._signal.append(signal(x, y, m, self.check_label(label), xside, yside))
		return self

	def check_label(self, label):
		return 'signal(' + str(self.get_length()) + ')' if label is None else label

	def get_signal(self, i):
		return self._signal[i]


	def get_signal_limits(self, axis = 0, side = 0):
		return self.get_signal_ylim(side) if axis else self.get_signal_xlim(side)

	def get_signal_xlim(self, side = 0):
		return (self._get_signal_xmin(side), self._get_signal_xmax(side))

	def get_signal_ylim(self, side = 0):
		return (self._get_signal_ymin(side), self._get_signal_ymax(side))

	def _get_signal_xmin(self, side = 0):
		return min([s.get_xmin() for s in self._signal if s.xside == side], default = None)

	def _get_signal_xmax(self, side = 0):
		return max([s.get_xmax() for s in self._signal if s.xside == side], default = None)

	def _get_signal_ymin(self, side = 0):
		return min([s.get_ymin() for s in self._signal if s.yside == side], default = None)

	def _get_signal_ymax(self, side = 0):
		return max([s.get_ymax() for s in self._signal if s.yside == side], default = None)



class signal:
	def __init__(self, x, y, m, label, xside, yside):
		length = len(x)
		self._pointer = points_new(length)
		[self.add(x[i], y[i], m[i]) for i in range(length)]
		self.label = label
		self.xside = xside
		self.yside = yside

	def __del__(self):
		points_delete(self._pointer)

	def get_length(self):
		return points_get_length(self._pointer)

	def add(self, x, y, marker):
		points_add(self._pointer, x, y, marker._pointer, 0, 0, 0)
		return self

	def at(self, index):
		return point(pointer = points_at(self._pointer, index))

	def get_xmin(self):
		return points_get_xmin(self._pointer)

	def get_xmax(self):
		return points_get_xmax(self._pointer)

	def get_ymin(self):
		return points_get_ymin(self._pointer)

	def get_ymax(self):
		return points_get_ymax(self._pointer)

	def _get_string(self, full = True):
		p = points_get_wstring(self._pointer, full)
		string = wstring.from_buffer(p).value
		wstring_delete(p)
		return string

	def log(self):
		print(self._get_string(1))

	def __repr__(self):
	 	return self._get_string(0)




class point:
	def __init__(self, pointer = None):
		self._pointer = pointer 
		
	def __del__(self):
		point_delete(self._pointer)

	def _get_string(self):
		p = point_get_wstring(self._pointer)
		string = wstring.from_buffer(p).value
		wstring_delete(p)
		return string

	def __repr__(self):
		return self._get_string()