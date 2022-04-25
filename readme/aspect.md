# Plot Aspect

- [Plot Size](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-size)
- [Plot Labels](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-labels)
- [Plot Limits](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-limits)
- [Axes Ticks](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#axes-ticks)
- [Plot Lines](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-lines)
- [Colors](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors)
- [Markers](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#markers)

[Plotext Guide](https://github.com/piccolomo/plotext#guide)


## Plot Size

By default the plot size adapts to the dimensions of the terminal. To change this behaviour, use one of the following functions:

 - `plt.plot_size()` to set the plot size to the desired `width` and `height`, in units of character dimensions.

 - `plt.limit_size()` to set, whatever or not, to limit the plot size to, respectively, the terminal width and height. This function is only available for the main figure and not for its subplots, if present.

 - `plt.take_mine()`: in a matrix of subplot, the final widths/heights will be the same for each column/row and, by default, the maximum is taken. If `take_min()` is called, the minimum is considered instead.

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Plot Labels

You could easily add the following text labels to the plot:

- a **title** on the top of the active plot with `plt.title()`.
 
- the **x axes labels** with `plt.xlabel()`: its parameter `xside` is used to address a specific `x` axis , `"lower"` or `"upper"` (in short `1` or `2`). 

- Analogously the **y axes labels** with `plt.ylabel()`: `yside` parameter, is used to address a specific `y` axis , `"left"` or `"right"` (in short `1` or `2`).

- The axes labels will all appear at the bottom of the plot, with the exception of the upper `x` axis label, which will appear on the top center of the plot, moving the plot title to the top left, if present.

- To change the labels colors and styles, use the functions `ticks_colors()` and `ticks_style()`, as explained in [this section](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors)
 
[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)



## Plot Limits

The plot limits are set automatically; to set them manually you can use the following functions:

 - `plt.xlim()` sets the minimum and maximum limits on the x axis. To address a specific x axis (`lower` or `upper`) use the `xside` parameter as describer in the previous section. 

 - `plt.ylim()` sets the minimum and maximum limits on the y axis. To address a specific y axis (`left` or `right`) use the `yside` parameter


[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Axes Ticks

To change the numerical ticks on the `x` axis, you could use one of the following functions:

- `plt.xfrequency()` to set the numerical ticks frequency on the `x` axis, to an integer value.

- `plt.xticks()` to manually sets the `x` axis ticks to the list provided. If two lists are provided, the second is intended as the list of `labels` to be placed at the coordinates provided by the first.

- In both cases, the parameter `xside` is used to address a specific `x` axis (`lower` or `upper`).

- Naturally, the functions used to specify the plot limits on the `y` axis, are `plt.yfrequency()`, `plt.yticks()` and behave similarly.

Here is a coded example:
```python
import plotext as plt
l, p = 300, 2
plt.plot(plt.sin(length = l, periods = p), label = "My Signal")
plt.plotsize(100, 30)
plt.title('Some Smart Title')
plt.xlabel('Time')
plt.ylabel('Movement')
plt.ticks_color('red')
plt.ticks_style('bold')
plt.xlim(-l//10, l + l//10)
plt.ylim(-1.5, 1.5)
xticks = [l * i / (2 * p)  for i in range(2 * p + 1)]
xlabels = [str(i) + "π" for i in range(2 * p + 1)]
plt.xticks(xticks, xlabels)
plt.yfrequency(5)
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; l, p = 300, 2; plt.plot(plt.sin(length = l, periods = p), label = 'My Signal'); plt.plotsize(100, 30); plt.title('Some Smart Title'); plt.xlabel('Time'); plt.ylabel('Movement'); plt.ticks_color('red'); plt.ticks_style('bold'); plt.xlim(-l//10, l + l//10); plt.ylim(-1.5, 1.5); xticks = [l * i / (2 * p)  for i in range(2 * p + 1)]; xlabels = [str(i) + 'π' for i in range(2 * p + 1)]; plt.xticks(xticks, xlabels); plt.yfrequency(5); plt.show()"
```
![ticks](https://raw.githubusercontent.com/piccolomo/plotext/master/images/ticks.png)

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)



## Axes and Grid Lines

Here are the main functions used to alter the plot lines:

- `plt.xaxes()` to set whatever or not to show the `x` axes; it accepts two Boolean inputs, one for each `x` axis (`lower` and `upper`).

- `plt.yaxes()` to set whatever or not to show the `y` axes; it accepts two Boolean inputs, one for each `y` axis (`left` and `right`).
 
- To control all axes simultaneously, use the function `plt.frame()` instead, which will show or remove the plot frame (composed of all 4 axes). It require a single Boolean.

- The function `plt.grid()` is used to add or remove the horizontal and vertical grid lines and requires two Boolean inputs.

- To add extra lines at some specific coordinates use the functions `vertical_line()` and `horizontal_line()` ad explained in [this section](https://github.com/piccolomo/plotext/blob/master/readme/tools.md#extra-lines).

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Colors

Colors could easily applied to the entire plot, using the following functions:

- `canvas_color()` to set the background color of the plot canvas alone (the area where the data is plotted).

- `axes_color()` to sets the background color of the axes, axes numerical ticks, axes labels and plot title.

- `ticks_color()` sets the (fullground) color of the axes ticks, the grid lines, title, and legend labels, if present.

- `ticks_style()` sets the style of the axes ticks, title, and legend labels, if present.

To quickly set all those values at once use the function `theme()`. To check the available themes use the function `themes()`; here is its output: 

![themes](https://raw.githubusercontent.com/piccolomo/plotext/master/images/themes.png)
`
Note: to add, tweak, rename any theme presented, please feel free to open an issue dropping your favourite combination of canvas, axes, ticks color and style together with 3 signal colors in sequence: any idea is welcomed. 

To remove all plot colors and styles from the current subplot, use `clear_color()` - in short `clc()`, which is equivalent to `theme('clear')`

If instead you want to set the colors manually, here are the types of color codes that could be provided as input for the functions `canvas_color()`, `axes_color()` and `ticks_color()` or to the `color` parameter of any plotting function, as well as the `fullground` or `background` parameter of the function `plt.colorize()`:

- The following **color string codes**: 

  ![color-codes](https://raw.githubusercontent.com/piccolomo/plotext/master/images/color-codes.png)

  `default` will use the default terminal color.

- An **integer between 0 and 255**, resulting in the following colors:

  ![integer-codes](https://raw.githubusercontent.com/piccolomo/plotext/master/images/integer-codes.png)

  Note: the first 16 produce the same results as the previous string color codes.

- An **RGB color** consisting of a tuple of three values (red, green, blue), each between 0 and 255, to obtain the most realistic color rendering.

- A **list of color codes** to give a different color to each plot marker: the length of the list of colors will adapt to the length of the data set. Each color could be of a different kind (string, integer or rgb).

- Access the function `colors()` for the available string and integer codes.


Finally these are the available **style codes** that could be provided as input to the function ticks_style() or to the `style` parameter of any plotting function, including `colorize()`:

![style-codes](https://raw.githubusercontent.com/piccolomo/plotext/master/images/style-codes.png)

- any number of styles could be used at the same time, provided they are separated by a space. 

- using `flash` will result in an actual white flashing marker.

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)



## Plot Markers

To specify which marker to use, use the parameter `marker`, available for most plotting functions, eg: `plt.scatter(data, marker = "x")`. You could provide the following:

- A **single character**: if the space character, the plot will be invisible. 

- A **list of specific markers**, one for each data point: its length will automatically adapt to the data set.

- One of the following **marker codes** which will translate in the marker specified (some may not be available in Windows): 

  ![markers](https://raw.githubusercontent.com/piccolomo/plotext/master/images/markers.png)

- The marker code `sd` stands for "standard resolution".

- **`hd`** stands for *high resolution*, which uses 2 x 2 unicode block characters, such as ▞. 

- **`fhd`** stands for *full high resolution*, which uses 3 x 2 unicode block characters, such as 🬗.  This marker works only in Unix systems and only in some terminals.

- Access the function `markers()` for the available marker codes.

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)