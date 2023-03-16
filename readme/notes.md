# Notes

- [Install](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#install)
- [Future Ideas](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#future-ideas)
- [Updates](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#updates)
- [Credits](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#credits)
- [Similar Projects](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#similar-projects)
- [Some Questions](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#some-questions)


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

From [Issue Reports](https://github.com/piccolomo/plotext/issues): 

- add OHLC date-time plots, solving [Issue 149](https://github.com/piccolomo/plotext/issues/148)
- add custom lines (dotted, or any marker), solving [Issue 145](https://github.com/piccolomo/plotext/issues/145)
- add heatmap plot, solving [Issue 143](https://github.com/piccolomo/plotext/issues/143)
- add unit testing, as suggested in [Issue 130](https://github.com/piccolomo/plotext/issues/130)

Any new relevant idea is welcomed under request, opening an [issue report](https://github.com/piccolomo/plotext/issues/new), here are some:

- add bar `alignment` parameter
- add `clear_settings()` method to clear only the plot settings (labels, title and so on) and not the data and colors
- add `matrix_plot()` side bar to connect intensity level with actual matrix value
- high resolution markers available on Windows and other rarer terminals (under request and not sure how)
- correct doc strings
- add direct parameters doc strings in the `doc` container
- remove `trend` parameter in `text()` method
- change `text` parameter to `label`  in `text()`
- change `frame` parameter to `show` in `frame()` method
- add `plotter()` function, to scatter and plot at the same time
- add `simple_hist()` function, just like `simple_bar()`
- change `colorize()` to output a `matrix_class()` object such that it can be inserted in `text()`, `indicator()` or any `label` parameter and any two objects can be easily summed as strings would. 
- allow simple plots and fast image rendering to fit in subplots 
- add matrix plot side bar 
- make simple bar plots handle negative values
- allow user to decide plot legend position and frame

[Main Guide](https://github.com/piccolomo/plotext#guide), [Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#notes)

## Updates

#### In version 5.2

<!--- Available on [GitHub](https://github.com/piccolomo/plotext) only:--->

In version 5.2.8:

- solved issue [Issue 153](https://github.com/piccolomo/plotext/issues/153) allowing bar plots to handle 0 data sets
- solved issue [Issue 151](https://github.com/piccolomo/plotext/issues/151) due to wrong inheritance of nested subplots from parent figure
- solved issue [Issue 150](https://github.com/piccolomo/plotext/issues/150) due to maximum number of subplots reached
- solved issue [Issue 142](https://github.com/piccolomo/plotext/issues/142) by removing side symbol (like ⅃) in legend for single data set
- added `xside` and `yside` parameters to `candlestick()` function, solving another bug in [Issue 138](https://github.com/piccolomo/plotext/issues/138)
- removed decimals points if axes ticks are all integers, solving [Issue 136](https://github.com/piccolomo/plotext/issues/136)
- added `marker` parameter to the `from_matplotlib()` method, solving [Issue 134](https://github.com/piccolomo/plotext/issues/134)
- made `from_matplotlib()` method to be compatible with `matplotlib 3.6`, solving [Issue 133](https://github.com/piccolomo/plotext/issues/133)
- added date time support for `xlim()` and `ylim()` methods, solving [Issue 138](https://github.com/piccolomo/plotext/issues/138)

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

- `@luator` for fixing legend symbol for braille markers in [Pull Request 135](https://github.com/piccolomo/plotext/pull/135)
- `@Freed-Wu` for introducing TAB completions to the command line tool in [Pull Request 118](https://github.com/piccolomo/plotext/pull/118) 
- `@pankajp` for allowing `plotext` to be used with `python3` with `-m` flag in [Pull Request 107](https://github.com/piccolomo/plotext/pull/107)
- `@soraxas` for functionality that accounts for exponential float notation: [Pull 82](https://github.com/piccolomo/plotext/pull/82)

From [Issue Reports](https://github.com/piccolomo/plotext/issues):

- `@luator` for requesting `marker` parameter in the `from_matplotlib()` method in [Issue 134](https://github.com/piccolomo/plotext/issues/134)
- `@darul75` for requesting multiple lines in [Issue 127](https://github.com/piccolomo/plotext/issues/127)
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
- `@kris927b` for requesting histogram plot: [Issue 6](https://github.com/piccolomo/plotext/issues/6)

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

## Some Questions

- Is [Consciousness](https://www.youtube.com/watch?v=Bim73icRzCk) and [Love](https://www.youtube.com/watch?v=GHzAfj-62Uc) the unified truth of life, transcendent of space, time and death?
- is there a [global cabal](https://www.youtube.com/watch?v=ZSqBNGxLiAs&list=PLnzMmEt4pIb83lZgEA3nALsDM1QogyvC0&index=17) of psychopaths/narcissists trying to manipulate humanity through fear and ignorance? If so, are they a manifestation of our collective shadow or ego? 
- Is it possible then, that collective [shadow work](https://www.youtube.com/watch?v=YgvrUi8BIWw), or ego-transcendence, is the most important effort humanity as a whole needs to face in order to evolve spiritually?
- Are there [credible witness testimonies](https://www.youtube.com/watch?v=AmNzkxVwAYg&list=PLnrEt2fIdZ0aBgPuVF0C_T559YR20eDTc) of UFO activity and deep state cover-up? If so, could the deep state and the military industrial complex have any interest in portraying them in the future as a treat to humanity to justify the militarization of space?
- What in the world is actually going on in [Hollywood](https://www.youtube.com/watch?v=TbNknirhUeA)? 

Your choice deciding the answer to such fundamental questions. I made mine a long time ago. My mind and heart is set free! 

[Main Guide](https://github.com/piccolomo/plotext#guide), [Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#notes)
