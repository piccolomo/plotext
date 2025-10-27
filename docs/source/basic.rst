Basic Plots
===========


Scatter Plot
------------

Here is a simple scatter plot, using the :func:`plotext.scatter` function:

.. code-block:: python

    import plotext as plt
    y = plt.sin()  # sinusoidal test signal
    plt.scatter(y)
    plt.title("Scatter Plot")  # to apply a title
    plt.show()  # to finally plot

Or directly on terminal:

.. code-block:: console

    python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Scatter Plot'); plt.show()"

.. image:: https://raw.githubusercontent.com/piccolomo/plotext/master/data/scatter.png
    :alt: scatter

More documentation can be accessed with ``plotext.doc.scatter()``.



Line Plot
---------

For a line plot, use the :func:`plotext.plot` function instead:

.. code-block:: python

   import plotext as plt
   y = plt.sin()
   plt.plot(y)
   plt.title("Line Plot")
   plt.show()

or directly on terminal:

.. code-block:: console

   python3 -c "import plotext as plt; y = plt.sin(); plt.plot(y); plt.title('Line Plot'); plt.show()"

.. image:: https://raw.githubusercontent.com/piccolomo/plotext/master/data/plot.png
   :alt: plot

More documentation can be accessed with :func:`plotext.doc.plot`.


Logarithmic Plot
----------------

For a logarithmic plot, use the :func:`plotext.xruler` (or func:`plotext.yruler`) method, which accepts the parameter ``scale = "log"``  .


Example
-------

.. code-block:: python

    import plotext as plt

    l = 10 ** 4
    y = plt.sin(periods = 2, length = l)

    plt.plot(y)

    plt.xruler(scale = "log", frequency = 5)    # for logarithmic x scale
    plt.yruler(scale = "linear", frequency = 7) # for linear y scale, redundant but shown for completion 
    #plt.grid(0, 1)       # to add vertical grid lines

    plt.title("Logarithmic Plot")
    plt.xlabel("logarithmic scale")
    plt.ylabel("linear scale")

    plt.show()

Or directly on the terminal:

.. code-block:: console

    python3 -c "import plotext as plt; l = 10 ** 4; y = plt.sin(periods=2, length=l); plt.plot(y); plt.xscale('log'); plt.yscale('linear'); plt.grid(0, 1); plt.title('Logarithmic Plot'); plt.xlabel('logarithmic scale'); plt.ylabel('linear scale'); plt.show();"

.. image:: https://raw.githubusercontent.com/piccolomo/plotext/master/data/log.png
   :alt: log

.. note:: The logarithmic function used is ``log10``.



Stem Plot
---------

For a `stem plot <https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html>`_, use either the ``fillx`` or ``filly`` parameters (available for most plotting functions) to fill the canvas with data points up to the ``y = 0`` or ``x = 0`` level, respectively.

Example
-------

.. code-block:: python

    import plotext as plt
    y = plt.sin(length = 50)
    plt.plot(y, fillx = True)
    plt.title("Stem Plot")
    plt.show()

Or directly on the terminal:

.. code-block:: console

    python3 -c "import plotext as plt; y = plt.sin(); plt.plot(y, fillx=True); plt.title('Stem Plot'); plt.show()"

.. image:: images/stem.png
   :alt: stem



Elaborate Stem Plot
~~~~~~~~~~~~~~~~~~~
.. toctree::
   :hidden:

To create more complex stem plots with customized filling levels, use the :func:`plotext.signal` and :func:`plotext.draw` methods, as shown in the following example:

.. code-block:: python

    import plotext as plt

    l = 1000
    signal = plt.signal(plt.sin(length=l, periods=2))
    fill = plt.signal(plt.sin(length=l, periods=2, amplitude=0.3))

    signal.set_fill(fill)

    plt.draw(signal)
    plt.show()

.. image:: images/stem2.png
   :alt: Elaborate Stem Plot


Datetime Plot
-------------

To plot dates and/or times, use the :func:`plt.draw` function directly.  
Before doing so, notify ``plotext`` that you intend to use date values along a specific axis using the :func:`plt.date` function.  
Plotext automatically interprets date and time values from strings, ``datetime`` objects, timestamps (in seconds) or ``pandas.DatetimeIndex``.


Here is an example, which requires the ``yfinance`` package:

.. code-block:: python

    import plotext as plt
    import yfinance as yf

    plt.date(); # or explicitally p.date(axis = 0, side = 0, form = "%d/%m/%Y", active = True); 

    start = plt.convert('11/04/2022', "datetime"); end = plt.convert('22/10/2025', "datetime")
    data = yf.download('GOOG', start = start, end = end, auto_adjust = False, progress = False)

    prices = data[('Close', 'GOOG')]
    dates = data.index # or plt.convert(data.index, "string")

    plt.draw(dates, prices, marker = "fhd", plot = 1)

    plt.title("Google Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Stock Price $")
    plt.show()

.. image:: images/date.png
   :alt: Date and Time Plot

Alternatively, you can run this example directly from the terminal:

.. code-block:: console

   python3 -c "import plotext as plt, yfinance as yf; plt.clf(); plt.date(); start=plt.convert('11/04/2022','datetime'); end=plt.convert('22/10/2025','datetime'); data=yf.download('GOOG', start=start, end=end, auto_adjust=False, progress=False); prices=list(data[('Close','GOOG')]); dates=plt.convert(data.index,'string'); plt.draw(dates, prices, marker='hd', plot=1, fillx=0); plt.title('Google Stock Price'); plt.xlabel('Date'); plt.ylabel('Stock Price ($)'); plt.show()"


.. note::
   By default, ``plotext`` assumes the date format ``"%d/%m/%Y"``.  
   To change this, use the ``form`` parameter within the :func:`plt.date` function.

.. note::
   You can also convert between strings, ``datetime`` objects, and timestamps manually using :func:`plt.convert`.  
   This function automatically detects the input type and allows you to specify the desired output format using the ``output`` parameter.

.. note::
   Functions such as :func:`plt.xticks` and :func:`plt.xlim` can use directly date/time values in whatever form allowed.  
   ``plotext`` will automatically convert them internally to timestamps.







