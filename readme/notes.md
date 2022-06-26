# Notes
- [Plans](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#plans)
- [Updates](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#updates)
- [Credits](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#credits)
- [Similar Projects](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#similar-projects)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Plans
 - high resolution markers available on windows and other rarer terminals (under request and not sure how)
 - add bar alignment parameter (if requested)
 - matrix plot side bar to connect intensity level with actual value

[Main Guide](https://github.com/piccolomo/plotext#guide), [Project Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#project-notes)


## Updates
Note: there are many new features from previous version: any bug report is useful and very welcomed.

#### In version 5.1
For now only available in GitHub
- all `.md` files corrected and integrated
- test files are now available on line and not downloaded during installation, to make package lighter
- 4 x 2 `braille` markers now available, as requested in in [Issue 89](https://github.com/piccolomo/plotext/issues/89)
- changed `--file` flag in command line tool to `--path`
- added `--lines` flag  in command line tool to deal with big data
- added `--xcolumn` and `--ycolumns` flags to easily set the `x` and `y` data from the data table
- added `log` parameter to most of the [file functions](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities)
- solved [Issue 90](https://github.com/piccolomo/plotext/issues/90) to plot small axes numerical ticks in exponential form and in 'log' scale
- added `error()` function as requested in [Issue 91](https://github.com/piccolomo/plotext/issues/91)
- solved [Issue 94](https://github.com/piccolomo/plotext/issues/94) caused by consecutive calls to `show()` function with text plot



#### In version 5.0
- added `play_gif()`, `play_video()`, `play_youtube()`, `download()`, `get_youtube()` functions, to play GIFs and videos 
- rewritten command line tool
- added the backend function `from_matplotlib()`, as requested in [Issue 75](https://github.com/piccolomo/plotext/issues/75)
- added `candlestick()` plot function
- new logic behind the creation of a matrix of subplots, with nested sub-matrices allowed and settings on top level peculating on lower levels
- removed `span()` function
- added `take_min()` function
- re-written entire code 
- faster plotting from 2 (for long data) to 5 (for small data) times faster (on my machine)
- replaced `xaxis()` with `xaxes()` to set the presence of both axes at the same time, without the `xside` parameter; analogously for `yaxis()`
- added `ticks_style()` function 
- added `theme()` function
- removed `clear_plot()` function, `clear_figure()` takes its place depending on which level of the subplot matrix is applied
- removed `colorless()` function, `clear_color()` takes its place depending on which level of the subplot matrix is applied
- introduced `fast` parameter in `matrix_plot()` and `image_plot()` for faster plotting
- removed `size`, `keep_ratio` and `resample` parameters from `image_plot()`
- introduced `event_plot()` as inspired by [Issue 83](https://github.com/piccolomo/plotext/issues/83)
- added `text()` function to add string labels to the plot
- added `keep_colors` parameter in `save_fig()` to keep ansi color codes in `txt` files (file could be read with `less -R file_path.txt`)
- removed datetime class, all tools rewritten and moved to normal level
- introduced `input_form` and `output_form` for date/time string objects
- removed `plot_date()` and `scatter_date()` functions: date/time plots are now dealt freely by `plot()` and `scatter()`
- most of the plotting functions accept now date/time strings as well as coordinates
- removed file class, all tools moved to normal level
- introduced `test()` function
- new simpler string color codes
- `xside` and `yside` parameter could accept 1 and 2 as well for simplicity
- larger plots outside `ipython`, which prints an extra line or two

#### In version 4.3
- accounted for exponential float notation as requested in [Pull 82](https://github.com/piccolomo/plotext/pull/82) by `@soraxas`
- added functionality to properly read `numpy` data as requested in [Issue 84](https://github.com/piccolomo/plotext/issues/84) and [Issue 85](https://github.com/piccolomo/plotext/issues/85). 


#### In version 4.2
- added `norm` parameter in `hist()` function as requested in [Issue 76](https://github.com/piccolomo/plotext/issues/76) and pulled in [Pull 79](https://github.com/piccolomo/plotext/pull/79) by `@ZaydH`


#### In version 4.1
 - added `horizontal_line` and `vertical_line` functions, as requested in [Issue 65](https://github.com/piccolomo/plotext/issues/65)
 - the plotting functions now deal also with non numerical values (by not plotting them) as requested in [Issue 65](https://github.com/piccolomo/plotext/issues/65)
 - solved single bar plot error discussed in [Issue 63](https://github.com/piccolomo/plotext/issues/63)
 - added command line tool discussed in [Issue 47](https://github.com/piccolomo/plotext/issues/47) and [Pull 57](https://github.com/piccolomo/plotext/pull/57), [52](https://github.com/piccolomo/plotext/pull/52) and [51](https://github.com/piccolomo/plotext/pull/51)
 - set default marker to `hd` to avoid complications with `fhd` marker in some terminals [Issue 62](https://github.com/piccolomo/plotext/issues/62)
 - changed default canvas background color back to `bright-white` (feel free to express any other preference)
 - fixed bar error reported in [Issue 61](https://github.com/piccolomo/plotext/issues/61)
 - added guide for integration with package `rich`, as discussed in [Issue 26](https://github.com/piccolomo/plotext/issues/26)
 - added guide for integration with `tkinter`, as discussed in [Issue 33](https://github.com/piccolomo/plotext/issues/33)
 - added exception thrown when subplots size is bigger then default (see [Issue 60](https://github.com/piccolomo/plotext/issues/60))
 - `pillow` is now an optional dependency, as requested in [Issue 56](https://github.com/piccolomo/plotext/issues/56)
 - `numpy` is no longer a dependency (not even optional)
 - `platform` function changed, as recommended in [ Issue 55 ](https://github.com/piccolomo/plotext/issues/55)
 - `shell` function and parameter removed as found to be useless
 - all `.md` files corrected and integrated

#### In version 4.0
  - entire code re-written
  - faster plotting
  - 2 x 2 marker is now called `hd` (as for *high resolution*) instead of `small`
  - added higher resolution 3 x 2 unicode mosaics markers (not available in Windows), called `fhd` (as for *full high resolution*)
  - added new color codes, which include 256 color codes and full RGB colors
  - added multiple and stacked bar charts
  - added datetime scatter and plot functions
  - added datetime class to better handle most datetime objects
  - added `plt.matrix_plot()` function
  - added `plt.image_plot()` to plot images
  - plots now can also be saved in color using `.html` extension
  - added file class to better handle files and file paths
  - data can now also be plotted on the upper x axis
  - added `unittest` file, called `test.py`
  - `xside` and `yside` parameters introduced for many related functions
  - `span()` function added to span columns and rows in the matrix of subplots
  - added more `clear` functions
  - added function `limit_size()` to limit or not the plot dimensions to the terminal size
  - bar chart log scale issue solved on both axes
  - bar chart 0 value issue solved
  - added optional legend extra characters to identify on which axes each data is plotted
  - `time()` function added to check plotting computational time
  - `xfreq()` is now `xfrequency()`, `yfreq()` is `yfrequency()`
  - added doc class to easily access all functions doc-strings 
  - `get_canvas()` is now `build()`
  - `plt.frame()` function reinstated

#### In version 3.1
  - fixed [Issue 23](https://github.com/piccolomo/plotext/issues/23) on plot resizing 
  - added `plt.clear_data()` and `plt.test()` functions

#### In version 3.0
  - direct terminal command line tool added (of first type)  
  - added marker "small" (with improved resolution), and new marker codes  
  - added matrix of subplots  
  - added log plots  
  - stem plot added  
  - added double `y` axes plot
  - added bar plot  
  - added date/time plot  
  - added function `plt.get_canvas()`  
  - added function `plt.sin()`  
  - added `plt.clear_figure()`  
  - `plt.figsize()` changed to `plt.plotsize()`  
  - `plt.nocolor()` changed to `plt.colorless()`  
  - `plt.frame()` function removed and replaced with `plt.xaxes()` and `plt.yaxes()`
  - re-written most of the code 

#### In version 2.3
  - solved histogram error reported on [Issue 15](https://github.com/piccolomo/plotext/issues/15)  
  - added histogram plot
  - added `fillx` and `filly` parameters  

#### In version 2.2
  - new `readme.md` description file, 
  - changed `plt.fig_size()` to `plt.figsize()`
  - changed `plt.facecolor()` to `plt.axes_color()`
  - slightly modified the behaviour under Windows  
  - new markers that are Windows friendly (when the plot is saved, they occupy one character)
  - the plots are printed with a default color combination, instead of being colorless by default  
  - removed the `force_size` parameter  
  - added the `plt.grid()` function to add optional grid lines. 
  - added the `plt.frame()` function to add a frame (present by default)  
  - the only parameters available in the `plot` and `scatter` function are now only those which are dependent on the data set (like `point_marker`, `point_color`, `fill` etc..), all others can be set before the `plt.show()` function with dedicated functions (like `plt.ticks()`, `plt.title()` etc.. )
  - changed `plt.canvas_size()` to `plt-fig_size()` to avoid confusion
  - added `plt.nocolor()` function
  - improved the algorithm for getting the lines between consecutive points and the filling point (when using `fill = True`)
  - added `plt.clp()` and `plt.clt()` functions, short versions for `plt.clear_plot()` and `plt.clear_terminal()` respectively.
  - color codes updated
  - added function `plt.parameters()`
  - added function `docstrings()`

#### In version 2.1
 - the plot now shows the actual data ticks using a simpler algorithm  
 - changed `ticks_number` to `ticks`  
 - changed set functions like plt.set_title() to `plt.title()`  
 - an optional grid can now be added  
 - added `fill` parameter  
 - changed `plt.axes_color()` to `plt.facecolor()` to adapt to `matplotlib`  
 - new legend positioning  
 - new color codes  
 - code restructured and revised

#### In version 2.0
 - the plot now shows the actual data ticks, which was more complicated then expected as the ticks should adapt to a limited amount of characters available (ticks_length)  
 - added `plt.set_xticks()` and `plt.set_yticks()` functions 
 - labels can be added to the axes  
 - a title can be added to the plot  
 - a legend can be shown when plotting multiple data sets  
 - set functions involving a list of two parameters can be used in two different ways. For example `plt.set_xlim([xmin, xmax])` is equivalent to `plt.set_xlim(xmin, xmax)`  
 - removed `point` and `line` parameters 
 - removed `background` parameter: `canvas_color` takes his place  
 - `axes_color` could now also be a list of two colors where the second sets the axes background color
 - changed `spacing` parameter to `ticks_number`  
 - `equations` parameter removed as the equations will be printed automatically if needed  
 - `decimals` parameter removed  
 - code restructured and revised


#### In version 1.0
  - `plotext` now works also in Windows with colors
  - `plotext` now works also using Python IDLE3 but with no colors and no adaptive dimensions
  - new color codes with background codes added
  - added `force_size` parameter
  - adeed the function `plt.savefig()`
  - added the function `plt.get_version()`
  - added the function `plt.run_test()`
  - no need for `numpy` or `time` packages
  - the code has been updated and it is more legible
  - the documentation has been updated
  - `equations` parameter now is set by default to `False`
  - when `thick` is `False`, the axes non numerical ticks are also removed
  - removed `get` functions for plot parameters

[Main Guide](https://github.com/piccolomo/plotext#guide), [Project Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#project-notes)



## Credits
 - `@PhilipVinc` for `error()` plot idea, requested in [Issue 91](https://github.com/piccolomo/plotext/issues/91)
 - `@Neo-Oli` for requesting braille based markers in [Issue 89](https://github.com/piccolomo/plotext/issues/89)
 - `@MartinThoma` for inspiring the idea behind `event_plot()` in [Issue 83](https://github.com/piccolomo/plotext/issues/83)
 - `@soraxas` for functionality that accounts for exponential float notation: [Pull 82](https://github.com/piccolomo/plotext/pull/82)
 - `@wookayin` for requesting the backend function `from_matplotlib()` in [Issue 75](https://github.com/piccolomo/plotext/issues/75)
 - `@NLKNguyen` for ideas inspiring the `horizontal_line` and `vertical_line` functions: [Issue 65](https://github.com/piccolomo/plotext/issues/65)
 - `@asartori86` for the awesome command line tool: [Issue 47](https://github.com/piccolomo/plotext/issues/47)
 - `@jtplaarj` for the great ideas and codes regarding multiple and stacked bar plots: [Issue 48](https://github.com/piccolomo/plotext/issues/48)
 - `@ethack` for  requesting log scale on bar plot: [Issue 37](https://github.com/piccolomo/plotext/issues/37)
 - `@ethack` for  solving single bar error: [Pull 43](https://github.com/piccolomo/plotext/issues/43)
 - `@gregwa1953` for  inspiring `plt.limit_size()`: [Issue 33](https://github.com/piccolomo/plotext/issues/33)
 - `@rbanffy` for suggestion of using 3 x 2 unicode mosaic box characters: [Issue 29](https://github.com/piccolomo/plotext/issues/29).
 - `@henryiii` for unittest suggestion: [Issue 32](https://github.com/piccolomo/plotext/issues/32)
 - `@whisller` and `@willmcgugan` for integration with `Rich` package: [Issue 26](https://github.com/piccolomo/plotext/issues/26)
 - `@garid3000` for the idea of a function that returns the plot canvas: [Issue 20](https://github.com/piccolomo/plotext/issues/20)
 - `@robintw` and `@Sauci` for horizontal bar plot idea and code, respectively: [Issue 16](https://github.com/piccolomo/plotext/issues/16)
 - `@Zaneo` for multiple data set idea: [Issue 13](https://github.com/piccolomo/plotext/issues/13)
 - `@Zaneo` for double axes idea: [Issue 12](https://github.com/piccolomo/plotext/issues/12)
 - users `@geoffrey-eisenbarth` and  `@matthewhanson` for requesting datetime support: [Issue 7](https://github.com/piccolomo/plotext/issues/7)
 - `@kris927b` for requesting histogram plot: [Issue 6](https://github.com/piccolomo/plotext/issues/6)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Project Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#project-notes)

## Similar Projects
These count, as well, as source of inspiration:
- [plotille](https://github.com/tammoippen/plotille)
- [termplot](https://github.com/justnoise/termplot)
- [termgraph](https://github.com/sgeisler/termgraph)
- [terminalplot](https://github.com/kressi/terminalplot)
- [asciichart](https://github.com/cashlo/asciichart)
- [uniplot](https://github.com/olavolav/uniplot)
- [bashplotlib](https://github.com/glamp/bashplotlib)
- [termplotlib](https://github.com/nschloe/termplotlib)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Project Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#project-notes)
