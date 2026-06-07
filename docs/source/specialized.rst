Specialized Plots
=================

Plot types that don't fit the basic line/scatter/bar mould — error bars, event plots, and confusion matrices. See :doc:`image` for heatmap and image-style plots.


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


.. _confusion_matrix:

Confusion Matrix
----------------

:meth:`~plotext._plotter.plot.plot_class.confusion_matrix` cross-tabulates per-sample ``actual`` and ``predicted`` labels and renders the result as a square grid of gradient-coloured rectangles. Each cell carries its count (or, with ``norm = True``, the row-normalized percentage) as a centered label whose colour adapts automatically to the cell's fill. The returned signal is composite (one rectangle per cell) — pass it to :meth:`~plotext._plotter.plot.plot_class.draw`. Tick labels, axis labels and title are the caller's responsibility (so any label scheme works).

.. code-block:: python

   import plotext as plt
   from plotext._methods.sequence import _crosstab

   actual    = ['cat','dog','cat','dog','cat','bird','bird','dog','cat','bird']
   predicted = ['cat','dog','dog','dog','cat','bird','cat', 'dog','dog','bird']

   labels, _ = _crosstab(actual, predicted)
   n = len(labels)

   fig = plt.figure
   fig.clear()
   fig.plot_size(60, 30)
   fig.draw(fig.confusion_matrix(actual, predicted, norm = True, map = 'viridis'))
   fig.ticks(list(range(n)), labels = labels,       axis = "x")
   fig.ticks(list(range(n)), labels = labels[::-1], axis = "y")
   fig.label("Predicted", axis = "x")
   fig.label("Actual",    axis = "y")
   fig.title("Confusion Matrix")
   fig.show()

Parameters:

- ``actual`` / ``predicted`` — per-sample true and predicted labels (same length).
- ``labels`` — optional explicit label order; if omitted, the unique labels from ``actual ∪ predicted`` are sorted.
- ``norm`` — when ``True``, cell labels show row-normalized percentages (each row sums to 100%); when ``False`` (default), labels show raw counts. Cell colours always use raw counts so the gradient stays meaningful regardless.
- ``map`` — colormap name applied to the count grid (defaults to ``"gray"``; ``"viridis"`` reads well on most terminals).

.. note:: More documentation is available via :code:`plotext.doc.confusion_matrix()`.


.. _indicator:

Indicator (single-value KPI)
----------------------------

A "big-number" indicator — a single value with a title and optional trend arrow, inside a clean framed box — can be built from existing primitives without a dedicated method:

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   value, label, trend = 123, "Active Users", +5

   parts = plt.colorize(str(value), foreground = 'orange+', style = 'bold')
   if trend is not None:
       arrow       = '↑' if trend > 0 else '↓' if trend < 0 else '↔'
       arrow_color = 'green' if trend > 0 else 'red' if trend < 0 else 'orange'
       parts = parts.hstack(plt.colorize(' ' + arrow, foreground = arrow_color, style = 'bold'))

   fig.frequency(0, axis = 'x'); fig.frequency(0, axis = 'y')   # hide ticks (frame stays for the boxed look)
   fig.lim(0, 1, axis = 'x'); fig.lim(0, 1, axis = 'y')   # fix the canvas extent
   fig.title(label)
   fig.draw(fig.text(0.5, 0.5, parts, alignment = 'center'))
   fig.show()

Wrap this in a helper function if you display many indicators in a dashboard layout (each one in its own :ref:`subplot <subplots>`).


Command-line
------------

Error bars and confusion matrix translate directly; the event plot is a config call (it registers stems on the rulers and doesn't return a drawable). The indicator recipe is intentionally skipped — it's a multi-step composition of ``colorize`` / ``hstack`` / ``frequency`` / ``lim`` / ``text`` that's cleaner to keep in Python.

.. code-block:: shell

   # Error bars: error(x, y, yerr, xerr); all positional
   plotext --error '[0,1,2,3,4]' '[0.0, 0.84, 0.91, 0.14, -0.76]' \
                   '[0.1, 0.2, 0.15, 0.3, 0.2]' '[0.1, 0.15, 0.2, 0.1, 0.25]' \
           --label sin --draw \
           --title 'Error Plot' --legend --show

   # Event plot: stems registered on the ruler, no drawable to --draw
   plotext --event '[2.3, 5.7, 8.1, 9.4, 12.6, 15.2, 18.7, 20.5, 22.8]' label=events \
           --title 'Event Plot' --label hour axis=x --legend --show

   # Confusion matrix
   plotext --confusion-matrix \
           '["cat","dog","cat","dog","cat","bird","bird","dog","cat","bird"]' \
           '["cat","dog","dog","dog","cat","bird","cat","dog","dog","bird"]' \
           norm=true map=viridis --draw \
           --title 'Confusion Matrix' --show

For longer event series, drop in ``@path:your.csv:1`` (a single-column CSV) instead of the literal list.
