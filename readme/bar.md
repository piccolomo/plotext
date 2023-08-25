# Bar Plots

- [Vertical Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#vertical-bar-plot)
- [Horizontal Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#horizontal-bar-plot)
- [Multiple Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#multiple-bar-plot)
- [Stacked Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#stacked-bar-plot)
- [Box Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#box-plot)
- [Histogram Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#histogram-plot)

[Main Guide](https://github.com/piccolomo/plotext#guide)

## Vertical Bar Plot

Simply use the `bar()` function:

- the `marker`, `color`, and `fill` properties of the bar plot could be changed using their respective parameters: [markers](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#markers) and [colors](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors) are described in their linked sections.
- the `orientation` (vertical by default) and relative bar `width` (`4/5` by default) could also be changed using their respective parameters.

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

More documentation can be accessed with `doc.bar()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)

## Horizontal Bar Plot

Simply set `orientation = "horizontal"`  in the `bar()` function. Here is an example:

```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.bar(pizzas, percentages, orientation = "horizontal", width = 3 / 5) # or in short orientation = 'h'
plt.title("Most Favoured Pizzas in the World")
plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages, orientation = 'h', width = 3 / 5); plt.title('Most Favored Pizzas in the World'); plt.show()"
```

![horizontal-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/data/horizontal-bar.png)

More documentation can be accessed with `doc.bar()`.

To create a **simpler and sketchier version** of the same bar plot, use the function `simple_bar()` instead:

- the advantage of this bar plot is that it produces a very predictable output in terms of bar width (a single character),
- the disadvantages are that its only orientation is horizontal, it cannot be used inside a [matrix of subplots](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md#subplots) and any setting method which follows will not have any effect (like `xlabel()`, `plotsize()` and so on),

Here is an example:The default value for quintuples is False

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

More documentation can be accessed with `doc.simple_bar()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)

## Multiple Bar Plot

To plot multiple offsetted bars, each group with the same label, use the function `plt.multiple_bar()`, as in this example:

```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
male_percentages = [14, 36, 11, 8, 7, 4]
female_percentages = [12, 20, 35, 15, 2, 1]

plt.multiple_bar(pizzas, [male_percentages, female_percentages], labels = ["men", "women"])
plt.title("Most Favored Pizzas in the World by Gender")
plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.multiple_bar(pizzas, [male_percentages, female_percentages], labels = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.show()"
```

![multiple-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/data/multiple-bar.png)

More documentation can be accessed with `doc.multiple_bar()`.

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

Note that this kind of plot has the same disadvantages as `simple_bar()`, as discussed [in this section](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#horizontal-bar-plot). More documentation can be accessed with `doc.simple_multiple_bar()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)

## Stacked Bar Plot

To plot multiple bars on top of each other, each group with the same label, use the function `plt.stacked_bar()` as in this example:

```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
male_percentages = [14, 36, 11, 8, 7, 4]
female_percentages = [12, 20, 35, 15, 2, 1]

plt.stacked_bar(pizzas, [male_percentages, female_percentages], labels = ["men", "women"])
plt.title("Most Favored Pizzas in the World by Gender")
plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.stacked_bar(pizzas, [male_percentages, female_percentages], labels = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.show()"
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

Note that this kind of plot has the same disadvantages as `simple_bar()`, as discussed [in this section](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#horizontal-bar-plot). More documentation can be accessed with `doc.simple_stacked_bar()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)

## Box Plot
Box plot is common and useful in statistics plot. 
`plot.box` function supports two types of input data. The first form involves providing the raw data to calculate the distribution(`quintuples=False`, default). Alternatively, one can directly provide the pre-calculated metrics, namely the minimum, first quartile, median, third quartile, and maximum(`quintuples=True`).

the first form:
```python
import plotext as plt

labels = ["apple", "orange", "pear", "banana"]
datas = [
    [1,2,3,5,10,8],
    [4,9,6,12,20,13],
    [1,2,3,4,5,6],
    [3,9,12,16,9,8,3,7,2]]

plt.box(labels, datas, width=0.3)
plt.title("The weight of the fruit")
plt.show()
```

or directly on terminal:

```shell
python3 -c 'import plotext as plt;labels = ["apple", "orange", "pear", "banana"];datas = [[1,2,3,5,10,8],[4,9,6,12,20,13],[1,2,3,4,5,6],[3,9,12,16,9,8,3,7,2]];plt.box(labels, datas, width=0.3);plt.title("The weight of the fruit");plt.show()'
```
![box-plot-1](https://raw.githubusercontent.com/is/plotext/box/data/box-plot-1.png)

the second form:
```python
import plotext as plt

labels = ["apple", "orange", "pear", "banana"]
datas = [
    # max, q75, q50, q25, min
    [10, 7, 5, 3, 1.5],
    [19, 12.3, 9, 7, 4],
    [15, 14, 11, 9, 8],
    [13, 12, 11, 10, 6]]

plt.box(labels, datas, width=0.3, quintuples=True)
plt.title("The weight of the fruit")
plt.show()
```

or directly on terminal:

```shell
python3 -c 'import plotext as plt;labels = ["apple", "orange", "pear", "banana"];datas = [[10, 7, 5, 3, 1.5],[19, 12.3, 9, 7, 4],[15, 14, 11, 9, 8],[13, 12, 11, 10, 6]];plt.box(labels, datas, width=0.3, quintuples=True);plt.title("The weight of the fruit");plt.show()'
```
![box-plot-2](https://raw.githubusercontent.com/is/plotext/box/data/box-plot-2.png)
This feauture may require further development. 
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
plt.hist(data1, bins, label = "mean 0")
plt.hist(data2, bins, label = "mean 3")
plt.hist(data3, bins, label = "mean 6")

plt.title("Histogram Plot")
plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; import random; l = 7 * 10 ** 4; data1 = [random.gauss(0, 1) for el in range(10 * l)]; data2 = [random.gauss(3, 1) for el in range(6 * l)];  data3 = [random.gauss(6, 1) for el in range(4 * l)]; bins = 60; plt.hist(data1, bins, label = 'mean 0'); plt.hist(data2, bins, label = 'mean 3'); plt.hist(data3, bins, label = 'mean 6'); plt.title('Histogram Plot'); plt.show()"
```

![hist](https://raw.githubusercontent.com/piccolomo/plotext/master/data/hist.png)

More documentation can be accessed with `doc.hist()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)
