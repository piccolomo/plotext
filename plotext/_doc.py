# this file contains all docstrings

from ._doc_utils import method, doc, par, past, out, t

method("subplots")
doc("It creates a matrix of subplots.\n\nNested subplots are allowed; for example: subplots(2, 2); subplot(1, 1); subplots(3, 4) - or directly subplots(2, 2).subplot(1, 1).subplots(3, 4) - creates a 2 by 2 matrix where the first subplot is a 3 by 4 matrix.")
par("rows", "sets the number of rows relative to the matrix of subplots.", t.int, 1)
par("cols", "sets the number of columns relative to the matrix of subplots.", t.int, 1)
out('the figure object containing the matrix of subplots', t.fig)


method("subplot")
doc("It sets (and returns) the active subplot in the matrix of subplots, such that further commands will refer to it.\n\nNote that most of the commands referring to the active subplot, could be alternatively passed directly to it. Eg: subplot(1, 3); plotsize(100, 30) becomes subplot(1, 3).plotsize(300, 30).")
par("row", "sets the row relative to the active subplot in the matrix of subplots, from above and counting from 1.", t.int, 1)
par("col", "sets the column relative to the active subplot in the matrix of subplots, from left and counting from 1.", t.int, 1)
out('the selected figure object', t.fig)


method("main")
doc("It returns the main figure (at the uppermost level in the matrix of subplots, if present), and sets the active figure to it. Any further commands will apply to the entire figure and to any of its subplots.")
out('the main figure object', t.fig)


method("active")
doc("It returns the active figure, which can be changed using the subplot() method.")
out('the active figure object', t.fig)


method("interactive")
doc("It allows to plot dynamically without using the show() method. A new plot is shown automatically when any change is made to the plot. By default plots are not shown dynamically.")
par("interactive", "is the Boolean required to make the plot dynamic.", 'bool', False)


method("plot_size", "plotsize")
doc("It sets the plot size of the active figure.\n\n")
par("width", "sets the width of the active subplot (in unit of character width). If None the terminal width is used.", t.int, None)
par("height", "sets the height of the active subplot (in unit of character height). If None the terminal height is used.", t.int, None)
out('The plot width and height (in character units).', t.list_int(2))


method("limit_size", "limitsize"),
doc("It sets, whatever or not, to limit the plot size to the terminal dimensions. To manually set the plot dimensions use the plot_size() method afterwards.\n\nThis method is only available to the main figure and not to its subplots, if present   ")
par("width", "sets whatever or not to limit the plot width to the terminal width.", t.bool, True)
par("height", "sets whatever or not to limit the plot height to the terminal height.", t.bool, True)


method("take_min", "takemin")
doc("In a matrix of subplots, the plot widths/heights will be set to the same value for each column/row.\n\nBy default the maximum value is considered, but if the take_min() method is called, the minimum is considered instead.\n\nThis method is available to the main figure, as well any of its subplot independently.")      


method("title")
doc("It sets the title of the active plot.")
par("label", "the string label required", t.str)      



method("xlabel")
doc("It sets the label relative to the x axis.")
past("label", "title")
par("xside", "it allows to independently address either the 'lower' or 'upper' x axis (1 or 2 in short).", t.str_int, 'lower')      


method("ylabel")
doc("It sets the label of the y axis.")
past("label", "xlabel")
par("yside", "it allows to independently address either the 'left'  or 'right' y axis (1 or 2 in short).", t.str_int, 'left')


lim_message = ' If \'None\', the limit is calculated automatically.'

method("xlim")
doc("It sets the numerical limits relative to the x axis. Values outside this range will not be plotted.")
par("left", "it sets the left (or minimum) plot limit relative to the x axis. A date in string form is accepted." + lim_message, t.str_num, None)
par("right", "it sets the right (or maximum) plot limit relative to the x axis. A date in string form is accepted." + lim_message, t.str_num, None)
past("xside", "xlabel")


method("ylim")
doc("It sets the limits relative to the y axis. Values outside this range will not be plotted.")
par("lower", "it sets the lower (or minimum) plot limit relative the y axis. A date in string form is accepted." + lim_message, t.str_num, None)
par("upper", "it sets the upper (or maximum) plot limit relative the y axis. A date in string form is accepted." + lim_message, t.str_num, None)
past("yside", "ylabel")


method("xscale") 
doc("It sets the scale (linear or base 10 logarithmic) relative to the x axis.")
par("scale", "the axis scale, either 'linear' or 'log'.", t.str, 'linear')
past("xside", "xlim")


method("yscale") 
doc("It sets the scale (linear or base 10 logarithmic) relative to the y axis.")
past("scale", "xscale")
past("yside", "ylim")

   
method("xticks") 
doc("It sets the numerical data ticks and string labels relative to the x axis.")
par("ticks", "the list of numerical data ticks. Dates in string form are accepted.", t.list_str_num())
par("labels", "the optional list of ticks labels to be printed at the ticks coordinates given.", t.list_str_num())
past("xside", "xlim")      



method("yticks") 
doc("It sets the numerical data ticks and string labels relative to the y axis.")
past("ticks", "xticks")
past("labels", "xticks")
past("yside", "ylim") 


method("xfrequency") 
doc("It sets the number of numerical ticks relative to the x axis. The actual numerical values are calculated automatically.\n\nTo set the ticks manually use the xticks() method instead. Note that xticks() overrules xfrequency().")
par("frequency", "the integer number of numerical ticks.", t.int, 5)
past("xside", "xlim")

method("yfrequency") 
doc("It sets the number of numerical ticks relative to the y axis. The actual numerical values are calculated automatically.\n\nTo set the ticks manually use the yticks() method instead. Note that yticks() overrules yfrequency().")
par("frequency", "the integer number of numerical ticks.", t.int, 7)
past("yside", "ylim")


method("xreverse")
doc("It reverses the x axis direction.")
par("reverse", "the Boolean required to reverse the axis (if True).", t.bool, False)
past("xside", "xlim")


method("yreverse")
doc("It reverses the y axis direction.")
past("reverse", "xreverse")
past("yside", "ylim")      


method("xaxes") 
doc("It is used to show or remove the x axes independently.")
par("lower", "the Boolean required to show or not the lower x axis.", t.bool, True)
par("upper", "the Boolean required to show or not the upper x axis.", t.bool, True)      


method("yaxes") 
doc("It is used to show or remove the y axes independently.")
par("left",  "the Boolean required to show or not the left y axis.", t.bool)
par("right", "the Boolean required to show or not the right y axis.", t.bool)


method("frame") 
doc("It is used to show or remove all 4 axes (which constitute the canvas frame) at the same time.\n\nTo address any individual axis use the xaxes() and yaxes() methods instead.")
par("frame", "the Boolean required to show or not all plot axes.", t.bool, True) 


method("grid") 
doc("It is used to show or remove the plot grid lines.")
par("horizontal", "the Boolean required to show the horizontal grid lines.", t.bool, False)
par("vertical", "the Boolean required to show the vertical grid lines.", t.bool, False)      


method("canvas_color") 
doc("It sets the background color relative to the plot canvas, which is the area where the data points are plotted.")
par("color", "the color code: access the colors() method for the available codes.", t.color, 'white')


method("axes_color") 
doc("It sets the background color relative to the axes, which is the area where the axes are plotted, and include the axes numerical ticks, the axes labels and the plot title (but not the plot legend, which is set automatically using the canvas_color() method).")
past("color", "canvas_color")


method("ticks_color") 
doc("It sets the color relative to any writing on the plot: the axes, its numerical ticks and labels, the plot title and the plot legend.")
past("color", "canvas_color", 'black')


method("ticks_style") 
doc("It sets the style relative to any writing on the plot: the axes, its numerical ticks and labels, the plot title and the plot legend.")
par("style", "the style code: access the styles() method for the available style codes.", t.str, 'default')      


method("theme") 
doc("It sets the color theme relative to the active plot.")
par("theme", "the string theme code: access the themes() method for the available theme codes.", t.str, 'default')      


method("clear_figure", "clf")
doc("It clears everything relative to the addressed figure, including its subplots.")


method("clear_data", "cld")
doc("It clears only the data, previously plotted, relative to the addressed figure, including its subplots, without clearing any other plot settings.")

method("clear_color", "clc")
doc("It clears only the color settings relative to the addressed figure, including its subplots, without clearing any other plot settings. The final rendering of this subplot will be colorless.")


method("clear_terminal", "clt") 
doc("It clears the terminal screen and it is generally useful when plotting a continuous stream of data.\n\nNote that depending on the terminal shell used, few extra lines may be printed after the plot.")
par("lines", "the optional number of terminal lines to be cleared. If None, the entire terminal will be cleared.", t.int, None)      


method("scatter") 
doc("It creates a scatter plot of coordinates given by the x and y lists provided.\n\nMultiple data sets can be plotted using consecutive plotting functions.")
par("args", "The coordinates x and y (or just y) of the data points to be plotted; string dates are accepted.", t.xy)
par("marker", "the marker used to identify the data points, which could be a single character or the available marker codes, accessible with the markers() method; a list of markers, one for each data point, could also be provided.", t.marker, 'hd')
par("color", "the color code of the data points, accessible with the colors() method; a list of colors, one for each data point, could also be provided.", t.color_list, 'blue+')
par("style", "the style of the data points, accessible with the styles() method; a list of styles, one for each data point, could also be provided.", t.marker, 'default')
par("fillx", "if True, for each data point, a vertical line ending on the x axis (the level y = 0) will be printed; if a specific numerical value is provided, the line will stop at that y coordinate; if the string code 'internal' is provided, the line will stop when another data point is reached (if it exists); if False, no line will be printed.", t.bool_num_str, False)
par("filly", "if True, for each data point, an horizontal line ending on the y axis (the level x = 0) will be printed; if a specific numerical value is provided, the line will stop at that x coordinate; if the string code 'internal' is provided, the line will stop when another data point is reached (if it exists); if False, no line will be printed.", t.bool_num_str, False)
past("xside", "xlim")
past("yside", "ylim")
par("label", "the label of the current data set, which will appear in the legend menu at the top left corner of the plot canvas. If None, no label is added.", t.str, None)


method("plot") 
doc("It creates a plot of lines between consecutive data points using the coordinates given by the x and y lists. \n\nMultiple data sets can be plotted using consecutive plotting functions.")
past("args", "scatter")
past("marker", "scatter")
past("color", "scatter")
past("style", "scatter")
past("fillx", "scatter")
past("filly", "scatter")
past("xside", "scatter")
past("yside", "scatter")
past("label", "scatter")

   
method("candlestick") 
doc("It creates a candlestick plot.")
par("dates", "the list of strings, each representing a date time object; use the date_form() method to set the accepted date/time forms.", t.list_str())
par("data", "the numerical data to be plotted.", t.dic)
par("colors", "the two colors used to identify the positive and negative candlesticks; access the colors() method for the available color codes.", t.list_color(2), ['blue+', 'green+'])
par("orientation", "the orientation of the plot which could be either 'vertical' (in short 'v', as by default) or 'horizontal' (in short 'h').", t.str, 'vertical')
past("xside", "scatter")
past("yside", "scatter")
past("label", "scatter")


method("bar") 
doc("It creates a bar plot using the x and y data provided.")
par("args", "The coordinates x and y (or just y), of the bars; string labels or dates are accepted (but only as x values).", t.xy)
par("marker", "the marker used to identify the bars, which could be a single character or the available marker codes, accessible with the markers() method.", t.str, 'sd')
par("color", "the color code of the bars, accessible with the colors() method.", t.color, 'blue+')
par("fill", "if True, the bars will be filled with the the given colored markers, otherwise only its borders would be printed.", t.bool, True)
par("width", "the relative width of the bars, expressed as a float ranging from 0 to 1.", 'number', 4 / 5)
past("orientation", "candlestick")
par("minimum", "the minimum value of all the bars; this value could be easily tweaked, particularly when a logarithmic scale is chosen along the bars height.", 'number', 0)
par("reset_ticks", "if True, the center coordinates at the base of each bar will be calculated (starting from 1) and printed automatically; otherwise the numerical ticks, along the base of the bars, will be calculated as for any other plot.", t.bool, True)
past("xside", "scatter")
past("yside", "scatter")
past("label", "scatter")


method("simple_bar") 
doc("It creates a simpler and sketchier version of an horizontal bar plot.\n\nNote that this plot cannot be fit into a matrix of subplots and any setting methods - like plot_size() or canvas_color() etc ... - will not have any effect on it.")
past("args", "bar")
past("marker", "bar")
past("color", "bar")
par("title", "the title of the plot. If None, no title will be added.", t.str, None)
par("width", "sets the horizontal width of the plot; if None, the width will adapt to the terminal size.", t.int, None)


method("multiple_bar") 
doc("It creates a bar plot where multiple bars are grouped together (along the bar width axis) and have the same bar label.")
par("args", "The coordinates x and Y (or just Y), of the bars, where Y is a list of lists, each containing the bar heights of the correspondent bar plot; string labels or dates are accepted (but only as x values).", t.multiple_xy)
par("marker", "the marker used to identify the bars, which could be a single character or the available marker codes, accessible with the markers() method; a list of markers (with same length as Y) could also be provided to separately set the marker of each bar", t.str_list, 'sd')
par("color", "the list of colors (with same length as Y) used to identify each bar in a group of bars; access the colors() method for the available color codes.", t.list_color())
past("fill", "bar")
past("width", "bar")
past("orientation", "bar")
past("minimum", "bar")
past("reset_ticks", "bar")
past("xside", "scatter")
past("yside", "scatter")
par("labels", "the list of labels, one for each bar plot (with same length as Y), which will appear in the legend menu at the top left corner of the plot canvas.", t.list_str())


method("simple_multiple_bar") 
doc("It creates a simpler and sketchier version of an horizontal multiple bar plot.\n\nNote that this plot cannot be fit into a matrix of subplots and any setting methods - like plot_size() or canvas_color() etc ... - will not have any effect on it.")
past("args", "multiple_bar")
past("marker", "multiple_bar")
par("colors", "the list of colors (with same length as Y) used to identify each bar in a group of bars; access the colors() method for the available color codes.", t.list_color())
past("title", "simple_bar")
past("width", "simple_bar")
past("labels", "multiple_bar")


method("stacked_bar") 
doc("It creates a bar plot where multiple bars are stacked on top of each other (along the bar height axis) and have the same bar label.")
past("args", "multiple_bar")
past("marker", "multiple_bar")
past("color", "multiple_bar")
past("fill", "bar")
past("width", "bar")
past("orientation", "bar")
past("minimum", "bar")
past("reset_ticks", "bar")
past("xside", "scatter")
past("yside", "scatter")
past("labels", "multiple_bar")


method("simple_stacked_bar") 
doc("It creates a simpler and sketchier version of an horizontal stacked bar plot. \n\nNote that this plot cannot be fit into a matrix of subplots and any setting methods - like plot_size() or canvas_color() etc ... - will not have any effect on it.")
past("args", "multiple_bar")
past("marker", "multiple_bar")
past("colors", "simple_multiple_bar")
past("title", "simple_bar")
past("width", "simple_bar")
past("labels", "multiple_bar")


method("hist") 
doc("It builds the histogram plot.")
par("data", "the data to build an histogram upon.", t.list_num())
par("bins", "the number of channels between the minimum and maximum values of the data set, used to count the data frequency.", t.int, 10)
past("marker", "scatter")
past("color", "scatter")
past("fill", "bar")
par("norm", "If true, each frequency count is normalized, such that the sum of all counts is 1 (instead of the length of the data set).", t.bool, False)
past("width", "bar")
past("orientation", "bar")
past("minimum", "bar")
past("xside", "scatter")
past("yside", "scatter")
past("label", "scatter")


method("box")
doc("It creates a box plot. Further development needed.")
par("args", "The coordinates x and Y (or just Y), of the bars, where Y is a list of lists, one for each box element; string labels or dates are accepted (but only as x values).", t.multiple_xy)
par("quintuples", "If True, the input data is an array of 5 elements, each representing the precomputed quantiles at levels 0, 25, 50, 75, 100 s, otherwise it's the original data.", t.bool, False)
par("colors", "A list of two colors, one for the box body and the other for its inner lines", t.list_color(2), ['green', 'red'])
past("fill", "bar")
past("width", "bar")
past("orientation", "bar")
past("minimum", "bar")
past("reset_ticks", "bar")
past("xside", "scatter")
past("yside", "scatter")
past("label", "scatter")


method("bar") 
doc("It creates a bar plot using the x and y data provided.")
par("args", "The coordinates x and y (or just y), of the bars; string labels or dates are accepted (but only as x values).", t.xy)
par("marker", "the marker used to identify the bars, which could be a single character or the available marker codes, accessible with the markers() method.", t.str, 'sd')
par("color", "the color code of the bars, accessible with the colors() method.", t.color, 'blue+')
par("fill", "if True, the bars will be filled with the the given colored markers, otherwise only its borders would be printed.", t.bool, True)
par("width", "the relative width of the bars, expressed as a float ranging from 0 to 1.", 'number', 4 / 5)
past("orientation", "candlestick")
par("minimum", "the minimum value of all the bars; this value could be easily tweaked, particularly when a logarithmic scale is chosen along the bars height.", 'number', 0)
par("reset_ticks", "if True, the center coordinates at the base of each bar will be calculated (starting from 1) and printed automatically; otherwise the numerical ticks, along the base of the bars, will be calculated as for any other plot.", t.bool, True)
past("xside", "scatter")
past("yside", "scatter")
past("label", "scatter")

method("error") 
doc("It build a scatter plot with error bars.\n\nNote that no marker parameter is needed, as the markers are automatically set to straight lines.")
past("args", "scatter")
par("xerr", "The errors relative to the x data.", t.list_num())
par("yerr", "The errors relative to the y data.", t.list_num())
past("color", "scatter")
past("xside", "scatter")
past("yside", "scatter")
past("label", "scatter")



method("event_plot", "eventplot") 
doc("It plots parallel lines at the coordinates provided.")
par("data", "The list of coordinates identifying each line; string dates are also accepted.", t.x)
past("marker", "scatter")
past("color", "scatter")
past("orientation", "bar")
par("side", "It is used to identify on which axis to plot the data. It could be the 'lower' or 'upper' x axis (1 or 2 in short) for 'vertical' orientation, and 'left' or 'right' y axis (1 or 2 in short) for 'horizontal' orientation.", t.str_int, 'lower')



method("vertical_line", "vline") 
doc("It plots a vertical line, spanning the entire canvas range, along the y axis.")
par("coordinate", "the x coordinate where the vertical line should be placed; string dates are allowed.", t.str_num)
par("color", "the color code of the line, accessible with the colors() method.", t.color, 'black')
past("xside", "scatter")


method("horizontal_line", "hline") 
doc("It plots an horizontal line, spanning the entire canvas range, along the y axis.")
par("coordinate", "the y coordinate where the horizontal line should be placed; string dates are allowed.", t.str_num)
past("color", "vertical_line")
past("yside", "scatter")


method("text") 
doc("It adds a text label to the plot at the given coordinate.")
par("label", "The text to add to the plot; the new line character \\n will return multiple sub strings with the same alignment.", t.str)
par("x", "the x coordinate of the text; date strings are accepted.", t.str_num)
par("y", "the y coordinate of the text; date strings are accepted.", t.str_num)
par("color", "the color code of the text, accessible with the colors() method.", t.color, 'green+')
par("background", "the text background color code, accessible with the colors() method.", t.color, 'white')
par("style", "the style code of the text, accessible with the styles() method.", t.str, 'default')
past("orientation", "bar", 'horizontal')
par("alignment", "the text alignment, which could be either 'left', 'center', and 'right' (for horizontal orientation) or 'top', 'center' and 'bottom' (for vertical orientation).", t.str, "center")
past("xside", "scatter")
past("yside", "scatter")



method("rectangle") 
doc("It creates a rectangle with the given coordinates.")
par("x", "the two x coordinates of the rectangle.", t.list_str(2))
par("y", "the two y coordinates of the rectangle.", t.list_str(2))
par("marker", "the marker used to identify the shape plotted, which could be a single character or the available marker codes, accessible with the markers() method,", t.marker, 'hd')
par("color", "the color code of shape plotted, accessible with the colors() method", t.color, 'blue+')
par("lines", "If True, the shape borders will be shown, otherwise just its vertices.", t.bool, True)
par("fill" , "if True, the body of the shape will be filled with colored markers.", t.bool, True)
past("xside", "scatter")
past("yside", "scatter")
past("label", "scatter")


method("polygon") 
doc("It creates a polygon centered at the given coordinates.")
par("x", "the polygon center x coordinate.")
par("y", "the polygon center y coordinate.")
par("radius", "the distance of the polygon vertices to the center; for a circle, it corresponds to its actual radius, hence the name.", 'number', 1)
par("sides", "the number of sides of the polygon. To simulate a circle, input a high number (> 50).", t.int, 3)
past("marker", "rectangle")
past("color", "rectangle")
past("lines", "rectangle")
past("fill" , "rectangle")
past("xside", "scatter")
past("yside", "scatter")
past("label", "scatter")


method("confusion_matrix", "cmatrix") 
doc("It plots the confusion matrix correspondent to the actual and predicted data sets provided.")
par("actual", "the real data", t.list_num_bool())
par("predicted", "the predicted data, of same size as the 'actual' data", t.list_num_bool())
par("color", "the color code of any writing on the plot, including the axes; this will affects the canvas colors, which are automatic levels of gray-scale; access the colors() method for the available color codes.", t.color, 'orange+')
par("style", "the style code of any writing on the plot; access the styles() method for the available style codes.", t.str, 'bold')
par("labels", "a list of labels, one for each unique and sorted data value; the labels will automatically appear on both axes.", t.list_str())


method("indicator") 
doc("It creates a simple widget indicator, which occupies the entire plot and could be conveniently used in a matrix of subplots.")
par("value", "the value to be displayed at the center of the plot.", t.str_num)
par("label", "the label describing the value, appearing a plot title.", t.str)
past("color", "confusion_matrix")
past("style", "confusion_matrix")


method("matrix_plot")
doc("It creates a two dimensional plot of a matrix. The intensity of each element in the plot (a gray-scale level) is proportional to the correspondent element in the matrix (whiter for higher values). If a matrix of RGB colors is provided, each like (13, 45, 176), the color of each pixel will be the actual RGB color code provided.")
par("matrix", "the matrix of data to be plotted", t.matrix)
par("marker", "the marker used to identify the data points, which could be a single character or the available marker codes, accessible with the markers() method; note that higher resolution markers ('hd', 'fhd' and 'braille') will not result in an improved spatial resolution, as the color resolution is limited by a full character in all cases.", t.marker, 'sd')
past("style", "scatter")
par("fast", "if True, the plot will be rendered faster but most setting methods - like plot_size() or canvas_color() etc... - will not have any effect and the plot could not be nested in a matrix of subplots.",t.bool, False)


method("image_plot") 
doc("It plots an image from file. \n\nIt is recommended to call the plot_size() method before this one, especially for larger images, to reduce the image size and so the computational load.")
par("path", "the file path of the image", t.str)
past("marker", "matrix_plot")
past("style", "matrix_plot")
past("fast", "matrix_plot")
par("grayscale", "If True, the image will be rendered in gray-scale levels.", t.bool, False)


method("play_gif") 
doc("It plays a GIF on terminal. The images will adapt to the screen size unless plot_size() method is used before.\n\nNote: this feature may require further development.")
par("path", "image_plot")


method("play_video") 
doc("It plays a video, with audio, from file. The frames will adapt to the screen size unless plot_size() is used before.\n\nNote: this feature may require further development.")
par("path", "the file path of the video", t.str)
par("from_youtube", "set this parameter to True, if the video was downloaded from YouTube.",t.bool, False)


method("play_youtube")
doc("It plays a YouTube video, with audio, from url.\n\nNote: this feature may require further development.")
par("url", "the url link of the YouTube video", t.str)


path_message = " If only the file name is provided, the parent folder will be automatically set to the user home directory."

method("get_youtube") 
doc("It downloads a youtube video.")
past("url", "play_youtube")
par("path", "The location where the video should be saved." + path_message, t.str)
par("log", "if True, a simple confirmation or warning message will appear on terminal.", t.bool, True)


method("show") 
doc("It builds and prints the final figure on terminal.\n\nIf interactive(True) has been previously called, the show() method will not be necessary.")

method("build") 
doc("It created and returns the final figure canvas in string form, without actually printing it.\n\nTo build and print, use the show() method instead.")
out('The plot canvas in string form', t.str)

method("sleep") 
doc("It adds a sleeping time to the computation and it is generally useful when plotting a continuous stream of data, in order to reduce undesired screen flickering effects. Manually tweak this value to reduce the flickering.")
par("time", "The sleeping time, in seconds.", t.float, 0)


method("time") 
doc("It returns the computational time of the latest show() or build() method called.\n\nNote that functions, such as matrix_plot() or image_plot(), add a non-negligible computational time before the show() or build() methods are called.")
par("show", "If True, the time is also printed in an easier to read format.", t.bool, True)
out('The computation time of the latest show() or build() method called (in seconds).', t.float)


method("save_fig", "savefig") 
doc("It saves the plot canvas as text or html. \n\nIt is recommended to use it after the show() or build() method.")
par("path", "The file path where the plot should be saved." + path_message, t.str)
par("append", "If True, the final figure is appended to the text file, instead of replacing it.", t.bool, False)
par("keep_colors", "If True, the ansi color codes will be preserved. Note that if the path file extension is '.html', the colors will be preserved automatically.", t.bool, False)


method("from_matplotlib") 
doc("It takes a matplotlib figure and turns it into a plotext one.\n\nNote: this feature may require further development.")
par("fig", 'The matplotlib figure to turn into a plotext one.', 'a matplotlib figure')
past('marker', 'bar')



iso_message = " It uses the standard Python ISO string forms, except '%' symbol is removed for simplicity. "
global_message = "Use the date_form() method to set this parameter globally. "


method("date_form") 
doc("It sets how to interpret string as datetime objects.\n\nNote that most methods that deal with string dates, have an internal 'input_form' or 'output_form' parameter for further flexibility.")
par("input_form", "The string form used to interpret input strings as dates." + iso_message, t.str, 'd/m/Y')
par("output_form", "The string form used to print dates as an output string. By default, it corresponds to the input one." + iso_message + global_message, t.str, 'd/m/Y')


method("set_time0") 
doc("It sets the origin of time using the string provided. \n\nThis method is useful with logarithmic scale in date plots, in order to avoid 'hitting' the 0 timestamp.")
par("string", "The string identifying the 0 time mark.", t.str, '01/01/1900')
par("input_form", "The string form used to interpret the input string as a date." + iso_message + global_message, t.str, 'd/m/Y')


method("today_datetime") 
doc("It returns today's date and time as a datetime object.")
out("Today's date time.", t.datetime)


method("today_string") 
doc("It returns today's date and time in string form.")
par("output_form", "The string form used to print the today's date as an output string." + iso_message + global_message, t.str, 'd/m/Y')
out("Today's date time.", t.str)


method("datetime_to_string") 
doc("It turns a datetime object to a string.")
par("datetime", "A datetime object.", t.datetime)
par("output_form", "The string form used to print the datetime object as an output string." + iso_message + global_message, t.str, 'd/m/Y')
out('the correspondent date time string', t.str)


method("datetimes_to_strings")
doc("It turns a list of datetime objects to a list of strings.")
par("datetimes", "A list of datetime objects.", t.list_datetime)
par("output_form", "The string form used to print the datetime objects as output strings." + iso_message + global_message, t.str, 'd/m/Y')
out('A correspondent list of date time strings', t.list_str())



method("string_to_datetime")
doc("It turns a string into a datetime object.")
par("string", "The string to convert to a datetime object.", t.str)
past("input_form", "set_time0")
out('The datetime object corresponded to the string provided.', t.datetime)



method("script_folder")
doc("It returns the parent folder (in string form) of the script where this method is run from.")
out('The script folder', t.str)


method("parent_folder") 
doc("It returns the parent folder of the path provided.")
par("path", "The file path.")
par("level", "The numbers of levels above the current one, in the folder structure, used to identify the parent folder.", int, 1)
out('The parent folder', t.str)

path_message = " Note that the symbol '~', is interpreted as the user home folder and if no folder is specified, the home folder is considered by default. "


method("join_paths") 
doc("It turns a sequence of strings into a properly formatted file or folder path, dependent on the operating system used.\n\nFor example, the strings \"/\", \"home\" and \"file.txt\" would be properly joined into \"/home/file.txt\" in Unix systems.")
par("args", "The list of strings to turn into a path." + path_message, t.list_str())
out('The joined paths.', t.str)



method("save_text") 
doc("It saves some text to file.")
par("text", "The string to save", t.str)
par("path", "The path location where the text should be saved." + path_message, t.str)
past("log", "get_youtube")     


method("read_data") 
doc("It reads and properly interprets the tabular data from the path selected.")
par("path", "The path location of the data." + path_message, t.str)
par("delimiter", "The character used to separate data columns in the text file.", t.str, ' ')
par("columns", 'The list of column indexes to consider (starting from 0); if None, all columns will be included.', t.list_int(), None)
par("first_row", "The first row from which to acquire data (counting from 0).", t.int, 0)
past("log", "save_text")
out('The data read.', 'a matrix of numbers or strings')


method("write_data") 
doc("It writes a tabular data to file.")
par("data", "The data to write to file.", t.data)
past("path", "save_text")
past("delimiter", "read_data")
past("columns", "read_data")
past("log", "read_data")


method("download") 
doc("It downloads an image/gif/video (or other) from the given URL to file.")
par("url", "The URL to download.", t.str)
par("path", "The path location where the content should be saved." + path_message, t.str)
past("log", "read_data")


method("delete_file") 
doc("It deletes the file selected, if it exists.")
par("path", "The file path to delete." + path_message, t.str)
past("log", "read_data")


method("colorize") 
doc("It adds colors and styles to a string.")
par("string", "The string to add colors and styles to", t.str)
par("color", "the fullground color code: access the colors() method for the available codes.", t.color)
par("style", "the style code: access the styles() method for the available codes.", t.str)
par("background", "the background color code: access the colors() method for the available codes.", t.color)
par("show", "If True, the string is also directly printed.", t.bool, False)
out('The colorized and stylized string.', t.str)


method("uncolorize")
doc("It removes any coloring codes from a string.")
par("string", "The string to remove color codes from.", t.str)
out('The string with no color or style ansi codes.', t.str)


method("terminal_size", "ts") 
doc("It returns the terminal size.")
out('The terminal width and height (in character units)', t.list_int(2))


method("terminal_width", "tw")
doc("It returns the terminal width.")
out('The terminal width (in character units)', t.int)


method("terminal_height", "th")
doc("It returns the terminal height.")
out('The terminal height (in character units)', t.int)


method("sin") 
doc("It returns a sinusoidal signal useful, for example, to quickly test some plotext plotting methods.")
par("periods", "The number of periods in the signal.", t.float, 2)
par("length", "The number of data points.", t.int, 200)
par("amplitude", "The amplitude of the signal.", t.float, 1)
par("phase", "The relative phase of the sinusoidal (in pi units); 0.5 returns a cosine signal, while 1 a negative sinusoidal.", t.float, 0)
par("decay", "The relative decay rate of the signal, independent on the number of data points.", t.float, 0)
out('the sinusoidal signal', t.list_num())


method("square") 
doc("It returns a square wave signal useful, for example, to quickly test some plotext plotting methods.")
past("periods", "sin")
past("length", "sin")
past("amplitude", "sin")
out('the square signal', t.list_num())


method("transpose") 
doc("It transposes a matrix of data.")
past("data", "write_data")
out('The transpose data', 'A list of lists')


method("colors") 
doc("It displays the available string, integer and RGB color codes available in plotext.")


method("styles") 
doc("It displays the available string style codes available in plotext.")


method("markers") 
doc("It displays the available marker codes available in plotext. Note that any other single character is a valid marker.")


method("themes") 
doc("It displays the available plot themes available in plotext.")


method("test")
doc("It builds a matrix of plots, useful to quickly test plotext after installation.")
