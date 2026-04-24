Rulers
======

The *ruler* defines the area of the plot where numerical ticks appear along each axis. Each of the functions below can be applied independently to any axis; see :ref:`axis` for how to target a specific axis.


Limits
------

:func:`plotext.lim` sets the visible numerical range of an axis via the ``lower`` and ``upper`` parameters. Only data values within the given range are drawn — values outside it are dropped silently. Limits affect display only; the underlying data is untouched.

Limits can be given as numeric values or as date strings, depending on the data.

.. code-block:: python

   import plotext as plt

   y = plt.sin()
   signal = plt.signal(y)
   plt.draw(signal)

   plt.lim(50, 150,   axis = "x")    # show only x in [50, 150]
   plt.lim(-0.5, 0.5, axis = "y")    # and y in [-0.5, 0.5]

   plt.title("Limits")
   plt.show()


Ticks
-----

Plotext gives full control over the **placement and appearance of numerical ticks** on both axes. Ticks are managed by two functions: :func:`plotext.frequency` for automatic placement, and :func:`plotext.ticks` for manual placement.


Automatic placement
~~~~~~~~~~~~~~~~~~~

:func:`plotext.frequency` sets the number of ticks to display along an axis. Plotext distributes them evenly across the current axis range.

.. code-block:: python

   import plotext as plt

   y = plt.sin()
   signal = plt.signal(y)
   plt.draw(signal)

   plt.frequency(3, axis = "y")

   plt.title("Frequency Method")
   plt.show()


Manual placement
~~~~~~~~~~~~~~~~

Use :func:`plotext.ticks` when you need full control over tick positions and labels. This is useful when ticks must appear at specific meaningful values (e.g. multiples of π), when values are non-uniformly spaced, or when custom text labels are required instead of numeric values.

.. code-block:: python

   import plotext as plt

   y = plt.sin()
   signal = plt.signal(y)
   plt.draw(signal)

   plt.ticks(positions = [-1, 0, 1],
             labels = ["minimum", "center", "maximum"],
             axis = "y")

   plt.title("Scatter Plot with Manual Tick Placement")
   plt.show()


.. note:: Tick positions may be numeric values; dates, timestamps and datetime objects are also accepted when a date plot is active (see :doc:`date`). Tick labels may be plain strings or :class:`plotext.colorize` objects (see :doc:`colorize`).

.. note:: :func:`plotext.ticks` takes precedence over :func:`plotext.frequency` on the same axis.


Scale
-----

:func:`plotext.scale` controls how data values are mapped to positions on an axis. By default axes use a linear scale — equal differences in data correspond to equal distances on the axis. With a logarithmic scale, equal distances on the axis correspond to equal ratios between values instead.

.. note::

   A log scale is useful when data spans several orders of magnitude or grows exponentially. Multiplicative changes (e.g. doubling or halving) appear as equal distances on the axis, revealing relative growth that may be hidden on a linear scale.

The example below draws a sinusoidal signal on a logarithmic x axis, using :func:`plotext.scale` to switch the x scale, :func:`plotext.frequency` to set the tick count, and :func:`plotext.grid` to add vertical gridlines:

.. code-block:: python

   import plotext as plt

   l = 10 ** 4
   y = plt.sin(periods = 2, length = l)
   signal = plt.signal(y).lines()
   plt.draw(signal)

   plt.scale("log", axis = "x")
   plt.frequency(5, axis = "x")
   plt.frequency(7, axis = "y")

   plt.grid(axis = "x")

   plt.title("Logarithmic Plot")
   plt.label("x", "logarithmic scale")
   plt.label("y", "linear scale")

   plt.show()

.. image:: https://raw.githubusercontent.com/piccolomo/plotext/master/data/log.png
   :alt: log

.. note:: The logarithm used is ``log10``.


Grid
----

:func:`plotext.grid` controls the visibility and appearance of grid lines. The lines run inside the plot canvas and are aligned with the numerical ticks defined by the rulers, giving visual guidance when reading values.

The ``active`` parameter (bool, default ``True``) toggles the grid on or off; the ``pixel`` parameter controls the colour (see :ref:`pixel`). Grids can be applied selectively to a specific axis and side, supporting full or single-axis grids.

The ``style`` parameter is a string accepting one of two values:

- ``default`` — single solid line (the default)
- ``double`` — double solid line

.. code-block:: python

   import plotext as plt

   y = plt.sin()
   signal = plt.signal(y)
   plt.draw(signal)

   plt.grid(style = "double",                         # double cyan vertical grid lines
            pixel = plt.pixel(foreground = "cyan"),
            axis = "x")

   plt.title("Grid")
   plt.show()


Direction
---------

:func:`plotext.direction` controls **in which direction values increase along an axis**. It changes the visual orientation but **does not modify the data**. The parameter takes ``+1`` (default: values grow left-to-right on x and bottom-to-top on y) or ``-1`` (reversed).


Alignment
---------

When a plot is rendered with a fixed number of bins, each numerical value must be mapped to one of them. The :func:`plotext.alignment` function controls how the axis numerical limits (the minimum and maximum values) are placed within the first and last bins.

With ``center`` alignment the limits sit at the centre of the outermost bins, producing a symmetrical layout. With ``edge`` alignment they sit at the outer boundary of those bins, flush against the plot edge.

.. image:: images/alignment.png
   :alt: alignment
   :width: 400px
   :align: center

In the two plots above, the top uses centre alignment on both axes and the bottom uses edge alignment. In both cases the first and last markers occupy the same characters on the canvas; only their position within those characters differs.
