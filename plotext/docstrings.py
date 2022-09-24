#    Subplots Function
subplots_doc = """It creates a matrix of subplots. It requires two integers (different from 0) where the first sets the number of rows and the second the number of columns of the subplots matrix."""

subplot_doc = """It sets the subplot to use to plot data: further commands will refer to the subplot chosen. It requires two integers, where the first sets the row (from above) and the second the column (from left) which define the coordinates of the subplot addressed. Those values have to be lower then the correspondent ones set using the function subplots()."""

 
#    Clear Functions
clear_terminal_doc = """It clears the terminal screen and it is generally useful before plotting or when plotting a continuous stream of data. 
The functions clt() and clear_terminal() are equivalent."""

clear_figure_doc = """It clear all internal definitions of the figure, including its subplots. 
The functions clf() and clear_figure() are equivalent."""

clear_plot_doc = """It clear all internal definitions of the active subplot. 
The functions clp() and clear_plot() are equivalent."""

clear_data_doc = """It clear only the data relative to the active subplot, without clearing the plot style.
The functions cld() and clear_data() are equivalent."""


#    Set Functions
plotsize_doc = """It sets the plot size of the active subplot. It requires two parameters: the desired width and height of the plot. 
Note that plotsize(width, height) is equivalent to plotsize([width, height]) and that plotsize(integer) is equivalent to plotsize(integer, integer).
The functions plotsize() and plot_size() are equivalent."""


title_doc = """It set the title of the active subplot."""

xlabel_doc = """It set the label of the x axis relative to the active subplot."""

ylabel_doc = """It set the label of the y axis relative to the active subplot."""


xaxes_doc = """It sets whatever or not to show the x axes. It requires two Boolean parameters, one for each axis (lower and upper x axis). 
Note that xaxes(bool1, bool2) is equivalent to xaxes([bool1, bool2]) and that xaxes(bool) is equivalent to xaxes(bool, bool)."""

yaxes_doc = """It sets whatever or not to show the y axes. It requires two Boolean parameters, one for each axis (left and right y axis). 
Note that yaxes(bool1, bool2) is equivalent to yaxes([bool1, bool2]) and that yaxes(bool) is equivalent to yaxes(bool, bool)."""

grid_doc = """It sets whatever or not to show the x and y grid lines. It requires two Boolean parameters, one for each axis. 
Note that grid(bool_x, bool_y) is equivalent to grid([bool_x, bool_y]) and that grid(bool) is equivalent to grid(bool, bool)."""

axes_color_doc = """It sets the color of the axes background. 
Access the function plt.colors() to check the available color codes."""

ticks_color_doc = """It sets the color relative to any writing in the plot (title, legend, axes labels and ticks). 
Access the function plt.colors() to check the available color codes."""

canvas_color_doc = """It sets the canvas color. The canvas is the area where data is plotted. 
Access the function plt.colors() to check the available color codes."""

colorless_doc = """It removes all colors from the active subplot.
The function cls() and colorless() are equivalent."""


xlim_doc = """It sets the minimum and maximum values that could be plotted on the x axis. It requires a list of two numbers, where the first sets the left (minimum) limit and the second the right (maximum) limit.
Note that xlim(width, height) is equivalent to xlim([width, height])."""

ylim_doc = """It sets the minimum and maximum values that could be plotted on the y axis. It requires a list of two numbers, where the first sets the lower (minimum) limit and the second the upper (maximum) limit.
Note that ylim(width, height) is equivalent to ylim([width, height])."""


ticks_doc = """It sets the number of numerical ticks to show on the x axis and y axis respectively. It requires two integers, one for each axis. 
Note that ticks(width, height) is equivalent to ticks([width, height]) and that ticks(integer) is equivalent to ticks(integer, integer)."""

xticks_doc = """It sets the data ticks on the x axis. The ticks should be provided as a list of values. If two lists are provided, the second is intended as the list of labels to be printed at the coordinates given by the first list. If no list is provided, the ticks are calculated automatically."""

yticks_doc = """It sets the data ticks on the y axis. The ticks should be provided as a list of values. If two lists are provided, the second is intended as the list of labels to be printed at the coordinates given by the first list. If no list is provided, the ticks are calculated automatically."""

xscale_doc = """It sets the scale relative to the x axis, which could be either 'linear' (as by default) or 'log' (for logarithmic plots)."""

yscale_doc = """It sets the scale relative to the y axis, which could be either 'linear' (as by default) or 'log' (for logarithmic plots). Setting the parameter 'yscale' to either 'left' (by default) or 'right' the yscale of the two y axes could be set independently."""


#    Plotting Functions
scatter_doc = """It creates a scatter plot of coordinates given by the x and y lists. Optionally, a single y list could be provided. Here is a basic example:
  \x1b[32mimport plotext as plt
  plt.scatter(x, y)
  plt.show()\x1b[0m

Multiple data sets could be plotted using consecutive scatter functions:
  \x1b[32mplt.scatter(x1, y1)
  plt.scatter(y2)
  plt.show()\x1b[0m

Here are all the parameters of the scatter function:
 
\x1b[33myaxis\x1b[0m sets whatever to plot the data relative to the left or right y axis. It accepts 'left' and 'right' as inputs.

\x1b[33mlabel\x1b[0m sets the label of the current data set, which will appear in the legend at the top left of the plot. The default value is an empty string. If all labels are an empty string no legend will be printed. 

\x1b[33mmarker\x1b[0m sets the marker used to identify each data point, relative to the current data set. A single character could be provided or the available marker coded.  Access the function markers() for the available extra marker codes. The default value is "small". If 'None' is provided, the marker is set automatically.

\x1b[33mcolor\x1b[0m
It sets the color of the data points. Access the function plt.colors() to find the available full-ground color codes. If 'None' is provided (as by default) the colors are set automatically.

\x1b[33mfillx\x1b[0m
if True, extra data points will be plotted from the current plot to the x axis. The default value is False.

\x1b[33mfilly\x1b[0m
if True, extra data points will be plotted from the current plot to the y axis. The default value is False.
"""  

plot_doc = """It plots lines between the data points provided. It is very similar to the scatter function, except that no data point is plotted. 
Access the scatter function docstring for further documentation on its internal parameters."""

bar_doc = """It creates a bar plot using to the x and y values provided. The x values could be a list of numbers or strings, or optionally not provided. 
It accepts the same parameters as the scatter and plot functions (except for 'fillx' and 'filly', which are not allowed). Access the scatter function docstring for further documentation on its internal parameters.

Here are its extra parameters:

\x1b[33mfill\x1b[0m if set to True (as by default), the plot fills the bars with the chosen color; if False only the bars borders are plotted.

\x1b[33mwidth\x1b[0m is the relative width of the bars and could be a float ranging from 0 to 1. The default value is 4 / 5.

\x1b[33morientation\x1b[0m sets the orientation of the bar plot and could be either 'vertical' (in short 'v', as by default) or 'horizontal' (in short 'h')."""

hist_doc = """It builds the histogram plot relative to the data provided. It accepts the same parameters as the bar plot (access its docstring for further documentation) with the following extra parameter:

\x1b[33mbins\x1b[0m defines the number of equal-width bins in the range (default 10)."""


#    Show
show_doc = """It builds and prints the final figure on terminal. The parameter 'hide', if set to True, allows to build the figure without actually printing it (the default value is False)."""


#    Other Functions
string_to_time_doc = """It takes a date/time as a string and returns the correspondent number of seconds. The string format should be: 'DD/MM/YYYY hh:mm:ss'. Other accepted formats are:

'DD/MM/YYYY': in this case the time is set to 00:00:00.

'hh:mm:ss' in this case the date is set to today.

'DD/MM/YYYY hh:mm' in this case the seconds are set to 0.

'hh:mm' in this case the date is set to today and the seconds to 0."""


get_canvas_doc = """It returns the figure canvas as a string and it can be used only after the show() function."""

sleep_doc = """It adds a sleeping time to the computation and it is generally useful when continuously plotting a stream of data, in order to decrease a possible screen flickering effect.
An input of, for example, 0.01 would add (depending on your machine) approximately 0.01 secs to the computation. Manually tweak this value to reduce the possible flickering."""

savefig_doc = """It saves the plot canvas (without colors) as a text file, at the path provided as input. It can be used only after the show() function. 
The functions savefig() and save_fig() are equivalent."""

terminal_size_doc = """It returns the terminal size as width x height."""

version_doc = """It returns the version of the current installed plotext package."""

docstrings_doc = """It prints all the available docstrings"""

colors_doc = """It shows the available full-ground and background color codes."""

markers_doc = """It shows the available marker codes."""

sin_doc = """It creates a sinusoidal signal useful, for example, to test the plotext package. Here are its parameters:

length: the length of the signal.

peaks: the number of periods in the signal.

decay: the decay rate of the signal (normalized to length). If positive the signal exponentially increases. 

phase: if 0.5 the cosine is returned; if 1, -sine is returned. 
"""
