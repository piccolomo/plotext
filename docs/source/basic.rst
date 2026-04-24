Basic Plots
===========

Scatter Plot
------------

To create a basic plot, build a signal with :func:`plotext.signal` and pass it to :func:`plotext.draw`:

.. code-block:: python

   import plotext as plt

   y = plt.sin()              # sinusoidal test signal
   signal = plt.signal(y)

   plt.draw(signal)
   plt.title("Scatter Plot")
   plt.show()

.. image:: https://raw.githubusercontent.com/piccolomo/plotext/master/data/scatter.png
   :alt: scatter

.. note:: The plot is built and rendered only when :func:`plotext.show` is called.

.. note:: More documentation is available via :code:`plotext.doc.signal()`.


Line Plot
---------

For a line plot, chain :meth:`.lines() <plotext._signal.signal.signal_class.lines>` onto the signal returned by :func:`plotext.signal`:

.. code-block:: python

   import plotext as plt

   y = plt.sin()
   signal = plt.signal(y).lines()

   plt.draw(signal)
   plt.title("Line Plot")
   plt.show()

.. image:: https://raw.githubusercontent.com/piccolomo/plotext/master/data/plot.png
   :alt: line plot

.. note::

   Plotext offers two line drawing methods:
      - ``simple`` (the default) — draws evenly-spaced points along the line, similar to ``linspace``. Light and fast, but may leave small gaps on steep segments.
      - ``full`` — fills every cell crossed by the line, producing a denser, visually continuous result.

   Switch with :meth:`~plotext._signal.signal.signal_class.line_method`, e.g. ``signal.line_method("full")``.


Stem Plot
---------

A *stem plot* draws a line from each data point down to an axis baseline (typically ``y = 0`` for a vertical stem, or ``x = 0`` for a horizontal one). It is useful for emphasising discrete values — impulse responses, sampled signals, simple bar-like displays — rather than a smooth curve.

In plotext, any signal becomes a stem plot by chaining :meth:`.fillx() <plotext._signal.signal.signal_class.fillx>` (vertical stems to the x axis) or :meth:`.filly() <plotext._signal.signal.signal_class.filly>` (horizontal stems to the y axis) onto it before drawing:

.. code-block:: python

   import plotext as plt

   y = plt.sin(length = 50)
   signal = plt.signal(y).fillx()

   plt.draw(signal)
   plt.title("Stem Plot")
   plt.show()

.. image:: images/stem.png
   :alt: stem


Elaborate Stem Plot
~~~~~~~~~~~~~~~~~~~

By default the stem baseline is the axis (``0``). For a varying baseline, build a second signal describing the fill level and pass it to the main signal's :meth:`.fill() <plotext._signal.signal.signal_class.fill>` method:

.. code-block:: python

   import plotext as plt

   l      = 1000
   y      = plt.sin(length = l, periods = 2)
   y_fill = plt.sin(length = l, periods = 2, amplitude = 0.3)

   signal = plt.signal(y)                                            # base stems
   fill   = plt.signal(y_fill, marker = plt.marker("hd", "blue+"))   # fill level

   signal.fill(fill)                                                 # link base and fill

   plt.draw(signal)
   plt.show()

.. image:: images/stem2.png
   :alt: elaborate stem plot

.. note:: The base signal and the fill signal should have the same number of points. If they differ, filling is applied only up to the shorter of the two.
