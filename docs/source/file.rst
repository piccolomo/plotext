File Operations
===============

plotext exposes a small set of file utilities under :mod:`plotext.file`. They cover path expansion, text/CSV I/O, URL download, existence checks, and parent/script-folder lookups — enough to read input data and write rendered plots without reaching for the full ``os.path`` module.

.. code-block:: python

   import plotext as plt
   plt.file.write("hello", "~/note.txt")     # ~ is expanded
   text = plt.file.read("~/note.txt")
   plt.file.exists("~/note.txt")             # True
   plt.file.delete("~/note.txt")

Reading and writing tabular data
--------------------------------

:meth:`~plotext._methods.file.file.read` and :meth:`~plotext._methods.file.file.write` dispatch on the file extension. For ``.csv`` they use the stdlib :mod:`csv` module (so quoting, escaping and commas-in-values work correctly) and exchange a *list of rows* with the caller; for any other extension they exchange a string:

.. code-block:: python

   plt.file.write([["x", "y"], [1, 2.5], [3, 4.0]], "data.csv")    # list of rows → CSV
   rows = plt.file.read("data.csv")                                # → [['x', 'y'], ['1', '2.5'], ['3', '4.0']]

   plt.file.write("hello", "note.txt")                              # str → text file
   plt.file.read("note.txt")                                       # → "hello"


Downloading a URL
-----------------

:meth:`~plotext._methods.file.file.download` wraps ``urllib.request.urlretrieve`` for the one-line cases where you just want to grab a remote file to disk before plotting it:

.. code-block:: python

   plt.file.download("https://example.com/data.csv", "~/data.csv")
   rows = plt.file.read("~/data.csv")

Saving a plot
-------------

:meth:`~plotext._plotter.plot.plot_class.save` builds the figure and writes it to disk in one call. The output format is selected by file extension:

* ``.html`` — rich HTML representation with embedded colors. Suitable for embedding in web pages or sharing as a self-contained document.
* ``.ansi`` — text preserving ANSI escape codes for colour. Suitable for tools that render ANSI (``less -R``, modern terminals, ansilove).
* anything else — plain colorless text.

.. code-block:: python

   fig.save("plot.html")    # HTML
   fig.save("plot.ansi")    # coloured text
   fig.save("plot.txt")     # plain text

Pass ``append=True`` to append to the file instead of overwriting it.

If you already hold the rendered matrix (e.g. from ``fig.build()`` or from :func:`plotext.image`), use :meth:`~plotext._primitives.matrix.matrix.save` on the matrix directly — same extension-based dispatch:

.. code-block:: python

   m = fig.build()
   m.save("plot.html")

See :doc:`api` for the full reference of the methods exposed under :mod:`plotext.file`.
