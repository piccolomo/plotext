[Plotext Guide](https://github.com/piccolomo/plotext#guide)

# Basic Plots

- [Scatter Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#scatter-plot)
- [Line Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#line-plot)
- [Stem Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#stem-plot)
- [Multiple Data Sets](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#multiple-data-sets)
- [Multiple Axes Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#multiple-axes-plot)
- [Log Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#log-plot)
- [Streaming Data](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#streaming-data)


## Scatter Plot

Here is an example of a simple scatter plot:
```
import plotext as plt
y = plt.sin() # sinusoidal signal 
plt.clp()
plt.scatter(y)
plt.title("Scatter Plot")
plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Scatter Plot'); plt.show()"
```
![scatter](https://raw.githubusercontent.com/piccolomo/plotext/master/images/scatter.png)

Access the `plt.scatter()` function documentation with `plt.doc.scatter()`

**Note**: the default marker is `hd` (the 2 x 2 high resolution characters) in `unix` systems only as it doesn't seem to render well in Windows; the 3 x 2 highest resolution marker, named `fhd`, works in Unix only and only in some terminals and the only way to find out is to test it.

[Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)



## Line Plot

For a line plot use the `plt.plot()` function instead:

```
import plotext as plt
y = plt.sin()
plt.clp()
plt.plot(y)
plt.title("Line Plot")
plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; y = plt.sin(); plt.plot(y); plt.title('Line Plot'); plt.show()"
```
![plot](https://raw.githubusercontent.com/piccolomo/plotext/master/images/plot.png)

Access the `plt.plot()` doc-string with `plt.doc.plot()`.

[Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)



## Stem Plot

For a stem plot use either the `fillx` or `filly` parameters (available for most plotting functions) to fill the canvas of data points till the `x` or `y` axis, respectively. Here is a basic example:

```
import plotext as plt
y = plt.sin()
plt.plot(y, fillx = True)
plt.title("Stem Plot")
plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; y = plt.sin(); plt.plot(y, fillx = True); plt.title('Stem Plot'); plt.show()"
```

![stem](https://raw.githubusercontent.com/piccolomo/plotext/master/images/stem.png)

[Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)




## Multiple Data Sets

Multiple data sets can be plotted using consecutive plotting functions. Here is an example:

```
import plotext as plt

y1 = plt.sin()
y2 = plt.sin(phase = -1)

plt.plot(y1, label = "plot")
plt.scatter(y2, label = "scatter")

plt.title("Multiple Data Set")
plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; y1 = plt.sin(); y2 = plt.sin(phase = -1); plt.plot(y1, label = 'plot'); plt.scatter(y2, label = 'scatter'); plt.title('Multiple Data Set'); plt.show()"
```
![multiple-data](https://raw.githubusercontent.com/piccolomo/plotext/master/images/multiple-data.png)

Using the `label` parameter, inside a plotting functions, adds automatically a legend in the upper left corner of the plot.

[Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)



## Multiple Axes Plot

Data could be plotted independently on both lower and upper `x` axes, as well as, left and right `y` axes, using respectively the `xside` and `yside` parameters. Here is how:

```
import plotext as plt

y1 = plt.sin()
y2 = plt.sin(2, phase = -1)

plt.plot(y1, xside= "lower", yside = "left", label = "lower left")
plt.plot(y2, xside= "upper", yside = "right", label = "upper right")

plt.title("Multiple Axes Plot")
plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; y1 = plt.sin(); y2 = plt.sin(2, phase = -1); plt.plot(y1, xside= 'lower', yside = 'left', label = 'lower left'); plt.plot(y2, xside= 'upper', yside = 'right', label = 'upper right'); plt.title('Multiple Axes Plot'); plt.show()"
```
![multiple-axes](https://raw.githubusercontent.com/piccolomo/plotext/master/images/multiple-axes.png)

**Note**:  on the right side of each legend entry, a symbol is introduce to easily identify on which axes the data set refers to: the interpretation should be intuitive.

[Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)



## Log Plot

For a log plot use the the functions `plt.xscale()` or `plt.yscale()` before `plt.show()`, to specify the scale used as either `linear` (as by default) or `log`. Here is a basic example:

```
import plotext as plt

l = 10 ** 4
x = range(1, l + 1)
y = plt.sin(1, 2, l)

plt.plot(x, y)

plt.xscale("log")
plt.yscale("linear")
plt.grid(1, 0)

plt.title("Logarithmic Plot")
plt.xlabel("logarithmic scale")
plt.ylabel("linear scale")

plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; l = 10 ** 4; x = range(1, l + 1); y = plt.sin(1, 2, l); plt.plot(x, y); plt.xscale('log'); plt.yscale('linear'); plt.grid(1, 0); plt.title('Logarithmic Plot'); plt.xlabel('logarithmic scale'); plt.ylabel('linear scale'); plt.show()"
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/log.png)

**Note**: the functions `plt.xscale()` and `plt.yscale()` can use the `xside` and `yside` parameters respectively, to independently set the scale of both `x` or `y` axes.

**Note**: the log function used is *log10*.

[Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)



## Streaming Data

When streaming a continuous flow of data, consider using the following functions:

- `plt.clear_data()` - in short `plt.cld()` - to clear only the plot data (without clearing the plot style) of the active subplot.

- `plt.clear_terminal()` - in short `plt.clt()` - to clear the terminal screen before the actual plot.

- `plt.sleep(time)` to reduce a possible screen flickering: for example `sleep(0.01)` would add approximately 10 ms to the computation.

- optionally `plt.clear_color()` - in short `plt.clc()` - to remove the plot coloring, and so to make the streaming more responsive.

Here is a coded example:

```
import plotext as plt

l = 1000
x = range(1, l + 1)
frames = 50

plt.title("Streaming Data")
plt.clc()

for i in range(frames):
    plt.clt()
    plt.cld()

    y = plt.sin(1, periods = 2, length = l, phase = 2 * i  / frames)
    plt.scatter(x, y, marker = "dot")

    #plt.sleep(0.001)
    plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; l = 1000; x = range(1, l + 1); frames = 50; plt.title('Streaming Data'); plt.clc(); [(plt.cld(), plt.clt(), plt.plot(x, plt.sin(1, periods = 2, length = l, phase = 2 * i  / frames), marker = 'dot'), plt.sleep(0), plt.show()) for i in range(frames)]"
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/stream.gif)

[Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)