# Bar Plots

- [ Simple Bar Plot ](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#simple-bar-plot)
- [ Multiple Bar Plot ](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#multiple-bar-plot)
- [ Stacked Bar Plot ](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#stacked-bar-plot)
- [ Histogram Plot ](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#histogram-plot)

[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)



## Simple Bar Plot

Here is a simple bar plot:

```
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.bar(pizzas, percentages)
plt.title("Most Favored Pizzas in the World")
plt.show()
```

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/bar.png)

The `bar()` doc-string is available using `plt.doc.bar()`.

[ Bar Plots Menu ](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)



## Multiple Bar Plot

To plot multiple offsetted bars with the same labels, use the `plt.multiple_bar()` function, as in this example:

```
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
male_percentages = [14, 36, 11, 8, 7, 4]
female_percentages = [12, 20, 35, 15, 2, 1]

plt.multiple_bar(pizzas, [male_percentages, female_percentages], label = ["men", "women"])
plt.title("Most Favored Pizzas in the World by gender")
plt.show()
```

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/multiple-bar.png)

[ Bar Plots Menu ](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)



## Stacked Bar Plot

To plot multiple bars on top of each other with the same labels, use the `plt.stacked_bar()` function as in this example:

```
import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
male_percentages = [14, 36, 11, 8, 7, 4]
female_percentages = [12, 20, 35, 15, 2, 1]

plt.stacked_bar(pizzas, [male_percentages, female_percentages], label = ["men", "women"])
plt.title("Most Favored Pizzas in the World by gender")
plt.show()
```

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/stacked-bar.png)

[ Bar Plots Menu ](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)



## Histogram Plot

For a histogram plot use the the `plt.hist()` function. Here is an example:

```
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
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/hist.png)

Access the `hist()` function doc-string for more documentation, using `plt.doc.hist()`.

[ Bar Plots Menu ](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#bar-plots)
