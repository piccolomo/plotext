# Other Utilities

- [ Clear Functions ](https://github.com/piccolomo/plotext/blob/master/readme/other.md#clear-functions)
- [ File Utilities ](https://github.com/piccolomo/plotext/blob/master/readme/other.md#file-utilities)
- [ Command Line Tool ](https://github.com/piccolomo/plotext/blob/master/readme/other.md#command-line-tool)
- [ Other Functions ](https://github.com/piccolomo/plotext/blob/master/readme/other.md#other-functions)
- [ Docstrings ](https://github.com/piccolomo/plotext/blob/master/readme/other.md#docstrings)

[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)



## Clear Functions

Here are all the clear functions:

- `plt.clear_figure()` - in short `plt.clf()` clears all internal definitions of the final figure, including its subplots.

- `plt.colorless()` - in short `plt.cls()` - removes all colors from the entire figure, including its subplots.

- `plt.clear_plot()` - in short `plt.clp()` - clears all the internal definitions relative only to the active subplot. 

- `plt.clear_data()` - in short `plt.cld()` - clears only the data information relative to the active subplot, without clearing all the other plot settings.

- `plt.clear_color()` - in short `plt.clc()` - clears only the color settings relative to the active subplot, without clearing all other plot settings. The final rendering of this subplot will be colorless.

- `plt.clear_terminal()` - in short `plt.clt()` - clears the terminal screen and it is generally useful before plotting a continuous stream of data. It is recommended to use it before show(). If its parameter 'lines' is set to an integer (it is 'None' by default), only the specified lines will be cleared. In this case, it is recommended to use it after show(). Note that, the shell used may print extra lines, which need to be added to 'lines' in order for the clearing to have an effect. 

- `plt.datetime.clear()` restores the internal definitions of the `datetime` container.

[ Other Utilities Menu ](https://github.com/piccolomo/plotext/blob/master/readme/other.md#other-utilities)




## File Utilities

`Plotext` has a container of tools, called `plt.file`, to more easily manipulate files and file paths.

Here is the list of its utilities:

- `plt.parent_folder(path, level = 1)` returns the parent folder of the path at the level up specified.

- `plt.file.script_folder()` returns the folder containing the current script.

- `plt.file.join_paths()` it joins as many strings into a proper file path. If the first parameter is "~", it will be interpreted as the user home folder. Eg: `plt.file.join_paths("/", "home", "file.txt")` returns "/home/file.txt".
 
- `plt.file.save_text(path, text)` saves some text to the path selected.

- `plt.file.read_data(path, delimiter, columns, header)` reads numerical data from the 'path' selected with the given delimiter between columns (by default " "), and the selected list of columns (`None` returns all of them by default); the parameter header is used to include or not the first data row.

- `plt.file.write_data(path, matrix, delimiter, columns)` write a matrix of data in the 'path' selected.

[ Other Utilities Menu ](https://github.com/piccolomo/plotext/blob/master/readme/other.md#other-utilities)




## Command Line Tool

It is easy to transalte any `plotext` python code into a direct command line. Here is an example:
```
import plotext as plt

y = plt.sin() # sinusoidal signal 

plt.clp()
plt.scatter(y)
plt.title("Scatter Plot")
plt.show()
```

translates into this direct command line:
```
python3 -c "import plotext as plt; y=plt.sin(); plt.clp(); plt.scatter(y); plt.title('Scatter Plot'); plt.show();"
```

[ Other Utilities Menu ](https://github.com/piccolomo/plotext/blob/master/readme/other.md#other-utilities)




## Other Functions

- `plt.build()` is equivalent to `plt.show()` except that the final figure canvas is returned and not printed. 

- `plt.savefig(path)` saves the plot as a text file at the `path` provided. **If the path extension is `.html` the colors will be preserved.**

- `plt.terminal_size()` returns the size of the terminal.

- `plt.markers()` and `plt.colors()` print useful information on how to use markers and colors.

- `plt.sleep()` adds a sleeping time to the computation.

- `plt.sin(amplitude, periods, length, phase, decay) outputs a sinusoidal signal with the given parameters.

- `plt.colorize(string, full-ground, background, show)` it paints a string with the given color codes. If `show` is True, the string is printed and not returned.

- `plt.uncolorize(string)` removes all color codes from a string.

- `version()` returns the version of the current installed `plotext` package.

[ Other Utilities Menu ](https://github.com/piccolomo/plotext/blob/master/readme/other.md#other-utilities)



## Docstrings

All main `plotext` functions have a doc-string that can be accessed in three ways. For example for the function `plt.scatter()`:

- with `print(plt.scatter.__doc__)`

- more easily with the doc container: `plt.doc.scatter()`. Note that in the case of functions which are part of a container like `plt.datetime.string_to_timestamp()`, its  doc-string can be accessed with `plt.doc.string_to_timestamp()` (and not `plt.doc.datetime.string_to_timestamp()`)

- with `plt.doc.all()` which prints all `plotext` doc-strings.

[ Other Utilities Menu ](https://github.com/piccolomo/plotext/blob/master/readme/other.md#other-utilities)
