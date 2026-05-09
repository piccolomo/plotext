Clearing
========

A plot accumulates signals, layout settings, pixels, styles and a possibly nested grid of subplots over its lifetime. The clearing API lets you reset all of that, or just one slice of it, before reusing the same figure.

Every clearing method is available on ``plt.figure`` and on any subplot returned by ``fig.subplot(r, c)``. Calls cascade automatically through nested subplots, so clearing the master clears every descendant too.


Clear everything
----------------

:meth:`~plotext._plotter.plot.plot_class.clear` resets the plot to an empty state. It is the union of all the granular methods below — signals, settings, pixels, styles and sizes are all returned to defaults in one call.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()                         # the canonical "fresh figure" line

:meth:`clf() <plotext._plotter.plot.plot_class.clear>` is an alias for :meth:`~plotext._plotter.plot.plot_class.clear`.


Granular clears
---------------

Each granular method touches one slice of the plot's state and leaves the rest untouched. Use them when you want to keep, say, the layout while dropping the signals, or to swap colour schemes without losing the data.

- :meth:`~plotext._plotter.plot.plot_class.clear_data` (alias ``cld``) — drops every signal previously added via *draw* and removes the matching entries from the legend. Settings, pixels, styles and sizes are preserved, so you can replay a different dataset on the same configured plot.
- :meth:`~plotext._plotter.plot.plot_class.clear_settings` (alias ``cls``) — resets the plot's settings (title, axis labels, limits, frequencies, manual ticks, scale, alignment, direction, grid, frame status, legend status) back to defaults. Signals, pixels, styles and sizes are preserved.
- :meth:`~plotext._plotter.plot.plot_class.clear_size` (alias ``clz``) — drops any explicit *plot_size* value. On the master, the size reverts to the current terminal dimensions. Signals, subplots, settings, pixels and styles are preserved.
- :meth:`~plotext._plotter.plot.plot_class.clear_subplots` (alias ``clss``) — wipes the *subplots* grid configured on this plot, returning to a single-panel layout. Signals, settings, pixels, styles and size are preserved.
- :meth:`~plotext._plotter.plot.plot_class.clear_pixels` (alias ``clp``) — resets every pixel on the plot (labels, rulers, axes, legend and the canvas itself) to the package defaults, and rewinds the per-signal colour cycler. Signals, settings, styles and sizes are preserved, so this is the right knob for a colour-scheme reset.
- :meth:`~plotext._plotter.plot.plot_class.clear_styles` — resets ruler and axis line styles to *default*. Signals, settings, pixels and sizes are preserved.


Cascading
---------

When called on the master, every clearing method cascades through the entire subplot tree, so a single ``fig.clear_settings()`` resets settings on the master and every nested subplot in one shot. To clear only a specific subplot, address it first: ``fig.subplot(2, 1).clear_settings()``.


Terminal clearing
-----------------

The methods above act on a *plot's* internal state. The terminal object exposes its own pair of resets, reached through *plt.terminal* rather than *plt.figure*:

- :meth:`~plotext._kernel.terminal.terminal.clean` (alias ``clt``) — wipes printed output from the terminal screen. Pass an integer to remove a specific number of printed lines (plus the prompt height); call without arguments to clear the visible screen entirely. Useful when plotting a continuous stream of data. Note that, depending on the terminal shell used, a few extra lines may be printed after the plot.
- :meth:`~plotext._kernel.terminal.terminal.clear` — resets the terminal object's own state: prompt height, *limit* settings (see :doc:`size`) and the cached terminal size are all returned to defaults.

These are unrelated to the plot's signals or layout — calling :meth:`~plotext._kernel.terminal.terminal.clear` does not touch the figure, and calling :meth:`~plotext._plotter.plot.plot_class.clear` does not touch the terminal.
