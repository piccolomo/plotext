# Other Plots
- [Event Plot](https://github.com/piccolomo/plotext/blob/master/readme/other.md#event-plot)
- [Line Plot](https://github.com/piccolomo/plotext/blob/master/readme/other.md#line-lines)
- [Text Plot](https://github.com/piccolomo/plotext/blob/master/readme/other.md#text-plot)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Event Plot
To signal the timing of certain events, `eventplot()` function could be of use. Here is an example:

```python
import plotext as plt
from random import randint
from datetime import datetime, timedelta

plt.date_form("H:M") # also "H" looks ok

times = [datetime(2022, 3, 27, randint(0, 23), randint(0, 59), randint(0, 59)) for i in range(100)] # A random list of times during the day
times = plt.datetimes_to_string(times)

plt.plotsize(None, 20) # Set the height you prefer or comment for maximum size 

plt.eventplot(times)

plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; from random import randint; from datetime import datetime, timedelta; plt.date_form('H:M'); times = [datetime(2022, 3, 27, randint(0, 23), randint(0, 59), randint(0, 59)) for i in range(100)]; times = plt.datetimes_to_string(times); plt.plotsize(None, 20); plt.eventplot(times); plt.show()"
```

![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/images/eventplot.png)

The documentation of the `eventplot()` function can be accessed with `doc.eventplot()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Datetime Menu](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-menu)


## Line Plot
To plot extra vertical or horizontal lines use the functions `horizontal_line()` - `hline()` in short - and `vertical_line()` - `vline()` in short.

```python
import plotext as plt
y = plt.sin() 
plt.scatter(y)
plt.title("Extra Lines")
plt.vline(100, "magenta")
plt.hline(0.5, "blue+")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Extra Lines'); plt.vline(100, 'magenta'); plt.hline(0.5, 'blue+'); plt.show()"
```

![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/images/extralines.png)

- Note that `vline()` and `hline()` accept as coordinates numbers, date/time strings or bar labels (if the plot allows it).
- The documentation of the `vline()` and `hline()` functions can be accessed with `doc.vertical_line()` and `doc.horizontal_line()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)


## Text Plot
To add text to a plot use the `text()` function. Here is how to use it for a labelled bar plot:
 
```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.bar(pizzas, percentages)
plt.title("Labelled Bar Plot using Text()")

[plt.text(pizzas[i], x = pizzas[i], y = percentages[i] + 0.8, alignment = 'center', color = 'red') for i in range(len(pizzas))]
plt.ylim(0, 38)
plt.show()
```

or directly on terminal:
```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages); plt.title('Labelled Bar Plot using Text()'); [plt.text(pizzas[i], x = pizzas[i], y = percentages[i] + 0.8, alignment = 'center', color = 'red') for i in range(len(pizzas))]; plt.ylim(0, 38); plt.show()"
```

![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/images/labelled-bar.png)

- note that `text()` accepts as coordinates numbers, date/time strings or bar labels, if the plot allows it,
- the full documentation of the `text()` function can be accessed with `doc.text()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)
