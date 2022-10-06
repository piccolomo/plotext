from plotext._utility import colorize as colorizing
from plotext._utility import title_color, positive_color

__doc__ = "It contains the doc-strings of all the main plotext functions."


_subplots = """It creates a matrix of subplots with the given number of 'rows' and 'cols' (columns) and returns the figure containing the subplots created. 
Note that each subplot - accessible with subplot() - could create its own matrix of subplots. Eg: subplots(2, 2); subplot(1, 1); subplots(3, 4) or directly subplots(2, 2).subplot(1, 1).subplots(3, 4) will create a 2 by 2 matrix where the first subplot is a 3 by 4 matrix."""
subplots = lambda: print(_subplots)

_subplot = """It sets and returns the active subplot in the matrix of subplots, such that further commands will refer to it. It requires the 'row' (from above) and 'col' (column from left) of the chosen subplot, starting from 1. 
Note that most of the commands referring to the active subplot, could be alternatively passed directly. Eg: subplot(1, 3); plotsize(100, 30) becomes subplot(1, 3).plotsize(300, 30)."""
subplot = lambda: print(_subplot)

_main = """It returns the main figure at the uppermost level, and sets the active figure to it. Any further commands will apply to the entire figure and to any of its subplots."""
main = lambda: print(_main)

_active = """It returns the active figure."""
active = lambda: print(_active)


_interactive = """It sets whatever to show the final plot soon after any plotting or setting function is called, without using show() each time. Any modification to the plot is displayed immediately in a new canvas."""
interactive = lambda: print(_interactive)

_plot_size = """It sets the plot size - 'width' and 'height' - of the active subplot (in units of character size). 
If the plot is part of a matrix of subplots, its final widths / heights will be the same for each column / row: by default the maximum value is taken: use take_min() to take the minimum instead.
The functions plotsize() and plot_size() are equivalent."""
plot_size = lambda: print(_plot_size)
plotsize = plot_size

_limit_size = """It is used to limit (as by default) or not the main figure size to the terminal dimensions. It needs two Booleans, one for each dimension ('width' and 'height') and should be used before plotsize(), because the later function check if dimensions are limited, before setting them. 
The functions limitsize() and limit_size() are equivalent."""
limit_size = lambda: print(_limit_size)
limitsize = limit_size

_take_min = """In a matrix of subplot, the final widths / heights will be the same for each column / row: by default the maximum value is taken. If take_min() is called, the minimum is considered instead. Note that this setting could made different for different levels of nested matrices."""
take_min = lambda: print(_take_min)



_title = """It set the title of the active subplot."""
title = lambda: print(_title)

_xlabel = """It sets the label of the x axis, relative to the active subplot. 
The parameter 'xside' allows to independently address either the 'lower' (by default) or 'upper' x axis (1 or 2 in short)."""
xlabel = lambda: print(_xlabel)

_ylabel = """It sets the label of the y axis, relative to the active subplot. 
The parameter 'yside' allows to independently address either the 'left' (by default) or 'right' x axis (1 or 2 in short)."""
ylabel = lambda: print(_ylabel)

_xlim = """It sets the minimum and maximum values that could be plotted on the x axis. It accepts dates in string form.
The parameter 'xside' allows to independently address either the 'left' (by default) or 'right' y axis (1 or 2 in short)."""
xlim = lambda: print(_xlim)

_ylim = """It sets the minimum and maximum values that could be plotted on the y axis. It accepts dates in string form.
The parameter 'yside' allows to independently address either the 'lower' (by default) or 'upper' x axis (1 or 2 in short)."""
ylim = lambda: print(_ylim)

_xscale = """It sets the scale of the x axis:  either 'linear' (as by default) or 'log' (for logarithmic plots). 
The parameter 'xside' allows to independently address either the 'left' (by default) or 'right' y axis (1 or 2 in short)."""
xscale = lambda: print(_xscale)

_yscale = """It sets the scale of the x axis:  either 'linear' (as by default) or 'log' (for logarithmic plots). 
The parameter 'yside' allows to independently address either the 'lower' (by default) or 'upper' x axis (1 or 2 in short)."""
yscale = lambda: print(_yscale)

_xticks = """It sets the data ticks on the x axis. If two lists are provided, the second is intended as the list of labels to be printed at the coordinates given by the first list. It accepts dates in string form.
The parameter 'xside' allows to independently address either the 'lower' (by default) or 'upper' x axis (1 or 2 in short)."""
xticks = lambda: print(_xticks)

_yticks = """It sets the data ticks on the y axis. If two lists are provided, the second is intended as the list of labels to be printed at the coordinates given by the first list. It accepts dates in string form.
The parameter 'yside' allows to independently address either the 'left' (by default) or 'right' y axis (1 or 2 in short)."""
yticks = lambda: print(_yticks)

_xfrequency = """It sets the number of numerical ticks to show on the x axis. 
The parameter 'xside' allows to independently address either the 'lower' (by default) or 'upper' x axis (1 or 2 in short)."""
xfrequency = lambda: print(_xfrequency)

_yfrequency = """It sets the number of numerical ticks to show on the y axis. 
The parameter 'yside' allows to independently address either the 'left' (by default) or 'right' y axis (1 or 2 in short)."""
yfrequency = lambda: print(_yfrequency)

_xreverse = """It reverse the x axis if True is passed. The parameter 'xside' allows to independently address either the 'lower' (by default) or 'upper' x axis (1 or 2 in short)."""
xreverse = lambda: print(_xreverse)

_yreverse = """It reverse the y axis if True is passed. The parameter 'yside' allows to independently address either the 'left' (by default) or 'right' y axis (1 or 2 in short)."""
yreverse = lambda: print(_yreverse)

_xaxes = """It sets whatever or not to show the x axes and accepts two Boolean inputs, one for each x axis (lower and upper).""" 
xaxes = lambda: print(_xaxes)

_yaxes = """It sets whatever or not to show the y axes and accepts two Boolean inputs (the second is optional), one for each y axis (left and right).""" 
yaxes = lambda: print(_yaxes)

_frame = """It sets whatever or not to show all subplot axes (which constitute the canvas frame) and it requires a single Boolean. To address any individual axis use the functions xaxes() or yaxes() instead."""
frame = lambda : print(_frame)

_grid = """It sets whatever or not to show the 'horizontal' and 'vertical' grid lines on the active subplot and accepts two Boolean inputs."""
grid = lambda: print(_grid)

_canvas_color = """It sets the background color of the plot canvas: the area where data points are plotted. 
Access the function plt.colors() for the available color codes."""
canvas_color = lambda: print(_canvas_color)

_axes_color = """It sets the background color of the axes area, including its numerical ticks, title and axes labels (not the plot legend). 
Access the function plt.colors() for the available color codes."""
axes_color = lambda: print(_axes_color)

_ticks_color = """It sets the color relative to any writing on the plot: the axes and its numerical ticks, title and axes labels, including the legend labels. 
Access the function plt.colors() for the available color codes."""
ticks_color = lambda: print(_ticks_color)

_ticks_style = """It sets the style relative to any writing on the plot: the axes and its numerical ticks, title and axes labels, including the legend labels. 
Access the function plt.styles() for the available style codes."""
ticks_style = lambda: print(_ticks_style)

_theme = """It sets the color theme for the active plot.
Access the function plt.themes() for the available theme codes."""
theme = lambda: print(_theme)


_clear_figure = """It clears all internal definitions of the addressed figure, including its subplots.
The functions clf() and clear_figure() are equivalent."""
clear_figure = clf = lambda: print(_clear_figure)

_clear_data = """It clears only the data of the addressed figure, including its subplots, without clearing all other plot settings.
The functions cld() and clear_data() are equivalent."""
clear_data = cld = lambda: print(_clear_data)

_clear_color = """It clears only the color settings of the addressed figure, including its subplots, without clearing all other plot settings. The final rendering of this subplot will be colorless.
The functions clc() and clear_color() are equivalent."""
clear_color = clc = lambda: print(_clear_color)

_clear_terminal = """It clears the terminal screen and it is generally useful before plotting a continuous stream of data. It is recommended to use it before show().
If the parameter 'lines' is set to an integer, only the specified terminal lines will be cleared. In this case, it is recommended to use it after show(). 
Note that, the shell used may print extra lines after the plot, which may need to be added to 'lines' in order for the clearing to have an effect. 
The functions clt() and clear_terminal() are equivalent."""
clear_terminal = clt = lambda: print(_clear_terminal)


_scatter = """It creates a scatter plot of data coordinates given by the x and y lists. Optionally, only y could be provided. Either x or y could be a list of string based dates. Multiple data sets could also be plotted using consecutive scatter() functions. Here is a basic example:

 \x1b[96mplt.scatter(x, y1)
 plt.scatter(y2)
 plt.show()\x1b[0m

Here are all of its parameters:

\x1b[96mmarker\x1b[0m sets the marker used to identify each data point on the canvas. A single character could be provided or the available marker codes. A list of markers - one for each data point - could also be provided. Access the function plt.markers() for the available marker codes.

\x1b[96mcolor\x1b[0m sets the color of the data points. A list of colors - one for each data point - could also be provided. Access the function plt.colors() for the available color codes.

\x1b[96mstyle\x1b[0m sets the style of the data points. A list of styles - one for each data point - could also be provided. Access the function plt.styles() for the available style codes.

\x1b[96mlabel\x1b[0m sets the label of the current data set, which will appear in the legend menu at the top left corner of the plot canvas.

\x1b[96mfillx\x1b[0m sets whatever to fill the canvas from each data point, towards the x axis, till level y = 0. The default value is False. If a numerical value is provided, it is intended as the y level where the filling stops. If the code 'internal' is provided, the filling will stop when another data point is reached horizontally (if it exists).

\x1b[96mfilly\x1b[0m sets whatever to fill the canvas from each data point, towards the y axis, till level x = 0. The default value is False. If a numerical value is provided, it is intended as the x level where the filling stops. If the code 'internal' is provided, the filling will stop when another data point is reached vertically (if it exists).

\x1b[96mxside\x1b[0m sets whatever to plot the data on the 'lower' or 'upper' x axis (1 or 2 in short).

\x1b[96myside\x1b[0m sets whatever to plot the data on the 'left' or 'right' x axis (1 or 2 in short).""" 
scatter = lambda: print(_scatter)

_plot = """It creates a plot of lines between consecutive data points. It accept the same parameters as the scatter() function. """
plot = lambda: print(_plot)

_candlestick = """It creates a candlestick plot. Here are its parameters:

\x1b[96mdates\x1b[0m is the list of strings, each representing a date/time object. Use the function date_form() to set accepted date/time form.

\x1b[96mdata\x1b[0m is a dictionary with the following mandatory keys: 'Open', 'Close', 'High', 'Low'. Each value should be a list of prices.

\x1b[96mcolors\x1b[0m is list of two colors, where the first is used for positive and the second for negative candlesticks. Access the function plt.colors() for the available color codes.

\x1b[96mlabel\x1b[0m sets the label of the current data set, which will appear in the legend menu at the top left corner of the plot canvas.

\x1b[96morientation\x1b[0m sets the orientation of the plot and could be either 'vertical' (in short 'v', as by default) or 'horizontal' (in short 'h')."""
candlestick = lambda: print(_candlestick)

_bar = """It creates a bar plot using the x and y values provided. Optionally, only y could be provided. As the scatter() function, it accepts the parameters 'marker', 'color', 'xside', 'yside' and 'label'. Here are its extra parameters:

\x1b[96mfill\x1b[0m sets whatever to fill each bar with the the given colored markers, or just show the its borders.

\x1b[96mwidth\x1b[0m is the relative width of the bars and could be a float ranging from 0 to 1. The default value is 4 / 5.

\x1b[96morientation\x1b[0m sets the orientation of the bar plot and could be either 'vertical' (in short 'v', as by default) or 'horizontal' (in short 'h').

\x1b[96mminimum\x1b[0m sets the minimum value of all the bars (0 by default). This value could be easily tweaked, particularly where 'log' scale is chosen along the bars height."""
bar = lambda: print(_bar)

_simple_bar = """It creates a simpler and sketchier version of an horizontal bar plot. Note that this plot cannot be fit into a matrix of subplots and any setting function will not have any effect. Here are its parameters:

\x1b[96mwidth\x1b[0m sets the horizontal width of the plot.

\x1b[96mmarker\x1b[0m sets the marker used create the bars.

\x1b[96mcolor\x1b[0m sets the color of the bars. Optionally a list of colors (one for each bar) could be provided.

\x1b[96mtitle\x1b[0m sets the title of the plot.

Use show() as usual to display the final result."""
simple_bar = lambda: print(_simple_bar)

_multiple_bar = """It creates a bar plot where multiple bars are grouped together (along the bar width axis) each having the same bar label. It requires the bars x coordinates or labels and the matrix Y, where each of its element is a list of bar heights. 
As the scatter() function, it accepts the parameters 'marker', 'color', 'xside', 'yside' and 'label' and as the bar() function, all of its extra parameters."""
multiple_bar = lambda: print(_multiple_bar)

_simple_multiple_bar = """It creates a simpler and sketchier version of an horizontal multiple bar plot. It requires the bars x coordinates or labels and the matrix Y, where each of its element is a list of bar heights. Note that this plot cannot be fit into a matrix of subplots and any setting function will not have any effect. This function accept the parameters 'width', 'marker', 'title' as in simple_bar(); here are its extra parameters:

\x1b[96mcolors\x1b[0m sets the colors of the bars in each group. It should have the same length as each Y element.

\x1b[96mlabels\x1b[0m sets the labels of each bar plot. It should have the same length as the Y matrix.

Use show() as usual to display the final result."""
simple_multiple_bar = lambda: print(_simple_multiple_bar)

_stacked_bar = """It creates a bar plot where multiple bars are stacked on top of each other (along the bar height axis). It requires the bars x coordinates or labels and the matrix Y, where each of its element is a list of heights. Optionally, only Y could be provided. 
As the scatter() function, it accepts the parameters 'marker', 'color', 'xside', 'yside' and 'label' and as the bar() function, all of its extra parameters."""
stacked_bar = lambda: print(_stacked_bar)

_simple_stacked_bar = """It creates a simpler and sketchier version of an horizontal stacked bar plot. It requires the bars x coordinates or labels and the matrix Y, where each of its element is a list of bar heights. Note that this plot cannot be fit into a matrix of subplots and any setting function will not have any effect. This function accept the parameters 'width', 'marker', 'title' as in simple_bar(); here are its extra parameters:

\x1b[96mcolors\x1b[0m sets the colors of the bars in each group. It should have the same length as each Y element.

\x1b[96mlabels\x1b[0m sets the labels of each bar plot. It should have the same length as the Y matrix.

Use show() as usual to display the final result."""
simple_stacked_bar = lambda: print(_simple_stacked_bar)

_hist = """It builds the histogram plot relative to the 'data' provided. As the scatter() function, it accepts the parameters 'marker', 'color', 'xside', 'yside' and 'label' and as the bar() function, all of its extra parameters. Here are its other parameters:

\x1b[96mbins\x1b[0m sets the number of channels (10 by default) between the minimum and maximum value of the data set, used to count the data frequency.

\x1b[96mnorm\x1b[0m normalises each frequency count, such that the sum of all counts is 1 (instead of the length of the data set)."""
hist = lambda: print(_hist)

_matrix_plot = """It creates a two dimensional plot of a matrix where the intensity of each element is translated in gray-scale level (whiter for higher values). If a matrix of rgb colors is provided, each pixel (eg: (13, 45, 176)) will have its actual rgb color instead.
As the scatter() function, it accepts the parameters 'marker' and 'style', with the following extra parameter:

\x1b[96mfast\x1b[0m if True the final plot is elaborated faster, but its final dimensions are locked to the matrix size, and won't adapt to the terminal or subplot size. It is not recommended when plotting inside a matrix of subplots. 

Note that using higher resolution markers ('hd' and 'fhd') will not result in an improved spatial resolution as the color resolution is limited by a full character in all cases.
A list of markers could be provided and will be repeated on the plot: the style 'inverted' is recommended in this case."""
matrix_plot = lambda: print(_matrix_plot)

_image_plot = """It plots the image located at the given required file 'path'. As the scatter() function, it accepts the parameters 'marker' and 'style', and as the matrix_plot() function the 'fast' parameter (for faster plotting). Here is its extra parameter:

\x1b[96mgrayscale\x1b[0m if True the image will be plotted in gray-scale.

It is recommended to use the function plotsize() before, especially for larger images, to reduce the image size and so the computational load. If 'fast' is True, only the raw image is displayed (with no possible title, labels or frame)."""
image_plot = lambda: print(_image_plot)


_play_gif = """It plays a GIF image on screen. The images will adapt to the screen size unless plot_size() is used before.
Note: this feature may require further development."""
play_gif = lambda: print(_play_gif)

_play_video = """It plays a video, with audio, from the 'path' selected. The frames will adapt to the screen size unless plot_size() is used before. 
Set the parameter 'from_youtube' to True (False by default) to make sure that the color rendering is correct for videos downloaded from youtube.
Note: this feature may require further development."""
play_video = lambda: print(_play_video)

_play_youtube = """It plays a youtube video, with audio, from the given 'url'. 
Note: this feature may require further development."""
play_youtube = lambda: print(_play_youtube)

_get_youtube = """It downloads a youtube video from the given 'url' to the selected 'path'."""
get_youtube = lambda: print(_get_youtube)


_error = """It plots the x and y data provided (x is optional) with the error bars, provided as lists to the 'xerr' and 'yerr' parameters. Optionally either one or both error bars could not be omitted, in which case they are set automatically to 0. 
As the scatter() function, it accepts the parameters 'color', 'xside', 'yside' and 'label'. No 'marker' parameter is accepted, as markers are automatically set to straight lines."""
error = lambda: print(_error)

_event_plot = """It plots parallel lines at the given positions given by 'data', which could be a list of number or date/time strings. As the bar plot it accepts the 'orientation' parameter and as the scatter() function the 'marker' and 'color' parameters. 

The parameter 'side' is used to identify on which axis to plot the events coordinates. It could be 'lower' or 'upper' x axis (1 or 2 in short) for 'vertical' orientation, and 'left' and 'right' y axis (1 or 2 in short) for 'horizontal' orientation.
The functions eventplot() and event_plot() are equivalent."""
event_plot = lambda: print(_event_plot)
eventplot = event_plot

_vertical_line = """It plots a vertical line at the given 'coordinate' and specified 'color'. The coordinate could be a number or a date/time string.
The parameter 'xside' allows to independently address either the 'lower' (by default) or 'upper' x axis (1 or 2 in short).
The functions vline() and vertical_line() are equivalent."""
vertical_line = lambda: print(_vertical_line)
vline = vertical_line

_horizontal_line = """It plots a horizontal line at the given 'coordinate' and specified 'color'. The coordinate could be a number or a date/time string.
The parameter 'yside' allows to independently address either the 'left' (by default) or 'right' y axis (1 or 2 in short).
The functions hline() and horizontal_line() are equivalent."""
horizontal_line = lambda: print(_horizontal_line)
hline = horizontal_line

_text = """It adds a 'text' to the plot at the given 'x' and 'y' coordinates. The coordinates could be a number, a date/time string or a bar label. As the scatter() function it accepts the parameters 'color', 'style', 'xside', 'yside', with the following extra parameter:

\x1b[96mbackground\x1b[0m to set the text background color. Access the function plt.colors() for the available color codes.

\x1b[96morientation\x1b[0m sets the orientation of the text and could be either 'vertical' (in short 'v', as by default) or 'horizontal' (in short 'h').

\x1b[96malignment\x1b[0m sets the text horizontal / vertical alignment to either 'left', 'center', and 'right' or 'top', 'center' and 'bottom' ('left' and 'top' by default). 

Note that the new line character \\n is allowed: multiple sub strings will be printed in sequence with same alignment."""
text = lambda: print(_text)

_rectangle = """It creates a rectangle with coordinates given by x and y, each being a list of length 2. As the scatter() function, it accepts the parameters 'color', 'marker', 'xside', 'yside', and 'label', with the following extra parameters:

\x1b[96mlines\x1b[0m to set whatever to show the rectangle borders or just its vertexes (True by default).

\x1b[96mfill\x1b[0m to set whatever to fill the rectangle with colored markers (False by default)."""
rectangle = lambda: print(_rectangle)

_polygon = """It creates a polygon centered at the given x and y coordinates. As the scatter() function, it accepts the parameters 'color', 'marker', 'xside', 'yside', and 'label', and as the rectangle() function, it accepts the parameters 'lines' and 'fill'. Here are its extra parameters:

\x1b[96msides\x1b[0m to set the number of sides of the polygon (3 by default). To simulate a circle use a high number.

\x1b[96mradius\x1b[0m to set the distance of each vertex of the polygon to the center (1 by default). For a circle, it corresponds to its actual radius, hence the name."""

polygon = lambda: print(_polygon)

_confusion_matrix = """It creates the confusion matrix correspondent to the 'actual' and 'predicted' data. It accepts the parameters 'color' and 'style' to define any writing on the plot. The functions cmatrix() and confusion_matrix() are equivalent. """
confusion_matrix = lambda: print(_confusion_matrix)
cmatrix = confusion_matrix

_indicator = """It creates a simple widget indicator of a certain numerical or string 'value' with given string 'label'. This plot could be conveniently used in a matrix of subplots. If its optional 'trend' parameter is bigger, equal or lower then zero an upper, lower, or stable arrow is added to the plot to indicate if the value is increasing, decreasing or stable. It accepts also the parameters 'color' and 'style' to define any writing on the plot. """
indicator = lambda: print(_indicator)


_show = """It builds and prints the final figure on terminal. It is not necessary, if interactive(True) is called before.x"""
show = lambda: print(_show)

_build = """It created and returns the final figure canvas in string form, without actually printing it."""
build = lambda: print(_build)

_sleep = """It adds a sleeping time to the computation and it is generally useful when continuously plotting a stream of data, in order to reduce a possible screen flickering effect. Manually tweak this value to reduce the flickering."""
sleep = lambda: print(_sleep)

_time = """It returns the computational time of the latest show() or build() function. Note that functions, such as matrix_plot() or image_plot(), add a non-negligible computational time before show() or build() is called."""
time = lambda: print(_time)

_save_fig = """It saves the plot canvas to the file 'path' provided. If the file extension is '.html' the colors will be preserved. For all other file text extensions (like '.txt') all ansi color codes will be removed, unless the parameter 'keep_colors' is set to True. If True is passed to its 'append' parameter (False by default), the final result is appended to the file instead of replacing its content. 
To be used after the show() or build() function.
The functions savefig() and save_fig() are equivalent."""
save_fig = lambda: print(_save_fig)
savefig = save_fig

_from_matplotlib = """It takes a matplotlib figure and turns it into a plotext figure. It accepts the optional marker parameter.
Note: this feature may require further development."""
from_matplotlib = lambda: print(_from_matplotlib)



_date_form = """It sets how some functions interpret string based datetime objects; it accepts these two parameters: 

\x1b[96minput_form\x1b[0m to control how some functions - like string_to_datetime() - take strings as input and interpret them as date/time object.

\x1b[96moutput_form\x1b[0m to control how some functions - like datetime_to_string() - translates date/time objects into output strings. This includes functions internally called during the plotting process, to output date/time axes ticks. If not provided, it is internally set to 'input_form'. 

All the internal functions which deal with date/time objects have an internal 'input_form' or 'output_form' parameter (by default set to the previous values) for further flexibility. 
Date/time forms are the standard ones with the '%' removed for simplicity. Common forms are 'd/m/Y' (by default), 'H:M:S', 'd/m/Y H:M:S'."""
date_form = lambda: print(_date_form)

_set_time0 = """It sets the origin of time to the date/time string provided. The default value is 01/01/1900. This function is useful when using 'log' scale with date plots, in order to avoid "hitting" the 0 timestamp.
The date/time form could be set either with its 'input_form' parameter or with the date_form() function. Note that, for simplicity, '%' is not allowed in the forms."""
set_time0 = lambda: print(_set_time0)

_today_datetime = """It returns today's date/time as a datetime object."""
today_datetime = lambda: print(_today_datetime)

_today_string = """It returns today's date/time in string form. The date/time form could be set either with its 'output_form' parameter or with the date_form() function. Note that, for simplicity, '%' is not allowed in the forms."""
today_string = lambda: print(_today_string)

_datetime_to_string = """It turns a datetime object to a string. The date/time form could be set either with its 'output_form' parameter or with the date_form() function. Note that, for simplicity, '%' is not allowed in the forms."""
datetime_to_string = lambda: print(_datetime_to_string)

_datetimes_to_string = """It turns a list of datetime objects to a list of strings. The date/time form could be set either with its 'output_form' parameter or with the date_form() function. Note that, for simplicity, '%' is not allowed in the forms."""
datetimes_to_string = lambda: print(_datetimes_to_string)

_string_to_datetime = """It turns a string based date/time object into a datetime object. The date/time form could be set either with its 'input_form' parameter or with the date_form() function. Note that, for simplicity, '%' is not allowed in the forms."""
string_to_datetime = lambda: print(_string_to_datetime)



_script_folder = """It returns the folder containing the current script."""
script_folder = lambda: print(_script_folder)

_parent_folder = """It returns the parent folder of the given 'path'. The 'level' parameter is used to specify how many levels above to return (1 by default)."""
parent_folder = lambda: print(_parent_folder)

_join_paths = """It accepts as many strings as necessary and returns a properly formatted path. Eg: join_paths("/", "home", "file.txt") = "/home/file.txt".
The symbol '~', is interpreted as the user home folder. If no folder is specified, the home folder is considered."""
join_paths = lambda: print(_join_paths)

_save_text = """It saves some 'text' to the 'path' selected. Set 'log' to False to avoid printing a final message (True by default). If True is passed to its 'append' parameter (False by default), the final result is appended to the file instead of replacing its content. """
save_text = lambda: print(_save_text)

_read_data = """It reads and properly interprets some data from the 'path' selected. 

Here are its parameters:

\x1b[96mdelimiter\x1b[0m the delimiter between each data column (by default a space).

\x1b[96mcolumns\x1b[0m the list of columns to be returned (starting from 1): by default, all.

\x1b[96mheader\x1b[0m if True (as by default) the columns headers (i.e. the file first line) will be included. Set it to False to exclude those values.

\x1b[96mlog\x1b[0m if True (as by default) a final message is printed."""
read_data = lambda: print(_read_data)

_write_data = """It writes a matrix of 'data' to the 'path' selected. As the function read_data() it accepts the 'delimiter' and 'columns' parameters. 
If needed use the transpose() function. 
Set 'log' to False to avoid printing a final message (True by default)."""
write_data = lambda: print(_write_data)

_download = """It downloads an image/gif/video (or other) from the given 'url' to the 'path' selected. Set 'log' to False to avoid printing a final message (True by default)."""
download = lambda: print(_download)

_delete_file = """It deletes the file 'path', if it is a file. Set 'log' to False to avoid printing a final message (True by default)."""
delete_file = lambda: print(_delete_file)



_colorize = """It adds color codes to a 'string'. Here are its parameters:

\x1b[96mfullground\x1b[0m to sets the fullground string color.

\x1b[96mstyle\x1b[0m to sets the string style or styles. 

\x1b[96mbackground\x1b[0m to sets the background string color.

\x1b[96mshow\x1b[0m if True the final string is printed on terminal, otherwise it is returned (as by default).

Access the function plt.colors() and plt.styles() for the available color and style codes."""
colorize = lambda: print(_colorize)

_uncolorize = """It removes any coloring from a string."""
uncolorize = lambda: print(_uncolorize)

_terminal_size = """It returns the terminal size as [width, height]."""
terminal_size = lambda: print(_terminal_size)

_terminal_width = """It returns the terminal width."""
terminal_width = lambda: print(_terminal_width)

_terminal_height = """It returns the terminal height."""
terminal_height = lambda: print(_terminal_height)

_sin = """It creates a sinusoidal signal useful, for example, to test the plotext package. Here are its parameters:

\x1b[96mperiods\x1b[0m: the number of periodic repetitions (2 by default).

\x1b[96mlength\x1b[0m: the number of data points (200 by default).

\x1b[96mamplitude\x1b[0m: the maximum value of the sinusoidal signal (1 by default).

\x1b[96mphase\x1b[0m: if 0 (as by default), the sine function is returned; if 0.5, the cosine; if -1, the -sine; if -0.5, -cosine. Any float number is allowed.

\x1b[96mdecay\x1b[0m: adds a decay rate (normalized to the number of data points) which will cause the signal to exponentially decay for positive values or increase for negative ones. It is 0 by default. """
sin = lambda: print(_sin)

_square = """It creates a square wave signal useful, for example, to test the plotext package. As the sin() function it accepts the 'periods', 'length' and 'amplitude', parameters. """
square = lambda: print(_square)

_transpose = """It transposes a matrix."""
transpose = lambda: print(_transpose)

_colors = """It displays the available string, integer and RGB color convention available in plotext."""
colors = lambda: print(_colors)

_styles = """It displays the available text styles available in plotext."""
styles = lambda: print(_styles)

_markers = """It displays the available marker codes available in plotext. Note that any other single character is a legal possibility."""
markers = lambda: print(_markers)

_themes = """It displays the available plot themes available in plotext."""
themes = lambda: print(_themes)

_test = """It builds a matrix of plots, useful to quickly test plotext in your system."""
test = lambda: print(_test)


_all_docstrings = []
for _key, _value in list(locals().items()):
   if type(_value) == str and _key[:2] != "__" and _key not in ["positive_color", "negative_color", "title_color"]:
      _key = _key[1:]
      _all_docstrings.append([_key, _value])
       
def all():
   #print('\033c', end = "")
   print(colorizing("All Plotext Docstrings\n", title_color, "bold"))
   for el in _all_docstrings:
       print(colorizing(el[0], positive_color, "bold"))
       print(el[1])
       if el != _all_docstrings[-1]:
           print("")
