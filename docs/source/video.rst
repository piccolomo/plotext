Video and YouTube Plots
=======================

Methods that play moving images in the terminal — local video files via ffpyplayer (synced audio + video), YouTube URLs resolved via yt-dlp. Both share the rendering pipeline used by :doc:`image`: decode-on-fly, paint each frame through :func:`plotext.image`, sleep only the remainder of the inter-frame interval, terminal-resize support for free.

- :ref:`video` — play a local video file.
- :ref:`youtube` — play a YouTube URL.


.. _video:

Video
-----

:func:`plotext.video` plays a local video file in the terminal with **synchronised audio**. A single ``ffpyplayer.MediaPlayer`` owns both streams: it pushes audio to the sound device on its own thread and yields video frames paired with a per-frame *seconds-to-sleep* value. Honouring that value keeps the visible frames locked to the audio timeline. Press ``q`` to exit.

Like :ref:`gif`, this is decode-on-fly: no upfront pre-decode pass, terminal-resize support comes for free, and the cost per frame is one PIL conversion + one matrix paint.

.. code-block:: python

   import plotext as plt

   plt.video("path/to/video.mp4")              # default: loop forever, fit terminal, preserve aspect

Parameters:

- ``path`` — filesystem path to the video (any format ffpyplayer can decode).
- ``gray`` — if ``True``, convert each frame to grayscale before rendering.
- ``ratio`` — if ``True`` (default), preserve the source aspect ratio (with cell-aspect compensation); if ``False``, stretch each frame to exactly ``(width, height)``.
- ``loop`` — if ``True`` (default), replay forever until ``q`` is pressed; if ``False``, play once and return.
- ``width`` / ``height`` — target dimensions in canvas chars; default to the current terminal size, otherwise clamped against the terminal when :meth:`plt.terminal.limit <plotext._kernel.terminal.terminal.limit>` is on for that axis.

.. note::

   ``video`` requires ``ffpyplayer`` — both the video frames and the audio come from a single ``MediaPlayer``, so they share a clock and stay in sync. We honour the per-frame sleep value returned by ``MediaPlayer.get_frame()`` to track the player's timeline. Install with ``pip install plotext[video]``.

.. note:: More documentation is available via :code:`plotext.doc.video()`.


.. _youtube:

YouTube
-------

:func:`plotext.youtube` plays a YouTube URL in the terminal. It resolves the URL to a direct stream URL via `yt-dlp <https://github.com/yt-dlp/yt-dlp>`_, then delegates to :func:`plotext.video`. Press ``q`` to exit.

.. code-block:: python

   import plotext as plt

   plt.youtube("https://www.youtube.com/watch?v=YE7VzlLtp-4")

Parameters mirror :ref:`video` — ``gray``, ``ratio``, ``loop``, ``width``, ``height`` — with ``url`` replacing ``path``.

.. note::

   ``youtube`` requires both ``yt-dlp`` and ``ffpyplayer`` — install with ``pip install plotext[video]``. Stream URLs returned by yt-dlp expire after a while; for very long sessions the URL is re-resolved at the start of each ``loop`` pass when the player reaches end-of-stream.

.. note::

   ``yt-dlp`` is the modern fork of the abandoned ``youtube-dl``; this is a deliberate dependency choice — YouTube extractors break frequently and ``youtube-dl`` is no longer kept in sync.

.. note:: More documentation is available via :code:`plotext.doc.youtube()`.
