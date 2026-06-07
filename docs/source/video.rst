Video Plot
==========

:func:`plotext.video` plays a video in the terminal with **synchronised audio**. A single ``ffpyplayer.MediaPlayer`` owns both streams: it pushes audio to the sound device on its own thread and yields video frames paired with a per-frame *seconds-to-sleep* value. Honouring that value keeps the visible frames locked to the audio timeline. Press ``q`` to exit — a ``press q to exit`` hint (``q`` in bold red, on a discrete dark label) is stamped onto the bottom-left of every frame as a reminder, overwriting those cells in place so the frame keeps its size.

Like :ref:`gif`, this is decode-on-fly: no upfront pre-decode pass, terminal-resize support comes for free, and the cost per frame is one PIL conversion + one matrix paint.

A single entry point handles three source kinds:

- **local file** — ``plt.video("path/to/video.mp4")`` or ``"~/Movies/clip.mp4"``.
- **direct media URL** (http/https/ftp) — downloaded once into a per-user temp folder (``<tempfile.gettempdir()>/plotext/``) and reused on subsequent calls, same as :ref:`image` and :ref:`gif`.
- **YouTube URL** (any host matching ``youtube.com`` / ``youtu.be``) — resolved internally via `yt-dlp <https://github.com/yt-dlp/yt-dlp>`_ to a time-limited stream URL and played directly. The stream URL is *not* cached because YouTube tokens expire.

.. code-block:: python

   import plotext as plt

   plt.video("path/to/video.mp4")                                                                      # local file
   plt.video("https://raw.githubusercontent.com/piccolomo/plotext/master/data/moonwalk.mp4")          # direct URL — cached after first download
   plt.video("https://www.youtube.com/watch?v=YE7VzlLtp-4")                                            # YouTube — resolved via yt-dlp

Parameters:

- ``path`` — local filesystem path, ``"~/…"`` user-home path, direct http/https media URL, or YouTube URL.
- ``gray`` — if ``True``, convert each frame to grayscale before rendering.
- ``ratio`` — if ``True`` (default), preserve the source aspect ratio (with cell-aspect compensation); if ``False``, stretch each frame to exactly ``(width, height)``.
- ``loop`` — if ``True``, replay forever until ``q`` is pressed; if ``False`` (default), play once and return.
- ``width`` / ``height`` — target dimensions in canvas chars; default to the current terminal size, otherwise clamped against the terminal when :meth:`plt.terminal.limit <plotext._kernel.terminal.terminal.limit>` is on for that axis.

.. note::

   ``video`` requires ``ffpyplayer`` for playback (both video frames and audio come from a single ``MediaPlayer``, so they share a clock and stay in sync). YouTube support additionally requires ``yt-dlp``. Install both with ``pip install plotext[video]``.

.. note::

   ``yt-dlp`` is the modern fork of the abandoned ``youtube-dl``; this is a deliberate dependency choice — YouTube extractors break frequently and ``youtube-dl`` is no longer kept in sync.

.. note::

   The pre-6.0 ``plt.youtube(url)`` helper has been folded into ``plt.video``: pass the YouTube URL to ``video`` and the host-based detection routes it through ``yt-dlp`` for you. No separate entry point.

.. note:: More documentation is available via :code:`plotext.doc.video()`.


Command-line
------------

Same three source kinds work from the CLI:

.. code-block:: shell

   plotext --video /path/to/clip.mp4
   plotext --video 'https://raw.githubusercontent.com/piccolomo/plotext/master/data/moonwalk.mp4'
   plotext --video 'https://www.youtube.com/watch?v=YE7VzlLtp-4'

``--video`` resolves to :func:`plotext.video` directly (no figure pipeline). All three sources behave the same as in the Python API.
