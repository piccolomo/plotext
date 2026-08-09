Change Log
==========


Version 6.0
-----------

A major rewrite, compared here against version `5.3.2 <https://pypi.org/project/plotext/5.3.2/>`_, the latest published one. In version 5 a plot was made by calling functions of the package itself, as ``plotext.scatter()``; in version 6 they are methods of one master figure, :class:`plotext.figure <plotext._plotter.plot.plot_class>`, and the rendering is done by a new kernel written in C++.


Internals and Primitives
^^^^^^^^^^^^^^^^^^^^^^^^

**New**

- The rendering kernel is written in C++, in `plotext/_kernel/cpp/ <https://github.com/piccolomo/plotext/tree/master/plotext/_kernel/cpp>`_, reached from Python through the `clink <https://github.com/piccolomo/plotext/blob/master/plotext/_kernel/clink.py>`_ bindings; it is compiled during the installation, and the package warns, without failing, when no compiler is found.
- :ref:`plotext.pixel <pixel>` bundles a foreground color, a background color and a style into one object, accepted wherever a color was given before.
- :ref:`plotext.matrix <matrix>` is a grid of colored characters, sliceable in two dimensions, stackable, saveable and convertible to a web page; it is what :meth:`figure.build() <plotext._plotter.plot.plot_class.build>` gives back.
- :ref:`plotext.marker <markers>` builds a symbol with its own coloring, and accepts a matrix or a colorize object, so that a marker may cover several cells.
- :func:`plotext.line() <plotext.line>` builds a line character marker, merging with the others at their crossings.
- The whole tree is mapped in `structure.txt <https://github.com/piccolomo/plotext/blob/master/structure.txt>`_, one line per file, each taken from the opening comment of the file itself.

**Changed**

- :ref:`plotext.colorize <colorize>` is now a class, not a function: it holds a string with its coloring, prints with :meth:`colorize.print() <plotext.colorize.print>`, stacks with ``+`` and ``/``, and is sliceable. Its ``fullground`` parameter is gone, the coloring living in the pixel.
- The package is reorganized: `_primitives/ <https://github.com/piccolomo/plotext/tree/master/plotext/_primitives>`_ for pixel, colorize, matrix, marker and box, `_signal/ <https://github.com/piccolomo/plotext/tree/master/plotext/_signal>`_ for the signal and its points, `_plotter/ <https://github.com/piccolomo/plotext/tree/master/plotext/_plotter>`_ for the figure, its drawing methods, its frame and its legend, `_kernel/ <https://github.com/piccolomo/plotext/tree/master/plotext/_kernel>`_ for the public interface and the bridge to C++, `_correct/ <https://github.com/piccolomo/plotext/tree/master/plotext/_correct>`_ for the parameter validation, `_methods/ <https://github.com/piccolomo/plotext/tree/master/plotext/_methods>`_ for the standalone tools, `_settings/ <https://github.com/piccolomo/plotext/tree/master/plotext/_settings>`_ for the defaults and the themes, `_constants/ <https://github.com/piccolomo/plotext/tree/master/plotext/_constants>`_ for the accepted names, `_doc/ <https://github.com/piccolomo/plotext/tree/master/plotext/_doc>`_ for the docstrings, `_demos/ <https://github.com/piccolomo/plotext/tree/master/plotext/_demos>`_ for the reference tables, `_data/ <https://github.com/piccolomo/plotext/tree/master/plotext/_data>`_ for the sample files, `_tests/ <https://github.com/piccolomo/plotext/tree/master/plotext/_tests>`_ for the test suite, `_cli/ <https://github.com/piccolomo/plotext/tree/master/plotext/_cli>`_ for the command line tool, and `prettydoc/ <https://github.com/piccolomo/plotext/tree/master/plotext/prettydoc>`_ for the docstring builder and its interactive menu.


Vocabulary and Defaults
^^^^^^^^^^^^^^^^^^^^^^^

**Markers**

- ``sd`` is renamed ``full`` and ``lightning`` is renamed ``zigzag``; ``gclef`` and ``note`` are replaced by ``eighth``, ``beamed``, ``flat`` and ``sharp``.
- The ten digit markers, from ``zero`` to ``nine``, and ``osiris`` are removed.
- Twenty two are added: ``brick``, ``sun``, ``cloud``, ``umbrella``, ``emptystar``, ``square``, ``emptysquare``, ``circle``, ``emptycircle``, ``diamond``, ``emptydiamond``, ``up``, ``down``, ``left``, ``right``, ``arrowup``, ``arrowdown``, ``arrowleft``, ``arrowright``, ``infinity``, ``check`` and ``xmark``.
- A :ref:`marker <markers>` may also be a plain string of several characters, a :ref:`matrix <matrix>` or a :ref:`colorize <colorize>` object, stamped whole at each point, or a list of any of these, one per point.

**Themes**

- Six are kept: *default*, *dark*, *dreamland*, *matrix*, *retro* and *windows*.
- Ten are removed: *clear*, *elegant*, *girly*, *grandpa*, *mature*, *pro*, *sahara*, *salad*, *scream* and *serious*.
- Six are added: *colorless*, *dusk*, *garden*, *sand*, *simple* and *wine*.

**Colors and styles**

- ``yellow`` is accepted, as another name for ``orange+``; the ``gold`` of the version 5 color sequence, which was never a valid color, is gone.
- The eight :ref:`style codes <styles>` are unchanged, and several of them now combine in one string.

**Defaults**

- The number of numerical ticks is 7 on the *x* axis and 5 on the *y* one; version 5 had 5 and 7.
- The rulers are written in ``blue+`` instead of black.
- The legend appears on its own when something is labelled, as described above.


Plot Creation
^^^^^^^^^^^^^

**Renamed**

- ``scatter()`` and ``plot()`` become one :meth:`figure.signal() <plotext._plotter.plot.plot_class.signal>` method, whose result is passed to :meth:`figure.draw() <plotext._plotter.plot.plot_class.draw>`; the connecting lines are set on the signal itself, with :meth:`signal.lines() <plotext._signal.signal.signal_class.lines>`.
- ``bar()``, ``multiple_bar()`` and ``stacked_bar()`` become one :meth:`figure.bar() <plotext._plotter.plot.plot_class.bar>` method: a list of height sequences groups the bars, and ``stacked = True`` stacks them.
- A bar of value **zero** draws nothing, where version 5 painted its base row; in a stacked bar that row covered the group below it, as reported in `Issue 187 <https://github.com/piccolomo/plotext/issues/187>`_.
- ``event_plot()`` becomes :meth:`figure.event() <plotext._plotter.plot.plot_class.event>`, ``matrix_plot()`` becomes :meth:`figure.heatmap() <plotext._plotter.plot.plot_class.heatmap>`, ``image_plot()`` becomes :meth:`figure.image() <plotext._plotter.plot.plot_class.image>`, and ``confusion_matrix()`` becomes :meth:`figure.cmatrix() <plotext._plotter.plot.plot_class.cmatrix>`.

**Removed**

- ``simple_bar()``, ``simple_multiple_bar()`` and ``simple_stacked_bar()``: the same frame-less look is now a recipe of the regular bar plot, described in the :ref:`simple bar style <simple_bar>` section.
- ``indicator()``: it is now built from :meth:`figure.text() <plotext._plotter.plot.plot_class.text>` and a couple of settings, as shown in the :ref:`indicator <indicator>` section.
- The ``heatmap()`` of version 5, which took a pandas dataframe, printed it as a side effect and carried no documentation; the new :meth:`figure.heatmap() <plotext._plotter.plot.plot_class.heatmap>` takes a two dimensional sequence of numbers, or of ``(r, g, b)`` triples.

**Changed**

- :meth:`figure.candlestick() <plotext._plotter.plot.plot_class.candlestick>` takes one dictionary, with keys ``date``, ``open``, ``close``, ``high`` and ``low``, instead of the two positional arguments of version 5, and gains the ``style`` parameter, *candle* or *ohlc*, with its ``tick`` length, as asked in `Issue 149 <https://github.com/piccolomo/plotext/issues/149>`_.
- :meth:`figure.box() <plotext._plotter.plot.plot_class.box>` is complete: it was added in version 5.3, as asked in `Issue 169 <https://github.com/piccolomo/plotext/issues/169>`_, and marked there as needing further development.
- :meth:`figure.error() <plotext._plotter.plot.plot_class.error>` takes its errors as leading arguments, ``(x, y, yerr, xerr)``, instead of the ``xerr`` and ``yerr`` named parameters.
- :meth:`figure.bar() <plotext._plotter.plot.plot_class.bar>` accepts a list of :ref:`markers <marker_objects>`, one per bar, so each bar can carry its own color, as :meth:`figure.signal() <plotext._plotter.plot.plot_class.signal>` already accepts one per point; a shorter list repeats. Version 5 painted every bar of a call the same, as asked in `Issue 204 <https://github.com/piccolomo/plotext/issues/204>`_.
- Its ``labeled`` parameter takes a list beside ``True``, writing your own text in each bar instead of its height, each entry a string, a :ref:`colorize <colorize>` or a :ref:`matrix <matrix>`; grouped and stacked bars take one such list per series, as the heights are given.
- Every plotting method returns a :ref:`signal <signal>` and draws nothing by itself: :meth:`figure.draw() <plotext._plotter.plot.plot_class.draw>` puts it on the plot. :meth:`figure.line() <plotext._plotter.plot.plot_class.line>` and :meth:`figure.event() <plotext._plotter.plot.plot_class.event>` reach the plot on their own instead, since they draw across the whole canvas rather than at data points.


The Signal
^^^^^^^^^^

**New**

- The :ref:`signal <signal>` is the object every plotting method returns, configured before being drawn: :meth:`signal.lines() <plotext._signal.signal.signal_class.lines>` and :meth:`signal.line() <plotext._signal.signal.signal_class.line>` for the connecting lines, :meth:`signal.fillx() <plotext._signal.signal.signal_class.fillx>`, :meth:`signal.filly() <plotext._signal.signal.signal_class.filly>` and :meth:`signal.fill() <plotext._signal.signal.signal_class.fill>` for the fills, :meth:`signal.label() <plotext._signal.signal.signal_class.label>` for the legend entry.
- :meth:`signal.density() <plotext._signal.signal.signal_class.density>` chooses how densely the connecting and filling lines are drawn, *simple* or *full*, on the lines, the fills or both.

**Changed**

- The ``fillx`` and ``filly`` parameters of version 5 accepted ``True``, a number or the word *internal*; :meth:`signal.fillx() <plotext._signal.signal.signal_class.fillx>` and :meth:`signal.filly() <plotext._signal.signal.signal_class.filly>` now take a boolean alone, and a varying fill level comes from :meth:`signal.fill() <plotext._signal.signal.signal_class.fill>`, given another signal.


Axes and Rulers
^^^^^^^^^^^^^^^

**Renamed**

- ``xlim()``, ``ylim()``, ``xscale()``, ``yscale()``, ``xticks()``, ``yticks()``, ``xfrequency()`` and ``yfrequency()`` become methods of the :ref:`ruler <rulers>` returned by :meth:`figure.ruler() <plotext._plotter.plot.plot_class.ruler>`: :meth:`ruler().lim() <plotext._plotter.frame.ruler.ruler_class.lim>`, :meth:`ruler().scale() <plotext._plotter.frame.ruler.ruler_class.scale>`, :meth:`ruler().ticks() <plotext._plotter.frame.ruler.ruler_class.ticks>` and :meth:`ruler().frequency() <plotext._plotter.frame.ruler.ruler_class.frequency>`.
- ``xreverse()`` and ``yreverse()`` become :meth:`ruler().direction() <plotext._plotter.frame.ruler.ruler_class.direction>`, taking ``1`` or ``-1``.
- ``grid()`` becomes :meth:`ruler().grid() <plotext._plotter.frame.ruler.ruler_class.grid>`, so that each axis carries its own lines, with their style and colors.
- ``frame()``, ``xaxes()`` and ``yaxes()`` become one :meth:`figure.axes() <plotext._plotter.plot.plot_class.axes>` method, acting on all four sides by default.

**New**

- :meth:`ruler().alignment() <plotext._plotter.frame.ruler.ruler_class.alignment>` sets where the axis limits sit inside their cells, and where each tick label sits with respect to its position.
- :meth:`ruler().pixel() <plotext._plotter.frame.ruler.ruler_class.pixel>` colors the tick labels and the strip they sit in; :meth:`ruler().clear() <plotext._plotter.frame.ruler.ruler_class.clear>` resets the selected rulers alone.

**Changed**

- One call reaches several axes at once: the ``axis`` and ``side`` parameters accept a list, or the word *both*, so ``figure.ruler("both", "both")`` addresses all four rulers.


Labels and Legend
^^^^^^^^^^^^^^^^^

**Renamed**

- ``xlabel()`` and ``ylabel()`` become one :meth:`figure.label() <plotext._plotter.plot.plot_class.label>` method, taking the axis and side.

**Changed**

- The :ref:`legend <legend>` appears on its own as soon as a signal, or a line, carries a label, and lists only what is labelled; version 5 listed every drawn signal, naming the unlabelled ones ``signal[n]``. :meth:`figure.legend() <plotext._plotter.plot.plot_class.legend>` is now needed only to place it, color it, draw its box in another :ref:`line style <line_styles>`, or hide it with ``active = False``.
- :meth:`figure.title() <plotext._plotter.plot.plot_class.title>` and :meth:`figure.label() <plotext._plotter.plot.plot_class.label>` accept a :ref:`colorize <colorize>` or a :ref:`matrix <matrix>` object beside a plain string, so that the animated text of :func:`plotext.effect() <plotext.effect>` can be used as a title.
- The signal :meth:`label() <plotext._signal.signal.signal_class.label>` accepts them too, so one legend entry can carry more than one color; the colors are no longer counted as characters, which in version 5 widened the legend box and pushed a centered label off center, as reported in `Issue 144 <https://github.com/piccolomo/plotext/issues/144>`_.


Colors and Styling
^^^^^^^^^^^^^^^^^^

**Renamed**

- The ``color``, ``style`` and ``background`` parameters, scattered across the version 5 methods, become one ``pixel`` parameter, taking a :ref:`pixel <pixel>` object, a bare color, or a ``(foreground, background, style)`` tuple.
- ``canvas_color()`` becomes :meth:`figure.canvas() <plotext._plotter.plot.plot_class.canvas>`, taking a background color alone, since the canvas holds no characters of its own.
- That color may be ``default``, which leaves the canvas **unpainted**, so a plot drawn inside another program keeps whatever is behind it, as asked in `Issue 230 <https://github.com/piccolomo/plotext/issues/230>`_.
- ``axes_color()``, ``ticks_color()`` and ``ticks_style()`` become the pixel of each element: :meth:`figure.axes() <plotext._plotter.plot.plot_class.axes>`, :meth:`ruler().pixel() <plotext._plotter.frame.ruler.ruler_class.pixel>` and :meth:`figure.legend() <plotext._plotter.plot.plot_class.legend>`.

**New**

- :func:`plotext.add_theme() <plotext.add_theme>` registers a custom theme, from its canvas background, its text pixel, its color sequence and its grid pixel, ready to be applied like a built-in one.
- :func:`plotext.line_styles() <plotext.line_styles>` previews the five line styles.

**Changed**

- :meth:`figure.theme() <plotext._plotter.plot.plot_class.theme>` colors the grid lines too, which stayed blue under every version 5 theme.
- The *default* theme is literally the out of the box look, so that applying it leaves a fresh figure untouched.
- Several styles combine in one string, as ``"bold italic"``.


Shapes and Text
^^^^^^^^^^^^^^^

**Renamed**

- ``vertical_line()`` and ``horizontal_line()`` become one :meth:`figure.line() <plotext._plotter.plot.plot_class.line>` method, taking the position and the orientation, and gaining a ``style`` parameter, so the line is no longer always ``─``, as asked in `Issue 145 <https://github.com/piccolomo/plotext/issues/145>`_.

**New**

- :meth:`figure.segment() <plotext._plotter.plot.plot_class.segment>` draws a straight line between two points.
- :meth:`figure.rectangle() <plotext._plotter.plot.plot_class.rectangle>` takes a ``label``, written centered inside it, with colors picked automatically; :meth:`figure.polygon() <plotext._plotter.plot.plot_class.polygon>` takes ``up``, placing a vertex or a flat side on top.

**Changed**

- :meth:`figure.text() <plotext._plotter.plot.plot_class.text>` loses its ``color``, ``background`` and ``style`` parameters: a :ref:`colorize <colorize>` label carries its own colors.
- The :ref:`line styles <line_styles>` are named *default*, *double*, *heavy*, *dotted* and *rounded*, the last one available on the axes alone.


Dates
^^^^^

**Renamed**

- The nine date functions of version 5, ``date_form()``, ``set_time0()``, ``today_datetime()``, ``today_string()``, ``datetime_to_string()``, ``datetimes_to_strings()``, ``string_to_datetime()``, ``string_to_time()`` and ``strings_to_time()``, become the six methods of the date selection returned by :meth:`figure.date() <plotext._plotter.plot.plot_class.date>`: :meth:`date().activate() <plotext._plotter.frame.date.date_class.activate>`, :meth:`date().convert() <plotext._plotter.frame.date.date_class.convert>`, :meth:`date().today() <plotext._plotter.frame.date.date_class.today>`, :meth:`date().origin() <plotext._plotter.frame.date.date_class.origin>`, :meth:`date().active() <plotext._plotter.frame.date.date_class.active>` and :meth:`date().clear() <plotext._plotter.frame.date.date_class.clear>`.

**Changed**

- Date support belongs to one axis, turned on by :meth:`date().activate() <plotext._plotter.frame.date.date_class.activate>`, which also takes the date form and the time origin; that axis then accepts strings, timestamps and datetime objects alike, with no separate date plotting method.
- A date axis is written in a **zone of its own**, set by the ``zone`` parameter of :meth:`date().activate() <plotext._plotter.frame.date.date_class.activate>` as the hours from UTC, where version 5 always wrote UTC, as reported in `Issue 193 <https://github.com/piccolomo/plotext/issues/193>`_.
- The colors of a candle, green when the price rises and red when it falls, are named in the defaults, ``candlestick_up_color`` and ``candlestick_down_color``, so a :doc:`theme <theme>` of your own can change them once for every plot.


Media
^^^^^

**Renamed**

- ``play_gif()`` becomes :func:`plotext.gif() <plotext.gif>` and ``play_video()`` becomes :func:`plotext.video() <plotext.video>`.

**Removed**

- ``play_youtube()`` and ``get_youtube()``: a YouTube address given to :func:`plotext.video() <plotext.video>` plays through `yt-dlp <https://github.com/yt-dlp/yt-dlp>`_ directly.

**New**

- :func:`plotext.image() <plotext.image>` paints an image into a :ref:`matrix <matrix>`, printed as it is, roughly five to ten times faster than :meth:`figure.image() <plotext._plotter.plot.plot_class.image>`.
- The media methods take ``gray``, ``width``, ``height`` and ``ratio``, and the animated ones ``loop`` and ``seconds``, stopping the playback after a given time.

**Changed**

- Any path may be a url: the file is downloaded once, into a plotext folder inside the system temporary one, and reused on later calls.
- A missing optional package now prints a clear message naming the extra to install, instead of failing on the first use.
- :meth:`figure.image() <plotext._plotter.plot.plot_class.image>` shrinks the picture to the size of the whole figure rather than to the terminal size, so a picture drawn inside a :ref:`subplot <subplots>` taller than the terminal fills it instead of coming out with blank rows between its lines.


Subplots and Sizing
^^^^^^^^^^^^^^^^^^^

**Removed**

- ``main()`` and ``active()``: a subplot is reached by :meth:`figure.subplot() <plotext._plotter.plot.plot_class.subplot>` and used directly, while :meth:`figure.master() <plotext._plotter.plot.plot_class.master>`, :meth:`figure.parent() <plotext._plotter.plot.plot_class.parent>`, :meth:`figure.position() <plotext._plotter.plot.plot_class.position>`, :meth:`figure.size() <plotext._plotter.plot.plot_class.size>` and :meth:`figure.log() <plotext._plotter.plot.plot_class.log>` navigate and inspect the tree.
- ``take_min()``: the same choice is now the ``policy`` parameter of :meth:`figure.plot_size() <plotext._plotter.plot.plot_class.plot_size>`, *minimum* or *maximum*.

**Renamed**

- ``limit_size()`` becomes :meth:`terminal.limit() <plotext._kernel.terminal.terminal.limit>`.

**Changed**

- :meth:`figure.plot_size() <plotext._plotter.plot.plot_class.plot_size>` gains ``direction``, deciding which subplot absorbs the space left over, and ``policy``, deciding how disagreeing subplots are harmonized.


Clearing
^^^^^^^^

**Renamed**

- ``clear_figure()`` becomes :meth:`figure.clear() <plotext._plotter.clear.clear_class.all>`, ``clear_data()`` becomes :meth:`clear.data() <plotext._plotter.clear.clear_class.data>`, ``clear_color()`` becomes :meth:`clear.pixels() <plotext._plotter.clear.clear_class.pixels>` and ``clear_terminal()`` becomes :meth:`terminal.clean() <plotext._kernel.terminal.terminal.clean>`.

**New**

- :meth:`clear.settings() <plotext._plotter.clear.clear_class.settings>`, :meth:`clear.styles() <plotext._plotter.clear.clear_class.styles>`, :meth:`clear.size() <plotext._plotter.clear.clear_class.size>` and :meth:`clear.subplots() <plotext._plotter.clear.clear_class.subplots>` reset one aspect of the plot each, leaving the rest untouched.

**Changed**

- Clearing the figure no longer resets the :doc:`terminal <terminal>` settings: the :ref:`prompt height <prompt_height>` and the :ref:`size limits <size_limits>` survive a :meth:`figure.clear() <plotext._plotter.clear.clear_class.all>`, so a loop that clears and redraws keeps them, and only :meth:`terminal.clear() <plotext._kernel.terminal.terminal.clear>` puts them back to their defaults.


Rendering and Saving
^^^^^^^^^^^^^^^^^^^^

**Renamed**

- ``save_fig()`` becomes :meth:`matrix.save() <plotext.matrix.save>`, called on the matrix that :meth:`figure.build() <plotext._plotter.plot.plot_class.build>` gives back, as in ``figure.build().save("plot.html")``; the format follows the extension, *html*, *ansi* or plain text.
- ``interactive()`` becomes :meth:`figure.interactive() <plotext._plotter.plot.plot_class.interactive>`.
- ``time()`` becomes :meth:`figure.time() <plotext._plotter.plot.plot_class.time>`, printing the duration of each rendering step, subplots included.

**Changed**

- :meth:`figure.build() <plotext._plotter.plot.plot_class.build>` gives back a :ref:`matrix <matrix>` instead of a string, so that the plot can be sliced, stacked, saved or turned into a web page.
- A plot saved as ``html`` is a **whole web page**, naming the character set and a monospaced font, so a browser draws it as the terminal does; version 5 wrote the colored block alone, which a browser read with a guessed character set and a proportional font, as reported in `Issue 215 <https://github.com/piccolomo/plotext/issues/215>`_. :meth:`matrix.html() <plotext.matrix.html>` still gives that block alone, to sit inside a page of your own.
- :func:`plotext.sleep() <plotext.sleep>` returns nothing, where version 5 gave back the seconds slept.


Files and Utilities
^^^^^^^^^^^^^^^^^^^

**Renamed**

- ``parent_folder()``, ``join_paths()``, ``save_text()``, ``read_data()``, ``write_data()``, ``download()`` and ``delete_file()`` become the methods of the :ref:`file toolkit <file_api>`: :meth:`file.parent() <plotext._methods.file.file_class.parent>`, :meth:`file.join() <plotext._methods.file.file_class.join>`, :meth:`file.write() <plotext._methods.file.file_class.write>`, :meth:`file.csv() <plotext._methods.file.file_class.csv>`, :meth:`file.string() <plotext._methods.file.file_class.string>`, :meth:`file.download() <plotext._methods.file.file_class.download>` and :meth:`file.delete() <plotext._methods.file.file_class.delete>`, plus :meth:`file.read() <plotext._methods.file.file_class.read>` and :meth:`file.exists() <plotext._methods.file.file_class.exists>`.
- With :meth:`file.delete() <plotext._methods.file.file_class.delete>`, only files inside the folder the program runs in can be removed; anything outside is refused with a note, unless ``safe = False`` is passed. Version 5 removed whatever path it was handed, as asked in `Issue 234 <https://github.com/piccolomo/plotext/issues/234>`_.
- ``terminal_size()``, ``terminal_width()`` and ``terminal_height()`` become :meth:`terminal.size() <plotext._kernel.terminal.terminal.size>`, giving both dimensions.
- ``from_matplotlib()`` becomes :func:`plotext.matplotlib() <plotext.matplotlib>`, turning a matplotlib figure into the plotext one.

**Removed**

- ``transpose()`` and ``script_folder()``; the folder of the running script is given by :meth:`file.parent() <plotext._methods.file.file_class.parent>` called with no argument.
- Every short alias: version 6 defines none at all, so ``clf``, ``cld``, ``clc``, ``clt``, ``cmatrix``, ``datetimes_to_string``, ``eventplot``, ``hline``, ``vline``, ``limitsize``, ``plotsize``, ``savefig``, ``takemin``, ``ts``, ``tw`` and ``th`` are gone, each method having one name only.

**New**

- :func:`plotext.noise() <plotext.noise>` generates gaussian test data, and :func:`plotext.sample() <plotext.sample>` gives the path of a file shipped with the package: *pizzas*, *stock*, *puppy* and *shaq*.
- :meth:`terminal.is_pressed() <plotext._kernel.terminal.terminal.is_pressed>` tells whether a key was typed, without pausing the program, and :meth:`terminal.prompt() <plotext._kernel.terminal.terminal.prompt>` sets the rows left free below the plot, two by default, so a plot no longer runs under the prompt, as asked in `Issue 181 <https://github.com/piccolomo/plotext/issues/181>`_.
- :func:`plotext.effect() <plotext.effect>` colors a text with a moving effect, *shimmer*, *pulse*, *rainbow* or *gradient*, animated by its ``step`` parameter.

**Changed**

- :func:`plotext.sin() <plotext.sin>` gains an ``offset`` parameter; the file methods take a ``log`` parameter, printing a short report of the operation; :func:`plotext.uncolorize() <plotext.uncolorize>` accepts a colorize or a matrix object beside a string.


Documentation
^^^^^^^^^^^^^

**New**

- The :doc:`prettydoc <prettydoc>` module builds the colored docstrings, and the whole documentation of the package is written with it.
- ``plotext.doc`` holds every docstring: ``plotext.doc.bar()`` prints one, and ``plotext.doc()`` opens the interactive menu, three scrollable columns holding the sections, the methods and the docstring of the picked one.
- Every documented method gains a ``doc()`` method of its own, printing its colored docstring, while its ``__doc__`` keeps the plain one.

**Changed**

- :func:`plotext.test() <plotext.test>` no longer draws a sample plot: it runs the **test suite** of the package, over the primitives, the built plots, the dates and every bug already fixed, plus a few whole plots frozen by their hash; :func:`plotext.prettydoc.test() <plotext.prettydoc.test>` runs the one of :doc:`prettydoc <prettydoc>`.


Command Line
^^^^^^^^^^^^

**Changed**

- The :doc:`command line <cli>` tool is rewritten: the version 5 subcommands, ``scatter``, ``plot``, ``plotter``, ``bar``, ``hist``, ``image``, ``gif``, ``video`` and ``youtube``, each with its own flags, are replaced by a chain of methods mirroring the Python ones, as ``plotext --figure --sin --signal --lines --draw --show``.

**New**

- A method is written as ``--`` followed by its name; the words after it are its arguments, and ``name=value`` sets a named parameter.
- ``--figure`` and ``--terminal`` select the object the following methods act on; ``--draw`` puts the waiting signal on the plot, and ``--show`` renders the figure.
- ``@path:<path>`` reads a csv file, on disk or at a url, with the endings ``:2``, ``:1,3`` and ``:dict``; ``@sample:<name>`` reads a bundled sample; ``-`` reads the piped input.
- The test data functions feed the next plotting method: ``--sin --signal`` draws a sinusoid, and ``--sin periods=1 --sin periods=2 --signal`` hands the two waves to the same call.
- ``--doc`` opens the documentation menu, ``--method --doc`` prints one docstring, and ``--methods`` lists every reachable method.
- ``plotext -c "<code>"`` runs Python code directly, for the cases the chain cannot express.

**Removed**

- TAB completion of the command names, which version 5 offered through the `shtab <https://github.com/iterative/shtab>`_ package: the tool no longer reads a fixed list of subcommands, so the completions have to be written again for the new chain of methods.


Version 5.3
-----------
Available on `Plotext GitHub 5.30 <https://github.com/piccolomo/plotext/releases/tag/5.3.0>`_ only.

**Documentation Updates**

- All docstrings updated.
- The colored docstrings of all methods can now be easily printed using a dedicated ``.doc()`` internal method. For example, ``plotext.scatter.doc()`` will print the colorized docstring of the ``scatter()`` function.

**Function and Parameter Renaming**

- Renamed ``text`` parameter to ``label`` in the ``text()`` method.
- Renamed ``label`` parameter to ``labels`` in the ``multiple_bar()`` and ``stacked_bar()`` functions.
- Renamed ``fullground`` parameter to ``color`` in the ``colorize()`` method.
- Renamed ``datetimes_to_string()`` method to ``datetimes_to_strings()``.

**Function Modifications**

- Removed ``trend`` parameter from the ``indicator()`` function.
- Added ``log`` and ``header`` parameters to the ``read_data()`` method.
- Changed text default alignment to ``center`` in the ``text()`` method.

**New Feature**

- Added ``boxplot`` as requested in `Issue 169 <https://github.com/piccolomo/plotext/issues/169>`_ and proposed in `Pull Request 170 <https://github.com/piccolomo/plotext/pull/170>`_.


Version 5.2
-----------

version 5.2.8
^^^^^^^^^^^^^
Published on `PyPI <https://pypi.org/project/plotext/5.2.8/>`_

**Bug Fixes**

- Solved `Issue 153 <https://github.com/piccolomo/plotext/issues/153>`_ allowing bar plots with zero datasets.
- Solved `Issue 151 <https://github.com/piccolomo/plotext/issues/151>`_ regarding nested subplot inheritance.
- Addressed `Issue 142 <https://github.com/piccolomo/plotext/issues/142>`_ by removing side symbols (e.g., ⅃) in legends for single datasets.
- Fixed bar plot issue due to max number of subplots (`Issue 150 <https://github.com/piccolomo/plotext/issues/150>`_).

**Enhancements**

- Added date-time support for ``xlim()`` and ``ylim()``, fixing `Issue 138 <https://github.com/piccolomo/plotext/issues/138>`_.
- Added ``marker`` parameter to ``from_matplotlib()``, solving `Issue 134 <https://github.com/piccolomo/plotext/issues/134>`_.


versions < 5.2.8 
^^^^^^^^^^^^^^^^

**New Features**

- Added ``indicator()`` function as requested in `Issue 121 <https://github.com/piccolomo/plotext/issues/121>`_.
- Added ``interactive()`` function as requested in `Issue 115 <https://github.com/piccolomo/plotext/issues/115>`_.
- Added ``confusion_matrix()`` function as requested in `Issue 113 <https://github.com/piccolomo/plotext/issues/113>`_.
- Added ``square()`` function as requested in `Issue 108 <https://github.com/piccolomo/plotext/issues/108>`_.
- Added ``simple_bar()``, ``simple_multiple_bar()``, and ``simple_stacked_bar()`` functions as requested in `Issue 98 <https://github.com/piccolomo/plotext/issues/98>`_.
- Added ``xreverse()`` and ``yreverse()`` functions as requested in `Issue 86 <https://github.com/piccolomo/plotext/issues/86>`_.
- Added ``polygon()`` and ``rectangle()`` functions.
- Added ``append`` parameter to the ``save_fig()`` function as requested in `Issue 109 <https://github.com/piccolomo/plotext/issues/109>`_.
- Introduced ``background`` color option in the ``text()`` function.
- Introduced ``shtab`` optional dependency as discussed in `Pull Request 118 <https://github.com/piccolomo/plotext/pull/118>`_.

**Improvements**

- Improved handling of ``Nan`` and ``None`` values in the data, as requested in `Issue 114 <https://github.com/piccolomo/plotext/issues/114>`_.
- Simplified bar ticks creation and added ``reset_ticks`` parameter to optionally disable default ticks creation.
- Enhanced functionality of ``fillx`` and ``filly`` parameters to accept ``True``, ``False``, numerical values, and ``"internal"`` for more flexible filling options.
- Updated code structure:
- Introduced ``_global.py`` and ``_matrix.py`` files.
- Changed ``_utility`` folder to a single file.
- Introduced ``_dict.py`` file containing long dictionaries related to markers, colors, styles, and themes.
- Introduced ``_build.py`` to handle the long ``build_plot()`` function separately.

**Fixes**

- Fixed legend symbol for braille markers, merging `Pull Request 135 <https://github.com/piccolomo/plotext/pull/135>`_.
- Allowed compatibility with Python 3.7, resolving `Issue 130 <https://github.com/piccolomo/plotext/issues/130>`_.
- Enabled new line ``'\n'`` in ``text()`` to properly plot, addressing `Issue 127 <https://github.com/piccolomo/plotext/issues/127>`_.
- Enabled TAB completion in command line tool, as discussed in `Pull Request 126 <https://github.com/piccolomo/plotext/pull/126>`_.
- Solved incorrect definitions of ``xlim()`` and ``ylim()``, fixing `Issue 112 <https://github.com/piccolomo/plotext/issues/112>`_ and `Issue 123 <https://github.com/piccolomo/plotext/issues/123>`_.
- Removed ``version()`` function; it is now represented as simply ``version`` value.

**Other Changes**

- Integrated changes from `Pull Request 107 <https://github.com/piccolomo/plotext/pull/107>`_ related to allowing ``plotext`` with ``python -m`` flag.
- Removed memory of past plotted bars in bar functions; bars can now have negative values.
- Code reorganized for improved maintainability.


Version 5.1
-----------
This version is available on `Plotext GitHub 5.1.0 <https://github.com/piccolomo/plotext/releases/tag/5.1.0>`_ only.

**New Features**

- Added ``error()`` function as requested in `Issue 91 <https://github.com/piccolomo/plotext/issues/91>`_.
- Added ``--lines`` flag in the command line tool to handle large data sets.
- Added ``--xcolumn`` and ``--ycolumns`` flags to easily set the ``x`` and ``y`` data from the data table.
- Added ``log`` parameter to most of the `file functions <https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities>`_.
- Introduced 4 x 2 ``braille`` markers, as requested in `Issue 89 <https://github.com/piccolomo/plotext/issues/89>`_.

**Improvements**

- Corrected and integrated all ``.md`` files.
- Test files are now available online rather than being downloaded during installation, reducing package size.
- Added ``--path`` flag to the command line tool, replacing the ``--file`` flag.
- Improved handling of small axis numerical ticks in exponential form and in ``log`` scale, solving `Issue 90 <https://github.com/piccolomo/plotext/issues/90>`_.
- Changed default bar marker to ``hd``, addressing `Issue 96 <https://github.com/piccolomo/plotext/issues/96>`_.

**Fixes**

- Solved issue with consecutive calls to ``show()`` function causing problems with text plots, as detailed in `Issue 94 <https://github.com/piccolomo/plotext/issues/94>`_.


Version 5.0
-----------

**Improvements**

- Added ``play_gif()``, ``play_video()``, ``play_youtube()``, ``download()``, and ``get_youtube()`` functions to play GIFs and videos.
- Rewritten command line tool for enhanced functionality.
- Added :meth:`~plotext._plotter.plot.plot_class.candlestick` plot function.
- Introduced new logic for creating a matrix of subplots, allowing nested sub-matrices and settings propagation from top to bottom levels.
- Added ``take_min()`` function.
- Improved plotting performance, up to 5 times faster for small data and 2 times faster for long data (performance varies by machine).
- Replaced ``xaxis()`` with ``xaxes()`` and ``yaxis()`` with ``yaxes()`` to set the presence of both axes simultaneously without needing the ``xside`` parameter.
- Added ``ticks_style()`` function to customize tick styles.
- Added :meth:`~plotext._plotter.plot.plot_class.theme` function for setting plot themes.
- Introduced ``fast`` parameter in ``matrix_plot()`` and ``image_plot()`` for faster plotting.
- Added :meth:`~plotext._plotter.plot.plot_class.text` function to add string labels to the plot.
- Added ``keep_colors`` parameter in ``save_fig()`` to retain ANSI color codes in ``txt`` files (viewable with ``less -R file_path.txt``).
- Introduced ``event_plot()`` inspired by `Issue 83 <https://github.com/piccolomo/plotext/issues/83>`_.
- Simplified string color codes.
- ``xside`` and ``yside`` parameters can now accept 1 and 2 for simplified usage.
- Larger plots are now handled outside of ``ipython``, which prints an extra line or two.

**Bug Fixes**

- Added the back-end function ``from_matplotlib()``, as requested in `Issue 75 <https://github.com/piccolomo/plotext/issues/75>`_.
- Solved `Issue 90 <https://github.com/piccolomo/plotext/issues/90>`_ to plot small axis numerical ticks in exponential form and in `log` scale.
- Solved `Issue 94 <https://github.com/piccolomo/plotext/issues/94>`_ caused by consecutive calls to the :meth:`~plotext._plotter.plot.plot_class.show` function with text plots.
- Changed the default bar marker to ``hd`` to address `Issue 96 <https://github.com/piccolomo/plotext/issues/96>`_.

**Deprecations and Removals**

- Removed ``span()`` function.
- Removed ``clear_plot()`` function; ``clear_figure()`` now handles its functionality based on the subplot matrix level.
- Removed ``colorless()`` function; ``clear_color()`` now handles its functionality based on the subplot matrix level.
- Removed ``size``, ``keep_ratio``, and ``resample`` parameters from ``image_plot()``.
- Removed ``plot_date()`` and ``scatter_date()`` functions; date/time plots are now handled by ``plot()`` and ``scatter()``.
- Removed file class; all related tools have been moved to a normal level.
- Removed date-time class; all tools rewritten and moved to a normal level.

**Refactoring**

- Rewritten entire code for improved performance and maintainability.
- Introduced ``input_form`` and ``output_form`` for handling date/time string objects.
- Introduced ``test()`` function for improved testing capabilities.


Version 4.3
-----------
- Accounted for exponential float notation as requested in `Pull 82 <https://github.com/piccolomo/plotext/pull/82>`_.
- Added functionality to properly read ``numpy`` data as requested in `Issue 84 <https://github.com/piccolomo/plotext/issues/84>`_ and `Issue 85 <https://github.com/piccolomo/plotext/issues/85>`_.


Version 4.2
-----------
- Added ``norm`` parameter in :meth:`~plotext._plotter.plot.plot_class.hist` function as requested in `Issue 76 <https://github.com/piccolomo/plotext/issues/76>`_ and incorporated changes from `Pull 79 <https://github.com/piccolomo/plotext/pull/79>`_.


Version 4.1
-----------

**Improvements**

- Added ``horizontal_line`` and ``vertical_line`` functions, as requested in `Issue 65 <https://github.com/piccolomo/plotext/issues/65>`_.
- The plotting functions now handle non-numerical values by excluding them from plots, as requested in `Issue 65 <https://github.com/piccolomo/plotext/issues/65>`_.
- Added command line tool discussed in `Issue 47 <https://github.com/piccolomo/plotext/issues/47>`_, `Pull 57 <https://github.com/piccolomo/plotext/pull/57>`_, `Pull 52 <https://github.com/piccolomo/plotext/pull/52>`_, and `Pull 51 <https://github.com/piccolomo/plotext/pull/51>`_.
- Added guide for integration with package ``rich``, as discussed in `Issue 26 <https://github.com/piccolomo/plotext/issues/26>`_.
- Added guide for integration with ``tkinter``, as discussed in `Issue 33 <https://github.com/piccolomo/plotext/issues/33>`_.

**Bug Fixes**

- Solved single bar plot error discussed in `Issue 63 <https://github.com/piccolomo/plotext/issues/63>`_.
- Fixed bar error reported in `Issue 61 <https://github.com/piccolomo/plotext/issues/61>`_.
- Added exception handling when subplot size exceeds default, as noted in `Issue 60 <https://github.com/piccolomo/plotext/issues/60>`_.
- Removed ``shell`` function and parameter as they were deemed useless.

**Miscellaneous**

- Set default marker to ``hd`` to avoid complications with ``fhd`` marker in some terminals, as noted in `Issue 62 <https://github.com/piccolomo/plotext/issues/62>`_.
- Changed default canvas background color back to ``bright-white``.
- Made ``pillow`` an optional dependency, as requested in `Issue 56 <https://github.com/piccolomo/plotext/issues/56>`_.
- Removed ``numpy`` as a dependency (not even optional).
- Changed ``platform`` function as recommended in `Issue 55 <https://github.com/piccolomo/plotext/issues/55>`_.
- Corrected and integrated all ``.md`` files.


Version 4.0
-----------

**Improvements**

- Entire code re-written for better performance.
- Improved plotting speed.
- Changed 2 x 2 marker to ``hd`` (high resolution) instead of ``small``.
- Added higher resolution 3 x 2 Unicode mosaic markers (not available in Windows), called ``fhd`` (full high resolution).
- Added new color codes, including 256 color codes and full RGB colors.
- Introduced multiple and stacked bar charts.
- Added date-time scatter and plot functions.
- Added date-time class for better handling of date-time objects.
- Added ``matrix_plot()`` and ``image_plot()`` functions.
- Plots can now be saved in color using ``.html`` extension.
- Added file class for better file and path handling.
- Data can now be plotted on the upper *x* axis.
- Added ``unittest`` file named ``test.py``.
- Introduced ``xside`` and ``yside`` parameters for many related functions.
- Added ``span()`` function to span columns and rows in the matrix of subplots.
- Added more ``clear`` functions.
- Added ``limit_size()`` function to control plot dimensions relative to terminal size, inspired by `Issue 33 <https://github.com/piccolomo/plotext/issues/33>`_.
- Added optional legend extra characters for axis identification.
- Added ``time()`` function to check plotting computational time.
- Renamed ``xfreq()`` to ``xfrequency()`` and ``yfreq()`` to ``yfrequency()``.
- Added doc class for easy access to function docstrings.
- Renamed ``get_canvas()`` to ``build()``.
- Reinstated ``frame()`` function.

**Bug Fixes**

- Solved bar chart log scale issue on both axes.
- Solved bar chart zero value issue.


Version 3.1
-----------
- Fixed plot resizing issue discussed in `Issue 23 <https://github.com/piccolomo/plotext/issues/23>`_.
- Added ``clear_data()`` and ``test()`` functions.


Version 3.0
-----------
- Re-written most of the code.
- Added direct terminal command line tool (first type).
- Introduced ``"small"`` marker with improved resolution, and new marker codes.
- Added matrix of subplots.
- Added log plots, stem plot, and double ``y`` axes plot.
- Added bar plot and date/time plot functions.
- Added ``get_canvas()`` and ``sin()`` functions.
- Added ``clear_figure()`` function.
- Changed ``figsize()`` to ``plotsize()``.
- Renamed ``nocolor()`` to ``colorless()``.
- Replaced ``frame()`` function with ``xaxes()`` and ``yaxes()``.


Version 2.3
-----------
- Solved histogram error reported in `Issue 15 <https://github.com/piccolomo/plotext/issues/15>`_.
- Added histogram plot and ``fillx`` and ``filly`` parameters.


Version 2.2
-----------
- Updated ``readme.md`` description file.
- Changed ``fig_size()`` to ``figsize()``, ``facecolor()`` to ``axes_color()``, and ``canvas_size()`` to ``fig_size()``.
- Slightly modified behavior under Windows.
- Introduced new Windows-friendly markers.
- Default color combination for plots instead of colorless.
- Removed ``force_size`` parameter.
- Added ``grid()`` function for optional grid lines.
- Added ``frame()`` function (present by default).
- Streamlined parameters in ``plot`` and ``scatter`` functions.
- Added ``nocolor()`` function and improved line-filling algorithm.
- Added ``clp()`` and ``clt()`` functions for ``clear_plot()`` and ``clear_terminal()``.
- Updated color codes and added ``parameters()`` and ``docstrings()`` functions.


Version 2.1
-----------
- Plot now shows actual data ticks using a simpler algorithm.
- Changed ``ticks_number`` to ``ticks``.
- Updated set functions like ``set_title()`` to ``title()``.
- Added optional grid and ``fill`` parameter.
- Changed ``axes_color()`` to ``facecolor()`` to align with ``matplotlib``.
- Improved legend positioning and introduced new color codes.
- Code restructured and revised.


Version 2.0
-----------
- Plot now shows actual data ticks with improved adaptability.
- Added ``set_xticks()`` and ``set_yticks()`` functions.
- Added labels to axes, titles, and legends for multiple data sets.
- Updated set functions for list parameters to accept different formats.
- Changed ``spacing`` to ``ticks_number``.
- Removed ``equations`` and ``decimals`` parameters.
- Code restructured and revised.


Version 1.0
-----------
- ``plotext`` now works in Windows with colors and Python IDLE3 (without colors and adaptive dimensions).
- Added new color codes with background codes.
- Introduced ``force_size`` parameter.
- Added ``savefig()``, ``get_version()``, and ``run_test()`` functions.
- Removed dependency on ``numpy`` and ``time`` packages.
- Updated code for improved readability and documentation.
- Set ``equations`` parameter to ``False`` by default.
- Removed ``get`` functions for plot parameters.