# Decorator Plots

- [Line Plot](https://github.com/piccolomo/plotext/blob/master/readme/other.md#line-plot)
- [Text Plot](https://github.com/piccolomo/plotext/blob/master/readme/other.md#text-plot)
- [Indicator](https://github.com/piccolomo/plotext/blob/master/readme/other.md#indicator)
- [Shape Plot](https://github.com/piccolomo/plotext/blob/master/readme/other.md#shape-plot)

[Main Guide](https://github.com/piccolomo/plotext#guide)

## ## Line Plot

To plot extra vertical or horizontal lines use the functions `horizontal_line()` - `hline()` in short - or `vertical_line()` - `vline()` in short. Note that both methods  accept as coordinates date-time strings, if the plot allows it.

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

More documentation can be accessed with `doc.vertical_line()` and `doc.horizontal_line()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)

## Text Plot

To add text to a plot at given coordinates use the `text()` function. Here is how to use it for a labelled bar plot:

```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.bar(pizzas, percentages)
plt.title("Labelled Bar Plot using Text()")

[plt.text(pizzas[i], x = i + 1, y = percentages[i] + 1.5, alignment = 'center', color = 'red') for i in range(len(pizzas))]
plt.ylim(0, 38)
plt.plotsize(100, 30)
plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages); plt.title('Labelled Bar Plot using Text()'); [plt.text(pizzas[i], x = i + 1, y = percentages[i] + 1.5, alignment = 'center', color = 'red') for i in range(len(pizzas))]; plt.ylim(0, 38); plt.plotsize(100, 30); plt.show()"
```

![text](https://raw.githubusercontent.com/piccolomo/plotext/master/data/text.png)

- note that `text()` accepts as coordinates numbers, and date/time strings, if the plot allows it,
- the documentation of the `text()` function can be accessed with `doc.text()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)

## Indicator

To add a simple label + value indicator to, for example, a matrix of plots, use the function `indicator(value, label)`. 

- Note that both `label` and `value` could be numerical or in string form. 

- the `color` and `style` of the plot could be changed using the correspondent parameters,

- depending on the sign of `trend` (an optional parameter) an optional arrow is included to show the trend of past values.

Here is a basic example:

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

More documentation can be accessed with `doc.indicator()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)

## Shape Plot

To add shapes to a plot use the `rectangle()` or `polygon()` functions. 

- The dimensions and position of each shape could be changed using its `x`, `y` parameters (for both rectangles and polygons), `sides` and `radius` (for polygons only).
- A circle could be simulated by a polygon with high `sides`.
- The `radius` parameter is the distance of the polygon vertexes to its center: for a simulated circle this corresponds to its actual radius, hence the name.
- The aspect of the shapes could be changed with the `lines` and `fill` parameters, to plot lines between the vertexes (as by default) and fill the shape with colored markers (False by default),

Here is an example

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

More documentation can be accessed with `doc.rectangle()` and `doc.polygon()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)
