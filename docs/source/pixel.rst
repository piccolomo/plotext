.. _pixel:

Pixel
=====

| A :class:`~plotext.pixel` object bundles a foreground :ref:`color <colors>`, a background color and a :ref:`style <styles>` into **one object**.
| It is the **coloring unit** of |plotext|: every colored object, from a :ref:`marker <markers>` to a plot element, carries one.

Construct one with any combination of its three parameters:

.. code-block:: python

   import plotext as plt
   px = plt.pixel(foreground = 'red', background = 'blue', style = 'bold')
   print(px)

Printing the pixel shows its representation, painted with its own colors:

.. image:: images/pixel.png
   :alt: pixel representation


.. _pixel_forms:

Pixel Forms
-----------

Every ``pixel`` parameter across |plotext| accepts, beside a :class:`~plotext.pixel` object, a few shorthand forms:

- a single :ref:`color <colors>`, read as the foreground: a string code, an integer, or a tuple of three integers, read as RGB
- a (foreground, background, style) tuple, like ``("red", "white", "bold")``, where the trailing entries can be omitted
- ``None``, for the default pixel of the method

.. caution:: Each entry of the tuple form can itself be an RGB tuple, which calls for a disambiguation: a bare tuple of three integers is always read as an RGB foreground, not as (foreground, background, style). To use the tuple form with an RGB foreground alone, nest it, as in ``((16, 100, 200),)``.


Common Uses
-----------

- **Recolor a** :ref:`colorized object <colorize>` after creation:

   .. code-block:: python
      :emphasize-lines: 4

      import plotext as plt
      string = plt.colorize("Colorless String")
      px     = plt.pixel(foreground = 'red')
      string.fill(px)

- **Fill a** :ref:`matrix <matrix>` **with a uniform pixel**:

   .. code-block:: python

      import plotext as plt
      pixel  = plt.pixel(background = "blue+")
      matrix = plt.matrix(100, 30, pixel)

- **Style a prettydoc component**, pass a pixel to change the coloring of any prettydoc element (see the prettydoc :ref:`colors <doc_color>` section).

- **Color a marker**, pass a pixel to the ``pixel`` parameter of :class:`plotext.marker` (see :ref:`marker object <marker_objects>`).

- **Color a plot element**, pass a pixel to any method whose ``pixel`` parameter sets the element's coloring (:meth:`axes() <plotext._plotter.plot.plot_class.axes>`, :meth:`ruler().grid() <plotext._plotter.frame.ruler.ruler_class.grid>`, :meth:`ruler().pixel() <plotext._plotter.frame.ruler.ruler_class.pixel>`, :meth:`legend() <plotext._plotter.plot.plot_class.legend>`, :meth:`line() <plotext._plotter.plot.plot_class.line>`, :meth:`error() <plotext._plotter.plot.plot_class.error>`, :meth:`event() <plotext._plotter.plot.plot_class.event>`).

.. note:: More documentation is available via ``plotext.doc.pixel()``.


.. _colors:

Colors
------

A |plotext| color could be either a foreground or a background. The corresponding parameters accept three input forms:

- **Color string codes.** Predefined short names (see the reference image below).

  .. image:: images/color-codes.png
     :alt: color string codes

  .. note:: ``"default"`` writes **no color at all**, so whatever the :doc:`terminal <terminal>` already shows stays there: as a background it leaves the character see through. Any unrecognized code falls back to the same.

- **Integer codes** from 0 to 255.

  .. image:: images/integer-codes.png
     :alt: integer color codes

  .. note:: The first 16 integers correspond to the string color codes above.

.. |rgb| image:: images/rgb-color.png
   :width: 110

- **RGB tuples**: three integers for the red, green and blue channels, for example |rgb|. Each component must be from 0 to 255.

.. seealso:: The :func:`plotext.colors() <plotext.colors>` function prints the full live reference of available color codes.

.. tip:: A color is read back with :meth:`foreground() <plotext.pixel.foreground>` and :meth:`background() <plotext.pixel.background>`, each giving an ``(r, g, b)`` tuple, or ``None`` when that color is not set. A name, or a number from 0 to 255, is translated into red, green and blue values by the |plotext| color table; a :doc:`terminal <terminal>` using its own palette may draw the same code with different values.


.. _styles:

Styles
------

The ``style`` parameter accepts one or more style codes (see below).

.. image:: images/styles.png
   :alt: style codes
   :align: left

.. note:: The ``"flash"`` style renders as an actual flashing white :ref:`marker <markers>`.

.. note:: Multiple styles can be combined by separating them with a space: ``"bold italic"`` applies both **bold** and *italic* to the text.

.. seealso:: The :func:`plotext.styles() <plotext.styles>` function prints the full live reference of available style codes.
