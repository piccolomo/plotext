from plotext._utility.color import colorize as colorizing

__doc__ = "It contains the doc-strings of all the main plotext functions."

_figure = """It contains all internal parameters of the plot figure including its subplots. It is meant to be used only for maintenance and testing and not in normal conditions."""
figure = lambda: print(_figure)

##############################################
##########    Subplot Functions    ###########
##############################################

_subplots = """It creates a matrix of subplots. It requires two integers: the first sets the number of rows and the second the number of columns of the matrix of subplots. If only one integer is provided, the other is set to 1. 
Note that the dimensions of the plot is rearranged such that the plot widths of each column is the same; likewise the heights of each row is the same."""
subplots = lambda: print(_subplots)

_subplot = """It sets the active subplot such that further commands will refer to it. It requires two integers, where the first sets the row (from above) and the second the column (from left) of the chosen subplot in the matrix of subplots. 
Both values start from 1 and have to be lower or equal to the correspondent subplots matrix dimension set using subplots().
If only one integer is provided, the other is set to 1."""
subplot = lambda: print(_subplot)

##############################################
###########    Clear Functions    ############
##############################################

_clear_figure = """It clears all internal definitions of the final figure, including its subplots.
The functions clf() and clear_figure() are equivalent."""
clear_figure = clf = lambda: print(_clear_figure)

_colorless = """It remove all colors from the entire figure, including its subplots.
The functions cls() and colorless() are equivalent."""
colorless = cls = lambda: print(_colorless)

_clear_plot = """It clears all the internal definitions relative only to the active subplot. 
The functions clp() and clear_plot() are equivalent."""
clear_plot = clp = lambda: print(_clear_plot)

_clear_data = """It clears only the data information relative to the active subplot, without clearing all the other plot settings.
The functions cld() and clear_data() are equivalent."""
clear_data = cld = lambda: print(_clear_data)

_clear_color = """It clears only the color settings relative to the active subplot, without clearing all other plot settings. The final rendering of this subplot will be colorless.
The functions clc() and clear_color() are equivalent."""
clear_color = clc = lambda: print(_clear_color)

_clear_terminal = """It clears the terminal screen and it is generally useful before plotting a continuous stream of data. It is recommended to use it before show().
If the parameter 'lines' is set to an integer (it is 'None' by default), only the specified lines will be cleared. In this case, it is recommended to use it after show(). Note that, the shell used may print extra lines, which need to be added to 'lines' in order for the clearing to have an effect. 
The functions clt() and clear_terminal() are equivalent."""
clear_terminal = clt = lambda: print(_clear_terminal)

##############################################
###########    Set Functions    ##############
##############################################

_plot_size = """It sets the plot size of the active subplot (in units of character size). It requires two integers for the desired width and height of the plot. 
If the plot is part of a matrix of subplots, the final plot dimensions may be different from the one chosen and are changed in order for the plot widths of each column and heights of each row to be the same.
Note that the functions plotsize() and plot_size() are equivalent."""
plot_size = lambda: print(_plot_size)

_limit_size = """If is used to limit the figure size to the terminal dimensions. It needs two Booleans, one for each dimension. 
By default the plot is limited by the terminal size in both directions. 
Note that limit_size(True) is equivalent to limit_size(True True). 
The functions 'limitsize' and 'limit_size' are equivalent."""
limit_size = lambda: print(_limit_size)

_span = """When a matrix of subplots is build, this function could be used to specify whatever the dimensions of a particular subplot should span as specified by the parameters 'colspan' and 'rowspan' (by default both 1)."""
span = lambda: print(_span)

_title = """It set the title of the active subplot."""
title = lambda: print(_title)

_xlabel = """It sets the label of the x axis, relative to the active subplot. The parameter 'xside' allows to the independently set either the 'lower' (by default) or 'upper' x axis label."""
xlabel = lambda: print(_xlabel)

_ylabel = """It sets the label of the y axis, relative to the active subplot. The parameter 'yside' allows to the independently set either the 'left' (by default) or 'right' y axis label."""
ylabel = lambda: print(_ylabel)

_xaxis = """It sets whatever or not to show the x axis and it requires a Boolean input. The parameter 'xside' allows to the independently set either the 'lower' (by default) or 'upper' x axis.""" 
xaxis = lambda: print(_xaxis)

_yaxis = """It sets whatever or not to show the y axis and it requires a Boolean input. The parameter 'yside' allows to the independently set either the 'left' (by default) or 'right' y axis."""
yaxis = lambda: print(_yaxis)

_frame = """It sets whatever or not to include all subplot axes (which constitute the plot frame) and it requires a Boolean. 
Note that this function can interfere with xaxis() and yaxis(). """
frame = lambda : print(_frame)

_grid = """It sets whatever or not to show the horizontal and vertical grid lines on the active subplot. It requires two Boolean parameters, one for each direction. 
Note that grid(True) is equivalent to grid(True, True). """
grid = lambda: print(_grid)

_canvas_color = """It sets the background color of the plot canvas, which is the area where data points are plotted. 
Access the function plt.colors() for the available color codes."""
canvas_color = lambda: print(_canvas_color)

_ticks_color = """It sets the color relative to any writing in the plot (title, legend, axes labels, axes and numerical ticks). 
Access the function plt.colors() for the available color codes."""
ticks_color = lambda: print(_ticks_color)

_axes_color = """It sets the color of the axes background, including numerical ticks, title and axes labels (but not the plot legend). 
Access the function plt.colors() for the available color codes."""
axes_color = lambda: print(_axes_color)

_xlim = """It sets the minimum and maximum values that could be plotted on the x axis. It requires a list of two numbers, where the first sets the left (minimum) limit and the second the right (maximum) limit.
The parameter 'xside' allows to the independently set either the 'lower' (by default) or 'upper' x axis limits."""
xlim = lambda: print(_xlim)

_ylim = """It sets the minimum and maximum values that could be plotted on the y axis. It requires a list of two numbers, where the first sets the lower (minimum) limit and the second the upper (maximum) limit.
The parameter 'yside' allows to the independently set either the 'left' (by default) or 'right' y axis limits."""
ylim = lambda: print(_ylim)

_xscale = """It sets the scale with which to plot data relative to the x axis: it could be either 'linear' (as by default) or 'log' (for logarithmic plots).
The parameter 'xside' allows to the independently set either the 'lower' (by default) or 'upper' x axis scale."""
xscale = lambda: print(_xscale)

_yscale = """It sets the scale with which to plot data relative to the y axis: it could be either 'linear' (as by default) or 'log' (for logarithmic plots).
The parameter 'yside' allows to the independently set either the 'left' (by default) or 'right' y axis scale."""
yscale = lambda: print(_yscale)

_xfrequency = """It sets the number of numerical ticks to show on the x axis and it requires one positive integer. 
The parameter 'xside' allows to the independently set either the 'lower' (by default) or 'upper' x axis ticks frequency.  
Note that the function xticks() and xfrequency() can interfere."""
xfrequency = lambda: print(_xfrequency)

_yfrequency = """It sets the number of numerical ticks to show on the y axis and it requires one positive integer. 
The parameter 'yside' allows to the independently set either the 'left' (by default) or 'right' y axis ticks frequency.
Note that the function yticks() and yfrequency() can interfere."""
yfrequency = lambda: print(_yfrequency)

_xticks = """It sets the data ticks on the x axis. The ticks should be provided as a list of values. If two lists are provided, the second is intended as the list of labels to be printed at the coordinates given by the first list. If empty list are provided, no ticks are printed. If 'None' is provided (as by default), the ticks are calculated automatically.
The parameter 'xside' allows to the independently set either the 'lower' (by default) or 'upper' x axis ticks and labels.
Note that the function xticks() and xfrequency() can interfere."""
xticks = lambda: print(_xticks)

_yticks = """It sets the data ticks on the y axis. The ticks should be provided as a list of values. If two lists are provided, the second is intended as the list of labels to be printed at the coordinates given by the first list. If empty list are provided, no ticks are printed. If 'None' is provided (as by default), the ticks are calculated automatically.
The parameter 'yside' allows to the independently set either the 'left' (by default) or 'right' y axis ticks and labels.
Note that the function yticks() and yfrequency() can interfere."""
yticks = lambda: print(_yticks)

##############################################
#########    Plotting Functions    ###########
##############################################

_scatter = """It creates a scatter plot of data coordinates given by the x and y lists. Optionally, a single y list could be provided. Here is a basic example:

  \x1b[96mimport plotext as plt
  plt.scatter(x, y)
  plt.show()\x1b[0m

Multiple data sets could also be plotted using consecutive scatter functions:

  \x1b[96mplt.scatter(x1, y1)
  plt.scatter(y2)
  plt.show()\x1b[0m

Here are all the parameters of the scatter function:
 
\x1b[96mmarker\x1b[0m sets the marker used to identify each data point for the current data set. A single character could be provided or the available marker codes, which could be accessed using the function markers(). If 'None' is provided (as by default), the marker is set automatically. A list of strings could also be provided, to give to each data point its own marker. 

\x1b[96mcolor\x1b[0m sets the color of the data points. Access the function plt.colors() for the available full-ground color codes. If 'None' is provided (as by default) the color is set automatically. A list of colors could also be provided, to give to each data point its own color.

\x1b[96mlabel\x1b[0m sets the label of the current data set, which will appear in the legend menu at the top left of the plot. If 'None' is provided (as by default), the label will not be printed in the legend. 

\x1b[96mfillx\x1b[0m sets whatever to fill the canvas of markers from each data point to the xaxis. The default value is False.

\x1b[96mfilly\x1b[0m sets whatever to fill the canvas of markers from each data point to the yaxis. The default value is False.

\x1b[96mxside\x1b[0m sets whatever to plot the data relative to the 'lower' or 'upper' x axis.

\x1b[96myside\x1b[0m sets whatever to plot the data relative to the 'left' or 'right' y axis.""" 
scatter = lambda: print(_scatter)

_plot = """It is identical to the scatter function, except that lines between two consecutive data points are plotted.
Access the scatter function doc-string for further documentation on its internal parameters."""
plot = lambda: print(_plot)

_build = """It created and returns the final figure canvas in string form, without actually printing it."""
build = lambda: print(_build)

_show = """It builds and prints the final figure on terminal."""
show = lambda: print(_show)

##############################################
########     DateTime Functions    ###########
##############################################

_datetime = """It contains tools to easily manipulate datetime objects."""
datetime = lambda: print(_datetime)

_datetime_functions = ["today", "set_time0", "set_datetime_form", "clear", "string_to_datetime", "datetime_to_timestamp", "string_to_timestamp", "datetime_to_string"]

_today = """It stores today's date in string, tuple, or datetime form."""

_set_time0 = """It sets the origin of time to the 'year', 'month', 'day', 'hour', 'minute' and 'second' provided as integer. The default value is 01/01/1900. 
This function is useful when using log scale with date plots in order to avoid "hitting" the 0 timestamp.
Note that 'hour', 'minute' and 'second' are set to 0, if not provided."""
set_time0 = lambda: print(_set_time0)

_set_datetime_form = """It sets how to interpret string based datetime objects and accepts two parameters: 'date_form' for date forms (by default '%d/%m/%Y') and 'time_form' for time forms (by default '%H:%M:%S')."""
set_datetime_form = lambda: print(_set_datetime_form)

_clear = """It restores the internal definitions of the datetime class."""
clear = lambda: print(_clear)

_string_to_datetime = """It turns a string based datetime object into a datetime object of the datetime package according to the datetime forms set using the function set_datetime_form()."""
string_to_datetime = lambda: print(_string_to_datetime)

_datetime_to_timestamp = """It turns a datetime object of the datetime package to a timestamp. The values is relative to the origin of time, which could be fixed using the function set_time0()."""
datetime_to_timestamp = lambda: print(_datetime_to_timestamp)

_string_to_timestamp = """It turns a string based datetime object into a timestamp. The conversion is done according to the datetime form which can be changed using the function set_datetime_form(). 
The final value is relative to the origin of time, which could be fixed using the function set_time0(). """
string_to_timestamp = lambda: print(_string_to_timestamp)

_datetime_to_string = """It turns a datetime object of the datetime package to a string according to the datetime forms set using the function set_datetime_form()."""
datetime_to_string = lambda: print(_datetime_to_string)

_scatter_date = """It creates a scatter plot of coordinates given by the x and y lists, where x is a list of strings, each representing a date and/or time. 
It has the same internal parameters as the scatter() function."""
scatter_date = lambda: print(_scatter_date)

_plot_date = """It creates a plot (with lines connecting each pair of data points) of coordinates given by the x and y lists, where x is a list of strings, each representing a date and/or time. 
It has the same internal parameters as the plot() function."""
plot_date = lambda: print(_plot_date)

##############################################
###########     Bar Functions    #############
##############################################

_bar = """It creates a bar plot using the x and y values provided. The x values could be a list of numbers or of strings, or optionally not provided. 
It accepts the same parameters as the scatter() and plot() functions (except for 'fillx' and 'filly', which are substituted by 'fill'). 

Here are its extra parameters:

\x1b[96mfill\x1b[0m if set to 'True' (as by default), the plot bars are filled with the given colored markers. If 'False' only the bars borders are plotted.

\x1b[96mwidth\x1b[0m is the relative width of the bars and could be a float ranging from 0 to 1. The default value is 4 / 5.

\x1b[96morientation\x1b[0m sets the orientation of the bar plot and could be either 'vertical' (in short 'v', as by default) or 'horizontal' (in short 'h').

\x1b[96mminimum\x1b[0m sets the minimum value of all the bars. By default a non-zero convinient value is calculated. This value could be easily tweaked, particularly where log scale is chosen along the bars height."""
bar = lambda: print(_bar)

_multiple_bar = """It allows to plot multiple bars with the same labels or coordinates. It requires the bars x coordinates or labels and the matrix of bar heights. Each row of the matrix will add a bar plot at the given x coordinates, with a slight offset. 
It accepts the same parameters as the bar() function."""
multiple_bar = lambda: print(_multiple_bar)
 
_stacked_bar = """It allows to plot multiple bars with the same labels or coordinates, stacked on top of each other along the bar height. It requires the bars x coordinates or labels and the matrix of bar heights. Each row of the matrix will add a bar plot at the given x coordinates on top of the previous. 
It accepts the same parameters as the bar() function."""
stacked_bar = lambda: print(_stacked_bar)

_hist = """It builds the histogram plot relative to the data provided. It accepts the same parameters as the bar plot (except for 'minimum' which is not available here) with the following extra parameters:

\x1b[96mbins\x1b[0m used to calculate the histogram transform of the data (10 by default).
\x1b[96mnorm\x1b[0m if True, the bin heights are normalised so that the plot would simulate a probability distribution."""
hist = lambda: print(_hist)

##############################################
######     Matrix/Image Functions    #########
##############################################

_matrix_plot = """It creates a two dimensional plot of a matrix where the intensity of each element is translated in gray-scale levels (whiter for higher values). If a matrix of rgb colors (eg: (13, 45, 176)) is provided, each pixel will have its actual color instead.
As for the scatter() function, it accepts the parameters 'marker', 'xside', 'yside', but no others. 
Note that using higher resolution markers ('hd' and 'fhd') will not result in an improved spatial resolution as the color resolution is limited by a full character in all cases."""
matrix_plot = lambda: print(_matrix_plot)

_image_plot = """It plots the image located at the given required file path and returns the size of the final plot. 

Here is the list of its optional parameters:

\x1b[96mmarker\x1b[0m sets the marker used to identify each pixel of the plot. The default value is 'sd'.

\x1b[96mgrayscale\x1b[0m if True allows to plot pictures in gray-scale.

\x1b[96msize\x1b[0m fixes the size of the picture and it is highly recommended for big pictures, as the reduction to a smaller size, drastically diminishes the plotting time. If this parameter is used, one still need to use plotsize(size) right after image_plot()

\x1b[96mkeep_ratio\x1b[0m changes the plot size to keep the original image ratio. In this case, it is recommended to use the size image_plot() returns to make sure the aspect ratio is preserved.

\x1b[96mresample\x1b[0m when the image size is adapted to the plot canvas a smoothing algorithm could be optionally applied (as by default)."""
image_plot = lambda: print(_image_plot)

##############################################
#############     Line Plot    ###############
##############################################

_vertical_line = """It plots a vertical line at the given 'coordinate' and specified 'color'. Use the parameter 'xside' to specify which x axis, 'lower' (as by default) or 'upper', the parameter 'coordinate' refers to. It also works with string based datetime coordinates."""
vertical_line = lambda: print(_vertical_line)

_horizontal_line = """It plots a horizontal line at the given 'coordinate' and specified 'color'. Use the parameter 'yside' to specify which y axis, 'left' (as by default) or 'right', the parameter 'coordinate' refers to. It also works with string based datetime coordinates."""
horizontal_line = lambda: print(_horizontal_line)

##############################################
##########     File Functions    #############
##############################################

_file = """It contains tools to easily access and manipulate files and file paths."""
file = lambda: print(_file)

_file_functions = ['parent_folder', 'script_folder', 'join_paths', 'save_text', 'read_data', 'write_data']

_parent_folder = """It returns the parent folder of the given path. The 'level' parameter is used to specify how many levels above the provided path the parent folder should be (1 by default)."""
parent_folder = lambda: print(_parent_folder)

_script_folder = """It returns the folder containing the current script."""
script_folder = lambda: print(_script_folder)

_join_paths = """It accepts as many strings as necessary and returns a properly formatted path. Eg: join_paths("/", "home", "file.txt") = "/home/file.txt".
If the first parameter is "~", it will be interpreted as the user home folder."""
join_paths = lambda: print(_join_paths)

_save_text = """It saves text to the path selected. The first parameter is 'path' and the second the 'text' to be saved."""
save_text = lambda: print(_save_text)

_read_data = """It reads and formats data from the 'path' selected. 

Here are its parameters:

\x1b[96mdelimiter\x1b[0m the delimiter between each data column (by default " ").

\x1b[96mcolumns\x1b[0m the list of columns to be returned (starting from 0). If 'None' (as by default) all columns will be returned.

\x1b[96mheader\x1b[0m if 'True' (as by default) the columns header (i.e. their first element) will be included. Set it to 'False' to exclude those values."""
read_data = lambda: print(_read_data)

_write_data = """It writes a matrix of data to the 'path' selected. 

Here are its parameters:

\x1b[96mdelimiter\x1b[0m the delimiter between each data column (by default " ").

\x1b[96mcolumns\x1b[0m the list of columns to be saved (starting from 0). If 'None' (as by default) all columns will be returned."""
write_data = lambda: print(_write_data)

##############################################
##########     Other Functions    ############
##############################################

_save_fig = """It saves the plot canvas to a file. To be used after the show() function. If the file extension is '.html' the colors will be preserved. For all other file text extensions (like '.txt') no colors will be preserved.
The functions save_fig() and savefig() are equivalent."""
save_fig = lambda: print(_save_fig)

_terminal_size = """It returns the terminal size as [width, height]."""
terminal_size = lambda: print(_terminal_size)

_markers = """It prints the list of available marker codes."""
markers = lambda: print(_markers)

_colors = """It prints the list of available color codes."""
colors = lambda: print(_colors)

_sleep = """It adds a sleeping time to the computation and it is generally useful when continuously plotting a stream of data, in order to decrease a possible screen flickering effect. This function returns the actual time slept.
Manually tweak this value to reduce the possible flickering."""
sleep = lambda: print(_sleep)

_time = """It returns the computational time of the last show() or build() function. Note that in the case of matrix_plot() or image_plot() there is a not negligible computational time outside and before the show() function. """
time = lambda: print(_time)

_sin = """It creates a sinusoidal signal useful, for example, to test the plotext package. Here are its parameters:

\x1b[96mamplitude\x1b[0m: the maximum value of the sinusoidal signal (1 by default).

\x1b[96mperiods\x1b[0m: the number of signal repetitions (2 by default).

\x1b[96mlength\x1b[0m: the number of data points (1000 by default).

\x1b[96mphase\x1b[0m: if 0 (as by default), the sine function is returned; if 0.5, the cosine; if -1, the function -sine; if -0.5, -cosine. Any float number is allowed.  

\x1b[96mdecay\x1b[0m: adds a decay rate (normalized to the number of data points) which will cause the signal to exponentially decay for positive values or increase for negative ones. It is 0 by default. """
sin = lambda: print(_sin)

_colorize = """It "paints" a string with the fullground and/or background colors provided to either or both the parameters 'fullground' and 'background'. 
If the parameter 'show' is set to 'True' the colored string is printed on terminal, otherwise it is returned (as by default).
Access the function plt.colors() for the available color codes."""
colorize = lambda: print(_colorize)

_uncolorize = """It removes any coloring from a string."""
uncolorize = lambda: print(_uncolorize)

_version = """It returns the version of the current installed plotext package."""
version = lambda: print(_version)

_all_docstrings = []
for _key, _value in list(locals().items()):
    if type(_value) == str and _key[:2] != "__":
        _key = _key[1:]
        _key = "file." + _key if _key in _file_functions else _key
        _key = "datetime." + _key if _key in _datetime_functions else _key
        _all_docstrings.append([_key, _value])
        
def all():
    print('\033c', end="")
    print(colorizing("ALL PLOTEXT DOCSTRINGS\n", "bright-cyan bold"))
    for el in _all_docstrings:
        print(colorizing(el[0], "bright-yellow bold"))
        print(el[1])
        if el != _all_docstrings[-1]:
            print("\n")
