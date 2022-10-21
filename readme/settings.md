# Plot Settings

- [Plot Size](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-size)
- [Plot Limits](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-limits)
- [Axes Ticks](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#axes-ticks)

[Main Guide](https://github.com/piccolomo/plotext#guide)

## Plot Size

By default the plot size adapts to the dimensions of the terminal. To change this behavior, use the following functions:

- `plot_size(width, height)` to set the **plot size** to the desired `width` and `height`, in units of character dimensions.

- `limit_size()` to set, whatever or not, to **limit the plot size to the terminal dimensions**. It requires to Boolean (one for each dimension) and it is only available for the main figure and not for its subplots, if present, and should be used before `plot_size()`.

- In a matrix of subplot, the final widths / heights will be the same for each column / row and, by default, their *maximum* is taken. If `take_min()` is called, the minimum is considered instead. This method is available to all subplots levels. 

Here are some other useful functions:

- `terminal_size()`, in short `ts()`, returns the width and height of the terminal.

- `terminal_width()`, in short `tw()`, returns the width of the terminal.

- `terminal_height()`, in short `th()`, returns the height of the terminal.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-aspect)

## Plot Limits

The plot limits, on each axes, are set automatically; to set them manually you can use the following functions:

- `xlim()` to set the `left` and `right` limits on the x axis; use the `xside` parameter, to address a specific x axis, `lower` or `upper`, `1` or `2` in short.

- `ylim()` to set the `lower` and `upper` limits on the y axis; use the `yside` parameter, to address a specific y axis, `left` or `right`, `1` or `2` in short.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md)

## Axes Ticks

To change the numerical ticks on the x axis, you could use one of the following functions:

- `xfrequency()` to set the numerical ticks frequency on the x axis: the actual ticks will be evaluated automatically.

- `xticks()` to manually sets to x `ticks` provided; if two lists are provided, the second is intended as the list of string `labels` to be placed at the coordinates provided by the first.

- To change the direction of the x axes use the `xreverse()` function. 

- In all cases, the parameter `xside` is used to address a specific x axis, `lower` or `upper`, `1`or`2` in short.

- Naturally, the functions used to specify the ticks on the y axis, are `yfrequency()`, `yticks()` and `yreverse()` and they behave similarly. In all cases, to address a specific y axis, set the parameter `yside` to `left` or `right`, `1` or `2` in short.

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
More documentation is available in the correspondent docstrings. 

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md)