Canvas
======

The *canvas* is the rectangular area inside the frame where signals, gridlines and the legend are drawn. Three methods directly control its appearance: ``canvas_pixel`` for the canvas background, ``legend`` for the floating legend that sits on top of it, and ``grid`` for gridlines spanning the canvas.


Canvas pixel
------------

``canvas_pixel`` sets the foreground colour, background colour and style of the canvas itself — the empty cells inside the plot area, before any signal is drawn on top. Pass a :class:`plotext.pixel` (see :ref:`pixel`).

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   y = plt.sin()
   fig.draw(fig.signal(y))

   fig.canvas_pixel(plt.pixel(background = "black"))

   fig.title("Black canvas")
   fig.show()


Legend
------

``legend`` configures the floating legend that lists each drawn signal alongside its marker. By default plots render without a legend; calling ``legend()`` with no arguments turns it on.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   y = plt.sin()
   fig.draw(fig.signal(y).label("sine"))
   fig.draw(fig.signal(plt.sin(phase = 0.5)).label("sine + π/2"))

   fig.legend()

   fig.title("Plot with legend")
   fig.show()

Parameters:

- ``status`` — turns the legend on or off. The default is *on*, so any call to *legend* with no arguments simply makes it appear; pass *false* to hide it without removing the rest of the configuration you have set.
- ``x`` and ``y`` — coordinates of the legend's anchor point on the canvas. By default they are read in the same units as your data, so you can place the legend at, for instance, *x* equal to a tick value and *y* near the top of the visible range. The value of *relative* below changes how these numbers are interpreted.
- ``relative`` — when *true*, *x* and *y* are no longer in data units but in fractions of the canvas going from *zero* at the lower-left corner to *one* at the upper-right. This is convenient when you want the legend pinned to a corner regardless of the data limits, for example a top-right legend at *0.95* and *0.95*.
- ``ha`` — horizontal alignment of the legend block around its anchor point. Choose *left* to have the anchor be the legend's left edge, *center* to have it be the midpoint, or *right* to have it be the right edge. Short forms *l*, *c*, *r* and the integers *-1*, *0*, *1* mean the same thing.
- ``va`` — vertical alignment of the legend block around its anchor point. Choose *top*, *center* or *bottom* (short *t*, *c*, *b*; or *-1*, *0*, *1*) depending on whether the anchor sits at the top edge, the middle, or the bottom edge of the legend.
- ``xside`` — selects which horizontal axis the *x* coordinate is read against. By default it is the *lower* axis; set it to *upper* if you want the legend positioned relative to a signal that lives on the upper x axis. The integers *0* and *1* are also accepted.
- ``yside`` — same idea for the vertical axis: the default is *left*, set it to *right* if the legend should be positioned relative to a signal on the right y axis.
- ``pixel`` — colour and style applied to the legend text and frame. Pass a *plotext pixel* (see :ref:`pixel`). Note that any colour baked into an individual signal's label via *plotext.colorize* is preserved — only the legend's own decoration is affected.

.. note:: Signals without an explicit *label* call still appear in the legend under an auto-generated name like *signal[N]* where *N* is the signal's index in the plot's draw queue.


Grid
----

``grid`` controls the visibility and appearance of grid lines. The lines run inside the canvas and are aligned with the numerical ticks defined by the rulers, giving visual guidance when reading values.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   y = plt.sin()
   fig.draw(fig.signal(y))

   fig.grid(style = "double",                         # double cyan vertical grid lines
            pixel = plt.pixel(foreground = "cyan"),
            axis = "x")

   fig.title("Grid")
   fig.show()

Parameters:

- ``active`` — turns the grid on or off. The default is *on*, so calling *grid* with no arguments simply makes the lines appear; pass *false* to hide them while keeping the rest of the configuration intact.
- ``style`` — appearance of each grid line. The *default* style draws a single solid line, while *double* draws a doubled solid line that stands out more on dense plots.
- ``pixel`` — colour and style of the grid lines themselves. Pass a *plotext pixel* (see :ref:`pixel`); *foreground* sets the line colour, *background* harmonises with the canvas, and *style* can apply emphases such as *bold* or *dim*.
- ``axis`` and ``side`` — restrict the grid to a specific axis or side. By default the grid is drawn for both axes and both sides; pass these to limit it, for example to vertical lines only or to ticks on a single side. See :ref:`axis` for the accepted values.
