.. _subplots:

Subplots
========

``plotext`` can create and render a matrix of subplots, each with its own data and settings. Each subplot can itself be a matrix of subplots, recursively.

The following example exercises every subplot-related method. It creates a 2 × 2 master grid where row 1 has explicit conflicting widths (so the master ``size_direction`` is visible), and the bottom-right subplot hosts a nested 3 × 3 grid with the opposite direction (so the contrast between the two levels makes both cases easy to read):

.. code-block:: python

   import plotext as plt

   fig = plt.figure
   fig.clear()

   # Data
   y = plt.sin()

   # Master figure layout
   fig.size_direction(-1)            # leftover absorbed by the FIRST column/row
   fig.size_policy("maximum")        # column/row takes the largest requested size

   # 2 x 2 grid
   fig.subplots(2, 2)

   sub = fig.subplot(1, 1)
   sub.plot_size(200, 10)
   sub.draw(sub.signal(y).label("(1,1)"))
   sub.title("top-left")

   sub = fig.subplot(1, 2)
   sub.plot_size(200, 10)
   sub.draw(sub.signal(y).label("(1,2)"))
   sub.title("top-right")

   sub = fig.subplot(2, 1)
   sub.draw(sub.signal(y).label("(2,1)"))
   sub.title("bottom-left")

   # (2, 2): nested 3 x 3 with the opposite direction
   sub = fig.subplot(2, 2)
   sub.plot_size(100, 10)
   sub.size_direction(+1)            # nested: leftover absorbed by the LAST column/row
   sub.size_policy("minimum")        # nested: column/row takes the smallest requested size
   sub.subplots(3, 3)

   sub.subplot(2, 2).plot_size(60, 6)
   for r in range(1, 4):
       for c in range(1, 4):
           sub.subplot(r, c).title(f"{r}-{c}")

   fig.legend()
   fig.show()


Create
------

``subplots`` divides a subplot into a *rows × cols* grid. Calling it on *plt.figure* (the master) builds the top-level grid; calling it on any subplot turns that subplot into a container for a nested grid.


Address
-------

``subplot`` returns the subplot at a given *(row, col)* so it can be addressed directly. Plotting calls — *signal*, *draw*, *title*, *plot_size*, and so on — are then invoked on that subplot. Each subplot can be resized independently via *plot_size* (see :doc:`size` for details).


Resolve
-------

Within a matrix of subplots of possibly different sizes, the sizes need to be resolved before the plot is rendered. By default each subplot's size is derived from its parent's dimensions (the terminal, for the master plot). When explicit sizes are set, the resolution happens in two steps.


Size direction
~~~~~~~~~~~~~~

First, the total sizes in a row (widths) or column (heights) cannot exceed the parent's own dimensions. ``size_direction`` decides the direction in which this check is performed: with *+1* the check runs left-to-right for widths and top-to-bottom for heights, so every subplot receives at most its requested size and the last subplot along the axis absorbs whatever remains of the budget. With *-1* the direction is reversed, and the first subplot absorbs the leftover instead.


Size policy
~~~~~~~~~~~

Lastly, all widths in a given column, and all heights in a given row, must share a single value. When nested subplots disagree on their requested size, ``size_policy`` decides the rule: with *maximum* (the default) each column/row takes the largest requested size and the canvas grows to accommodate, while with *minimum* it takes the smallest and all subplots shrink to fit.


Navigate
--------

Once a tree of subplots has been built, the following methods let you walk it:

- :meth:`~plotext._plotter.plot.plot_class.get_parent` — returns the parent plot at the given nesting level (``0`` is the plot itself, ``1`` its immediate parent, and so on; the walk stops at the master).
- :meth:`~plotext._plotter.plot.plot_class.get_master` — returns the master plot at the top of the tree.
- :meth:`~plotext._plotter.plot.plot_class.get_terminal` — returns the :class:`~plotext._kernel.terminal.terminal` object that owns the master.
- :meth:`~plotext._plotter.plot.plot_class.get_position` — returns this subplot's ``(row, col)`` within its parent grid; ``(None, None)`` for the master.
- :meth:`~plotext._plotter.plot.plot_class.get_size` — returns this subplot's ``(width, height)`` in terminal cells.
- :meth:`~plotext._plotter.plot.plot_class.get_log` and :meth:`~plotext._plotter.plot.plot_class.log` — return / print a multi-line indented dump of this subplot and every nested subplot, useful when debugging layout resolution.
