Labels
======

Plot labels — title and axis labels — describe the content of your plot. They can be plain strings or :class:`plotext.colorize` objects.


Plot Title
----------

Use ``title`` to set the plot title:

.. code-block:: python

   import plotext as plt
   fig = plt.figure

   fig.title("Temperature Over Time")

The title accepts a colorized string as well:

.. code-block:: python

   fig.title(plt.colorize("Temperature Over Time", foreground = "cyan"))

.. note:: By default the title sits at the top centre. If the upper x-axis has its own label, the title shifts to the top left.


Axis Labels
-----------

Use ``label`` to set the x and y axis labels:

.. code-block:: python

   fig.label("Time (days)", axis = "x")
   fig.label("Amplitude",   axis = "y")

Like the title, each label accepts either a plain or colorized string.

See :ref:`axis` for how the ``axis`` and ``side`` parameters select a specific axis.
