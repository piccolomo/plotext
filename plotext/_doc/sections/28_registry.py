# Registry section: the store of strings shared by several docstrings

from plotext._doc.tools import *
from plotext import prettydoc


section('prettydoc registry')


add(prettydoc.registry)
doc("Initializes a registry: it keeps long strings under short names, so that a text needed in many docstrings is written once and asked for by name.\n"
    "A type explanation, a recurring message, a long sentence: store it with the add() method, then pass registry('name') wherever it is needed.")
source("plotext.prettydoc")
out("The initialized registry", explanation("registry"))

add(prettydoc.registry.add)
doc("Stores a string under a short name.\n"
    "For example, after add('celsius', 'a temperature in Celsius degrees'), registry('celsius') gives that sentence back.")
source("plotext.prettydoc.registry()")
par("name", "Name the string is stored under", explanation("string"))
par("doc", "The string to store", explanation("string"))
out("The registry itself", explanation("registry"))

add(prettydoc.registry.get)
doc("Gives the string stored under a name, or the given default when nothing is stored under it. Calling the registry with the name does the same, but complains when the name is missing.")
source("plotext.prettydoc.registry()")
past_par("name", "plotext.prettydoc.registry().add")
par("default", "Value given back when nothing is stored under that name", explanation("string"), None)
out("The string stored under the name", explanation("string"))
