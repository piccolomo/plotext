# Plot Aspect

- [ Plot Limits ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-limits)
- [ Axes Ticks ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#axes-ticks)
- [ Plot Size ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-size)
- [ Axes and Grids ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#axes-and-grids)
- [ Plot Labels ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-labels)
- [ Plot Markers ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-markers)
- [ Marker Colors ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#marker-colors)
- [ Plot Colors ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-colors)

[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)



## Plot Limits

The plot limits are set automatically; to set them manually you can use the following functions:

 - `plt.xlim(xmin, xmax)` sets the minimum and maximum limits on the x axis. The parameter `xside` is used to access a specific `x` axis (lower or upper).

 - `plt.ylim(ymin, ymax)` sets the minimum and maximum limits on the y axis. The parameter `yside` is used to access a specific `y` axis (left or right).
 
Here is a coded example:

```
import plotext as plt

l = 1000
x = range(1, l + 1)
y = plt.sin(1, l)
plt.scatter(x, y)
plt.xlim(x[0] - 101, x[-1] + 100)
plt.ylim(-1.2, 1.2)
plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; l = 1000; x = range(1, l + 1); y = plt.sin(1, l); plt.scatter(x, y); plt.xlim(x[0] - 101, x[-1] + 100); plt.ylim(-1.2, 1.2); plt.show()"
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/limits.png)


[ Plot Aspect Menu ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)



## Axes Ticks

To change the numerical ticks on the `x` axis, you could use one of the following functions:

 - `plt.xfrequency(xfreq)` sets the numerical ticks frequency on the `x` axis to an integer.
 
 - `plt.xticks(xticks)` manually sets the x ticks to the list provided. If two lists are provided, the second is intended as the list of `labels` to be placed at the coordinates provided by the first.

In both cases, the parameter `xside` is used to access a specific `x` axis (lower or upper).

Naturally, the functions used to specify the plot limits on the `y` axis behave similarly and are `plt.yfrequency(yfreq)`, `plt.yticks(yticks)`.

Here is a coded example:
```
import plotext as plt

l, p = 1000, 3
y = plt.sin(1, p, l)

plt.scatter(y)

xticks = [l * i / (2 * p)  for i in range(2 * p + 1)]
xlabels = [str(i) + "π" for i in range(2 * p + 1)]

plt.xticks(xticks, xlabels)
plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; l, p = 1000, 3; y = plt.sin(1, p, l); plt.scatter(y); xticks = [l * i / (2 * p)  for i in range(2 * p + 1)]; xlabels = [str(i) + 'π' for i in range(2 * p + 1)]; plt.xticks(xticks, xlabels); plt.show()"
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/ticks.png)

[ Plot Aspect Menu ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)




## Plot Size

By default the plot size adapts to the dimensions of the terminal. To alter the plot size use one of the following functions:

 - `plt.plot_size(width, height)` to set the width and height of the plot to the desired values.

 - `plt.limit_size(boolx, booly)` to set whatever or not to limit both plot dimensions to the terminal width and height.

[ Plot Aspect Menu ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)




## Axes and Grids

 - Use the function `plt.xaxis(bool)` to specify whatever or not to show the x axis: the parameter `xside` is used to specify the `x` axis (lower or upper) to address.

 - The function `plt.yaxis(bool)` behaves analogously but for the `y` axis.

 - To control all axes simultaneously, use the function `plt.frame(bool)` instead, which will show or remove the plot frame (composed by all 4 axes).

 - The function `grid(xbool, ybool)` is used to add or remove the horizontal and vertical grid lines. A single Boolean sets both grid lines simultaneously. 

[ Plot Aspect Menu ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)



## Plot Labels

You could easily add the following text labels to the plot:

 - a title with `plt.title(string)` which adds a title on the top of the plot.
 
 - the axes labels with `plt.xlabel(string)` and `plt.ylabel(string)`. The parameters `xside` and `yside` are used to address specific axes. The labels will all appear at the bottom of the plot, with the exception of the upper `x` label, which will appear on the upper right side of the plot.

Here is an example:

```
import plotext as plt

plt.scatter(plt.sin())

plt.plot_size(100, 30)
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
```
python3 -c "import plotext as plt; plt.scatter(plt.sin()); plt.plot_size(100, 30); plt.frame(True); plt.grid(True); plt.title('Plot Title'); plt.xlabel('Lower'); plt.ylabel('Left'); plt.xlabel('Upper', xside = 'upper'); plt.ylabel('Right', yside = 'right'); plt.show()"
```

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/labels.png)
 
[ Plot Aspect Menu ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)




## Plot Markers

To manually specify which marker to use, use the parameter `marker`, available in all plotting functions (eg: `plt.scatter(data, marker = "x")`). You could provide the following:

- `None` (as by default): in this case, the marker is set automatically. 

- A **single character**: if the space character " ", the plot will be invisible. 

- A **list of specific markers**, one for each data point: its length will automatically adapt to the data length.

- One of the following **marker codes** which will translate in the single character specified: sd █, dot •, dollar $, euro €, bitcoin ฿, at @, heart  ♥, smile  ☺, gclef 𝄞, note 𝅘𝅥, shamrock ☘, atom ⚛, snowflake ❄, lightning 🌩, queen ♕, king ♔, cross ♰, yinyang ☯, om ॐ, osiris 𓂀, zero  🯰, one 🯱, two 🯲, three  🯳, four 🯴, five 🯵, six 🯶, seven  🯷, eight 🯸, nine   🯹. Some of those markers codes are not availabel in Windows.

- The marker code "sd" stands for "standard resolution". To plot in higher resolution use one of following two extra codes instead:

    - **hd** for high resolution, which uses 2 x 2 unicode block characters, such as ▞.

    - **fhd** for full high resolution, which uses 3 x 2 unicode block characters, such as 🬗. This is the default marker of the first data set plotted, and it is not available in Windows. 

Further documentation is available using `plt.markers()`.

[ Plot Aspect Menu ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)



## Marker Colors

To specify the marker colors use the `color` parameter. You could provide the following:

- `None` (as by default): in this case, the color is set automatically. 

- the following **color string codes**: `default, black, red, green, yellow, blue, magenta, cyan, white, bright-black, bright-red, bright-green, bright-yellow, bright-blue, bright-magenta, bright-cyan, bright-white`. Using `default` will result in the standard terminal coloring. 

    - along side the string color codes, one can add as many **styles** as desired among these: `bold, dim, italic, underline, double-underline, strike, inverted, flash`. The color and styles must be separated by a space. Using `flash` will result in an actual white flashing marker (therefore it will not work with white canvas background color).

- **an integer between 0 and 255** to plot 256 colors.

- **an RGB color** consisting of a tuple of three integer values (red, green, blue), each between 0 and 255, to obtain the most realistic color rendering.

- a list of color codes, one for each data point.

[ Plot Aspect Menu ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)



## Plot Colors

Colors could also be applied to the rest of the plot, using the following functions:

- `plt.canvas_color(color)` to set the background color of the plot canvas alone (the area where the data is plotted).

- `plt.axes_color(color)` to sets the background color of the axes, axes numerical ticks, axes labels and title.

- `plt.ticks_color(color)` sets the (full-ground) color of the axes ticks, the grid lines, title, labels and legend, if present.

The color codes conventions are analogous to the [ Marker Colors ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#marker-colors) except that for background colors - naturally - the styles won't work. 

To remove the plot colors, use one of the following functions:

- `plt.clear_color()` - in short `plt.clc()` - to removes all colors from the current subplot.

- `plt.colorless()` - in short `plt.cls()` - to remove all colors from the entire figure.

Here is an example:

```
import plotext as plt
l = 256
plt.plot(plt.sin(length = l), marker = "fhd", color = list(range(l)))

plt.title("Plot Colors")
plt.canvas_color((200, 200, 200)) # rgb coloring
plt.axes_color("bright-black")
plt.ticks_color("bright-yellow")

plt.plot_size(100, 30)
plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; l = 256; plt.plot(plt.sin(length = l), marker = 'fhd', color = list(range(l))); plt.title('Plot Colors'); plt.canvas_color((200, 200, 200)); plt.axes_color('bright-black'); plt.ticks_color('bright-yellow'); plt.plot_size(100, 30); plt.show()"
```

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/colors.png)

[ Plot Aspect Menu ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)
