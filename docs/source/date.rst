Datetime Plot
=============

Basic Plot
----------

To plot datetime objects just notify ``plotext`` that you intend to do so along a specific axis using the :func:`plotext.date` function.  

.. note:: Once notified via :func:`plotext.date`, ``plotext`` automatically recognises the input type and interprets date and time values from strings, ``datetime`` objects (including ``pandas.DatetimeIndex``), or timestamps (seconds from the origin of time).


Here is an example, which requires the ``yfinance`` package:

.. code-block:: python

   import plotext as plt
   import yfinance as yf

   plt.date(axis = 'x') # plt.date() would also work in this case

   start = plt.convert('11/04/2024', "datetime");
   end = plt.convert('22/10/2025', "datetime")
   data = yf.download('GOOG', start = start, end = end, auto_adjust = False, progress = False)

   prices = data[('Close', 'GOOG')]
   dates = data.index # or plt.convert(data.index, "string")

   signal = plt.signal(dates, prices, marker = "fhd").lines()

   plt.draw(signal)

   plt.title("Google Stock Price")
   plt.label("Date", 0)
   plt.label("Stock Price $", 1)
   plt.show()


.. image:: images/date.png
   :alt: Date and Time Plot

.. note::
   By default, ``plotext`` assumes the date format to be ``"%d/%m/%Y"``. To change this, use the ``form`` parameter of :func:`plotext.date`.

.. note::
   The :func:`plotext.convert` function can be used to explicitly convert between strings, ``datetime`` objects, and timestamps (i.e. floats).
   The input type is detected automatically, while the desired output type is specified with the ``output`` parameter.
   Valid output values are ``"datetime"``, ``"timestamp"``, and ``"string"``.


Candlestick Plot
----------------

To plot a candlestick chart, use :func:`plotext.candlestick`. It takes a single dictionary with string keys date, open, close, high, low, where each value is a sequence. 

The function returns a signal that can be further configured (for example with :meth:`.label() <plotext._signal.signal.signal_class.label>`) and then passed to :func:`plotext.draw`.

Here is an example, which requires the ``yfinance`` package:

.. code-block:: python

   import yfinance as yf
   import plotext as plt

   plt.date(axis = "x")                              # treat x as a date axis (default format "%d/%m/%Y")

   start = plt.convert("11/04/2022", "datetime")
   end   = plt.convert("11/06/2022", "datetime")
   data  = yf.download("GOOG", start = start, end = end,
                       auto_adjust = False, progress = False)

   ohlc = {
       "date":  plt.convert(data.index, "string"),
       "open":  data[("Open",  "GOOG")],
       "close": data[("Close", "GOOG")],
       "high":  data[("High",  "GOOG")],
       "low":   data[("Low",   "GOOG")],
   }

   signal = plt.candlestick(ohlc).label("GOOG")
   plt.draw(signal)

   plt.title("Google Stock Price Candlesticks")
   plt.label("Date", "x")
   plt.label("Stock Price $", "y")
   plt.legend(True)
   plt.show()

.. note:: More documentation is available via :code:`plotext.doc.candlestick()`.




