# Plot Settings
- [Plot Size](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-size)
- [Plot Limits](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-limits)
- [Axes Ticks](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#axes-ticks)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Plot Size
By default the plot size adapts to the dimensions of the terminal. To change this behaviour, use the following functions:

 - `limit_size()` to set, whatever or not, to **limit or not the plot size to the terminal dimensions**. It requires to Boolean (one for each dimension) and it is only available for the main figure and not for its subplots, if present, and should be used before `plot_size()`,
 - `plot_size(width, height)` to set the **plot size** to the desired `width` and `height`, in units of character dimensions,
 - in a matrix of subplot, the final widths / heights will be the same for each column / row and, by default, their *maximum* is taken. If `take_min()` is called, the minimum is considered instead.

Here are some related useful functions:
- `terminal_size()` - in short `ts()` - returns the width and height of the terminal,
- `terminal_width()` - in short `tw()` - returns the width of the terminal,
- `terminal_height()` - in short `th()` - returns the height of the terminal.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-aspect)


## Plot Limits
The plot limits are set automatically; to set them manually you can use the following functions:

 - `xlim()` to set the `left` and `right` limits of the `x` axis; use the `xside` parameter, to address a specific `x` axis: `lower` or `upper` - 1 or 2 in short,
 - `ylim()` to set the `lower` and `upper` limits of the `y` axis; use the `yside` parameter, to address a specific `y` axis: `left` or `right` - 1 or 2 in short.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md)


## Axes Ticks
To change the numerical ticks on the `x` axis, you could use one of the following functions:

- `xfrequency()` to set the numerical tick frequency of the `x` axis to an integer value: the ticks will be automatically calculated,
- `xticks()` to manually sets the ticks to the list of `ticks` provided; if two lists are provided, the second is intended as the list of string `labels` to be placed at the coordinates provided by the first,
- in both cases, the parameter `xside` is used to address a specific `x` axis, `lower` or `upper` - 1 or 2 in short,
- naturally, the functions used to specify the ticks relative to the `y` axis, are `yfrequency()`, `yticks()` and behave similarly.

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
![ticks](https://raw.githubusercontent.com/piccolomo/plotext/master/data/ticks.png)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md)