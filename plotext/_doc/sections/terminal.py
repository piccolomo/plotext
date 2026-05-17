# Terminal class: clean/clear/prompt/limit/get_size/log/is_pressed

from plotext._doc.tools import *
from plotext._kernel.terminal import terminal as terminal_class


add(terminal_class, name = "terminal")
doc("High-level manager for terminal interaction and sizing inside plotext.")
out("A terminal object", type.terminal)

add(terminal_class.clean, name = "terminal.clean")
alias("clt")
doc("Clears the visible terminal output — either entirely, or by a specific number of lines above the prompt. Useful when plotting a continuous stream of data. Note that, depending on the terminal shell used, a few extra lines may be printed after the plot.")
par("lines", "How many lines to clean. None (default) clears the whole terminal with a hard reset. A positive integer clears that many lines above the prompt. -1 clears the screen without resetting the terminal — experimental, not used by plotext yet."); spec(type.int, None)
out("The terminal itself", type.terminal)

add(terminal_class.clear, name = "terminal.clear")
doc("Resets terminal settings, including prompt height, limit settings, and current terminal size.")
past_out("terminal.clean")

add(terminal_class.prompt, name = "terminal.prompt")
doc("Sets the height of the terminal prompt (the area reserved for user input).")
par("height", "Number of lines reserved for the terminal prompt; if None, defaults to the standard prompt height."); spec(type.int, 2)
past_out("terminal.clean")

add(terminal_class.limit, name = "terminal.limit")
doc("Sets whether to limit the master plot size to the terminal's plottable area.")
par("width", "If False, the plot width is not limited by the terminal width."); spec(type.bool, True)
par("height", "If False, the plot height is not limited by the terminal height."); spec(type.bool, True)
past_out("terminal.clean")

add(terminal_class.get_size, name = "terminal.get_size")
doc("Returns the current terminal size as a (width, height) tuple.")
par("update", "If True, updates the terminal size before returning it; if False (default), returns the last known size."); spec(type.bool, False)
par("plottable", "If True, returns only the plottable size (excluding prompt lines); if False, returns the total size."); spec(type.bool, True)
out("A tuple (width, height).", type.tuple)

add(terminal_class.log, name = "terminal.log")
doc("Prints a detailed log of the terminal, its master plot, and any subplots.")
past_out("terminal.clean")

add(terminal_class.is_pressed, name = "terminal.is_pressed")
doc("Non-blocking key poll: returns True if the user has pressed the given key since the last call. The first call sets the terminal into cbreak mode (so each keystroke is delivered immediately, without waiting for Enter) and registers an atexit hook to restore cooked mode. When stdin is not a TTY (piped, redirected, /dev/null) the function always returns False — useful for live-streaming demos that should also run cleanly in non-interactive sweeps.")
par("key", "Single character to poll for; case-insensitive"); spec(type.string, repr('q'))
out("True if the user has pressed key, else False", type.bool)
