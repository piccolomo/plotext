Streaming Plots
===============

A streaming plot is just a regular plot in a tight loop: clear the previous frame, recompute the data, redraw, sleep (or block on input). plotext makes this flicker-free with two primitives:

- :func:`plt.terminal.clean(n) <plotext._kernel.terminal.terminal.clean>` — wipe exactly ``n`` rows above the cursor, so the next render overwrites the previous one cleanly with no scroll.
- ``fig.show(flush = 1)`` — emit the rendered frame in a single write, eliminating tearing.
- :func:`plt.sleep(seconds) <plotext.sleep>` — pause between frames; throttles the loop and further reduces flicker on fast terminals.

Combine those with :func:`plt.terminal.get_size(update=True) <plotext._kernel.terminal.terminal.get_size>` and you also get free terminal-resize handling: the next frame fills the new size. Animated title and axis labels follow naturally — feed :func:`plt.effect` into :func:`fig.title` and :func:`fig.label`, advancing the effect's ``step`` each iteration.

- :ref:`stream_single`  — a single scrolling signal.
- :ref:`stream_pattern` — the loop skeleton, line by line.


.. _stream_single:

Single signal
-------------

A sine wave scrolling left at 4 cycles per window. Press ``q`` to exit:

.. code-block:: python

   import math
   import plotext as plt

   fig    = plt.figure
   length = 200

   fig.clear()
   fig.lim(0, length, axis = "x")
   fig.lim(-1, 1,     axis = "y")

   x = range(length)
   i = 0
   while True:
       if plt.terminal.is_pressed('q'): break
       fig_height = fig.get_size()[1]                                # rows currently on screen
       if i: plt.terminal.clean(fig_height)                          # wipe the previous frame
       w, h = plt.terminal.get_size(update = True)
       fig.cld()                                                     # clear data, keep axes/limits
       fig.plot_size(w, h)                                           # adapt to current terminal
       y = [math.sin(2 * math.pi * (k - i) / length * 4) for k in range(length)]
       fig.title(plt.effect("streaming sin wave", "rainbow",  step = i * 0.4))
       fig.label(plt.effect("samples",            "shimmer",  step = i * 0.4), axis = 0)
       fig.label(plt.effect("amplitude",          "gradient", step = i * 0.2), axis = 1)
       fig.draw(fig.signal(x, y).lines(1).label("sin"))
       fig.show(flush = 1)
       print("press q to exit")
       i += 1

This is the source of ``tests/22_stream.py``.


.. _stream_pattern:

The loop skeleton
-----------------

Every streaming plot in plotext follows the same five-step skeleton:

.. code-block:: python

   i = 0
   while True:
       if plt.terminal.is_pressed('q'): break                        # 1. exit on keypress
       if i: plt.terminal.clean(fig.get_size()[1])                   # 2. wipe previous frame
       w, h = plt.terminal.get_size(update = True)                   # 3. re-read terminal size
       fig.cld(); fig.plot_size(w, h)                                # 4. clear data, adapt size
       # ... compute new data, fig.draw(...) ...
       fig.show(flush = 1)                                           # 5. render in one write
       i += 1

Notes:

- ``fig.cld()`` only clears **data**; axis limits, labels, and titles set outside the loop survive — set ``lim``, ``title``, ``xlabel`` etc. *before* the loop.
- ``flush = 1`` is what makes the redraw look atomic; without it you can see partial frames on slow terminals.
- The first iteration ``i == 0`` is special: nothing is on screen yet, so ``terminal.clean`` would eat the prompt above. The ``if i:`` guard skips it.

.. note:: A runnable streaming example lives at ``tests/22_stream.py``.


Command-line
------------

Streaming plots are control-flow-heavy: each frame's data is computed inside the loop, frames are cleared with :func:`plt.terminal.clean`, and rendering is keyed off ``fig.show(flush=1)``. The CLI's chain syntax can't express that — so for animation you reach for ``plotext -c "<code>"``, which runs arbitrary Python with ``plt`` (and ``plotext``) pre-bound.

The Python example above translates onto a shell line one-to-one:

.. code-block:: shell

   plotext -c "
   import math
   fig = plt.figure
   length = 200
   fig.clear()
   fig.lim(0, length, axis='x')
   fig.lim(-1, 1, axis='y')
   x = range(length)
   i = 0
   while True:
       if plt.terminal.is_pressed('q'): break
       if i: plt.terminal.clean(fig.get_size()[1] - 2)
       fig.cld()
       y = [math.sin(2 * math.pi * (k - i) / length * 4) for k in range(length)]
       fig.draw(fig.signal(x, y).lines(1))
       fig.show(flush=1)
       i += 1
   "

The ``- 2`` in ``terminal.clean(fig.get_size()[1] - 2)`` cancels the default 2-row prompt offset that :meth:`plt.terminal.clean(N) <plotext._kernel.terminal.terminal.clean>` adds for an IPython-style input area. In IPython the offset is real and the Python example earlier on this page leaves it; from bash the offset is spurious and would shift the new frame down, leaving the previous frame's bottom row (the x-ticks) visible.

``plotext -c "<code>"`` is equivalent to ``python -c "import plotext as plt; <code>"`` — same one-shot Python execution, just with ``plt`` already imported. Anywhere the chain syntax falls short (animation, real event handling, custom data generation per frame), reach for it.
