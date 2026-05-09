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
   fig.title("Rectangle")
   fig.show()

Parameters:

- ``x`` — the x range of the rectangle, as a two-value tuple or list. Endpoint order doesn't matter; *min* and *max* are taken internally.
- ``y`` — the y range of the rectangle, same format as *x*.
- ``marker`` — the symbol used to render the rectangle. Pass a single character or a *plotext marker* (see :ref:`markers`).
- ``lines`` — when *true* (default), the rectangle outline is densified so the border draws cleanly (and the body fills, when fill is also true). When *false*, only the corner points are placed.
- ``fill`` — when *true* (default), the rectangle's body is filled with markers. When *false*, only the clockwise outline is drawn.
- ``xside``, ``yside`` — which axis pair the rectangle is plotted against (see :ref:`axis`).


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
