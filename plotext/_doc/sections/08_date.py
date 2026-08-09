# Date section: the date converter methods

from plotext._doc.tools import *
from plotext._plotter.frame.date import date_class


section('date')


add(date_class.activate)
doc("Enables (or disables) date support on the axis, optionally setting the date form, origin and zone in one call.")
source(["plotext.figure.date()", "plotext.figure.subplot().date()"])
par("active", "enables or disables date support", explanation("bool"), True)
par("form", "String format used to interpret and display dates", explanation("string"), repr('%d/%m/%Y'))
par("origin", "The date used as time zero: every timestamp counts from it. Dates close to the origin keep timestamps small, making log scaled date axes readable. The origin must match the current form", explanation("date_par"), repr('01/01/1900'))
par("zone", "The hours from UTC the axis is written in, 3 for Moscow and 5.5 for India: a date given with no zone of its own is read in it, and every date is written back in it", explanation("float"), 0)
out("The date selection itself", explanation("date_converter"))


add(date_class.convert)
doc("Converts a date, or a list of dates, between string, datetime and timestamp forms.")
source(["plotext.figure.date()", "plotext.figure.subplot().date()"])
par("time", "The date to convert, or a list of dates", explanation("date_par") + "; a list of dates is also allowed")
par("output", "Output form of the conversion", explanation("date_output"), repr('timestamp'))
out("The converted date, or list of dates", explanation("date_par") + "; a list of dates is also allowed")


add(date_class.today)
doc("Returns today's date in the requested form.")
source(["plotext.figure.date()", "plotext.figure.subplot().date()"])
par("output", "Output form of the date", explanation("date_output"), repr('datetime'))
out("Today's date", explanation("date_par"))


add(date_class.origin)
doc("Returns the date used as time zero, in the requested form.")
source(["plotext.figure.date()", "plotext.figure.subplot().date()"])
past_par("output", "plotext.figure.date().today")
out("The origin date", explanation("date_par"))


add(date_class.active)
doc("Returns whether date support is on for the axis.")
source(["plotext.figure.date()", "plotext.figure.subplot().date()"])
out("Whether date support is on for the axis", explanation("bool"))


add(date_class.clear)
doc("Resets the date form and origin and turns date support off.")
source(["plotext.figure.date()", "plotext.figure.subplot().date()"])
past_out("plotext.figure.date().activate")
