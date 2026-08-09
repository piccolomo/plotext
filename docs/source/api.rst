API Documentation
=================

plotext
-------

The |plotext| module is the **main package**: it holds the functions listed below, the primitive classes and the :ref:`prettydoc <prettydoc_api>` module, each described in its own section of this page, and four attributes: the master figure :class:`plotext.figure <plotext._plotter.plot.plot_class>`, the :class:`plotext.terminal <plotext._kernel.terminal.terminal>` object, the ``plotext.doc`` :doc:`documentation container <prettydoc>` and the :ref:`plotext.file <file_api>` toolkit.

Two module-level constants are also available:

* ``plotext.version``: the installed |plotext| version string, the same as ``plotext.__version__``.
* ``plotext.platform``: ``"unix"`` or ``"windows"``, detected when the package is imported and used internally for the differences in terminal handling.

.. autofunction:: plotext.sin

.. autofunction:: plotext.square

.. autofunction:: plotext.noise

.. autofunction:: plotext.sample

.. autofunction:: plotext.uncolorize

.. autofunction:: plotext.colors

.. autofunction:: plotext.styles

.. autofunction:: plotext.markers

.. autofunction:: plotext.line_styles

.. autofunction:: plotext.themes

.. autofunction:: plotext.add_theme

.. autofunction:: plotext.effect

See :doc:`colorize` for usage and :doc:`stream` for the animation pattern.

.. autofunction:: plotext.sleep

See :doc:`stream` for the animation pattern.

.. autofunction:: plotext.image

See :doc:`media` for full usage notes and a comparison with the figure-integrated ``plotext.figure.image()``.

.. autofunction:: plotext.gif

See :doc:`media` for full usage notes.

.. autofunction:: plotext.video

See :doc:`media` for full usage notes, ``plotext.video`` handles local files, direct media URLs, and YouTube URLs natively.

.. autofunction:: plotext.matplotlib

.. autofunction:: plotext.test


pixel
-----

.. autoclass:: plotext.pixel
   :members:


.. _colorize_api:

colorize
--------

.. autoclass:: plotext.colorize
   :members:


.. _matrix_api:

matrix
------

.. autoclass:: plotext.matrix
   :members:


.. _marker_api:

marker
------

.. autoclass:: plotext.marker
   :members:


line
----

.. autoclass:: plotext.line
   :members:


.. _signal_api:

signal
------

A :ref:`signal <signal>` is a **sequence of points** plus its drawing settings, created by :meth:`signal() <plotext._plotter.plot.plot_class.signal>` and passed to :meth:`draw() <plotext._plotter.plot.plot_class.draw>`.

.. autoclass:: plotext._signal.signal.signal_class()
   :members: lines, line, label, fillx, filly, fill, density, length, get, copy, clone, log, clear


.. _point:

point
-----

The point class is what :meth:`signal.get() <plotext._signal.signal.signal_class.get>` returns: one data point, with its coordinates and marker. It cannot be created directly.

.. autoclass:: plotext._signal.point_filled.point()
   :members: x, y, marker


figure
------

:class:`plotext.figure <plotext._plotter.plot.plot_class>` is the **master figure** instance. The same methods are available on any subplot returned by :meth:`plotext.figure.subplot() <plotext._plotter.plot.plot_class.subplot>`.

.. autoclass:: plotext._plotter.plot.plot_class()
   :members: signal, draw, candlestick, line, segment, rectangle, polygon, bar, hist, box, error, event, heatmap, cmatrix, image, text, show, build, theme, interactive,
             title, label, axes, canvas, legend,
             ruler, date,
             plot_size, subplots, subplot,
             parent, master, position, size, log,
             time


ruler
-----

:meth:`plotext.figure.ruler() <plotext._plotter.plot.plot_class.ruler>` returns the :ref:`ruler <rulers>` of the selected axis and side.

.. autoclass:: plotext._plotter.frame.ruler.ruler_class()
   :members: frequency, ticks, lim, scale, direction, alignment, pixel, grid, clear


date
----

:meth:`plotext.figure.date() <plotext._plotter.plot.plot_class.date>` returns the :doc:`date <date>` selection of the chosen rulers; its methods turn date support on and off, convert dates between forms and report reference dates.

.. autoclass:: plotext._plotter.frame.date.date_class()
   :members: activate, active, convert, today, origin, clear


clear
-----

:class:`plotext.figure.clear <plotext._plotter.clear.clear_class>` groups the clearing methods; each method resets one aspect of the plot. Calling it directly, as :class:`plotext.figure.clear() <plotext._plotter.clear.clear_class>`, resets everything, and it is equivalent to :meth:`plotext.figure.clear.all() <plotext._plotter.clear.clear_class.all>`.

.. autoclass:: plotext._plotter.clear.clear_class()
   :members: all, data, settings, pixels, styles, size, subplots


.. _file_api:

file
----

:class:`plotext.file <plotext._methods.file.file_class>` is the pre-built **file toolkit** object; its methods read, write and manage files.

.. autoclass:: plotext._methods.file.file_class()
   :members: read, write, csv, string, exists, delete, parent, join, download


.. _terminal_api:

terminal
--------

:class:`plotext.terminal <plotext._kernel.terminal.terminal>` is the pre-built terminal object: its methods read and limit the terminal size, wipe printed rows and check key presses.

.. autoclass:: plotext._kernel.terminal.terminal()
   :members: limit, size, clean, clear, prompt, log, is_pressed, parent


.. _prettydoc_api:

prettydoc
---------

The :doc:`prettydoc <prettydoc>` module is responsible for managing and customizing **docstrings** and their formatting.

.. autoclass:: plotext.prettydoc.docs
   :members:

.. autoclass:: plotext.prettydoc.registry
   :members: add, get

.. autofunction:: plotext.prettydoc.components

.. autofunction:: plotext.prettydoc.test
