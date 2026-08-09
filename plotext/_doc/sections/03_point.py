# Point section: the point returned by signal.get()

from plotext._doc.tools import *
from plotext._signal.point_filled import point


section('point')


# Getters

add(point.x)
doc("Returns the x coordinate of the point.")
source(["plotext.figure.signal().get()", "plotext.figure.subplot().signal().get()"])
out("The x coordinate", explanation("float"))

add(point.y)
doc("Returns the y coordinate of the point.")
source(["plotext.figure.signal().get()", "plotext.figure.subplot().signal().get()"])
out("The y coordinate", explanation("float"))

add(point.marker)
doc("Returns the marker stamped at the point.")
source(["plotext.figure.signal().get()", "plotext.figure.subplot().signal().get()"])
out("The marker object", explanation("marker"))
