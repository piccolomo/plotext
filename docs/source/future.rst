Future Plan
===========

| Open ideas for |plotext| 6.x, kept here as **inspiration** rather than committed work, unless an `Issue` is linked, which marks something somebody has already asked for.
| Contributions are welcome: open an `issue <https://github.com/piccolomo/plotext/issues/new>`_ or a `pull request <https://github.com/piccolomo/plotext/compare>`_.


Bug Fixes
---------

- **Business days**: an optional :doc:`date <date>` axis skipping weekends, and holidays, so that a series of trading days shows no flat gaps between them (`Issue 148 <https://github.com/piccolomo/plotext/issues/148>`_).
- **Bars meeting at zero**: a bar runs from zero to its value, so a positive and a negative bar of the same plot both paint the zero column, and the two touch. Drawing them from either side of that column, leaving it to a zero line, would separate them, at the cost of half a character of accuracy on every bar (`Pull Request 222 <https://github.com/piccolomo/plotext/pull/222>`_, which solved the same matter in version 5 by assembling each row as text).
- **Limits as a wall**: a point just outside the :meth:`limits <plotext._plotter.frame.ruler.ruler_class.lim>` is still drawn on the edge row, because the default :meth:`alignment <plotext._plotter.frame.ruler.ruler_class.alignment>` centers each value in its character, leaving half a character of tolerance beyond the range asked for. Pinning them with ``alignment(lim = "edge")`` works today; the same strictness should hold with the centered alignment too, which means selecting the points against the limits instead of against the canvas (`Issue 185 <https://github.com/piccolomo/plotext/issues/185>`_).


Settings
--------

- **Changing the defaults**: every default sits in `defaults.py <https://github.com/piccolomo/plotext/blob/master/plotext/_settings/defaults.py>`_, from the :ref:`marker <markers>` used when none is given to the first *x* coordinate of a plot drawn from a single list of values, 1 rather than 0, as `Issue 176 <https://github.com/piccolomo/plotext/issues/176>`_ asked. A method setting any of them by name, as ``plotext.default("first x", 0)``, would let a user pick their own once, instead of repeating the choice at every call.


Plots
-----

- **Color bar**: an optional bar beside the :ref:`heatmap <heatmap>`, pairing the color gradient with the values it spans, so that a color can be read back as a number.
- **Networks**: a plot of nodes and of the edges joining them, with a rule placing the nodes on the canvas (`Issue 160 <https://github.com/piccolomo/plotext/issues/160>`_). The drawing is already possible by hand, an edge being a :meth:`segment() <plotext._plotter.plot.plot_class.segment>` and a node a :meth:`text() <plotext._plotter.plot.plot_class.text>`; what is missing is the placing rule, deciding where each node goes.
- **Tables**: a plain text table, distinct from the :ref:`heatmap <heatmap>` and the :ref:`confusion matrix <confusion_matrix>`, which color cells instead of aligning text.
- **Date errors**: :meth:`error() <plotext._plotter.plot.plot_class.error>` accepts numbers only, since it adds and halves its coordinates; date coordinates would need the horizontal errors written as durations, *2 days* rather than a date, with a conversion of their own.
- **Gifs and videos in a plot**: a still picture goes inside a plot with :meth:`figure.image() <plotext._plotter.plot.plot_class.image>`, but a :ref:`gif <gif>` and a :ref:`video <video>` cannot: :func:`plotext.gif() <plotext.gif>` and :func:`plotext.video() <plotext.video>` take over the whole terminal, so neither can sit in a :ref:`panel <subplots>` beside other plots. A ``figure.gif()`` and a ``figure.video()`` would draw one picture per frame into the panel, which is what a user has to write by hand today.
- **Event colors**: :meth:`event() <plotext._plotter.plot.plot_class.event>` paints every line with one :ref:`pixel <pixel_forms>`; a list of pixels, one per event, would match what :meth:`bar() <plotext._plotter.plot.plot_class.bar>` already accepts per group.


Signals
-------

- **A title over a grid**: :meth:`figure.title() <plotext._plotter.plot.plot_class.title>` on a figure divided into :ref:`subplots <subplots>` does not title the grid, it copies the title into every panel, since only a plot with a canvas has a row for it. A heading over the whole grid would need a row of its own above the panels.
- **Axis sides**: replace the ``xside`` and ``yside`` parameters of the drawing methods with methods setting them on the returned :ref:`signal <signal>`. It is blocked by the date conversion, which happens when the signal is created and reads settings held per axis side: those settings would have to move to the axis itself. :meth:`line() <plotext._plotter.plot.plot_class.line>` and :meth:`event() <plotext._plotter.plot.plot_class.event>` draw on the figure without returning a signal, so they would keep their parameters.
- **Bent lines**: a :ref:`line plot <line>` whose characters turn with it, ``╭ ╮ ╰ ╯`` where it changes row and ``│`` between them, the look of `asciichart <https://github.com/kroitor/asciichart>`_, asked for in `Issue 199 <https://github.com/piccolomo/plotext/issues/199>`_. The pieces are already there: the box marker takes its four arms separately, and arms accumulate when two of them land on the same character, so the work is to give each point of a connecting line the arms pointing at its neighbours, inside the kernel, where the points are already counted in canvas characters.
- **Cell positions**: :meth:`line() <plotext._plotter.plot.plot_class.line>` and :meth:`legend() <plotext._plotter.plot.plot_class.legend>` already take a ``relative`` setting, counting their position in canvas cells instead of data units. The same setting on a :ref:`signal <signal>`, and on :meth:`text() <plotext._plotter.plot.plot_class.text>` first of all, would pin a drawing to a place on the screen that the data and the limits cannot move; it needs the setting on the C++ signal, and the skip of the data to cell conversion when it is on.


Terminals
---------

- **Asking the terminal**: the :ref:`higher resolution codes <resolutions>` may not draw on a rare terminal, and |plotext| has no way of knowing beforehand; asking the terminal which characters it can draw would let each system pick the finest marker it can show, rather than the safest one.
- **Clickable plots**: reading the mouse, so that a point can be picked on the plot (`Issue 175 <https://github.com/piccolomo/plotext/issues/175>`_); hard on a plain terminal.
- **Command line completion**: pressing TAB after ``plotext --`` could list the methods, as version 5 did for its subcommands; the list is already there, since :doc:`--methods <cli>` prints every reachable method.


Documentation
-------------

- **IPython**: an `IPython <https://ipython.org/>`_ extension for :doc:`prettydoc <prettydoc>`, so that ``object?`` prints the colored docstring where one exists, and the usual page otherwise. It would be loaded once per session, with ``%load_ext``, since patching IPython on every ``import plotext`` is too large a side effect.
