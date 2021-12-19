[Plotext Guide](https://github.com/piccolomo/plotext#guide)


# Utilities
- [Command Line Tool](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool)
- [Colorized Text](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#colorized-text)
- [File Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities)
- [Clear Functions](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#clear-functions)
- [Other Functions](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#other-functions)
- [Docstrings](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#docstrings)


## Command Line Tool

There are two ways one could use `plotext` directly on terminal. The first is by using the command line tool discussed in [Issue 47](https://github.com/piccolomo/plotext/issues/47) and [Pull 57](https://github.com/piccolomo/plotext/pull/57), [52](https://github.com/piccolomo/plotext/pull/52) and [51](https://github.com/piccolomo/plotext/pull/51), which will probably be further developed in the future. For further documentation run, on terminal:
```console
plotext --help
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
**Note 1**: each line has to terminate with a `;` and python strings, in any given line, should be surrounded by `'` instead of `"`. 

**Note 2**: each coded example in the [Plotext Guide](https://github.com/piccolomo/plotext#guide) is followed by the correspondent direct terminal command line (of the latter type).

[Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Colorized Text

To obtained colorized strings use the function `plt.colorize(string, fullground, background, show)` which paints a string with the given fullground and background [color and style codes](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#marker-colors). If `show = True` the string is directly printed and not returned. Here are a few examples:
```python
import plotext as plt

plt.colorize("black on white, bold", fullground = "black bold", background = "white", show = True)
plt.colorize("red on green, italic", fullground = "red italic", background = "green", show = True)
plt.colorize("yellow on blue, flash", fullground = "yellow flash", background = "blue", show = True)
plt.colorize("magenta on cyan, underlined", fullground = "magenta underline", background = "cyan", show = True)
plt.colorize("integer color codes", fullground = 201, background = 158, show = True)
plt.colorize("RGB color codes", fullground = (16, 100, 200), background = (200, 100, 100), show = True)
```
![colorize](https://raw.githubusercontent.com/piccolomo/plotext/master/images/colorize.png)
where using `flash` will result in an actual flashing character.

**Note**: to remove any coloring use the function `plt.uncolorize(string)`.


## File Utilities

`Plotext` has a container of tools, named `plt.file`, to easily manipulate files and file paths. Here is the list of its utilities:

- `plt.file.script_folder()` returns the folder containing the script used.

- `plt.file.parent_folder(path, level = 1)` returns the parent folder of the path provided at the level up specified.

- `plt.file.join_paths()` joins as many strings into a proper file path. Eg: `plt.file.join_paths("/", "home", "file.txt")` returns `/home/file.txt`. **Note**: if its first parameter is `~`, it will be interpreted as the user home folder.
 
- `plt.file.save_text(path, text)` saves some text to the `path` specified.

- `plt.file.read_data(path, delimiter, columns, header)` reads numerical data from the `path` specified, using the given delimiter between data columns (by default the space character), selecting the specified list of columns (`None` returns all of them by default); the parameter `header` is used to include or not the first data row.

- `plt.file.write_data(path, matrix, delimiter, columns)` write a matrix of data at `path` specified.

[Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Clear Functions

Here are all the available clear functions:

- `plt.clear_figure()` - in short `plt.clf()` - clears all internal definitions of the entire figure, including its subplots.

- `plt.colorless()` - in short `plt.cls()` - removes all colors from the entire figure, including its subplots.

- `plt.clear_plot()` - in short `plt.clp()` - clears all the internal definitions relative only to the active subplot. 

- `plt.clear_data()` - in short `plt.cld()` - clears only the data information relative to the active subplot, without clearing all the other plot settings.

- `plt.clear_color()` - in short `plt.clc()` - clears only the color settings relative to the active subplot, without clearing all other plot settings. The final rendering of this subplot will be colorless.

- `plt.clear_terminal()` - in short `plt.clt()` - clears the terminal screen and it is generally useful before plotting a continuous stream of data. It is recommended to use it before `plt.show()`. If its `lines` parameter is set to an integer (it is `None` by default), only the specified number of lines will be cleared. In this case, it is recommended to use it after `plt.show()`. Note that, depending on shell used, few extra lines may be printed after the plot.

- `plt.datetime.clear()` restores the internal definitions of the `datetime` container.

[Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Other Functions

- `plt.savefig(path)` saves the colourless version of the plot, as a text file, at the `path` specified. **If the path extension is `.html` the colours will be preserved.**

- `plt.build()` is equivalent to `plt.show()` except that the final figure canvas is returned as a string and not printed. 

- `plt.time()` returns the computation time of the latest `plt.show()` or `plt.build()` functions. 

- `plt.terminal_size()` returns the size of the terminal.

- `plt.sleep()` adds a sleeping time to the computation.

- `plt.sin(amplitude, periods, length, phase, decay)` outputs a sinusoidal signal with the given parameters.

- `version()` returns the version of the current installed `plotext` package.

[Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)


## Docstrings

All main `plotext` functions have a doc-string that can be accessed in three ways. For example the doc-string of the function `plt.scatter()` can be accessed:

- using `print(plt.scatter.__doc__)`

- more easily through the `doc` container: `plt.doc.scatter()`.

- with `plt.doc.all()` which prints all `plotext` doc-strings.

The functions `plt.markers()` and `plt.colors()` directly print useful information on how to use respectively [markers](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-markers) and [colors](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#marker-colors).

[Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)

[Plotext Guide](https://github.com/piccolomo/plotext#guide)
