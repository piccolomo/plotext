# Bar Plots

- [Simple Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#simple-bar-plot)
- [Horizontal Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#horizontal-bar-plot)
- [Sketchy Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#sketchy-bar-plot)
- [Multiple Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#multiple-bar-plot)
- [Stacked Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#stacked-bar-plot)
- [Histogram Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#histogram-plot)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Simple Bar Plot

```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.bar(pizzas, percentages)
plt.title("Most Favored Pizzas in the World")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages); plt.title('Most Favored Pizzas in the World'); plt.show()"
```
![simple-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/images/simple-bar.png)

- The color, marker, width, fill properties and orientation of the bars, could be changed using the respective parameters. 

- The full documentation of the `bar()` function can be accessed with `doc.bar()`.

- To label each bar with a string follow [this](https://github.com/piccolomo/plotext/blob/master/readme/tools.md#text-plot) example.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)


## Horizontal Bar Plot

To change the orientation of the bar plot use its `orientation` parameter (available also for all other types of bar plots).

```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.bar(pizzas, percentages, orientation = "horizontal", width = 3 / 5) # or shorter orientation = 'h'
plt.title("Most Favoured Pizzas in the World")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages, orientation = 'h', width = 3 / 5); plt.title('Most Favored Pizzas in the World'); plt.show()"
```

![horizontal-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/images/horizontal-bar.png)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)


## Sketchy Bar Plot
Here is a sketchy version of the previous bar plot:
```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.bar(pizzas, percentages, orientation = "h", width = 0.3, marker = 'fhd') 
plt.title("Most Favoured Pizzas in the World")
plt.clc() # to remove colors
plt.plotsize(100, (2 * len(pizzas) - 1) + 4) # 4 = (1 for x numerical ticks + 2 for x axes + 1 for title)
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages, orientation = 'h', width = 0.3, marker = 'fhd'); plt.title('Most Favoured Pizzas in the World'); plt.clc(); plt.plotsize(100, 2 * len(pizzas) + 4); plt.show()"
```

![horizontal-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/images/sketchy-bar.png)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)


## Multiple Bar Plot

To plot multiple offsetted bars, with the same labels, use the function `plt.multiple_bar()`, as in this example:

```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
male_percentages = [14, 36, 11, 8, 7, 4]
female_percentages = [12, 20, 35, 15, 2, 1]

plt.multiple_bar(pizzas, [male_percentages, female_percentages], label = ["men", "women"])
plt.title("Most Favored Pizzas in the World by Gender")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.multiple_bar(pizzas, [male_percentages, female_percentages], label = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.show()"
```

![multiple-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/images/multiple-bar.png)

The full documentation of the `multiple_bar()` function can be accessed with `doc.multiple_bar()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)


## Stacked Bar Plot

To plot multiple bars on top of each other and with the same labels, use the function `plt.stacked_bar()` as in this example:

```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
male_percentages = [14, 36, 11, 8, 7, 4]
female_percentages = [12, 20, 35, 15, 2, 1]

plt.stacked_bar(pizzas, [male_percentages, female_percentages], label = ["men", "women"])
plt.title("Most Favored Pizzas in the World by Gender")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.stacked_bar(pizzas, [male_percentages, female_percentages], label = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.show()"
```
![stacked-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/images/stacked-bar.png)

The full documentation of the `stacked_bar()` function can be accessed with `doc.stacked_bar()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)


## Histogram Plot

For a histogram plot use the function `plt.hist()`. Here is an example:

```python
import plotext as plt
import random

l = 7 * 10 ** 4
data1 = [random.gauss(0, 1) for el in range(10 * l)]
data2 = [random.gauss(3, 1) for el in range(6 * l)]
data3 = [random.gauss(6, 1) for el in range(4 * l)]

bins = 60
plt.hist(data1, bins, label="mean 0")
plt.hist(data2, bins, label="mean 3")
plt.hist(data3, bins, label="mean 6")

plt.title("Histogram Plot")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; import random; l = 7 * 10 ** 4; data1 = [random.gauss(0, 1) for el in range(10 * l)]; data2 = [random.gauss(3, 1) for el in range(6 * l)];  data3 = [random.gauss(6, 1) for el in range(4 * l)]; bins = 60; plt.hist(data1, bins, label='mean 0'); plt.hist(data2, bins, label='mean 3'); plt.hist(data3, bins, label='mean 6'); plt.title('Histogram Plot'); plt.show()"
```
![hist](https://raw.githubusercontent.com/piccolomo/plotext/master/images/hist.png)

The full documentation of the `hist()` function can be accessed with `doc.hist()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)
