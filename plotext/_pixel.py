from plotext._clink import clink, wstring


class pixel:

    # Initialize pixel pointer and optionally set foreground, background, style
    def __init__(self, foreground = None, background = None, style = None, _pointer = None):
        self._pointer = clink.pixel_new() if _pointer is None else _pointer
        self.set(foreground, background, style)

    # Delete pixel pointer on destruction
    def __del__(self):
        clink.pixel_delete(self._pointer)

    # Set pixel properties: foreground, background, style
    def set(self, foreground = None, background = None, style = None):
        self._set_foreground(foreground)
        self._set_background(background)
        self._set_style(style)
        return self

    # Set foreground color based on type
    def _set_foreground(self, color = None):
        if color is None:
            return self
        if isinstance(color, int):
            return self._set_foreground_integer(color)
        if isinstance(color, (tuple, list)):
            return self._set_foreground_rgb(*color)
        return self._set_foreground_code(color)

    # Set background color based on type
    def _set_background(self, color = None):
        if color is None:
            return self
        if isinstance(color, int):
            return self._set_background_integer(color)
        if isinstance(color, (tuple, list)):
            return self._set_background_rgb(*color)
        return self._set_background_code(color)

    # Set style code if provided
    def _set_style(self, style = None):
        if style is not None:
            self._set_style_code(style)
        return self

    # Foreground setters
    def _set_foreground_integer(self, r):
        clink.pixel_set_fullground_integer(self._pointer, r)
        return self

    def _set_foreground_rgb(self, r, g, b):
        clink.pixel_set_fullground_rgb(self._pointer, r, g, b)
        return self

    def _set_foreground_code(self, code):
        clink.pixel_set_fullground_code(self._pointer, code.encode('utf-8'))
        return self

    # Background setters
    def _set_background_integer(self, r):
        clink.pixel_set_background_integer(self._pointer, r)
        return self

    def _set_background_rgb(self, r, g, b):
        clink.pixel_set_background_rgb(self._pointer, r, g, b)
        return self

    def _set_background_code(self, code):
        clink.pixel_set_background_code(self._pointer, code.encode('utf-8'))
        return self

    # Style setter
    def _set_style_code(self, code):
        clink.pixel_set_style_code(self._pointer, code.encode('utf-8'))
        return self

    # Fix pixel by copying from another pixel
    def _fix_background(self, other):
        clink.pixel_fix_background(self._pointer, other._pointer)
        return self

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
        return pixel(_pointer = clink.pixel_copy(self._pointer))

    # Clone pixel data from another pixel
    def clone(self, pixel):
        clink.pixel_copy_pixel(self._pointer, pixel._pointer)
        return self

    # Get pixel code
    def get_code(self):
        return clink.pixel_get_code(self._pointer)

    # Log pixel info for debugging
    def _log(self):
        clink.pixel_log(self._pointer)
        return self

    # Get string representation
    def get_string(self):
        p = clink.pixel_get_wstring(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Override equality to clone pixel
    def __eq__(self, pixel):
        self.clone(pixel)
        return self

    # String representation
    def __repr__(self):
        return self.get_string()

    # Support copy module
    def __copy__(self):
        return self.copy()
