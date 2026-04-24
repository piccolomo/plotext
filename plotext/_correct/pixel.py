# Pixel normalization utilities

from plotext._methods.object import is_list_like


# Normalize a pixel into a pixel_class instance
def pixel(pixel, default_pixel):
    if pixel is None:
        return default_pixel.copy()
    if isinstance(pixel, (str, int)):
        return pixel_class(pixel)
    if is_list_like(pixel):
        return pixel_class(*pixel)
    return pixel