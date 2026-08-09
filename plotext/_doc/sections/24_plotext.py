# Plotext components section: the file and prettydoc attributes (doc joins from the aggregator)

from plotext._doc.tools import *
from plotext._methods.file import file
from plotext import prettydoc


section('plotext components')


add(file, name = "file")
doc("Accesses the file toolkit. This is an attribute. Its methods build and check paths (join, parent, exists), read, write and delete text files (read, write, delete), turn tables to and from the csv form (csv, string) and download files from the web (download).")
source("plotext")
out("The file toolkit", explanation("file"))


add(prettydoc, name = "prettydoc")
doc("Accesses the prettydoc package, used by plotext to build its styled docstrings and available to document any other project. This is an attribute. It holds the docs manager (docs), the preview of its visual components (components) and its test suite (test). The whole plotext documentation, accessed by plotext.doc, is built with this package.")
source("plotext")
out("The prettydoc package", explanation("prettydoc"))
