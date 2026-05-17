Axes
====

The *frame axes* are the four lines drawn at the edges of the plot canvas: the lower and upper x axes and the left and right y axes. They control the visible borders or frame of the plot itself, and can optionally carry ticks corresponding to the numerical ones placed by the :doc:`ruler`.

Two methods manage their appearance: ``axis`` for a single axis side, and ``frame`` as a batch shortcut for all four at once.


Single axis
-----------

``axis`` controls the visibility (``status``), line style, and colour (via ``pixel``) of one frame side.

.. _line_styles:

The ``style`` parameter is a string accepting one of four values:

- ``default`` — single solid line (the default)
- ``double`` — double solid line
- ``dotted`` — dashed/dotted line
- ``rounded`` — solid line with rounded corners at the frame intersections

For ``grid``, only ``default`` and ``double`` are supported.

See :ref:`pixel` for details on the ``pixel`` parameter.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   y = plt.sin()
   signal = fig.signal(y)
   fig.draw(signal)

   fig.axis(status = False, axis = "x", side = "upper")   # hide the upper x axis
   fig.axis(style = "dotted",                              # red dotted left y axis
            pixel = plt.pixel(foreground = "red"),
            axis = "y", side = "left")

   fig.title("Axis")
   fig.show()


All four sides at once
----------------------

``frame`` applies the same ``status``, ``style`` and ``pixel`` to every frame side in one call — useful when you want a uniform frame.

.. code-block:: python

   import plotext as plt
   fig = plt.figure
   fig.clear()

   y = plt.sin()
   signal = fig.signal(y)
   fig.draw(signal)

   fig.frame(status = False)        # hide the whole frame
   # fig.frame(style = "dashed")    # or set a common line style

   fig.title("Frame")
   fig.show()


.. _axis:

Selecting an axis
-----------------

Many plotext methods take an ``axis`` parameter — and, when the choice is ambiguous, a ``side`` parameter — to choose which axis they apply to.

The ``axis`` parameter accepts:

- ``"x"`` or ``0`` — the x axis
- ``"y"`` or ``1`` — the y axis
- a list (``["x", "y"]`` or ``[0, 1]``) — both axes at once

The ``side`` parameter disambiguates between the two sides of a given axis:

- for x: ``"lower"`` or ``0`` (default) / ``"upper"`` or ``1``
- for y: ``"left"`` or ``0`` (default) / ``"right"`` or ``1``
