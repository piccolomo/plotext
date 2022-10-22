# Utilities

- [Clearing Functions](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#clearing-functions)
- [Canvas Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#canvas-utilities)
- [File Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities)
- [Testing Tools](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#testing-tools)
- [Command Line Tool](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool)
- [Colored Text](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#colored-text)
- [Docstrings](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#docstrings)

[Main Guide](https://github.com/piccolomo/plotext#guide)

## Clearing Functions

Here are all the available clearing functions:

- `clear_figure()`, in short `clf()`, clears **all internal definitions** of the subplot it refers to, including its subplots, if present; If it refers to the entire figure, it will clear everything.

- `clear_data()`, in short `cld()`, clears only the **data information** relative to the active subplot, without clearing all the other plot settings.

- `clear_color()`, in short `clc()`, clears only the **color settings** relative to the active subplot, without clearing all other plot settings. The final rendering of this subplot will be colorless. This function is equivalent to `theme('clear')`.

- `clear_terminal()`, in short `clt()`, clears the **terminal screen** and it is generally useful when plotting a continuous stream. If its `lines` parameter is set to an integer, only the specified number of lines will be cleared: note that, depending on shell used, few extra lines may be printed after the plot.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)

## Canvas Utilities

These functions are useful to save or change how the final result is outputted.

- `interactive(True)` allows to **plot dynamically** without needing to use the `show()` method. A new plot is shown when a change is made.

- `build()` is equivalent to `show()` except that the final **figure is returned as a string** and not printed.

- `save_fig(path)` **saves** the colorless version of **the plot**, as a text file, at the `path` specified:
  
  - if the path extension is `.html` the colors will be preserved,
  - if `append = True` (`False` by default), the final result will be appended to the file, instead of replacing it,
  - if `keep_colors = True` (`False` by default), the `txt` version will keep the ansi color codes and in Linux systems, the command `less -R path.txt` can be used to render the colored plot on terminal.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)

## File Utilities

`plotext` includes the following set of tools to easily manipulate files and file paths:

- `script_folder()` returns the folder containing the script where it is run.

- `parent_folder()` returns the parent folder of the `path` provided, at the `level` above specified.

- `join_paths()` joins as many strings into a proper file path. The `~` character will be interpreted as the user home folder. If no folder is provided, the home folder is considered by default.

- `save_text()` saves some `text` to the `path` specified.

- `read_data()` reads numerical data from the `path` specified, using the given `delimiter` between columns (by default the space character), selecting the specified list of `columns` (starting from 1) and including or not the first data row with the `header` parameter.

- `write_data()` write a matrix of data at the `path` specified, with given `delimiter` and considering the specified `columns`. 

- `transpose()` simply transposes a matrix.

- `download()` downloads the content from the given `url` to the `path` selected.

- `delete_file()` deletes the file at the `path` specified, if it exists.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)

## Testing Tools

Here are some tools useful to test the `plotext` package:

- `sin()` outputs a **sinusoidal signal** with the given `periods`, `length`, `amplitude`, `phase` and `decay` rate. More documentation is available using `doc.sin()`.

- `square()` outputs a **square wave signal** with the given n `periods`, `length` and `amplitude`. More documentation is available using `doc.square()`.

- `test()` to perform a **quick plotting test** (up to image rendering): it will download and finally remove a test image. 

- `time()` returns the **computation time** of the latest `show()` or `build()` function.

- A series of **test files** can be downloaded using the following url paths in conjunction with the `download()`method:
  
  - `test_data_url`  is the url of some 3 columns test data,
  - `test_bar_data_url` is the url of a simple 2 columns data used to test the `bar()` plot,
  - `test_image_url` is the url of a test image,
  - `test_gif_url` is the url of a test GIF image,
  - `test_video_url` is the url of a test video,
  - `test_youtube_url` is the url to a test YouTube video.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)

## Command Line Tool

There are two ways one could use `plotext` directly on terminal. The first is by using its dedicated command line tool, to print a simple scatter, line, bar or histogram plot, as well as for image plotting, GIFs, video and YouTube rendering.  For further documentation run, on terminal:

```console
plotext --help
```

![command-tool](https://raw.githubusercontent.com/piccolomo/plotext/master/data/command-tool.png)

The documentation of each function is also available. For example with:

```console
plotext scatter --help
```

![scatter-tool](https://raw.githubusercontent.com/piccolomo/plotext/master/data/scatter-tool.png)

- The  `--path` option is used to read from the specified path.

- The `--lines` option is used to plot a long data table at chunks of given `LINES` (1000 by default). 

- The tool recognizes the keyword `test` as path, to internally downloads and finally remove some test file. Here are some example: 
  
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

- you can type `python3 -m plotext` (or `python -m plotext` depending on your system) instead of `plotext` on your terminal, if the command tool is not directly available.

- to allow TAB completion, install `plotext` with flag `[completion]`, as explained [here](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#install). For issues on this feature, please report [here](https://github.com/piccolomo/plotext/pull/118). 

The second way to use `plotext` directly on terminal requires the translation of a script into a single string and passing it to the `python3 -c` tool. For example:

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

- Each `python` line has to terminate with a semi-colon `;` and not a new line.

- Strings should be surrounded by the single quote `'` , while the double quote `"` should be avoided.

Each coded example in this [guide](https://github.com/piccolomo/plotext#guide) is followed by the correspondent direct terminal command line (of the second type).

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)

## Colored Text

To obtained colored strings use the `colorize()` method, which paints a string with the given `fullground` color, `style`  and `background` color.  If `show = True` the string is directly printed and not returned. Here are a few examples:

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

- The available color codes are presented [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors), while the available styles [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#styles).

- Using the `flash` style will result in an actual flashing string.

- To remove any coloring use the `uncolorize()` method.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)

## Docstrings

All main `plotext` methods have a doc-string that can be accessed in three ways. For example the doc-string of the `scatter()` function can be accessed:

- using `print(scatter.__doc__)`,

- more easily through the `doc` container with `doc.scatter()`,

- with `doc.all()` which prints all `plotext` doc-strings.

Here are some methods that directly output some useful `plotext` guides:

- the `markers()` method displays the available **marker codes**, also discussed  [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#markers),

- the `colors()` method displays the available **color codes**, also discussed [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors),

- the `styles()` method displays the available **style codes**, also discussed [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#styles),

- the `theme()` method displays the available **themes**, also discussed [here](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#themes).

[Main Guide](https://github.com/piccolomo/plotext#guide), [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#utilities)
