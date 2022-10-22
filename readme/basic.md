# Basic Plots

- [Introduction](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#introduction)
- [Scatter Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#scatter-plot)
- [Line Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#line-plot)
- [Log Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#log-plot)
- [Stem Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#stem-plot)
- [Multiple Data Sets](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#multiple-data-sets)
- [Multiple Axes Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#multiple-axes-plot)

[Main Guide](https://github.com/piccolomo/plotext#guide)

## Introduction

**First Things to Know**:

- The **plot dimensions** by default adapt to the terminal size but can be changed using the `plotsize()` method described [here](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-size).

- To plot a matrix of subplots, use the `subplots()` and `subplot()` methods, described in [this section](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md#subplots).

- The `marker` parameter of most plotting functions can be used to change the **marker** character used to plot the data, as described in [this section](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#markers). High definition `"hd"` and `"fhd"` markers are available, including `"braille"`. 

- Similarly the `color` parameter is used to define the **color** of the data points, as described in [this section](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors).

- To rapidly generate some test **sinusoidal** or a **square wave** data, use respectively the `sin()` or `square()` methods, described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#useful-functions).

- To add **labels** to the plot use the `title()`, `xlabel()`, and `ylabel()` methods, described [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-labels), as well as the `label` parameter of most plotting functions to add an entry to the [plot legend](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#multiple-data-sets).

- To change the **plot colors** and ticks style, use the `axes_color()`, `canvas_color()`, `ticks_color()`, `ticks_style()` methods, described [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors), or more directly using the `theme()` method, described [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#themes). 

- To **add lines** to the plot, use the `grid()`, `horizontal_line()` or `vertical_line()` methods, described [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-lines). 

- To add or remove the **axes** use the methods `xaxes()`, `yaxes()` or directly `frame()`, described [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-lines).

- To change the **axes numerical ticks** use the functions `xfrequency()`, `xticks()`, `yfrequency()` and `yticks()`, described [here](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#axes-ticks).

- As with `matplotlib`, the plot is only displayed when the `show()` method is finally called.

- To **display the plot dynamically** - without using `show()` - use the `interactive(True)` method, as described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#canvas-utilities).

- To finally **save the plot** use the function `savefig(path)` described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#canvas-utilities).

- To **clear the figure, data or color** settings, use the `clear_figure()`, `clear_data()` or `clear_color()` methods respectively, described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#clearing-functions).

- To **clear the screen**, before or after plotting, use the `clear_terminal()` method, described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#clearing-functions).

- The **documentation** of all `plotext` methods and plotting functions is available in its `doc` container, as described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#docstrings).

- The package is under development, so any **bug report** or **feature request** is very welcomed, just by [opening an issue](https://github.com/piccolomo/plotext/issues/new). 

[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)

## Scatter Plot

Here is a simple scatter plot:

```python
import plotext as plt
y = plt.sin() # sinusoidal test signal
plt.scatter(y) 
plt.title("Scatter Plot") # to apply a title
plt.show() # to finally plot
```

or directly on terminal:

```console
python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Scatter Plot'); plt.show()"
```

![scatter](https://raw.githubusercontent.com/piccolomo/plotext/master/data/scatter.png)

More documentation can be accessed with `doc.scatter()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)

## Line Plot

For a line plot use the `plot()` function instead:

```python
import plotext as plt
y = plt.sin()
plt.plot(y)
plt.title("Line Plot")
plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; y = plt.sin(); plt.plot(y); plt.title('Line Plot'); plt.show()"
```

![plot](https://raw.githubusercontent.com/piccolomo/plotext/master/data/plot.png)

More documentation can be accessed with `doc.plot()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)

## Log Plot

For a logarithmic plot use the the `xscale("log")` or `yscale("log")` methods:

- `xscale()` accepts the parameter `xside` to independently set the scale on each `x` axis , `"lower"` or `"upper"` (in short `1` or `2`).
- Analogously `yscale()` accepts the parameter `yside` to independently set the scale on each `y` axis , `"left"` or `"right"` (in short `1` or `2`).
- The log function used is `math.log10`.

Here is an example:

```python
import plotext as plt

l = 10 ** 4
y = plt.sin(periods = 2, length = l)

plt.plot(y)

plt.xscale("log")    # for logarithmic x scale
plt.yscale("linear") # for linear y scale
plt.grid(0, 1)       # to add vertical grid lines

plt.title("Logarithmic Plot")
plt.xlabel("logarithmic scale")
plt.ylabel("linear scale")

plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; l = 10 ** 4; y = plt.sin(periods = 2, length = l); plt.plot(y); plt.xscale('log'); plt.yscale('linear'); plt.grid(0, 1); plt.title('Logarithmic Plot'); plt.xlabel('logarithmic scale'); plt.ylabel('linear scale'); plt.show();"
```

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/data/log.png)

More documentation is available with `doc.xscale()` or `doc.yscale()` .

[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)

## Stem Plot

For a [stem plot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html) use either the `fillx` or `filly` parameters (available for most plotting functions), in order to fill the canvas with data points till the `y = 0` or `x = 0` level, respectively.  

If a numerical value is passed to the `fillx` or `filly` parameters, it is intended as the `y` or `x` level respectively, where the filling should stop. If the string value `"internal"` is passed instead, the filling will stop when another data point is reached respectively vertically or horizontally (if it exists).

Here is an example:

```python
import plotext as plt
y = plt.sin()
plt.plot(y, fillx = True)
plt.title("Stem Plot")
plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; y = plt.sin(); plt.plot(y, fillx = True); plt.title('Stem Plot'); plt.show()"
```

![stem](https://raw.githubusercontent.com/piccolomo/plotext/master/data/stem.png)
[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)

## Multiple Data Sets

Multiple data sets can be plotted using consecutive plotting functions. The `label` parameter, available in most plotting function, is used to add an entry in the **plot legend**, shown in the upper left corner of the plot canvas.

Here is an example:

```python
import plotext as plt

y1 = plt.sin()
y2 = plt.sin(phase = -1)

plt.plot(y1, label = "plot")
plt.scatter(y2, label = "scatter")

plt.title("Multiple Data Set")
plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; y1 = plt.sin(); y2 = plt.sin(phase = -1); plt.plot(y1, label = 'plot'); plt.scatter(y2, label = 'scatter'); plt.title('Multiple Data Set'); plt.show()"
```

![multiple-data](https://raw.githubusercontent.com/piccolomo/plotext/master/data/multiple-data.png)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)

## Multiple Axes Plot

Data could be plotted on the lower or upper `x` axis, as well as on the left or right `y` axis, using respectively the `xside` and `yside` parameters of most plotting functions. 

On the left side of each legend entry, a symbol is introduce to easily identify on which couple of axes the data has been plotted to: its interpretation should be intuitive.

Here is an example:

```python
import plotext as plt

y1 = plt.sin()
y2 = plt.sin(2, phase = -1)

plt.plot(y1, xside = "lower", yside = "left", label = "lower left")
plt.plot(y2, xside = "upper", yside = "right", label = "upper right")

plt.title("Multiple Axes Plot")
plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; y1 = plt.sin(); y2 = plt.sin(2, phase = -1); plt.plot(y1, xside = 'lower', yside = 'left', label = 'lower left'); plt.plot(y2, xside = 'upper', yside = 'right', label = 'upper right'); plt.title('Multiple Axes Plot'); plt.show()"
```

![multiple-axes](https://raw.githubusercontent.com/piccolomo/plotext/master/data/multiple-axes.png)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)