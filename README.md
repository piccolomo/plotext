Plotting directly on terminal.


# Scatter Plot
Use `plotext` to plot data directly on terminal: the syntax is very similar to `matplotlib`. Here is an example:
```
import plotext as plt
import numpy as np

l = 100
x = np.arange(0, l + 1)
f = 2 * np.pi / l
y = np.sin(2 * f * x)

plt.scatter(y)
plt.show()
```
which outputs this plot on terminal:
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/scatter.png)
Each data point is represented by the character • and the plot automatically extends to fill the entire terminal.


# Line Plot
For a line plot use the the `plot` function instead:
```
import plotext as plt
import numpy as np

l = 1000
x = np.arange(0, l + 1)
f = 2 * np.pi / l
y = np.sin(2 * f * x)

plt.plot(x, y)
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/plot.png)
Incidentally here we have shown that both the `x` and `y` coordinates could be inputted in either the `plot` or `scatter` function (or `y` alone as in the first example).


# Multiple Data
Multiple data sets could be plotted using consecutive `scatter` or `plot` functions:
```
import plotext as plt
import numpy as np

l = 1000
x = np.arange(0, l + 1)
f = 2 * np.pi / l
y1 = np.sin(2 * f * x)
y2 = y1 * np.exp(-0.25 * f * x)
plt.plot(x, y1, label = "periodic signal")
plt.scatter(x, y2, label = "decaying signal")
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/multiple.png)
where using the `label` parameter, a legend is automatically added in the upper left corner of the plot.

# Plot Aspect
You can personalize the plot aspect in many ways. Here is an example:
```
import plotext as plt
import numpy as np

l = 1000
x = np.arange(0, l + 1)
n = 2
f = n * np.pi / l
y1 = np.sin(n * f * x)
y2 = y1 * np.exp(-0.25 * f * x)

plt.plot(x, y1, label="periodic signal", line_color="tomato")
plt.scatter(x, y2, label="decaying signal", point_color="blue")
plt.canvas_size(150, 40)
plt.grid(1)
plt.title("plotext demonstrative plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.canvas_color("white")
plt.facecolor("cloud")
plt.ticks_color("iron")
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/aspect.png)
Here we have changed the color of each line plotted, changed the figure dimensions, added a title on the top and the axes labels on the bottom, changed the background color of the canvas (`canvas_color`), the color of the surrounding elements (`facecolor`) and the ticks full-ground color (`ticks_color`).

# Data Ticks
You can change the numerical ticks on both axes:
```
import plotext as plt
import numpy as np

l = 1000
x = np.arange(0, l + 1)
n = 2
f = n * np.pi / l
y1 = np.sin(n * f * x)
y2 = y1 * np.exp(-0.25 * f * x)
xticks = np.arange(0, l + l / (2 * n), l / (2 * n))
xlabels = [str(i) + "𝜋" for i in range(2*n+1)]

plt.plot(x, y1, label="periodic signal")
plt.scatter(x, y2, label="decaying signal")
plt.ticks(7)
plt.xticks(xticks, xlabels) 
plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/ticks.png)
where we have first set 7 ticks on both axes (using `plt.ticks()`) and then we have directly changed only the x axis ticks coordinates and corresponding labels (with `plt.xticks()`).


# Streaming Data
You can use plotext to plot a continuous flow of data:
```
import plotext as plt
import numpy as np

n = 2
frames = 18
l = 30 * frames
f = 2 * np.pi / l
x = np.arange(0, l)
xticks = np.arange(0, l + l / (2 * n), l / (2 * n))
xlabels = [str(i) + "π" for i in range(2*(n+1))]
for i in range(frames):
    y = np.sin(n * f * x + 2 * np.pi / frames * i)
    plt.clear_terminal()
    plt.clear_plot()
    plt.scatter(x, y, point_color = "blue")
    plt.ylim(-1, 1)
    plt.canvas_size(150, 40)
    plt.title("plotting streaming data using plotext")
    plt.ticks_color("blue")
    plt.xticks(xticks, xlabels)
    plt.sleep(0.001)
    plt.show()
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/stream.gif)
where before each plot we have used the function `clear_terminal` (or in short `clt`) to clear the terminal, and the function `clear_plot` (or short `clp`) to resets all the plot parameters to their default value, including the data coordinates. Without it, the previous code would add the trailing data to the same plot.
Also note that we have set the plot limits, on the `y` axis, using `ylim`. Finally, in order to reduce a possible screen flickering, we have used the `sleep` function: an input of, for example, `0.001` to it would add approximately `0.001` secs to the computation; this `time` parameters will depend on your processor speed and it needs some manual tweaking.
Plotting the same data using `matplotlib` was roughly 15 to 50 times slower on my Linux-based machine (depending on the colors and data size).

## Other Functions
- **fill** is a parameter (of the `scatter` or `plot` function) which allows to fill the area between the data and the `y=0` level:
```
import plotext as plt
import numpy as np

l = 1000
x = np.arange(0, l + 1)
f = 2 * np.pi / l
y = np.sin(2 * f * x)
plt.scatter(x, y, point_color="blue", fill=True)
plt.ylim(-1.2 , 1.2)
plt.canvas_size(150, 40)
plt.title("plotext demonstrative plot using fill")
plt.canvas_color("cloud")
plt.facecolor("iron")
plt.ticks_color("gold")
plt.show()
```
![colors](https://raw.githubusercontent.com/piccolomo/plotext/master/images/fill.png)

- **set_legend** provides and alternative way to set the labels of each plot (as a list of strings) to be printed as a legend. If all labels are an empty string, no legend will be printed. Here is the idea:
```
plt.scatter(y1)
plt.plot(y2)
plt.set_legend(["signal 1", "signal2"])
plt.show()
```
- **save_fig** saves your plot as a text file. Here is the idea:
```
plt.scatter(y)
plt.show()
plt.save_fig(path)
```
where `path` is the file address where the data will be written. Note that (for now), this function doesn't preserve the plot colors.

- **colors** You can uce `plt.colors()` to see the available full-ground and background color codes. Here is the output for simplicity:
![colors](https://raw.githubusercontent.com/piccolomo/plotext/master/images/colors.png)
where using `flash` will result in an actually flashing character. 

- **version** In order to check the installed plotext version use `plt.version()` 

### Other Documentation
Other relevant documentation could be accessed using the following commands:
```
print(plx.scatter.__doc__)
print(plx.plot.__doc__)
print(plx.set_xticks.__doc__)
print(plx.set_yticks.__doc__)
print(plx.show.__doc__)
print(plx.clear_terminal.__doc__)
print(plx.clear_plot.__doc__)
print(plx.sleep.__doc__)
print(plx.save_fig.__doc__)
```

### Installation
Use `pip install plotext --upgrade` 


### Main Updates:
- the plot now shows the actual data ticks using a simpler algorithm (no necessity for `ticks_length`).
- `ticks_number` is now simply `ticks`
- set functions like plt.set_title have reduced to `plt.title()`
- an optional grid can be added
- `fill` option added
- `axes_color` is now `facecolor` to adapt to matplotlib standards
- new legend positioning
- new color codes
- code restructured and revised. 


### Future Plans:
Any help on the following or new ideas is more then welcomed.

- creation of an *histogram plot*.
- creation of logarithmic plots
- data ticks for time based data.
- color and terminal size support for IDLE python editor and compiler.
- same as previous point but for Spider. 
- saving text files with color.
