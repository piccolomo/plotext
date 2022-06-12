# Utilities
- [Clearing Functions](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#clearing-functions)
- [Useful Functions](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#useful-functions)
- [File Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities)
- [Command Line Tool](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool)
- [Colored Text](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#colored-text)
- [Docstrings](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#docstrings)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Clearing Functions
Here are all the available clear functions:

- `clear_figure()` - in short `clf()` - clears **all internal definitions** of the subplot it refers to, including its subplots; if it refers to the entire figure, it will clear everything,
- `clear_data()` - in short `cld()` - clears only the **data information** relative to the active subplot, without clearing all the other plot settings,
- `clear_color()` - in short `clc()` - clears only the **color settings** relative to the active subplot, without clearing all other plot settings; the final rendering of this subplot will be colorless; this function is equivalent to `theme('clear')`,
- `clear_terminal()` - in short `clt()` - clears the **terminal screen** and it is generally useful before plotting a continuous stream of data; it is recommended to use it before `show()`; if its `lines` parameter is set to an integer, only the specified number of lines will be cleared; in this case, it is recommended to use it after `show()`. Note that, depending on shell used, few extra lines may be printed after the plot.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Useful Functions
- `savefig(path)` saves the colourless version of the plot, as a text file, at the `path` specified:
    - if the path extension is `.html` the colors will be preserved,
    - if its parameter `keep_colors` is `True`, the `txt` version will keep the ansi color codes; in this case, in linux systems, the plot could be rendered on terminal with the command `less -R` followed by the file path,
    - to easily manipulate **file paths**, use the tools recommended in [this section](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities),
- `build()` is equivalent to `show()` except that the final figure canvas is returned as a string and not printed,
- `time(time)` returns the computation time of the latest `show()` or `build()` functions,
- `terminal_size()` - in short `ts()` - returns the width and height of the terminal,
- `terminal_width()` - in short `tw()` - returns the width of the terminal,
- `terminal_height()` - in short `th()` - returns the height of the terminal,
- `sleep(time)` adds a sleeping time to the computation,
- `sin(amplitude, periods, length, phase, decay)` outputs a sinusoidal signal with the given parameters: its documentation is available using `doc.sin()`,
- `transpose(matrix)` simply transposes a matrix,
- `version()` returns the version of the current installed `plotext` package.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## File Utilities
`plotext` includes a set of tools to easily manipulate files and file paths. Here is the list of its utilities:

- `script_folder()` returns the folder containing the script where it is run,
- `parent_folder(path, level = 1)` returns the parent folder of the `path` provided, at the level above specified,
- `join_paths(string1, string2 ...)` joins as many strings into a proper file path; eg: `plt.file.join_paths("/", "home", "file.txt")` returns `/home/file.txt`; if its first parameter is `~`, it will be interpreted as the user home folder; if no folder is specified, the home folder is considered,
- `save_text(text, path)` saves some text to the `path` specified,
- `read_data(path, delimiter, columns, header)` reads numerical data from the `path` specified, using the given `delimiter` between data columns (by default the space character), selecting the specified list of `columns` (starting from 1); the parameter `header` is used to include or not the first data row,
- `write_data(data, path, delimiter, columns, log)` write a matrix of data at the `path` specified; if `log` is True a final message is printed,
- `download(url, path, log = True)` downloads an image/gif/video or other, from the given `url` to the `path` selected,
- `get_youtube(url, path, log = True)` downloads a YouTube video from the given `url` to the `path` selected,
- `delete_file(path, log = True)` deletes `path`, if it is a file,
- a series of test files can be downloaded using the following url paths in conjunction with the function `download()`:
    - `test_data_url`  is the url of some 3 columns test data,
    - `test_bar_data_url` is the url of a simple 2 columns data used to test the `bar()` plot,
    - `test_image_url` is the url of a test image,
    - `test_gif_url` is the url of a test GIF image,
    - `test_video_url` is the url of a test video,
    - `test_youtube_url` is the url to a test YouTube video.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Command Line Tool
There are two ways one could use `plotext` directly on terminal. The first is by using its dedicated command line tool, to print a simple scatter, line, bar or histogram plot, as well as image plotting, and to play GIFs, video and YouTube. For further documentation run, on terminal:

```console
plotext --help
```
![command-tool](https://raw.githubusercontent.com/piccolomo/plotext/master/data/command-tool.png)

The documentation of each function is also available: eg: `plotext scatter -h`

![scatter-tool](https://raw.githubusercontent.com/piccolomo/plotext/master/data/scatter-tool.png)
The flag `--path` is used to read from file path, while `--lines` to plot a long data table iteratively at chunks, each `lines` long (1000 by default). 

The tool recognizes the keyword `test` as path, to internally downloads and finally remove some test file, in order for the user to easily test its tools. For example, run one of the following commands for the relative test:

```console
plotext scatter --path test --xcolumn 1 --ycolumns 2 --lines 5000 --title 'Scatter Plot Test' --marker braille
plotext plot --path test --xcolumn 1 --ycolumns 2 --sleep 0.1 --lines 2500 --clear_terminal True --color magenta+ --title 'Plot Test'
plotext plotter --path test --xcolumn 1 --ycolumns 2 --sleep 0.1 --lines 120 --clear_terminal True --marker hd --title 'Plotter Test'
plotext bar --path test --xcolumn 1 --title 'Bar Plot Test' --xlabel Animals --ylabel Count
plotext hist --path test --xcolumn 1 --ycolumns 2 --lines 5000 --title 'Histogram Test'
plotext image --path test
plotext gif --path test
plotext video --path test --from_youtube True
plotext youtube --url test
```

The second way is more completed, but more complex, and requires the translation of a script into a single string and passing it to the `python3` command with flag `-c`.For example:
```python
import plotext as plt
plt.scatter(plt.sin())
plt.title('Scatter Plot')
plt.show()
```
translates into:
```console
python3 -c "import plotext as plt; plt.scatter(plt.sin()); plt.title('Scatter Plot'); plt.show();"
```
- Each line has to terminate with a `;` and python strings, in any given line, should be surrounded by `'` instead of `"`. 
- each coded example in this [guide](https://github.com/piccolomo/plotext#guide) is followed by the correspondent direct terminal command line (of the second type).

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Colored Text
To obtained colored strings use the function `colorize(fullground, style, backgound, show)` which paints a string with the given fullground color, style or styles and background color. The color and available are presented [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors), while the styles [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#styles). If `show = True` the string is directly printed and not returned. Here are a few examples:
```python
import plotext as plt
                                            #Fullground     #Style       #Background      #Show
plt.colorize("black on white, bold",        "black",        "bold",      "white",         True)
plt.colorize("red on green, italic",        "red",          "italic",    "green",         True)
plt.colorize("yellow on blue, flash",       "yellow",       "flash",     "blue",          True)
plt.colorize("magenta on cyan, underlined", "magenta",      "underline", "cyan",          True)
plt.colorize("integer color codes",         201,            "default",   158,             True)
plt.colorize("RGB color codes",             (16, 100, 200), "default",   (200, 100, 100), True)
```
![colorize](https://raw.githubusercontent.com/piccolomo/plotext/master/data/colorize.png)
- Using the style `flash` will result in an actual flashing string,
- to remove any coloring use the function `uncolorize(string)`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Docstrings
All main `plotext` functions have a doc-string that can be accessed in three ways. For example the doc-string of the function `scatter()` can be accessed:
- using `print(scatter.__doc__)`,
- more easily through the `doc` container: `doc.scatter()`,
- with `doc.all()` which prints all `plotext` doc-strings.

The functions `markers()`, `colors()`, `styles()` and `themes()` directly print useful information on how to use respectively [markers](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#markers), [colors](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors), [styles](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#styles) and [themes](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#themes).


[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)

