File Operations
===============

plotext exposes a small set of file utilities under :mod:`plotext.file`. They cover path expansion, text I/O, existence checks, and parent/script-folder lookups — enough to read input data and write rendered plots without reaching for the full ``os.path`` module.

.. code-block:: python

   import plotext as plt
   plt.file.write("hello", "~/note.txt")     # ~ is expanded
   text = plt.file.read("~/note.txt")
   plt.file.exists("~/note.txt")             # True
   plt.file.delete("~/note.txt")

Saving a plot
-------------

Once a plot has been built into a matrix via ``fig.build()``, the matrix can be saved to disk via :meth:`~plotext._primitives.matrix.matrix.save`. The output format is selected by file extension:

* ``.html`` — rich HTML representation with embedded colors. Suitable for embedding in web pages or sharing as a self-contained document.
* ``.ansi`` — text preserving ANSI escape codes for colour. Suitable for tools that render ANSI (``less -R``, modern terminals, ansilove).
* anything else — plain colorless text.

.. code-block:: python

   m = fig.build()
   m.save("plot.html")    # HTML
   m.save("plot.ansi")    # coloured text
   m.save("plot.txt")     # plain text

Pass ``append=True`` to append to the file instead of overwriting it.

See :doc:`api` for the full reference of the methods exposed under :mod:`plotext.file`.
