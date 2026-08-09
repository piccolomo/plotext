# Simulate section: the sin, square and noise data generators, plus the bundled sample files

from plotext._doc.tools import *
from plotext import sin, square, noise, sample


section('simulate')


add(sin)
doc("Generates a sinusoidal signal, useful for example to test plotting routines.")
source("plotext")
par("periods", "Number of sinusoidal cycles", explanation("float"), 2)
par("length", "Total number of sample points", explanation("int"), 200)
par("amplitude", "Half the peak-to-peak amplitude of the sine wave", explanation("float"), 1)
par("phase", "Phase shift in units of pi (half cycle): 0.5 turns the sine into a cosine, 1 into its negative", explanation("float"), 0)
par("decay", "Exponential decay over the signal length; the final amplitude shrinks by a factor exp(-decay)", explanation("float"), 0)
par("offset", "Additional vertical offset", explanation("float"), 0)
out("List of floats representing the generated signal", explanation("floats"))


add(square)
doc("Generates a square wave signal alternating between +amplitude and -amplitude, useful for example to test plotting routines.")
source("plotext")
par("periods", "Number of complete square-wave cycles", explanation("float"), 2)
par("length", "Total number of sample points", explanation("int"), 200)
par("amplitude", "Half the peak-to-peak value of the square wave", explanation("float"), 1)
out("List of floats representing the generated signal", explanation("floats"))


add(noise)
doc("Generates Gaussian noise samples, useful for example to test histogram rendering.")
source("plotext")
par("length", "Total number of sample points", explanation("int"), 200)
par("amplitude", "Standard deviation of the Gaussian distribution", explanation("float"), 1)
par("offset", "Mean of the Gaussian distribution (shifts every sample by this amount)", explanation("float"), 0)
par("seed", "Integer seed for reproducible output; None (default) draws fresh values at each call", explanation("int"), repr(None))
out("List of floats representing the noise samples", explanation("floats"))


add(sample)
doc("Returns the location of a sample file shipped with plotext, useful to try the media and file methods without providing your own files.")
source("plotext")
par("name", "Name of the sample file, without extension: puppy (an image), shaq (a gif), pizzas or stock (csv tables)", explanation("string"), repr("puppy"))
out("The full path of the sample file", explanation("string"))
