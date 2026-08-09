Clear
=====

| A plot accumulates signals, settings, :ref:`pixels <pixel>`, styles and a possibly nested grid of :ref:`subplots <subplots>` over its lifetime.
| The clear methods take all of that, or just **one slice** of it, back to the defaults.
| They are grouped under the :class:`clear <plotext._plotter.clear.clear_class>` attribute of the figure, and of any :ref:`subplot <subplots>`.


Clear Everything
----------------

Calling the attribute itself as a method, as in ``plotext.figure.clear()``, resets the plot to an **empty state**: signals, settings, :ref:`pixels <pixel>`, styles and sizes all return to their defaults in one call.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

The :meth:`plotext.figure.clear.all() <plotext._plotter.clear.clear_class.all>` method does the same, the call form being a shortcut for it.


Granular Clears
---------------

Each granular method touches one slice of the plot state and leaves the rest untouched.

- :meth:`plotext.figure.clear.data() <plotext._plotter.clear.clear_class.data>`: drops the plotted data: every signal added via ``draw()``, the lines placed by the :meth:`line() <plotext._plotter.plot.plot_class.line>` and :meth:`event() <plotext._plotter.plot.plot_class.event>` methods, and their :ref:`legend <legend>` entries; the color :ref:`cycler <color_cycling>` resets, every color available again. Settings, :ref:`pixels <pixel>`, styles and sizes are *preserved*, ready for new data on the same configured plot.
- :meth:`plotext.figure.clear.settings() <plotext._plotter.clear.clear_class.settings>`: resets the plot settings back to defaults: the title, the :doc:`axis <axis>` labels, the limits, the :ref:`numerical ticks <ticks>` and their frequency, the scale, the alignments, the direction, the :doc:`date <date>` support, the :ref:`grid <grid>`, the frame visibility, and the :ref:`legend <legend>` visibility, position and alignment. Signals, :ref:`pixels <pixel>`, styles and sizes are *preserved*.
- :meth:`plotext.figure.clear.size() <plotext._plotter.clear.clear_class.size>`: drops any explicit :meth:`plot_size() <plotext._plotter.plot.plot_class.plot_size>` value and resets every :ref:`subplot <subplots>` size, so the next :meth:`plot_size() <plotext._plotter.plot.plot_class.plot_size>` call redistributes the space proportionally. On the master, the :doc:`terminal <terminal>` size is read again, in case the window was resized. Signals, :ref:`subplots <subplots>`, settings, :ref:`pixels <pixel>`, styles and the terminal own settings are *preserved*.
- :meth:`plotext.figure.clear.subplots() <plotext._plotter.clear.clear_class.subplots>`: wipes the :ref:`subplots <subplots>` grid configured on this plot, returning to a single panel layout. Signals, settings, :ref:`pixels <pixel>`, styles and size are *preserved*.
- :meth:`plotext.figure.clear.pixels() <plotext._plotter.clear.clear_class.pixels>`: resets every :ref:`pixel <pixel>` on the plot (labels, :doc:`rulers <ruler>`, :doc:`axes <axis>`, legend and the :doc:`canvas <canvas>` itself) to the package defaults, and rewinds the color cycler. Signals, settings, styles and sizes are *preserved*.
- :meth:`plotext.figure.clear.styles() <plotext._plotter.clear.clear_class.styles>`: resets the line styles of the :doc:`axes <axis>` and of the :ref:`grid <grid>` lines to *default*. Signals, settings, :ref:`pixels <pixel>` and sizes are *preserved*.

.. note:: Calling :meth:`plotext.figure.clear.pixels() <plotext._plotter.clear.clear_class.pixels>` is equivalent to applying the *default* :doc:`theme <theme>`: both take every color on the plot back to its package default.


Cascading
---------

| Every clear method cascades through the :ref:`subplots <subplots>` of the plot it is called on: a single :meth:`plotext.figure.clear.settings() <plotext._plotter.clear.clear_class.settings>` on the master figure resets the settings on the master and on every nested subplot.
| The same holds at any depth: called on a subplot that holds its own subplots, the method clears that whole branch, leaving the rest of the plot untouched.
| To clear a single :ref:`subplot <subplots>`, address it first, as in :meth:`plotext.figure.subplot(2, 1).clear.settings() <plotext._plotter.clear.clear_class.settings>`.

.. seealso:: The :doc:`terminal <terminal>` object holds its own pair of resets, :meth:`clean() <plotext._kernel.terminal.terminal.clean>` and :meth:`clear() <plotext._kernel.terminal.terminal.clear>`, described in the :ref:`terminal clearing <terminal_clearing>` section of its page.
