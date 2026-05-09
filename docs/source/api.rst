API Documentation
=================

.. toctree::
   :maxdepth: 2
   :caption: API Overview


plotext
-------

The ``plotext`` module is the main package. It exposes a small set of module-level helpers and reference tables, plus the master figure (``plt.figure``) through which every plot operation is invoked.

.. autofunction:: plotext.sin

.. autofunction:: plotext.uncolorize

.. autofunction:: plotext.colors

.. autofunction:: plotext.styles

.. autofunction:: plotext.markers

.. autofunction:: plotext.test


figure
------

``plt.figure`` is the master figure instance — an object of :class:`plotext._plotter.plot.plot_class`. Every plotting call (drawing signals, configuring axes, creating subplots) is a method on it. The same methods are available on any subplot returned by ``fig.subplot(r, c)``.

.. autoclass:: plotext._plotter.plot.plot_class()
   :members: signal, draw, candlestick, segment, rectangle, polygon, bar, text, show, build,
             clear, clear_data, clear_settings, clear_size, clear_subplots, clear_pixels, clear_styles,
             title, label, legend,
             axis, frame, alignment, direction,
             scale, lim, frequency, ticks, ruler_pixel, tick_alignment, grid,
             date, convert,
             plot_size, subplots, subplot,
             size_direction, size_policy,
             canvas_pixel,
             get_parent, get_master, get_terminal, get_position, get_size, get_log, log,
             time


.. _signal:

signal
------

The signal class holds a sequence of points plus drawing options. Do not instantiate it directly — use ``fig.signal(...)`` (or ``sub.signal(...)`` on any subplot), which handles date conversion and marker color cycling on your behalf. The returned signal can then be configured with its direct methods below before being passed to ``fig.draw(...)``.

.. autoclass:: plotext._signal.signal.signal_class()
   :members: lines, point_lines, label, fillx, filly, fill, line_method, fill_method, get_length, copy, clone, log, clear


pixel
-----

.. autoclass:: plotext.pixel
   :members:


colorize
--------

.. autoclass:: plotext.colorize
   :members:


matrix
------

.. autoclass:: plotext.matrix
   :members:


marker
------

.. autoclass:: plotext.marker
   :members:


terminal
--------

``plt.terminal`` is the pre-built terminal object; use its methods to inspect and constrain the terminal in which plotext renders.

.. autoclass:: plotext._kernel.terminal.terminal()
   :members: limit, get_size, clean, clear, prompt, log


.. _prettydoc_api:

prettydoc
---------

The ``prettydoc`` module is responsible for managing and customizing docstring formatting.

.. autoclass:: plotext.prettydoc.docs
   :members:
