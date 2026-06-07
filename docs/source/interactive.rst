.. _interactive:

Interactive Mode
================

Normally the figure is rendered only when you call ``show``. :meth:`~plotext._plotter.plot.plot_class.interactive` flips that: while it is on, every figure-mutating call reprints the whole figure immediately, so each change appears without an explicit ``show`` — the same convenience as matplotlib's ``plt.ion()``. It is handy at a REPL when building a plot up step by step.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   fig.interactive()                       # turn interactive mode on

   fig.draw(fig.signal(plt.sin()))         # each of these reprints the figure
   fig.title("Interactive")
   fig.theme("dark")

   fig.interactive(False)                  # back to manual show()

What triggers a reprint:

- **Mutating calls** — ``draw``, ``line``, ``event`` and every setter (``title``, ``label``, ``lim``, ``scale``, ``grid``, ``theme``, ``canvas_pixel``, ``subplots``, the ``clear`` family, …) reprint once they complete. A single call reprints exactly once, even when it cascades internally (``clear`` calls several sub-clears) or propagates across subplots.
- **Builders** — ``bar``, ``box``, ``signal``, ``rectangle`` and the like only *return* a drawable; they reprint when their result is passed to ``draw``, which is the moment the content actually lands on the figure.

.. note:: Interactive mode is a session toggle, not a plot setting: it persists across ``clear`` and is switched off only by ``interactive(False)``. Enabling it is silent — the next mutating call produces the first reprint.
