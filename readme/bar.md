# Bar Plots
- [Vertical Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#vertical-bar-plot)
- [Horizontal Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#horizontal-bar-plot)
- [Multiple Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#multiple-bar-plot)
- [Stacked Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#stacked-bar-plot)
- [Histogram Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#histogram-plot)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Vertical Bar Plot
Here is an example:
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
![vertical-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/data/vertical-bar.png)

- The `marker`, `color`, and `fill` properties could be changed using their respective parameters: [markers](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#markers) and [colors](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors) are described in their linked section. 
- the `orientation` and relative `width` (4 / 5 by default) of the bars could also be changed using their respective parameters, 
- the full documentation of the `bar()` function can be accessed with `doc.bar()`.

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

![horizontal-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/data/horizontal-bar.png)

To create a **simpler and sketchier version** of the same bar plot, use the function `simple_bar()` instead, as in this example:
```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.simple_bar(pizzas, percentages, width = 100, title = 'Most Favored Pizzas in the World')
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.simple_bar(pizzas, percentages, width = 100, title = 'Most Favored Pizzas in the World'); plt.show()"
```

![simple-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/data/simple-bar.png)

- The advantage of this bar plot is that it produces a very predictable output in terms of bar width (a single character),
- the disadvantages are that its only orientation is horizontal, it cannot be used inside a [matrix of subplots](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md) and any setting function which follows will not have any effect (like `xlabel()`, `plotsize()` and so on), 
- the full documentation of the `simple_bar()` function can be accessed with `doc.simple_bar()`.


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

![multiple-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/data/multiple-bar.png)


The full documentation of the `multiple_bar()` function can be accessed with `doc.multiple_bar()`.

To produce a **simpler and sketchier version** of the same bar plot, use the function `simple_multiple_bar()` instead, as in this example:
```python
import plotext as plt
pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']
male_percentages = [14, 36, 11, 8, 7, 4]
female_percentages = [12, 20, 35, 15, 2, 1]
plt.simple_multiple_bar(pizzas, [male_percentages, female_percentages], width = 100, labels = ['men', 'women'], title = 'Most Favored Pizzas in the World by Gender')
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.simple_multiple_bar(pizzas, [male_percentages, female_percentages], width = 100, labels = ['men', 'women'], title = 'Most Favored Pizzas in the World by Gender'); plt.show()"
```

![simple-multiple-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/data/simple-multiple-bar.png)


The full documentation of the `simple_multiple_bar()` function can be accessed with `doc.simple_multiple_bar()`.


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
![stacked-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/data/stacked-bar.png)

The full documentation of the `stacked_bar()` function can be accessed with `doc.stacked_bar()`.

To produce a **simpler and sketchier version** of the same bar plot, use the function `simple_stacked_bar()` instead, as in this example:
```python
import plotext as plt
pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']
male_percentages = [14, 36, 11, 8, 7, 4]
female_percentages = [12, 20, 35, 15, 2, 1]
plt.simple_stacked_bar(pizzas, [male_percentages, female_percentages], width = 100, labels = ['men', 'women'], title = 'Most Favored Pizzas in the World by Gender')
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.simple_stacked_bar(pizzas, [male_percentages, female_percentages], width = 100, labels = ['men', 'women'], title = 'Most Favored Pizzas in the World by Gender'); plt.show()"
```

![simple-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/data/simple-stacked-bar.png)

The full documentation of the `simple_stacked_bar()` function can be accessed with `doc.simple_stacked_bar()`,

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
![hist](https://raw.githubusercontent.com/piccolomo/plotext/master/data/hist.png)

The full documentation of the `hist()` function can be accessed with `doc.hist()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)
