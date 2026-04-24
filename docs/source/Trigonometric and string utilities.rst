:orphan:

.. autofunction:: plotext.sin
   :no-index:

.. autofunction:: plotext.draw
   :no-index:

.. autoclass:: plotext._plotter.draw.draw_class
   :members:
   :no-index:

   This class represents a plot object. Users should **not instantiate it directly**.
   Instead, use the factory function :func:`plotext.create_plot()` to obtain a ready-to-use plot instance.


.. autoclass:: plotext._plotter.plot.plot_class
   :members:
   :undoc-members:
   :no-index:

   This class represents a plot object. Users should **not instantiate it directly**.
   Instead, use the factory function :func:`plotext.create_plot()` to obtain a ready-to-use plot instance.


.. autofunction:: plotext.title
   :no-index:
.. autofunction:: plotext.show
   :no-index:
.. autofunction:: plotext.grid
   :no-index:
.. autofunction:: plotext.label
   :no-index:

.. autofunction:: plotext.signal
   :no-index:

.. autoclass:: plotext._signal.signal.signal_class
   :members: clear, fill, copy, clone, log
   :show-inheritance:
   :no-index:

.. autoclass:: plotext.marker
    :members:
    :undoc-members:
    :inherited-members:
    :no-index:




.. .. autoclass:: plotext.pixel
..    :members:
..    :undoc-members:
..    :show-inheritance:

.. .. autoclass:: plotext.colorize
..    :members:
..    :undoc-members:
..    :show-inheritance:

.. .. autofunction:: plotext.uncolorize

.. .. autoclass:: plotext.matrix
..    :members:
..    :undoc-members:
..    :show-inheritance:


.. .. autofunction:: plotext.colors
.. .. autofunction:: plotext.styles
.. .. autofunction:: plotext.test


.. .. _prettydoc_api:

.. prettydoc
.. ---------

.. The `prettydoc` module is responsible for managing and customizing docstring formatting.

.. .. autoclass:: plotext.prettydoc.docs
..    :members:
..    :undoc-members:
..    :show-inheritance:

.. .. autofunction:: plotext.prettydoc.components
.. .. autofunction:: plotext.prettydoc.test
