The package **`plotext`** allows to plot data directly on terminal. 


# Basic Example
You can use `plotext` to plot data as you would with `matplotlib`. Here is a basic example of a scatter plot:
```
import plotext as plt
plt.scatter(x, y)
plt.show()
```
where `x` and `y` are the coordinates of the points to be plotted; optionally, a single `y` list could be provided. 

Alternatively, you could plot the lines between each point using the `plot` function instead. 

Multiple data set could be plotted using consecutive `scatter` or `plot` functions.  Here is a plot example:

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/example.png)

Each data point is represented by a character (in this case `•`).


# Parameters
You can personalize the plots in many ways using the following parameters (of both the `plot` and `scatter` functions):

- **xlim**
It sets the minimum and maximum limits of the plot in the x axis. It requires a list of two numbers, where the first sets the left (minimum) limit and the second the right (maximum) limit. If one or both values are not provided, they are calculated automatically. Alternatively use `set_xlim(xlim)` after the scatter function. 

- **ylim**
It sets the minimum and maximum limits of the plot in the y axis. It requires a list of two numbers, where the first sets the lower (minimum) limit and the second the upper (maximum) limit. If one or both values are not provided, they are calculated automatically. Alternatively use `set_ylim(ylim)` after the scatter function. 

- **cols**
It sets the number of columns of the plot. By default, it is the highest value allowed by the terminal size. Alternatively use `set_cols(cols)` or `set_canvas_size(cols, rows)` after the scatter function.

- **rows**
It sets the number of rows of the plot. By default, it is the highest value allowed by the terminal size. Alternatively use `set_rows(rows)` or `set_canvas_size(cols, rows)` after the scatter function.

- **force_size**
By default, the plot dimensions are limited by the terminal size. Set force_size to True in order to allow bigger plots. Alternatively use `set_force_size(True)` after the scatter function (but before the functions `set_cols` and `set_rows`, if present).
Note: plots bigger then the terminal size may not be readable. 

- **point_marker**
It sets the marker used to identify each data point plotted. It should be a single character and it could be a different value for each data set. If an empty string is provided, no data point is plotted. The default value is '•'. This parameter can only be set internally, because it is associated to the current data set plotted. 

- **line_marker**
It sets the marker used to identify the lines between two consecutive data points. It should be a single character and it could be a different value for each data set. If an empty string is provided (as by default), no lines are plotted. This parameter can only be set internally, because it is associated to the current data set plotted.

- **canvas_color**
It sets the canvas background color, without affecting the axes color. Alternatively use `set_canvas_color(color)` after the scatter function. Use `get_colors()` to find the available color codes. The default value is 'norm'.

- **point_color**
It sets the color of the data points. Use `get_colors()` to find the available color codes. The default value is 'norm'. This parameter can only be set internally, because it is associated to the current data set plotted.

- **line_color**
It sets the color of the lines, if plotted. Use `get_colors()` to find the available color codes. The default value is 'norm'. This parameter can only be set internally, because it is associated to the current data set plotted.

- **axes**
When set to True (as by default), the x and y axes are added to the plot. A list of two Booleans will set the x and y axis independently (eg: `axes = [True, False]`). Alternatively, use `set_axes(axes)` after the scatter function.  

- **axes_color**
It sets the axes color, without affecting the canvas. The same color is applied to the axes ticks, labels, equations, legend and title, if present. Use `get_colors()` to find the available color codes. The default value is 'norm'. If a list of two colors is provided, the second is interpreted as a background color. Alternatively use `set_axes_color(color)` after the scatter function. 

- **ticks_number**
It sets the number of data ticks printed on each axis. If a list of two values is provided, the number of ticks for each axis is set independently (eg: `ticks_number = [5, 6]`). If set to 0, no ticks are printed. The default value is 5. Alternatively use `set_ticks_number(num)` after the scatter function.
Note: you could also directly provide all ticks coordinates and labels for each axis using the functions `set_xticks` and `set_yticks`. Access their docstrings for further guidance. In this case the value of `ticks_number` would not affect what is printed. 

- **ticks_length**
It sets the maximum allowed number of characters of all data ticks on each axes. If the number of characters of any of the ticks coordinates is longer then this value, the ticks are re-scaled and an equation would appear at the end of the plot to clarify the conversion. If a list of two values is provided, the ticks length are set independently (eg: `ticks_length = [5, 6]`). If set to 0, no ticks are printed. The default value is 4. Alternatively use `set_ticks_length(num)` after the scatter function. 
Note: you could also directly provide all ticks coordinates and labels for each exes using the functions `set_xticks` and `set_yticks`. Access their docstrings for further guidance. In this case the value of `ticks_length` needs to be higher that the maximum number of characters of the chosen ticks, otherwise some of the characters could be cut out of the plot. 

- **title**
It sets the title of the plot. Alternatively use `set_title(label)` after the scatter function. 

- **xlabel**
It sets the label of the x axis. Alternatively use `set_xlabel(label)` after the scatter function. 

- **ylabel**
It sets the label of the y axis. Alternatively use `set_ylabel(label)` after the scatter function. 

- **label**
It sets the label of the current data set, which will appear in the legend at the end of the plot. The default value is an empty string. If all labels are an empty string no legend is printed. Alternatively use `set_legend(labels)` to set all labels (as a list of strings) after the scatter function.


## Usefull Functions
- **set_xticks** and **set_yticks**
respectivelly set the ticks on the x and y axis. The ticks should be provided as a list of values. If two lists are provided, the second is intended as the list of labels to be printed at the coordinates given by the first list. Here is an example:
```
plt.scatter(data)
plt.set_xticks(xticks, xlabels)
plt.set_yticks(yticks, ylabels)
plt.show()
```
If no list is provided, the ticks will be calculated automatically. If the ticks are not calculated automatically, any value given to the `ticks_number` parameter of the scatter or plot function will not affect the ticks plotted. On the contrary, the value of the `ticks_length` parameter needs to be higher that the maximum number of characters of the chosen ticks (or labels if present), otherwise some or all of the characters could be cut out of the plot. 
- **set_legend**
sets the labels of each plot (as a list of strings) to be printed as a legend. If all labels are an empty string, no legend will be printed. Here is an example:
```
plt.scatter(y1)
plt.plot(y2)
plt.set_legend(["signal 1", "signal2"])
plt.show()
```
Alternatively the labels can be provided directly inside the scatter or plot function. Here is an example:
```
plt.scatter(y1, label = "signal 1")
plt.plot(y2, label = "signal 2")
plt.show()
```
- **clear_terminal**
It clears the terminal screen and it useful to make the plot cleared as it would be printed at the beginning of a clean terminal. Here is an example:
```
plt.clear_terminal()
plt.scatter(x, y)
plt.show()
```
- **clear_plot**
is similar to `cla` and `clf` in `matplotlib`, as it resets all the plot parameters to their default value, including the data coordinates. Here is an example:
```
plt.scatter(y1, cols = 10)
plt.show()

plt.clear_plot()
plt.plot(y2, rows = 20, title = "new plot")
plt.show()
```
which would print two independent plots. Without `clear_plot`, the previous code would result in a single plot including both data sets (y1 and y2).

- **save_fig**
saves your plot as a text file. Here is an example:
```
plt.scatter(y)
plt.show()
plt.save_fig(path)
```
where `path` is the file address where the data will be written. Note that (for now), this function doesn't preserve the plot colors. 

- **sleep**
A common problem when plotting streaming data is the screen flickering. In order to remove or reduce this problem use:
```
plt.sleep(time)
```
which adds a sleeping time to the computation. An input of, for example, `0.01` would add approximately `0.01` secs to the computation. The `time` parameters will depend on your processor speed and it needs some manual tweaking. 

Here is an example of plotting a continuous stream of data:

![stream](https://raw.githubusercontent.com/piccolomo/plotext/master/images/animation.gif)

Plotting the same data using `matplotlib` was roughly 15 to 50 times slower on a linux machine.


## Colors
You can access the function `plx.get_colors()` in order to find the available full ground and background color codes. Here is the output for simplicity:
![colors](https://raw.githubusercontent.com/piccolomo/plotext/master/images/colors.png)


## Installation
In Windows, to install the latest version of the `plotext` package use this command :
```
pip install plotext --upgrade
```
while in Linux:
```
sudo -H pip install plotext --upgrade
```
In order to check the version of the installed package use: 
```
import plotext as plt
plt.get_version()
```


## Other Documentation
Other relevant documentation could be accessed using commands like these:
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


### Main Updates:
- the plot now shows the actual data ticks, which was more complicated then expected as the ticks should adapt to a limited amount of characters available (`ticks_length`). This is a new features and it may require some adjustments. Please communicate any issues regarding data ticks.
- `set_xticks` and `set_yticks` functions added to set the ticks values, directly.
- labels can be added to the axes.
- a title can be added to the plot.
- a legend can be shown when plotting multiple data sets.
- set functions involving a list of two parameters can be used in two different ways. For example `set_xlim([xmin, xmax])` is equivalent to `set_xlim(xmin, xmax)`.
- `point` and `line` parameters removed. To remove the data points (or lines), it is sufficient to set the point marker (or line marker) to an empty string.
- `background` parameter removed and `canvas_color` takes his place, but can set only the canvas background color.
- `axes_color` could now also be a list of two colors where the second sets the axes background color.
- `spacing` parameter removed, `ticks_number` takes his place.
- `equations `parameter removed as the equations will be printed automatically if needed.
- `decimals` parameter removed.
- code restructured and revised. 


### Future Plans:
Any help on the following or new ideas is more then welcomed.

- creation of an *histogram plot*.
- data ticks for time based data.
- color and terminal size support for IDLE python editor and compiler.
- same as previous point but for Spider. 
- add new colors using ansi codes.
- saving text files with color.
- adding an optional grid (not sure how).


### Contributors
- Dominik Wetzel, Schmetzler for the Windows support.
- Dominik Wetzel for force_size idea.
- Kexul, Madrian for their inputs regarding plotting multiple lines.