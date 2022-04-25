# Datetime Menu

- [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-utilities)
- [Basic Plot](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#basic-plot)
- [Candlestick Plot](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#candlestick-plot)

[Plotext Guide](https://github.com/piccolomo/plotext#guide)


## Datetime Utilities

`Plotext` has a set of utilities to easily manipulate datetime objects:

- `date_form(input_form, output_form)` sets how some functions interpret string based datetime objects; `input_form` is used to control functions that take strings as input while `output_form` (by default equal to `input_form`) is used to control functions that output strings. 

- Date/time forms are the standard ones, with the `%` symbol removed for simplicity. Common forms are `d/m/Y` (by default), or `d/m/Y H:M:S`. Here is an extensive [guide](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) on date/time format codes.

- `set_time0()` sets the origin of time to string provided. This function is useful when using `log` scale with datetime plots, in order to avoid *hitting* the 0 timestamp. 

- `today_datetime()` and `today_string()` return today date/time as `datetime` object or string form.

- `plt.datetime_to_string(datetime, output_form)` turns a `datetime` object into a string. The `output_form` could be either set directly or with the `date_form()` function.  

- `plt.datetimes_to_string(datetime, output_form)` turns a list of `datetime` objecst into a list of strings. 

- `plt.string_to_datetime(string, input_form)` turns a string into a `datetime` object. The `input_form` could be either set directly or with the `date_form()` function.

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Datetime Menu](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-menu)



## Basic Plot

To plot dates and/or times use either `plt.scatter()` or `plt.plot()`. Here is an example, which requires the package `yfinance`:

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

![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/images/datetime.png)

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Datetime Menu](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-menu)


## Candlestick Plot

For this kind of plot, use the function `candlestick()` which requires a list of string dates and a dictionary with the following mandatory keys: 'Open', 'Close', 'High', 'Low', where each value should be a list of prices. Here is an example, which requires the package `yfinance`:

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

The documentation of the `candlestick()` function can be accessed with `plotext.doc.candlestick()`.


![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/images/candlestick.png)

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Datetime Menu](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-menu)
