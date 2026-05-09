Inspection
==========

Plotext exposes a small set of helpers for poking at the live state of a plot — useful when investigating layout problems or render performance.


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
