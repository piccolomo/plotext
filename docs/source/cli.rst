Command Line
============

| Installing |plotext| also installs the ``plotext`` command line tool.
| Typed in the :doc:`terminal <terminal>`, with the right arguments, it draws a plot **directly**, without needing Python code for it.


Method Names
------------

| Any |plotext| method is reached by writing ``--`` followed by its name: for example, a method called ``method()`` becomes ``--method``.
| Hyphens and underscores are interchangeable: ``--method-name`` and ``--method_name`` are the same.


Documentation
-------------

- ``plotext --help`` prints the usage, the value parsing rules and some examples.
- ``plotext --methods`` lists every reachable method, grouped by section.
- ``plotext --doc`` opens the interactive documentation menu, mirroring ``plotext.doc()`` in Python.
- ``plotext --figure --method --doc`` prints the docstring of a single method, as in ``plotext --figure --candlestick --doc``, mirroring ``plotext.doc.<method>()``.


Attributes
----------

The |plotext| attributes are written the same way: for example, an attribute called ``object`` is selected with ``--object``, and the methods after it act on it.

.. note:: Examples of actual attributes are ``--figure``, selecting :class:`plotext.figure <plotext._plotter.plot.plot_class>`, the master figure holding the whole plot, and ``--terminal``, selecting the :doc:`terminal <terminal>` object: for example, ``plotext --terminal --size`` prints the terminal size.

.. caution:: A callable attribute runs as a method: for example, ``--clear`` resets the whole figure, like :meth:`fig.clear() <plotext._plotter.clear.clear_class.all>`, described in the :doc:`clear <clear>` page.

The methods act through a selected attribute, so a plot normally needs ``--figure`` **first** and ``--show`` **last**.

.. note:: The media methods are an exception: ``--image``, ``--gif`` and ``--video`` run directly and display immediately, with no ``--figure`` and no ``--show`` needed at the end; their parameters are described in the :doc:`media <media>` page.


Parameters
----------

| The method arguments follow the method name, separated by spaces: for example, ``method(3, 5)`` becomes ``--method 3 5``.
| A string argument goes without quotes: for example, ``method("hello")`` becomes ``--method hello``.
| A named parameter is written as ``name=value``: for example, ``method(3, bins = 4)`` becomes ``--method 3 bins=4``.

In more detail, one value form at a time:

- **Quoted strings**: a string with spaces needs shell quotes, as in ``--title 'Two series'``.
- **Lists**: square brackets, with no spaces inside, as in ``[1,2,3]`` or ``[a,b,c]``; bare words inside are read as strings.
- **Dictionaries**: written as ``{a:1}``.
- **Special words**: ``True``, ``False`` and ``None`` are written ``true``, ``false`` and ``null``.
- **Numbers and strings**: numbers are read as numbers, anything unrecognized as a string.
- **Named parameters**: the name must match one of the method parameters, or the whole thing is read as a plain string.


.. _cli_data:

Reading Files
-------------

The ``@`` forms are **values, not methods**: they go after the method name, like any other parameter.

Csv Files
~~~~~~~~~

| A method argument written as ``@path:<path>`` is replaced by the **content** of the csv file at that path, either on disk or a :ref:`url <cli_urls>`.
| The file is read with the :meth:`csv() <plotext._methods.file.file_class.csv>` method, described in the :ref:`tabular data <tabular_data>` section: each file column enters the call as one argument.
| An ending ``:1``, or ``:1,2``, picks specific columns, counted from 1: for example, ``@path:data.csv:2`` reads only the second column.
| An ending ``:dict`` uses the first row as keys, giving a dictionary of columns, the form taken by ``--candlestick``.

.. caution:: **Every row is read**, the first included, so a file carrying a header needs it removed first, for example with ``tail -n +2``. The ``:dict`` ending is the exception, wanting that row as its keys. Empty rows are skipped, so a file ending with a new line reads as it should.

Sample Files
~~~~~~~~~~~~

A method argument written as ``@sample:<name>`` is replaced by the content of the :ref:`sample file <sample_files>` with that name: each file column enters the call as one argument, and the ``:1`` and ``:dict`` endings work here too; for the *puppy* image, it gives its file path instead.


.. _cli_urls:

Reading Urls
------------

| A file path can also be a url, starting with ``http://``, ``https://`` or ``ftp://``: the file is downloaded **once**, into a plotext folder inside the system temporary one, and reused on later calls.
| It works for the ``@path`` form and the media paths alike:

.. code-block:: shell

   plotext --figure --signal @path:https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data:1 --lines --draw --show
   plotext --image https://picsum.photos/400/300

.. note:: YouTube urls passed to ``--video`` play through `yt-dlp <https://github.com/yt-dlp/yt-dlp>`_: nothing is saved for later calls, since the stream address it gets from YouTube stops working after a short time.


Piped Input
-----------

| In the :doc:`terminal <terminal>`, ``command1 | command2`` sends the printed output of the first command to the second, and, by standard practice, many tools accept ``-`` in place of a file path, reading the piped data as if it were the file content.
| |plotext| adapts the practice to its data parameters: a method argument written as ``-`` is replaced by the piped data, so any program that prints numbers can **feed a plot** directly, with no file in between.
| For example, ``echo '1 2 3' | plotext --figure --signal - --draw --show`` plots the three numbers, the lone ``-`` after ``--signal`` standing for them.
| A single row of whitespace separated numbers becomes one list.
| On several rows, each printed line is one row of a csv table, with its values separated by spaces or commas: each column then enters the call as one argument, as for the csv files above.
| For example, ``printf '1 4\n2 5\n3 6' | plotext --figure --signal - --draw --show`` pipes three rows of two values each, so two columns, plotting the second against the first.


Chain Syntax
------------

| More methods can follow on the same command, running **in order**, as successive lines of a Python script would.
| Each new ``--method`` ends the arguments of the previous method and starts the call of the new one.
| For example, ``method1(0)`` followed by ``method2("hello")`` is written ``--method1 0 --method2 hello``.


Returned Objects
----------------

| The methods act on the **last returned object**, mirroring the Python dot chaining.
| For example, if ``method1()`` returns an object with its own ``method2()``, then ``--method1 --method2`` is the same as ``method1().method2()``.
| If ``method1()`` returns nothing, ``method2()`` acts on the same object ``method1()`` did.


Data Feed
---------

| When a method returns data, rather than an object, the data feeds the next data accepting method, entering the call as its **leading arguments**: for example, if ``method1()`` returns data, ``--method1 --method2`` is the same as ``method2(method1())``.
| More returned data accumulates, in order, and enters the same call together: for example, if ``method1()`` and ``method2()`` both return data, ``--method1 --method2 --method3`` is the same as ``method3(method1(), method2())``.

.. note:: In |plotext|, the data accepting methods are only the plotting ones, like ``signal()`` or ``bar()``, described in the :doc:`basic plots <basic>` page.

.. caution:: A created signal reaches the plot only through ``--draw``: without it, nothing is drawn.

.. note:: The main use is feeding the :doc:`test data <simulate>` functions to a plot: for example, ``plotext --figure --sin --signal --lines --draw --show`` draws a sinusoid, like ``fig.draw(fig.signal(plt.sin()).lines())`` followed by ``fig.show()`` in Python, while ``plotext --figure --sin periods=1 --sin periods=2 --signal --draw --show`` hands the two waves to ``signal()`` as its *x* and *y* data, like ``fig.draw(fig.signal(plt.sin(periods = 1), plt.sin(periods = 2)))`` followed by ``fig.show()``.


Examples
--------

Each ``plotext`` command starts with a fresh figure, so the ``fig.clear()`` line of the Python versions below has no shell counterpart.

**A basic plot**, in Python and translated in the terminal:

.. code-block:: python

   import plotext as plt

   fig = plt.figure
   fig.clear()
   signal = fig.signal([1, 4, 9, 16, 25])
   signal.lines()
   fig.draw(signal)
   fig.title("Squares")
   fig.show()

.. code-block:: shell

   plotext --figure --signal [1,4,9,16,25] --lines --draw --title Squares --show

**Named parameters** and quoted strings:

.. code-block:: python

   import plotext as plt

   fig = plt.figure
   fig.clear()
   fig.draw(fig.hist(plt.noise(length = 1000), bins = 20))
   fig.title("Noise Distribution")
   fig.show()

.. code-block:: shell

   plotext --figure --noise length=1000 --hist bins=20 --draw --title 'Noise Distribution' --show

**Special words** and nested lists:

.. code-block:: python

   import plotext as plt

   fig = plt.figure
   fig.clear()
   fig.draw(fig.bar(["a", "b", "c"], [[1, 2, 3], [4, 5, 6]], stacked = True))
   fig.show()

.. code-block:: shell

   plotext --figure --bar [a,b,c] [[1,2,3],[4,5,6]] stacked=true --draw --show

**A returned object**, the chain moving onto the ruler:

.. code-block:: python

   import plotext as plt

   fig = plt.figure
   fig.clear()
   fig.ruler("y").lim(-1, 1)
   fig.draw(fig.signal(plt.sin()).lines())
   fig.show()

.. code-block:: shell

   plotext --figure --ruler y --lim -1 1 --sin --signal --lines --draw --show

**Test data** feeding a plot:

.. code-block:: python

   import plotext as plt

   fig = plt.figure
   fig.clear()
   fig.draw(fig.signal(plt.sin(periods = 2)).lines())
   fig.show()

.. code-block:: shell

   plotext --figure --sin periods=2 --signal --lines --draw --show

**A sample file**:

.. code-block:: python

   import plotext as plt

   fig = plt.figure
   fig.clear()
   rows = plt.file.csv(plt.sample("pizzas"))[1:]
   names = [row[0] for row in rows]
   values = [float(row[1]) for row in rows]
   fig.draw(fig.bar(names, values))
   fig.show()

.. code-block:: shell

   plotext --figure --bar @sample:pizzas --draw --show

**A media method**, direct:

.. code-block:: python

   import plotext as plt

   plt.image(plt.sample("puppy"))

.. code-block:: shell

   plotext --image @sample:puppy

**The terminal attribute**:

.. code-block:: python

   import plotext as plt

   print(plt.terminal.size())

.. code-block:: shell

   plotext --terminal --size

.. note:: More examples are printed directly in the :doc:`terminal <terminal>` by ``plotext --help``.


Python Fallback
---------------

| The ``python3 -c "<code>"`` form runs the given Python code **directly**, with no chain syntax involved.
| Use it when the chain syntax cannot express what you need, as in the following cases.

.. code-block:: shell

   python3 -c "import plotext as plt; fig = plt.figure; fig.draw(fig.signal(plt.sin()).lines()); fig.show()"

.. note:: ``python3 -c`` works when |plotext| is installed in that ``python3``. The ``plotext -c "<code>"`` form exists for exactly the case where it is not: with a pipx-style install, |plotext| lives in its own environment, invisible to the plain ``python3``, while the ``plotext`` command always finds its own interpreter.

.. note:: :doc:`Streaming <stream>` loops, and anything else needing real control flow, stay Python only: run their code this way, or write a script.


.. _cli_subplots:

Subplots
--------

For a **flat grid** of :ref:`subplots <subplots>`, with no nesting, the chain syntax works: each ``--subplot`` moves the chain into one subplot, where the following methods act, ``--draw`` included:

.. code-block:: shell

   plotext --figure --subplots 1 2 --subplot 1 1 --sin --signal --lines --draw --title left --subplot 1 2 --noise --hist --draw --title right --show

The same plot, running Python code directly:

.. code-block:: shell

   python3 -c "import plotext as plt; fig = plt.figure; fig.subplots(1, 2); sub = fig.subplot(1, 1); sub.draw(sub.signal(plt.sin()).lines()); sub.title('left'); sub = fig.subplot(1, 2); sub.draw(sub.hist(plt.noise())); sub.title('right'); fig.show()"

A nested grid cannot be expressed by the chain syntax (a grid of subplots inside a subplot): it takes full Python code, as in the command above.

