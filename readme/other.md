# Other Plots
- [Error Plot](https://github.com/piccolomo/plotext/blob/master/readme/other.md#error-plot)
- [Event Plot](https://github.com/piccolomo/plotext/blob/master/readme/other.md#event-plot)
- [Line Plot](https://github.com/piccolomo/plotext/blob/master/readme/other.md#line-plot)
- [Text Plot](https://github.com/piccolomo/plotext/blob/master/readme/other.md#text-plot)
- [Shape Plot](https://github.com/piccolomo/plotext/blob/master/readme/other.md#shape-plot)
- [Indicator](https://github.com/piccolomo/plotext/blob/master/readme/other.md#indicator)


[Main Guide](https://github.com/piccolomo/plotext#guide)


## Error Plot
To plot data with error bars, along both the `x` and `y` axes use the `error()` function as in this example:

```python
import plotext as plt
from random import random 
l = 20
n = 1
ye = [random() * n for i in range(l)]; xe = [random() * n for i in range(l)]
y = plt.sin(length = l); 
plt.error(y, xerr = xe, yerr = ye)
plt.title('Error Plot')
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; plt.clf();  from random import random; l = 20; n = 1; ye = [random() * n for i in range(l)]; xe = [random() * n for i in range(l)]; y = plt.sin(length = l); plt.error(y, xerr = xe, yerr = ye); plt.title('Error Plot'); plt.show();"
```
![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/data/error.png)
- Optionally also the `x` coordinates could be provided,
- the documentation of the `error()` function can be accessed with `doc.error()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)


## Event Plot
To signal the timing of certain events, `event_plot()` function could be of use. Here is an example:

```python
import plotext as plt
from random import randint
from datetime import datetime, timedelta

plt.date_form("H:M") # also just "H" looks ok

times = [datetime(2022, 3, 27, randint(0, 23), randint(0, 59), randint(0, 59)) for i in range(100)] # A random list of times during the day
times = plt.datetimes_to_string(times)

plt.plotsize(None, 20) # Set the preferred height or comment for maximum size 

plt.event_plot(times)

plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; from random import randint; from datetime import datetime, timedelta; plt.date_form('H:M'); times = [datetime(2022, 3, 27, randint(0, 23), randint(0, 59), randint(0, 59)) for i in range(100)]; times = plt.datetimes_to_string(times); plt.plotsize(None, 20); plt.event_plot(times); plt.show()"
```

![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/data/eventplot.png)

The documentation of the `event_plot()` function can be accessed with `doc.event_plot()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)


## Line Plot
To plot extra vertical or horizontal lines use the functions `horizontal_line()` - `hline()` in short - and `vertical_line()` - `vline()` in short.

```python
import plotext as plt
y = plt.sin() 
plt.scatter(y)
plt.title("Extra Lines")
plt.vline(100, "magenta")
plt.hline(0.5, "blue+")
plt.plotsize(100, 30)
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Extra Lines'); plt.vline(100, 'magenta'); plt.hline(0.5, 'blue+'); plt.plotsize(100, 30); plt.show()"
```

![line](https://raw.githubusercontent.com/piccolomo/plotext/master/data/line.png)

- Note that `vertical_line()` and `horizontal_line()` accept as coordinates numbers and date/time strings, if the plot allows it,
- The documentation of the `vertical_line()` and `horizontal_line()` functions can be accessed with `doc.vertical_line()` and `doc.horizontal_line()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)


## Text Plot
To add text to a plot use the `text()` function. Here is how to use it for a labelled bar plot:
 
```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.bar(pizzas, percentages)
plt.title("Labelled Bar Plot using Text()")

[plt.text(pizzas[i], i + 1, y = percentages[i] + 1.5, alignment = 'center', color = 'red') for i in range(len(pizzas))]
plt.ylim(0, 38)
plt.plotsize(100, 30)
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages); plt.title('Labelled Bar Plot using Text()'); [plt.text(pizzas[i], i + 1, y = percentages[i] + 1.5, alignment = 'center', color = 'red') for i in range(len(pizzas))]; plt.ylim(0, 38); plt.plotsize(100, 30); plt.show()"
```

![text](https://raw.githubusercontent.com/piccolomo/plotext/master/data/text.png)

- note that `text()` accepts as coordinates numbers, and date/time strings, if the plot allows it,
- the documentation of the `text()` function can be accessed with `doc.text()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)


## Shape Plot
To add shapes to a plot use the `rectangle()` and `polygon()` functions. Here is an example
 
```python
import plotext as plt
plt.title('Shapes')
plt.polygon()
plt.rectangle()
plt.polygon(sides = 100) # to simulate a circle
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; plt.clf(); plt.title('Shapes'); plt.polygon(); plt.rectangle(); plt.polygon(sides = 100); plt.show()"
```

![shapes](https://raw.githubusercontent.com/piccolomo/plotext/master/data/shapes.png)

- the dimensions and position of each shape could be changed using its parameters `x`, `y` (for both rectangles and polygons), `sides` and `radius` (for polygons only),
- a circle could be simulated by a polygon with high `sides`, 
- `radius` is the distance of the polygon vertexes to its center: for a simulated circle this corresponds to its actual radius, hence the name, 
- the aspect of the shapes could be changed with the `lines` and `fill` parameters, to plot lines between the vertexes (as by default) and fill the shape with coloured markers (False by default),
- the documentation of the `rectangle()` function can be accessed with `doc.rectangle()`,
- the documentation of the `polygon()` function can be accessed with `doc.polygon()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)



## Indicator

To add a simple label + value indicator to, for example, a matrix of plots, use the function `indicator(value, label)`. Here is a basic example:
 
```python
import plotext as plt
plt.indicator(45.3, 'Price')
plt.plotsize(30, 10)
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; plt.indicator(45.3, 'Price'); plt.plotsize(30, 10); plt.show()"
```

![indicator](https://raw.githubusercontent.com/piccolomo/plotext/master/data/indicator.png)

- the `color` and `style` could be changed using the correspondent parameters,
- depending on the sign of `trend` (an optional parameter) an optional arrow is included to show the trend of past values.
- the documentation of the `indicator()` function can be accessed with `doc.indicator()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)
