# File section: the file toolkit methods

from plotext._doc.tools import *
from plotext._methods.file import file


section('file')


add(file.join)
doc("Joins path components into an absolute path. The first part can be ~ to mean the home folder.")
source("plotext.file")
par("*args", "Path parts to join", explanation("string"))
out("Absolute joined path", explanation("string"))

add(file.parent)
doc("Returns the parent directory of a path. With no path argument, returns the caller's script folder. level > 1 walks further up.")
source("plotext.file")
par("path", "Path whose parent is wanted; None means the caller's script", explanation("string"), None)
par("level", "How many levels to walk up", explanation("int"), 1)
out("Parent path", explanation("string"))

add(file.read)
doc("Reads the contents of a file as a string.")
source("plotext.file")
par("path", "File path", explanation("string"))
past_par("log", "plotext.matrix().save")
out("The file's text", explanation("string"))

add(file.write)
doc("Writes a string to a file.")
source("plotext.file")
par("text", "The text to write", explanation("string"))
par("path", "File path", explanation("string"))
par("append", "appends to the file instead of overwriting", explanation("bool"), False)
past_par("log", "plotext.file.read")

add(file.csv, name = "csv")
doc("Reads a csv file as a table: a list of rows, each being a list of strings.")
source("plotext.file")
par("path", "File path", explanation("string"))
par("delimiter", "Character separating the values of a row", explanation("string"), repr(','))
past_par("log", "plotext.file.read")
out("The file's table", "a list of rows, each being a list of strings")

add(file.string, name = "string")
doc("Turns a table (a list of rows, holding strings or numbers) into a single string in csv form, ready to be written with write().")
source("plotext.file")
par("data", "The table to convert", "a list of rows, each being a list of strings or numbers")
past_par("delimiter", "plotext.file.csv")
out("The string version of the data", explanation("string"))

add(file.exists)
doc("Returns True if the given path exists.")
source("plotext.file")
par("path", "Path to check", explanation("string"))
out("True if the path exists", explanation("bool"))

add(file.download)
doc("Downloads a URL to a local path.")
source("plotext.file")
par("url", "url path to download", explanation("string"))
par("path", "Local file path", explanation("string"))
past_par("log", "plotext.file.read")

add(file.delete)
doc("Deletes the file at the given path; nothing happens if the file does not exist, and a folder is never removed.")
source("plotext.file")
par("path", "Path to remove", explanation("string"))
par("safe", "only files inside the folder the program runs in can be removed; with False any file the program can reach can be, so never pass a path your program did not build itself", explanation("bool"), True)
past_par("log", "plotext.file.read")
