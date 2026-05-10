Heatmap, Image and GIF Plots
============================

Methods that render 2D data as a coloured grid of cells — one canvas character per matrix entry. plotext exposes three flavours, each suited to a different use case:

- :ref:`heatmap` — render any 2D matrix (numeric or RGB) as a *plot signal* that participates in the figure pipeline (axes, ticks, overlays).
- :ref:`image` — render an image file from disk. Available in two forms: a **figure-integrated** :meth:`~plotext._plotter.plot.plot_class.image` (slower, plot-aware) and a **direct** module-level :func:`plotext.image` (fast, returns a printable matrix).
- :ref:`gif` — animate a GIF in the terminal at its natural per-frame speed.

Pick the figure-integrated forms when the rendering needs to coexist with axes, ticks, titles, or other signals. Pick the module-level direct forms when you just want pixels on screen as fast as possible.

For moving-image content (local video files, YouTube URLs), see :doc:`video`.


.. _heatmap:

Heatmap
-------

:meth:`~plotext._plotter.plot.plot_class.heatmap` renders a 2D matrix as a coloured grid. Numeric input is normalized to the chosen colormap (``"gray"`` or ``"viridis"``); RGB-tuple input passes through untouched. Row 0 of the matrix is drawn at the top of the canvas (matching ``imshow`` convention).

The result is a single signal — pass it to :meth:`~plotext._plotter.plot.plot_class.draw`. There are two rendering modes:

- ``fill=False`` (default): one full-block character per cell. Cells map to canvas chars one-to-one, so size the canvas to ``(cols, rows)`` via :meth:`~plotext._plotter.plot.plot_class.plot_size` before drawing — otherwise cells appear sparsely on a default-sized canvas. Best for image-style data where the canvas is meant to *be* the matrix.
- ``fill=True``: every cell is a filled rectangle that auto-scales to whatever canvas size is currently set. No ``plot_size`` hand-tuning needed. Best for small heatmaps you want to display at a comfortable on-screen size.

.. code-block:: python

   import math
   import plotext as plt

   fig = plt.figure
   fig.clear()

   cols, rows = plt.terminal.get_size()
   data = [[math.sin(c / cols * 2 * math.pi) * math.cos(r / rows * math.pi)
            for c in range(cols)] for r in range(rows)]

   fig.frame(0)
   fig.draw(fig.heatmap(data, map = "viridis", fill = 1))
   fig.show()

Parameters:

- ``data`` — 2D sequence; either numeric values (colormap applied) or ``(r, g, b)`` integer triples (used as cell colour directly). All rows must share the same length; ragged input is truncated to the shortest row.
- ``map`` — colormap name applied to numeric input: ``"gray"`` (default) or ``"viridis"``. Ignored when input is already RGB.
- ``fill`` — if ``False`` (default), one symbol per cell (caller sizes the plot via ``plot_size`` to match cols/rows); if ``True``, each row is densified into a filled band that auto-scales to the canvas.
- ``symbol`` — symbol used to render every cell. Default ``'█'`` (full block). Accepts any single character or a named symbol code (see :func:`plotext.markers`). Higher-resolution codes (``"hd"``, ``"fhd"``, ``"braille"``) are not accepted: a single terminal character can carry only one foreground colour, so splitting it into sub-cells forces every sub-cell to share that one colour — the per-data-point resolution stays locked at one full character regardless of the marker.
- ``xside``, ``yside`` — which axis pair the cells are anchored to (see :ref:`axis`).

.. note::

   The default ticks may not be meaningful for categorical heatmap cells — call ``fig.frequency(0, axis = "x"); fig.frequency(0, axis = "y")`` after drawing to hide them.

.. note:: More documentation is available via :code:`plotext.doc.heatmap()`.


.. _image:

Image
-----

plotext exposes two image entry points that share the same rendering core but live at different scopes.


Figure-integrated: ``fig.image(...)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:meth:`~plotext._plotter.plot.plot_class.image` opens the image via Pillow, optionally converts it to grayscale, resamples it to the current ``plot_size`` (or terminal size when no plot size has been set), and returns a :ref:`heatmap` signal mapping each pixel 1:1 to a canvas char. Plot-integrated — supports ``xside`` / ``yside``, can overlay other signals, lives inside the figure's frame and ticks. Caller is responsible for ``plot_size``, ``frame`` and tick frequency settings.

.. code-block:: python

   import plotext as plt

   fig = plt.figure
   fig.clear()

   cols, rows = plt.terminal.get_size()
   fig.plot_size(cols, rows); fig.frame(0)
   fig.frequency(0, axis = "x"); fig.frequency(0, axis = "y")
   fig.draw(fig.image("path/to/image.jpg"))
   fig.show()


Direct: ``plt.image(...)``
~~~~~~~~~~~~~~~~~~~~~~~~~~

:func:`plotext.image` is the **fast** alternative. It bypasses the figure pipeline entirely: opens via Pillow, optional grayscale, resamples to ``(width, height)`` (default = terminal size; user-specified values are clamped against the terminal when :meth:`plt.terminal.limit <plotext._kernel.terminal.terminal.limit>` is on for that axis — the default — or passed through unchanged when the limit has been disabled), and paints the pixels straight into a :class:`plotext.matrix`. The returned matrix is print-ready — caller does ``img.print()``.

Typically **5–10× faster** than the figure-integrated form because there's no axis layout, no ruler harmonization, no signal pipeline — just a per-pixel paint into a flat matrix.

.. code-block:: python

   import plotext as plt

   img = plt.image("path/to/image.jpg")           # default size = current terminal
   img.print()

Parameters (same for both forms):

- ``path`` — filesystem path to the image (any format supported by Pillow).
- ``gray`` — if ``True``, convert the image to grayscale before rendering.
- ``width``, ``height`` — *(direct form only)* target dimensions in canvas chars. None falls back to the terminal dim; otherwise clamped against the terminal when :meth:`plt.terminal.limit <plotext._kernel.terminal.terminal.limit>` is on for that axis (the default) or passed through unchanged when the limit has been disabled (e.g. ``plt.terminal.limit(height=False)``).
- ``symbol`` — *(figure-integrated form only)* symbol used to render every pixel. Default ``'█'`` (full block); same input forms as :ref:`heatmap`.

.. note::

   Both forms require `Pillow <https://pillow.readthedocs.io/>`_, which is **not** installed by default. Install plotext with the ``image`` extras::

      pip install "plotext[image]"

   Calling either ``image`` without Pillow installed raises a clear ``ImportError``. See :doc:`install` for the full list of optional extras.

.. note:: More documentation is available via :code:`plotext.doc.image()` (direct form) and :code:`plotext.doc.figure.image()` (figure-integrated form).


.. _gif:

GIF
---

:func:`plotext.gif` animates a GIF in the terminal. It uses a **decode-on-fly** strategy: each frame is decoded, painted, and printed inside the playback loop, with the program then sleeping only the remainder of the GIF's per-frame duration before moving on. Press ``q`` to exit.

This design has three nice properties:

1. **No upfront pre-decode wait.** The first frame appears within ~10 ms instead of after a multi-second pre-pass.
2. **Natural playback timing.** Frames target their authored per-frame delay (``img.info['duration']``); when the paint cost exceeds that delay the GIF gracefully slows down rather than racing ahead at maximum speed.
3. **Free terminal-resize support.** Each frame is painted using the current terminal size (with the same clamping rules as :func:`plotext.image`), so resizing the window mid-playback simply takes effect on the next frame — no resize listener, no cache to invalidate.

.. code-block:: python

   import plotext as plt

   plt.gif("path/to/animation.gif")            # default: loop forever, fit terminal

Parameters:

- ``path`` — filesystem path to the GIF.
- ``gray`` — if ``True``, convert each frame to grayscale before rendering.
- ``width`` / ``height`` — target dimensions in canvas chars; default to the current terminal size, otherwise clamped against the terminal when :meth:`plt.terminal.limit <plotext._kernel.terminal.terminal.limit>` is on for that axis (the default) or passed through unchanged when the limit has been disabled.
- ``loop`` — if ``True`` (default), replay forever until ``q`` is pressed; if ``False``, play once and return.

.. note:: ``gif`` requires Pillow — install with ``pip install plotext[image]``.

.. note:: More documentation is available via :code:`plotext.doc.gif()`.


Performance & design notes
--------------------------

When choosing between the figure-integrated and direct forms:

+------------------------+----------------------------+----------------------------+
| Concern                | ``fig.image`` (slow)       | ``plt.image`` (fast)       |
+========================+============================+============================+
| Returns                | a signal (pass to ``draw``)| a printable ``matrix``     |
+------------------------+----------------------------+----------------------------+
| Plot pipeline          | yes (axes, ticks, overlay) | no                         |
+------------------------+----------------------------+----------------------------+
| Typical 80×30 image    | ~50 ms                     | ~10 ms                     |
+------------------------+----------------------------+----------------------------+
| Sizing                 | ``fig.plot_size``          | ``width`` / ``height``     |
+------------------------+----------------------------+----------------------------+

For pure "show me this image" or "play this gif" use cases, prefer the direct module-level forms — they're substantially faster and have a smaller surface area. Reach for ``fig.image`` when the image needs to coexist with other plot signals, axes, or annotations.

The shared internals live in ``git/plotext/_methods/image.py``:

- ``_resolve_size(width, height)`` — clamps user-supplied dims against the terminal so the canvas never overflows; falls back to the terminal dim when ``None``. Used by both ``image()`` and ``gif()``.
- ``_render_image(img, gray, width, height)`` — the single PIL-Image → painted ``plotext.matrix`` path. Both ``image()`` and ``gif()`` route every paint through this helper.
- ``heatmap(data, map='gray', symbol=None)`` — internal numeric/RGB matrix painter (no figure pipeline). Used by ``_render_image``; not exported at module level.
