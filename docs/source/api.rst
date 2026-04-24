API Documentation
=================

.. toctree::
   :maxdepth: 2
   :caption: API Overview


plotext
-------

The `plotext` module is the main package, offering various tools for creating visual representations in the terminal.

.. autofunction:: plotext.sin

.. autofunction:: plotext.signal

.. autofunction:: plotext.draw

.. autofunction:: plotext.candlestick

.. autofunction:: plotext.show

.. autofunction:: plotext.title

.. autofunction:: plotext.label

.. autofunction:: plotext.legend

.. autofunction:: plotext.alignment

.. autofunction:: plotext.direction

.. autofunction:: plotext.scale

.. autofunction:: plotext.lim

.. autofunction:: plotext.frequency

.. autofunction:: plotext.ticks

.. autofunction:: plotext.grid

.. autofunction:: plotext.axis

.. autofunction:: plotext.frame


.. autofunction:: plotext.date

.. autofunction:: plotext.convert

.. autofunction:: plotext.uncolorize

.. autofunction:: plotext.colors

.. autofunction:: plotext.styles

.. autofunction:: plotext.markers


.. _signal:

signal
------

The signal class holds a sequence of points plus drawing options. Do not instantiate it directly — use :func:`plotext.signal` instead, which is a method of the plot class that handles date conversion and marker color cycling on your behalf. The returned signal can then be configured with its direct methods below before being passed to :func:`plotext.draw`.

.. autoclass:: plotext._signal.signal.signal_class()
   :members: lines, label, fillx, filly, line_method, fill_method


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


.. _prettydoc_api:

prettydoc
---------

The `prettydoc` module is responsible for managing and customizing docstring formatting.

.. autoclass:: plotext.prettydoc.docs
   :members:
