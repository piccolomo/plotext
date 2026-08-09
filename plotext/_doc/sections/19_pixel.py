# Pixel section: the pixel object methods

from plotext._doc.tools import *
from plotext._primitives.pixel import pixel as pixel_class


section('pixel')


# Setters

add(pixel_class.clear)
doc("Clears all color and style properties of the pixel.")
source("plotext.pixel()")
out("The pixel object itself", explanation("pixel"))


# Getters

add(pixel_class.foreground)
doc("Returns the foreground color of the pixel, as an (r, g, b) tuple, and None when the pixel carries no foreground. A name, or a number from 0 to 255, is translated into red, green and blue values by the plotext color table.")
source("plotext.pixel()")
out("The foreground color", explanation("rgb_tuple"))

add(pixel_class.background)
doc("Returns the background color of the pixel, as an (r, g, b) tuple, and None when the pixel carries no background. A name, or a number from 0 to 255, is translated into red, green and blue values by the plotext color table.")
source("plotext.pixel()")
out("The background color", explanation("rgb_tuple"))

add(pixel_class.html)
doc("Returns the HTML representation of the pixel.")
source("plotext.pixel()")
out("html string for the pixel", explanation("string"))


# Copy / clone

add(pixel_class.copy)
doc("Returns a copy of the pixel.")
source("plotext.pixel()")
out("Pixel copy", explanation("pixel"))

add(pixel_class.clone)
doc("Copies the properties from another pixel into this pixel.")
source("plotext.pixel()")
par("pixel", "Pixel object whose properties are to be cloned", explanation("pixel"))
out("The pixel object itself", explanation("pixel"))
