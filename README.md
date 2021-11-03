![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/logo.png)

`plotext` plots directly on terminal, it has no dependencies and the syntax is very similar to `matplotlib`. It also provide a simple command line tool.

Note: there are many new features from the previous version, any bug report is useful and very welcomed.

<a name="contents"></a>
## Table of Contents

- [ Scatter Plot ](https://github.com/piccolomo/plotext#scatter-plot)
- [ Line Plot ](https://github.com/piccolomo/plotext#line-plot)
- [ Log Plot ](https://github.com/piccolomo/plotext#log-plot)
- [ Stem Plot ](https://github.com/piccolomo/plotext#stem-plot)
- [ Multiple Data Sets ](https://github.com/piccolomo/plotext#multiple-data-sets)
- [ Double Y Axes ](https://github.com/piccolomo/plotext#doubley)
- [ Bar Plot ](https://github.com/piccolomo/plotext#bar-plot)
- [ Histogram Plot ](https://github.com/piccolomo/plotext#histogram-plot)
- [ Data Ticks ](https://github.com/piccolomo/plotext#data-ticks)
- [ Date Time Plot ](https://github.com/piccolomo/plotext#date-time-plot)
- [ Plot Limits ](https://github.com/piccolomo/plotext#plot-limits)
- [ Plot Aspect ](https://github.com/piccolomo/plotext#plot-aspect)
- [ Multiple Subplots ](https://github.com/piccolomo/plotext#subplots)
- [ Streaming Data ](https://github.com/piccolomo/plotext#streaming-data)
- [ Other Functions ](https://github.com/piccolomo/plotext#other-functions)
- [ Installation ](https://github.com/piccolomo/plotext#installation)
- [ Main Updates ](https://github.com/piccolomo/plotext#main-updates)
- [ Future Plans ](https://github.com/piccolomo/plotext#future-plans)



<a name="scatter"></a>
# Scatter Plot
Here is a basic example of a scatter plot:
```
import plotext as plt
y = plt.sin(100, 3) # sinuisodal signal with 100 points and 3 periods
plt.scatter(y)
plt.plotsize(100, 30)
plt.title("Scatter Plot Example")
plt.show()
```
which prints this on terminal:
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/scatter.png)

The equivalent direct terminal command line is:
```
python3 -m plotext "import plotext as plt; y = plt.sin(100, 3); plt.scatter(y); plt.plotsize(100, 30); plt.title('Scatter Plot Example'); plt.show()"
```
Access the `scatter` docstring for more documentation.

**Note**: the higher resolution marker shown in the picture doesn't work in Windows for now, use other available markers in this case, like `dot`, `big` or others. See the section [ Plot Aspect ](https://github.com/piccolomo/plotext#plot-aspect) for further guidance.

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)


<a name="plot"></a>
# Line Plot
For a line plot use the the `plot` function instead:
```
import plotext as plt
y = plt.sin(100, 3)
plt.plot(y)
plt.plotsize(100, 30)
plt.title("Plot Example")
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/plot.png)
The equivalent direct terminal command line is:

```
python3 -m plotext "import plotext as plt; y = plt.sin(100, 3); plt.plot(y); plt.plotsize(100, 30); plt.title('Plot Example'); plt.show()"

```
Access the `plot` docstring for more documentation.

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)


<a name="log"></a>
# Log Plot
For a log plot use the the `xscale()` or `yscale()` functions after the plotting functions:
```
import plotext as plt
l = 10 ** 4
x = range(1, l + 1)
y = plt.sin(l, 2)
plt.plot(x, y)
plt.plotsize(100, 30)
plt.xscale("log")
plt.yscale("linear")
plt.title("Logarithmic Plot")
plt.xlabel("logarithmic scale")
plt.ylabel("linear scale")
plt.grid(1, 0)
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/log.png)
The equivalent direct terminal command line is:

```
python3 -m plotext "import plotext as plt; l = 10 ** 4; x = range(1, l + 1); y = plt.sin(l, 2); plt.plot(x, y); plt.plotsize(100, 30); plt.xscale('log'); plt.yscale('linear'); plt.title('Logarithmic Plot'); plt.xlabel('logarithmic scale'); plt.ylabel('linear scale'); plt.grid(1, 0); plt.show()"
```
Access the `xscale` and `yscale` docstring for more documentation.

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)



<a name="stem"></a>
# Stem Plot
For a stem plot use either `fillx` or `filly` parameters. Here is a basic example:
```
import plotext as plt
y = plt.sin(50, 2)
plt.scatter(y, fillx = True)
plt.plotsize(100, 30)
plt.title("Stem Plot")
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/stem.png)
The equivalent direct terminal command line is:

```
python3 -m plotext "import plotext as plt; y = plt.sin(50, 2); plt.scatter(y, fillx = True); plt.plotsize(100, 30); plt.title('Stem Plot'); plt.show()"
```

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)



<a name="multiple"></a>
# Multiple Data Sets
Multiple data sets can be plotted using consecutive `scatter` or `plot` functions. Here is a basic example:
```
import plotext as plt
y1 = plt.sin(1000, 3)
y2 = plt.sin(1000, 3, 1.5, phase = 1)
plt.plot(y1, label = "plot")
plt.scatter(y2, label = "scatter", marker = "small")
plt.plotsize(100, 30)
plt.title("Multiple Data Set")
plt.show()
```
Using the `label` parameter inside the plotting calls, a legend is automatically added in the upper left corner of the plot.

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/multiple.png)

The equivalent direct terminal command line is:

```
python3 -m plotext "import plotext as plt; y1 = plt.sin(1000, 3); y2 = plt.sin(1000, 3, 1.5, phase = 1); plt.plot(y1, label = 'plot'); plt.scatter(y2, label = 'scatter', marker = 'small'); plt.plotsize(100, 30); plt.title('Multiple Data Set'); plt.show()"
```

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)


<a name="doubley"></a>
# Double Y Axis
Data could be plotted indipendently on both left and right `y` axes, using the `yaxis` parameter. Here is a simple example:
```
import plotext as plt
y1 = plt.sin(1000, 3)
y2 = [2 * el for el in plt.sin(1000, 1, 0, phase = 1)]
plt.plot(y1, label = "plot", yaxis = "left")
plt.scatter(y2, label = "scatter", marker = "small", yaxis = "right")
plt.plotsize(100, 30)
plt.title("Double Y Axis")
plt.ylabel("left axis", "right axis")
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/doubley.png)

The equivalent direct terminal command line is:
```
python3 -m plotext "import plotext as plt; y1 = plt.sin(1000, 3); y2 = [2 * el for el in plt.sin(1000, 1, 0, phase = 1)]; plt.plot(y1, label = 'plot'); plt.scatter(y2, label = 'scatter', marker = 'small', yaxis = 'right'); plt.plotsize(100, 30); plt.title('Double Y Axis'); plt.ylabel('left axis', 'right axis'); plt.show()"
```
The `yaxis` parameter is also used in the functions `yscale`, `yticks`, `ylim`, `plot`, `bar` and `hist`.

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)




<a name="bar"></a>
# Bar Plot
For a bar plot use the the `bar` function. Here is an example:
```
import plotext as plt
cities = ["Tokyo", "Delhi", "Shanghai", "São Paulo", "Mexico City", "Cairo", "Mumbai", "Beijing"]
population = [37400068, 28514000, 25582000, 21650000, 21581000, 20076000, 19980000, 19618000]
plt.bar(cities, population)
plt.plotsize(100, 30)
plt.title("Bar Plot of the World Largest Cities")
plt.xlabel("City")
plt.ylabel("Population")
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/bar.png)

The equivalent direct terminal command line is:

```
python3 -m plotext "import plotext as plt; cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mexico City', 'Cairo', 'Mumbai', 'Beijing']; population = [37400068, 28514000, 25582000, 21650000, 21581000, 20076000, 19980000, 19618000]; plt.bar(cities, population); plt.plotsize(100, 30); plt.title('Bar Plot of the World Largest Cities'); plt.xlabel('City'); plt.ylabel('Population'); plt.show()"
```
Access the `bar` docstring for more documentation. Note: for now it doesn't work with log scale.

**Note**: the higher resolution marker shown in the picture doesn't work in Windows for now, use other available markers in this case, like `dot`, `big` or others. See the section

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)



<a name="hist"></a>
# Histogram Plot
For a histogram plot use the the `hist` function. Here is an example:
```
import plotext as plt
import random
l = 10 ** 3
data1 = [random.gauss(0, 1) for el in range(10 * l)]
data2 = [random.gauss(3, 1) for el in range(6 * l)]
data3 = [random.gauss(6, 1) for el in range(4 * l)]
plt.clp()
bins = 60
plt.hist(data1, bins, label="mean 0")
plt.hist(data2, bins, label="mean 3")
plt.hist(data3, bins, label="mean 6")
plt.title("Histogram Plot")
plt.xlabel("data bin")
plt.ylabel("frequency")
plt.plotsize(100, 30)
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/hist.png)

The equivalent direct terminal command line is:

```
python3 -m plotext "import plotext as plt; import random; l = 10 ** 3; data1 = [random.gauss(0, 1) for el in range(10 * l)]; data2 = [random.gauss(3, 1) for el in range(6 * l)]; data3 = [random.gauss(6, 1) for el in range(4 * l)]; plt.clp(); bins = 60; plt.hist(data1, bins, label='mean 0'); plt.hist(data2, bins, label='mean 3'); plt.hist(data3, bins, label='mean 6'); plt.title('Histogram Plot'); plt.xlabel('data bin'); plt.ylabel('frequency'); plt.plotsize(100, 30); plt.show()"
```
Access the `hist` docstring for more documentation. Note: for now it doesn't work with log scale.

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)



<a name="ticks"></a>
# Data Ticks
You can change the numerical ticks on both axes with the following three functions - to be placed before `show()`:

 - `plt.ticks(xnum, ynum)` sets the ticks frequency on respectively the `x` and `y` axis.
 - `plt.xticks(ticks, labels)` manually sets the `x` ticks to the list of `labels` at the list of coordinates provided in `ticks`. If only one list is provided (`ticks`), the labels will correspond to the coordinates.
 - `plt.yticks(ticks, labels)` is the equivalent of `plt.xticks()` but for the `y` axis. It also takes the optional parameter `yaxis` in case multiple `y` axes are used in the plot.

Here is a coded example:
```
import plotext as plt
l, n = 1000, 3
y1 = plt.sin(l, n)
y2 = plt.sin(l, n, 2)
import numpy as np
xticks = np.arange(0, l + l / (2 * n), l / (2 * n))
xlabels = [str(i) + "π" for i in range(2 * n + 1)]
plt.scatter(y1, label = "periodic signal")
plt.scatter(y2, label = "decaying signal", marker = "small", color = "gold")
plt.plotsize(100, 30)
plt.ticks(None, 3)
plt.xticks(xticks, xlabels)
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/ticks.png)

The equivalent direct terminal command line is:

```
python3 -m plotext "import plotext as plt; l, n = 1000, 3; y1 = plt.sin(l, n); y2 = plt.sin(l, n, 2); import numpy as np; xticks = np.arange(0, l + l / (2 * n), l / (2 * n)); xlabels = [str(i) + 'π' for i in range(2 * n + 1)]; plt.scatter(y1, label = 'periodic signal'); plt.scatter(y2, label = 'decaying signal', marker = 'small', color = 'gold'); plt.plotsize(100, 30); plt.ticks(None, 3); plt.xticks(xticks, xlabels); plt.show()"
```
Access the `ticks`, `xticks`, `yticks` docstrings for more documentation.

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)


<a name="datetime"></a>
# Date Time Plot
To plot dates and/or times use the `string_to_time()` function like in the example below:
```
import plotext as plt
plt.clp()
dates = ["01/01/2021 12:20", "02/01/2021 15:40", "03/01/2021 15:10", "04/01/2021 15:24", "05/01/2021", "05/01/2021 18:10", "05/01/2021 23:20", "06/01/2021 12:10","07/01/2021"]
prices = [100, 110, 130, 140, 150, 160, 170, 180]
dates_x = [plt.string_to_time(el) for el in dates] 
plt.plot(dates_x, prices, marker = ".")
plt.scatter(dates_x, prices, marker = "small")
plt.xticks(dates_x, dates)
plt.title("Date-Time Plot")
plt.xlabel("Date-Time")
plt.ylabel("Stock Price $")
plt.plotsize(100, 30)
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/date.png)
The equivalent direct terminal command line is:

```
python3 -m plotext "import plotext as plt; plt.clp(); dates = ['01/01/2021 12:20', '02/01/2021 15:40', '03/01/2021 15:10', '04/01/2021 15:24', '05/01/2021', '05/01/2021 18:10', '05/01/2021 23:20', '06/01/2021 12:10','07/01/2021']; prices = [100, 110, 130, 140, 150, 160, 170, 180]; dates_x = [plt.string_to_time(el) for el in dates]; plt.plot(dates_x, prices, marker = '.'); plt.scatter(dates_x, prices, marker = 'small'); plt.xticks(dates_x, dates); plt.title('Date-Time Plot'); plt.xlabel('Date-Time'); plt.ylabel('Stock Price $'); plt.plotsize(100, 30); plt.show()"
```
Access the `string_to_time` docstrings for more documentation.

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)



<a name="limits"></a>
# Plot Limits
The plot limits are set automatically, to set them manually you can use the following functions - to be placed before `show()`:

 - `plt.xlim(xmin, xmax)` sets the minimum and maximum limits of the plot on the `x` axis. It requires a list of two numbers, where the first `xmin` sets the left (minimum) limit and the second `xmax` the right (maximum) limit. If one or both values are not provided, they are calculated automatically.
 - `plt.ylim(ymin, ymax)` is the equivalent of `plt.xlim()` but for the `y` axis. It also takes the optional parameter `yaxis` in case multiple y axes are used in the plot.

Here is a coded example:
```
import plotext as plt
l, n = 1000, 2
x = range(1, l + 1)
y = plt.sin(l, n)
plt.scatter(x, y, color = "indigo")
plt.xlim(x[0] - 101, x[-1] + 100)
plt.ylim(-1.2, 1.2)
plt.plotsize(100, 30)
plt.show()
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/limits.png)

The equivalent direct terminal command line is:
```
python3 -m plotext "import plotext as plt; l, n = 1000, 2; x = range(1, l + 1); y = plt.sin(l, n); plt.scatter(x, y, color = 'indigo'); plt.xlim(x[0] - 101, x[-1] + 100); plt.ylim(-1.2, 1.2); plt.plotsize(100, 30); plt.show()"
```

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)




<a name="aspect"></a>
# Plot Aspect
You can personalize the plot aspect in many ways. You could use the following parameters - to be placed inside the `scatter`, `plot`, `bar` and `hist` calls:

 - `marker` sets the marker used to identify each data point to the specified character. For example `plt.scatter(data, marker = "x")`. Access the `markers()` function for further marker codes. 
 - `color = color` sets the color of the `marker` used. Access the `colors()` function for the color codes available. 
 - `fillx = True` fills the area between the data and the `x` axis with data points (if used inside `scatter`) or line points (if used inside `plot`). For example: `plt.plot(data, fillx = True)`. By default `fillx = False`
 - `filly` is the correspondent parameter of `fillx` but for the `y` axis.
 - Note that the functions `bar` and `hist` use the parameter `fill` (instead of `fillx` and `filly`) which is used to fill the bars with colors

You could also use the following functions - to be placed before `show()`:

 - `plotsize(width, height)` sets the width and height of the plot to the desired values. Note that the plot automatically extends to fill the entire terminal: use this function in order to reduce this size. 
 - `title(string)` adds a plot title on the top of the plot.
 - `xlabel(string)` and `ylabel(string)` adds a label for respectively the `x` and `y` axis on the bottom of the plot. If two strings are provided to `plt.ylabel()` the second is indended for the right `y` axis.
 - `grid(xbool, ybool)` adds the `x` grid lines to the plot if `xbool == True` and the `y` grid lines if `ybool == True`. If only one Boolean value is provided both grid lines are set simultaneously.
 - `xaxes(bool1, bool2)` adds the lower `x` axis if `bool1 == True` and the upper `x` axis if `bool2 == True`. If only one boolean value is provided both axes are set simultaneously.
 - `yaxes(bool1, bool2)` adds the left `y` axis if `bool1 == True` and the right `y` axis if `bool2 == True`. If only one boolean value is provided both axes are set simultaneously.
 - `canvas_color(color)` sets the color of the plot canvas alone (the area where the data is plotted).
 - `axes_color(color)` sets the background color of all the labels surrounding the actual plot, i.e. the axes, axes labels and ticks, title and legend, if present.
 - `ticks_color(color)` sets the (full-ground) color of the axes ticks and of the grid lines, if present.
 - `colorless()` (in short `cls()`) removes all colors from the current plot.

Here is a coded example:
```
import plotext as plt
l, n = 1000, 2
x = range(1, l + 1)
y = plt.sin(l, n)
plt.plot(x, y1, label = "periodic signal", color = "violet", marker = "small")
plt.plotsize(100, 30)
plt.grid(True)
plt.title("Plot Style Example")
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.canvas_color("white")
plt.axes_color("cloud")
plt.ticks_color("iron")
plt.xaxes(1, 0)
plt.yaxes(1, 0)
plt.ticks(10)
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/aspect.png)



The equivalent direct terminal command line is:
```
python3 -m plotext "import plotext as plt; l, n = 1000, 2; x = range(1, l + 1); y = plt.sin(l, n); plt.plot(x, y, label = 'periodic signal', color = 'violet', marker = 'small'); plt.plotsize(100, 30); plt.grid(True); plt.title('Plot Style Example'); plt.xlabel('x axis label'); plt.ylabel('y axis label'); plt.canvas_color('white'); plt.axes_color('cloud'); plt.ticks_color('iron'); plt.xaxes(1, 0); plt.yaxes(1, 0); plt.ticks(10); plt.show()"
```

Here are the colors and markers codes:

![colors](https://raw.githubusercontent.com/piccolomo/plotext/master/images/colors.png)

Note: using `flash` will result in an actual white flashing marker (therefore it will not work with white canvas background color).

![colors](https://raw.githubusercontent.com/piccolomo/plotext/master/images/markers.png)


[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)


<a name="subplots"></a> 
# Multiplie Subplots
In order to plot a grid of plots, use the following main functions:
 - `plt.subplots(rows, cols)` creates a matrix of plots with the given number of rows and columns.
 - `plt.subplot(row, col)` access the plot at the given row and column, counting (from 1) from the upper left corner of the matrix of plots, previously set. 

Note that if subplots are manually resized with `plotsize`, they can overflow the figure, in which case they will be cut (and possibly made completely invisible if their size is set to 0). A figure can be automatically resized in the vertical direction to fit all the subplots by passing `allow_scrolling=True` to `show`.

Here is a coded basic example:
```
import plotext as plt
l, n = 1000, 5
y = plt.sin(l, n)

plt.clf()
plt.subplots(2, 1)

plt.subplot(1, 1)
plt.plot(y, yaxis = "right")
plt.plotsize(100, 27)

plt.subplot(2, 1)
plt.hist(y, color = "indigo")
plt.plotsize(100, 27)

plt.show()
# plt.show(allow_scrolling=True)  # if your terminal is less than 54 px in height
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/subplots.png)

The equivalent direct terminal command line is:
```
python3 -m plotext "import plotext as plt; l, n = 1000, 5; y = plt.sin(l, n); plt.clf(); plt.subplots(2, 1); plt.subplot(1, 1); plt.plot(y, yaxis = 'right'); plt.plotsize(100, 27); plt.subplot(2, 1); plt.hist(y, color = 'indigo'); plt.plotsize(100, 27); plt.show()"
```

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)



<a name="streaming"></a>
# Streaming Data
When streaming a continuous flow of data, consider using the following functions:
 - `clear_figure` (in short `clf`) clears the entire figure, including its subplots. 
 - `clear_plot()` (in short `clp()`) clears the plot and all its internal parameters; it is useful when running the same script several times in order to avoid adding the same data to the plot; it is very similar to `cla()` in `matplotlib`.
 - `clear_data()` (in short `cld()`) clear only the plot data (without clearing the plot style).
 - `clear_terminal()` (in short `clt()`) clear the terminal before the actual plot.
 - `sleep(time)` is used in order to reduce a possible screen flickering; for example `sleep(0.01)` would add approximately 10 ms to the computation. Note that the `time` parameters will depend on your processor speed and it needs some manual tweaking.
 - The function `colorless()` is recommended to make the streaming more responsive, but not mandatory.

Here is a coded example:
```
import plotext as plt
import numpy as np
l, n = 1000, 2
x = np.arange(0, l)
xticks = np.linspace(0, l - 1, 5)
xlabels = [str(i) + "π" for i in range(5)]
frames = 100
    
plt.clf()
plt.ylim(-1, 1)
plt.xticks(xticks, xlabels)
plt.yticks([-1, 0, 1])
plt.plotsize(100, 30)
plt.title("Streaming Data")
plt.colorless()

for i in range(frames):
    y = plt.sin(l, n, 0, phase = 2 * i  / frames)	

    plt.cld()
    plt.clt()
    plt.scatter(x, y, marker = "dot")
    plt.sleep(0.01)
    plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/stream.gif)

The equivalent direct terminal command line is:
```
python3 -m plotext "import plotext as plt; import numpy as np; l, n = 1000, 2; x = np.arange(0, l); xticks = np.linspace(0, l - 1, 5); xlabels = [str(i) + 'pi' for i in range(5)]; frames = 100; plt.clf(); plt.ylim(-1, 1); plt.xticks(xticks, xlabels); plt.yticks([-1, 0, 1]); plt.plotsize(100, 30); plt.title('Streaming Data'); plt.colorless();  y = lambda i: plt.sin(l, n, 0, phase = 2 * i  / frames); [(plt.cld(), plt.scatter(x, y(i), marker = 'dot'), plt.sleep(0.01), plt.show()) for i in range(frames)]"
```
Plotting the same data using `matplotlib` was roughly 10 to 50 times slower on my Linux-based machine (depending on the colors settings and data size).

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)


<a name="other"></a>
## Other Functions
- `savefig(path)` saves the plot as a text file at the `path` provided. Note: no colors are preserved at the moment, when saving.
- `get_canvas()` return the plot final canvas as a string. To be used after the `show` function possibly with its `hide` parameter set to True.
- `version()` returns the version of the current installed `plotext` package.
- `sin()` returns a sinusoidal function useful for testing. Access its docstring for further documentation.
- `plt.docstrings()` prints all the available doc-strings.
- `test()` runs all the above tests in sequence:
```
import plotext as plt
plt.test()
```

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)


<a name="install"></a>
## Installation
To install the latest version of `plotext` use: `pip install plotext --upgrade` or in Linux `sudo -H pip install plotext --upgrade`

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)


<a name="updates"></a>
## Main Updates:
 - from version 3.1.0: fixed issue of plot resizing reported by @nicrip
 - from version 3.0.1: added `clear_data()` and `test()` functions

from version 2:

 - Direct terminal command line tool added
 - Smaller marker added (with improved resolution), with new marker codes
 - Subplots added
 - Log plots added
 - Stem plot added
 - Double Y Axes added
 - Bar plot added
 - Date/Time Plot added
 - `get_canvas()` function added
 - `sin()` function added
 - `clear_figure()` function added
 - `figsize()` changed to `plotsize()`
 - `nocolor()` changed to `colorless()`
 - `frame` option removed and replaced with `xaxes` and `yaxes`.
 - most of the code re-written

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)


<a name="plans"></a>
## Future Plans:
Under request (just open an issue report about it):
- higher resolution marker support for Windows (the one named `small`)
- log scale for bar/hist plot
- subplots with `columnspan` and `rowspan` parameters
- Spider/Idle terminal support or for other more rare terminals (if possible)
- saving plot text files with color (not sure if useful)

Any help or new ideas are welcomed.

[ Table of Contents ](https://github.com/piccolomo/plotext#table-of-contents)
