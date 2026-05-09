# Pixel normalization utilities

from plotext._methods.object import is_list_like
from plotext._primitives.pixel import pixel as pixel_class


# Normalize a pixel into a pixel_class instance and fill any unset fields from default_pixel
def pixel(pixel, default_pixel):
    if pixel is None:
        return default_pixel.copy()
    if isinstance(pixel, (str, int)):
        result = pixel_class(pixel)
    elif is_list_like(pixel):
        result = pixel_class(*pixel)
    else:
        result = pixel.copy()
    result._fix(default_pixel)
    return result