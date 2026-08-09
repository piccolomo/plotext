.. _label:

Labels
======

| Plot labels, the **title** and the :doc:`axis <axis>` **labels**, describe the content of your plot.
| They can be plain strings, :ref:`colorize <colorize>` objects, or :ref:`matrix <matrix>` objects, as returned by :func:`plotext.effect` for an animated title.

.. caution:: Title and labels are painted on a single row, so a :class:`plotext.matrix` taller than one row, or a :ref:`colorized <colorize>` string containing a new line, is silently dropped.


Plot Title
----------

The title is set with :meth:`plotext.figure.title() <plotext._plotter.plot.plot_class.title>`, a method of the figure (and of any :ref:`subplot <subplots>`):

.. code-block:: python

   import plotext as plt
   fig = plt.figure

   fig.title("Temperature Over Time")

The title accepts a :ref:`colorized <colorize>` string as well:

.. code-block:: python

   fig.title(plt.colorize("Temperature Over Time", pixel = "cyan"))

Called with no argument, it **clears** the title.

.. note:: By default the title sits at the top center. If the upper *x* :doc:`axis <axis>` has its own label, the title shifts to the top left.


Axis Labels
-----------

Use :meth:`plotext.figure.label() <plotext._plotter.plot.plot_class.label>` to set the *x* and *y* :doc:`axis <axis>` labels:

.. code-block:: python

   fig.label("Time (days)", axis = "x")
   fig.label("Amplitude",   axis = "y")

| Like the title, each label accepts a plain string, a :class:`plotext.colorize` object or a :class:`plotext.matrix` object.
| Called with no argument, it clears the label of the selected :doc:`axis <axis>` and side.

.. note:: The *y* labels are drawn in the bottom row of the plot, at its corners: the left *y* label at the far left, the right *y* label at the far right, and the lower *x* label centered between them.

.. seealso:: See :ref:`axis selection <axis>` for how the ``axis`` and ``side`` parameters select a specific :doc:`axis <axis>`.
