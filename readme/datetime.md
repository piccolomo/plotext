# Datetime Plots

- [Introduction](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#introduction)
- [Datetime Plot](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-plot)
- [Candlestick Plot](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#candlestick-plot)

[Main Guide](https://github.com/piccolomo/plotext#guide)

## Introduction

* Plotting dates or times simply requires passing a list of date-time string objects (such as `"01/01/2000"`, `"12:30:32"` or `"01/01/2000 12:30:32"`) to the plotting functions. 

* To control how `plotext` interprets string as date-time objects use the `date_form(input_form, output_form)` method, where you can change its: 
  
  * `input_form` to control the form of date-time strings inputted by the user,
  
  * `output_form` to control the form of date-time strings outputted by `plotext` (by default equal to `input_form`), including outputted axes date-time ticks.

* The date-time string forms are [the standard ones](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes), with the `%` symbol removed for simplicity; eg: `d/m/Y` (by default), or `d/m/Y H:M:S`.

* Most of the functions that follow allow to set its input and output form independently if needed and possible, with their dedicated parameters.
- To get today in `datetime` or string form use `today_datetime()` and `today_string()` respectively.

- To turn a `datetime` object into a string use `datetime_to_string()` and `datetimes_to_string()` for a list instead. 

- To turn a string to a `datetime` object use `string_to_datetime()`.

- To turn a string to a numerical timestamp use `string_to_time()` and `strings_to_time()` for a list of strings.

- The method `set_time0()` sets the origin of time to the string provided; this function is useful in `log` scale, in order to avoid *hitting* the 0 timestamp,

[Main Guide](https://github.com/piccolomo/plotext#guide), [Datetime Menu](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-plots)

## Datetime Plot

To plot dates and/or times use either `plt.scatter()` or `plt.plot()` functions directly. 

Here is an example, which requires the package `yfinance`:

```python
import yfinance as yf
import plotext as plt

plt.date_form('d/m/Y')

start = plt.string_to_datetime('11/04/2022')
end = plt.today_datetime()
data = yf.download('goog', start, end)

prices = list(data["Close"])
dates = plt.datetimes_to_string(data.index)

plt.plot(dates, prices)

plt.title("Google Stock Price")
plt.xlabel("Date")
plt.ylabel("Stock Price $")
plt.show()
```

or directly on terminal:

```console
python3 -c "import yfinance as yf; import plotext as plt; plt.date_form('d/m/Y'); start = plt.string_to_datetime('11/04/2022'); end = plt.today_datetime(); data = yf.download('goog', start, end); prices = list(data['Close']); dates = plt.datetimes_to_string(data.index); plt.plot(dates, prices); plt.title('Google Stock Price'); plt.xlabel('Date'); plt.ylabel('Stock Price $'); plt.show()"
```

![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/data/datetime.png)

Note that you could easily add [text](https://github.com/piccolomo/plotext/blob/master/readme/other.md#text-plot) and [lines](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-lines) to the plot, as date-time string coordinates are allowed in most plotting functions.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Datetime Menu](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-plots)

## Candlestick Plot

For this kind of plot, use the function `candlestick()`, which requires a list of date-time strings and a dictionary with the following mandatory keys: `'Open'`, `'Close'`, `'High'`, and `'Low'`, where each correspondent value should be a list of prices. 

Here is an example, which requires the package `yfinance`:

```python
import yfinance as yf
import plotext as plt

plt.date_form('d/m/Y')

start = plt.string_to_datetime('11/04/2022')
end = plt.today_datetime()
data = yf.download('goog', start, end)

dates = plt.datetimes_to_string(data.index)

plt.candlestick(dates, data)

plt.title("Google Stock Price CandleSticks")
plt.xlabel("Date")
plt.ylabel("Stock Price $")
plt.show()
```

or directly on terminal:

```console
python3 -c "import yfinance as yf; import plotext as plt; plt.date_form('d/m/Y'); start = plt.string_to_datetime('11/04/2022'); end = plt.today_datetime(); data = yf.download('goog', start, end); dates = plt.datetimes_to_string(data.index); plt.candlestick(dates, data); plt.title('Google Stock Price Candlesticks'); plt.xlabel('Date'); plt.ylabel('Stock Price $'); plt.show()"
```

![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/data/candlestick.png)

More documentation can be accessed with `doc.candlestick()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Datetime Menu](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-plots)
