# Datetime Plots
- [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#utilities)
- [Datetime Plot](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-plot)
- [Candlestick Plot](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#candlestick-plot)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Utilities
`Plotext` has a set of utilities to easily manipulate date-time objects:
- `date_form(input_form, output_form)` sets how its functions interpret string based date-time objects:
    - `input_form` is used to control functions that take date-time strings as input,
    - `output_form` is used to control functions that output date-time strings (by default equal to `input_form`),
- date/time string forms are [the standard ones](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes), with the `%` symbol removed for simplicity; eg: `d/m/Y` (by default), or `d/m/Y H:M:S`,
- `set_time0(date)` sets the origin of time to the date-time string provided; this function is useful when using `log` scale with datetime plots, in order to avoid *hitting* the 0 timestamp,
- `today_datetime()` and `today_string()` return today date/time as `datetime` object or string form,
- `datetime_to_string(datetime)` turns a `datetime` object into a string. Its `output_form` could be set either with its optional parameter or with the `date_form()` function described above,
- `datetimes_to_string(datetime, output_form)` turns a list of `datetime` objects into a list of strings,
- `string_to_datetime(string, input_form)` turns a string into a `datetime` object; its `input_form` could be set either with its optional parameter or with the `date_form()` function described above,
- `string_to_time(string, input_form)` turns a string into a numerical timestamp; its `input_form` could be set either with its optional parameter or with the `date_form()` function, described above,
- `strings_to_time(string, input_form)` turns a list of strings into a list of numerical timestamps; it accepts `input_form` has an optional parameter.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Datetime Menu](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-plots)


## Datetime Plot
To plot dates and/or times use either `plt.scatter()` or `plt.plot()` functions directly. Here is an example, which requires the package `yfinance`:

```python
import yfinance as yf
import plotext as plt

plt.date_form('d/m/Y')

start = plt.string_to_datetime("11/07/2020")
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
python3 -c "import yfinance as yf; import plotext as plt; plt.date_form('d/m/Y'); start = plt.string_to_datetime('11/07/2020'); end = plt.today_datetime(); data = yf.download('goog', start, end); prices = list(data['Close']); dates = plt.datetimes_to_string(data.index); plt.plot(dates, prices); plt.title('Google Stock Price'); plt.xlabel('Date'); plt.ylabel('Stock Price $'); plt.show()"
```

![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/data/datetime.png)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Datetime Menu](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-plots)


## Candlestick Plot
For this kind of plot, use the function `candlestick()`, which requires a list of string based dates/times and a dictionary with the following mandatory keys: `'Open', 'Close', 'High', 'Low'`, where each value should be a list of prices. Here is an example, which requires the package `yfinance`:

```python
import yfinance as yf
import plotext as plt

plt.date_form('d/m/Y')

start = plt.string_to_datetime("01/02/2022")
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
python3 -c "import yfinance as yf; import plotext as plt; plt.date_form('d/m/Y'); start = plt.string_to_datetime('01/02/2022'); end = plt.today_datetime(); data = yf.download('goog', start, end); dates = plt.datetimes_to_string(data.index); plt.candlestick(dates, data); plt.title('Google Stock Price Candlesticks'); plt.xlabel('Date'); plt.ylabel('Stock Price $'); plt.show()"
```

![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/data/candlestick.png)

The documentation of the `candlestick()` function can be accessed with `doc.candlestick()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Datetime Menu](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-plots)
