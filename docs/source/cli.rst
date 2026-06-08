Command Line
============

plotext ships a command-line tool — runnable as ``plotext`` after install or ``python -m plotext`` from a source checkout. It exposes every figure method through a single chainable syntax: each ``--METHOD`` token opens a call, tokens until the next ``--METHOD`` become that call's args. No subcommands, no hand-maintained method list — the CLI introspects ``plt.figure`` at runtime so it tracks the API automatically.

.. code-block:: shell

   plotext --signal [1,4,9,16,25] --lines --title squares --show
   plotext --bar [a,b,c] [10,25,18] --title Counts --show
   plotext --hist [1,1,2,2,2,3] bins=4 --show


Chain syntax
------------

Each method call is introduced by ``--name``; tokens between it and the next ``--name`` are that call's args:

.. code-block:: shell

   plotext --plot-size 60 12 \
           --signal [1,2,3,4] --lines --label A --draw \
           --signal [4,3,2,1] --lines --label B --draw \
           --title 'Two series' --legend --show

Methods that return a signal (``signal``, ``bar``, ``hist``, ``candlestick`` …) enter a **drawable-config phase**: subsequent ``--name``s dispatch to the drawable (``--lines``, ``--label``, ``--fillx`` …) instead of the figure. ``--draw`` exits the phase and adds the drawable to the figure. ``--show`` must be explicit for plot methods (mirroring the Python API): without it, nothing is rendered.

Media methods (``--image``, ``--gif``, ``--video``) are special: they print directly to the terminal (bypassing the figure pipeline entirely), so they don't need ``--show`` and don't enter the drawable-config phase.

Module-level data helpers (``--sin``, ``--square``, ``--noise``) feed the next signal-creating method: ``--sin --signal --lines --show`` runs ``signal(sin())`` because ``--sin``'s output is held until the next ``--signal``/``--bar``/``--hist``/… call consumes it as the first positional argument. ``--noise --hist bins=20 --show`` does the same for a histogram of Gaussian noise.

``--method-name`` and ``--method_name`` are equivalent — hyphens map to underscores.


Value parsing
-------------

Each token is parsed independently:

* ``key=value`` becomes a kwarg when ``key`` matches a parameter name; otherwise positional.
* ``[1,2,3]`` or ``[a,b,c]`` becomes a list (bare words become strings). ``{a:1}`` becomes a dict. Numbers, ``true`` / ``false`` / ``null`` map to the obvious Python values.
* ``@path:<path>`` loads a CSV from disk (or URL) via :func:`plotext.file.read`. Multi-column CSVs are transposed and splatted into separate positional args. Append ``:1`` (1-indexed) or ``:1,2`` to pick specific columns, or ``:dict`` to use the first row as keys and return a dict of column lists (useful for ``--candlestick`` and other dict-shaped inputs).
* ``@sample:<name>`` loads a bundled sample shipped with plotext: ``@sample:pizzas`` / ``@sample:stock`` are CSVs (same suffixes apply: ``:1``, ``:dict``…); ``@sample:puppy`` returns the path to a bundled sample image. The set is auto-discovered from ``plotext/_examples/data/`` so any file dropped there appears in ``plotext --help``.
* ``-`` reads stdin and parses it as whitespace-split numbers (or a multi-column CSV that splats into separate positional args).
* Anything else is a string.

URL handling
~~~~~~~~~~~~

``http://``, ``https://`` and ``ftp://`` arguments are downloaded once into ``<tempfile.gettempdir()>/plotext/`` (i.e. ``/tmp/plotext/`` on Unix, ``%TEMP%\plotext\`` on Windows) and reused on subsequent calls. This works wherever a method expects a path — ``--image``, ``--gif``, ``--video``, ``@path:https://…/file.csv``, etc. — because it's wired into the Python ``plotext._methods.file.correct()`` helper, not the CLI parser. YouTube URLs passed to ``--video`` route through ``yt-dlp`` internally; their stream URLs are *not* cached because the tokens expire.


Shortcuts
---------

* ``-c "<code>"`` skips the chain parser and runs arbitrary Python with ``plotext`` (already loaded as ``plt``) pre-bound — equivalent to ``python -c "import plotext as plt; <code>"``. Use when the chain syntax can't express the control flow you need (e.g. animation loops with ``plt.terminal.clean`` / ``fig.show(flush=1)``, or any case where each frame's data is computed inside the loop rather than piped in from outside).


Discovering methods
-------------------

* ``plotext --help`` prints the usage, value-parsing rules, ``@`` syntax, and a handful of examples.
* ``plotext --doc`` opens the interactive doc picker — sections in side-by-side columns, arrow-key navigation, Enter shows the selected method's title + docstring. Mirrors ``plotext.doc()`` in the Python API.
* ``plotext --METHOD --doc`` prints the docstring of a single method (e.g. ``plotext --candlestick --doc``). Mirrors ``plotext.doc.<method>()`` in the Python API.



Limitations
-----------

* Methods that take plotext objects (``pixel``, ``marker``, ``colorize``) work when the argument can be passed as a string the constructor accepts (e.g. ``pixel='red'``). Fully programmatic object construction stays Python-only.
* Per-frame animation loops, custom event handling, and anything else that needs real control flow stay Python-only too — use ``-c "<code>"`` to inline that Python on the command line, or write a script.
