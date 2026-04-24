.. _markers:

Markers
=======

Most plotting functions in ``plotext`` accept a ``marker`` parameter that controls the symbol drawn at each data point. For example::

   signal = plt.signal(x, y, marker = "x")

The ``marker`` parameter accepts three input forms:

- **A single character** — any printable character. A space character makes the point invisible.
- **A list of characters or codes** — one per data point; the list automatically adapts to match the length of the data.
- **A marker code** — either a named character code (``"dot"``, ``"heart"``, ``"star"``, ...) or one of the resolution codes listed below.

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
     - 𝅘𝅥
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


.. note:: Run :func:`plotext.markers` to print the live reference of every available code alongside its rendered glyph.

Four additional resolution codes control the character grid used to place a point. Some may not be available on every terminal or operating system.

- ``sd`` — *standard definition*: one full-width block (``█``) per data point.
- ``hd`` — *high definition* (default): 2 × 2 Unicode block characters (``▞``, ``▘``, ...), so each terminal cell can hold up to four sub-points.
- ``fhd`` — *full high definition*: 3 × 2 Unicode block characters (``🬗``). Unix-only, only on some terminals.
- ``braille`` — 4 × 2 Unicode braille characters (``⢕``). Finest resolution. Unix-only; supported by only a few terminals.

.. note:: Markers of different resolutions can coexist in the same plot across different signals. Within a single signal, mixing resolutions is safe for scatter plots but discouraged for line plots — the intermediate grid positions between consecutive points may not line up.

A marker also accepts ``foreground``, ``background`` and ``style`` parameters to set its colour and text style. See :ref:`colors` and :ref:`styles` for the available values.

The underlying :class:`~plotext.marker` class is documented in the API reference.
