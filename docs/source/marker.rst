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
- **A resolution code** — one of *sd*, *hd*, *fhd*, or *braille* (described after the table).

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
   * - ``sd``
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

Four codes control the character grid used to place a point. Some may not be available on every terminal or operating system.

- ``sd`` — *standard definition*: one full-width block (``█``) per data point.
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

- ``code`` — the symbol to draw. Accepts any :ref:`string code <string_codes>`.
- ``pixel`` — a :class:`plotext.pixel` carrying the colour + style. Defaults to a blank pixel. See :ref:`pixel`.
