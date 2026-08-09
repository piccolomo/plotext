.. _size:

Size
====

| By default, |plotext| sizes the plot to **fit** the :doc:`terminal <terminal>` (minus the lines reserved for the prompt).
| Two methods let you override that behavior: :meth:`plot_size() <plotext._plotter.plot.plot_class.plot_size>`, which sets the plot size directly, and :meth:`plotext.terminal.limit() <plotext._kernel.terminal.terminal.limit>`, which allows a plot larger than the :doc:`terminal <terminal>`.


Plot Size
---------

Use :meth:`~plotext._plotter.plot.plot_class.plot_size` to set width and height explicitly, in :doc:`terminal <terminal>` characters:

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   fig.plot_size(80, 25)
   fig.draw(fig.signal(plt.sin()))
   fig.show()

Called with no arguments, it goes back to **automatic** sizing, where the plot takes the :doc:`terminal <terminal>` size.

:meth:`plot_size() <plotext._plotter.plot.plot_class.plot_size>` also carries the ``direction`` and ``policy`` parameters, which govern how sizes are resolved across subplots; see :doc:`subplots <subplot>` for those.

.. tip:: A :doc:`terminal <terminal>` character is normally about twice as tall as it is wide, the same ratio |plotext| assumes when fitting an image to the terminal. A plot meant to look square therefore needs roughly twice as many columns as rows, as in ``plotext.figure.plot_size(80, 40)``.


Limit Size
----------

| By default the plot cannot grow beyond the :doc:`terminal <terminal>`.
| To allow a larger plot (and let the terminal scroll), call :meth:`plotext.terminal.limit() <plotext._kernel.terminal.terminal.limit>` **before** :meth:`plotext.figure.plot_size() <plotext._plotter.plot.plot_class.plot_size>`, as the size is trimmed when it is set:

.. code-block:: python

   plt.terminal.limit(width = False, height = True)   # unlimited width, bounded height
   fig.plot_size(200, 25)                             # now width can exceed the terminal

| :meth:`plotext.terminal.limit() <plotext._kernel.terminal.terminal.limit>` takes two booleans, one for the width and one for the height.
| To undo its effect (and reset the last known terminal size and prompt height in one shot), call :meth:`plotext.terminal.clear() <plotext._kernel.terminal.terminal.clear>` on the :doc:`terminal <terminal>`:

.. code-block:: python

   plt.terminal.clear()                               # restores default limit, prompt and size
