# Terminal section: the terminal methods

from plotext._doc.tools import *
from plotext._kernel.terminal import terminal as terminal_class
from plotext._settings import defaults


section('terminal')


# Setters

add(terminal_class.clean)
doc("Cleans the terminal output. Called with no argument, it clears the whole terminal; called with a number of lines, it cleans only the lines printed last, so the next print takes their place, useful when streaming plots. The experimental value -1 also cleans the whole screen, but keeps the older output reachable by scrolling up, which None erases entirely; not used by plotext yet.")
source("plotext.terminal")
par("lines", "Number of last lines to clean, the whole terminal if None (default).", explanation("int"), None)
out("The terminal itself", explanation("terminal"))

add(terminal_class.clear)
doc("Resets terminal settings, including prompt height, limit settings, and current terminal size.")
source("plotext.terminal")
past_out("plotext.terminal.clean")

add(terminal_class.prompt)
doc("Sets the height of the terminal prompt (the area reserved for user input).")
source("plotext.terminal")
par("height", "Number of lines reserved for the terminal prompt; if None, defaults to the standard prompt height.", explanation("int"), 2)
past_out("plotext.terminal.clean")

add(terminal_class.limit)
doc("Sets whether to limit the master plot size to the terminal's plottable area.")
source("plotext.terminal")
par("width", "limits the plot width to the terminal width, otherwise the plot width is not limited", explanation("bool"), True)
par("height", "limits the plot height to the terminal height, otherwise the plot height is not limited", explanation("bool"), True)
past_out("plotext.terminal.clean")


# Getters

add(terminal_class.size)
doc("Returns the current terminal size.")
source("plotext.terminal")
par("update", "updates the terminal size before returning it, otherwise returns the last known size", explanation("bool"), False)
par("plottable", "returns only the plottable size (excluding prompt lines), otherwise returns the total size", explanation("bool"), True)
out("A (width, height) tuple", explanation("int_tuple"))

add(terminal_class.parent)
doc("Returns the terminal itself: the terminal sits at the top of the plots hierarchy, above the master figure, and is its own parent at every level. This method exists so that every parent() climb, from any subplot, safely ends at the terminal; calling it directly has little use.")
source("plotext.terminal")
par("level", "Ignored: the terminal is its own parent at every level", explanation("int"), 1)
out("The terminal itself", explanation("terminal"))

add(terminal_class.is_pressed)
doc("Tells whether the user has typed the given key, answering right away: if nothing was typed, it returns False instead of pausing the program to wait. It is meant to be called repeatedly inside a loop, to let the user stop a stream of plots by typing a single key; the key is caught the moment it is typed, with no need for Enter. If the program input does not come from a keyboard, as when scripts run automatically, it always returns False.")
source("plotext.terminal")
par("key", "The key to check, a single character, case-insensitive", explanation("string"), repr('q'))
out("True if the user has typed the key, False otherwise", explanation("bool"))


# Output

add(terminal_class.log)
doc("Prints the terminal state, its size, prompt height and size limits, followed by the tree of nested subplots, one indented line per plot, showing its position, its size, and the rows and columns of subplots it is divided into.")
source("plotext.terminal")
past_out("plotext.terminal.clean")
