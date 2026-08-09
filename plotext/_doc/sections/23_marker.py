# Marker section: the marker object methods

from plotext._doc.tools import *
from plotext._primitives.marker import marker as marker_class


section('marker')


# Setters

add(marker_class.fill)
doc("Applies a pixel to the marker, replacing its current color and style.")
source("plotext.marker()")
par("pixel", "Pixel that determines the color and style", explanation("pixel_par"))
out("The marker object itself", explanation("marker"))


# Getters

add(marker_class.pixel)
doc("Returns the pixel holding the marker's color and style.")
source("plotext.marker()")
out("A pixel object", explanation("pixel"))

add(marker_class.copy)
doc("Returns a copy of the marker.")
source("plotext.marker()")
out("Marker copy", explanation("marker"))
