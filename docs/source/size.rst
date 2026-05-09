.. _size:

Size
====

By default, plotext sizes the plot to fit the full terminal area. Two methods let you override that behaviour.


Plot Size
---------

Use ``plot_size`` to set width and height explicitly, in units of terminal characters:

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   fig.plot_size(80, 25)
   fig.draw(fig.signal(plt.sin()).label("sine"))
   fig.show()


Limit Size
----------

By default the plot cannot grow beyond the terminal. To allow a larger plot (and let the terminal scroll), call :meth:`~plotext._kernel.terminal.terminal.limit` **before** ``plot_size``:

.. code-block:: python

   plt.terminal.limit(width = False, height = True)   # unlimited width, bounded height
   fig.plot_size(200, 25)                             # now width can exceed the terminal

:meth:`~plotext._kernel.terminal.terminal.limit` takes two booleans, one per dimension.

To undo the effect of :meth:`~plotext._kernel.terminal.terminal.limit` (and reset the cached terminal size and prompt height in one shot), call :meth:`~plotext._kernel.terminal.terminal.clear` on the terminal:

.. code-block:: python

   plt.terminal.clear()                               # restores default limit, prompt and size


Terminal Size
-------------

:meth:`~plotext._kernel.terminal.terminal.get_size` returns the current ``(width, height)`` of the terminal in characters — useful to size the plot relative to the current terminal window:

.. code-block:: python

   w, h = plt.terminal.get_size()
   fig.plot_size(w, h // 2)   # half-height plot
