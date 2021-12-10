# Basic Plots
- [ Scatter Plot ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#scatter-plot)
- [ Line Plot ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#line-plot)
- [ Stem Plot ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#stem-plot)
- [ Multiple Data Sets ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#multiple-data-sets)
- [ Multiple Axes Plot ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#multiple-axes-plot)
- [ Log Plot ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#log-plot)
- [ Streaming Data ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#streaming-data)

[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)


## Scatter Plot

Here is a basic example of a scatter plot:
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
which prints this on terminal:
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/scatter.png)

Access the `scatter()` function documentation with `plt.doc.scatter()`

**Note**: the 3 x 2 higher resolution marker (named `fhd`) used by default in the example above, doesn't work in Windows for now. But the 2 x 2 marker (named `hd`) does!

[ Basic Plots Menu ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)



## Line Plot

For a line plot use the `plot()` function instead:

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
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/plot.png)

Access the `plot()` doc-string with `plt.doc.plot()`.

[ Basic Plots Menu ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)



## Stem Plot

For a stem plot use either the `fillx` or `filly` parameters, available for most plotting functions, to fill the canvas of data till the x or y axis, respectively.

Here is a basic example:

```
import plotext as plt

y = plt.sin()

plt.scatter(y, fillx = True)
plt.title("Stem Plot")
plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y, fillx = True); plt.title('Stem Plot'); plt.show()"
```

which outputs:

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/stem.png)

[ Basic Plots Menu ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)




## Multiple Data Sets

Multiple data sets can be plotted using consecutive plotting functions. Here is a basic example:

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
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/multiple-data.png)

Using the `label` parameter, a legend is automatically added in the upper left corner of the plot.

[ Basic Plots Menu ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)



## Multiple Axes Plot

Data could be plotted independently on both lower and upper `x` axes, as well as left and right `y` axes, using respectivelly the `xside` and `yside` parameters.

Here is a simple example:

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
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/multiple-axes.png)

Note that on the right side of each legend entry, a symbol is introduce to easily identify on which axes the data set refers to: the interpretation should be intuitive.

[ Basic Plots Menu ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)



## Log Plot

For a log plot use the the functions `plt.xscale()` or `plt.yscale()` before `plt.show()`.

Here is a basic example:

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

Note that the the `xscale()` and `yscale()` functions can use the `xside` and `yside` parameters respectively, to set the scale of both `x` or `y` axes independently and if needed.

[ Basic Plots Menu ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)



## Streaming Data

When streaming a continuous flow of data, consider using the following functions:

- `plt.clear_data()` - in short `plt.cld()` - to clear only the plot data (without clearing the plot style) of the active subplot.

- `plt.clear_terminal()` - in short `plt.clt()` to clear the terminal screen before the actual plot.

- `plt.sleep(time)` to reduce a possible screen flickering; for example `sleep(0.01)` would add approximately 10 ms to the computation.

- optionally `plt.clear_color()` - in short `plt.clc()` - to remove the plot coloring, and so to make the streaming more responsive.

Here is a coded example:

```
import plotext as plt

l = 200
x = range(1, l + 1)
frames = 50

plt.title("Streaming Data")
plt.clc()

for i in range(frames):
    y = plt.sin(1, periods = 2, length = l, phase = 2 * i  / frames)	
    
    plt.cld()
    plt.clt()
    plt.plot(x, y, marker = "dot")

    #plt.sleep(0.001)
    plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; l = 200; x = range(1, l + 1); frames = 50; plt.title('Streaming Data'); plt.clc(); [(plt.cld(), plt.clt(), plt.plot(x, plt.sin(1, periods = 2, length = l, phase = 2 * i  / frames), marker = 'dot'), plt.sleep(0), plt.show()) for i in range(frames)]"
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/stream.gif)

[ Basic Plots Menu ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#basic-plots)
