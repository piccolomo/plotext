.. _markers:

Markers
=======

A *marker* is the visual unit that represents a single data point — a symbol with optional colour and style. To change the marker of a plot, you have two options: pass a *string code* for quick selection (see :ref:`string_codes`), or a :class:`plotext.marker` object for full control over colour and style (see :ref:`marker_objects`).


Usage
-----

Every drawable method's ``marker`` parameter accepts:

- a :ref:`string code <string_codes>` — the simplest form.
- a :ref:`marker object <marker_objects>` — for full control over colour and style.
- a list of either — one entry per internal point, repeated to match the data length when shorter. For :meth:`~plotext._plotter.plot.plot_class.signal` and :meth:`~plotext._plotter.plot.plot_class.candlestick` the list maps to user data points; for shape primitives like :meth:`~plotext._plotter.plot.plot_class.rectangle` and :meth:`~plotext._plotter.plot.plot_class.polygon` it maps to vertex points instead.

A bare string code or marker object:

.. code-block:: python

   fig.signal(x, y, marker = "x")                                            # shorthand
   fig.signal(x, y, marker = plt.marker("x"))                                # explicit
   fig.signal(x, y, marker = plt.marker("x", plt.pixel(foreground="red")))   # styled

A list of string codes or marker objects (one per data point):

.. code-block:: python

   fig.signal(x, y, marker = ["x", "heart", "star"])                  # list of string codes
   fig.signal(x, y, marker = [plt.marker("x",     plt.pixel(foreground="red")),
                              plt.marker("heart", plt.pixel(foreground="blue")),
                              plt.marker("star",  plt.pixel(foreground="green"))])  # list of marker objects


.. _string_codes:

String codes
------------

A string code is one of three things:

- **A single printable character** — any character. A space makes the point invisible.
- **A named character code** — one of the entries in the table below.
- **A resolution code** — one of *hd*, *fhd*, or *braille* (described after the table).

.. note::

   Multi-character strings that aren't a named code or a resolution code raise a clear ``ValueError`` listing the valid options. Single characters (e.g. ``"x"``, ``"#"``) always pass through as literal glyphs. The previous ``"block"`` alias for the full block ``█`` has been replaced by ``"full"``.

.. code-block:: python

   fig.signal(x, y, marker = "x")          # single character
   fig.signal(x, y, marker = "heart")      # named character code
   fig.signal(x, y, marker = "braille")    # resolution code


Named character codes
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 10 20 10 20 10 20 10

   * - Code
     -
     - Code
     -
     - Code
     -
     - Code
     -
   * - ``full``
     - █
     - ``dot``
     - •
     - ``dollar``
     - $
     - ``euro``
     - €
   * - ``bitcoin``
     - ฿
     - ``at``
     - @
     - ``heart``
     - ♥
     - ``smile``
     - ☺
   * - ``gclef``
     - 𝄞
     - ``note``
     - 𝅘𝅥
     - ``shamrock``
     - ☘
     - ``atom``
     - ⚛
   * - ``snowflake``
     - ❄
     - ``star``
     - ❋
     - ``flower``
     - ❁
     - ``lightning``
     - 🌩
   * - ``queen``
     - ♕
     - ``king``
     - ♔
     - ``cross``
     - ♰
     - ``yinyang``
     - ☯
   * - ``om``
     - ॐ
     - ``osiris``
     - 𓂀
     - ``zero``
     - 🯰
     - ``one``
     - 🯱
   * - ``two``
     - 🯲
     - ``three``
     - 🯳
     - ``four``
     - 🯴
     - ``five``
     - 🯵
   * - ``six``
     - 🯶
     - ``seven``
     - 🯷
     - ``eight``
     - 🯸
     - ``nine``
     - 🯹

.. note:: Run :func:`plotext.markers` to print the live reference of every available code alongside its rendered symbol.


.. _resolutions:

Resolution codes
~~~~~~~~~~~~~~~~

Three codes control the character grid used to place a point. Some may not be available on every terminal or operating system.

- ``hd`` — *high definition* (default): 2 × 2 Unicode block characters (``▞``, ``▘``, ...), so each terminal cell can hold up to four sub-points.
- ``fhd`` — *full high definition*: 3 × 2 Unicode block characters (``🬗``). Unix-only, only on some terminals.
- ``braille`` — 4 × 2 Unicode braille characters (``⢕``). Finest resolution. Unix-only; supported by only a few terminals.

.. note:: Markers of different resolutions can coexist in the same plot across different signals. Within a single signal, mixing resolutions is safe for scatter plots but discouraged for line plots — the intermediate grid positions between consecutive points may not line up.


.. _marker_objects:

Marker objects
--------------

For full control over colour and style, construct a marker with :class:`plotext.marker` and an explicit :class:`plotext.pixel`:

.. code-block:: python

   import plotext as plt
   m = plt.marker("heart", plt.pixel("red", "white", "bold"))

Parameters:

- ``symbol`` — the symbol to draw. Accepts any :ref:`string code <string_codes>`, or a :class:`~plotext.matrix` / :class:`~plotext.colorize` for a multi-cell marker (see :ref:`plotting_matrices`).
- ``pixel`` — a :class:`plotext.pixel` carrying the colour + style. Defaults to a blank pixel. See :ref:`pixel`. Ignored when ``symbol`` is a matrix or colorize (those carry their own per-cell pixels).
- ``ha`` — *only when symbol is a matrix or colorize*: horizontal alignment of the matrix around the data point — ``-1`` left, ``0`` centered, ``1`` right (default ``-1``).
- ``va`` — *only when symbol is a matrix or colorize*: vertical alignment of the matrix around the data point — ``-1`` top, ``0`` centered, ``1`` bottom (default ``-1``).


.. _color_cycling:

Automatic colour cycling
------------------------

When a drawable is built without an explicit ``pixel`` (or marker pixel), its colour is drawn from a per-figure *cycler* — a fixed pool of pixels that each :meth:`~plotext._plotter.plot.plot_class.draw` call advances through. The default pool is 16 palette colours (cycled in order); calling :meth:`~plotext._plotter.plot.plot_class.clear_pixels` rewinds it.

The cycler also tracks colours the user *did* set explicitly: if a drawable is rendered with a pixel that matches one of the cycler's slots (foreground + background + style), that slot is marked used and skipped on subsequent implicit picks — so two series never end up the same palette colour by accident. Colours outside the pool (e.g. RGB triples) are not tracked: an explicit RGB pick won't influence what the cycler hands out next.

The pool itself lives at ``plotext._settings.defaults.pixel_sequence`` (a list of :class:`~plotext.pixel` objects) and can be replaced at import time before any figure is created.
