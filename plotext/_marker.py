from ._link import *
from ._pixel import pixel as pixel_class
from ._default import hd_markers, default_marker

class marker:
	def __init__(self, marker = None, foreground = None, background = None, style = None, lines = False, fillx = False, filly = False, pointer = None):
		if pointer is not None:
			self._pointer = pointer
		else:
			pixel = pixel_class(foreground, background, style); p = pixel._pointer
			marker = default_marker if marker is None else marker
			marker = hd_markers.index(marker) + 1 if marker in hd_markers else str(marker)[0]
			self._pointer = marker_new_normal(wchar(marker), p) if isinstance(marker, str) else marker_new_hd(marker, p)
		self._lines = lines
		self._fillx = fillx
		self._filly = filly

	def get_lines(self):
		return self._lines

	def get_fillx(self):
		return self._fillx

	def get_filly(self):
		return self._filly

	def _get_string(self):
		p = marker_get_wstring(self._pointer)
		string = wstring.from_buffer(p).value
		wstring_delete(p)
		return string

	def copy(self):
		pointer = marker_copy(self._pointer)
		return marker(pointer = pointer, lines = self.get_lines(), fillx = self.get_fillx(), filly = self.get_filly())

	def __repr__(self):
		return self._get_string()

	def __copy__(self):
		return self.copy()