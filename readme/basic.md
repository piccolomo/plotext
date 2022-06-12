# Basic Plots
- [Scatter Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#scatter-plot)
- [Line Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#line-plot)
- [Stem Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#stem-plot)
- [Multiple Data Sets](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#multiple-data-sets)
- [Multiple Axes Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#multiple-axes-plot)
- [Log Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#log-plot)
- [Streaming Data](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#streaming-data)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Scatter Plot
Here is an example of a simple scatter plot:
```python
import plotext as plt
y = plt.sin() # sinusoidal signal
plt.scatter(y)
plt.title("Scatter Plot")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Scatter Plot'); plt.show()"
```
![scatter](https://raw.githubusercontent.com/piccolomo/plotext/master/data/scatter.png)

- By default, the plot size adapts to the terminal size; to change this use the function `plot_size(width, height)`, described [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-size),
- the default marker is `hd` (the 2 x 2 higher definition marker) and it is available only in `Unix` systems, as it doesn't seem to render well in Windows,
- the 3 x 2 higher definition marker, named `fhd`, works only in `Unix` systems and only in some terminals,
- the 4 x 2 highest definition marker, named `braille`, is now available (from version 5.1) and should work in `unix` systems,
- to save the plot as colorless `txt` or as colored `html`, use the function `save_fig(path)` described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#useful-functions),
- the documentation of the `scatter()` function can be accessed with `doc.scatter()`.

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

The documentation of the `plot()` function can be accessed with `doc.scatter()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)


## Stem Plot
For a stem plot use either the `fillx` or `filly` parameters (available for most plotting functions) to fill the canvas with data points till the `y = 0` or `x = 0` level, respectively. Here is an example:
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
Multiple data sets can be plotted using consecutive plotting functions. Here is an example:

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

The `label` parameter, inside any plotting function, can be used to add an entry in the plot legend, shown in the upper left corner of the plot canvas.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)


## Multiple Axes Plot
Data could be plotted independently on both lower and upper `x` axes, as well as, left and right `y` axes, using respectively the `xside` and `yside` parameters. Here is how:

```python
import plotext as plt

y1 = plt.sin()
y2 = plt.sin(2, phase = -1)

plt.plot(y1, xside= "lower", yside = "left", label = "lower left")
plt.plot(y2, xside= "upper", yside = "right", label = "upper right")

plt.title("Multiple Axes Plot")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; y1 = plt.sin(); y2 = plt.sin(2, phase = -1); plt.plot(y1, xside= 'lower', yside = 'left', label = 'lower left'); plt.plot(y2, xside= 'upper', yside = 'right', label = 'upper right'); plt.title('Multiple Axes Plot'); plt.show()"
```
![multiple-axes](https://raw.githubusercontent.com/piccolomo/plotext/master/data/multiple-axes.png)

On the right side of each legend entry, a symbol is introduce to easily identify on which axes the data refers to: its interpretation should be intuitive.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)


## Log Plot
For a log plot use the the functions `plt.xscale("log")` or `plt.yscale("log")`. Here is a basic example:

```python
import plotext as plt

l = 10 ** 4
y = plt.sin(periods = 2, length = l)

plt.plot(y)

plt.xscale("log")
plt.yscale("linear")
plt.grid(0, 1)

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

- the function `plt.xscale()` accept the parameter `xside`, to independently set the scale of each `x` axes , `"lower"` or `"upper"` - in short `1` or `2`,
- Analogously `plt.yscale()` accept the parameter `yside`, to independently set the scale of each `y` axes , `"left"` or `"right"` - in short `1` or `2`,
- the log function used is `math.log10`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)


## Streaming Data
When streaming a continuous flow of data, consider using the following functions:

- `plt.clear_data()` - in short `plt.cld()` - to clear only the plot data (without clearing the plot style) of the active subplot,
- `plt.clear_terminal()` - in short `plt.clt()` - to clear the terminal screen before the actual plot,
- `plt.sleep(time)` to reduce a possible screen flickering: for example `sleep(0.01)` would add approximately 10 ms to the computation,
- optionally `plt.clear_color()` - in short `plt.clc()` - to remove the plot coloring, at the beginning, and so to make the streaming more responsive.

Here is a coded example:

```python
import plotext as plt

l = 1000
frames = 200

plt.title("Streaming Data")
# plt.clc()

for i in range(frames):
    plt.clt()
    plt.cld()

    y = plt.sin(periods = 2, length = l, phase = 2 * i  / frames)
    plt.scatter(y)

    #plt.sleep(0.001)
    plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; l = 1000; frames = 200; plt.title('Streaming Data'); [(plt.cld(), plt.clt(), plt.plot(plt.sin(periods = 2, length = l, phase = 2 * i  / frames)), plt.sleep(0), plt.show()) for i in range(frames)]"
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/data/stream.gif)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)