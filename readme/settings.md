# Plot Settings

- [Plot Size](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-size)
- [Plot Limits](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-limits)
- [Axes Ticks](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#axes-ticks)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Plot Size

By default the plot size adapts to the dimensions of the terminal. To change this behaviour, use one of the following functions:

 - `plt.plot_size()` to set the plot size to the desired `width` and `height`, in units of character dimensions.

 - `plt.limit_size()` to set, whatever or not, to limit the plot size to, respectively, the terminal width and height. This function is only available for the main figure and not for its subplots, if present.

 - `plt.take_mine()`: in a matrix of subplot, the final widths/heights will be the same for each column/row and, by default, the maximum is taken. If `take_min()` is called, the minimum is considered instead.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-aspect)


## Plot Labels

You could easily add the following text labels to the plot:

- a **title** on the top of the active plot with `plt.title()`.
 
- the **x axes labels** with `plt.xlabel()`: its parameter `xside` is used to address a specific `x` axis , `"lower"` or `"upper"` (in short `1` or `2`). 

- Analogously the **y axes labels** with `plt.ylabel()`: `yside` parameter, is used to address a specific `y` axis , `"left"` or `"right"` (in short `1` or `2`).

- The axes labels will all appear at the bottom of the plot, with the exception of the upper `x` axis label, which will appear on the top center of the plot, moving the plot title to the top left, if present.

- To change the labels colors and styles, use the functions `ticks_colors()` and `ticks_style()`, as explained in [this section](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#colors).
 
[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-aspect)



## Plot Limits

The plot limits are set automatically; to set them manually you can use the following functions:

 - `plt.xlim()` sets the minimum and maximum limits on the x axis. To address a specific x axis (`lower` or `upper`) use the `xside` parameter as describer in the previous section. 

 - `plt.ylim()` sets the minimum and maximum limits on the y axis. To address a specific y axis (`left` or `right`) use the `yside` parameter.


[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-aspect)


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

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-aspect)