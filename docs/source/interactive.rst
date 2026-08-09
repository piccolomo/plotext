.. _interactive:

Interactive Mode
================

| Normally the figure is rendered only when you call :meth:`show() <plotext._plotter.plot.plot_class.show>`.
| The :meth:`interactive() <plotext._plotter.plot.plot_class.interactive>` method flips that: while it is on, every figure-mutating call reprints the whole figure *immediately*, so each change appears without an explicit :meth:`show() <plotext._plotter.plot.plot_class.show>` call.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   fig.interactive()                       # turn interactive mode on

   fig.draw(fig.signal(plt.sin()))         # each of these reprints the figure
   fig.title("Interactive")
   fig.theme("dark")

   fig.interactive(False)                  # back to manual show()

.. note:: This is the same convenience as `matplotlib <https://matplotlib.org/>`_'s ``plt.ion()``: handy at the interactive Python prompt, when building a plot up step by step.

What triggers a reprint:

- Every method changing the figure reprints it once complete: :meth:`draw() <plotext._plotter.plot.plot_class.draw>`, :meth:`line() <plotext._plotter.plot.plot_class.line>`, :meth:`event() <plotext._plotter.plot.plot_class.event>`, and every setting method, like :meth:`title() <plotext._plotter.plot.plot_class.title>`, :meth:`theme() <plotext._plotter.plot.plot_class.theme>`, :meth:`ruler().lim() <plotext._plotter.frame.ruler.ruler_class.lim>` or the :doc:`clear <clear>` family.
- A single call reprints exactly **once**, even when it acts on several settings internally, like :meth:`clear() <plotext._plotter.clear.clear_class.all>`, or reaches several :ref:`subplots <subplots>` at once.
- The signal creating methods, like :meth:`signal() <plotext._plotter.plot.plot_class.signal>` or :meth:`bar() <plotext._plotter.plot.plot_class.bar>`, only return their signal, leaving the figure *untouched*: the reprint comes when the signal is passed to :meth:`draw() <plotext._plotter.plot.plot_class.draw>`, the moment the content actually lands on the figure.

.. important:: Interactive mode is a session toggle, not a plot setting: it persists across :meth:`clear() <plotext._plotter.clear.clear_class.all>` and is switched off only by :meth:`interactive(False) <plotext._plotter.plot.plot_class.interactive>`. Enabling it is silent, the next figure-changing call produces the first reprint.
