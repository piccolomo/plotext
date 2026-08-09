# Media section: image, gif and video

from plotext._doc.tools import *
from plotext._plotter.plot import plot_class
from plotext import image, gif, video


section('media')


add(plot_class.image)
doc("Creates an image signal from a local path or a web address. Slower than plotext.image, but it renders as a normal plot.")
source(["plotext.figure", "plotext.figure.subplot()"])
par("path", "Local path or web address of the file; web addresses are downloaded once and reused on later calls", explanation("string"))
par("gray", "converts the image to grayscale before rendering", explanation("bool"), False)
past_par("symbol", "plotext.figure.heatmap")
out("The composed image signal", explanation("signal"))


add(image)
doc("Opens an image file, from a local path or a web address, and paints it into a plotext matrix; call .print() on the result. Roughly 5-10x faster than figure.image().")
source("plotext")
past_par("path", "plotext.figure.image")
past_par("gray", "plotext.figure.image")
par("width", "image width in canvas characters", explanation("int"), None)
par("height", "image height in canvas characters", explanation("int"), None)
par("ratio", "keeps the image proportions (accounting for terminal cells being taller than wide), otherwise the image is stretched to exactly the given width and height", explanation("bool"), True)
out("A painted plotext.matrix ready to print", explanation("matrix"))


add(gif)
doc("Plays a GIF, from a local path or a web address. Pressing q stops the stream.")
source("plotext")
past_par("path", "plotext.figure.image")
par("gray", "converts each frame to grayscale before rendering", explanation("bool"), False)
past_par("width", "plotext.image")
past_par("height", "plotext.image")
par("ratio", "keeps each frame's proportions (accounting for terminal cells being taller than wide), otherwise each frame is stretched to exactly the given width and height", explanation("bool"), True)
par("loop", "replays forever until q is pressed, otherwise plays once and returns", explanation("bool"), False)
par("seconds", "stops the stream after this many seconds, if None it goes on until its natural end or when q is pressed", explanation("float"), repr(None))


add(video)
doc("Plays a video, with its audio, from a local path, a web address or a YouTube address. Pressing q stops the stream.")
source("plotext")
par("path", "Local path, web address or YouTube address of the video; web addresses are downloaded once and reused on later calls, while YouTube addresses are streamed directly", explanation("string"))
past_par("gray", "plotext.gif")
past_par("width", "plotext.image")
past_par("height", "plotext.image")
past_par("ratio", "plotext.gif")
par("loop", "replays forever until q is pressed, otherwise plays once and returns", explanation("bool"), False)
past_par("seconds", "plotext.gif")
