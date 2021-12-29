[Plotext Guide](https://github.com/piccolomo/plotext#guide)


# Plot Aspect

- [Plot Limits](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-limits)
- [Axes Ticks](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#axes-ticks)
- [Plot Size](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-size)
- [Axes, Grids and Lines](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#axes-and-grids)
- [Plot Labels](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-labels)
- [Plot Markers](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-markers)
- [Marker Colors](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#marker-colors)
- [Plot Colors](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-colors)


## Plot Limits

The plot limits are set automatically; to set them manually you can use the following functions:

 - `plt.xlim(xmin, xmax)` sets the minimum and maximum limits on the x axis. The parameter `xside` is used to access a specific `x` axis (lower or upper).

 - `plt.ylim(ymin, ymax)` sets the minimum and maximum limits on the y axis. The parameter `yside` is used to access a specific `y` axis (left or right).
 
Here is a coded example:

```python
import plotext as plt

l = 1000
x = range(1, l + 1)
y = plt.sin(length = l)
plt.scatter(x, y)
plt.xlim(x[0] - 101, x[-1] + 100)
plt.ylim(-1.2, 1.2)
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; l = 1000; x = range(1, l + 1); y = plt.sin(1, l); plt.scatter(x, y); plt.xlim(x[0] - 101, x[-1] + 100); plt.ylim(-1.2, 1.2); plt.show()"
```
![limits](https://raw.githubusercontent.com/piccolomo/plotext/master/images/limits.png)


[Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Axes Ticks

To change the numerical ticks on the `x` axis, you could use one of the following functions:

 - `plt.xfrequency(xfreq)` sets the numerical ticks frequency on the `x` axis to an integer.

 - `plt.xticks(xticks)` manually sets the `x` axis ticks to the list provided. If two lists are provided, the second is intended as the list of `labels` to be placed at the coordinates provided by the first.

In both cases, the parameter `xside` is used to access a specific `x` axis (lower or upper).

Naturally, the functions used to specify the plot limits on the `y` axis, behave similarly and are `plt.yfrequency(yfreq)`, `plt.yticks(yticks)`.

Here is a coded example:
```python
import plotext as plt

l, p = 1000, 3
y = plt.sin(periods = p, length = l)

plt.scatter(y)

xticks = [l * i / (2 * p)  for i in range(2 * p + 1)]
xlabels = [str(i) + "π" for i in range(2 * p + 1)]

plt.xticks(xticks, xlabels)
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; l, p = 1000, 3; y = plt.sin(periods = p, length = l); plt.scatter(y); xticks = [l * i / (2 * p)  for i in range(2 * p + 1)]; xlabels = [str(i) + 'π' for i in range(2 * p + 1)]; plt.xticks(xticks, xlabels); plt.show()"
```
![ticks](https://raw.githubusercontent.com/piccolomo/plotext/master/images/ticks.png)

[Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)



## Plot Size

By default the plot size adapts to the dimensions of the terminal. To alter the plot size use one of the following functions:

 - `plt.plot_size(width, height)` to set the width and height of the plot to the desired values, in units of character dimensions.

 - `plt.limit_size(boolx, booly)` to set, whatever or not, to limit the plot width and height to, respectively, the terminal width and height.

[Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Axes and Grid Lines

 - Use the function `plt.xaxis(bool)` to specify whatever or not to show the `x` axis: the parameter `xside` is used to specify which `x` axis (lower or upper) to address.

 - The function `plt.yaxis(bool)` behaves analogously but for the `y` axis.

 - To control all axes simultaneously, use the function `plt.frame(bool)` instead, which will show or remove the plot frame (composed by all 4 axes).

 - The function `grid(xbool, ybool)` is used to add or remove the horizontal and vertical grid lines. A single Boolean sets both grid lines simultaneously. 
 
 - The function `vertical_line(coordinate, color, xside)` plots a vertical line at the given `coordinate` and specified `color`; the parameter `xside` to specify which `x` axis, `lower` (as by default) or `upper`, the parameter `coordinate` refers to.

 - The function `horizontal_line(coordinate, color, yside)` plots a horizontal line at the given `coordinate` and specified `color`; the parameter `yside` to specify which `y` axis, `left` (as by default) or `right`, the parameter `coordinate` refers to.

[Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Plot Labels

You could easily add the following text labels to the plot:

 - a title with `plt.title(string)` which adds a title on the top of the plot.
 
 - the axes labels with `plt.xlabel(string)` and `plt.ylabel(string)`. The parameters `xside` and `yside` are used to address specific axes. The labels will all appear at the bottom of the plot, with the exception of the upper `x` label, which will appear on the upper right side of the plot.

Here is an example:

```python
import plotext as plt

plt.plot(plt.sin())

plt.plot_size(150, 45)
plt.frame(True)
plt.grid(True)

plt.title("Plot Title")

plt.xlabel("Lower")
plt.ylabel("Left")

plt.xlabel("Upper", xside = "upper")
plt.ylabel("Right", yside = "right")

plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; plt.plot(plt.sin()); plt.plot_size(150, 45); plt.frame(True); plt.grid(True); plt.title('Plot Title'); plt.xlabel('Lower'); plt.ylabel('Left'); plt.xlabel('Upper', xside = 'upper'); plt.ylabel('Right', yside = 'right'); plt.show()"
```

![labels](https://raw.githubusercontent.com/piccolomo/plotext/master/images/labels.png)
 
[Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Plot Markers

To manually specify which marker to use, use the parameter `marker`, available in all plotting functions (eg: `plt.scatter(data, marker = "x")`). You could provide the following:

- `None` (as by default) to set the marker automatically to `hd` in Unix systems and to `dot` in Windows (see below).

- A **single character**: if the space character " ", the plot will be invisible. 

- A **list of specific markers**, one for each data point: its length will automatically adapt to the data length.

- One of the following **marker codes** which will translate in the single character specified: 

  ![markers](https://raw.githubusercontent.com/piccolomo/plotext/master/images/markers.png)

   **Note**: some of these are not available in Windows.

- The marker code `sd` stands for "standard resolution". To plot in **higher resolution** use one of following two extra codes instead:

    - **`hd`** for *high resolution*, which uses 2 x 2 unicode block characters, such as ▞. 

    - **`fhd`** for *full high resolution*, which uses 3 x 2 unicode block characters, such as 🬗.  **Note**: this marker works only in Unix systems and only in some terminals.

The same documentation is available using `plt.markers()`.

[Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Marker Colors

These are the types of color codes that could be provided to the `color` parameter of any plotting function, as well as the `fullground` parameter of the function `plt.colorize()`, or as input for the functions `plt.canvas_color()`, `plt.axes_color()` and `plt.ticks_color()`:

- `None` (as by default), to set the color automatically. 

- The following **color string codes**: 

  ![color-codes](https://raw.githubusercontent.com/piccolomo/plotext/master/images/color-codes.png)

  **Note**: `default` will use the terminal default color settings.

- Along side the previous string color codes, one can add as many styles as desired among the following **string style codes**: 

  ![style-codes](https://raw.githubusercontent.com/piccolomo/plotext/master/images/style-codes.png)

   **Note**: the color and style codes must be separated by a space. Using `flash` will result in an actual white flashing marker (therefore it will not work with `bright-white` canvas background color). Naturally those style won't work as background colors.

- An **integer between 0 and 255**, resulting in the following colors:

  ![integer-codes](https://raw.githubusercontent.com/piccolomo/plotext/master/images/integer-codes.png)

  **Note**: the first 16 produce the same results as the previous string color codes.

- An **RGB color** consisting of a tuple of three values (red, green, blue), each between 0 and 255, to obtain the most realistic color rendering.

- a **list of color codes** to give a different color to each plot marker: the length of the list of colors will adapt to the length of the data set.

**Background Colors**: all color codes above are valid also as background color, if provided to the `background` parameter of the function `plt.colorize()` or as input for the functions `plt.canvas_color()`, and `plt.axes_color()`. For example, here is the effect of the string color codes above, intended as background color: 

![background-codes](https://raw.githubusercontent.com/piccolomo/plotext/master/images/background-codes.png)

The same documentation is available using `plt.colors()`.

[Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Plot Colors

Colors could also be applied to the rest of the plot, using the following functions:

- `plt.canvas_color(color)` to set the background color of the plot canvas alone (the area where the data is plotted).

- `plt.axes_color(color)` to sets the background color of the axes, axes numerical ticks, axes labels and plot title.

- `plt.ticks_color(color)` sets the (fullground) color of the axes ticks, the grid lines, title, labels and legend, if present.

The color codes conventions are explained in section [Marker Colors](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#marker-colors).

To remove the plot colors, use one of the following functions:

- `plt.clear_color()` - in short `plt.clc()` - to removes all colors from the current subplot.

- `plt.colorless()` - in short `plt.cls()` - to remove all colors from the entire figure.

Here is an example:

```python
import plotext as plt
l = 256
plt.plot(plt.sin(length = l), marker = "fhd", color = list(range(l)))

plt.title("Plot Colors")
plt.canvas_color(254) 
plt.axes_color((20, 40, 100)) # rgb coloring
plt.ticks_color("bright-yellow")

plt.plot_size(150, 45)
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; l = 256; plt.plot(plt.sin(length = l), marker = 'fhd', color = list(range(l))); plt.title('Plot Colors'); plt.canvas_color(254); plt.axes_color((20, 40, 100)); plt.ticks_color('bright-yellow'); plt.plot_size(150, 45); plt.show()"
```

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/colors.png)

[Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)

[Plotext Guide](https://github.com/piccolomo/plotext#guide)