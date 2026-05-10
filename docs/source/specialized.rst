Specialized Plots
=================

Plot types that don't fit the basic line/scatter/bar mould — error bars, event plots, and (in future) confusion matrices. See :doc:`image` for heatmap and image-style plots.


Error Bars
----------

:meth:`~plotext._plotter.plot.plot_class.error` plots a scatter point at every ``(x, y)`` and surrounds it with horizontal and/or vertical error bars centred on the point. The error sequences are positional (yerr first, matching :func:`matplotlib.pyplot.errorbar`'s ordering): ``error(y)``, ``error(x, y)``, ``error(x, y, yerr)`` or ``error(x, y, yerr, xerr)``. Each error sequence may be a scalar (broadcast to every point) or a per-point list. Like every other drawable, the result is a single signal — pass it to :meth:`~plotext._plotter.plot.plot_class.draw`.

.. code-block:: python

   import random
   import plotext as plt

   random.seed(0)
   fig = plt.figure
   fig.clear()

   l = 20
   x  = list(range(l))
   y  = plt.sin(length = l)
   ye = [random.random() for _ in range(l)]
   xe = [random.random() for _ in range(l)]

   fig.draw(fig.error(x, y, ye, xe).label("sin"))
   fig.title("Error Plot")
   fig.legend()
   fig.show()

Parameters:

- ``args`` — input data; positional sequences are interpreted as ``y`` / ``(x, y)`` / ``(x, y, yerr)`` / ``(x, y, yerr, xerr)``. Errors may be scalar or per-point.
- ``pixel`` — colour and styling for every stroke of the error bars; if omitted, a fresh colour is taken from the cycler.
- ``style`` — line-drawing style applied to the bars (*default*, *double*, *heavy*, *dotted*, *rounded*).
- ``xside``, ``yside`` — which axis pair the points are anchored to (see :ref:`axis`).
- ``label`` — legend label for the error series.

.. note:: More documentation is available via :code:`plotext.doc.error()`.


Event Plot
----------

:meth:`~plotext._plotter.plot.plot_class.event` draws a stem at every event coordinate — useful for marking the timing of discrete occurrences (spike trains, request timestamps, alert times, …). Each stem is a ruler-registered line (``│`` for vertical orientation, ``─`` for horizontal) that spans the full canvas and merges with the axes (``┼`` / ``┴`` / ``┬`` on the axis cells where stems hit). The perpendicular axis is squashed to ``[0, 1]`` and its ticks removed since it carries no data.

Unlike most plot methods, ``event`` does not return a signal — the stems are registered directly on the rulers, so there's nothing to pass to :meth:`~plotext._plotter.plot.plot_class.draw`. Use the ``label`` keyword to add a single legend entry for the whole event series.

.. code-block:: python

   import random
   import plotext as plt

   random.seed(0)
   fig = plt.figure
   fig.clear()

   events = sorted(random.uniform(0, 24) for _ in range(60))   # 60 events across a 24-hour day
   fig.event(events, label = "events")

   fig.title("Event Plot")
   fig.label("hour", axis = "x")
   fig.legend()
   fig.show()

Parameters:

- ``data`` — sequence of event coordinates along the chosen orientation.
- ``orientation`` — *vertical* (events along x) or *horizontal* (events along y); short *v* / *h* / *0* / *1* also accepted.
- ``pixel`` — colour and styling for every stem; if omitted, a fresh colour is taken from the cycler.
- ``style`` — line-drawing style for the stems (*default*, *double*, *heavy*, *dotted*, *rounded*).
- ``side`` — which axis side the events are anchored to (xside if vertical, yside if horizontal).
- ``label`` — legend label for the event series (carried by the first stem only, so the legend stays a single entry).

.. note::

   ``event`` mutates the figure's ``lim`` and ``frequency`` on the perpendicular axis as a side-effect — that's how the ``[0, 1]`` strip and the hidden ticks are achieved. If you want to overlay events on top of an existing plot without disturbing its limits, drive the equivalent vertical / horizontal lines yourself via :meth:`~plotext._plotter.plot.plot_class.line` per event.

.. note:: More documentation is available via :code:`plotext.doc.event()`.
