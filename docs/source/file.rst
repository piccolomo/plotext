File Toolkit
============

| The :class:`plotext.file` object gathers a small set of **file utilities**: text reading and writing, csv table reading and writing, URL download, existence checks, deletion, and the path helpers :meth:`parent() <plotext._methods.file.file_class.parent>` and :meth:`join() <plotext._methods.file.file_class.join>`.

.. note:: Every reading and writing method takes a ``log`` parameter, printing a short report of the operation when ``True``.

File Management
---------------

The :meth:`exists(path) <plotext._methods.file.file_class.exists>` method tells whether a file or folder is present at the given path:

.. code-block:: python

   import plotext as plt
   plt.file.exists("~/note.txt")     # True or False

The :meth:`delete(path) <plotext._methods.file.file_class.delete>` method removes the file, doing nothing when there is none:

.. code-block:: python

   plt.file.delete("note.txt")                    # a file the program made, beside it
   plt.file.delete("~/note.txt", safe = False)    # anywhere else, saying so explicitly

.. caution:: The :meth:`delete() <plotext._methods.file.file_class.delete>` method removes files only: a folder is never removed.

.. caution:: Only files **inside the folder the program runs in** can be removed. Anything outside is refused, with a note saying so, unless you pass ``safe = False``, which lets any file the program can reach be removed, exactly as Python's own ``os.remove`` does. Never hand it a path your program did not build itself.

The :meth:`parent(path, level) <plotext._methods.file.file_class.parent>` method returns the folder containing the given path, ``level`` levels up (1 by default); with no path, it starts from the running script:

.. code-block:: python

   folder = plt.file.parent("~/data/note.txt")   # the data folder path

.. tip:: Called with no arguments, :meth:`parent() <plotext._methods.file.file_class.parent>` gives the folder of the running script, handy to reach data files stored next to it.

The :meth:`join(...) <plotext._methods.file.file_class.join>` method joins the given pieces into a single absolute path:

.. code-block:: python

   path = plt.file.join(folder, "other.txt")     # the other.txt path in the folder above

.. note:: Paths starting with ``~`` expand to the user home folder, in every method.


Text Files
----------

The :meth:`write(text, path) <plotext._methods.file.file_class.write>` method writes the given string to the file; with ``append = True``, it adds at the end instead of overwriting:

.. code-block:: python

   plt.file.write("hello", "~/note.txt")

The :meth:`read(path) <plotext._methods.file.file_class.read>` method returns the file content as a single string:

.. code-block:: python

   text = plt.file.read("~/note.txt")            # → "hello"


.. _tabular_data:

Tabular Data
------------

The :meth:`csv(path) <plotext._methods.file.file_class.csv>` method reads a csv file as a table: a list of rows, each a list of strings; the ``delimiter`` parameter, ``,`` by default, sets the column separator:

.. code-block:: python

   rows = plt.file.csv(plt.sample("stock"))      # the bundled stock sample table

.. caution:: Every cell comes back **as a string**: numerical columns need converting, as the :ref:`candlestick <candlestick>` example does with ``float()``.

The :meth:`string(rows) <plotext._methods.file.file_class.string>` method turns a list of rows into its csv text, ready for :meth:`write() <plotext._methods.file.file_class.write>`, with the same ``delimiter`` parameter:

.. code-block:: python

   plt.file.write(plt.file.string(rows), "stock.csv")

.. note:: The rows can hold any type, numbers included, all written as text.

.. note:: A few sample files, csv tables and media, are shipped with |plotext| and located by the :func:`sample() <plotext.sample>` function: see the :ref:`sample files <sample_files>` section.


URL Download
------------

The :meth:`download(url, path) <plotext._methods.file.file_class.download>` method saves a remote file to disk:

.. code-block:: python

   plt.file.download("https://example.com/data.csv", "~/data.csv")
   rows = plt.file.csv("~/data.csv")


Saving a Plot
-------------

To save a plot, call :meth:`build() <plotext._plotter.plot.plot_class.build>` on the figure, obtaining its rendered :ref:`matrix <matrix>`, then call :meth:`save() <plotext.matrix.save>` on it; the output format follows the file extension:

* ``.html``: an **HTML page**, with the plot colors embedded, ready for a browser
* ``.ansi``: text **keeping the color codes**, for tools that render them (like ``less -R`` in Linux terminals)
* anything else: plain **colorless** text

.. code-block:: python

   fig.build().save("plot.html")    # HTML
   fig.build().save("plot.ansi")    # colored text
   fig.build().save("plot.txt")     # plain text

| Pass ``append = True`` to append to the file instead of overwriting it.
| The ``colorless`` parameter overrides the extension default: ``True`` removes the colors, even from the ``.ansi`` and ``.html`` outputs, while ``False`` keeps them, even where they would normally be removed.

.. code-block:: python

   fig.build().save("plot.ansi", colorless = True)   # ANSI extension but plain text
   fig.build().save("plot.txt", colorless = False)   # .txt with ANSI escape codes inline


.. seealso:: The full method list is in the :ref:`file section <file_api>` of the :doc:`api <api>` page.

.. note:: More documentation for any of the methods is available via ``plotext.doc.file.<method>()`` (for example :meth:`plotext.doc.file.csv() <plotext._methods.file.file_class.csv>`).
