Inspection
==========

Plotext exposes a small set of helpers for poking at the live state of a plot or generating quick test data — useful when investigating layout problems, profiling renders, or just exercising the pipeline.


Test data
---------

Two synthetic-data generators are bundled for tests and examples:

- :func:`~plotext.sin` — sinusoidal samples, with optional ``phase``, ``decay`` and ``offset``.
- :func:`~plotext.square` — square wave alternating between ``+amplitude`` and ``-amplitude``.

Both share the same ``periods``, ``length`` and ``amplitude`` parameters and return a plain Python list of floats — drop-in input to :meth:`~plotext._plotter.plot.plot_class.signal`.

.. code-block:: python

   import plotext as plt

   fig = plt.figure
   fig.clear()
   fig.draw(fig.signal(plt.sin(periods = 4)).lines().label("sin"))
   fig.draw(fig.signal(plt.square(periods = 4)).lines().label("square"))
   fig.title("Test data generators")
   fig.legend()
   fig.show()


Timing
------

:meth:`~plotext._plotter.plot.plot_class.time` prints a timing report of the most recent ``show()`` / ``build()`` — total elapsed time and a per-step breakdown for each profiled section.

.. code-block:: python

   import plotext as plt

   fig = plt.figure
   fig.clear()
   fig.draw(fig.signal(plt.sin()).lines(True))
   fig.show()
   fig.time()                           # full report
   fig.time(full = False)               # total only

Pass ``full = False`` to print only the total.


Tree dumps
----------

- :meth:`~plotext._kernel.terminal.terminal.log` on ``plt.terminal`` prints the terminal, the master plot and every nested subplot.
- :meth:`~plotext._plotter.plot.plot_class.log` on any plot or subplot prints just that subtree.
- :meth:`~plotext._plotter.plot.plot_class.get_log` returns the same dump as a string, for capture or logging.
- :meth:`~plotext._signal.signal.signal_class.log` on a signal prints its points (pass ``full = True`` to include fill information).
