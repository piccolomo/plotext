[Plotext Guide](https://github.com/piccolomo/plotext#guide)

# Bar Plots

- [Simple Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#simple-bar-plot)
- [Horizontal Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#horizontal-bar-plot)
- [Multiple Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#multiple-bar-plot)
- [Stacked Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#stacked-bar-plot)
- [Histogram Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#histogram-plot)



## Simple Bar Plot

Here is a simple bar plot:

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

Access the function `plt.bar()` documentation with `plt.doc.bar()`.

[Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)


## Horizontal Bar Plot

To change the orientation of the bar plot use its `orientation` parameter (available also for all other types of bar plots).

```python
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.bar(pizzas, percentages, orientation = "horizontal") # or shorter orientation = 'h'
plt.title("Most Favoured Pizzas in the World")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages, orientation = 'h'); plt.title('Most Favored Pizzas in the World'); plt.show()"
```
![horizontal-bar](https://raw.githubusercontent.com/piccolomo/plotext/master/images/horizontal-bar.png)

[Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)



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

Access the function `plt.multiple_bar()` documentation with `plt.doc.multiple_bar()`.

[Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)



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

Access the function `plt.stacked_bar()` documentation with `plt.doc.stacked_bar()`.

[Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)



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

Access the function `plt.hist()` documentation with `plt.doc.hist()`.

[Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)

[Plotext Guide](https://github.com/piccolomo/plotext#guide)
