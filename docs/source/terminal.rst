Terminal
========

The :class:`plotext.terminal <plotext._kernel.terminal.terminal>` object tracks the terminal the plots print to: its size, the prompt height (the lines reserved below the plot for user input) and the screen cleaning during :doc:`streaming plots <stream>`.

Use it to:

- set the **prompt height** (:meth:`prompt() <plotext._kernel.terminal.terminal.prompt>`)
- read the terminal **size**, and limit the master plot size to it (:meth:`size() <plotext._kernel.terminal.terminal.size>`, :meth:`limit() <plotext._kernel.terminal.terminal.limit>`)
- **clean** the last printed lines, between frames of a streaming plot (:meth:`clean() <plotext._kernel.terminal.terminal.clean>`)
- check for a **key press**, without pausing the program (:meth:`is_pressed() <plotext._kernel.terminal.terminal.is_pressed>`)

.. note:: The :meth:`size() <plotext._kernel.terminal.terminal.size>`, :meth:`clean() <plotext._kernel.terminal.terminal.clean>` and :meth:`is_pressed() <plotext._kernel.terminal.terminal.is_pressed>` methods drive streaming plots, with the full pattern described in the :doc:`streaming plots <stream>` page.


.. _prompt_height:

Prompt Height
-------------

The :meth:`prompt() <plotext._kernel.terminal.terminal.prompt>` method sets the height of the terminal prompt, the area reserved for **user input** below the plot, 2 lines by default; with no arguments, it restores the default.


.. _terminal_size:

Terminal Size
-------------

The :meth:`size() <plotext._kernel.terminal.terminal.size>` method returns the last known ``(width, height)`` of the terminal in characters, useful to size the plot relative to the terminal window. Pass ``update = True`` to read the terminal size afresh, and ``plottable = False`` to include the prompt lines in the height:

.. code-block:: python

   w, h = plt.terminal.size()
   fig.plot_size(w, h // 2)   # half-height plot


.. _no_terminal:

No Terminal
~~~~~~~~~~~

| |plotext| asks the system how many characters fit on the screen. **Sometimes there is no answer**: the output is piped into another program, or the program runs inside a container, or a web server runs it with nothing attached.
| The system then reports a size of zero, or the fallback 80 by 22, and, since a plot is normally kept inside the terminal, either everything is drawn far too small or nothing is drawn at all.
| Nothing is broken there: |plotext| simply believes the screen has no room. Say what the room is, in one of two ways:

.. code-block:: python

   plt.terminal.limit(False, False)   # stop keeping the plot inside the terminal
   fig.plot_size(140, 40)             # and state the size yourself

or leave the code alone and set the size in the environment the program runs in, which |plotext| reads:

.. code-block:: shell

   COLUMNS=140 LINES=40 python3 my_plot.py

.. caution:: A **browser** is a different case: it cannot read the color codes a terminal uses, so a plot printed into a web page comes out as unreadable text. Write the page instead, with :meth:`matrix.html() <plotext.matrix.html>` or :meth:`matrix.save() <plotext.matrix.save>` on the :ref:`matrix <matrix>` that :meth:`figure.build() <plotext._plotter.plot.plot_class.build>` gives back.


.. _size_limits:

Size Limits
-----------

| The :meth:`limit() <plotext._kernel.terminal.terminal.limit>` method sets whether the master plot size is limited to the terminal plottable area, one boolean per dimension (``width`` and ``height``, both ``True`` by default).
| With a limit turned off, a larger plot can be set with :meth:`plot_size() <plotext._plotter.plot.plot_class.plot_size>`, and the terminal scrolls.
| Call :meth:`limit() <plotext._kernel.terminal.terminal.limit>` **before** :meth:`plot_size() <plotext._plotter.plot.plot_class.plot_size>`: the requested size is clamped to the terminal the moment it is set, so lifting a limit afterwards has no effect on it. See the :doc:`size <size>` page.


.. _is_pressed:

Polling for Keys
----------------

The :meth:`is_pressed() <plotext._kernel.terminal.terminal.is_pressed>` method tells whether the given key (``q`` by default, a single character, case insensitive) has been typed, answering **right away**, with no waiting; it is useful when :doc:`streaming <stream>`, checked at every frame, to stop the stream:

.. code-block:: python

   if plt.terminal.is_pressed('q'):
       break

.. note:: The typed keys reach the program without showing on screen and with no Enter needed; when the input is not a keyboard, as in automated runs, the answer is always ``False``, and the stream runs to its end.

.. note:: The typed keys wait in a queue: each check takes the oldest one out and compares it, so on a stream a typed ``q`` is always caught, a few frames later when other keys sit in front of it.

.. caution:: Outside a stream, a single call just answers ``False``, as no key is waiting; the exception is a key typed while the program was busy, say in a long computation, which the next check finds.


.. _terminal_clearing:

Terminal Clearing
-----------------

The terminal object holds its own pair of resets:

- :meth:`clean() <plotext._kernel.terminal.terminal.clean>`: cleans the given number of last printed lines, so the next print takes their place; with no arguments, it clears the whole terminal. Useful when :doc:`streaming plots <stream>`.
- :meth:`clear() <plotext._kernel.terminal.terminal.clear>`: resets the terminal object state: the :ref:`prompt height <prompt_height>`, the width and height :ref:`limits <size_limits>` and the last known terminal :ref:`size <terminal_size>`.

Calling :meth:`clear() <plotext._kernel.terminal.terminal.clear>` only resets the terminal object, leaving the figure *untouched*.

.. note:: The figure clear methods leave these settings alone: a :meth:`plotext.figure.clear() <plotext._plotter.clear.clear_class.all>` inside a loop keeps the :ref:`prompt height <prompt_height>` and the :ref:`limits <size_limits>` you set, and only this method puts them back to their defaults.


.. seealso:: The full method list is in the :ref:`terminal section <terminal_api>` of the :doc:`api <api>` page.

.. note:: More documentation for any of the methods is available via ``plotext.doc.terminal.<method>()`` (for example :meth:`plotext.doc.terminal.is_pressed() <plotext._kernel.terminal.terminal.is_pressed>`).
