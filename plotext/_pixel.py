from plotext._clink import clink, wstring


class pixel:
    
    # Initialize pixel pointer and set foreground, background, style
    def __init__(self, foreground = None, background = None, style = None, _pointer = None):
        self._pointer = clink.pixel_new() if _pointer is None else _pointer
        self.set(foreground, background, style)


    # Delete pixel pointer on destruction
    def __del__(self):
        clink.pixel_delete(self._pointer)

    # Set pixel colors and style
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

    # Set foreground color by integer code
    def _set_foreground_integer(self, r):
        clink.pixel_set_fullground_integer(self._pointer, r)
        return self

    # Set foreground color by RGB tuple
    def _set_foreground_rgb(self, r, g, b):
        clink.pixel_set_fullground_rgb(self._pointer, r, g, b)
        return self

    # Set foreground color by code string
    def _set_foreground_code(self, code):
        clink.pixel_set_fullground_code(self._pointer, code.encode('utf-8'))
        return self

    # Set background color by integer code
    def _set_background_integer(self, r):
        clink.pixel_set_background_integer(self._pointer, r)
        return self

    # Set background color by RGB tuple
    def _set_background_rgb(self, r, g, b):
        clink.pixel_set_background_rgb(self._pointer, r, g, b)
        return self

    # Set background color by code string
    def _set_background_code(self, code):
        clink.pixel_set_background_code(self._pointer, code.encode('utf-8'))
        return self

    # Set style by code string
    def _set_style_code(self, code):
        clink.pixel_set_style_code(self._pointer, code.encode('utf-8'))
        return self

    # Fix pixel by copying from another pixel's pointer
    def _fix_background(self, other):
        clink.pixel_fix_background(self._pointer, other._pointer)
        return self

    # Fix pixel by copying from another pixel's pointer
    def _fix(self, other):
        clink.pixel_fix(self._pointer, other._pointer)
        return self

    # Copy background from another pixel
    def _copy_background(self, other):
        clink.pixel_copy_background(self._pointer, other._pointer)
        return self

    # Check if pixel has no background set
    def _no_background(self):
        return clink.pixel_no_background(self._pointer)

    # Create and return a copy of this pixel object
    def copy(self):
        return pixel(_pointer = clink.pixel_copy(self._pointer))

    # Clone pixel data from another pixel
    def clone(self, pixel):
        clink.pixel_copy_pixel(self._pointer, pixel._pointer)
        return self

    def get_code(self):
        return clink.pixel_get_code(self._pointer)

    # Log pixel information (for debugging)
    def _log(self):
        clink.pixel_log(self._pointer)
        return self

    # Get string representation of the pixel
    def get_string(self):
        p = clink.pixel_get_wstring(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    def __eq__(self, pixel):
        self.clone(pixel)
        return self

    # Representation of the pixel object as string
    def __repr__(self):
        return self.get_string()

    def __copy__(self):
        return self.copy()
