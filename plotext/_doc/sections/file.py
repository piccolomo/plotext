# File I/O helpers exposed under plotext.file

from plotext._doc.tools import *
from plotext._methods.file import file

section('file')


add(file.correct, name = "file.correct")
doc("Expands `~/...` paths to the user's home folder. Other paths pass through unchanged.")
par("path", "Path to expand"); spec(type.string)
out("Expanded path", type.string)

add(file.read, name = "file.read")
doc("Reads the contents of a file. Dispatches by extension: `.csv` returns a list of rows (uses the stdlib csv module, so quoting/escaping/commas-in-values work correctly); any other extension returns the file's text as a string.")
par("path", "File path"); spec(type.string)
out("File contents (string for text files, list of rows for .csv)", type.string)

add(file.write, name = "file.write")
doc("Writes to a file. Dispatches by extension: `.csv` expects a list of rows; any other extension expects a string. Pass `append=True` to append instead of overwriting.")
par("data", "Text (for non-csv extensions) or list of rows (for .csv)"); spec(type.string)
par("path", "File path"); spec(type.string)
par("append", "If True, append to the file instead of overwriting"); spec(type.bool, False)

add(file.exists, name = "file.exists")
doc("Returns True if the path refers to an existing filesystem entry.")
par("path", "Path to check"); spec(type.string)
out("True if the path exists", type.bool)

add(file.delete, name = "file.delete")
doc("Removes the file at the given path. No-op if it does not exist.")
par("path", "Path to remove"); spec(type.string)

add(file.parent, name = "file.parent")
doc("Returns the parent directory of a path. With no `path` argument, returns the caller's script folder. `level > 1` walks further up.")
par("path", "Path whose parent is wanted; None means the caller's script"); spec(type.string, None)
par("level", "How many levels to walk up"); spec(type.int, 1)
out("Parent path", type.string)

add(file.join, name = "file.join")
doc("Joins path components into an absolute path. The first part can be `~` to mean the home folder.")
par("args", "Path parts to join"); spec(type.string)
out("Absolute joined path", type.string)

add(file.download, name = "file.download")
doc("Downloads a URL to a local path (wraps urllib.request.urlretrieve).")
par("url", "URL to download"); spec(type.string)
par("path", "Local file path"); spec(type.string)
