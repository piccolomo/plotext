# Pixel normalization utilities

from plotext._methods.object import is_list_like
from plotext._primitives.pixel import pixel as pixel_class


# Normalize a pixel into a pixel_class instance and fill any unset fields from default_pixel
def pixel(pixel, default_pixel):
    if pixel is None:
        return default_pixel.copy()
    if isinstance(pixel, (str, int)):
        result = pixel_class(pixel)
    elif is_list_like(pixel) and len(pixel) <= 3:
        result = pixel_class(*pixel)
    else:
        result = pixel.copy()
    result._fix(default_pixel)
    return result


# Coerce a pixel_par (None, string, integer, tuple, or pixel object) into a fresh pixel_class instance. A tuple/list of all integers is read as an RGB foreground color; otherwise it is read as (foreground, background, style) and must have at most 3 entries.
def pixel_par(par):
    if par is None:
        return pixel_class()
    if isinstance(par, pixel_class):
        return par.copy()
    if isinstance(par, (str, int)):
        return pixel_class(par)
    if is_list_like(par) and len(par) == 3 and all(isinstance(el, int) and 0 <= el <= 255 for el in par):
        return pixel_class(par)
    if is_list_like(par) and len(par) <= 3:
        return pixel_class(*par)
    return par