# Notes

- [Install](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#install)
- [Future Ideas](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#future-ideas)
- [Updates](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#updates)
- [Credits](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#credits)
- [Similar Projects](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#similar-projects)


[Main Guide](https://github.com/piccolomo/plotext#guide)

## Install

Here are the terminal commands to install `plotext` on your machine:

- `pip install plotext` for normal installation and  `pip install plotext --upgrade` to upgrade to the latest [PyPi version](https://pypi.org/project/plotext).

- `pip install "plotext[image]"` to install the optional dependency necessary for **image plotting** (including GIFs).

- `pip install "plotext[video]"` to install the optional dependencies necessary for **video rendering**, which will also allow to plot images.

- `pip install "plotext[completion]"` to allow TAB completion in the [command line tool](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool).

- The optional packages are `pillow` (for image plotting), `opencv-python` (for video rendering), `ffpyplayer` (to stream audio), `pafy` and `youtube-dl` (to stream YouTube), `shtab` (for TAB completion).

- `pip install git+https://github.com/piccolomo/plotext`, to install the [GitHub version](https://github.com/piccolomo/plotext), if more updated and you feel courageous:
  
  - `pip install "plotext[image] @ git+https://github.com/piccolomo/plotext.git"` to include image plotting dependencies,
  - `pip install "plotext[video] @ git+https://github.com/piccolomo/plotext.git"` to include video plotting dependencies,
  - `pip install "plotext[completion] @ git+https://github.com/piccolomo/plotext.git"` to include the TAB completion dependency,

- Use the `test()` method to quickly test (up to image rendering) your newly installed version of `plotext`. This function will download and finally remove a [test image](https://raw.githubusercontent.com/piccolomo/plotext/master/data/cat.jpg) into your home folder. 

- Any relevant [Issue Report](https://github.com/piccolomo/plotext/issues) or [Pull request](https://github.com/piccolomo/plotext/pulls) is very welcomed. 

- The `plotext` package has been **created and tested** using Ubuntu 22.04 and Python 3.10.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#notes)

## Future Ideas
Any new relevant idea is welcomed, opening an [issue report](https://github.com/piccolomo/plotext/issues/new), or any help with the following ideas with a new [pull requst](https://github.com/piccolomo/plotext/compare):


### Bug Fixes
- solve issue with `clear_color()` method not working properly, as presented in [Issue 156](https://github.com/piccolomo/plotext/issues/156)
- solve simple stacked and multiple bar plot not working with single data set, as presented in issue [Issue 155](https://github.com/piccolomo/plotext/issues/155) about
- solve chinese text bug, as presented in [Issue 158](https://github.com/piccolomo/plotext/issues/158)
- `frame()` methods changes behaviors if called before `subplots()`; eg: `import plotext as plt; plt.clf(); plt.subplots(2,2);plt.subplot(1,2); plt.frame(0); plt.subplots(2,2); plt.show();` versus `import plotext as plt; plt.clf(); plt.frame(0); plt.subplots(2,2); plt.show();`
- solve issue with `labels` parameter in `confusion_matrix()` (for non boolean data) which doesn't seem to work properly
- solve weekends time gap issue in datetime plots, as presented in [Issue 148](https://github.com/piccolomo/plotext/issues/148)


### New Features
- add custom lines, as requested in issue [Issue 145](https://github.com/piccolomo/plotext/issues/145)
- support datetime integration, as requested in issue [Issue 154](https://github.com/piccolomo/plotext/issues/154)
- add command line arguments to set plot limits, as requested in issue [Issue 173](https://github.com/piccolomo/plotext/issues/173)
- allow plot and scatter to start from 0 and not 1 (optionally), as requested in issue [Issue 176](https://github.com/piccolomo/plotext/issues/176)
- add heatmap plot, as requested in issue [Issue 143](https://github.com/piccolomo/plotext/issues/143)
- add OHLC date time plot, as requested in issue [Issue 149](https://github.com/piccolomo/plotext/issues/149)
- add network graphs, as requested in issue [Issue 160](https://github.com/piccolomo/plotext/issues/160)
- integrate `colorize()` in `text()` and `indicator()` or or any string `label` parameter, as requested in issue [Issue 144](https://github.com/piccolomo/plotext/issues/144); possible idea: `colorize()` to output a `matrix_class()` object
- allow simple bar plots in matrix of subplots, as requested in issue [Issue 171](https://github.com/piccolomo/plotext/issues/171); this could be possibly extended to allow images also, rendered with fast parameter set to `True`
- allow user to decide plot legend position and frame
- allow clickable plots, as requested in issue [Issue 175](https://github.com/piccolomo/plotext/issues/175); this sounds hard!
- add text table feature, with nice formatting (?)


### New Functions
- add `bold()` function
- add `plotter()` function, to scatter and plot at the same time
- add `clear_settings()` method to clear only the plot settings (labels, title and so on) and not the data, or colors
- add `simple_hist()` function, analogous to `simple_bar()`


### General Improvements
- add all-caps style
- add log parameter to `save_fig()` and similar
- no float in axes labels if ticks are all integers
- catch errors in video reproduction and get youtube
- in read data, default folder should be script folder
- allow simple bar plots to handle negative values
- allow `limit_size()` to be used also after `plot_size()`
- add bar `alignment` and `style` parameter
- add matrix plot side bar, to connect intensity level with actual matrix value
- high resolution markers available on Windows and other rarer terminals (under request and not sure how)
- add method to optionally set the sizes of a matrix of subplots giving priority to the subplots closer to bottom right edge, instead of upper left ones (as by default)
- convert the class `matrix_class()`, the engine running the plots, in C++ and connect it to the Python code (not sure how and would appreciate some help regarding this)


### Internal Conventions
- change candlestick data name conventions, as requested in [Issue 148](https://github.com/piccolomo/plotext/issues/148)
- add parameter on bar plot methods for custom texts above bars, as proposed in [Pull Request 164](https://github.com/piccolomo/plotext/pull/164)
- unify name for `color` and `colors` parameters in `candlestick()`, `multiple_bar()` etc ...
- change `coordinate` parameter to `x` and `y` in `hline()` and `vline()`
- change `trings_to_time()` to `strings_to_times()`
- decide general convention for method aliases
- change `frame` parameter to `show` in `frame()` method

### Documentation and Testing
- add docstring for `string_to_time()` and `strings_to_times()`
- add unit testing, as suggested in [Issue 130](https://github.com/piccolomo/plotext/issues/130)
- extend command line tool so that `man plotext` and `whatis plotext` are allowed


[Main Guide](https://github.com/piccolomo/plotext#guide), [Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#notes)

## Updates

#### In version 5.3

Available on [GitHub](https://github.com/piccolomo/plotext) only:

- all docstrings updated
- the colored doctrings of all methods can now be easily printed using a dedicated `.doc()` internal method; eg: `plotext.scatter.doc()` will print the colorized docstring of the `scatter()` function.
- renamed `text` parameter to `label` in `text()` method 
- renamed `label` parameter to `labels` in `multiple_bar()` and `stacked_bar()` functions 
- renamed `fullground` parameter to `color` in `colorize()` method
- renamed `datetimes_to_string()` method to `datetimes_to_strings()`
- removed `trend` parameter from `indicator()` function
- added `log` and `header` parameters to `read_data()` method
- changed text default allignment to `'center'` in `text()` method
- added boxplot as requested in [Issue 169](https://github.com/piccolomo/plotext/issues/169) and proposed in [Pull Request 170](https://github.com/piccolomo/plotext/pull/170)


#### In version 5.2


In version 5.2.8 (published on [PyPi](https://pypi.org/project/plotext)):

- solved issue [Issue 153](https://github.com/piccolomo/plotext/issues/153) allowing bar plots to handle 0 data sets
- added `xside` and `yside` parameters to `candlestick()` function, solving [Issue 152](https://github.com/piccolomo/plotext/issues/152)
- solved issue [Issue 151](https://github.com/piccolomo/plotext/issues/151) due to wrong inheritance of nested subplots from parent figure
- solved issue [Issue 150](https://github.com/piccolomo/plotext/issues/150) due to maximum number of subplots reached
- solved issue [Issue 142](https://github.com/piccolomo/plotext/issues/142) by removing side symbol (like ⅃) in legend for single data set
- added date time support for `xlim()` and `ylim()` methods, solving [Issue 138](https://github.com/piccolomo/plotext/issues/138)
- removed decimals points if axes ticks are all integers, solving [Issue 136](https://github.com/piccolomo/plotext/issues/136)
- added `marker` parameter to the `from_matplotlib()` method, solving [Issue 134](https://github.com/piccolomo/plotext/issues/134)
- made `from_matplotlib()` method compatible with `matplotlib 3.6`, solving [Issue 133](https://github.com/piccolomo/plotext/issues/133)

<!--- Published on [PyPi](https://pypi.org/project/plotext): --->

In previous versions:

- fixed legend symbol for braille markers, merging [Pull Request 135](https://github.com/piccolomo/plotext/pull/135)
- allowed compatibility with Python 3.7, solving [Issue 130](https://github.com/piccolomo/plotext/issues/130)
- allowed new line `'\n'` in `text()` to properly plot, solving [Issue 127](https://github.com/piccolomo/plotext/issues/127)
- allowed TAB completion in command line tool retrieving [Pull Request 126](https://github.com/piccolomo/plotext/pull/126)
- solved `xlim()` and `ylim()` wrong definition, solving [Issue 112](https://github.com/piccolomo/plotext/issues/112) and [Issue 123](https://github.com/piccolomo/plotext/issues/123)
- added `indicator()` function as requested in [Issue 121](https://github.com/piccolomo/plotext/issues/121)
- added `shtab` optional dependency as introduced in [Pull Request 118](https://github.com/piccolomo/plotext/pull/118)
- integrated changes in [Pull Request 107](https://github.com/piccolomo/plotext/pull/107) related to allowing `plotext` with `python` with `-m` flag 
- added `interactive()` function as requested in [Issue 115](https://github.com/piccolomo/plotext/issues/115)
- improved way to handle `Nan` and `None` values in the data as requested in [Issue 114](https://github.com/piccolomo/plotext/issues/114)
- added `confusion_matrix()` function, as requested in [Issue 113](https://github.com/piccolomo/plotext/issues/113)
- added `append` parameter to the `save_fig()` function as requested in [Issue 109](https://github.com/piccolomo/plotext/issues/109)
- added `square()` function as requested in [Issue 108](https://github.com/piccolomo/plotext/issues/108)
- added `simple_bar()`, `simple_multiple_bar()` and `simple_stacked_bar()` functions as requested in [Issue 98](https://github.com/piccolomo/plotext/issues/98)
- added `xreverse()` and `yreverse()` functions are requested in [Issue 86](https://github.com/piccolomo/plotext/issues/86)
- added `polygon()` and `rectangle()` function
- simplified bar ticks creation and added `reset_ticks` parameter, to optionally disable default ticks creation
- no memory of past plotted bars in bar functions
- bars can now have negative values
- `fillx` and `filly` can now accept `True` and `False` as usual, but also a numerical value (to fill till that value) and `"internal"` (to fill till another data point is reached)
- added `background` color in `text()` function
- removed `version()` function, now simply `version` value
- code reorganized:
  - introduced `_global.py` and `_matrix.py` files 
  - changed `_utility` folder to a file
  - introduced `_dict.py` file containing long dictionaries related to markers, color, styles and themes
  - introduced `_build.py` to separately deals with the long `build_plot()` function

#### In version 5.1

This version is only available on [GitHub](https://github.com/piccolomo/plotext/tree/b080e231cb5dbe005cdd6d54f6ee0cbf5e893aaa).

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
- changed default bar marker to `hd` to solve [Issue 96](https://github.com/piccolomo/plotext/issues/96)

#### In version 5.0

- added `play_gif()`, `play_video()`, `play_youtube()`, `download()`, `get_youtube()` functions, to play GIFs and videos 
- rewritten command line tool
- added the back-end function `from_matplotlib()`, as requested in [Issue 75](https://github.com/piccolomo/plotext/issues/75)
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
- removed date-time class, all tools rewritten and moved to normal level
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
- added higher resolution 3 x 2 Unicode mosaics markers (not available in Windows), called `fhd` (as for *full high resolution*)
- added new color codes, which include 256 color codes and full RGB colors
- added multiple and stacked bar charts
- added date-time scatter and plot functions
- added date-time class to better handle most date-time objects
- added `matrix_plot()` function
- added `image_plot()` to plot images
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
- `frame()` function reinstated

#### In version 3.1

- fixed [Issue 23](https://github.com/piccolomo/plotext/issues/23) on plot resizing 
- added `clear_data()` and `test()` functions

#### In version 3.0

- direct terminal command line tool added (of first type)  
- added marker `"small"` (with improved resolution), and new marker codes  
- added matrix of subplots  
- added log plots  
- stem plot added  
- added double `y` axes plot
- added bar plot  
- added date/time plot  
- added function `get_canvas()`  
- added function `sin()`  
- added `clear_figure()`  
- `figsize()` changed to `plotsize()`  
- `nocolor()` changed to `colorless()`  
- `frame()` function removed and replaced with `xaxes()` and `yaxes()`
- re-written most of the code 

#### In version 2.3

- solved histogram error reported on [Issue 15](https://github.com/piccolomo/plotext/issues/15)  
- added histogram plot
- added `fillx` and `filly` parameters  

#### In version 2.2

- new `readme.md` description file, 
- changed `fig_size()` to `figsize()`
- changed `facecolor()` to `axes_color()`
- slightly modified the behavior under Windows  
- new markers that are Windows friendly (when the plot is saved, they occupy one character)
- the plots are printed with a default color combination, instead of being colorless by default  
- removed the `force_size` parameter  
- added the `grid()` function to add optional grid lines. 
- added the `frame()` function to add a frame (present by default)  
- the only parameters available in the `plot` and `scatter` function are now only those which are dependent on the data set (like `point_marker`, `point_color`, `fill` etc..), all others can be set before the `show()` function with dedicated functions (like `ticks()`, `title()` etc.. )
- changed `canvas_size()` to `fig_size()` to avoid confusion
- added `nocolor()` function
- improved the algorithm for getting the lines between consecutive points and the filling point (when using `fill = True`)
- added `clp()` and `clt()` functions, short versions for `clear_plot()` and `clear_terminal()` respectively.
- color codes updated
- added function `parameters()`
- added function `docstrings()`

#### In version 2.1

- the plot now shows the actual data ticks using a simpler algorithm  
- changed `ticks_number` to `ticks`  
- changed set functions like `set_title()` to `title()`  
- an optional grid can now be added  
- added `fill` parameter  
- changed `axes_color()` to `facecolor()` to adapt to `matplotlib`  
- new legend positioning  
- new color codes  
- code restructured and revised

#### In version 2.0

- the plot now shows the actual data ticks, which was more complicated then expected as the ticks should adapt to a limited amount of characters available
- added `set_xticks()` and `set_yticks()` functions 
- labels can be added to the axes  
- a title can be added to the plot  
- a legend can be shown when plotting multiple data sets  
- set functions involving a list of two parameters can be used in two different ways. For example `set_xlim([xmin, xmax])` is equivalent to `set_xlim(xmin, xmax)`  
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
- added the function `savefig()`
- added the function `get_version()`
- added the function `run_test()`
- no need for `numpy` or `time` packages
- the code has been updated and it is more legible
- the documentation has been updated
- `equations` parameter now is set by default to `False`
- when `thick` is `False`, the axes non numerical ticks are also removed
- removed `get` functions for plot parameters

[Main Guide](https://github.com/piccolomo/plotext#guide), [Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#notes)

## Credits

From [Pull requests](https://github.com/piccolomo/plotext/pulls):

- `@cwaldbieser` for the `first_row` parameter idea in the `read_data()` method in [Pull Request 166](https://github.com/piccolomo/plotext/pull/166)
- `@luator` for fixing legend symbol for braille markers in [Pull Request 135](https://github.com/piccolomo/plotext/pull/135)
- `@luator` for fixing legend symbol for braille markers in [Pull Request 135](https://github.com/piccolomo/plotext/pull/135)
- `@Freed-Wu` for introducing TAB completions to the command line tool in [Pull Request 118](https://github.com/piccolomo/plotext/pull/118) 
- `@pankajp` for allowing `plotext` to be used with `python3` with `-m` flag in [Pull Request 107](https://github.com/piccolomo/plotext/pull/107)
- `@soraxas` for functionality that accounts for exponential float notation: [Pull 82](https://github.com/piccolomo/plotext/pull/82)

From [Issue Reports](https://github.com/piccolomo/plotext/issues):

- `@luator` for requesting `marker` parameter in the `from_matplotlib()` method in [Issue 134](https://github.com/piccolomo/plotext/issues/134)
- `@darul75` for requesting multiple lines in `text()` in [Issue 127](https://github.com/piccolomo/plotext/issues/127)
- `@PhilipVinc` for `error()` plot idea, requested in [Issue 122](https://github.com/piccolomo/plotext/issues/122)
- `@darul75` for requesting a simple KPI indicator  in [Issue 121](https://github.com/piccolomo/plotext/issues/121)
- `@Freed-Wu` for requesting interactive mode in [Issue 115](https://github.com/piccolomo/plotext/issues/115)
- `@Freed-Wu` for requesting a better way to deal with `Nan` and `None` values in [Issue 114](https://github.com/piccolomo/plotext/issues/114)
- `@3h4` for requesting confusion matrix in [Issue 113](https://github.com/piccolomo/plotext/issues/113)
- `@dns13` for requesting `append` option in save_fig() function in [Issue 109](https://github.com/piccolomo/plotext/issues/109)
- `@vps-eric` for requesting square waves in [Issue 108](https://github.com/piccolomo/plotext/issues/108)
- `@newbiemate` for requesting simple bar functionality in [Issue 98](https://github.com/piccolomo/plotext/issues/98)
- `@Neo-Oli` for requesting braille based markers in [Issue 89](https://github.com/piccolomo/plotext/issues/89)
- `@pieterbergmans` for requesting reverse axes functionality in [Issue 86](https://github.com/piccolomo/plotext/issues/86)
- `@MartinThoma` for inspiring the idea behind `event_plot()` in [Issue 83](https://github.com/piccolomo/plotext/issues/83)
- `@wookayin` for requesting the back-end function `from_matplotlib()` in [Issue 75](https://github.com/piccolomo/plotext/issues/75)
- `@NLKNguyen` for ideas inspiring the `horizontal_line` and `vertical_line` functions: [Issue 65](https://github.com/piccolomo/plotext/issues/65)
- `@jtplaarj` for the great ideas and codes regarding multiple and stacked bar plots: [Issue 48](https://github.com/piccolomo/plotext/issues/48)
- `@asartori86` for the awesome command line tool: [Issue 47](https://github.com/piccolomo/plotext/issues/47)
- `@ethack` for  solving single bar error: [Pull 43](https://github.com/piccolomo/plotext/issues/43)
- `@ethack` for  requesting log scale on bar plot: [Issue 37](https://github.com/piccolomo/plotext/issues/37)
- `@gregwa1953` for  inspiring `limit_size()`: [Issue 33](https://github.com/piccolomo/plotext/issues/33)
- `@rbanffy` for suggestion of using 3 x 2 unicode mosaic box characters: [Issue 29](https://github.com/piccolomo/plotext/issues/29).
- `@henryiii` for unit-test suggestion: [Issue 32](https://github.com/piccolomo/plotext/issues/32)
- `@whisller` and `@willmcgugan` for integration with `Rich` package: [Issue 26](https://github.com/piccolomo/plotext/issues/26)
- `@garid3000` for the idea of a function that returns the plot canvas: [Issue 20](https://github.com/piccolomo/plotext/issues/20)
- `@robintw` and `@Sauci` for horizontal bar plot idea and code, respectively: [Issue 16](https://github.com/piccolomo/plotext/issues/16)
- `@Zaneo` for multiple data set idea: [Issue 13](https://github.com/piccolomo/plotext/issues/13)
- `@Zaneo` for double axes idea: [Issue 12](https://github.com/piccolomo/plotext/issues/12)
- users `@geoffrey-eisenbarth` and  `@matthewhanson` for requesting datetime support: [Issue 7](https://github.com/piccolomo/plotext/issues/7)
- `@kris927b` for requesting histogram - [Some Questions](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#some-questions)plot: [Issue 6](https://github.com/piccolomo/plotext/issues/6)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#notes)

## Similar Projects

These count as well as source of inspiration:

- [plotille](https://github.com/tammoippen/plotille)
- [termplot](https://github.com/justnoise/termplot)
- [termgraph](https://github.com/sgeisler/termgraph)
- [terminalplot](https://github.com/kressi/terminalplot)
- [asciichart](https://github.com/cashlo/asciichart)
- [uniplot](https://github.com/olavolav/uniplot)
- [bashplotlib](https://github.com/glamp/bashplotlib)
- [termplotlib](https://github.com/nschloe/termplotlib)
- [termgraph](https://github.com/mkaz/termgraph)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#notes)
