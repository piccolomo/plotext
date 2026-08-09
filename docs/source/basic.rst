Basic Plots
===========

.. _scatter:

Scatter Plot
------------

To create a basic **scatter plot**, build a :ref:`signal <signal>` with the
:meth:`~plotext._plotter.plot.plot_class.signal` method and pass it to
:meth:`~plotext._plotter.plot.plot_class.draw` on the master figure:

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   y = plt.sin()                     # sinusoidal test signal
   signal = fig.signal(y)

   fig.draw(signal)
   fig.title("Scatter Plot")
   fig.show()

Or directly from the shell:

.. code-block:: shell

   plotext --figure --sin --signal --draw --title 'Scatter Plot' --show

.. image:: images/scatter.png
   :alt: scatter

.. important:: The plot is built and rendered *only* when :meth:`show() <plotext._plotter.plot.plot_class.show>` is called.

.. note:: The ``marker`` parameter of :meth:`signal() <plotext._plotter.plot.plot_class.signal>` sets the symbol drawn at each data point, the higher resolution code ``hd`` by default, ``dot`` on Windows: see the :doc:`marker <marker>` page for all the accepted forms.

.. note:: The ``xside`` and ``yside`` parameters of :meth:`signal() <plotext._plotter.plot.plot_class.signal>` pick which *x* and *y* axis the signal is plotted against: see :ref:`axis selection <axis>`.

.. note:: More documentation is available via ``plotext.doc.signal()``, ``plotext.doc.draw()`` and ``plotext.doc.show()``.

.. tip:: To display the plot dynamically as you build it, without calling :meth:`show() <plotext._plotter.plot.plot_class.show>` each time, turn on :ref:`interactive mode <interactive>`, every mutating call then reprints the figure immediately, `matplotlib <https://matplotlib.org/>`_-style.


.. _line:

Line Plot
---------

For a line plot, chain :meth:`lines() <plotext._signal.signal.signal_class.lines>` onto a signal: it connects **every point** and switches the signal from a scatter into a continuous line:

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   y = plt.sin()
   signal = fig.signal(y).lines()

   fig.draw(signal)
   fig.title("Line Plot")
   fig.show()

Or directly from the shell:

.. code-block:: shell

   plotext --figure --sin --signal --lines --draw --title 'Line Plot' --show

.. image:: images/line.png
   :alt: line plot

.. note::

   :meth:`lines() <plotext._signal.signal.signal_class.lines>` toggles every segment uniformly. To turn a single segment on or off without touching the rest, use :meth:`line() <plotext._signal.signal.signal_class.line>`, which controls the line connecting a point to the previous one.

.. _stem:

Stem Plot
---------

A *stem plot* draws a line from each data point down to an :doc:`axis <axis>` **baseline** (typically ``y = 0`` for a vertical stem, or ``x = 0`` for a horizontal one). It is useful for emphasizing discrete values, impulse responses, sampled signals, simple bar-like displays, rather than a smooth curve.

In |plotext|, any signal becomes a stem plot by chaining :meth:`fillx() <plotext._signal.signal.signal_class.fillx>` (for vertical stems, reaching the *x* :doc:`axis <axis>`) or :meth:`filly() <plotext._signal.signal.signal_class.filly>` (for horizontal stems, reaching the *y* axis) onto it before drawing:

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   y = plt.sin(length = 50)
   signal = fig.signal(y).fillx()

   fig.draw(signal)
   fig.title("Stem Plot")
   fig.show()

Or directly from the shell:

.. code-block:: shell

   plotext --figure --sin length=50 --signal --fillx --draw --title 'Stem Plot' --show

.. image:: images/stem.png
   :alt: stem

.. _stem2:

Elaborate Stem Plot
~~~~~~~~~~~~~~~~~~~

By default each stem ends on the :doc:`axis <axis>`, at constant value 0. To make the stems end on a **varying level** instead, build a second signal describing that level and pass it to the main signal's :meth:`fill() <plotext._signal.signal.signal_class.fill>` method:

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   l      = 1000
   y      = plt.sin(length = l, periods = 2)
   y_fill = plt.sin(length = l, periods = 2, amplitude = 0.3)

   signal = fig.signal(y)                                            # base stems
   fill   = fig.signal(y_fill, marker = plt.marker("hd", pixel="blue+"))   # fill level

   signal.fill(fill)                                                 # link base and fill

   fig.draw(signal)
   fig.show()

.. image:: images/stem2.png
   :alt: elaborate stem plot

.. caution:: The base signal and the fill signal should have the same number of points. If they differ, filling is applied only up to the shorter of the two.

.. tip:: The fill signal above is colored through a :ref:`marker object <marker_objects>`, a symbol carrying its own :ref:`pixel <pixel_forms>`, the object holding a foreground color, a background color and a style.

.. note:: No chain equivalent: this example links two signals, while the
   :doc:`Command line <cli>` chain syntax builds one signal at a time. From the shell, use
   ``python3 -c "<code>"`` instead.
