# Datetime Menu

- [ Datetime Utilities ](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-utilities)
- [ Datetime Plots ](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-plots)

[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)



## Datetime Utilities 

`Plotext` has a container of tools, called `plt.datetime`, to easily manipulate datetime objects. Here is the list of its utilities:

- `plt.datetime.today` stores in its sub-entries today's date in string, tuple, or datetime form.

- `plt.datetime.set_time0()` sets the origin of time to the `year`, `month`, `day`, `hour`, `minute` and `second`, provided as integer. The default value is 01/01/1900. 
This function is useful when using log scale with datetime plots, in order to avoid "hitting" the 0 timestamp. Note that `hour`, `minute` and `second` are set to 0, if not provided.

- `plt.datetime.set_datetime_form()` is used to change how to interpret string based datetime objects. It accepts two parameters: `date_form` for date forms (by default `%d/%m/%Y`) and `time_form` for time forms (by default `%H:%M:%S`).

- `plt.datetime.clear()` restores the internal definitions of the `datetime` container.

- `plt.datetime.string_to_datetime()` turns a string based datetime object into an object of the `datetime` package.

- `plt.datetime.datetime_to_timestamp()` turns an object of the `datetime` package to a timestamp, relative to the origin of time.

- `plt.datetime.string_to_timestamp()` turns a string based datetime object into a timestamp.

- `plt.datetime.datetime_to_string()` turns an object of the `datetime` package into a string.

[ Datetime Menu ](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-menu)




## Datetime Plots

To plot dates and/or times use the functions `scatter_date()` and `plot_date()`.

Here is an example which uses the package `yfinance`.

```
import yfinance as yf
import plotext as plt
plt.datetime.set_datetime_form(date_form='%d/%m/%Y')

start = plt.datetime.string_to_datetime("11/07/2020")
end = plt.datetime.today.datetime
data = yf.download('goog', start, end)

prices = list(data["Close"])
dates = [plt.datetime.datetime_to_string(el) for el in data.index]

plt.plot_date(dates, prices)

plt.title("Google Stock Price")
plt.xlabel("Date")
plt.ylabel("Stock Price $")
plt.show()
```

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/datetime.png)

[ Datetime Menu ](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-menu)
