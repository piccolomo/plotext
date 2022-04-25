# Utilities
- [Command Line Tool](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool)
- [Colored Text](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#colored-text)
- [File Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities)
- [Clear Functions](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#clear-functions)
- [Other Functions](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#other-functions)
- [Docstrings](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#docstrings)

[Plotext Guide](https://github.com/piccolomo/plotext#guide)


## Command Line Tool

There are two ways one could use `plotext` directly on terminal. The first is by using the command line tool, for simple scatter, line, bar, histogram plot, as well as for image, gif, video and youtube rendering. For further documentation run, on terminal:

```console
plotext --help
```

![command-toll](https://raw.githubusercontent.com/piccolomo/plotext/master/images/command-tool.png)

Access the help for each function for further documentation; eg: `plotext scatter -h`. The flag -f is used to read from file; the tool recognizes some keywords for test files internally saved, so it is easy to test the tool following the examples shown on each function help page. For example:

```console
plotext scatter --file test_data -col 2 3 -m hd -c red+ -t 'Test Data' -xl time -yl Price -g True
plotext image --file test_image
plotext gif --file test_gif
plotext video --file test_video --from_youtube True
plotext youtube --url test_youtube
```

The second way requires the translation of a script into a single string and passing it to the `python3` command with flag `-c`.For example:
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
- each line has to terminate with a `;` and python strings, in any given line, should be surrounded by `'` instead of `"`. 

- each coded example in this [guide](https://github.com/piccolomo/plotext#guide) is followed by the correspondent direct terminal command line (of the second type).

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Colored Text

To obtained colored strings use the function `colorize(fullground, style, backgound, show)` which paints a string with the given styles, fullground and background colors. The styles and color codes are explained [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors). If `show = True` the string is directly printed and not returned. Here are a few examples:
```python
import plotext as plt

import plotext as plt
                                           #Fullground     #Style       #Backgroun        #Show
plt.colorize("black on white, bold",        "black",        "bold",      "white",         True)
plt.colorize("red on green, italic",        "red",          "italic",    "green",         True)
plt.colorize("yellow on blue, flash",       "yellow",       "flash",     "blue",          True)
plt.colorize("magenta on cyan, underlined", "magenta",      "underline", "cyan",          True)
plt.colorize("integer color codes",         201,            "default",   158,             True)
plt.colorize("RGB color codes",             (16, 100, 200), "default",   (200, 100, 100), True)
```
![colorize](https://raw.githubusercontent.com/piccolomo/plotext/master/images/colorize.png)

- Using the style `flash` will result in an actual flashing string.

- To remove any coloring use the function `uncolorize(string)`.

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## File Utilities

`Plotext` has a set of tools to easily manipulate files and file paths. Here is the list of its utilities:

- `script_folder()` returns the folder containing the script used.

- `parent_folder()` returns the parent folder of the path provided, at the level above specified.

- `join_paths()` joins as many strings into a proper file path. Eg: `plt.file.join_paths("/", "home", "file.txt")` returns `/home/file.txt`. If its first parameter is `~`, it will be interpreted as the user home folder. If no folder is specified, the home folder is considered.
 
- `save_text()` saves some text to the `path` specified.

- `read_data()` reads numerical data from the `path` specified, using the given delimiter between data columns (by default the space character), selecting the specified list of columns (starting from 1); the parameter `header` is used to include or not the first data row.

- `write_data()` write a matrix of data at the `path` specified.

- `download()` downloads an image/gif/video or other from the given `url` to the `path` selected.

- `get_youtube()` to download a youtube video.

- `delete_file()` deletes `path`, if it is a file.

- A series of test files are stored and could be easily accessed to test the main plotting functions:
    - `test_data_path`  is the path of some 3 columns test data
    - `test_image_path` is the path of a test image
    - `test_gif_path` is the path of a test GIF image
    - `test_video_path` is the path of a test video
    - `test_youtube_url` is the link to a test YouTube video

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Clear Functions

Here are all the available clear functions:

- `clear_figure()` - in short `clf()` - clears all internal definitions of the entire figure, including its subplots.

- `clear_data()` - in short `cld()` - clears only the data information relative to the active subplot, without clearing all the other plot settings.

- `clear_color()` - in short `clc()` - clears only the color settings relative to the active subplot, without clearing all other plot settings. The final rendering of this subplot will be colorless. This function is equivalent to `theme('clear')`

- `clear_terminal()` - in short `clt()` - clears the terminal screen and it is generally useful before plotting a continuous stream of data. It is recommended to use it before `show()`. If its `lines` parameter is set to an integer, only the specified number of lines will be cleared. In this case, it is recommended to use it after `show()`. Note that, depending on shell used, few extra lines may be printed after the plot.

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Other Functions

- `savefig(path)` saves the colourless version of the plot, as a text file, at the `path` specified. **If the path extension is `.html` the colors will be preserved.** To easily manipulate **file paths**, use the tools recommended in section [File Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities)

- `build()` is equivalent to `show()` except that the final figure canvas is returned as a string and not printed. 

- `time()` returns the computation time of the latest `show()` or `build()` functions. 

- `terminal_size()` - in short `ts()` - returns the size of the terminal.

- `terminal_width()` - in short `tw()` - returns the width of the terminal.

- `terminal_height()` - in short `th()` - returns the height of the terminal.

- `sleep()` adds a sleeping time to the computation.

- `sin(amplitude, periods, length, phase, decay)` outputs a sinusoidal signal with the given parameters.

- `transpose()` to transpose a matrix.

- `version()` returns the version of the current installed `plotext` package.

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Docstrings

All main `plotext` functions have a doc-string that can be accessed in three ways. For example the doc-string of the function `scatter()` can be accessed:

- using `print(scatter.__doc__)`

- more easily through the `doc` container: `doc.scatter()`.

- with `doc.all()` which prints all `plotext` doc-strings.

The functions `markers()` and `colors()` directly print useful information on how to use respectively [markers](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-markers) and [colors](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#marker-colors).


[Plotext Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)

