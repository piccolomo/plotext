Shapes
======

``plotext`` provides three primitives for drawing arbitrary geometric shapes onto the canvas: :meth:`~plotext._plotter.plot.plot_class.segment` for two-point lines, :meth:`~plotext._plotter.plot.plot_class.rectangle` for axis-aligned rectangles and :meth:`~plotext._plotter.plot.plot_class.polygon` for regular polygons (triangle, square, pentagon, hexagon, … up to a near-circle at high side counts).

Both methods follow the same pattern as :doc:`basic` plots — they return a signal that the caller passes to :meth:`~plotext._plotter.plot.plot_class.draw`.


Rectangle
---------

:meth:`~plotext._plotter.plot.plot_class.rectangle` builds a filled or outlined rectangle between two x and y ranges.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   fig.draw(fig.rectangle((0, 10), (0, 5)).label("filled"))
   fig.draw(fig.rectangle((12, 22), (0, 5), label = "labelled"))
   fig.title("Rectangle")
   fig.show()

Parameters:

- ``x`` — the x range of the rectangle, as a two-value tuple or list. Endpoint order doesn't matter; *min* and *max* are taken internally.
- ``y`` — the y range of the rectangle, same format as *x*.
- ``marker`` — the symbol used to render the rectangle. Pass a single character or a *plotext marker* (see :ref:`markers`).
- ``lines`` — when *true* (default), the rectangle outline is densified so the border draws cleanly (and the body fills, when fill is also true). When *false*, only the corner points are placed.
- ``fill`` — when *true* (default), the rectangle's body is filled with markers. When *false*, only the clockwise outline is drawn.
- ``label`` — optional text drawn centered inside the rectangle. Colours adapt to the rectangle automatically: when filled, the label is painted in the canvas background colour over the rectangle's foreground; when only outlined, the label takes the rectangle's foreground colour. Accepts a plain string, a :class:`~plotext.colorize` for explicit per-character styling, or a :class:`~plotext.matrix` for full pixel control.
- ``xside``, ``yside`` — which axis pair the rectangle is plotted against (see :ref:`axis`).

.. note::

   When the rectangle is drawn with a sub-cell marker (``"hd"``, ``"fhd"``, ``"braille"``) and the rectangle's edges don't land on integer cell boundaries, a half-cell canvas-coloured gap can appear immediately next to a label. This is rendering-correct — sub-cell edge glyphs like ``▌``/``▐`` split a cell into bar-colour and canvas-colour halves, and labels are full-cell, so the visual contrast surfaces the half-block's canvas side as a "white gap". To eliminate it, use a full-cell marker (``"full"``) or snap rectangle x-ranges to integer values.


Polygon
-------

:meth:`~plotext._plotter.plot.plot_class.polygon` builds a regular polygon centered at a point, with a configurable number of sides and radius.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   fig.draw(fig.polygon(sides=6).label("hexagon"))
   fig.draw(fig.polygon(sides=100, radius=0.5).label("circle"))
   fig.title("Polygons")
   fig.show()

Parameters:

- ``x``, ``y`` — coordinates of the polygon center.
- ``radius`` — distance from the center to each vertex. For a polygon with very many sides this is the effective circle radius.
- ``sides`` — number of polygon sides. Triangle is *3*, square is *4*, hexagon is *6*; values above ~50 approximate a circle.
- ``up`` — when *true*, rotates the polygon by half a side angle. For even-sided polygons this puts a flat edge on top; for odd-sided ones it puts a vertex on top.
- ``marker`` — symbol used for the vertices.
- ``lines`` — when *true* (default), the polygon outline is drawn between consecutive vertices. When *false*, only the vertex points are placed.
- ``fill`` — when *true*, every vertex gets a fill point at *(x, y)* — the polygon center, producing radial spokes from each vertex inward.
- ``xside``, ``yside`` — which axis pair the polygon is plotted against.


Segment
-------

:meth:`~plotext._plotter.plot.plot_class.segment` builds a straight line between two points — useful for arbitrary diagonals or axis-aligned segments without going through ``signal()`` and configuring lines manually.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   fig.draw(fig.segment((0, 10), (0, 5)).label("diagonal"))
   fig.draw(fig.segment((0, 10), (5, 5)).label("horizontal"))
   fig.title("Segment")
   fig.show()

Parameters:

- ``x`` — the x range of the segment, as a two-value tuple or list. Endpoint order matters (the line goes from the first to the second).
- ``y`` — the y range of the segment, same format as *x*.
- ``marker`` — symbol used to render the segment.
- ``xside``, ``yside`` — which axis pair the segment is plotted against.


Combining shapes
----------------

Shapes can be drawn into the same plot by issuing multiple draw calls; each shape becomes its own legend entry if labeled.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   fig.draw(fig.polygon().label("triangle"))
   fig.draw(fig.rectangle().label("rectangle"))
   fig.draw(fig.polygon(sides=100).label("circle"))

   fig.title("Shapes")
   fig.legend()
   fig.show()


Command-line
------------

All three shape primitives translate directly. Tuples on the shell need quoting (parentheses are shell metacharacters):

.. code-block:: shell

   # Rectangle
   plotext --rectangle '(0, 10)' '(0, 5)' --label filled --draw \
           --rectangle '(12, 22)' '(0, 5)' label=labelled --draw \
           --title Rectangle --show

   # Polygon
   plotext --polygon sides=6 --label hexagon --draw \
           --polygon sides=100 radius=0.5 --label circle --draw \
           --title Polygons --show

   # Segment
   plotext --segment '(0, 10)' '(0, 5)' --label diagonal --draw \
           --segment '(0, 10)' '(5, 5)' --label horizontal --draw \
           --title Segment --show

   # Combining shapes in one figure
   plotext --polygon --label triangle --draw \
           --rectangle --label rectangle --draw \
           --polygon sides=100 --label circle --draw \
           --title Shapes --legend --show

Each shape factory enters the drawable-config phase; ``--label`` chains on the just-built shape, ``--draw`` adds it to the figure and clears the slot for the next one.
