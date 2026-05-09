# Pixel primitive handling using clink bindings

from plotext._kernel.clink import clink
from plotext._kernel.tools import wstring


class pixel:
    # Initialize pixel pointer and optionally set properties
    def __init__(self, foreground=None, background=None, style=None, _pointer=None):
        self._pointer = clink.pixel_new() if _pointer is None else _pointer
        self.set(foreground, background, style)

    # Delete underlying pixel pointer
    def __del__(self):
        if self._pointer is not None:
            clink.pixel_delete(self._pointer)
            self._pointer = None

    # Clear pixel state
    def clear(self):
        clink.pixel_clear(self._pointer)
        return self

    # Set pixel properties
    def set(self, foreground=None, background=None, style=None):
        self._set_foreground(foreground) if foreground is not None else None
        self._set_background(background) if background is not None else None
        self._set_style(style) if style is not None else None
        return self

    # Set foreground color
    def _set_foreground(self, color=None):
        if color is None:
            return self
        if isinstance(color, int):
            return self._set_foreground_integer(color)
        if isinstance(color, (tuple, list)):
            return self._set_foreground_rgb(*color)
        return self._set_foreground_code(color)

    # Set background color
    def _set_background(self, color=None):
        if color is None:
            return self
        if isinstance(color, int):
            return self._set_background_integer(color)
        if isinstance(color, (tuple, list)):
            return self._set_background_rgb(*color)
        return self._set_background_code(color)

    # Set style
    def _set_style(self, style=None):
        if style is not None:
            self._set_style_code(style)
        return self

    # Set foreground from a palette integer
    def _set_foreground_integer(self, r):
        clink.pixel_set_fullground_integer(self._pointer, r)
        return self

    # Set foreground from an RGB triplet
    def _set_foreground_rgb(self, r, g, b):
        clink.pixel_set_fullground_rgb(self._pointer, r, g, b)
        return self

    # Set foreground from a color name string
    def _set_foreground_code(self, code):
        clink.pixel_set_fullground_code(self._pointer, code.encode('utf-8'))
        return self

    # Set background from a palette integer
    def _set_background_integer(self, r):
        clink.pixel_set_background_integer(self._pointer, r)
        return self

    # Set background from an RGB triplet
    def _set_background_rgb(self, r, g, b):
        clink.pixel_set_background_rgb(self._pointer, r, g, b)
        return self

    # Set background from a color name string
    def _set_background_code(self, code):
        clink.pixel_set_background_code(self._pointer, code.encode('utf-8'))
        return self

    # Style setter
    def _set_style_code(self, code):
        clink.pixel_set_style_code(self._pointer, code.encode('utf-8'))
        return self

    # Apply background from another pixel
    def _fix_background(self, other):
        clink.pixel_fix_background(self._pointer, other._pointer)
        return self

    # Apply full fix from another pixel
    def _fix(self, other):
        clink.pixel_fix(self._pointer, other._pointer)
        return self

    # Copy background from another pixel
    def _copy_background(self, other):
        clink.pixel_copy_background(self._pointer, other._pointer)
        return self

    # Check if pixel has no background
    def _no_background(self):
        return clink.pixel_no_background(self._pointer)

    # Return a copy of the pixel
    def copy(self):
        return pixel(_pointer=clink.pixel_copy(self._pointer))

    # Clone another pixel into this one
    def clone(self, pixel):
        clink.pixel_copy_pixel(self._pointer, pixel._pointer)
        return self

    # Debug log
    def _log(self):
        clink.pixel_log(self._pointer)
        return self

    # Get string representation
    def _get_string(self):
        p = clink.pixel_get_wstring(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # String representation
    def __repr__(self):
        return self._get_string()

    # Support copy
    def __copy__(self):
        return self.copy()
