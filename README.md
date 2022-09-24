The package **`plotext`** allows to plot data directly on terminal. 


# Basic Example
You can use `plotext` to plot directly on terminal, as you would normally with `matplotlib`. Here is a basic example on how to use it:
```
import plotext.plot as plx
plx.scatter(x, y)
plx.show()
```
where `x` and `y` are the lists for the of points coordinates; optionally, a single `y` list could be provided. Alternatively, you could plot data points with lines connecting them using the `plot` function instead of the `scatter` one. Multiple data set could also be plotted using consecutive `scatter` or `plot` functions.  Here is an output example:

![example](https://github.com/piccolomo/plotext/raw/master/images/example.png)


Each data point is represented by a character (in this case a `•`).

## Installation
To install the latest version of the `plotext` package use the following command:
```
sudo -H pip install plotext
```

# Parameters
You can personalize the plots in different ways using the `scatter` and `plot` function parameters. Here they are:

- **cols**
It sets the number of columns of the plot. Only integers are allowed. By default, it is set to the highest value allowed by the the terminal size. Alternatively you could set the number of rows using `set_cols(cols)` after the scatter function.

- **rows**
It sets the number of rows of the plot. Only integers are allowed. By default, it is set to the highest value allowed by the the terminal size. Alternatively you could set the number of columns using `set_rows(rows)` after the `scatter` or `plot` function.

- **force_size**
The plot dimensions are limited by the terminal size, when `force_size `is False and are allowed to be bigger otherwise. The default value is `False`. Alternatively you could set `force_size` using `set_force_size(force_size)` after the `scatter` or `plot` function but before `set_cols(cols)` and `set_rows(rows)`.

- **xlim**
It sets the minimum and maximum limits of the plot in the `x` axis. It requires a list of two numbers, where the first sets the left (minimum) limit and the second the right (maximum) limit. If one or both values are not provided, they are calculated automatically. Alternatively you could use `set_xlim(xlim)` after the `scatter` or `plot` function.

- **ylim**
It sets the minimum and maximum limits of the plot in the `y` axis. It requires a list of two numbers, where the first sets the lower (minimum) limit and the second the upper (maximum) limit. If one or both values are not provided, they are calculated automatically. Alternatively you could use `set_ylim(ylim)` after the `scatter` or `plot` function.

- **point**
When `True`, the plot shows the scatter data points. The default value is `True`.

- **point_marker**
It sets the marker used to identify each data point on the plot. Only single characters are allowed (eg: `'*'`). The default value is `'•'`.

- **point_color**
It sets the color used for the point marker. Use `get_colors()` to find the available color codes. The default value is `'norm'`.

- **line**
When True, the plot shows the lines between each data points. The default value is `False`.

- **line_marker**
It sets the marker used to identify the lines between data points. Only single characters are allowed (eg: `'*')`. The default value is `'•'`.

- **line_color**
It sets the color used for the line marker. Use `get_colors()` to find the available color codes. The default value is `'norm'`.

- **background**
It sets the plot background color. Use `get_colors()` to find the available color codes. The default value is `'norm'`. Alternatively you could set the background color using `set_background(background)` after the `scatter` or `plot` function.

- **axes**
When True, the `x` and `y` axes are added to the plot. A list of two Boolean will set the `x` and `y` axes separately (eg: `axes = [True, False]`). The default value is `True`.

- **axes_color**
It sets the color of the axes, ticks and equations, when present. Use `get_colors()` to find the available color codes. The default value is `'norm'`. Alternatively you could set the axes color using `set_axes_color(axes_color)` after the scatter function.

- **ticks**
When `True`, the `x` and `y` ticks are added to the respective axes (even when absent). A list of two Boolean will set the `x` and `y` ticks separately (eg: `ticks = [True, False]`). The default value is `True`.

- **spacing**
It sets the spacing between the `x` and `y` ticks. When a list of two numbers is given, the spacing of the `x` and `y` ticks are set separately (eg: `spacing = [5, 8]`). Only positive integers are allowed. The default value is `[10, 5]`. Alternatively you could use `set_spacing(spacing)` after the `scatter` or `plot` function.

- **equations**
When `True`, the equations - needed to to find the real `x` and `y` values from the plot coordinates - are added at the end of the plot. The default value is `False`.

- **decimals**
It sets the number of decimal points shown in the equations. Only positive integers are allowed. The default value is `2`. Alternatively you could set the decimal points using `set_decimals(decimals)` after the `scatter` or `plot` function.


## Save Plot
You can save your plot, as a text file, using `plx.savefig(path)` where `path` is the file address where the data will be written. Note that (for now), this function doesn't preserve the plot colors. 


## Streaming Data
The following functions are useful for example when continuously plotting a stream of data.

In order to clear the plot canvas use:
```
plx.clear_plot()
```
and to clear the terminal use:
```
plx.clear_terminal()
```
A common problem when plotting streaming data is the screen flickering. In order to remove or reduce this problem use:
```
plx.sleep(time)
```
which adds a sleeping time to the computation. An input of, for example, `0.01` would add approximately `0.01` secs to the computation. The `time` parameters will depend on your processor speed and it needs some manual tweaking. 
Here is an example of plotting a continuous stream of data:

![stream](https://github.com/piccolomo/plotext/raw/master/images/animation.gif)


## Equations
As previously written, you could add two equations at the end of the plot to transform the column and row coordinatesdisplayeddisplayed into real `x` and `y` coordinates. Here is an example of a plot with equations at the end:

![example_old](https://github.com/piccolomo/plotext/raw/master/images/example_old.png)

The errors in the equations are due to the fact that the pixel size reduces the resolution of the data displayed.

Alternatively you could access the functions `plx.get_x_from_col(col)` and `plx.get_y_from_row(row)` to make python do the transformation from your chosen column and row  to real, respectively, `x` and `y` coordinates.


## Colors
You can access the function `plx.get_colors()` in order to find the available full ground and background color codes. Here is the output for simplicity:

![colors](https://github.com/piccolomo/plotext/raw/master/images/colors.png)


## Test
You can run a simple initial test of your newly installed package, to check that `plotext` works well in your machine. Just use `plx.run_test()`


## Version
In order to check the installed version of the package use the command `plx.get_version()`


## Other Documentation

The full documentation of any of the functions shown above could be accessed using commands like these:
```
print(plx.scatter.__doc__)
print(plx.plot.__doc__)
print(plx.show.__doc__)
```


### Main Updates:
- `plotext` now works also in **Windows** comand line (CMD) with colors
- `plotext` now works also using Python IDLE3 but with no colors and no adaptive dimensions
- new color codes with **background** codes added
- **`force_size`** option added
- **`savefig`** function added
- **`get_version`** function added
- **`run_test`** function added
- no need for `numpy` or `time` packages
- the code has been updated and it is more legible
- the documentation has been updated
- `equations` options now is set by default to `False`
- When `thick` is `False`, the axes non numerical thicks are also removed
- Removed get functions for plot parameters


### Creator
- Author: Savino Piccolomo
- e-mail: piccolomo@gmail.com


### Contributors
- Dominik Wetzel, Schmetzler for the Windows support
- Dominik Wetzel for force_size idea
- Kexul, Madrian for their inputs regarding plotting multiple lines
