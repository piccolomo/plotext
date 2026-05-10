Terminal
========

``plt.terminal`` is the pre-built terminal object plotext uses to track the underlying terminal's size, the prompt height (lines reserved below the plot), and to drive screen-clearing during streaming loops. Unlike the primitives (:class:`plotext.pixel`, :class:`plotext.marker`, :class:`plotext.matrix`), it's a singleton you interact with rather than a value you construct.

Reach for it when you need to:

- query / constrain the rendering size (:meth:`~plotext._kernel.terminal.terminal.get_size`, :meth:`~plotext._kernel.terminal.terminal.limit`),
- wipe the visible region between frames in a live update loop (:meth:`~plotext._kernel.terminal.terminal.clean`),
- adjust the prompt height when adding or removing lines below the plot (:meth:`~plotext._kernel.terminal.terminal.prompt`),
- poll the keyboard non-blockingly inside a streaming loop (:meth:`~plotext._kernel.terminal.terminal.is_pressed`).


.. _streaming_pattern:

Streaming pattern
-----------------

The canonical "live update" idiom is:

1. Set ``plot_size`` so the plot occupies a known number of rows.
2. Each frame, call :meth:`~plotext._kernel.terminal.terminal.clean` with that row count to wipe the previous frame, :meth:`~plotext._plotter.plot.plot_class.clear_data` (alias ``cld``) to drop signals, redraw, then :meth:`~plotext._plotter.plot.plot_class.show` with ``flush=1``.
3. Poll :meth:`~plotext._kernel.terminal.terminal.is_pressed` at the top of each iteration so the user can quit cleanly with ``q``.

.. code-block:: python

   import math, itertools
   import plotext as plt

   fig    = plt.figure
   length = 200
   height = plt.terminal.get_size()[1]

   fig.clear()
   fig.plot_size(None, height)
   fig.lim(0, length, axis = "x")
   fig.lim(-1, 1,    axis = "y")

   x = range(length)
   for i in itertools.count():
       if plt.terminal.is_pressed('q'): break
       plt.terminal.clean(height)
       fig.cld()
       y = [math.sin(2 * math.pi * (k - i) / length * 4) for k in range(length)]
       fig.draw(fig.signal(x, y).lines(1).label("sin"))
       fig.show(flush = 1)
       print("press q to exit")

A full multi-stream variant — a 2×2 subplot grid where the top-right cell is itself split into two nested streaming rows — lives in ``tests/21_multi_stream.py``.


.. _is_pressed:

Polling for keys
----------------

:meth:`~plotext._kernel.terminal.terminal.is_pressed` is a non-blocking key poll. Calling it the first time switches the terminal into *cbreak* mode (each keystroke delivered immediately, no Enter required, no echo) and registers an ``atexit`` hook to restore *cooked* mode when the program ends. Subsequent calls just check whether a key is in the input buffer.

.. code-block:: python

   if plt.terminal.is_pressed('q'):
       break

Notes:

- The function takes a single character (case-insensitive). Default is ``'q'``.
- When ``stdin`` is not a TTY (piped input, redirected, ``/dev/null``) it always returns ``False`` — useful so live demos still run cleanly inside non-interactive sweeps.
- Cross-platform: ``msvcrt.kbhit`` / ``msvcrt.getch`` on Windows, ``termios`` + ``tty`` + ``select`` on Unix.


Reference
---------

The full method list is rendered in :doc:`api`.

.. note:: More documentation for any of the methods is available via :code:`plotext.doc.terminal.<method>()` (for example ``plotext.doc.terminal.is_pressed()``).
